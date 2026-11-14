---
title: "ax25ipd(5)"
name: "ax25ipd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-ax25ipd/"
description: "ax25ipd.conf – Control the operation of ax25ipd."
---

<p>ax25ipd.conf &#8211; Control the operation of ax25ipd.</p>
<h2>Description</h2>
<p>The <code>ax25ipd.conf</code> file controls the operation of the <a href="/docs/linux/man/8-ax25ipd/">ax25ipd</a>(8) program. The operation of the config file can best be seen in an example: </p>
<p> #<br />
 # ax25ipd configuration file for station floyd.vk5xxx.ampr.org<br />
 #<br />
 # Select axip transport. &#8216;ip&#8217; is what you want for compatibility<br />
 # with most other gates &#8230;<br />
 #<br />
 socket ip<br />
 #<br />
 # Set ax25ipd mode of operation. (digi or tnc)<br />
 #<br />
 mode tnc<br />
 #<br />
 # If you selected digi, you must define a callsign. If you selected<br />
 # tnc mode, the callsign is currently optional, but this may change<br />
 # in the future! (2 calls if using dual port kiss)<br />
 #<br />
 # mycall vk5xxx-4<br />
 # mycall2 vk5xxx-5<br />
 #<br />
 # In digi mode, you may use an alias. (2 for dual port)<br />
 #<br />
 # myalias svwdns<br />
 # myalias2 svwdn2<br />
 #<br />
 # Send an ident every 540 seconds &#8230;<br />
 #<br />
 # beacon after 540<br />
 # btext ax25ip &#8212; tncmode rob/vk5xxx &#8212; Experimental AXIP gateway<br />
 #<br />
 # Serial port, or pipe connected to a kissattach in my case<br />
 #<br />
 device /dev/ttyp0<br />
 #<br />
 # Set the device speed<br />
 #<br />
 speed 9600<br />
 #<br />
 # loglevel 0 &#8211; no output<br />
 # loglevel 1 &#8211; config info only<br />
 # loglevel 2 &#8211; major events and errors<br />
 # loglevel 3 &#8211; major events, errors, and AX25 frame trace<br />
 # loglevel 4 &#8211; all events<br />
 # log 0 for the moment, syslog not working yet &#8230;<br />
 #<br />
 loglevel 4<br />
 #<br />
 # If we are in digi mode, we might have a real tnc here, so use param to<br />
 # set the tnc parameters &#8230;<br />
 #<br />
 # param 1 20<br />
 #<br />
 # Broadcast Address definition. Any of the addresses listed will be forwarded<br />
 # to any of the routes flagged as broadcast capable routes.<br />
 #<br />
 broadcast QST-0 NODES-0<br />
 #<br />
 # ax.25 route definition, define as many as you need.<br />
 # format is route (call/wildcard) (ip host at destination)<br />
 # ssid of 0 routes all ssid&#8217;s<br />
 #<br />
 # route &lt;destcall&gt; &lt;destaddr&gt; [flags]<br />
 #<br />
 # Valid flags are:<br />
 # b &#8211; allow broadcasts to be transmitted via this route<br />
 # d &#8211; this route is the default route<br />
 #<br />
 route vk2sut-0 44.136.8.68 b<br />
 route vk5asf 44.136.188.221 b<br />
 route vk2abc 44.1.1.1 d<br />
 #<br />
 # </p>
<p> More to come &#8230;</p>
<h2>Files</h2>
<p>/etc/ax25/ax25ipd.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ax25ipd/">ax25ipd</a></code>(8). </p>
