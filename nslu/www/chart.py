#!/usr/bin/env python
from html import *

printHTTPHeader()

print """<HTML>
<BODY bgcolor="#FFFFFF">

<OBJECT classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
	codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" 
	WIDTH="400" 
	HEIGHT="300" 
	id="charts" 
	ALIGN="">
<PARAM NAME=movie VALUE="charts.swf?library_path=charts_library&xml_source=sample.xml">
<PARAM NAME=quality VALUE=high>
<PARAM NAME=bgcolor VALUE=#ffffff>
<param name="vmode" value="transparent">

<EMBED src="charts.swf?library_path=charts_library&xml_source=sample.xml"
       quality=high 
       bgcolor=#ffffff  
       WIDTH="400" 
       HEIGHT="300" 
       NAME="charts" 
       ALIGN="" 
       swLiveConnect="true" 
       vmode=transparent
       TYPE="application/x-shockwave-flash" 
       PLUGINSPAGE="http://www.macromedia.com/go/getflashplayer">
</EMBED>
</OBJECT>

</BODY>
</HTML>"""
