from django.shortcuts import render

# Create your views here.
from core.models import City,Country,AppPermission
from users.models import  User,Profile,Admin,Manager,Seller
from chat.models import ChatRoom

         

async def create_countries():
    try:
        Countries=[
            {1:"Moroco"},{2:"France"},{3:"USA"}]
        for c in Countries:
            print(c[1])
            count= await  Country(label=c[1])
            count.save()
            print(c)
      
    except :
        print('error country')
async def create_cities():
    print('im working')
    try:
        cities=[
        {"Moroco":"marrakech"},
        {"Moreco":"casa blanca"},
        {"France":"parise"},
        {"france":"lion"},
        {"USA":"amsterdam"},
        {"USA":"new york"}
        ]
        for ct in cities:
            city = await City.objects.create(country=ct[0],label=ct[1]) 
        print('fin')    
    except :
        print('error city')

def create_admin():
    try:
        us=Country.objects.create(label='USA')
        fr=Country.objects.create(label='France')
        mr=Country.objects.create(label='Moroco')
        marra = City.objects.create(coutry=mr,label="marrakech") 
        agadir= City.objects.create(coutry=mr,label="agadir") 
        casa= City.objects.create(coutry=mr,label="casa blanca") 
        adper=AppPermission.objects.create(label="admin")
        manper=AppPermission.objects.create(label="manager")
        sellerper=AppPermission.objects.create(label="seller")
#admin        
        pamd= Profile.objects.create(fname="ayoub",city=marra,country=mr,lname="sadi",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613676495/uwggzp7nkoqzo8qr1if4.jpg")
        User.objects.create(user_permission=adper,is_superuser=True,prof=prad,username="Admin",password="Azer1234")
#manager1 1
        pm1= Profile.objects.create(fname="hameza",city=casa,country=mr,lname="sabib",phone="0624567547",email="sabib1999@gmail.com",code_bank="124683321435674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613159789/jmms6mzngfehlj2g9tmd.png")
        chate_rm1=ChatRoom.objects.create(room_name=f'Mr-{pm1.fname}-{pm1.lname}-room')
        User.objects.create(user_permission=manper,prof=pm1,chat_room=chate_rm1,username="manager1",password="manager1")
#manager2

        Pm2= Profile.objects.create(fname="abdo",city=agadir,country=mr,lname="monir",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613159753/vriab4wdgrngyxcx5rn8.jpg")
        chate_rm2=ChatRoom.objects.create(room_name=f'Mr-{pm2.fname}-{pm2.lname}-room')
        User.objects.create(user_permission=manper,prof=Pm2,chat_room=chate_rm2,username="manager2",password="manager2")


        pr= Profile.objects.create(fname="ayoub",city=marra,country=mr,lname="sadi",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613676495/uwggzp7nkoqzo8qr1if4.jpg")
        prad= Profile.objects.create(fname="ayoub",city=marra,country=mr,lname="sadi",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613676495/uwggzp7nkoqzo8qr1if4.jpg")
        prad= Profile.objects.create(fname="ayoub",city=marra,country=mr,lname="sadi",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613676495/uwggzp7nkoqzo8qr1if4.jpg")
        us=User.objects.create(user_permission=adper,prof=prad)
        
        us.save()
        print('rrr')
        ad=Admin(us)
        ad.save()
        print('fin')
    except :
        print('errrr admin')    