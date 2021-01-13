from rest_framework import serializers
from rodzprod.models import Produkty,Rodzaje, Surowce,Zaklady,Narzedzia

class ZakladySerializer(serializers.ModelSerializer):
    class Meta:
        model = Zaklady
        fields = (
            'id',
            'nazwa',
            'rodzaje_zaklady'
        )
        
class RodzajeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rodzaje
        fields = (
            'id',
            'nazwa',
            'produkty_rodzaj',
            'surowce_rodzaj',
            'narzedzia_rodzaj'
        )
        
class ProduktySerializer(serializers.ModelSerializer):
    class Meta:
        model = Produkty
        fields = (
            'id', 
            'nazwa',
            'poziom',
            'idr'
        )
        
class SurowceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surowce
        fields = (
            'id', 
            'nazwa',
            'ilosc'
        )
        
class NarzedziaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Narzedzia
            fields = (
                'id', 
                'nazwa',
                'aktywnosc'
        )