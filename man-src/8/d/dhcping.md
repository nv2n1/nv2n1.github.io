---
title: "dhcping(8)"
name: "dhcping"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dhcping/"
description: "dhcping – send a DHCP request to DHCP server to see if it’s up and running"
---

<p><code>dhcping</code> &#8211; send a DHCP request to DHCP server to see if it&#8217;s up and running</p>
<h2>Synopsis</h2>
<p><code>dhcping</code> [<code>-v</code>] [<code>-q</code>] [<code>-i</code>] [<code>-r</code>] <code>-t</code> <i>maxwait</i> <code>-c</code> <i>client-IP-address</i> <code>-s</code> <i>server-IP-address</i> <code>-h</code> <i>client-hardware-address</i> [<code>-g</code> <i>gateway-IP-address</i>]</p>
<h2>Description</h2>
<p>This command allows the system administrator to check if a remote DHCP server is still functioning. </p>
<p> Options are: </p>
<dl>
<dt><code>-v</code></p>
<dd>Verbose, print some information. </p>
<dt><code>-i</code></p>
<dd>Use <font SIZE="-1">DHCPINFORM</font> packets. </p>
<dt><code>-r</code></p>
<dd>Use <font SIZE="-1">DHCPREQUEST</font> packets (default behaviour). </p>
<dt><code>-q</code></p>
<dd>Quiet, print nothing on the screen. </p>
<dt><code>-t</code> <i>maxwait</i></p>
<dd>Maximum time to wait for an answer from the server in seconds. Default is 3 seconds. </p>
<dt><code>-c</code> <i>client-</i><font SIZE="-1"><i>IP</i></font><i>-address</i></p>
<dd>Request this <font SIZE="-1">IP</font> address. Note that this is also the <font SIZE="-1">IP</font> address the answer will be sent to. </p>
<dt><code>-s</code> <i>server-</i><font SIZE="-1"><i>IP</i></font><i>-address</i></p>
<dd>Send the <font SIZE="-1">DHCP</font> packet to this <font SIZE="-1">IP</font> address. </p>
<dt><code>-h</code> <i>client-hardware-address</i></p>
<dd>Use this hardware-address in the <font SIZE="-1">DHCP</font> request. It can be up to sixteen octets seperated by colons (i.e. 01:02:03:04) </p>
<dt><code>-g</code> <i>gateway-</i><font SIZE="-1"><i>IP</i></font><i>-address</i></p>
<dd>Use this <font SIZE="-1">IP</font> address for the gateway <font SIZE="-1">IP</font> address in the <font SIZE="-1">DHCP</font> packet. This option is currently broken.</dl>
<h2>Return Values</h2>
<p>If everything goes okay, it returns 0. If there went something wrong, it returns 1.</p>
<h2>Setup</h2>
<p>This program should be installed setuid root or ran by root only. See SECURITY for more information. </p>
<p> On your DHCP server, add these lines to the dhcpd.conf: </p>
<pre> host &lt;your monitoring host FQDN&gt; {
 hardware ethernet &lt;your monitor host mac address&gt;;
 fixed-address &lt;your monitoring host IP address&gt;;
 }</pre>
<p>Then try it: </p>
<p> $ dhcping -c <i>your monitoring host IP address</i> \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr><i>your DHCP server IP address</i>&nbsp;<wbr>\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-h&nbsp;<wbr><i>your monitor host mac address</i> </p>
<p> It will either respond with &#8220;no answer&#8221; or &#8220;Got answer from: <i>your DHCP server IP address</i>&#8221; </p>
<p> The DHCP server logfile will give:<br />
&nbsp;<wbr>DHCPREQUEST for 192.168.1.1 from 00:20:18:56:29:8f via ed0<br />
&nbsp;<wbr>DHCPACK on 192.168.1.1 to 00:20:18:56:29:8f via ed0<br />
&nbsp;<wbr>DHCPRELEASE of 192.168.1.1 from 00:20:18:56:29:8f via ed0&nbsp;<wbr>(found) </p>
<p> Running in DHCPINFORM mode with <code>-i</code>: </p>
<p> If you see &#8220;DHCPINFORM from 192.168.1.1 via xl0: not authoritative for subnet 192.168.1.0&#8221;, you should add the authoritative statement to the subnet, See dhcpd.<i><a href="/docs/linux/man/5-conf/">conf</a></i>(5) for details. </p>
<p> When running in very verbose mode, <code>dhcping</code> tries to dump all data of the send and received DHCP packets. It will first dump the packet in hex-format, then decodes the header and finally the options.</p>
<h2>How It Works</h2>
<p>The client either sends a DHCPREQUEST or DHCPINFORM packet to the server and waits for an answer. Then, if a DHCPREQUEST was send, it will send a DHCPRELEASE back to the server.</p>
<h2>Security</h2>
<p>This program is installed setuid root as it requires the privileges to bind itself to port 68 (bootpc). Root privileges are dropped as soon as the program has bound itself to that port.</p>
<h2>Bugs</h2>
<p>Currently (this may, or may not, change in the future) the ISC DHCP daemon does not write leases with a fixed IP address in the dhcpd.leases file. </p>
<p> DHCPINFORM packets can only be used on subnets the server is authori- tative for. If the monitoring script runs on a subnet the server isn&#8217;t authoritative for, it should use the DHCPREQUEST packets. I also experienced some problems with ISC DHCPD v2 servers, but that is also in the README of it. </p>
<p> The <code>-V</code> option is still working, but shouldn&#8217;t be used for debugging of the packets. Better use <i><a href="/docs/linux/man/8-dhcpdump/">dhcpdump</a></i>(8) for that, which is available on my website. I wanted to remove it, but decided only to do it from the documentation, not from the code. Maybe I&#8217;ll need it one day for debugging.</p>
<h2>Author</h2>
<p>Edwin Groothuis, edwin [at] mavetju.org (<a rel="nofollow" href="http://www.mavetju.org)">http://www.mavetju.org)</a></p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-dhcpd/">dhcpd</a></i>(8), <i><a href="/docs/linux/man/8-dhclient/">dhclient</a></i>(8), dhcpd.<i><a href="/docs/linux/man/5-conf/">conf</a></i>(5), <i><a href="/docs/linux/man/8-dhcpdump/">dhcpdump</a></i>(8) </p>
