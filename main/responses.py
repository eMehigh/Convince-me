from .models import Room, CreatorMessages, JoinerMessages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404

@csrf_exempt
def wait_for_connection(request, name):
    if request.method == 'POST':
        room = Room.objects.get(room_name=name)
        if room.has_pair:
            pair_name = room.pair_name
            return HttpResponse(pair_name)
        else:
            return HttpResponse("gfndauigbna87th4378514bhjkbI^&VRT#!^*&IFEkfv4y3t*!&RGDS╝┴s☻")


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        try:  # Creator
            room = Room.objects.get(room_name=name)
            creator = CreatorMessages.objects.get(room=room)
            creator.message = message
            creator.save()
        except:  # Joiner
            room = Room.objects.get(pair_name=name)
            joiner = JoinerMessages.objects.get(room=room)
            joiner.message = message
            joiner.save()
        return HttpResponse(message)

    if request.method == 'GET':
        name = request.GET['name']
        if is_creator(name):
            room = Room.objects.get(room_name=name)
            try:
                joiner = JoinerMessages.objects.get(room=room)
                message = joiner.message
                print(message)
                if message == "mortiiteiboro":
                    pair_name = room.pair_name
                    room.delete()
                    content = [str(pair_name), message]
                    return JsonResponse(content, safe=False)
                else:
                    joiner.message = None
                    joiner.save()
                    if message:
                        content = [str(room.pair_name), message]
                        return JsonResponse(content, safe=False)
            except:
                pass
        else:
            try:
                room = Room.objects.get(pair_name=name)
                creator = CreatorMessages.objects.get(room=room)
                message = creator.message
                print(message)
                if message == 'mortiiteiboro':
                    room.delete()
                    return HttpResponse(message)
                creator.message = None
                creator.save()
                if message:
                    return HttpResponse(message)
            except:
                pass
    return HttpResponse('qqqquuuu^fwh&fg*ewg(*$@gmdsognds*&(^$#gbyrowiguyb')


def is_creator(name):
    rooms = Room.objects.all()
    creators = []
    pairs = []
    for room in rooms:
        creators.append(room.room_name)
        pairs.append(room.pair_name)
    if name in creators:
        return True
    else:
        return False
