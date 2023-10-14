import sys
import os

from infra.database.BuddyDataBase import BuddyDataBase

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy
from data.entities.student import Student
import requests
import json

class BuddyRemoteDataBase(BuddyDataBase):
    def __init__(self) -> None:
        self.dbUrl = "https://studybuddy-b2751-default-rtdb.firebaseio.com/"
    
    # Create
    def saveBuddies(self, buddies):
        for buddy in buddies:
            parameters = {
                'remoteId': "",
                'id': buddy.id,
                'name': buddy.name,
                'age': buddy.age,
                'password': buddy.password,
                'avatar': buddy.avatar,
                'interestSubjects': buddy.interest_subjects
            }
            createRequest = requests.post(f'{self.dbUrl}/Buddies/.json', data=json.dumps(parameters))

            # logs
            returnedId = createRequest.json()
            buddy.remoteId = returnedId['name']
            print(createRequest)
            print(createRequest.text)

    # Read
    def getBuddy(self, buddyId):
        getRequest = requests.get(f'{self.dbUrl}/Buddies/{buddyId}/.json')
        # logs
        print(getRequest)
        print(getRequest.text)

    # Busca por nome
    def getBuddyByName(self):
        getRequest = requests.get(f'{self.dbUrl}/.json')
        resultJson = getRequest.json()
        # logs
        print(getRequest)
        print(getRequest.raw)
        print(resultJson)

    # Update Remote Id
    def updateBuddyRemoteId(self, remoteId):
        parameters = {
            'remoteId': remoteId
        }
        patchRequest = requests.patch(f'{self.dbUrl}/Buddies/{remoteId}/.json', data=json.dumps(parameters))
        # logs
        print(patchRequest)
        print(patchRequest.text)

    # Update
    def updateBuddy(self, buddyId, name, avatar, interestSubjects):
        parameters = {
            'name': name,
            'avatar': avatar,
            'interestSubjects': interestSubjects
        }
        patchRequest = requests.patch(f'{self.dbUrl}/Buddies/{buddyId}/.json', data=json.dumps(parameters))
        # logs
        print(patchRequest)
        print(patchRequest.text)

    # Delete
    def deleteBuddy(self):
        deleteRequest = requests.delete(f'{self.dbUrl}/Buddies/-NdXW2yt-vPxTv9Z6-TY/.json')
        # logs
        print(deleteRequest)
        print(deleteRequest.text)

    def loadBuddies(self):
        getRequest = requests.get(f'{self.dbUrl}/Buddies/.json')
        # logs
        dictTest = getRequest.json()

        remoteBuddies = []
        for chave, valor in dictTest.items():
            # print(f'Chave = {chave}')
            # print(f'Valor = {valor}')
            remoteStudent = Student(
                remoteId=valor['remoteId'],
                id=valor['id'],
                name=valor['name'],
                age=valor['age'],
                password=valor['password'],
                avatar=valor['avatar'],
                interest_subject=[]
            )
            remoteBuddies.append(remoteStudent)
        
        return remoteBuddies
        # print(getRequest)
        # print(dictTest.items())


class TestObject:
    def __init__(self, age, avatar, id, name, password, remoteId) -> None:
        self.age = age
        self.avatar = avatar
        self.id = id
        self.name = name
        self.password = password
        self.remoteId = remoteId
        # '-NgaxRpKQRnxnD8pYarT': {
        #     'age': 22,
        #     'avatar': '',
        #     'id': 0,
        #     'name': 'catarina',
        #     'password': 'abcde12345',
        #     'remoteId': '-NgaxRpKQRnxnD8pYarT'
        #     },
        