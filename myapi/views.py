from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapi.models import Pitch, CounterOffer
from myapi.serializers import PitchSerializer, CounterOfferSerializer

@csrf_exempt
def pitch_list(request):
    if request.method == 'GET':
        pitchs = Pitch.objects.all()
        #Pitch.objects.all().delete()
        serializer = PitchSerializer(pitchs, many=True)
        new_dict = []
        for i in range(len(serializer.data)):
            new_dict.append(serializer.data[i])
            new_dict[i]['askAmount'] = int(new_dict[i]['askAmount'])
            new_dict[i]['id'] = str(new_dict[i]['id'])
        return JsonResponse(new_dict[::-1], safe=False)

    elif request.method == 'POST':
        #print(request)
        data = JSONParser().parse(request)
        #print(data)
        serializer = PitchSerializer(data=data)
        if serializer.is_valid() and serializer.validated_data['equity'] <= 100 and serializer.validated_data['equity'] >= 0:
            pid = serializer.save()
            return JsonResponse({'id' : str(pid)}, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def pitch_detail(request, pk):
    try:
        pitch = Pitch.objects.get(pk=pk)
        
    except Pitch.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PitchSerializer(pitch)
        offers = [] 
        for i in serializer.data['offers']:
            offers.append(CounterOfferSerializer(CounterOffer.objects.get(pk=i)).data)
            offers[-1]['id'] = i
        new_dict = {}
        for key in serializer.data:
            new_dict[key] = serializer.data[key]
        new_dict['offers'] = offers
        new_dict['askAmount'] = int(new_dict['askAmount'])
        return JsonResponse(new_dict)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PitchSerializer(pitch, data=data)
        if serializer.is_valid() and serializer.validated_data['equity'] <= 100 and serializer.validated_data['equity'] >= 0:
            pid = serializer.save()
            return JsonResponse({'id' : str(pid)}, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pitch.delete()
        return HttpResponse(status=204)

@csrf_exempt
def make_offer(request, pk):
    try:
        pitch = Pitch.objects.get(pk=pk)
    except Pitch.DoesNotExist:
        #print("NOTT ODUDND")
        return HttpResponse(status=404)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =  CounterOfferSerializer(data=data)
        if serializer.is_valid() and serializer.validated_data['equity'] <= 100.0 and serializer.validated_data['equity'] >= 0.0:
            pid = serializer.save()
            pitch.offers.add(pid)
            return JsonResponse({
                'id' : str(pid),
            }, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pitch.delete()
        return HttpResponse(status=204)