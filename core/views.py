from django.shortcuts import render

# Create your views here.
import random
import string

import re 
  
# Make a regular expression 
# for validating an Email 
regex_em = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
regex_ph = '\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}'      

def _genref(length):
    letters = string.hexdigits
    return ''.join(random.choice(letters) for i in range(length))

def check_email(email):
    return re.search(regex_em,email)

def check_phone(phone):
    return re.search(regex_ph,phone)    