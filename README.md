# smtp_mailer
Send/Spam text messages with smtplib using python3 

# Prerequisites
```
python3
apt/brew install tor
apt/brew install tesseract
```

```
==========================================
| ,dP""8a "888888b,  d8b    "888b  ,888" |
| 88b   "  888  d88 dPY8b    88Y8b,8888  |
| `"Y8888a 888ad8P'dPaaY8b   88 Y88P888  |
| a,   Y88 888    dP    Y8b  88  YP 888  |
| `"8ad8P'a888a  a88a;*a888aa88a   a888a |
|                ;*;;;;*;;;*;;;*,,       |
|        _,---''6ooc,*;;;*;;;*;;*d;,     |
|     .-'      666o6o6o6oc,*;;*;dHH;     |
|   .' nhhn,.  6666o66oo6o6o6cMMMMMM`.   |
|  / nhhhhhhhn,66666666666o6oo6MMMMMW,\  |
| .,nhhhhhhhhnhY666666666666666MMMMWHP", |
| |nhhhhhhhnhMFjj,boY6666666666MMMWWHP | |
| ``hhhhhnhWFjjjjjbbbbbboY6666MMMWWHPf ' |
|  \ `mYHMFjjjjjjjjbbbbbbbbbboYHHPP"` /  |
|   `. ""ijjjjjjjjjmbbbbbbbbbbbbbo, ,'   |
|     `-._`iijjjjmMF`"bbbbb<=========.   |
|         `---..._______...|<[Hormel |   |  SMTP_MAILER/SPAMMER
|                          `========='   |
==========================================
```

# Setup
```
# Optional
python3 -m venv venv
source venv/bin/activate

# required
pip3 install -r requirements
apt install tor or brew install tor
```
- Configure your SMTP information in the config.ini file

# Usage

```
usage: main.py [-h] [-e EMAIL] [-p PHONE] [-f FROM_ADDRESS] [-s SUBJECT] -b BODY [-a AMOUNT]

Spoofing Emails/MMS with SMTPLIB

optional arguments:
  -h, --help            show this help message and exit
  -e EMAIL, --email EMAIL
                        target email address
  -p PHONE, --phone PHONE
                        target phone number [777-999-2222]
  -f FROM_ADDRESS, --from_address FROM_ADDRESS
                        from address [optional]
  -s SUBJECT, --subject SUBJECT
                        subject of the message
  -b BODY, --body BODY  body of the message
  -a AMOUNT, --amount AMOUNT
                        amount to send
```

