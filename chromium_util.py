import os
from datetime import datetime, timedelta

# Paths
USER_PATH = os.environ["USERPROFILE"]


CHROME_PATH = os.path.join(USER_PATH, "AppData", "Local",
    "Google", "Chrome", "User Data")
EDGE_PATH = os.path.join(USER_PATH, "AppData", "Local",
    "Microsoft", "Edge", "User Data")

# Works for Edge and Chrome
BROWSER_PATH = EDGE_PATH

DEFAULT_PATH = os.path.join(BROWSER_PATH, "default")
LOCAL_STATE_PATH = os.path.join(BROWSER_PATH, "Local State")

def get_chrome_datetime(chromedate):
    # chromedate is formatted as the number of microseconds since 01-01-1601
    if chromedate != 86400000000 and chromedate:
        date = datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
        return date
    return ""

