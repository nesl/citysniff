import os, sys

class Mote:

    def getPort(self):
        """
        Returns the port on which the mote is connected.
        Currently this just returns a string. But it could
        be more sofisticated, if necessary.
        """
        return "/dev/ttyUSB0"

    def isConnected(self):
        """
        Checks if a base mote is conected to the NSLU's USB ports.
        """
        f = os.popen("cat /proc/bus/usb/devices | grep tmote")
        lines = f.readlines()
        if len(lines) != 1:
            return False
        else:
            return True
        
    def _program(self, filename, port):
        """
        Programs a mote connected to <port> with the image pointed to by <filename>.
        Programming the mote doesn't currently work. No idea why :(
        """

        f = os.popen('tos-bsl --telosb -c %s -r -e -I -p %s 2>&1'%(port, filename))
        while 1:
            line = f.readline()
            if not line:
                break
            if line.lower().find("error") >= 0:
                print '<font color="red">%s</font><br />'%(line,)
                print '<font color="red">%s</font><br />'%(f.readline(),)
                return False
                
            else:
                print line+"<br />"
            sys.stdout.flush()
        ret = f.close()
        if ret == None:
            return True
        return False

    def programBaseMote(self):
        """
        Programs an attached mote with the standard image for the base mote in /var/cache/main.ihex.out-0
        """
        if self.isConnected():
            return self._program("/var/cache/main.ihex.out-0", self.getPort())

        return False
