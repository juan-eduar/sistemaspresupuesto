from .models import material, Herramientas, LaborIndirecta, Factura
from rest_framework import viewsets
from .serializers import MaterialSerializers, HerramientasSerializers, LaborIndirectaSerializers, FacturaSerializers

class ViewsMaterial(viewsets.ModelViewSet):

	queryset = material.objects.all()

	serializer_class = MaterialSerializers

class ViewsHerramientas(viewsets.ModelViewSet):

	queryset = Herramientas.objects.all()

	serializer_class = HerramientasSerializers

class ViewsIndirectaSerializers(viewsets.ModelViewSet):

	queryset = LaborIndirecta.objects.all()

	serializer_class = LaborIndirectaSerializers

class ViewsFacturaSerializers(viewsets.ModelViewSet):

	queryset = Factura.objects.all()

	serializer_class = FacturaSerializers



    

	

		 