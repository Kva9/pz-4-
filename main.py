from PIL import Image, ImageDraw, ImageFont

img = Image.open('/home/KHPK.RU/student/Рабочий стол/kjkjkj.png')
img = Image.new('RGB', (400, 600), 'black')
font = ImageFont.truetype("arial.ttf", size=20)
idraw = ImageDraw.Draw(img)
idraw.text((145, 25), 'Приветствую вас', font=font)
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()

