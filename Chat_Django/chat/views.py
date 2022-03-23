from django.shortcuts import render

def index(request):
    """ function for main page """
    return render(request, 'chat/index.html')

def room(request, room_name):
    """ function for chat room page """
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
