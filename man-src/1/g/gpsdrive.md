---
title: "gpsdrive(1)"
name: "gpsdrive"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsdrive/"
description: "gpsdrive – displays GPS position on a map"
---

<h2>NAME</h2>
<p> gpsdrive &#8211; displays GPS position on a map</p>
<h2>SYNOPSIS</h2>
<p> <code>gpsdrive [options]</code> </p>
<h2>About this manual page</h2>
<p> This manual page explains the basic functions of <code>GpsDrive</code> 2.10 and additional information regarding map setup and interfacing with support software. </p>
<p> Within <code>GpsDrive</code> nearly all buttons have tooltips and there is also a HELP window describing the usage of mouse buttons and keyboard shortcuts. </p>
<p> For additional information concerning advanced topics consult the specialized README files, e.g. README.kismet, etc. </p>
<h2>DESCRIPTION</h2>
<p> <code>GpsDrive </code> is a car (bike, ship, plane, foot) navigation system. It will display your position on a map, record your track, and a number of other handy functions. </p>
<p> <code>GpsDrive</code> connects to a GPS receiver and displays your position on a zoomable map. The maps are auto-selected depending on your position. You can choose the preferred map scale, which the program then tries to match from the available maps. Basic worldwide maps are provided and tools are included to help you add your own localized maps. </p>
<p> <code>GpsDrive</code> will work with the vast majority of GPS receivers which output NMEA sentences to a serial device, and any USB GPS binary protocol known to the <code>Gpsd</code> software, which handles the back-end communication for <code>GpsDrive</code>. See the <code>Gpsd</code> website (<i><a rel="nofollow" href="http://gpsd.berlios.de">http://gpsd.berlios.de</a></i>) for an extensive list of GPS receivers known to work with that software. In most cases your GPS will &quot;just work&quot;. </p>
<p> &quot;<code>Gpsd</code> is a service daemon that monitors one or more GPSes attached to a host computer through serial or USB ports, making all data on the location/course/velocity of the sensors available to be queried on a TCP port of the host computer. With <code>gpsd</code>, multiple GPS client applications (such as navigational and wardriving software) can share access to GPSes without contention or loss of data.&quot; </p>
<p> You must install and launch <code>gpsd</code> before running <code>GpsDrive</code>. </p>
<h2>DISCLAIMER</h2>
<p> <code>Do not use GpsDrive as a primary means of navigation!</code><br />
 <code>Keep your eyes on the road and hands on the wheel.</code> </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License (GPL) for more details. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Displays a short help message.</p>
<dt><code>-e, &#8211;embedded</code></p>
<dd> Don&#8217;t show the GUI; for use in external GTK apps.</p>
<dt><code>-f, &#8211;force-position</code></p>
<dd> Force display of position even if the GPS fix is invalid. Before a GPS has a fix it often reports its position as 0,0. And if it has lost a fix some makes of GPS will repeat the last known position together with a fix-is-bad indicator. Normally (without this flag) <code>GpsDrive</code> skips plotting these points. Useful for debugging.</p>
<dt><code>-i, &#8211;ignore-checksum</code></p>
<dd> Ignore NMEA checksum. (risky, only for broken GPS receivers)</p>
<dt><code>-p, &#8211;explore-mode</code></p>
<dd> Start in Explore Mode. This will let you explore around your maps independently of your GPS position (or lack thereof).</p>
<dt><code>-s, &#8211;nosplash</code></p>
<dd> Don&#8217;t show the startup splash screen.</p>
<dt><code>-t, &#8211;touchscreen</code></p>
<dd> Set this special mode if you only have a single mouse button, for example when using <code>GpsDrive</code> on a touchscreen display.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Displays some basic debug information to the terminal as the program runs.</p>
<dt><code>-x, &#8211;use-DBUS</code></p>
<dd> Use DBUS for communication with <code>gpsd</code>; this disables socket communication.</p>
<dt><code>-A, &#8211;alt-offset=</code><i>&lt;OFFSET&gt;</i></p>
<dd> Adjust the displayed altitude by adding this value.</p>
<dt><code>-B, &#8211;gpsd-server=</code><i>&lt;SERVER&gt;</i></p>
<dd> Server name of the NMEA server. You can connect your GPS receiver to a remote <i>host</i> which is running <code>gpsd</code> and display the position on your local machine.</p>
<dt><code>-C, &#8211;config-file=</code><i>&lt;FILE&gt;</i></p>
<dd> Set this if you wish to use an alternative configuration file.</p>
<dt><code>-D, &#8211;debug=</code><i>&lt;LEVEL&gt;</i></p>
<dd> Set the debugging level. A level of 0 will show no debug information, while a level of 100 will show <code>a lot</code> of debugging information. If you have problems or program crashes, set this high enough to display relevant information send this output to the authors. See also the <code>BUGS</code> section below.</p>
<dt><code>-F, &#8211;friends-server=</code><i>&lt;SERVERFILE&gt;</i></p>
<dd> Select a friends server to exchange position information with other people, e.g. <i>friendsd.gpsdrive.de</i>. You can also set this from the Preferences/Friends menu. You can start your own friends server with the included <code>friendsd</code> program. More details are in the <code>FRIENDSD</code> section below.</p>
<dt><code>-G, &#8211;geometry=</code><i>&lt;GEOMETRY&gt;</i></p>
<dd> Specify the window geometry, e.g. 800&#215;600.</p>
<dt><code>-M, &#8211;gui-mode=</code>[<i>car</i>|<i>pda</i>|<i>desktop</i>]</p>
<dd> Set GUI mode. The default layout is &#8216;<i>desktop</i>&#8216;. <i>Car</i> modes sets up the display in a fullscreen mode suitable for use with a small LCD touchscreen. <i>PDA</i> mode dedicates even more screen real-estate to the map, controls are hidden behind tabs.</p>
<dt><code>-N, &#8211;nmeaout=</code><i>&lt;FILE&gt;</i></p>
<dd> Set a serial device, PTY master, or file to send NMEA sentences to. This is useful if you use <code>GpsDrive</code> in simulation mode to provide other GPS applications with test data.</p>
<dt><code>-S, &#8211;screenshot=</code><i>&lt;PATH&gt;</i></p>
<dd> Take auto-screenshots of different GUI windows then exit. Image files will be saved to the specified <i>path</i>. Don&#8217;t touch gpsdrive while this is running!</p>
<dt><code>-T, &#8211;run-test</code></p>
<dd> Run some internal unit tests and then exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the program version together with the SVN revision of the main gpsdrive.c source. If you send a bug report, also include this output.</p>
<dt><code>&#8211;display=</code><i>&lt;DISPLAY&gt;</i></p>
<dd> The X-Window display to use. </p>
</dl>
<h2>CONNECTING A GPS RECEIVER</h2>
<p> <code>Start GPSD</code><br />
 This program runs as daemon in background and provides a server which sends the GPS data on port number 2947. You can download and learn more about <code>gpsd</code> at <i><a rel="nofollow" href="http://gpsd.berlios.de">http://gpsd.berlios.de</a></i>. </p>
<p> Once <code>gpsd</code> is running you can monitor the raw NMEA output of your GPS with <code>telnet localhost 2947</code> and after the connection is made hit the <code>R</code> key to see the NMEA sentences. You can use the <code>xgps</code> program that comes with <code>gpsd</code> for a more comprehensive test. </p>
<p> If you have connected a GPS receiver, and are successfully communicating with it, you will see GpsDrive&#8217;s signal strength indicator turn from red to green. By clicking on the signal strength indicator you can open the <i>Satellite Info</i> window which will show you information about the satellites in view. </p>
<p> To calculate a 2D position the GPS must have at least 3 satellites in view. To calculate altitude you need at least 4 satellites. The antenna of your GPS receiver must have free sight to the sky, so you cannot expect to use it indoors. More satellites gives you a better accuracy. </p>
<p> If your receiver can not see enough satellites with a usable signal, the signal level indicator is red. If your signal is ok and gives a valid position, the <i>Satellite Info</i> indicator is green. </p>
<p> You can restart the connection to <code>gpsd</code> in the GPS tab of the <i>Preferences</i> menu. </p>
<h2>USAGE</h2>
<p> Start GpsDrive as a normal user with: <code>gpsdrive</code> from your shell, if you want another language see the <i>LOCALISATION</i> section. </p>
<p> On some distributions you may find a &quot;<code>GpsDrive</code>&quot; entry in your Gnome or KDE menu. </p>
<p> It is important that you have installed GpsDrive as root, so it can find the necessary files. <code>Don&#8217;t start GpsDrive as root!</code> </p>
<p> You can use GpsDrive without a GPS device connected. GpsDrive can automatically start in <code>Simulation mode</code> if no working GPS receiver is connected and no <code>gpsd</code> is running. The GPS signal level indicator is replaced with a message indicating the mode. </p>
<p> In simulation mode the pointer will move by itself on the map towards the target position. It may be switched permanently on or off in the <i>Preferences</i> menu. </p>
<h3>Modes Of Operation</h3>
<p> <code>GpsDrive</code> operates in three modes: </p>
<p> <code>Normal mode:</code><br />
 This mode is entered if you have a GPS receiver connected. The cursor is at the position your GPS receiver sends.<br />
 Black and red arrows show your position on the map. The <code>red arrow</code> points to your selected target (aka &quot;<i>Bearing</i>&quot;), and the <code>black arrow</code> shows the direction in which you are moving (aka &quot;<i>Heading</i>&quot;).<br />
 When the GPS is not sending a valid position the arrows blink. </p>
<p> <code>Simulation mode</code><br />
 If GpsDrive does not find a GPS receiver when the program starts, it shows the last known position and the cursor will move towards the target you set. You can set the target with a right-mouse click on the map or by selecting a waypoint from the <i>Find</i> dialog. The target appears as a cross-hair and is available in all modes. </p>
<p> <code>Explore mode</code><br />
 In this mode you can temporarily change the cursor position for looking around and jumping to other positions (e.g. for downloading maps). The lat/lon position shown in the dashboard is that of the current <code>mouse position</code>.<br />
 This mode is selected by ticking the &quot;Explore mode&quot; box in the <i>Map Control</i> window, or if you &quot;Jump to POI&quot; in the <i>Find</i> window. The <i>Jump</i> button simply jumps to the current target, so it is useful to move the target to a waypoint/POI first by selecting one from the list.<br />
 In this mode GpsDrive <code>does not show your real position</code> and the positioning arrows are replaced with a box.<br />
 You can relocate your position with a simple left-mouse click on the map or with the arrow keys (including diagonals on the keypad). Maps are automatically scrolled or load the next map when you click near the border.<br />
 To leave Explore Mode untick the &quot;Explore mode&quot; entry in the <i>Map Control</i> window, or middle or right-mouse click on the map. If a right-mouse click is used the target is reset to that position in the process. </p>
<p> You can change the preferred map scale with mouse wheel, or if there is no mouse wheel, with Shift-left and right mouse click. This works from any mode. </p>
<p> Please have a look in the <code>Help</code> menu in GpsDrive to learn more about available keyboard shortcuts and mouse functions. </p>
<h2>MAPS</h2>
<h3>OpenStreetMap Maps</h3>
<p> GpsDrive now supports OSM maps with the help of the Mapnik renderer. To activate this mode you have to build GpsDrive with the Mapnik option enabled. </p>
<h3>Map Download</h3>
<p> You can easily download maps from the internet with the <code>Download</code> tool. This is found in the Options -&gt; Maps menu. A preview of already downloaded maps near to the current preferred mapscale are shown as yellow rectangles drawn over the map. The area to be downloaded is drawn as a green rectangle over the map. Reposition the area to be downloaded with a left-mouse click. </p>
<p> There is also a program called <i>gpsfetchmap.pl</i> provided with GpsDrive which can be used to automatically download a series of maps covering a larger area.<br />
 <code>Please consider the copyright information and terms of service</code> of map providers if you want to use their maps! <code>Do not misuse this service by downloading more maps than you need!</code> You will risk being blocked by these servers, and possibly cause trouble for the GpsDrive project. </p>
<p> If you must access the internet via a proxy server, set the <i>HTTP_PROXY</i> or <i>http_proxy</i> environment variable to a value like <i><a rel="nofollow" href="http://proxy.provider.com:3128">http://proxy.provider.com:3128</a></i> where 3128 in this example is the proxy port. </p>
<h3>About Maps</h3>
<p> GpsDrive stores an index of your maps in a file called &quot;map_koord.txt&quot; in your ~/.gpsdrive/maps/ directory. You can use another directory for your maps if you like, to change this set the appropriate directory in the Preferences menu. </p>
<p> Here is a sample of its contents: </p>
<p> top_WORLD.jpg 0.00000 0.00000 88226037<br />
 map_file0000.gif 53.60751 10.01145 3160000<br />
 map_file0001.gif 43.08210 12.24552 3160000<br />
 map_file0002.gif 49.81574 9.71454 7900000<br />
 map_file0003.gif 47.72837 14.46487 592500 </p>
<p> The first column is the filename, then comes the latitude, the longitude and the scale of the map. Typical scales for all of Europe might be 1:10,000,000, and 1:100,000 for a town. To see detailed streets in a city, choose a scale like 1:10,000 or 1:5,000. </p>
<p> You can figure out the exact &quot;scale&quot; factor by meters/pixel * 2817.947378. The 2817 number is derived from some ancient screen dpi converted into pixels/meter. </p>
<p> GpsDrive selects the map with the best scale for your position. So you will want to get maps of different scales. e.g. You should have maps for Europe, Austria, and Vienna if you want to drive in Vienna. </p>
<h3>European decimal place:</h3>
<p> While the decimal points in way.txt must always be a dot (&#8216;.&#8217;), in map_koord.txt &#8216;.&#8217; or &#8216;,&#8217; are possible. If you download maps from within the program, GpsDrive writes the map_koord.txt respecting your LC_NUMERIC setting. </p>
<h3>Can I use other maps?</h3>
<p> You can also use your own (self drawn, scanned, exported from GIS, &#8230;) maps. The maps must be in PNG, JPEG, GIF, TIFF, or another common file format (the format must be recognized by the gdk-pixbuf library). The lat/long coordinates you write into the &quot;map_koord.txt&quot; file is measured at the center of the map. The map must have a size of 1280&#215;1024 pixels! </p>
<p> Important! The maps must be named &quot;map_*&quot; for UTM-like projections (lat:lon = 1:cos(lat)) and &quot;top_*&quot; for lat/lon Plate carr�e projection (lat:lon = 1:1). The prefix is given so that gpsdrive knows how to scale the maps correctly. Alternatively the maps can be stored without prefix in subdirectories of $HOME/.gpsdrive/maps/ which end in &quot;_map&quot; or &quot;_top&quot;. The georeferencing information (center coordinate and scale factor) for the maps in those subdirectories must be recorded in the main &quot;map_koord.txt&quot; file, typically stored in the <i>~/.gpsdrive/maps/</i> directory. To avoid distortion, anything more global than 1:150k to 1:500k should use &quot;top_*&quot;. </p>
<p> Beware if you are using an image originating from a map projection with a significant deviation between true north and the map projection&#8217;s local +y direction (known as the Convergence Angle). <code>GpsDrive</code> assumes that true north is always directly up! i.e. the Central Meridian of the map projection is located at the map tile&#8217;s center. For some map projections and areas of the country this can be a really bad assumption and your map will be significantly rotated. This effect is most visible at map scales covering a large area. This does not affect lat/lon maps. </p>
<p> There is an &quot;import assistant&quot; built in. Use it to import your non-georeferenced maps. If can be found in the menus under Options -&gt; Maps. </p>
<h2>WAYPOINTS AND POI</h2>
<h3>Importing waypoints</h3>
<p> The manual way: </p>
<p> You may create a file &quot;way.txt&quot; in your ~/.gpsdrive directory which looks like: </p>
<p> DFN-Cert 53.577694 9.991263 FRITZ<br />
 Finkenwerder 53.541765 9.842541 AIRPORT<br />
 Fritz_Wohnung 53.582700 9.971390 FRITZ </p>
<p> The rows are: {label latitude longitude waypoint-type}. The label may not exceed 80 characters or contain spaces. Use underscores (_) in place of spaces, these will automatically be converted into spaces by the program. A blank label is denoted by a single underscore. </p>
<p> Latitude and longitude may be in decimal degrees or in the form of DDDdMM&#8217;SS&quot;[NSEW] or DDD:MM:SS[NSEW]. Seconds or minutes and seconds may be omitted or in decimal form. Thus the following are valid: 42d30&#8217;55&quot;N, 75:30.6425W, -46.25. In fact the delimiters can be anything except numbers, &quot;.&quot;, or spaces. </p>
<p> You may omit the waypoint type. </p>
<p> Following the waypoint-type are (optionally) three space separated zeros, a proximity radius (in integer meters), and a comment. Comments follow the same space/underscore rules as label names, and are limited to 255 characters. </p>
<p> You can create any number of way-*.txt files and chose between them from the Preferences menu. </p>
<p> There is no need to create the way.txt file yourself, you can add the waypoints with GpsDrive using the &quot;x&quot; key. See the Help menu. </p>
<h3>Add new waypoints</h3>
<p> Waypoints created by GpsDrive will be stored in a SQLite database file locacted at ~/.gpsdrive/waypoints.db. </p>
<p> You can add new waypoints in two simple ways: </p>
<p> o To add a waypoint at the <code>current (GPS) position</code> simply press CTRL and RIGHT-mouse-click. You can also press the <code>x</code> key for this. </p>
<p> o To add a waypoint at the <code>mouse position</code>, simply press CTRL and LEFT-mouse-click. You can also press the <code>y</code> key for this. </p>
<p> In the popup window give the waypoint a name (spaces will be converted to underscores) and choose a waypoint type (see below for predefined waypoint types). </p>
<h3>Waypoint icons</h3>
<p> At the moment there a three different icon themes available, but not all have distinct icons for every type. You can choose the themes in the <code>Preferences</code> menu. The possible themes are: &quot;square.big&quot;, &quot;square.small&quot; and &quot;classic&quot;. </p>
<h3>SQL support</h3>
<p> For managing a larger number of waypoints SQL support is essential. Don&#8217;t be afraid, SQLite doesn&#8217;t need much in the way of resources, is very fast, and makes the management (including selection of waypoint types) of the waypoints much easier. In SQL mode you can select the waypoints to display in the <code>Preferences</code> menu. </p>
<h2>ROUTES</h2>
<p> A route is a list of waypoints. GpsDrive guides you from one waypoint to the next on the route. </p>
<p> You can add waypoints to a route using the <i>Find</i> waypoint (select target) window. Find some POIs, then open the <i>Route Listing</i> window with the <code>Edit Route</code> button in the <i>Find</i> window or from the button on the main window. When you click on waypoints in the the Find window&#8217;s Results list they will be added to the Route List. Click &quot;Start Route&quot; when you are ready to begin your journey. It is also possible to import a complete route from a GPX file. </p>
<p> You can add comments to a waypoint which will be spoken by the speech system and also be shown in the map window as scrolling text. </p>
<h3>Comments for routes</h3>
<p> To add comments create a file with the same name as the waypoint file, but change the suffix to .dsc, i.e way-trip.txt and way-trip.dsc, then enter comments in the way-*.dsc file in the manner of: </p>
<p> $waypoint_name Text which is displayed and spoken </p>
<p> $next_waypoint_name Some more text </p>
<p> Example: </p>
<p> $Fritz_Wohnung Hier wohnt Fritz, der Autor von diesem Programm. Er freut sich auf Besuch und eine Einladung zu einem saftigen Steak.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> $Hubertus Hier wohnt Hubertus, ein Freund von Fritz. </p>
<p> There is no limit of the length of the comment. It is important is to start the line with &#8216;$name&#8217; and the comment on the following line. </p>
<h3>Route planning</h3>
<p> There is no shortest-path route planning feature at the moment. We are keenly watching developments over at the OpenStreetMap project for utilizing software such as pgRouting and DGLib. </p>
<h2>KISMET support</h2>
<p> GpsDrive supports <i>kismet</i>. Kismet is a 802.11b wireless network (WLAN) sniffer. If you have kismet running, gpsdrive will detect it when the program starts and show new WLAN access points in real-time on the map. It is necessary to use SQL mode when using GpsDrive with Kismet. WLAN access points which are already stored in the SQL database from prior war-drivings are ignored. If you have enabled GpsDrive&#8217;s voice output, you will hear information about the newly found access point. </p>
<p> For more details have a look at the <i>README.kismet</i> file. </p>
<h2>LOCALISATION</h2>
<p> The program will display messages in English, German, French, Italian, Dutch, Dansk, Hungarian, Slovak, Swedish, Turkish or Spanish if your language is set either with LANG or LANGUAGE. LANGUAGE overrides all other settings. Call &quot;locale&quot; to see the settings and call &quot;set&quot; if LANG or LANGUAGE is set. For German do: </p>
<p> <code>export LANGUAGE=de</code><br />
 and then call gpsdrive in this shell. </p>
<p> You can also start it with the line <code>LANGUAGE=de gpsdrive</code> without setting the language for the shell. </p>
<p> Sometimes it is necessary use LANG instead of LANGUAGE. </p>
<p> If your own language isn&#8217;t available, please contact the GpsDrive Development Team if you want to make the translation. No programming experience is necessary! </p>
<h2>SPEECH OUTPUT</h2>
<p> If you want speech output you have to install speech dispatcher and at least one of the supported speech synthesizers (festival, espeak, &#8230;).<br />
 See <i><a rel="nofollow" href="http://www.freebsoft.org/speechd">http://www.freebsoft.org/speechd</a></i> for information. </p>
<p> For German output you can use espeak or the German festival from<br />
 <i><a rel="nofollow" href="http://www.ims.uni-stuttgart.de/phonetik/synthesis/index.html">http://www.ims.uni-stuttgart.de/phonetik/synthesis/index.html</a></i> </p>
<p> If you have a functional festival software call it as server with: </p>
<p> festival &#8211;server </p>
<p> When you start GpsDrive it will detect a running speechd and speak some status information. When speech output is enabled an additional <i>Mute</i> button is available to switch off sound output. </p>
<p> GpsDrive tries to use the correct language for your locale. If the voice used is not correct, you can choose another one in the <code>Preferences</code>, if installed. </p>
<h2>FRIENDSD server</h2>
<p> A server program called <code>friendsd</code> comes with GpsDrive. It acts as a server for coordinating the position of your friends. After enabling it in the Preferences menu you can see the position of all GpsDrivers connected to this server. </p>
<p> You will see the position of your friends as a car symbol on the map, including the name, time, day of week and the speed of their last connection. The blue arrow shows the last reported direction of your friend. </p>
<p> The time is transmitted as UTC, but shown on the display in your local time, so it is also correct if your friend lives in another time zone. </p>
<p> The server uses port 50123 (UDP), so be sure that you open the port in your firewall. The server needs no root privileges and should run as a normal user or a special user with no privileges. The server has NOT been tested for security. </p>
<p> There is a friends server running on friendsd.gpsdrive.de, you can try it if you enable it in the settings menu. </p>
<p> You can also send messages to other mobile targets (Options/Send Message) </p>
<h2>MAILING LIST</h2>
<p> The primary means of support and coordination of program development happens on the <code>GpsDrive</code> mailing list. </p>
<p> Information about subscription and a searchable archive can be found at <i><a rel="nofollow" href="http://www.gpsdrive.de/support.shtml">http://www.gpsdrive.de/support.shtml</a></i>. </p>
<h2>BUGS</h2>
<p> Please send bug reports to the development team! If we don&#8217;t know about them we can&#8217;t fix them and then they remain unfixed. </p>
<p> File bug reports in our tracker at <i><a rel="nofollow" href="http://bugzilla.gpsdrive.de/">http://bugzilla.gpsdrive.de/</a></i>. You will need to create yourself a SourceForge account at that site, it is rather painless and only takes a minute. This ensures you get feedback about the bug and we can communicate with you if we need further information. </p>
<p> Please report the version (<code>gpsdrive &#8211;version</code>), screen size, platform, and as much specific information about how to reproduce the bug as possible. Whenever possible cut and paste exact error messages and take screenshots. It is helpful to run gpsdrive for a minute with the -D debug level option set high and send us the output. </p>
<p> If <code>GpsDrive</code> crashes with a SegFault, we will need a backtrace of the program as well. Assuming <code>GpsDrive</code> was built with debugging symbols and the binaries were not stripped of them, create a backtrace by running the <code>GpsDrive</code> the GNU debugging software as follows: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>gdb&nbsp;<wbr>`which gpsdrive`</code> </p>
<p> Inside the debugger do: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>run</code>&nbsp;<wbr>(if you use command line arguments place these after the word&nbsp;<wbr><code>run</code>) </p>
<p> When you get the SegFault type in: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>bt full</code> </p>
<p> and send us this output. This gives us an indication of exactly what the program was doing when it broke. </p>
<h2>AUTHORS</h2>
<p> <code>GpsDrive</code> was originally written by Fritz Ganter. Today it is maintained and improved by a worldwide team of volunteer developers centered around the <i><a rel="nofollow" href="http://www.gpsdrive.de">http://www.gpsdrive.de</a></i> website. The source code repository, bug tracker, and collaborative wiki help site are hosted at <i><a rel="nofollow" href="http://gpsdrive.sourceforge.net">http://gpsdrive.sourceforge.net</a></i>. A partial list of contributing authors can be found in the Help-&gt;About menu within the program. </p>
<h2>WARRANTY</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-2004 by Fritz Ganter<br />
 Copyright (c) 2005-2008 by the members of the GpsDrive Development Team </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. Indeed, you are encouraged to do so! </p>
<h3>This document last modified</h3>
<p> $Date: 2009-06-13 00:14:17 +0200 (Sat, 13 Jun 2009) $ </p>
<h2>Index</h2>
