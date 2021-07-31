import time

from django.shortcuts import render
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def index(request):
    return render(request, 'notifier/home.html')


def status_form(request):
    if request.method == 'POST':
        num = int(request.POST['TB_sample'])
        progress = 10
        for i in range(num):
            room_group_name = f'notify'
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                room_group_name, {
                    "type": "status.notifier",  # interesting, here we call status_notifier function from consumers.py # TODO check if we replace this value with status_notifier string value
                    "data": progress
                }
            )
            message = "Status Running"  # TODO why it is in for loop? test if move to out of for loop
            progress += 10
            time.sleep(1)

    context = {'message': message}
    return render(request, 'notifier/home.html', context)
