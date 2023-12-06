import smtplib, json

def get_config(cwd):
    try:
        with open(f'{cwd}/config.ini', 'r') as file:
            config_json = file.read()
            config_json = json.loads(config_json)
            smtp_server = config_json["smtp_server"]
            smtp_port = config_json["smtp_port"]
            smtp_email = config_json["smtp_email"]
            smtp_username = config_json["smtp_username"]
            smtp_password = config_json["smtp_password"]
    except Exception as msg:
        print('[-] Failed to open config.ini..\n - be sure the file exists with the correct data')
        print(str(msg))
        return False, False
    try:
        server = smtp_login(smtp_server, smtp_port, smtp_username, smtp_password)
    except Exception as msg:
        print('[-] Failed to login with creds..\n - be sure the creds is valid')
        print(str(msg))
        return False, False

    return server, smtp_email

def smtp_login(smtp_server, smtp_port, smtp_username, smtp_password):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    return server


def send_message(server, sender_email, target, message, amount):
    for x in range(0, amount):
        print(f'[*] Sending message to {target}..')
        server.sendmail(sender_email, target, message)
    print("[!] Email(s) sent successfully!\n")
    server.quit()
