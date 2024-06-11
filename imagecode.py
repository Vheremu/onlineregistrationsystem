import os
from PIL import Image, ImageDraw,ImageFont
fontsfolder='C:\Windows\Fonts'
tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), 70)
impactFont = ImageFont.truetype(os.path.join(fontsfolder, 'impact.ttf'), 90)
sitkaFont = ImageFont.truetype(os.path.join(fontsfolder, 'Sitka.ttc'), 70)

def printpromo(image):
    im1=Image.open(image)
    width,height=im1.size
    fontsfolder='C:\Windows\Fonts'
    tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), width*0.06)
    
    print(width)
    print(height)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((width*0.625, height*0.35, width*1,height*0.5), fill='red')
    draw1.text((width*0.63, height*0.36), 'Get 10% Off', fill='blue', font=tahomaFont,fontsize=width*0.03)
    draw1.text((width*0.63, height*0.39), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((width*0.63, height*0.43), 'Your Code', fill='green', font=tahomaFont)
    draw1.text((width*0.63, height*0.47), 'Here!', fill='yellow', font=tahomaFont)
    im1.save('static/adds/promo.png')
   
    return im1
def printpromocode(image,promocode):
    im1=Image.open(image)
    width,height=im1.size
    fontsfolder='C:\Windows\Fonts'
    tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), width*0.06)
    
    print(width)
    print(height)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((width*0.625, height*0.35, width*1,height*0.5), fill='red')
    draw1.text((width*0.63, height*0.36), 'Get 10% Off', fill='blue', font=tahomaFont,fontsize=width*0.03)
    draw1.text((width*0.63, height*0.39), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((width*0.63, height*0.43), promocode, fill='green', font=tahomaFont)
    draw1.text((width*0.63, height*0.47), 'Now!', fill='yellow', font=tahomaFont)
    im1.save('static/adds/promocode.png')
   
    return im1
def a1(firstname,surname,invitee,inviteesurname,token):
    im1=Image.open('m3.png')
    width,height=im1.size
    print(width,height)
    draw1 = ImageDraw.Draw(im1)
    draw1.text((150, 100), 'Invitation Letter', fill='black', font=impactFont)
    draw1.text((1240, 300), firstname+' '+surname, fill='black', font=tahomaFont)
    draw1.text((1240,375 ), 'Associate', fill='black', font=tahomaFont)
    draw1.text((1240, 450), 'Aaron  Affiliate Program', fill='black', font=tahomaFont)
    draw1.text((1240, 525), 'Aaron Boarding School', fill='black', font=tahomaFont)
    draw1.text((1240, 600), 'Farm 49 Nyakapupu ,Guruve', fill='black', font=tahomaFont)
    
    verdanabFont = ImageFont.truetype(os.path.join(fontsfolder, 'verdanab.ttf'), 50)
    draw1.text((1240, 725), 'n/a', fill='black', font=verdanabFont)
    draw1.text((150, 825), 'Dear '+invitee+' '+inviteesurname, fill='black', font=sitkaFont)
    draw1.text((150, 950), 'Ref : Invitation for membership with Aaron Affiliate Program.', fill='black', font=tahomaFont)
    draw1.text((150, 1100), 'You are invited by '+firstname+' for membership with Aaron Affiliate Program.You ', fill='black', font=verdanabFont)
    draw1.text((150, 1150), 'have been invited as a '+'Associate'+', the number '+'2'+' highest', fill='black', font=verdanabFont)
    draw1.text((150,1200), 'rank from the Manager who is number 1 rank. Your rank comes with all the  ', fill='black', font=verdanabFont)
    draw1.text((150, 1250), 'benefits of being a '+'Associate'+' with Aaron Affiliate Program.', fill='black', font=verdanabFont)
    draw1.text((150, 1350), 'To begin as '+'Associate'+', you have been given token '+token+'.', fill='black', font=verdanabFont)
    draw1.text((150, 1400), 'You have to register for a free account on our website  ', fill='black', font=verdanabFont)
    draw1.text((150, 1450), 'at www.aaronboardingschool.co.zw. Entering your invitation token ', fill='black', font=verdanabFont)
    draw1.text((150, 1500), 'while registering will allow you to register for free whereas not ', fill='black', font=verdanabFont)
    draw1.text((150, 1550), 'registering with an invitation requires a payment of $1 fee for', fill='black', font=verdanabFont)
    draw1.text((150, 1600), 'registration to our affiliate marketing program. ', fill='black', font=verdanabFont)
    draw1.text((150, 1700), 'We provide affiliate marketers with the high quality marketing ', fill='black', font=verdanabFont)
    draw1.text((150, 1750), 'materials that allow then to instantly begin marketing campaigns ', fill='black', font=verdanabFont)
    draw1.text((150, 1800), 'and make money through our commision based affiliate marketing program.', fill='black', font=verdanabFont)
    draw1.text((150, 1850), 'Marketer will provide value for their potential clients by offering a ', fill='black', font=verdanabFont)
    draw1.text((150, 1900), 'discounted registestration to the school thereby saving money for their clients. ', fill='black', font=verdanabFont)
    draw1.text((150, 2000), 'Affiliate marketer in the Aaron Boarding School Affiliate Program ', fill='black', font=verdanabFont)
    draw1.text((150, 2050), 'are payed on commision from their registrations as well as commisions coming ', fill='black', font=verdanabFont)
    draw1.text((150, 2100), 'from registrations from marketers who joined the program through them. ', fill='black', font=verdanabFont)
   
    draw1.text((150, 2150), 'Marketers make money by helping potencial clients to register for school ', fill='black', font=verdanabFont)

    draw1.text((150, 2200), 'at Aaron Boarding School Through our online registration system. For every', fill='black', font=verdanabFont)
    
    draw1.text((150, 2250), 'student registered our marketers make $10 and they can invite other  ', fill='black', font=verdanabFont)
   
    draw1.text((150, 2300), 'marketers to profit from the program too. ', fill='black', font=verdanabFont)
  
    draw1.text((150, 2400), 'Your Faithfully', fill='black', font=verdanabFont)
    
    draw1.text((150, 2600), 'Associate'+', Aaron Affiliate Program. ', fill='black', font=verdanabFont)
    
    draw1.text((150, 2500), firstname+' '+surname, fill='black', font=verdanabFont)
    draw1.text((120, 3000), 'Invitation Code: '+token, fill='black', font=impactFont)
    draw1.text((120, 3100), 'Website Link:www.aaronboardingschool.co.zw ', fill='black', font=impactFont)
    
    im1.save('m4.png')
    return im1

