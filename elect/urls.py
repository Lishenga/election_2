from django.urls import include, path
from django.contrib.auth.models import User 
from rest_framework import routers, serializers, viewsets
from elect.logic import voter, election, position, candidate, region


urlpatterns = [
    
    #Voter routes
    path('voter/createvoter/', voter.create_voter),
    path('voter/updatevoter/', voter.update_voter),
    path('voter/voter_device_uid/', voter.voter_device_uid),
    path('voter/deletevoter/', voter.delete_voter),
    path('voter/getallvoters/', voter.get_all_voters),
    path('voter/email_login/', voter.get_voter_email_login),
    path('voter/resetvoterpassword/',voter.update_voter_password),
    path('voter/getparticularvoter/', voter.get_particular_voter_details),
    

    #Candidate routes
    path('candidate/createcandidate/', candidate.create_candidate),
    path('candidate/updatecandidate/', candidate.update_candidate),
    path('candidate/candidate_device_uid/', candidate.candidate_device_uid),
    path('candidate/deletecandidate/', candidate.delete_candidate),
    path('candidate/getallcandidates/', candidate.get_all_candidates),
    path('candidate/email_login/', candidate.get_candidate_email_login),
    path('candidate/resetcandidatepassword/',candidate.update_candidate_password),
    path('candidate/getparticularcandidate/', candidate.get_particular_candidate_details),
    path('candidate/uploadcandidatepicture/', candidate.upload__picture),
    path('candidate/getcandidatepic/', candidate.get_pic_for_candidate),

    #Election routes
    path('election/createelection/', election.create_election),
    path('election/updateelection/', election.update_election),
    path('election/deleteelection/', election.delete_election),
    path('election/getallelections/', election.get_all_elections),
    path('election/getparticularelection/', election.get_particular_election_details),
    path('election/votednotvoted/', election.who_voted_who_didnt),
    path('election/closeelection/', election.close_election),
    path('election/activateelection/', election.activate_election),

    #Token routes
    path('token/createtoken/', election.create_voter_token),
    path('token/getalltokens/', election.get_all_vote_tokens),
    path('token/getparticularvotertoken/', election.get_particular_voter_token),
    path('token/allvoters/', election.create_all_voter_tokens),

    #Voter routes
    path('voter/voter_elligibility/', election.voter_elligibility),
    path('voter/vote/', election.vote),
    path('voter/get_all_votes/', election.get_all_votes),
    path('voter/get_all_votes_for_candidate/', election.get_all_votes_for_candidate),
    path('voter/get_all_votes_for_position/', election.get_all_votes_for_position),
    path('voter/winner/', election.winner_for_position),

    #Position routes
    path('position/createposition/', position.create_position),
    path('position/updateposition/', position.update_position),
    path('position/deleteposition/', position.delete_position),
    path('position/getallpositions/', position.get_all_positions),
    path('position/getallcandidatesparticularposition/', position.get_all_candidates_positions),
    path('position/getparticularposition/', position.get_particular_position_details),
    path('position/getallpositionsforelection/', position.get_all_positions_for_an_election),
    path('position/getallpositionsvoterelligble', position.get_all_positions_voter_votes_for),


    #Region routes
    path('region/createregion/', region.create_region),
    path('region/updateregion/', region.update_region),
    path('region/deleteregion/', region.delete_region),
    path('region/getallregions/', region.get_all_regions),
    path('region/getparticularregion/', region.get_particular_region_details),

]