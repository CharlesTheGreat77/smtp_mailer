import os
from core.smtp_server import get_config, send_message
from core.tor_setup import start_tor_proxy
from core.carrier_lookup import get_carrier_from_carrierlookup
from argparse import ArgumentParser

def compose_message(target, from_address, subject, message_body):
    # can spoof the from to whatever, but gmail may mark as spam..
    return f'From: {from_address}\nTo: {target}\nSubject: {subject}\n{message_body}'.encode()

    return message

def main(target, option, from_address, subject, message_body, amount):
    # establish tor connection
    tor_process = start_tor_proxy()
    # establish connection to server
    server, smtp_email = get_config(os.getcwd())
    if server != False:
        # if target is a phone #, get carrier and set it as <phone_number>@<sms_gateway>
        if option == 1:
            sms_gateway = get_carrier_from_carrierlookup(target)
            phone_number = target.split('-')
            target = ''.join(phone_number) + sms_gateway
        if from_address == None:
            from_address = smtp_email

        message = compose_message(target, from_address, subject, message_body)
        send_message(server, smtp_email, target, message, amount)
        
    tor_process.kill()

if __name__=='__main__':
    parser = ArgumentParser(description='Spoofing Emails/MMS with SMTPLIB')
    parser.add_argument('-e', '--email', help='target email address', required=False, type=str, default=None)
    parser.add_argument('-p', '--phone', help='target phone number', required=False, type=str, default=None)
    parser.add_argument('-f', '--from_address', help='from address [optional]', required=False, default=None, type=str)
    parser.add_argument('-s', '--subject', help='subject of the message', required=False, type=str)
    parser.add_argument('-b', '--body', help='body of the message', required=True, type=str)
    parser.add_argument('-a', '--amount', help='amount to send', default=1, type=int)

    args = parser.parse_args()
    email_address = args.email
    phone_number = args.phone
    from_address = args.from_address
    subject = args.subject
    message_body = args.body
    amount = args.amount

    if email_address != None or phone_number != None:
        if email_address != None:
            target = email_address
            option = 0
        else:
            target = phone_number
            option = 1

        main(target, option, from_address, subject, message_body, amount)
    else:
        print(parser.usage)
