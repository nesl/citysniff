#!/usr/bin/env python
import os
from html import *
from ping import *

configfile = '/etc/citysniff.conf'

def configureSystem():
    printHTTPHeader()
    printHeader("Configuration")
    print """
    <p>This is the first time you started your CittySniff equippment. Therefore, we will go through a very simple configuration to setup everything.</p>
    """
    
    p = Ping()
    if not p.ping():
        print """
        <p><b><font color="red">Unfortunately we can not reach the CittySniff servers. Please check your internet connectivity and come back to this website.</fond></b></p>
"""
    else:
        print """
        <p>Internet Connection: <font color="green">OK</font></p>
"""
        print """
        <p>We now need some basic information from you. All fields are required.</p>

        <form action="config1.py" method="post">
        <table border="0">
        <tr>
          <td>Your Name</td><td><input type="text" name="name" /></td>
        </tr>
        <tr>
          <td>Your Address </td><td><input type="text" name="address" /></td>
        </tr>
        <tr>
          <td>Your ZIP code </td><td><input type="text" name="zip" /></td>
        </tr>
        <tr>
          <td>Your email </td><td><input type="text" name="email"/></td>
        </tr>
        <tr>
          <td>A password </td><td><input type="text" name="password"/></td>
        </tr>
        <tr>
          <td>Reenter password </td><td><input type="text" name="password_check"/></td>
        </tr>
        </table>
        <p>
        <input type="submit" value="continue">
        </p>
        </form>
"""
    printFooter()

def main():
    h = Html()
    h.setTitle("Home")
    h.setWhereOnPage((('', ''), ))
    h.setMainMenu([("#", "configure the hardware", "configure"), 
		   ("#", "show recorded data", "data"), 
		   ("/statistics.py", "show hardware statistics", "statistics"),
		   ])
    h.setLeftMenu(
	{'boxes': [
		{'headbox': 'References', 'menuentries': [('http://sensorscope.epfl.ch', 'Sensorscope is a nice project', 'SensorScope'), ('http://www.epfl.ch', 'Ecole Polytechnique Federal de Lausanne', 'EPFL')]}, 
		{'headbox': 'Others', 'menuentries': [('http://nesl.ee.ucla.edu', 'Networked Embedded Systems Lab', 'NESL')]}, 
		],
	 'dyncontents': ["Some dynamic content", "and some more..."]
	 })
    h.setBody("""Nothing here to see yet""")
    h.setRightBox([('News 8/21/06', 'Creating website for CitySniff'),
		   ])
    h.setFooter("""&copy; 2006 LCAV &nbsp;""")
		     
    h.printHtml()

if __name__== "__main__":

    if not os.path.isfile(configfile):
        configureSystem()
    else:
        f = file(configfile)
        if len(f.readlines()) < 2:
            configureSystem()
        else:
            main()

