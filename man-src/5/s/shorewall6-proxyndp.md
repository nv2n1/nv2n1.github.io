---
title: "shorewall6-proxyndp(5)"
name: "shorewall6-proxyndp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-proxyndp/"
---

proxyndp - Shorewall6 Proxy NDP file

<h2>Synopsis</h2>

<dl><dt> <b>/etc/shorewall6/proxyndp</b></dl>

<h2>Description</h2>

<dd>This file was added in Shorewall 4.4.16 and is used to define Proxy NDP. There is one entry in this file for each IPv6 address to be proxied. 

 The columns in the file are as follows. 

 <b>ADDRESS</b> - <i>address</i>
<dl><dd>IPv6 Address.</dl>
 

 <b>INTERFACE</b> - <i>interface</i> (Optional)
<dl><dd>Local interface where system with the ip address in ADDRESS is connected. Only required when the HAVEROUTE column is left empty or is set to <b>no</b> or <b>No</b>.</dl>
 

 <b>EXTERNAL</b> - <i>interface</i>
<dl><dd>External Interface to be used to access this system from the Internet.</dl>
 

 <b>HAVEROUTE</b> - [<b>-</b>|<b>Yes</b>|<b>No</b>]
<dl><dd>If there is already a route from the firewall to the host whose address is given, enter <b>Yes</b> or <b>yes</b> in this column. Otherwise, enter <b>no</b> or <b>No</b> or leave the column empty and Shorewall will add the route for you. If Shorewall6 adds the route, its persistence depends on the value of the<b>PERSISTENT</b> column contains <b>Yes</b>; otherwise, <b>shorewall6 stop</b> or <b>shorewall clear6</b> will delete the route.</dl>
 

 <b>PERSISTENT</b> - [<b>-</b>|<b>Yes</b>|<b>No</b>]
<dl><dd>If HAVEROUTE is <b>No</b> or <b>no</b>, then the value of this column determines if the route added by Shorewall persists after a <b>shorewall6 stop</b> or a <b>shorewall6 clear</b>. If this column contains <b>Yes</b> or <b>yes</b> then the route persists; If the column is empty or contains <b>No</b> or <b>no</b> then the route is deleted by <b>shorewall6 stop</b> or <b>shorewall6 clear</b>.</dl>

<h2>Example</h2>

Example 1:
<dl><dd>Host with IPv6 2001:470:b:227::44 is connected to interface eth1 and we want hosts attached via eth0 to be able to access it using that address. 

<dl><dd><pre> #ADDRESS INTERFACE EXTERNAL
 2001:470:b:227::44 eth1 eth0</pre></dl></dl>

<h2>Files</h2>

/etc/shorewall6/proxyndp

<h2>See Also</h2>

m[blue]<b><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></b>m[]<font SIZE="-2">[1]</font> 

 <a HREF="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a HREF="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a HREF="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a HREF="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a HREF="/docs/linux/man/5-shorewall6-exclusion/">shorewall6-exclusion</a>(5), <a HREF="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a HREF="/docs/linux/man/5-shorewall6-interfaces/">shorewall6-interfaces</a>(5), <a HREF="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a HREF="/docs/linux/man/5-shorewall6-nesting/">shorewall6-nesting</a>(5), <a HREF="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a HREF="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a HREF="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a HREF="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a HREF="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a HREF="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a HREF="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a HREF="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a HREF="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcclasses/">shorewall6-tcclasses</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tcdevices/">shorewall6-tcdevices</a>(5), <a HREF="/docs/linux/man/5-shorewall6-mangle/">shorewall6-mangle</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a HREF="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a HREF="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)

<h2>Notes</h2>

<dl><dt> 1.
<dd><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a>
<dl><dd><a rel="nofollow" HREF="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
 
