class HeiAsyst(object):

    def __init__(self, username):
        self.username = username

    def setUsername(self, username):
        self.username = username

# inheritance
class Account(HeiAsyst):

    #override
    def setUsername(self, username):
        self.username = username.replace(username, 'ETY')

    def setName(self, name):
        self.name = name
    
    #encapsulation
    def _setPassword(self, password):
        self.password = password.replace('a', '*')

    def getAccount(self):
        return print('Nama:{}, Username: {}, Password: {}'.format(self.name, self.username, self.password))

# inheritance
class Attendance(HeiAsyst):
    def setKehadiran(self, kehadiran):
        self.kehadiran = kehadiran

    def getKehadiran(self):
        return print('Username: {}, Kehadiran: {}'.format(self.username, self.kehadiran))


account = Account('PMR')
account.setName('Made Rezananda Putra')
account.setUsername('PMR')
account._setPassword('rezananda26')
account.getAccount()

attendance = Attendance('PMR')
attendance.setKehadiran('Hadir')
attendance.getKehadiran()