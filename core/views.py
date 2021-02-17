from django.shortcuts import render

# Create your views here.
import random
import string


def _genref(length):
    letters = string.hexdigits
    return ''.join(random.choice(letters) for i in length)