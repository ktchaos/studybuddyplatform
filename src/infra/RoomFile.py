import pickle

class RoomFile():
    # Carrega salas salvos no arquivo
    def loadRooms():
        try:
            with open('./src/infra/saveLocalData/rooms.bin', 'rb') as fp:
                roomList = pickle.load(fp)
                return roomList
        except FileNotFoundError:
            # se o arquivo nao existe, retorna uma lista vazia
            print('Arquivo de sala nao encontrado.')
            return []

    def addRooms(rooms):
        try:
            # salva a lista atualizada no arquivo
            with open('./src/infra/saveLocalData/rooms.bin', 'wb') as fp:
                pickle.dump(rooms, fp)
        except FileNotFoundError:
            print('Erro ao salvar sala. Arquivo nao encontrado.')
        
    
         