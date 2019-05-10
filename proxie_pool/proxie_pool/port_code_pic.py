from PIL import Image
import pytesseract
import requests
def code_text(cookie, url_list):
    port_list = []
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files/Tesseract-OCR/tesseract.exe'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie': cookie['proxy_token']
    }
    for url in url_list:
        response = requests.get(url=url, headers=headers)
        with open('code.png', 'wb') as f:
            f.write(response.content)
        image = Image.open('code.png')
        img = image.convert('P')

        threshold = 2

        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        # 图片二值化
        photo = img.point(table, '1')
        # photo.save('1_1.png')
        text = pytesseract.image_to_string(photo)
        port_list.append(text)
    return port_list

