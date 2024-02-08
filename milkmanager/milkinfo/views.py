from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Cistern, FillHistory


def index(request):
    cisterns = Cistern.objects.all()
    fill_history = FillHistory.objects.all().order_by('filled_at')
    # print(1)
    return render(request, 'milkinfo/index.html', {'cisterns': cisterns, 'fill_history': fill_history})


def fill_milk(request):

    if request.method == 'POST':
        name = request.POST['name']
        volume = int(request.POST['volume'])
        cistern = Cistern.objects.order_by('current_volume').first()
        if cistern.current_volume + volume <= cistern.volume:
            cistern.current_volume += volume
            cistern.save()
            FillHistory.objects.create(cistern=cistern, filler_name=name, filled_volume=volume)
            return JsonResponse({'success': True, 'cistern_id': cistern.id, 'cistern_volume': cistern.current_volume})
        else:
            return JsonResponse(
                {'success': False, 'error_message': 'Невозможно долить молоко, не хватает места в канистре'})
    return render(request, 'milkinfo/form.html')  # , {'name': name, 'volume': volume})
