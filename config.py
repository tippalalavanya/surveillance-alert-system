# ------------------ SENSITIVE DATA ------------------
# Store your email credentials and configuration here.
# IMPORTANT: This file is listed in .gitignore and will NOT be uploaded to GitHub.
# ----------------------------------------------------

# -- Email Configuration --
# For Gmail, you must generate an "App Password".
# 1. Go to your Google Account -> Security -> 2-Step Verification (must be ON).
# 2. Go to App Passwords, generate a new password for "Mail" on "Other".
# 3. Use that 16-character password here.
SENDER_EMAIL = "tippalalavanya05@gmail.com"
SENDER_PASSWORD = "Lavanya123060520"
RECEIVER_EMAIL = "renukalavanya98175@example.com"

# -- System Configuration --
KNOWN_FACES_DIR = "known_faces"
COOLDOWN_PERIOD = 300 # Time in seconds (e.g., 300 = 5 minutes) to wait before resending an alert for the same person.
MODEL_TOLERANCE = 0.6 # How strict the face comparison is. Lower is more strict. 0.6 is a good default.
