#!/usr/bin/env python

from html import *

def main():
    h = Html()
    h.setTitle("Statistics")
    h.setWhereOnPage((('/statistics.py', 'statistics'), ))
    h.setMainMenu([("#", "configure the hardware", "configure"), 
		   ("#", "show recorded data", "data"), 
		   ("/statistics.py", "show hardware statistics", "statistics"),
		   ])
    h.setLeftMenu(
	{'boxes': [
		{'headbox': 'Hardware', 'menuentries': [('#load', 'System Load', 'Load'), 
							('#memory', 'Memory', 'Memory')]}, 
		],
	 'dyncontents': [""]
	 })
    h.setBody("""
<h2><a name='load' />Load</h2>
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
	codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" 
	width="400" 
	height="300" 
	id="charts" 
	align="">
<param name="movie" value="charts.swf?library_path=charts_library&xml_source=sample.xml">
<param name="quality" value="high">
<param name="bgcolor" value="#ffffff">
<param name="wmode" value="transparent">

<embed src="charts.swf?library_path=charts_library&xml_source=sample.xml"
       quality="high" 
       bgcolor="#ffffff"  
       width="400" 
       height="300" 
       name="charts" 
       align="" 
       swLiveConnect="true" 
       wmode="transparent"
       type="application/x-shockwave-flash" 
       pluginspage="http://www.macromedia.com/go/getflashplayer">
</embed>
</object>
<h2><a name='memory' />Memory</h2>
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
	codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,0,0" 
	width="400" 
	height="300" 
	id="charts" 
	align="">
<param name="movie" value="charts.swf?library_path=charts_library&xml_source=sample.xml">
<param name="quality" value="high">
<param name="bgcolor" value="#ffffff">
<param name="wmode" value="transparent">

<embed src="charts.swf?library_path=charts_library&xml_source=sample.xml"
       quality="high" 
       bgcolor="#ffffff"  
       width="400" 
       height="300" 
       name="charts" 
       align="" 
       swLiveConnect="true" 
       wmode="transparent"
       type="application/x-shockwave-flash" 
       pluginspage="http://www.macromedia.com/go/getflashplayer">
</embed>
</object>
""")
    h.setRightBox([('News 8/21/06', 'Creating website for CitySniff'),
		   ])
    h.setFooter("""&copy; 2006 LCAV &nbsp;""")
		     
    h.printHtml()


if __name__== "__main__":
    main()
