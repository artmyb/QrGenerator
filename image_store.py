import base64

with open('qr_icon.png', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

with open('main_icon.py', 'w') as file:
    file.write(f'image_data = """{encoded_string}"""')