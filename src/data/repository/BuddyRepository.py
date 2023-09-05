import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from entities.buddy import Buddy
import requests
import json

class BuddyRepository:
    def __init__(self) -> None:
        self.dbUrl = "https://studybuddy-b2751-default-rtdb.firebaseio.com/"

    # Create
    def createBuddy(self, buddy: Buddy):
        parameters = {
            'id': buddy.id,
            'name': buddy.name,
            'age': buddy.age,
            'avatar': buddy.avatar,
            'interestSubjects': buddy.interest_subjects
        }
        createRequest = requests.post(f'{self.dbUrl}/Buddies/.json', data=json.dumps(parameters))

        # logs
        print(createRequest)
        print(createRequest.text)

    # Read
    def getBuddy(self, buddyId):
        getRequest = requests.get(f'{self.dbUrl}/Buddies/{buddyId}/.json')
        # logs
        print(getRequest)
        print(getRequest.text)

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

    def getAllBuddies(self):
        getRequest = requests.get(f'{self.dbUrl}/Buddies/.json')
        # logs
        dictTest = getRequest.json()
        print(getRequest)
        print(dictTest['-NdXW2yt-vPxTv9Z6-TY'])