# from infra.BuddyDataBaseFactory import BuddyDataBaseFactory
# from infra.BuddyRemoteDataBase import BuddyRemoteDataBase

from infra.database.remote.BuddyRemoteDataBase import BuddyRemoteDataBase
from infra.factories.BuddyDataBaseFactory import BuddyDataBaseFactory

class BuddyRemoteDataBaseFactory(BuddyDataBaseFactory):
    def makeDataBase():
        return BuddyRemoteDataBase()