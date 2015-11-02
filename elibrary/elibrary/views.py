__author__ = 'akash'

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm
from elibrary.forms import MyRegistrationForm
from django.contrib.auth.models import User
from django.contrib import admin
from books.models import Books
from django.db import IntegrityError
import json

def hello(request):
    return render_to_response('login.html')


def login(request):

    return render_to_response('login.html')

def auth_view(request):
    print request.POST
    
    username = request.POST['username']
    password = request.POST['password']
    # user = User(username=username)
    # user.set_password(password)
    # user.save()

    print username, password
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
    return render_to_response('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register(request):
    return render_to_response('register.html')

def register_user(request):
    
    print request.POST
    """first_name = request.POST['first_name']
    last_name = request.POST['last_name']"""
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    user = User(username=username,email=email)
    user.set_password(password)
    try:
        user.save()
    except IntegrityError:
        print "User already Exists..."
        
    return HttpResponseRedirect('/accounts/login/')

def register_success(request):
    return render_to_response('register_success.html')

def books_view(request):
    books = Books.objects.all()
    args = {}
    args['books'] = books
    return render_to_response('books_view.html', args)

def home(request):
    books = Books.objects.filter(tag="")
    args = {}
    args['tag']=''
    args['books'] = books
    return render_to_response('home.html', args)

def book_view(request):
    books = Books.objects.filter(tag="BOOK")
    category = Books.objects.filter(category="None")
    #book_id = Books.objects.filter(id=id)
    #count = Books.objects.filter(tag="BOOK").count()
    #print count
    args = {}
    args['tag']='BOOK'
    args['category']='None'
    #args['book_id']='id'
    args['books'] = books
    print args
    return render_to_response('home.html', args)

def video_view(request):
    books = Books.objects.filter(tag="VIDEO")
    #books = Books.objects.filter(category="None")
    args = {}
    args['tag']='VIDEO'
    #args['category']='None'
    args['books']=books
    print args
    return render_to_response('home.html',args)

def edit_book(request,book_id=None):

    book=Books.objects.get(id=book_id)
    print book
    args = {}
    args['book']=book
    print request
    #books = Books.objects.all()

    """  book_name=.GET['book_name']
    author_name=request.GET['author_name']


    description=request.GET['description']
    file=request.FILES['file']
    tag=request.GET['tag']
    category=request.GET['category']"""

    # print book_name,author_name,description,file,category
    
    # book=Books(book_name=book_name,author_name=author_name,description=description,thumbnail=file,tag=tag,category=category)

    return render_to_response('edit_form.html',args)

def comp_view(request):
    tag = Books.objects.filter(tag="BOOK")
    books = Books.objects.filter(category="Computer")
    args = {}
    args['category']='Computer'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)
    
def mech_view(request):
    books = Books.objects.filter(category="Mechanical",tag="BOOK")
    args = {}
    args['category']='Mechanical'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)

def etc_view(request):
    books = Books.objects.filter(category="E_&_TC",tag="BOOK")
    args = {}
    args['category']='E_&_TC'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)

def civil_view(request):
    books = Books.objects.filter(category="Civil",tag="BOOK")
    args = {}
    args['category']='Civil'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)

def it_view(request):
    books = Books.objects.filter(category="IT",tag="BOOK")
    args = {}
    args['category']='IT'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)

def electrical_view(request):
    books = Books.objects.filter(category="Electrical",tag="BOOK")
    args = {}
    args['category']='Electrical'
    args['tag']='BOOK'
    args['books'] = books
    return render_to_response('home.html',args)



def json_view(request):
    books = Books.objects.all()
    book_list = []
    for i in books:
        try:
            fileUrl = "Media/"+str(i.thumbnail)
        except Exception, e:
            fileUrl = None
        obj = {"book_name": i.book_name, "author_name": i.author_name, "fileUrl": fileUrl, "tag":i.tag, "description": i.description, "category": i.category}
        book_list.append(obj)
    return HttpResponse(json.dumps({"bookList": book_list}), content_type="application/json")

def angular_test(request):
    return render_to_response("angularTest.html")