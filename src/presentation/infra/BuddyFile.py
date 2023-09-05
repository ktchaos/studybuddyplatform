import pickle

class BuddyFile():

    def loadBuddies():
        try:
            with open('./src/presantation/infra/data/buddies.bin', 'rb') as fp:
                buddy_list = pickle.load(fp)
                return buddy_list
        except FileNotFoundError:
            print('Arquivo nao encontrado.')
            return []

    def saveBuddies(buddies):
        try:
            with open('./src/presentation/infra/data/buddies.bin', 'wb') as fp:
                pickle.dump(buddies, fp)
        except FileNotFoundError:
            print('Erro ao salvar buddy. Arquivo nao encontrado.')
        
    
         