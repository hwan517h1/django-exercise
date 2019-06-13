from django.shortcuts import render, redirect
from .models import Feed, FeedComment


def index(request):
    if request.method == 'GET': # index
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    elif request.method == 'POST': # create
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')

def show(request, id):
    if request.method == 'GET': # show
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/show.html', {'feed': feed})
    
    elif request.method == 'POST': # update
        title = request.POST['title']
        content = request.POST['content']
        
        feed = Feed.objects.get(id=id)
        feed.title = title
        feed.content = content
        feed.save()
        feed.update_date()
        
        return redirect('/feeds/' + str(id))

def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')

def create_comment(request, id):
    content = request.POST['content']
    FeedComment.objects.create(feed_id=id, content=content)
    return redirect('/feeds')

def delete_comment(request, id, cid):
    comment = FeedComment.objects.get(id=cid)
    comment.delete()
    return redirect('/feeds')