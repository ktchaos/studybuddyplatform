# from infra.BuddyDataBaseFactory import BuddyDataBaseFactory
# from infra.BuddyLocalDataBase import BuddyLocalDataBase

from infra.database.local.BuddyLocalDataBase import BuddyLocalDataBase
from infra.factories.BuddyDataBaseFactory import BuddyDataBaseFactory

class BuddyLocalDataBaseFactory(BuddyDataBaseFactory):
    def makeDataBase():
        return BuddyLocalDataBase()