import os
from asyncore import read
import mimetypes
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import text_to_speech_Data
from gtts import gTTS

from audiohelper import settings

def download_file(request, fileName):
    # fill these variables with real values
    fl_path = settings.MEDIA_ROOT + "/"
    filename = fileName
    file = fl_path + filename
    fl = open(file, 'rb')
    mime_type, _ = mimetypes.guess_type(file)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Имя пользователя или пароль введены неверно')
    context = {}
    return render(request, 'login.html', context)


def regist(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        name = request.POST.get('name')
        myobj = gTTS(text=text, lang='ru', slow=False)

        addAudioToDB(myobj, name, request)
        return redirect('index')
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')


def cabinetPage(request):
    all_audio = text_to_speech_Data.objects.filter(user = request.user)
    return render(request, 'cabinetPage.html', {'audio_list':all_audio})


def addAudioToDB (obj, name, req):
    f_name = name + "_" +  req.user.username + ".mp3"
    full_fn = settings.MEDIA_ROOT +  "/" + name + "_" +  req.user.username + ".mp3"
    audio = text_to_speech_Data(audio_name=f_name, user=req.user)
    audio.save()
    obj.save(full_fn)




