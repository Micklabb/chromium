import json
import os
from chromium_util import DEFAULT_PATH

def main():
    db_name = "Preferences"
    db_path = os.path.join(DEFAULT_PATH, db_name)

    with open(db_path) as f:
        settings = json.load(f)
        print(settings["sync"])

    # Interesting fields:
    # sync: current profile info, birthday etc.
    # translate_allowlists: good chance user reads in this language
    # account_info: speaks for itself
    # browser: window sizes
    # countryid_at_install: country id
    # language_model_counters: histogram encountered languages
    # sessions: times opened chrome and amount of tabs

if __name__ == "__main__":
    main()
