from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, CreatorMessages, JoinerMessages
from .responses import wait_for_connection, send_message
from django.contrib import messages

def main_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        rooms = Room.objects.all()
        users = []
        for room in rooms:
            users.append(room.room_name)
            users.append(room.pair_name)
        if name in users:
            messages.success(
                request, 'Name already taken!')
            return redirect('index')
        else:
            Room.objects.create(room_name=str(name))
            return redirect('create-room', name)
    return render(request, 'main/index.html', )


def list_view(request):
    if request.method == 'POST':
        room_name = request.POST['room-name']
        pair_name = request.POST['name']
        rooms = Room.objects.all()
        users = []
        for room in rooms:
            users.append(room.room_name)
            users.append(room.pair_name)
        if pair_name in users:
            messages.success(
                request, 'Name already taken!')
            return redirect('chat-list')
        else:
            room = Room.objects.get(room_name=room_name)
            JoinerMessages.objects.create(room=room)
            return redirect('chat', room_name, pair_name)
    try:
        rooms = Room.objects.all()
    except:
        rooms = None
    return render(request, 'main/user-list.html', {'rooms':rooms})

def chat_view(request, room_name, pair_name):
    room = Room.objects.get(room_name=room_name)
    if room.has_pair == True:
        messages.error(request, "Cannot enter this room.")
        return redirect('chat-list')
    else:
        room.pair_name = pair_name
        room.has_pair = True
        room.save()
    creator_name = room_name
    pair_name = pair_name
    context = {
        'creator_name': creator_name,
        'pair_name': pair_name
    }
    return render(request, 'main/chat.html', context)


def create_room_view(request, name):
    room = Room.objects.get(room_name=str(name))
    if room.created == True:
        messages.error(request, "Cannot enter this room.")
        return redirect('index')
    else:
        room.created = True
        room.save()
    CreatorMessages.objects.create(room=room)
    if request.method == 'POST':
        room = Room.objects.get(room_name = str(name))
        room.delete()
    return render(request, 'main/create-room.html', {'name': name})
