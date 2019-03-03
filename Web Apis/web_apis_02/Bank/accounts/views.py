from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Account
from accounts.serializers import AccountSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def account_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)

        return Response(accounts_serializer.data)
    elif request.method == 'POST':
        account_serializer = AccountSerializer(data=request.data)

        if account_serializer.is_valid():

            if account_serializer.validated_data['balance'] < 0:
                return Response(AccountSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def account_detail(request, pk):
    try:
        account = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response(AccountSerializer.errors, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        account_serializer = AccountSerializer(account)
        return Response(account_serializer.data)
    elif request.method == 'PUT':
        account_serializer = AccountSerializer(account, data=request.data)

        if account_serializer.is_valid():
            account_serializer.save()
            return Response(account_serializer.data)

        return Response(AccountSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        account_serializer = AccountSerializer(account, data=request.data)

        if account_serializer.is_valid():

            if account_serializer.validated_data['owner'] != account.owner or account_serializer.validated_data[
                'creation_date'] != account.creation_date:
                return Response(AccountSerializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

            balance = account_serializer.validated_data['balance']
            if balance < 0 and (balance * -1) > account.balance:
                return Response(AccountSerializer.errors, status=status.HTTP_401_UNAUTHORIZED)

            account_serializer.validated_data['balance'] += account.balance
            account_serializer.save()

            return Response(account_serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)
