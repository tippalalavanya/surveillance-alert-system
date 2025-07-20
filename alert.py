import face_recognition
import cv2
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time

# --- 1. Import Configuration from config.py ---
try:
    from config import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL, KNOWN_FACES_DIR, COOLDOWN_PERIOD, MODEL_TOLERANCE
except ImportError:
    print("Error: Could not import from config.py.")
    print("Please make sure you have created a config.py file with all the required variables.")
    exit()

# --- 2. Function to Send Email Alert ---
def send_alert_email(person_name, frame):
    """Connects to the SMTP server and sends an email with an image attachment."""
    print(f"Attempting to send alert email for {person_name}...")
    try:
        # Encode the image frame to JPG format in memory
        _, image_data = cv2.imencode('.jpg', frame)
        
        # Create the email message object
        msg = MIMEMultipart()
        msg['Subject'] = f"SURVEILLANCE ALERT: {person_name} Detected"
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        # Attach the text part of the email
        text_body = MIMEText(f"The surveillance system has identified a potential threat: {person_name} at {time.ctime()}.")
        msg.attach(text_body)
        
        # Attach the image part of the email
        image_attachment = MIMEImage(image_data.tobytes(), name=f"{person_name}_{time.time()}.jpg")
        msg.attach(image_attachment)
        
        # Connect to Gmail's SMTP server over SSL and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        
        print(f"✅ Alert email sent successfully for {person_name}!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

# --- 3. Load Known Face Encodings from the Directory ---
def load_known_faces(directory):
    """Loads face encodings and names from the known_faces directory."""
    print("Loading known faces...")
    known_encodings = []
    known_names = []
    
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' was not found.")
        return [], []

    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(directory, filename)
            # Use the filename (without extension) as the person's name
            person_name = os.path.splitext(filename)[0].replace("_", " ").title()
            
            try:
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                
                if encodings:
                    known_encodings.append(encodings[0])
                    known_names.append(person_name)
                    print(f"  - Loaded face for {person_name}")
                else:
                    print(f"  - Warning: No face found in {filename}. Skipping.")
            except Exception as e:
                print(f"  - Error loading {filename}: {e}")

    print(f"✅ Loaded {len(known_names)} known faces.")
    return known_encodings, known_names

# --- 4. Main Surveillance Application Logic ---
def run_surveillance():
    known_face_encodings, known_face_names = load_known_faces(KNOWN_FACES_DIR)

    if not known_face_encodings:
        print("No known faces were loaded. Please add images to the 'known_faces' directory.")
        return

    # Dictionary to track the last time an alert was sent for each person
    last_alert_times = {name: 0 for name in known_face_names}

    # Initialize video capture (0 is usually the default webcam/camera module)
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open video source.")
        return

    print("\n--- Starting Surveillance System ---")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame from camera. Exiting.")
            break

        # Find all face locations and create encodings for them
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=MODEL_TOLERANCE)
            
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                
                current_time = time.time()
                # Check if the cooldown period has passed for this specific person
                if current_time - last_alert_times.get(name, 0) > COOLDOWN_PERIOD:
                    print(f"🚨 THREAT DETECTED: {name}")
                    send_alert_email(name, frame.copy()) # Send a copy of the frame
                    last_alert_times[name] = current_time # Update the last alert time
                else:
                    # This message is for debugging; can be removed for cleaner output
                    print(f"Detected {name} again, but still in cooldown period.")

    # --- 5. Cleanup ---
    video_capture.release()
    print("--- Surveillance System Stopped ---")

if __name__ == "__main__":
    run_surveillance()
