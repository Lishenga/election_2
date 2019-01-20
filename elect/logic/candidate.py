from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elect.models import candidate
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
def create_candidate(request):
    """
    Create Candidate
    -----
        {
           
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            msisdn:254682312,
            password:roshie,
            region_id: 1
            position_id:1
            status: 1 or SUPER
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            candidates = candidate(
                fname=request.data['fname'],
                lname=request.data['lname'], 
                email=request.data['email'],  
                password=make_password(request.data['password']), 
                region_id=request.data['region_id'], 
                position_id=request.data['position_id'],
                picture='null',
                picture_thumb='null',
                description ='null',
                status=request.data['status'], 
                msisdn=request.data['msisdn'],
                created_at = datetime.datetime.now(tz=pytz.UTC),
                updated_at= datetime.datetime.now(tz=pytz.UTC)
            )
            candidates.save()
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



#upload picture for candidate   
@api_view(['POST'])
def upload__picture(request):    
    """
    Upload candidate picture
    -----
        {
            candidate_id:1,
            picture:leon,
            description: amnad
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST' and request.FILES['picture']:
            candidates = candidate.objects.get(id=request.data['candidate_id'])

            size=30 
            chars=string.ascii_uppercase + string.digits
            newName = ''.join(random.choice(chars) for _ in range(size))+'.jpg'
            newName_thumb = ''.join(random.choice(chars) for _ in range(size))+'_thumb'+'.png'
            basewidth = 300
            img = Image.open(request.FILES['picture'])
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            fs = FileSystemStorage()
            filename = fs.save(newName, request.FILES['picture'])
            img_thumb = img.save(newName_thumb, format="png", quality=70)

            candidates.picture = newName
            candidates.picture_thumb = newName_thumb
            candidates.description = request.data['description']
            candidates.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error) 


#get picture for candidate
@api_view(['POST'])  
def get_pic_for_candidate(request):

    """
    Get picture for a candidate
    -----
        {
            candidate_id:1,
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':
            candidates=candidate.objects.get(id=request.data['user_id'])
            details=[]
            values={
                'pictures': candidates.picture,
                'pictures_thumb': candidates.picture_thumb,
                'created_at': candidates.created_at,
                'updated_at': candidates.updated_at
            }

            details.append(values)

            data={'data':details,'message':'success','status_code':200}

            return Response(data)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)


#update existing candidate   
@api_view(['POST'])
def update_candidate(request):    
    """
    Update candidate details
    -----
        {
            id:1,
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            msisdn:254682312,
            position_id: 1
            region_id : 1,
            status : 1 or SUPER
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            candidates = candidate.objects.get(id=request.data['id'])
            candidates.fname = request.data['fname']
            candidates.lname=request.data['lname']
            candidates.email=request.data['email']
            candidates.msisdn=request.data['msisdn'],
            candidates.region_id=request.data['region_id'],
            candidates.position_id=request.data['position_id'],
            candidates.status=request.data['status'],
            candidates.updated_at=datetime.datetime.today(),
            user.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)     


#update existing candidate    
@api_view(['POST'])
def candidate_device_uid(request):    
    """
    Update candidate details
    -----
        {
            candidate_id:1,
            device_uid:aksdhjashja65546,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            candidates = candidate.objects.get(id=request.data['candidate_id'])
            candidates.device_uid = request.data['device_uid'],
            candidates.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)     

#update existing candidate password   
@api_view(['POST'])
def update_candidate_password(request):   
    """ 
    Update candidate Password
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
            candidates = candidate.objects.get(id=request.data['id'])
            candidates.password = make_password(request.data['password'])
            candidates.save()
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



#get all existing candidates
@api_view(['POST'])  
def get_all_candidates(request):  
    """
    See all candidates 
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        candidates= candidate.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(candidates, request.data['items'])
        details=[]
        for cands in paginator.page(page):
            values={
                'id':cands.id,
                'fname': cands.fname,
                'lname': cands.lname,
                'email': cands.email,
                'password': cands.password,
                'status': cands.status,
                'msisdn': cands.msisdn,
                'region_id': cands.region_id,
                'position_id': cands.position_id,
                'updated_at': cands.updated_at
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


#get one particular candidate details
@api_view(['POST'])  
def get_particular_candidate_details(request):

    """
    Get particular candidate details
    -----
        {
            candidate_id:1,
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            candidate_id=request.data['candidate_id']
            candidates=candidate.objects.get(id=candidate_id)
            details={
                'id':candidates.id,
                'fname': candidates.fname,
                'lname': candidates.lname,
                'email': candidates.email,
                'password': candidates.password,
                'status': candidates.status,
                'msisdn': candidates.msisdn,
                'region_id': candidates.region_id,
                'position_id': candidates.position_id,
                'created_at': candidates.created_at,
                'updated_at': candidates.updated_at
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
def delete_candidate(request):
    """
    remove candidate
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method=='DELETE':
            _id=request.data['id']
            delete=candidate.objects.filter(id=_id).delete()
            data={
                "data":"candidate deleted",
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



@api_view(['POST'])
def get_candidate_email_login(request):  

    """
    Update candidate details
    -----
        {
            email:roshie@gmail.com,
            password:roshie,
        }
    """

    try:
        candidate_email=request.data['email']
        user_input_pass=request.data['password']
        candidates=candidate.objects.get(email=candidate_email)

        if password_handler.verify(user_input_pass, candidates.password):
            success={
                'data':{
                    'id':candidates.id,
                    'fname': candidates.fname,
                    'lname': candidates.lname,
                    'email': candidates.email,
                    'password': candidates.password,
                    'status': candidates.status,
                    'msisdn': candidates.msisdn,
                    'region_id': candidates.region_id,
                    'position_id': candidates.position_id,
                    'created_at': candidates.created_at,
                    'updated_at': candidates.updated_at
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