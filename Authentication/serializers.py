from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#python -m pip install djangorestframework-simplejwt 

class CustomerToken_Serializer(TokenObtainPairSerializer):

    def validate(self, attrs):
         
         data = super().validate(attrs)

         data.update({
               'username' : self.user.username,
               'data' : self.user.date_joined
         })

         return data

