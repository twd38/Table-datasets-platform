from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
import pandas as pd
from pandas import DataFrame
import django_filters
import csv, io, codecs
import datetime




#VIEWS
def index(request):
	all_posts = Post.objects.all()

	return render(request, 'index.html', {'all_posts': all_posts})


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)


def createPost(request):
	return render(request, 'createpost.html')


def updateSettings(request):
	user = request.user

	if user:
		name = request._post['name']
		profile_pic = request.FILES['profile_pic']

		settings = UserSettings(name=name, profile_pic=profile_pic)
		settings.save()

		id = request.user.id
		url = reverse('userPosts', args=[id])
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def addPost(request):
	user = request.user

	if user:
		title = request._post['title']
		currentDT = datetime.datetime.now()
		timestamp = currentDT.strftime("%Y-%m-%d %H:%M:%S")
		description = request._post['description']
		source = request._post['source']
		keywords = request._post['keywords']
		dataset = request.FILES['csv_file']
		data = pd.read_csv(dataset)
		cropped_dataset_a = data.iloc[:5, :4]
		data_crop_html = cropped_dataset_a.to_html(classes=["table", "table-bordered"])
		data_html = data.to_html(classes=["table", "table-bordered"])
		new_post = Post(title=title, description=description, source=source, keywords=keywords, dataset=dataset, data_crop_html=data_crop_html, data_html=data_html, poster=user)
		new_post.save()
		id = request.user.id
		url = reverse('userPosts', args=[id])
		return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect('/')


def userPosts(request, user_id):
	user = User.objects.get(pk=user_id)
	context = {
		"user": user,
		"posts": user.tables.all(),
	}
	return render(request, "userposts.html", context)


def deletePost(request, post_id):
	post_to_delete = Post.objects.get(id=post_id)
	post_to_delete.delete()
	id = request.user.id
	url = reverse('userPosts', args=[id])
	return HttpResponseRedirect(url)


def searchResults(request):
	query = request.GET['query']
	filtered_posts = Post.objects.filter(keywords__icontains=query)

	context = {
		"query": query,
		"filtered_posts": filtered_posts
	}
	return render(request, 'searchResults.html', context)


def singleTable(request, post_id):
	post = Post.objects.get(pk=post_id)
	context = {
		"post": post
	}
	return render(request, "singleTable.html", context)