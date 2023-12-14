import smtplib
import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.hepsiburada.com/dji-mini-4-pro-dji-rc-2-ekranli-kumandali-pm-HBC00005AJFMB'

headers = {
    'User-Agent': 'xxx'
}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Ürün adı
    title = soup.find(id='product-name').get_text().strip()
    print("Ürün Adı:", title)

    # Fiyat bilgisi
    price_span = soup.find('span', {'data-bind': "markupText:'currentPriceBeforePoint'"})
    price_str = price_span.get_text() if price_span else "Fiyat bilgisi bulunamadı."
    price = float(price_str.replace('.', '').replace(',', '.'))  # Fiyatı sayıya dönüştür

    print("Fiyat:", price)
    if price < 78500:  # Fiyatı karşılaştır
        send_mail(title)


def send_mail(product_title):
    sender = 'erdemerzurumlu@gmail.com'
    receiver = 'erdemeruzrumlu@gmail.com'
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, 'xxx')
        subject = product_title.encode('utf-8') + b" istedigin fiyatta"  # Başlığı UTF-8 formatına dönüştür
        server.sendmail(sender, receiver, subject)
        print('Mail gönderimi Başarılı')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()


while True:
    check_price()
    time.sleep(60 * 60)
