import pickle

from infra.database.BuddyDataBase import BuddyDataBase
# from infra.BuddyDataBase import BuddyDataBase

class BuddyLocalDataBase(BuddyDataBase):

    #carrega buddies salvos no arquivo
    def loadBuddies(self):
        try:
            with open('./src/infra/saveLocalData/buddies.bin', 'rb') as fp:
                buddy_list = pickle.load(fp)
                return buddy_list
        except FileNotFoundError:
            # se o arquivo nao existe, retorna uma lista vazia
            print('Arquivo nao encontrado.')
            return []

    def saveBuddies(self, buddies):
        try:
            # salva a lista atualizada no arquivo
            with open('./src/infra/saveLocalData/buddies.bin', 'wb') as fp:
                pickle.dump(buddies, fp)
        except FileNotFoundError:
            print('Erro ao salvar buddy. Arquivo nao encontrado.')
        
    
         