import time

def printHTTPHeader():
    print 'Content-Type: text/html \n'
    
def printHeader(title=""):
    print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
  <head>
    <title>CittySniff - %s</title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <link rel="stylesheet" href="style.css" type="text/css" />
  </head>
  <body>
<br />
<table border="0" cellspacing="0" cellpadding="0" width="100%%">
  <tr> 
    <td colspan="3" class="pos1" height="55" valign="middle"> 
      <div class="topbox"><h2>CitySniff. %s.</h2></div>
    </td>
  </tr>
  <tr><td><br /></td></td>
  <tr> 
  <td width="10"></td>
  <td valign="top" class="mainbox"> 

"""%(title, title)

def printHTMLHeader(title=""):
    print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<head>
<title>CitySniff</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" href="style.css" type="text/css" />
</head>
"""

def printHTMLBody():
    print """
<body>
<br />
<table border="0" cellspacing="0" cellpadding="0" width="100%">
  <tr> 
    <td colspan="3" class="pos1" height="55" valign="middle"> 
      <div class="topbox"><h2>CitySniff. Sensing the Urban Environment.</h2></div>
    </td>
  </tr>
"""

def printHTMLMainMenu():
    print """
  <tr> 
  <td>
   <table width="100%" border="0" cellpadding="0" cellspacing="0" class="topnav">
    <tr>
  	      <td align="left" class="head">
		  	&nbsp;// <a href="#" title="back to the homepage">home</a> 
           		   / <a href="#" title="you are here">template</a>
		  </td>
    	  <td align="right"> 
			<a href="#" class="topmenu" title="configure the hardware">&nbsp;::configure::&nbsp;</a><a href="#" class="topmenu" title="show recorded data">&nbsp;::data::&nbsp;</a><a href="#" class="topmenu" title="show hardware statistics">&nbsp;::statistics::&nbsp;</a>
		  </td>
	</tr>
   </table>
   </td>
  </tr>
"""

def printHTMLLeftMenu():
    print """
  <tr> 
    <td> 
      <table width="100%" border="0" cellpadding="0" cellspacing="0">
        <tr> 
          <td valign="top" width="150"> <br />
		  	<div>
          	  <div class="headbox">References</div>
			  <a class="leftmenu" href="http://www.oswd.org" title="open source web design">OSWD</a> 
              
              <a class="leftmenu" href="http://validator.w3.org" title="ensure solid code with an html validator">W3 Validator</a> 
               
			  <a class="leftmenu" href="http://www.webmonkey.com" title="pick up some skills from the monkey">Webmonkey</a> 
                          
              <a class="leftmenu" href="http://www.w3schools.com" title="excellent reference for css">W3 Schools</a> 
			  
			  <a class="leftmenu" href="http://www.mozilla.org" title="gotta have cross browser compatibility">Mozilla</a> 
              
			  <br />
			  
              <div class="headbox">Inspirations</div>
              <a class="leftmenu" href="http://www.waferbaby.com" title="where i found the idea for this menu">Waferbaby</a> 
             
              <a class="leftmenu" href="http://oswd.org/viewdesign.phtml?id=553" title="pretension by krsna77">Pretension!</a> 
              
              <a class="leftmenu" href="http://oswd.org/viewdesign.phtml?id=559" title="libra by whompy">Libra</a> 
              
			  <a class="leftmenu" href="http://www.howitworks.com" title="somtimes i actually work here">How it Works</a> 
			  
			  <a class="leftmenu" href="http://epitonic.com" title="can't do anything without music">Epitonic</a> 
			  
			  <a class="leftmenu" href="http://themes.freshmeat.net/" title="everyone has their own style">Themes.org</a> 
			  
			  <br />
			  <div class="dynacontent">
			  Questions or Comments? Advice for me or from me? Please <a href="http://www.oswd.org/email.phtml?user=Phlash" class="dash" title="email the author">email me.</a>
			  </div>	
              
            </div>
          </td>
          <td valign="top"> <br />
            <table border="0" cellspacing="0" cellpadding="0" width="100%">
              <tr> 
                <td width="10"></td>
                <td valign="top" class="mainbox"> 
"""

def printHTMLBody():
    print """
				  <h3>The Power of CSS</h3>
				  <p>
				  The colors for every element on the page are based on 6 hex values which only appear once in the 
				  entire file, you edit these values and you have an entirely new theme for this design.
				  </p>
                  <p>
				  Pixel dimensions are specified only a few times (where I had to), but for the most part everything 
				  is relative to the fonts you have and the screen resolution you are using. This gives the page as much 
				  width as it can get while the fonts and layout have as much compatibility as possible.
				  </p>
				  <p>&nbsp;</p>
				  
                  <h3>The Evolution of this Design</h3>
                
                  <p>
				  I'm not exactly sure where it all started, but I think the first idea I found for this 
				  was from <a href="http://www.waferbabay.com" title="visit waferbaby" class="dash">waferbaby</a> where I realized that you could actually make rollovers, by specifying 
				  different background colors in a style sheet.
				  </p>
                  <p>
				  The layout for this is very common, but I guess I settled on it after looking at designs 
				  like Libra (by <a class="dash" href="http://oswd.org/userinfo.phtml?user=whompy" title="visit whompy's page on oswd">whompy</a>) and 
				  Pretension (by <a class="dash" href="http://oswd.org/userinfo.phtml?user=krsna77" title="visit krsna77's page on oswd">krsna77</a>) for a 
				  while. I also referred to Pretension for a lot of the style sheet information, mostly the 
				  fonts and the idea of making fonts relative sizes (%) rather than using specific sizes.
				  </p>
                  <p>
				  Two of the most challenging aspects of this whole thing were getting everything to look the same 
				  in both IE and Mozilla and setting up the style sheet so it had some flexibility. This was of course most difficult with the menus. Mozilla doesn't have quite 
				  as good of support for css as IE, but I was really quite surprised how well it all worked out in the 
				  end. In fact, when I converted the html to xhtml I started having problems with IE and all of a sudden Mozilla was working perfectly. 
				  The biggest difference was made when I specified the left menu links to display as block elements in 
				  the style sheet. This is what was done on the <a href="http://www.waferbabay.com" title="visit waferbaby" class="dash">waferbaby</a> website.
				  </p>



"""

def printHTMLRightMenu():
    print """
                </td>
                <td width="145" valign="top" class="dynabox">Today is 6.23.02
				<br />
				<br />
				<div class="headbox">&nbsp;Comment by <a class="dash" href="#" title="user">User</a></div>
				<div class="dynacontent">The whole "United We Stand" mantra really gets to me. Analyze "United States of America", broken down it's like united individual states, we're not one communistic body, were a community of individuals; unity in liberty. Divided we are Free!</div>

				
				<div class="headbox">&nbsp;Comment by <a class="dash" href="#" title="guest">Guest</a></div>
				<div class="dynacontent">With the current state of the anti-trust trial and Lindows PCs being sold at Walmart, I can't see any possible future for a Microsoft dominated world.</div>

								
				<div class="headbox">&nbsp;Comment by <a class="dash" href="#" title="admin">Admin</a></div>
				<div class="dynacontent">Building this has been an excellent learning experience and after studying XML and XSL, I know stylesheets will be the future and content will finally be independent.</div>

				
				</td>
              </tr>
            </table>
			<br />
          </td>
        </tr>
      </table>
    </td>
  </tr>	
"""

def printHTMLFooter():
    print """
  <tr class="pos1"> 
    <td height="20" colspan="2" class="head" align="right">&copy; 2006 LCAV &nbsp;</td>
  </tr>
</table>
</body>
</html>
"""

def printFooter():
    print """
  </td>
  </tr>
  </table>
  </body>
</html>
"""

class Html:
    def __init__(self):
	self.html = """Content-Type: text/html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
<head>
<title>CitySniff - __TITLE__ </title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" href="style.css" type="text/css" />
</head>
<body>
<br />
<table border="0" cellspacing="0" cellpadding="0" width="100%">
  <tr> 
    <td colspan="3" class="pos1" height="55" valign="middle"> 
      <div class="topbox"><h2>CitySniff. Sensing the Urban Environment - __TITLE__</h2></div>
    </td>
  </tr>
  <tr> 
  <td>
   <table width="100%" border="0" cellpadding="0" cellspacing="0" class="topnav">
    <tr>
      <td align="left" class="head">
      __WHEREONPAGE__
      </td>
      <td align="right"> 
      __MAINMENU__
      </td>
	</tr>
   </table>
   </td>
  </tr>
  <tr> 
    <td> 
      <table width="100%" border="0" cellpadding="0" cellspacing="0">
        <tr> 
          <td valign="top" width="150"> <br />
	    <div>
	    __LEFTMENU__
            </div>
          </td>
          <td valign="top"> <br />
            <table border="0" cellspacing="0" cellpadding="0" width="100%">
              <tr> 
                <td width="10"></td>
                <td valign="top" class="mainbox"> 
		__BODY__
                </td>
                <td width="145" valign="top" class="dynabox">
		__RIGHTBOX__
		</td>
              </tr>
            </table>
	    <br />
          </td>
        </tr>
      </table>
    </td>
  </tr>	
  <tr class="pos1"> 
    <td height="20" colspan="2" class="head" align="right">__FOOTER__</td>
  </tr>
</table>
</body>
</html>
"""
    def setTitle(self, title):
	self.html = self.html.replace("__TITLE__", title)

    def setWhereOnPage(self, where):
	if isinstance(where, list) or isinstance(where, tuple):
	    s = '&nbsp;// <a href="/" title="back to the homepage">home</a>' 
	    for e in where:
		s += ' / <a href="%s" title="%s">%s</a>'%(e[0], e[1], e[1])
	    where = s
	self.html = self.html.replace("__WHEREONPAGE__", where)

    def setMainMenu(self, mainmenu):
	""" mainmenu can either be a string or a list/tuple of list/tuples. The second list/tuples must
	contain two strings each. The first one is the long description, the second one the name of the
	menu entry.

	e.g. mainmenu = [('hardware configuration', 'configuration'), ('shows statistics', 'statistics')]
	"""
	if isinstance(mainmenu, list) or isinstance(mainmenu, tuple):
	    template = '<a href="%s" class="topmenu" title="%s">&nbsp;::%s::&nbsp;</a>'
	    s = ''
	    for e in mainmenu:
		s += template%e
	    mainmenu = s
	self.html = self.html.replace("__MAINMENU__", mainmenu)

    def setLeftMenu(self, leftmenu):
	""" Example leftmenu:
	leftmenu = {'boxes': [{'headbox': 'References', 'menuentries': [('http://sensorscope.epfl.ch', 'Sensorscope is a nice project', 'SensorScope'), ('http://www.epfl.ch', 'Ecole Polytechnique Federal de Lausanne', 'EPFL')]}, 
	                     {'headbox': 'Others', 'menuentries': [('http://nesl.ee.ucla.edu', 'Networked Embedded Systems Lab', 'NESL')]}, 
			     ],
                    'dyncontents': ["Some dynamic content", "and some more..."]
                   }
	"""
	if isinstance(leftmenu, dict):
	    headbox = '<div class="headbox">%s</div>'
	    menuentry = '<a class="leftmenu" href="%s" title="%s">%s</a>'
	    s = ''
	    for box in leftmenu['boxes']:
		s += headbox%box['headbox']
		for me in box['menuentries']:
		    s += menuentry%me
		s += '<br />'
	    for dyncont in leftmenu['dyncontents']:
		s += '<div class="dynacontent">%s</div>'%dyncont
	    leftmenu = s

	self.html = self.html.replace("__LEFTMENU__", leftmenu)

    def setBody(self, body):
	self.html = self.html.replace("__BODY__", body)

    def setRightBox(self, rightbox):
	if isinstance(rightbox, list) or isinstance(rightbox, tuple):
	    s = "Today is %s <br /><br />"%(time.strftime("%m/%d/%y"), )
	    header = '<div class="headbox">&nbsp;%s</div>'
	    box = '<div class="dynacontent">%s</div>'
	    for e in rightbox:
		s += header%e[0]
		s += box%e[1]
	    rightbox = s
	self.html = self.html.replace("__RIGHTBOX__", rightbox)

    def setFooter(self, footer):
	self.html = self.html.replace("__FOOTER__", footer)

    def printHtml(self):
	print self.html
