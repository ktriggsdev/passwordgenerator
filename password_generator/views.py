import random
import string

from django.shortcuts import render


def gen_password(request):
    if request.method == "POST":
        passlen = request.POST.get('passlen')
        if passlen:
            s1 = string.ascii_uppercase
            s2 = string.ascii_lowercase
            s3 = string.digits
            s4 = string.punctuation

            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))

            random.shuffle(s)
            pas = ("".join(s[0:int(passlen)]))
            return render(request, 'password_generator/gen_password.html', {'password': pas})

    return render(request, 'password_generator/gen_password.html')
