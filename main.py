from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
choose =int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))

bottom_text = ""
top_text = ""

if choose == 1:
    bottom_text = input("Введите нижний текст: ")
elif choose == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print('Перезагрузите программу')
    quit()

print(top_text, bottom_text)


memes = ["Кот в очках.png" , "Кот в ресторане.png", "кот_в_шоке.jpg", 'под_прикрытием.jpg' , 'сложный_выбор.jpg', 'тамара_в_недоумении.jpg','человек_на_могиле.jpg', 'человек_с_граблями.jpg']

print('Выбирите картинку для мема: ')
for i in range(len(memes)):
    print(i, memes[i])

image = Image.open(memes[int(input("Введите номер картинки: "))])
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0,0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill='black')

draw.text(((width - text[2]) / 2, (height - text[3] - 109)), bottom_text, font=font, fill='black')

image.save('new.mem.png')