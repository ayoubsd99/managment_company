from django.shortcuts import render

# Create your views here.
from core.models import City,Country,AppPermission
from users.models import  User,Profile,Admin,Manager,Seller

         

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
        p= Profile(fname="ayoub",lname="sadi",phone="0620166547",email="sadiayoub21@gmail.com",code_bank="124683668635674",miniature="https://res.cloudinary.com/dgjvthpnh/image/upload/v1613159789/jmms6mzngfehlj2g9tmd.png")
        p.save()
        permis = AppPermission(label="admin")
        permis.save()

        us = User(user_permission=permis,prof=p)
        us.save()
        print('rrr')
        ad=Admin(us)
        ad.save()
        print('fin')
    except :
        print('errrr admin')    