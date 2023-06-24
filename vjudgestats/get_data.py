# Created by Maruf Hasan
from bs4 import BeautifulSoup
import requests
import pandas as pd
from html_table_extractor.extractor import Extractor
import collections



import os
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teammanagement.settings")

# Initialize Django
django.setup()




from teamranking.models import teamInformation





collections.Callable = collections.abc.Callable

filename = open('ICPC61 (1).html', 'r')
soup = BeautifulSoup(filename, "html.parser")
extractor = Extractor(soup, id_='contest-rank-table')
extractor.parse()


teamlist = extractor.return_list()

flag = 0

newTeamList = []
for team in teamlist:
    try:
        if (int(team[0])):
            newTeamList.append(team)
    except:
        pass

#print(len(newTeamList))

teamlist = []

teamlist = newTeamList

mylist = []

for index in range(len(teamlist)):
    tempList = []
    # if(teamlist[index])
    # print(index, " ", teamlist[index][0])
    for j in range(3):
        tempList.append(teamlist[index][j])
    penalty = teamlist[index][3].split()[0]
    tempList.append(penalty)
    # print(index, tempList)
    # print(tempList)
    mylist.append(tempList)

# print(mylist)


df = pd.DataFrame(mylist, columns=['Rank', 'Team Name', 'Score', 'Penalty'])

df[['Score', 'Penalty']] = df[['Score', 'Penalty']].apply(pd.to_numeric)


#print(teamInformation)

#df.to_csv('rating_csv_files\ICPC_61.csv')
