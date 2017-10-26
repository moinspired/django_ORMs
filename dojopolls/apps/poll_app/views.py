# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Poll, Vote
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def new_user(request):
    valid = User.userManager.register(
        request.POST['username'],
        request.POST['password'],
        request.POST['confirm']
    )
    if valid[0]:
        pass
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
    print valid
    return redirect('/')
def new_session(request):
    valid = User.userManager.login(
        request.POST['username'],
        request.POST['password']
    )
    if valid[0]:
            request.session['user'] = {
                "id" : valid[1].id,
                "username" : valid[1].username
            }
            return redirect('/polls')
    else:
        for error in valid[1]:
            messages.add_message(request, messages.INFO, error)
    
    return redirect('/')
def polls(request):
    if request.method == 'GET':
        context = {
            "polls": Poll.objects.all(),
            "votes": Vote.voteManager.filter(voter_id=request.session['user']['id'])
        }
        return render(request, 'polls.html', context)
    elif request.method == 'POST':
        Poll.objects.create(
            question = request.POST['question'],
            option1 = request.POST['option1'],
            option2 = request.POST['option2'],
            option3 = request.POST['option3'],
            creator_id = request.session['user']['id']
        )
        return redirect('/polls')
        
{"poll": poll, "voted": voted, "results": results}
def new_poll(request):
    return render(request, "new_poll.html")

def vote(request, id):
    if request.method == 'GET':
        poll = Poll.objects.get(id=id)
        results = {
            poll.option1: 0,
            poll.option2: 0,
            poll.option3: 0
        }
        poll = Poll.objects.get(id=id)
        voted = False
        for vote in Vote.voteManager.filter(voter_id=request.session['user']['id']):
            if vote.selection == 1:
                results[poll.option1] += 1
            elif vote.selection == 2:
                results[poll.option2] += 1
            elif vote.selection == 3:
                results[poll.option3] += 1
                
            if vote.poll.id == int(id):
                voted = True
        return render(request, "vote.html", )
    elif request.method == 'POST': 
        Vote.voteManager.vote(
           int(request.POST['sellection']),
           request.session['user']['id'],
           int(id)
        )
        return redirect("/polls")