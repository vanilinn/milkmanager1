from django.shortcuts import render
from django.http import JsonResponse
from .models import Cistern, FillHistory


def index(request):
    cisterns = Cistern.objects.all()
    fill_history = FillHistory.objects.all().order_by('filled_at')
    return render(request, 'milkinfo/index.html', {'cisterns': cisterns, 'fill_history': fill_history})


def fill_milk(request):
    if request.method == 'POST':
        # имя из формы
        name = request.POST['name']
        # объем из формы
        volume = int(request.POST['volume'])
        # сортируем цистерны по текущему объему и выбираем наименее заполненную
        cistern = Cistern.objects.order_by('current_volume').first()
        # если можем в нее долить, то доливаем
        if cistern.current_volume + volume <= cistern.volume:
            cistern.current_volume += volume
            cistern.save()
            # сохраняем запись о заливке
            FillHistory.objects.create(cistern=cistern, filler_name=name, filled_volume=volume)
            return JsonResponse({'success': True, 'cistern_id': cistern.id, 'cistern_name': cistern.name, 'cistern_volume': cistern.current_volume,
                                 'milk_filled': volume, 'name': name})
        else:
            return JsonResponse(
                {'success': False, 'error_message': 'Невозможно долить молоко, не хватает места в цистерне'})
    return render(request, 'milkinfo/form.html')
