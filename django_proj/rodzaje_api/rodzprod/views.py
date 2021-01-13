from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.views.generic import ListView

from rodzprod.models import Produkty,Rodzaje,Surowce,Narzedzia,Zaklady
from rodzprod.serializers import ProduktySerializer,RodzajeSerializer,SurowceSerializer,NarzedziaSerializer,ZakladySerializer

from rest_framework.decorators import api_view

class ZakladyList(ListView):
    model = Zaklady
    

# Create your views here.
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def rodzaje_lista(request):
    if request.method == 'GET':
        try:
            rodzaje_lista = Rodzaje.objects.all()
            rodzaje_serializer = RodzajeSerializer(rodzaje_lista,many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z Rodzaj",
                'rodzaje': rodzaje_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać rodzaj_lista",
                'rodzaje': "[]",
                'error': "Bład"
            }
            return JsonResponse(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            rodzaje_data = JSONParser().parse(request)
            rodzaje_serializer = RodzajeSerializer(data=rodzaje_data)
            
            if rodzaje_serializer.is_valid():
                rodzaje_serializer.save()
                print(rodzaje_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Rodzaj o id = %d" % id, 
                    'rodzaje': [rodzaje_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz,status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'rodzaje': "[]",
                    'error': rodzaje_serializer.error
                }
                return JsonResponse(error,status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'rodzaje': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        try:
            Rodzaje.objects.all().delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except:
            exceptionError = {
                'wiadomosc': " nie można skutecznie skasować danych",
                'rodzaje':"[]",
                'error': 'Wystąpił błąd'
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def rodzaje_detail(request,pk):
    try:
        rodzaje = Rodzaje.objects.get(pk=pk)
    except Rodzaje.DoesNotExist:
        exceptionError ={
            'wiadomosc': "Nie znaleziono rodzaj 0 id =%s" % pk,
            'rodzaj': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }        
        return JsonResponse(exceptionError,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        rodzaje_serializer = RodzajeSerializer(Rodzaje)
        odpowiedz = {
            'wiadomosc': "Odczyt Rodzaj 0 id = %s" % pk,
            'rodzaje': [rodzaje_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            rodzaje_data = JSONParser().parse(request)
            rodzaje_serializer = RodzajeSerializer(Rodzaje,data=rodzaje_data)
            
            if rodzaje_serializer.is_valid():
                rodzaje_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w Rodzaj zakończona powodzeniem dla id = %s" % pk,
                    'rodzaj': [rodzaje_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w Rodzaj dla id = %s" % pk,
                'rodzaje': [rodzaje_serializer.data],
                'error': rodzaje_serializer.error
            }
            return JsonResponse(odpowiedz,status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie rodzaj o id=%s" % pk)
            Rodzaje.delete()
            rodzaje_serializer = RodzajeSerializer(rodzaje)
            odpowiedz = {
                'wiadomosc': " Rodzaj o id = %s został skasowany" %pk,
                'rodzaje': [rodzaje_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)
        
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def produkty_lista(request):
    if request.method == 'GET':
        try:
            produkty_lista = Produkty.objects.all()
            produkty_serializer = ProduktySerializer(produkty_lista,many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z Produkty",
                'produkty': produkty_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać produkt_lista",
                'produkty': "[]",
                'error': "Błąd"
            }
            return JsonResponse(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            produkty_data = JSONParser().parse(request)
            produkty_serializer = ProduktySerializer(data=produkty_data)
            
            if produkty_serializer.is_valid():
                produkty_serializer.save()
                print(produkty_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Produkt o id = %d" % id, 
                    'produkty': [produkty_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz,status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'produkty': "[]",
                    'error': produkty_serializer.error
                }
                return JsonResponse(error,status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'produkty': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
            try:
                Produkty.objects.all().delete()
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
            except:
                exceptionError = {
                    'wiadomosc': " nie można skutecznie skasować danych",
                    'produkty':"[]",
                    'error': 'Wystąpił błąd'
                }
                return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def produkty_detail(request,pk):
    try:
        produkt = Produkty.objects.get(pk=pk)
    except Produkty.DoesNotExist:
        exceptionError ={
            'wiadomosc': "Nie znaleziono produkt 0 id =%s" % pk,
            'produkty': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }        
        return JsonResponse(exceptionError,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        produkty_serializer = ProduktySerializer(Produkty)
        odpowiedz = {
            'wiadomosc': "Odczyt Rodzaj 0 id = %s" % pk,
            'produkty': [produkty_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            produkty_data = JSONParser().parse(request)
            produkty_serializer = ProduktySerializer(produkt,data=produkty_data)
            
            if produkty_serializer.is_valid():
                produkty_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w Rodzaj zakończona powodzeniem dla id = %s" % pk,
                    'produkty': [produkty_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w Rodzaj dla id = %s" % pk,
                'produkty': [produkty_serializer.data],
                'error': produkty_serializer.error
            }
            return JsonResponse(odpowiedz,status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie produkt o id=%s" % pk)
            Produkty.delete()
            produkty_serializer = ProduktySerializer(produkt)
            odpowiedz = {
                'wiadomosc': " Produkt o id = %s został skasowany" %pk,
                'produkty': [produkty_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)
        
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def zaklady_lista(request):
    if request.method == 'GET':
        try:
            zaklady_lista = Zaklady.objects.all()
            zaklady_serializer = ZakladySerializer(zaklady_lista,many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z zaklady",
                'zaklady': zaklady_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać zaklad_lista",
                'zaklady': "[]",
                'error': "Błąd"
            }
            return JsonResponse(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            zaklady_data = JSONParser().parse(request)
            zaklady_serializer = ZakladySerializer(data=zaklady_data)
            
            if zaklady_serializer.is_valid():
                zaklady_serializer.save()
                print(zaklady_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Zaklad o id = %d" % id, 
                    'zaklady': [zaklady_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz,status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'zaklady': "[]",
                    'error': zaklady_serializer.error
                }
                return JsonResponse(error,status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'zaklady': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
            try:
                Zaklady.objects.all().delete()
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
            except:
                exceptionError = {
                    'wiadomosc': " nie można skutecznie skasować danych",
                    'zaklady':"[]",
                    'error': 'Wystąpił błąd'
                }
                return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def zaklady_detail(request,pk):
    try:
        zaklad = Zaklady.objects.get(pk=pk)
    except Zaklady.DoesNotExist:
        exceptionError ={
            'wiadomosc': "Nie znaleziono zaklad 0 id =%s" % pk,
            'zaklady': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }        
        return JsonResponse(exceptionError,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        zaklady_serializer = ZakladySerializer(Zaklady)
        odpowiedz = {
            'wiadomosc': "Odczyt Zaklad o id = %s" % pk,
            'zaklady': [zaklady_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            zaklady_data = JSONParser().parse(request)
            zaklady_serializer = ZakladySerializer(Zaklady,data=zaklady_data)
            
            if zaklady_serializer.is_valid():
                zaklady_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w surowce zakończona powodzeniem dla id = %s" % pk,
                    'zaklady': [zaklady_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w surowce dla id = %s" % pk,
                'zaklady': [zaklady_serializer.data],
                'error': zaklady_serializer.error
            }
            return JsonResponse(odpowiedz,status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie produkt o id=%s" % pk)
            Zaklady.delete()
            zaklady_serializer = ZakladySerializer(zaklad)
            odpowiedz = {
                'wiadomosc': " Zaklad o id = %s został skasowany" %pk,
                'zaklady': [zaklady_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)
        
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def surowce_lista(request):
    if request.method == 'GET':
        try:
            surowce_lista = Surowce.objects.all()
            surowce_serializer = SurowceSerializer(surowce_lista,many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z Surowce",
                'surowce': surowce_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać surowce_lista",
                'surowce': "[]",
                'error': "Błąd"
            }
            return JsonResponse(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            surowce_data = JSONParser().parse(request)
            surowce_serializer = SurowceSerializer(data=surowce_data)
            
            if surowce_serializer.is_valid():
                surowce_serializer.save()
                print(surowce_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Zaklad o id = %d" % id, 
                    'surowce': [surowce_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz,status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'surowce': "[]",
                    'error': surowce_serializer.error
                }
                return JsonResponse(error,status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'surowce': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
            try:
                Surowce.objects.all().delete()
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
            except:
                exceptionError = {
                    'wiadomosc': " nie można skutecznie skasować danych",
                    'surowce':"[]",
                    'error': 'Wystąpił błąd'
                }
                return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def surowce_detail(request,pk):
    try:
        surowce = Surowce.objects.get(pk=pk)
    except Surowce.DoesNotExist:
        exceptionError ={
            'wiadomosc': "Nie znaleziono  surowce 0 id =%s" % pk,
            'surowce': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }        
        return JsonResponse(exceptionError,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        surowce_serializer = SurowceSerializer(Surowce)
        odpowiedz = {
            'wiadomosc': "Odczyt Surowce o id = %s" % pk,
            'surowce': [surowce_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            surowce_data = JSONParser().parse(request)
            surowce_serializer = SurowceSerializer(Surowce,data=surowce_data)
            
            if surowce_serializer.is_valid():
                surowce_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w surowce zakończona powodzeniem dla id = %s" % pk,
                    'surowce': [surowce_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w surowce dla id = %s" % pk,
                'surowce': [surowce_serializer.data],
                'error': surowce_serializer.error
            }
            return JsonResponse(odpowiedz,status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie produkt o id=%s" % pk)
            Surowce.delete()
            surowce_serializer = SurowceSerializer(Surowce)
            odpowiedz = {
                'wiadomosc': " Surowce o id = %s został skasowany" %pk,
                'surowce': [surowce_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)        
        
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def narzedzia_lista(request):
    if request.method == 'GET':
        try:
            narzedzia_lista = Narzedzia.objects.all()
            narzedzia_serializer = NarzedziaSerializer(narzedzia_lista,many=True)
            odpowiedz = {
                'wiadomosc': "Sukces - Pobrano dane z Narzedzia",
                'narzedzia': narzedzia_serializer.data,
                'error':  ""
            }
            return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
        except:
            error = {
                'wiadomosc': "Bład -> nie mogę odczytać narzedzia_lista",
                'narzedzia': "[]",
                'error': "Błąd"
            }
            return JsonResponse(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            narzedzia_data = JSONParser().parse(request)
            narzedzia_serializer = NarzedziaSerializer(data=narzedzia_data)
            
            if narzedzia_serializer.is_valid():
                narzedzia_serializer.save()
                print(narzedzia_serializer.data)
                odpowiedz = {
                    'wiadomosc': "Sukces - pobrano Zaklad o id = %d" % id, 
                    'narzedzia': [narzedzia_serializer.data],
                    'error': ""
                }
                return JsonResponse(odpowiedz,status=status.HTTP_201_CREATED)
            else:
                error = {
                    'wiadomosc': "Nie mogę pobrać danych",
                    'narzedzia': "[]",
                    'error': narzedzia_serializer.error
                }
                return JsonResponse(error,status=status.HTTP_400_BAD_REQUEST)
        except:
            exceptionError = {
                'wiadomosc': "Błąd w pobieraniu danych",
                'narzedzia': "[]",
                'error': "Wystąpił błąd"
            }
            return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
            try:
                Narzedzia.objects.all().delete()
                return HttpResponse(status=status.HTTP_204_NO_CONTENT)
            except:
                exceptionError = {
                    'wiadomosc': " nie można skutecznie skasować danych",
                    'narzedzia':"[]",
                    'error': 'Wystąpił błąd'
                }
                return JsonResponse(exceptionError,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def narzedzia_detail(request,pk):
    try:
        narzedzia = Narzedzia.objects.get(pk=pk)
    except Narzedzia.DoesNotExist:
        exceptionError ={
            'wiadomosc': "Nie znaleziono  narzedzia 0 id =%s" % pk,
            'narzedzia': "[]",
            'error': "Nie znaleziono - kod 404 error"
        }        
        return JsonResponse(exceptionError,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        narzedzia_serializer = NarzedziaSerializer(Narzedzia)
        odpowiedz = {
            'wiadomosc': "Odczyt Narzedzia o id = %s" % pk,
            'narzedzia': [narzedzia_serializer.data],
            'error': ""
        }
        return JsonResponse(odpowiedz,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        try:
            narzedzia_data = JSONParser().parse(request)
            narzedzia_serializer = NarzedziaSerializer(Narzedzia,data=narzedzia_data)
            
            if narzedzia_serializer.is_valid():
                narzedzia_serializer.save()
                odpowiedz = {
                    'wiadomosc': "Zmiana w narzedzia zakończona powodzeniem dla id = %s" % pk,
                    'narzedzia': [narzedzia_serializer],
                    'error': ""
                }
                return JsonResponse(odpowiedz)
            odpowiedz = {
                'wiadomosc': "Błąd w zapisie w narzedzia dla id = %s" % pk,
                'narzedzia': [narzedzia_serializer.data],
                'error': narzedzia_serializer.error
            }
            return JsonResponse(odpowiedz,status=status.HTTP_400_BAD_REQUEST)
        except request.method == 'DELETE':
            print("kasowanie produkt o id=%s" % pk)
            Narzedzia.delete()
            narzedzia_serializer = NarzedziaSerializer(Narzedzia)
            odpowiedz = {
                'wiadomosc': " Narzedzia o id = %s został skasowany" %pk,
                'narzedzia': [narzedzia_serializer.data],
                'error': ""
            }
            return JsonResponse(odpowiedz)        
        
