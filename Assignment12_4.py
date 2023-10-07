import os
from sys import *
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def create_process_log(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    log_file_path = os.path.join(directory, "process_log.txt")

    with open(log_file_path, "w") as log_file:
        log_file.write("Process Information:\n\n")

        for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
            try:
                process_info = process.info
                pid = process_info['pid']
                name = process_info['name']
                username = process_info['username']

                log_file.write(f"Process Name: {name}\n")
                log_file.write(f"PID: {pid}\n")
                log_file.write(f"Username: {username}\n")
                log_file.write("-" * 40 + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    return log_file_path

def send_email(email, password, to_email, log_file_path):
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_email
    msg['Subject'] = "Process Log"

    text = "Please find the attached process log file."
    msg.attach(MIMEText(text, 'plain'))

    with open(log_file_path, "rb") as log_file:
        attachment = MIMEApplication(log_file.read(), _subtype="txt")
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_file_path))
        msg.attach(attachment)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")

def main():
    print("Application name:",argv[0])
    
    if len(argv)!=2:
        print("Invalid number of Arguments:")
        exit()
        
    if argv[1] == "-h" or argv[1] == "-H":
        print("Application for showing running process ")
        exit()

    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: processInfo.py Notepad")
        exit()
        
    email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    to_email = input("Enter the recipient's email address: ")

    log_file_path = create_process_log(argv[1])
    send_email(email, password, to_email, log_file_path)

if __name__ == "__main__":
    main()
