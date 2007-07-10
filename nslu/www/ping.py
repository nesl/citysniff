import os

class Ping:

    def __init__(self, hosts=('sensorscope.epfl.ch', )):
        self._hosts = hosts

    def ping(self):
        for host in self._hosts:
            for i in range(5):
                #should return 0 if ping succeeded
                ret = os.system("ping -c 1 %s > /dev/null"%(host,))
                if not ret:
                    return True
        return False
