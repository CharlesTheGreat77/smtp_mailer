from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import pytesseract, requests, random
from io import BytesIO
from PIL import Image, ImageFilter, ImageEnhance

def get_carrier_from_carrierlookup(phone_number):
    with sync_playwright() as p:
        devices = p.devices
        rand_device = random.choice(list(devices.keys()))
        print(f'[*] Using device: {rand_device}')
        device = p.devices[rand_device]
        browser = p.webkit.launch(headless=False)
        context = browser.new_context(**device,)
        page = context.new_page()
        page.goto('https://currentcarrierlookup.com')
        page.wait_for_timeout(random.randint(1000,2000))
        html_content = page.content()
        soup = BeautifulSoup(html_content, 'html.parser')
        captcha = soup.select_one('form img.cimg')['src']
        get_captcha = requests.get(captcha)
        img = Image.open(BytesIO(get_captcha.content))
        img.convert('L')
        img = img.filter(ImageFilter.MedianFilter())
        enchancer = ImageEnhance.Contrast(img)
        img = enchancer.enhance(2)
        img.convert('1')
        img.save('temp.png')
        captcha_text = pytesseract.image_to_string(img, config='--oem 3 --psm 11 outputbase aplphanumeric')
        page.fill('#tn-tel', phone_number)
        page.wait_for_timeout(random.randint(1500,3000))
        page.fill("#bcap", captcha_text)
        page.wait_for_timeout(random.randint(1500,2500))
        page.click('input[value="check"]')
        page.wait_for_selector(".date-time span")
        carrier = page.text_content(".date-time span")
        sms_gateway = get_gateway_from_carrier(carrier)
        page.wait_for_timeout(random.randint(1500,2500))
        browser.close()

        return sms_gateway
    

def get_gateway_from_carrier(carrier):
    if 'Cingular Wireless/2' in carrier:
        sms_gateway = '@txt.att.net'
    elif 'Verizon Wireless:6006 - SVR/2' in carrier:
        sms_gateway = '@vtext.com'
    elif 'T-Mobile US-SVR-10X/2' in carrier:
        sms_gateway = '@tmomail.net'
    elif 'Metro PCS Communications Inc-SVR-10X/2' in carrier:
        sms_gateway = '@mymetropcs.com'
    
    return sms_gateway
