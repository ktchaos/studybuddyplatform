from abc import ABC, abstractmethod
from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory 

class ReportTemplate(ABC):
    def generateReport(self):
        print(" --------------------------------------------------------------")
        print(" --------------------------------------------------------------")
        print(" -------------- RELATÓRIO - STUDY BUDDY PLATFORM --------------")
        self.generateHeader()
        remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()
        buddies = remoteDb.loadBuddies()
        for buddy in buddies:
            print(f'Número de acessos do usuário - {buddy.name} -> {buddy.numberOfAccessesLastMonth} (último mês)')
        self.generateBody()
        self.generateFooter()
        print(" ----------------- FIM - STUDY BUDDY PLATFORM -----------------")
        print(" --------------------------------------------------------------")

    @abstractmethod
    def generateHeader(self):
        pass

    @abstractmethod
    def generateBody(self):
        pass

    @abstractmethod
    def generateFooter(self):
        pass