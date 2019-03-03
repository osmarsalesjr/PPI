from rest_framework import serializers, validators
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('owner', 'balance', 'creation_date')

    def validate(self, attrs):
        if attrs['creation_date'] is not None:
            raise validators.ValidationError('Creation Date cannot be an argument')

        if attrs['balance'] < 0:
            raise validators.ValidationError('Balance cannot be negative')

        if attrs['balance'] == 0:
            raise validators.ValidationError('Balance cannot be zero')
