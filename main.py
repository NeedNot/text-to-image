from PIL import Image, ImageDraw, ImageFont
import os


#dice
dice = input("Dice total:")

#color
color = input("Color:")

#card
card = input("Card:")

#number
number = input("Number:")

#battery
battery = input("Battery:")

#page
page = "Dice total:\n" + dice + "\n\n" + "Color:\n" + color +"\n\n" + "Card:\n" + card +"\n\n" + "Number:\n" + number +"\n\n" + "Battery:\n" + battery +"\n\n"

# name of the file to save
filename = "image.jpeg"
fnt = ImageFont.truetype('arial.ttf', 12)

# create new image
image = Image.new(mode = "RGB", size = (497,275), color = "white")
draw = ImageDraw.Draw(image)
draw.text((2,10), page, font=fnt, fill=(0,0,0))
image.save(filename)

# save the file
image.save(filename)


os.system("git add .")
os.system('git commit -m "image.jpeg"')
os.system("git push origin master")
