from .CommandIF import Command

#implementacao do comando
class LoginExternalCommand(Command):

    def __init__(self, facade, username, password):
            self.facade = facade
            self.username = username
            self.password = password

    def execute(self):
        self.facade.loginVm.currentBuddies = self.facade.managerVm.currentBuddies
        return self.facade.loginVm.authenticate(self.username, self.password)