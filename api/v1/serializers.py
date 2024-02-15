from rest_framework import serializers

from api.models import Advocate, CBUser, Company


class UserAuthSerializer(serializers.ModelSerializer):
    pass


class UserProfileSerializer(serializers.ModelSerializer):
    pass


class AdovateSerializer(serializers.ModelsSerializer):
    """
    Returns Python object for  Adocate modell.
    """

    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Advocate
        depth = 4


class CompanySerializer(serilaizers.ModelSerializer):
    """
    Serializers company object into native python \
        onject and vice-versa.
    """

    advocates = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Company
        depth = 1
