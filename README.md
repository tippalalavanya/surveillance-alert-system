
# 🔐 Surveillance Alert System

An intelligent, real-time facial recognition system that enhances home or facility security by detecting intruders and instantly alerting the owner via email. This lightweight and modular solution leverages computer vision, facial recognition, and SMTP-based alerts, making it ideal for Raspberry Pi and similar low-power devices.

---

## 🧠 System Architecture

```mermaid
graph TD
    A[Live Webcam] --> B(Face Detection);
    B --> C(Face Recognition);
    C --> D{Compare with Known Faces};
    D -- Yes --> E[Access Granted];
    D -- No --> F[Intruder Detected];
    F --> G[Capture + Save Image];
    F --> H[Send Email Notification];
````

-----

## 🚀 Key Features

  - 🎥 **Real-Time Video Monitoring**: Captures live feed from webcam or Pi camera.
  - 🧠 **Facial Recognition**: Identifies individuals using the `face_recognition` deep learning model.
  - 📧 **Instant Email Alerts**: Notifies the owner with a photo of the intruder.
  - 📁 **Intruder Image Logging**: Stores unrecognized faces for investigation.
  - ⚙️ **Configurable Parameters**: Alert interval, confidence threshold, and email credentials.
  - 💡 **Raspberry Pi Compatible**: Lightweight and optimized for edge deployment.

-----

## 🛠 Tech Stack

| Category        | Technologies                        |
| :-------------- | :---------------------------------- |
| Language        | Python 3.x                          |
| Computer Vision | OpenCV, face\_recognition            |
| Notifications   | SMTP (smtplib) for Email Alerts     |
| Hardware        | Webcam / Raspberry Pi Camera Module |

-----

## 📁 Folder Structure

```
surveillance-alert-system/
├── known_faces/         # Pre-labeled known face images
├── captured_intruders/  # Stores intruder images
├── alert.py      # Main program logic
├── config.py            # Email settings and system config
└── README.md            # Documentation
```

-----

## ⚙️ Configuration

Edit `config.py`:

```python
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"  # Use Gmail app-specific password
RECEIVER_EMAIL = "owner@example.com"

KNOWN_FACES_DIR = "known_faces"
ALERT_INTERVAL = 60  # Minimum seconds between alerts
MATCH_THRESHOLD = 0.6  # Face recognition confidence threshold
```

**🔐 Security Note**: Do not commit `config.py` to public repositories.

-----

## 📦 Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/tippalalavanya/surveillance-alert-system.git](https://github.com/tippalalavanya/surveillance-alert-system.git)
    cd surveillance-alert-system
    ```

2.  **Install Dependencies**

    ```bash
    pip install opencv-python face_recognition
    ```

3.  **Add Known Faces**

    Place clear, frontal face images in the `known_faces/` directory. Name the files based on the person (e.g., `john.jpg`, `lavanya.png`).

4.  **Run the Program**

    ```bash
    python alert.py
    ```

-----

## 📬 Email Alert Workflow

Face detected → Compared with known faces.

If match fails:

  * Capture and save intruder's image.
  * Send alert email with photo attached.
  * Enforce cooldown (e.g., 60 seconds) before next alert.

### ✅ Sample Output

**Console logs:**

```
[INFO] Found: Unknown Person
[ALERT] Email sent to owner with intruder image.
```

**Email:**

```
Subject: Intruder Detected!
Body: An unknown face was detected at your premises. Please see the attached image.
```

-----

## 🧑‍💻 Future Enhancements

  * 📱 SMS/WhatsApp alerts using Twilio or pywhatkit.
  * 🌐 Web-based dashboard with intruder logs.
  * ☁️ Cloud storage integration for remote monitoring.
  * 🔊 Buzzer or audio alert on detection.

-----

## 🙌 Contributors

  * Tippala Lavanya – Developer & ML Integrator

Feel free to contribute via pull requests or open issues.

-----



-----


-----

## 🔗 Repository

GitHub: [Surveillance Alert System](https://github.com/tippalalavanya/surveillance-alert-system)

