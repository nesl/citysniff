#!/usr/bin/env python

import cgi
from html import *

configfile = '/etc/citysniff.conf'

def main():
    printHTTPHeader()
    printHeader("Configuration 2")
    form = cgi.FieldStorage()
    if not (form.has_key("name") and \
            form.has_key("address") and \
            form.has_key("zip") and \
            form.has_key("email") and \
            form.has_key("password") and \
            form.has_key("password_check") \
            ):
        print '<p><font color="red">Something went wrong. Please start from the <a href="index.py">beginning</a>!</font> You might not have filled out all the fields. Note that all of the are required for a successfull configuration.</p>'
    elif "@" not in form["email"].value:
        print '<p><font color="red">You entered a non valid email address!</font> It is important that your email address is correct, because it is used to identify your setup in the CitySniff database.</p>'
    elif form["password"].value != form["password_check"].value:
        print '<p><font color="red">Passwords do not match!</font> Please go back and make sure that the two passwords you entered are the same."%s" "%s"</p>'%(form["password"].value, form["password_check"].value)
    elif len(form["password"].value) < 6:
        print '<p><font color="red">Your password is too short!</font> Your password should be at least 6 characters long.</p>'

    else:
        #we have a valid email, the passwords entered are the same and it is at least 6 characters long.
        
        try:
            conffile = file(configfile, 'w')
            conffile.write("name=%s\n"%(form["name"].value,))
            conffile.write("address=%s\n"%(form["address"].value,))
            conffile.write("zip=%s\n"%(form["zip"].value,))
            conffile.write("email=%s\n"%(form["email"].value,))
            conffile.write("password=%s\n"%(form["password"].value,))
            conffile.close
        except Exception, e:
            print '<font color="red">Could not open configuration file. Reason: %s</font>'%(str(e),)
        else:
            print "<p>Data successfully stored in the configuration file.</p>"
            print "<p>Next, we will configure the basestation mote. Please plug in the mote into the USB port. When you are ready, click the <b>Continue</b> button.</p>"
            print '<form action="config2.py" method="post"><input type="submit" value="Continue" /><input type="hidden" name="action" value="searchmote" /></form>'
    printFooter()


if __name__=="__main__":
    main()
