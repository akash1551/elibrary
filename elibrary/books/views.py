from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from books.models import Books
from books.forms import BookForm
import json
from django.core.context_processors import csrf
from django.contrib import admin	
from django.contrib.auth.models import User


def books(request):
    return render_to_response('books.html',{'books':Books.objects.all()})

def get_book(request,book_id=None):
	
    return render_to_response('home.html',{'book':Books.objects.get(id=book_id)})

def book_data(request):
	books = Books.objects.all()
	books_list = []
	for i in books:
		obj = {"book_name": i.book_name, "author_name": i.author_name, "description": i.description}
		books_list.append(obj)

	return HttpResponse(json.dumps({"books_list": books_list}), content_type="application/json")

def upload_book(request):
	return render_to_response('upload.html')


def upload_auth(request):
	
	print request.POST
	book_name=request.POST['book_name']
	author_name=request.POST['author_name']
	description=request.POST['description']
	file=request.FILES['file']
	tag=request.POST['tag']
	category=request.POST['category']

	print book_name,author_name,description,file,category
	
	book=Books(book_name=book_name,author_name=author_name,description=description,thumbnail=file,tag=tag,category=category)
	book.save()

	return HttpResponseRedirect('/books/uploadbook')

def new_book(request):
	return render_to_response('newbook.html')

def create(request):
	if request.POST:
		return render_to_response('books/all')
	else:
		form=BookForm()
	args={}
	args.update(csrf(request))

	args['form']=form

def search_titles(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
	else:
		search_text=''

	books = Books.objects.filter(book_name__contains=search_text)
	return render_to_response('ajax_search.html',{'books':books})

def save_data(request):
    print request.POST
    if request.method == "POST":
    	print True
    book_id=request.POST['id']
    book_name=request.POST['book_name']
    author_name=request.POST['author_name']
    description=request.POST['description']
   # file=request.FILES['file']
    book = Books.objects.get(id=book_id)
    book.book_name = book_name
    book.author_name = author_name
    book.description = description
    book.save()

    return render_to_response('home.html')
