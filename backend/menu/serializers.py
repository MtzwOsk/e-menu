from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from rest_framework.fields import SerializerMethodField

from menu.models import Menu
from dishes.serializers import DishSerializer


class MenuSerializer(ModelSerializer):
    """
    Menu model's serializer
    """

    dishes_number = SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'

    def get_dishes_number(self, menu):
        return menu.dishes.count()


class MenuSerializerWithDish(ModelSerializer):

    dishes = HyperlinkedIdentityField(view_name='dishes:api-dish-details', source='dishes')

    class Meta:
        model = Menu
        fields = ['id', 'title', 'description', 'created', 'dishes']


class MenuAndDishSerializer(ModelSerializer):
    """
    Menu model's serializer
    """

    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'

