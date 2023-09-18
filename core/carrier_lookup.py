from bs4 import BeautifulSoup
from playwright_stealth import stealth_sync
from playwright.sync_api import sync_playwright
import re


def get_carrier_from_spydialer(phone_number):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        context = browser.new_context()
        page = context.new_page()
        stealth_sync(page)
        page.goto('https://spydialer.com')
        page.fill('input#SearchTextBox', phone_number)
        page.click('input[value="Search"]')
        print("[*] Waiting for 6 seconds for spydialer search button to load")
        page.wait_for_timeout(6000)
        page.click('input[value="Search"]')
        print('[*] Waiting 10 seconds for other spydialer search button to load\n')
        page.wait_for_timeout(10000)
        html_content = page.content()
        browser.close()
        sms_gateway = get_carrier_from_html(html_content)

        return sms_gateway
    

def get_carrier_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    #name_element = soup.find('a', id='ctl00_ContentPlaceHolder1_NameLinkButton')
    #name = name_element.text if name_element else None
    message_element = soup.find('span', id='ctl00_ContentPlaceHolder1_DataMessageLabel')
    message = message_element.text if message_element else None
    carrier = re.findall(r'\b[A-Z]+(?:\W+[A-Z]+)*', message)
    provider = carrier[1].split()

    if 'AT&T' in provider[0]:
        carrier = '@mms.att.net'
    elif 'METROPCS' in provider[0]:
        carrier = '@mymetropcs.com' 
    elif 'TMOBILE' in provider[0]:
        carrier = '@tmomail.net'
    elif 'SPRINTPCS' in provider[0]:
        carrier = '@pm.sprint.com'
    elif 'VERIZON' in provider[0]:
        carrier = '@vzwpix.com'
    elif 'CRICKET' in provider[0]:
        carrier = '@mms.cricketwireless.net'
    elif 'US' in provider:
        carrier = '@mms.uscc.net'
    else:
        carrier = '@tmomail.net'

    return carrier