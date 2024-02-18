from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as lg, logout as lout

from .models import *
from .forms import *

def index(request):
    if request.user.is_authenticated:
        login = request.user.name + ' ' + request.user.surname
    else:
        login = ''
    return render(request, "index.html", {'login': login})

def register(request):

    if request.method == "POST":
        try:
            form = RegisterForm(request.POST)
            if form.is_valid():

                email = form['email'].value()
                name = form['name'].value()
                surname = form['surname'].value()
                password = form['password'].value()

                group = User(email=email, name=name, surname=surname, password=password, username=email)
                group.save()
                return redirect('/app/')
        except Exception as e:
            return HttpResponse(f"<h1>{e}</h1>")
    else:
        form = RegisterForm()
        return render(request, "add.html", {'form': form, 'btn_name': 'Register', 'path': ''})

def login(request):
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        if form.is_valid():

            email = form['email'].value()
            password = form['password'].value()

            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    lg(request, user)
                    return redirect('/app/')
                else:
                    return HttpResponse('Disabled account')
        return redirect('/app/')
        
    else:
        form = LoginForm()
        return render(request, "add.html", {'form': form, 'btn_name': 'Login', 'path': ''})

def logout(request):
    lout(request)
    return redirect('/app/')

def table(request, path):
        products = []

        match path:

            case 'users':
                out = User.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.email,
                        product.name,
                        product.surname,
                        product.password,
                        product.function
                    ))
                names = ['id', 'email', 'name', 'surname', 'password', 'function', '']

            case 'affiliates':
                out = Affiliate.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.adress,
                        product.country
                    ))
                names = ['id', 'adress', 'country', '']
            
            case 'offices':
                out = Office.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.affiliate.id,
                        product.room_num,
                        product.city,
                    ))
                names = ['id', 'affiliate_id', 'room_num', 'city', '']
            
            case 'rooms':
                out = Room.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.office.id,
                        product.storey,
                    ))
                names = ['id', 'office_id', 'storey', '']

            case 'history_moves':
                out = History_move.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.date_time,
                        product.status_workplace,
                        product.room.id,
                        product.worker.id,
                    ))
                names = ['id', 'date_time', 'status_workplace', 'room_id', 'worker_id', '']
            
            case 'workers_rooms':
                out = Worker_room.objects.all()
                for product in out:
                    products.append((
                        product.id,
                        product.room.id,
                        product.worker.id,
                    ))
                names = ['id', 'room_id', 'worker_id', '']

        return render(request, "table.html", {'products': products, 'names': names, 'path': path})

def create(request, path):
    if request.method == "POST":
        try:
            match path:

                case 'users':
                    form = UserForm(request.POST)
                    if form.is_valid():

                        name = form['name'].value()
                        surname = form['surname'].value()
                        function = form['function'].value()
                        email = form['email'].value()
                        password = form['password'].value()

                        user = User(name=name, surname=surname, function=function, email=email, password=password, 
                         username=email)
                        user.save()

                case 'affiliates':
                    form = AffiliateForm(request.POST)
                    if form.is_valid():

                        adress = form['adress'].value()
                        country = form['country'].value()

                        affiliate = Affiliate(adress=adress, country=country)
                        affiliate.save()

                case 'offices':
                    form = OfficeForm(request.POST)
                    if form.is_valid():

                        affiliate_id = form['affiliate_id'].value()
                        room_num = form['room_num'].value()
                        city = form['city'].value()

                        affiliate = Affiliate.objects.get(id=affiliate_id)
                        
                        post = Office(affiliate=affiliate, room_num=room_num, city=city)
                        post.save()

                case 'rooms':
                    form = RoomForm(request.POST)
                    if form.is_valid():

                        office_id = form['office_id'].value()
                        storey = form['storey'].value()

                        office = Office.objects.get(id=office_id)
                        
                        comm = Room(office=office, storey=storey)
                        comm.save()

                case 'history_moves':
                    form = History_moveForm(request.POST)
                    if form.is_valid():

                        status_workplace = form['status_workplace'].value()
                        room_id = form['room_id'].value()
                        worker_id = form['worker_id'].value()

                        room = Room.objects.get(id=room_id)
                        worker = User.objects.get(id=worker_id)

                        
                        emoji = History_move(status_workplace=status_workplace, room=room, worker=worker)
                        emoji.save()

                case 'workers_rooms':
                    form = Worker_roomForm(request.POST)
                    if form.is_valid():

                        room_id = form['room_id'].value()
                        worker_id = form['worker_id'].value()

                        room = Room.objects.get(id=room_id)
                        worker = User.objects.get(id=worker_id)
                        
                        post_emoji = Worker_room(room=room, worker=worker)
                        post_emoji.save()

            return redirect('/app/' + path)
        except Exception as e:
            return HttpResponse(f"<h1>{e}</h1>")
    else:
        match path:
            case 'users':
                form = UserForm()
            case 'affiliates':
                form = AffiliateForm()
            case 'offices':
                form = OfficeForm()
            case 'rooms':
                form = RoomForm()
            case 'history_moves':
                form = History_moveForm()
            case 'workers_rooms':
                form = Worker_roomForm()
        return render(request, "add.html", {'form': form, 'btn_name': 'Create', 'path': path})

def update(request, path, id):
    if request.method == "POST":
        try:
            match path:
                case 'users':
                    form = UserForm(request.POST)
                    if form.is_valid():

                        name = form['name'].value()
                        surname = form['surname'].value()
                        function = form['function'].value()

                        User.objects.filter(id=id).update(name=name, surname=surname, fumction=fumction)
                case 'affiliates':
                    form = AffiliateForm(request.POST)
                    if form.is_valid():

                        adress = form['adress'].value()
                        country = form['country'].value()

                        Affiliate.objects.filter(id=id).update(adress=adress, country=country)
                case 'offices':
                    form = OfficeForm(request.POST)
                    if form.is_valid():

                        affiliate_id = form['affiliate_id'].value()
                        room_num = form['room_num'].value()
                        city = form['city'].value()

                        affiliate = Affiliate.objects.get(id=affiliate_id)

                        Office.objects.filter(id=id).update(affiliate=affiliate, room_num=room_num, city=city)
                case 'rooms':
                    form = RoomForm(request.POST)
                    if form.is_valid():

                        office_id = form['office_id'].value()
                        storey = form['storey'].value()

                        office = Office.objects.get(id=office_id)

                        Room.objects.filter(id=id).update(office=office, storey=storey)
                case 'history_moves':
                    form = History_moveForm(request.POST)
                    if form.is_valid():

                        status_workplace = form['status_workplace'].value()
                        room_id = form['room_id'].value()
                        worker_id = form['worker_id'].value()

                        room = Room.objects.get(id=room_id)
                        worker = User.objects.get(id=worker_id)

                        History_move.objects.filter(id=id).update(status_workplace=status_workplace, room=room, worker=worker)
                case 'workers_rooms':
                    form = Worker_roomForm(request.POST)
                    if form.is_valid():

                        room_id = form['room_id'].value()
                        worker_id = form['worker_id'].value()

                        room = Room.objects.get(id=room_id)
                        worker = User.objects.get(id=worker_id)

                        Worker_room.objects.filter(id=id).update(room=room, worker=worker)
            return redirect('/app/' + path)
        except Exception as e:
            return HttpResponse(f"<h1>{e}</h1>")
    else:
        match path:
            case 'users':
                form = UserForm()
            case 'affiliates':
                form = AffiliateForm()
            case 'offices':
                form = OfficeForm()
            case 'rooms':
                form = RoomForm()
            case 'history_moves':
                form = History_moveForm()
            case 'workers_rooms':
                form = Worker_roomForm()
        return render(request, "add.html", {'form': form, 'btn_name': 'Edit', 'path': path})

def delete(request, path, id):
    try:
        match path:
            case 'users':
                user = User.objects.get(id=id)
                user.delete()
            case 'affiliates':
                group = Affiliate.objects.get(id=id)
                group.delete()
            case 'offices':
                post = Office.objects.get(id=id)
                post.delete()
            case 'rooms':
                comms = Room.objects.get(id=id)
                comms.delete()
            case 'history_moves':
                emojis = History_move.objects.get(id=id)
                emojis.delete()
            case 'workers_rooms':
                post_emojis = Worker_room.objects.get(id=id)
                post_emojis.delete()
        return redirect('/app/' + path)
    except Exception as e:
        return HttpResponse(f"<h1>{e}</h1>")