#!/usr/bin/env python

import cgi, sys
from html import *
from mote import *

configfile = '/etc/citysniff.conf'

def main():
    printHTTPHeader()
    printHeader("Configuration 3")
    form = cgi.FieldStorage()

    if not (form.has_key("action") and \
            form["action"] != "searchmote"
            ):
        print '<p><font color="red">Something went wrong. Please start from the <a href="index.py">beginning</a>!</font>.</p>'
    else:
        m = Mote()
        if not m.isConnected():
            print '<p><font color="red">I can not find the mote. Please detach and attach it again. Then, click on continue.</font></p>'
            print '<form action="config2.py" method="post"><input type="submit" value="Continue" /><input type="hidden" name="action" value="searchmote" /></form>'
        else:
            print '<p>Attempting to program the mote. This may take a while.</p>'
            sys.stdout.flush()
            if not m.programBaseMote():
                print '<p><font color="red">Programming failed!</font></p>'
            else:
                print '<p><font color="green">Programming successfull!</font></p>'
                print '<p>Now comes the connectivity test for the sensing mote.... not implemented yet.</p>'
                print '<p>Go <a href="index.html">home</a>.</p>'
    printFooter()


if __name__=="__main__":
    main()
