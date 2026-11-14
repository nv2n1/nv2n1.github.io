---
title: "anyremote(1)"
name: "anyremote"
section: "1"
letter: "a"
url: "/docs/linux/man/1-anyremote/"
---

<h2 class="name">NAME</h2>
 

 

 anyremote - control PC with Bluetooth cell phone 
 

<h2>SYNOPSIS</h2>

 

 anyremote [-f file] [-s connect string] [-log] [-a] 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[-fe port]&nbsp;<wbr>[-http]&nbsp;<wbr>[-u username]&nbsp;<wbr>[-name SDP service name]&nbsp;<wbr>[-password] 

 anyremote -h|-v 

<h2>DESCRIPTION</h2>

 

 The overall goal of this project is to provide remote control service on Linux through Bluetooth, InfraRed, Wi-Fi or just TCP/IP connection. 

 anyRemote supports wide range of modern cell phones like Nokia, SonyEricsson, Motorola and others. 

 It was developed as thin &quot;communication&quot; layer between Bluetooth (IR, Wi-Fi)-capabled phone and Linux, and in theory could be configured to manage almost any software. 

 anyRemote is console application, but in addition there are GUI front-ends for Gnome and KDE.

<h2>OPTIONS</h2>

<h3>-h</h3>

 

 print short help and exit

<h3>-v</h3>

 

 print version number and exit

<h3>-f /path/to/configuration/file</h3>

 

 By default anyremote will try to find and use $HOME/.anyremote.cfg, then ./.anyremote.cfg. It is possible to specify configuration file directly with -f option.

<h3>-s connect string</h3>

 

 where connect string can be one of: 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bluetooth:_channel_ (Server mode - bluetooth connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>socket:_port_<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (Server mode - TCP/IP connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>local:/dev/ircommX (Server mode - IR connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/rfcomm#<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (AT mode - bluetooth connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/ttyACM#<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (AT mode - cable connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/dev/ircomm#<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> (AT mode - IR connection)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ilirc:_AF_LOCAL socket file_ (use with inputlircd)
 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>stdin

<h3>-log</h3>

 

 print verbose logging information to $HOME/.anyRemote/anyremote.log

<h3>-a</h3>

 

 reconnect automatically in case of connection failure, used only in AT-mode

<h3>-fe _port_</h3>

 

 Work as backend for GUI frontend. Use specified port to connect to frontend.

<h3>-http</h3>

 

 Tune work with anyremote2html

<h3>-name SDP_service_name</h3>

 

 if bluetooth connection is used, allows to specify SDP service name. 

 Default value for SDP service name is &quot;anyRemote&quot;

<h3>-password</h3>

 

 If this option is specified, then anyRemote will ask java client for password. 

 Password phrase should be stored in $HOME/.anyRemote/password file in plain text.

<h3>-u|--user _username_</h3>

 

 if started from root, allows to set effective user ID to specified user 

 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
 

<h2>AUTHORS</h2>

 Mikhail Fedotov <i>anyremote [at] mail.ru</i> 

 <i><a rel="nofollow" HREF="http://anyremote.sf.net">http://anyremote.sf.net</a></i> 

<h2>BUGS</h2>

 If you find any bugs, please report to <i>anyremote [at] mail.ru</i> 

<h2>LICENCE</h2>

 

 This is free software. You may redistribute copies of it under the terms of the GNU General Public License <i><a rel="nofollow" HREF="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a></i>. There is NO WARRANTY, to the extent permitted by law. 

<h2>Index</h2>


