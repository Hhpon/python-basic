import random
import string
from PIL import Image
from claptcha import Claptcha

def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    return "".join(rndLetters)

# Initialize Claptcha object with random text, FreeMono as font, of size
# 100x30px, using bicubic resampling filter and adding a bit of white noise
c = Claptcha(randomString, "FreeMonospaced-7ZXP.ttf", (100,30),
             resample=Image.BICUBIC, noise=0.3)

text, _ = c.write('captcha1.png')
print(text)  # 'PZTBXB', string printed into captcha1.png

text, _ = c.write('captcha2.png')
print(text)  # 'NEDKEM', string printed into captcha2.png

# Change images' size to 150x90 and estimated margin to 25x25
c.size = (150,90)
c.margin = (25,25)

text, _ = c.write('captcha3.png')
print(text)  # 'XCQYVS', captcha3.png has different dimentions than
             # captcha1.png and captcha2.png