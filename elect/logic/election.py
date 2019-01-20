from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elect.models import election, vote_token, voter, votes, position, winner, candidate
from django.db.models import Count
import datetime
from django.core.paginator import Paginator
from django.conf import settings
import string
import random
import pytz

@api_view(['POST'])
def create_election(request):
    """
    Create election
    -----
        {
           
            name:Roshie's election,
            description: adams okode likes roshie and goretti,
            startdate : 11
            enddate: 12
            endmonth: 12
            startmonth:12
            endyear:2018
            startyear:2018
            tokentime: 24
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            elections = election(
                name=request.data['name'],
                description=request.data['description'],
                startdate=datetime.datetime(int(request.data['startyear']),int(request.data['startmonth']),int(request.data['startdate']), tzinfo=pytz.UTC),  
                enddate=datetime.datetime(int(request.data['endyear']),int(request.data['endmonth']),int(request.data['enddate']), tzinfo=pytz.UTC), 
                tokentime=request.data['tokentime'],    
                status='0', 
                created_at = datetime.datetime.now(tz=pytz.UTC),
                updated_at= datetime.datetime.now(tz=pytz.UTC)
            )
            elections.save()
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



#update existing election    
@api_view(['POST'])
def update_election(request):    
    """
    Update election details
    -----
        {
            id:1,
            name:Roshie's election,
            description: adams okode likes roshie and goretti,
            startdate : 11
            enddate: 12
            endmonth: 12
            startmonth:12
            endyear:2018
            startyear:2018
            tokentime: 24
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            elections = election.objects.get(id=request.data['id'])
            elections.name = request.data['name']
            elections.description=request.data['description']
            elections.startdate = datetime.datetime(int(request.data['startyear']),int(request.data['startmonth']),int(request.data['startdate']), tzinfo=pytz.UTC),  
            elections.enddate=datetime.datetime(int(request.data['endyear']),int(request.data['endmonth']),int(request.data['enddate']), tzinfo=pytz.UTC), 
            elections.tokentime=request.data['tokentime'], 
            elections.updated_at = datetime.datetime.now(tz=pytz.UTC)
            elections.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)    


#activate existing election    
@api_view(['POST'])
def activate_election(request):    
    """
    Deactivate / Activate election
    -----
        {
            election_id:1,
            status: 1 or 0
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            elect = election.objects.get(id=request.data['election_id'])
            elect.status = request.data['status']
            elect.updated_at = datetime.datetime.now(tz=pytz.UTC)
            elect.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)  
            

#get all existing elections
@api_view(['POST'])  
def get_all_elections(request):  
    """
    See all elections 
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        elections= election.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(elections, request.data['items'])
        details=[]
        for elect in paginator.page(page):
            values={
                'id':elect.id,
                'name': elect.name,
                'description': elect.description,
                'startdate':elect.startdate,
                'enddate': elect.enddate,
                'tokentime': elect.tokentime,
                'created_at': elect.created_at,
                'updated_at': elect.updated_at
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


#get one particelar election details
@api_view(['POST'])  
def get_particular_election_details(request):

    """
    Get particular election details
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
            elect=election.objects.get(id=id)
            details={
                'id':elect.id,
                'name': elect.name,
                'description': elect.description,
                'startdate':elect.startdate,
                'enddate': elect.enddate,
                'tokentime': elect.tokentime,
                'created_at': elect.created_at,
                'updated_at': elect.updated_at
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
def delete_election(request):
    """
    remove election
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method=='DELETE':
            _id=request.data['id']
            delete=election.objects.filter(id=_id).delete()
            data={
                "data":"Election deleted",
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

#Create vote token for voter
@api_view(['POST'])  
def create_voter_token(request):

    """
    Create vote token for voter
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

            size=100 
            chars=string.ascii_uppercase + string.digits
            token = ''.join(random.choice(chars) for _ in range(size))

            elections = election.objects.filter(status = 1)
            for elect in elections:
                vote_tokens = vote_token(
                    token=token,
                    voter_id=voter_id,  
                    election_id = elect.id,
                    status='1', 
                    created_at = datetime.datetime.now(tz=pytz.UTC),
                    updated_at= datetime.datetime.now(tz=pytz.UTC)
                )
                vote_tokens.save()

            data={'message':'success','status_code':200}

            return Response(data)
    
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)  

@api_view(['GET'])  
def create_all_voter_tokens(request):

    """
    Create vote token for all voters
    -----
    """
    try:
        if request.method == 'POST':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'GET':
            voters=voter.objects.all()
            elections= election.objects.filter(status = 1)
            for userss in voters:
                for elec in elections:

                    size=100 
                    chars=string.ascii_uppercase + string.digits
                    token = ''.join(random.choice(chars) for _ in range(size))

                    tokens = vote_token.objects.filter(voter_id=userss.id)
                    tokens.delete()

                    vote_tokens = vote_token(
                        token=token,
                        voter_id=userss.id,  
                        election_id = elec.id,
                        status='1', 
                        created_at = datetime.datetime.now(tz=pytz.UTC),
                        updated_at= datetime.datetime.now(tz=pytz.UTC)
                    )
                    vote_tokens.save()

            data={'message':'success','status_code':200}

            return Response(data)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)  


#get all vote tokens
@api_view(['POST'])  
def get_all_vote_tokens(request):  
    """
    See all vote tokens 
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        tokens = vote_token.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(tokens, request.data['items'])
        details=[]
        deta = []
        da = []
        for token in paginator.page(page):
            values={
                'id':token.id,
                'user_id': token.user_id,
                'token': token.token,
                'election_id': token.election_id,
                'status': token.status,
                'created_at': token.created_at,
                'updated_at': token.updated_at
            }

            details.append(values)

        for cats in details:
            voters=voter.objects.get(id=cats['user_id'])
            val={
                'id':cats['id'],
                'fname': voters.fname,
                'lname': voters.lname,
                'email': voters.email,
                'password': voters.password,
                'status': cats['status'],
                'election_id': cats['election_id'],
                'msisdn': voters.msisdn,
                'region_id': voters.region_id,
                'token': cats['token'],
                'created_at': cats['created_at'],
                'updated_at': cats['updated_at']
            }
            deta.append(val)

        for ca in deta: 
            elect=election.objects.get(id=ca['election_id'])
            va={
                'id':ca['id'],
                'fname': ca['fname'],
                'lname': ca['lname'],
                'email': ca['email'],
                'password': ca['password'],
                'token_status': cats['status'],
                'msisdn': ca['msisdn'],
                'region_id': ca['region_id'],
                'token': ca['token'],
                'election_name': elect.name,
                'lection_description': elect.description,
                'token_created_at': ca['created_at'],
                'token_updated_at': ca['updated_at']
            }
            da.append(va)
        data={
            'data':da,
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

#get one particular voter token details
@api_view(['POST'])  
def get_particular_voter_token(request):

    """
    Get particular voter token details
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

            id=request.data['voter_id']
            token=vote_token.objects.get(voter_id=id)
            data=[]
            da=[]
            deta=[]
            details={
                'id':token.id,
                'voter_id': token.voter_id,
                'token': token.token,
                'status': token.status,
                'election_id': token.election_id,
                'created_at': token.created_at,
                'updated_at': token.updated_at
            }

            data.append(details)

            for cats in data:
                voters=voter.objects.get(id=cats['voter_id'])
                val={
                    'id':voters.id,
                    'fname': voters.fname,
                    'lname': voters.lname,
                    'email': voters.email,
                    'password': voters.password,
                    'status': voters.status,
                    'msisdn': voters.msisdn,
                    'region_id': voters.region_id,
                    'election_id': cats['election_id'],
                    'token': cats['token'],
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }
                deta.append(val)

            for ca in deta: 
                elect=election.objects.get(id=ca['election_id'])
                va={
                    'id':ca['id'],
                    'fname': ca['fname'],
                    'lname': ca['lname'],
                    'email': ca['email'],
                    'password': ca['password'],
                    'token_status': cats['status'],
                    'msisdn': ca['msisdn'],
                    'region_id': ca['region_id'],
                    'token': cats['token'],
                    'election_name': elect.name,
                    'election_description': elect.description,
                    'token_created_at': ca['created_at'],
                    'token_updated_at': ca['updated_at']
                }
                da.append(va)
            data={
                'data':da,
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

#Check if user is elligible to vote
@api_view(['POST'])  
def voter_elligibility(request):

    """
    Check if voter is elligible to vote
    -----
        {
            voter_id:1,
            election_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            id=request.data['voter_id']
            token=vote_token.objects.filter(voter_id=id)
            election_id = request.data['election_id']
            elect = election.objects.get(id=election_id)
            if token.exists():
                tokens = vote_token.objects.filter(election_id=election_id).get(id=id) 
                day = datetime.datetime.now(tz=pytz.UTC) - elect.startdate
                if elect.enddate > datetime.datetime.now(tz=pytz.UTC) and day.seconds < elect.tokentime*3600:
                    data={
                    'message':'success',
                    'status_code':200
                    }
                    return Response(data)
                elif day.seconds > elect.tokentime*3600:
                    data={
                    'message':'Token has expired',
                    'status_code':500
                    }
                    return Response(data)

                elif elect.enddate < datetime.datetime.now(tz=pytz.UTC):
                    data={
                    'message':'Election ended',
                    'status_code':500
                    }
                    return Response(data)

            else:
                data={
                    'message':'User not elligible',
                    'status_code':500
                    }
                return Response(data)
    
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)   

#vote
@api_view(['POST'])  
def vote (request):
    """
    Vote for a particular candidate
    -----
        {
            voter_id:1,
            position_id:1,
            candidate_id: 1,

        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            vote= votes.objects.filter(voter_id=request.data['voter_id'])
            if vote.exists():
                success={
                    'message':'Voter already voted',
                    'status_code':500
                }
                return Response(success)
            else:
                voter = votes(
                    voter_id = request.data['voter_id'],
                    position_id = request.data['position_id'],
                    candidate_id= request.data['candidate_id'],
                    status = '1',
                    created_at = datetime.datetime.now(tz=pytz.UTC),
                    updated_at= datetime.datetime.now(tz=pytz.UTC)
                )
                voter.save()
                success={
                    'message':'success',
                    'status_code':200
                }
                return Response(success)
    
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)   

#get all existing votes
@api_view(['POST'])  
def get_all_votes(request):  
    """
    See all votes
    -----
        {
            page:1
            items: 5
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            vote= votes.objects.all()
            numbers = votes.objects.all().count()
            page = request.GET.get('page', request.data['page'])
            paginator = Paginator(vote, request.data['items'])
            details=[]
            deta=[]
            for voter in paginator.page(page):
                values={
                    'id':voter.id,
                    'voter_id': voter.voter_id,
                    'position_id': voter.position_id,
                    'candidate_id':voter.candidate_id,
                    'status': voter.status,
                    'created_at': voter.created_at,
                    'updated_at': voter.updated_at
                }

                details.append(values)

            for cats in details:
                voters = voter.objects.get(id=cats['voter_id'])
                candidates = candidate.objects.get(id=cats['candidate_id'])
                positions = position.objects.get(id=cats['position_id'])
                val={
                    'id':cats['id'],
                    'voter_fname': voters.fname,
                    'voter_lname': voters.lname,
                    'candidate_fname': candidates.fname,
                    'candidate_lname': candidates.lname,
                    'position_name':positions.name,
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }

                deta.append(val)

            data={
                'data':deta,
                'total': numbers,
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

#get all existing votes for candidate
@api_view(['POST'])  
def get_all_votes_for_candidate(request):  
    """
    See all votes for particular candidate
    -----
        {
            page:1
            items: 5
            candidate_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            vote= votes.objects.filter(candidate_id=request.data['candidate_id'])
            numbers = votes.objects.filter(candidate_id=request.data['candidate_id']).count()
            page = request.GET.get('page', request.data['page'])
            paginator = Paginator(vote, request.data['items'])
            details=[]
            deta=[]
            for vot in paginator.page(page):
                values={
                    'id':vot.id,
                    'voter_id': vot.voter_id,
                    'position_id': vot.position_id,
                    'candidate_id':vot.candidate_id,
                    'status': vot.status,
                    'created_at': vot.created_at,
                    'updated_at': vot.updated_at
                }

                details.append(values)

            for cats in details:
                voters = voter.objects.get(id=cats['voter_id'])
                candidates = candidate.objects.get(id=cats['candidate_id'])
                positions = position.objects.get(id=cats['position_id'])
                val={
                    'id':cats['id'],
                    'voter_fname': voters.fname,
                    'voter_lname': voters.lname,
                    'candidate_fname': candidates.fname,
                    'candidate_lname': candidates.lname,
                    'position_name':positions.name,
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }

                deta.append(val)

            data={
                'data':deta,
                'total': numbers,
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

#get all existing votes for candidate
@api_view(['POST'])  
def get_all_votes_for_position(request):  
    """
    See all votes for particular position
    -----
        {
            page:1
            items: 5
            position_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            vote= votes.objects.filter(position_id=request.data['position_id'])
            numbers = votes.objects.filter(position_id=request.data['position_id']).count()
            page = request.GET.get('page', request.data['page'])
            paginator = Paginator(vote, request.data['items'])
            details=[]
            deta=[]
            for vot in paginator.page(page):
                values={
                    'id':vot.id,
                    'voter_id': vot.voter_id,
                    'position_id': vot.position_id,
                    'candidate_id':vot.candidate_id,
                    'status': vot.status,
                    'created_at': vot.created_at,
                    'updated_at': vot.updated_at
                }

                details.append(values)

            for cats in details:
                voters = voter.objects.get(id=cats['voter_id'])
                candidates = candidate.objects.get(id=cats['candidate_id'])
                positions = position.objects.get(id=cats['position_id'])
                val={
                    'id':cats['id'],
                    'voter_fname': voters.fname,
                    'voter_lname': voters.lname,
                    'candidate_fname': candidates.fname,
                    'candidate_lname': candidates.lname,
                    'position_name':positions.name,
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }

                deta.append(val)

            data={
                'data':deta,
                'total': numbers,
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

#Get the winner for a particular position
@api_view(['POST'])  
def winner_for_position(request):  
    """
    Get the winner for a particular position
    -----
        {
            position_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            vote= votes.objects.filter(position_id=request.data['position_id'])
            numbers = votes.objects.filter(position_id=request.data['position_id']).count()
            details=[]
            deta=[]
            for voter in vote:
                values={
                    'candidate_id':voter.candidate_id,
                }

                details.append(values)

            for cats in details:
                candidates = candidate.objects.get(id=cats['candidate_id'])
                total = votes.objects.filter(candidate_id=cats['candidate_id'])
                counter = votes.objects.filter(candidate_id=cats['candidate_id']).count()
                delete=winner.objects.filter(position_id=request.data['position_id'])
                positions = position.objects.get(id=request.data['position_id'])
                for deleter in delete:
                    deleter.delete()
                win=winner(
                    position_id = request.data['position_id'],
                    position_name = positions.name,
                    candidate_id = cats['candidate_id'],
                    candidate_fname = candidates.fname,
                    candidate_lname = candidates.lname,
                    total = counter,
                    created_at = datetime.datetime.now(tz=pytz.UTC),
                    updated_at= datetime.datetime.now(tz=pytz.UTC)
                )
                win.save()

            winners = winner.objects.filter(position_id=request.data['position_id']).order_by('total')
            for results in winners:
                val={
                    'id':results.id,
                    'candidate_fname': results.candidate_fname,
                    'candidate_lname': results.candidate_lname,
                    'position_name': results.position_name,
                    'total_votes':results.total,
                    'created_at': results.created_at,
                    'updated_at': results.updated_at
                }

                deta.append(val)

            data={
                'data':deta,
                'total': numbers,
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

#Close election and calculate final tally
@api_view(['POST'])  
def close_election(request):  
    """
    Close election and calculate final tally
    -----
        {
            election_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            positions = position.objects.filter(election_id=request.data['election_id'])
            details=[]
            deta=[]

            for pose in positions:
                vote = votes.objects.filter(position_id=pose.id).exists()
                if vote:
                    vote = votes.objects.get(position_id=pose.id)
                    numbers = votes.objects.filter(position_id=pose.id).count()
                    values={
                        'candidate_id':vote.candidate_id,
                        'position_id': pose.id,
                        'position_name': pose.name
                    }
                    details.append(values)
            
            for cats in details:
                candidates = candidate.objects.get(id=cats['candidate_id'])
                total = votes.objects.filter(candidate_id=cats['candidate_id'])
                counter = votes.objects.filter(candidate_id=cats['candidate_id']).count()
                delete=winner.objects.filter(position_id=cats['position_id'])
                for deleter in delete:
                    deleter.delete()
                win=winner(
                    position_id = cats['position_id'],
                    position_name = cats['position_name'],
                    candidate_id = cats['candidate_id'],
                    candidate_fname = candidates.fname,
                    candidate_lname = candidates.lname,
                    total = counter,
                    created_at = datetime.datetime.now(tz=pytz.UTC),
                    updated_at= datetime.datetime.now(tz=pytz.UTC)
                )
                win.save()

            winners = winner.objects.all().order_by('total')
            for results in winners:
                val={
                    'id':results.id,
                    'candidate_fname': results.candidate_fname,
                    'candidate_lname': results.candidate_lname,
                    'position_name': results.position_name,
                    'total_votes':results.total,
                    'created_at': results.created_at,
                    'updated_at': results.updated_at
                }

                deta.append(val)
            
            elections = election.objects.get(id=request.data['election_id'])
            elections.status = 0 
            elections.enddate = datetime.datetime.now(tz=pytz.UTC)
            elections.updated_at = datetime.datetime.now(tz=pytz.UTC)
            elections.save()
            
            data={
                'data':deta,
                'total': numbers,
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


#Show tally of who voted and who didnt vote
@api_view(['POST'])  
def who_voted_who_didnt(request):  
    """
    Show tally of who voted and who didnt vote
    -----
        {
            election_id:1
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':
            deta=[]
            details=[]
            detai=[]
            positions = position.objects.filter(election_id=request.data['election_id'])
            for pose in positions:
                vote = votes.objects.get(position_id=pose.id)
                numbers = votes.objects.filter(position_id=pose.id).count()
                voters = voter.objects.all().count()
                didntvote = voters - numbers
                values={
                    'voter_id': vote.id
                }
                details.append(values)
            
            for cats in details:
                voters = voter.objects.get(id=cats['voter_id'])
                val={
                    'id':cats['voter_id'],
                    'fname': voters.fname,
                    'lname': voters.lname,
                }
                vot = voter.objects.all()
                for vots in vot:
                    if vots.id != cats['voter_id']:
                        vale = {
                            'id':vots.id,
                            'fname': vots.fname,
                            'lname': vots.lname,
                        }
                        detai.append(vale)

                deta.append(val)
            
            data={
                'data':{
                    'voted':deta,
                    'notvoted':detai
                },
                'voted': numbers,
                'didntvote': didntvote,
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

 