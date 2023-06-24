from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import csv
import pandas as pd 
from django.views import View
import numpy as np
import json

# Create your views here.
from teamranking.models import teamInformation

from .models import VjudgeStandings
from teamranking.models import teamInformation


def sigmoid(val):
    return 1/(1+np.exp(-val))

def scoreFunc(teamA,teamB,totalContestants):

    val=(sigmoid(np.sqrt(teamB/teamA))-0.7)*np.log2(totalContestants)*1500
    #print(val)
    return max(val,10)




#implementation of the rating system from https://tlx.toki.id/ranking/rating-system
def update_rating(team_list):
   
    
    teamHiddenRating={}
    teamPublicRating={}
    #attended_contests=1

    

    for i in range(len(team_list)):
        
        queryset=teamInformation.objects.get(team_name=team_list[i][0])
        
        hidden_rating=queryset.hidden_rating
        teamHiddenRating[team_list[i][0]]=hidden_rating
        rating=queryset.rating
        teamPublicRating[team_list[i][0]]=rating
        #if(i==0):
        #   attended_contests+=queryset.attended_contests
        #print(team_list[i][0]," ",teamHiddenRating[team_list[i][0]])


    
    for i in range(len(team_list)):
        delta=0
        teamA=team_list[i][0]
        rankA=team_list[i][1]
        scoreA=team_list[i][2]
        penaltyA=team_list[i][3]
        for j in range(len(team_list[i])):
            if(i==j):
                continue
            teamB=team_list[j][0]
            rankB=team_list[j][1]
            scoreB=team_list[j][2]
            penaltyB=team_list[j][3]
            hidden_ratingA=teamHiddenRating[teamA]
            hidden_ratingB=teamHiddenRating[teamB]
            if(scoreA==scoreB):
                if(penaltyA==penaltyB):
                    continue
                elif penaltyA<penaltyB:
                    delta+=scoreFunc(hidden_ratingA,hidden_ratingB,len(team_list))
                else:
                    delta-=scoreFunc(hidden_ratingB,hidden_ratingA,len(team_list))
            elif scoreA>scoreB:
                delta+=scoreFunc(hidden_ratingA,hidden_ratingB,len(team_list))
            else:
                delta-=scoreFunc(hidden_ratingB,hidden_ratingA,len(team_list))

        
        
        delta=delta/len(team_list)
       
        debt=teamHiddenRating[teamA]-teamPublicRating[teamA]

        if delta>=0:
            teamPublicRating[teamA]+=0.2*delta
            debt+=0.8*delta
            if debt>0:
                teamPublicRating[teamA]+=debt
                debt=0
        else:
            debt+=delta
            teamPublicRating[teamA]+=0.5*debt
            debt=0.5*debt
        

        teamHiddenRating[teamA]=teamPublicRating[teamA]+debt
        teamPublicRating[teamA]=np.floor(teamPublicRating[teamA])
        teamHiddenRating[teamA]=np.floor(teamHiddenRating[teamA])

        print(teamA,"",team_list[i][1]," ",teamPublicRating[teamA]," ",teamHiddenRating[teamA])



    for i in range(len(team_list)):
        team_name=team_list[i][0]
        queryset=teamInformation.objects.get(team_name=team_name)
        queryset.hidden_rating=teamHiddenRating[team_name]
        queryset.rating_change=teamPublicRating[team_name]-queryset.rating
        queryset.rating=teamPublicRating[team_name]
        queryset.attended_contests+=1
        print(team_name," ",queryset.attended_contests)
        queryset.save()




def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()


class FileUpload(View):
    
    
  
 
    def get(self,request):
        return render(request,'vjudgestats/file_upload.html')
    def post(self,request):
        #print(request.POST['ContestName'])
        contestName=request.POST['ContestName']
        csv_file=request.FILES['uploaded_csv_files']
        df=pd.read_csv(csv_file,on_bad_lines="skip")
        queryset=teamInformation.objects.all()
        team_list=[]

      
       
        for index in df.index:
            team_name=df['Team Name'][index]
            
            splited_name=team_name.split(' ')

            team_name=splited_name[1]
            result=teamInformation.objects.filter(team_name__icontains=team_name)
        
            if result :
                temp=[team_name,df['Rank'][index],df['Score'][index],df['Penalty'][index]]
                team_list.append(temp)
                #update_rating(team_name,df['Rank'][index],df['Score'][index],df['Penalty'][index])


        update_rating(team_list)
        Standings=VjudgeStandings()
        Standings.contest_name=contestName
        Standings.contest_details=json.dumps(team_list,default=np_encoder)
        print(Standings.contest_details)
        Standings.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    

def vjudgeContestStandings(request):
    queryset=VjudgeStandings.objects.all()
    print(queryset[0].contest_details)
    return render(request,"vjudgestats/vjudge_contest_standings.html",{"querysets":queryset})