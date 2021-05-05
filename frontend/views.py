from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from backend.forms import CommentForm
# from backend.forms import ReviewForm
# from backend.forms import FilterForm
from django.db.models import Count, Q



def index(request):
    music=Music.objects.all()
    songs=Songs.objects.all()
    about=About.objects.all()
    artiste=Artiste.objects.all()
    wizkid=Wizkid.objects.all()
    simi=Simi.objects.all()
    drake=Drake.objects.all()
    joefire=Joefire.objects.all()
    nicki=Nicki.objects.all()
    allmer=AllMar.objects.all()
    gyke=Gyke.objects.all()
    burna=Burna.objects.all()
    fire=Fire.objects.all()
    teni=Teni.objects.all()
    cuppy=Cuppy.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = 'MELODI'
        context = {
            'name':name,
            
            'phone':phone,
            'email':email,
            'message': message
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'GALAXY <ogunburebusayo.j@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                     'ogunburebusayo.j@gmail.com', email], html_message=html_message, fail_silently=True)
        if send:
            messages.success(request, 'Email sent, you will recieve an email shorthly!')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'frontend/index.html', {'mus': music, 'sng':songs, 'abt':about, 'art': artiste, 'wiz': wizkid,
    'sim':simi, 'dra':drake, 'jfb':joefire, 'nic':nicki, 'alm':allmer, 'gyk':gyke, 'bun':burna, 'foe':fire, 'ten':teni, 'cup':cuppy})


