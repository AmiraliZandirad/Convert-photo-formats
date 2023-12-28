#▄▀█ █▀▄▀█ █ █▀█ ▄▀█ █░░ █ ▀█ ▄▀█ █▄░█ █▀▄ █
#█▀█ █░▀░█ █ █▀▄ █▀█ █▄▄ █ █▄ █▀█ █░▀█ █▄▀ █
#==========================================================
from PIL import Image

image = Image.open ('your Image name.format image').convert('RBG')

image.save('1.Custom image format to convert' , 'Custom image format to convert')