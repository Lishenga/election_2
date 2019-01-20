from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elect.models import region
import datetime
import pytz
from django.core.paginator import Paginator
from django.conf import settings

@api_view(['POST'])
def create_region(request):
    """
    Create Region
    -----
        {
           
            name:J town,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            regions = region(
                name=request.data['name'],
                status='1', 
                created_at = datetime.datetime.now(tz=pytz.UTC),
                updated_at= datetime.datetime.now(tz=pytz.UTC)
            )
            regions.save()
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



#update existing Region    
@api_view(['POST'])
def update_region(request):    
    """
    Update region details
    -----
        {
            id:1,
            name:J town,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            regions = region.objects.get(id=request.data['id'])
            regions.name = request.data['name']
            regions.updated_at = datetime.datetime.now(tz=pytz.UTC)
            regions.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)    
            

#get all existing regions
@api_view(['POST'])  
def get_all_regions(request):  
    """
    See all regions 
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        regions = region.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(regions, request.data['items'])
        details=[]
        deta = []
        for reach in paginator.page(page):
            values={
                'id':reach.id,
                'name': reach.name,
                'status': reach.status,
                'created_at': reach.created_at,
                'updated_at': reach.updated_at
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


#get one particular region details
@api_view(['POST'])  
def get_particular_region_details(request):

    """
    Get particular region details
    -----
        {
            id:1,
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            id=request.data['id']
            regions=region.objects.get(id=id)
            deta=[]
            details={
                'id':regions.id,
                'name': regions.name,
                'status': regions.status,
                'created_at': regions.created_at,
                'updated_at': regions.updated_at
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
def delete_region(request):
    """
    remove region
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method=='DELETE':
            _id=request.data['id']
            delete=region.objects.get(id=_id).delete()
            data={
                "data":"region deleted",
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