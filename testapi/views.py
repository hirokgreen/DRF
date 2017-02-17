"""testapi views"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from testapi.models import Contact
from testapi.serializers import ContactSerializer

@api_view(['GET', 'POST'])
def contact_details(request):
    """GET for get all contact,\nPOST for create new contact.\n(in Content box do as following)\n{
        "name": "",
        "email": "",
        "address": ""
    }\n and press POST button."""
    if request.method == 'GET':
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
@api_view(['GET', 'DELETE', 'PUT'])
def contact_element(request, primary_key):
    """DELETE for delete contact of given id,\nPUT for update contact.\n(in Content box do as)\n{
        "name": "",
        "email": "",
        "address": ""
    }\n and press PUT button."""
    try:
        contact = Contact.objects.get(pk=primary_key)
    except Contact.DoesNotExist:
        return Response('Contact not found with this ID', status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        contact.delete()
        return Response('Deletion successfull', status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':  
        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully updated', status=status.HTTP_204_NO_CONTENT) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    serializer = ContactSerializer(contact, many=False)    
    return Response(serializer.data)    
