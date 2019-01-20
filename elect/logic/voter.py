from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elect.models import voter
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
from django.core.files.storage import FileSystemStorage
from PIL import Image
import datetime
import random
import string
import pytz
import os
from django.core.paginator import Paginator

@api_view(['POST'])
def create_voter(request):
    """
    Create Voter
    -----
        {
           
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            msisdn:254682312,
            password:roshie,
            region_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            voters = voter(
                fname=request.data['fname'],
                lname=request.data['lname'], 
                email=request.data['email'],  
                password=make_password(request.data['password']), 
                region_id=request.data['region_id'], 
                status='1', 
                msisdn=request.data['msisdn'],
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            voters.save()
            success={
                'message':'success',
                'status_code':200
            }
            return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)   


#update existing voter 
@api_view(['POST'])
def update_voter(request):    
    """
    Update voter details
    -----
        {
            id:1,
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            msisdn:254682312,
            region_id : 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            voters = voter.objects.get(id=request.data['id'])
            voters.fname = request.data['fname']
            voters.lname=request.data['lname']
            voters.email=request.data['email']
            voters.msisdn=request.data['msisdn'],
            voters.region_id=request.data['region_id'],
            voters.updated_at=datetime.datetime.today(),
            voters.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)     


#update existing voter   
@api_view(['POST'])
def voter_device_uid(request):    
    """
    Update voter details
    -----
        {
            voter_id:1,
            device_uid:aksdhjashja65546,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            voters = voter.objects.get(id=request.data['voter_id'])
            voters.device_uid = request.data['device_uid'],
            voters.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)     

#update existing voter  password   
@api_view(['POST'])
def update_voter_password(request):   
    """ 
    Update voter Password
    -----
        {
            id:1,
            password:123456
        } 
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            voters = voter.objects.get(id=request.data['id'])
            voters.password = make_password(request.data['password'])
            voters.save()
            success={
                'message':'success',
                'status_code':200,
                'data':{}
            }
            return Response(success)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)            



#get all existing voter
@api_view(['POST'])  
def get_all_voters(request):  
    """
    See all voters 
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        voters= voter.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(voters, request.data['items'])
        details=[]
        for vote in paginator.page(page):
            values={
                'id':vote.id,
                'fname': vote.fname,
                'lname': vote.lname,
                'email': vote.email,
                'password': vote.password,
                'status': vote.status,
                'msisdn': vote.msisdn,
                'region_id': vote.region_id,
                'updated_at': vote.updated_at
            }

            details.append(values)

        data={
            'data':details,
            'message':'success',
            'status_code':200
            }
        return Response(data)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)   


#get one particular voters details
@api_view(['POST'])  
def get_particular_voter_details(request):

    """
    Get particular voter details
    -----
        {
            voter_id:1,
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            voter_id=request.data['voter_id']
            voters=voter.objects.get(id=voter_id)
            details={
                'id':voters.id,
                'fname': voters.fname,
                'lname': voters.lname,
                'email': voters.email,
                'password': voters.password,
                'status': voters.status,
                'msisdn': voters.msisdn,
                'region_id': voters.region_id,
                'created_at': voters.created_at,
                'updated_at': voters.updated_at
            }

            data={'data':details,'message':'success','status_code':200}

            return Response(data)
    
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)   


@api_view(['DELETE'])
def delete_voter(request):
    """
    remove voter
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method=='DELETE':
            _id=request.data['id']
            delete=voter.objects.filter(id=_id).delete()
            data={
                "data":"voter deleted",
                "message":delete,
                "status_code":200
            }
            return Response(data)
        else:
            snippets={
                
                'message':"invalid request",
                "status_code":401
            }
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)    


#voter login credentials
@api_view(['POST'])
def get_voter_email_login(request):  

    """
    Update voter details
    -----
        {
            email:roshie@gmail.com,
            password:roshie,
        }
    """

    try:
        voter_email=request.data['email']
        user_input_pass=request.data['password']
        voters=voter.objects.get(email=voter_email)

        if password_handler.verify(user_input_pass, voters.password):
            success={
                'data':{
                    'id':voters.id,
                    'fname': voters.fname,
                    'lname': voters.lname,
                    'email': voters.email,
                    'password': voters.password,
                    'status': voters.status,
                    'msisdn': voters.msisdn,
                    'region_id': voters.region_id,
                    'created_at': voters.created_at,
                    'updated_at': voters.updated_at
                    },
                'status_code':200,
            }
                
            return Response(success)

        else:
            success={
                'message':'Error',
                'status_code':500
            }
                
            return Response(success)    
    except BaseException as e :
        
        error={
            'status_code':500,
            'message':'error'+str(e),
            'data':{
               
            }
        }
        return Response(error)