from rest_framework import serializers

from .models import material, Herramientas, LaborIndirecta, Factura




class MaterialSerializers(serializers.ModelSerializer):
    class Meta:
        model = material
        fields = ['codigo', 'title', 'unidad', 'precio']

class HerramientasSerializers(serializers.ModelSerializer):

	class Meta:

		model = Herramientas
		fields = ['codigo', 'titulo', 'COP', 'precio']

class LaborIndirectaSerializers(serializers.ModelSerializer):

	class Meta:

		model = LaborIndirecta
		fields = ['codigo', 'nombre', 'jornal']

class FacturaSerializers(serializers.ModelSerializer):

	class Meta:

		model = Factura
		fields = ['Titulo', 'Numero_Factura', 'Cod_Factura', 'Material', 'Herramientas', 'LaborIndirecta']




