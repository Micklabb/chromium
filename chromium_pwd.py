import json
import base64
import win32crypt
from Crypto.Cipher import AES
from chromium_db import ChromeDB
from chromium_util import get_chrome_datetime, LOCAL_STATE_PATH

def get_encryption_key():
    with open(LOCAL_STATE_PATH) as f:
        local_state = json.load(f)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

    # remove DPAPI str
    key = key[5:]

    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]

        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)

        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""

def main():
    db_name = "Login Data"
    with ChromeDB(db_name) as db:

        # get the AES key
        key = get_encryption_key()

        interesting_fields = [
            "origin_url",
            "action_url",
            "username_value",
            "password_value",
            "date_created",
            "date_last_used"
        ]
    
        db.cursor.execute(f"SELECT {', '.join(interesting_fields)} FROM logins ORDER BY date_created")

        accounts = [list(i) for i in db.cursor.fetchall()]
        for account in accounts:
            account[3] = decrypt_password(account[3], key)
            account[4] = str(get_chrome_datetime(account[4]))
            account[5] = str(get_chrome_datetime(account[5]))
            print(account)


if __name__ == "__main__":
    main()