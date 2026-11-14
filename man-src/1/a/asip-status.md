---
title: "asip-status(1)"
name: "asip-status"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asip-status/"
description: "asip-status.pl – Queries AFP servers for their capabilities"
---

<h2 class="name">NAME</h2>
<p> asip-status.pl &#8211; Queries AFP servers for their capabilities </p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/asip-status.pl</code> ADDRESS<i>:PORT</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>asip-status.pl</code> is a perl script that sends a FPGetSrvrInfo request to an AFP server at ADDRESS:PORT and displays the results, namely &quot;Machine type&quot;, the server&#8217;s name, supported AFP versions, UAMs and AFP flags, the &quot;server signature&quot; and the network addresses, the server provides AFP services on. </p>
<p> When you don&#8217;t supply :PORT, then the default AFP port, 548, will be used.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
<code>/usr/bin/asip-status.pl</code> 192.168.21.2
AFP reply from 192.168.21.2:548
Flags: 1  Cmd: 3  ID: 57005
Reply: DSIGetStatus
Request ID: 57005
Machine type: Macintosh
AFP versions: AFPVersion 1.1,AFPVersion 2.0,AFPVersion 2.1,AFP2.2
UAMs: Cleartxt passwrd,Randnum exchange,2-Way Randnum exchange
Flags: SupportsCopyFile,SupportsChgPwd,SupportsServerMessages,
SupportsServerSignature,SupportsTCP/IP,SupportsSuperClient
Server name: PowerMac 9600/200
Signature:
04 c1 6e 59 04 c1 6e 59 04 c1 6e 59 04 c1 6e 59  ..nY..nY..nY..nY
                                                  
Network address: 192.168.21.2:548 (tcp/ip address and port)
Network address: 10.20 (ddp address)
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<code>/usr/bin/asip-status.pl</code> 192.168.21.1:10548
AFP reply from 192.168.21.1:10548
Flags: 1  Cmd: 3  ID: 57005
Reply: DSIGetStatus
Request ID: 57005
Machine type: Netatalk
AFP versions: AFPVersion 1.1,AFPVersion 2.0,AFPVersion 2.1,AFP2.2,AFPX03,
AFP3.1
UAMs: Cleartxt passwrd,Randnum exchange,2-Way Randnum exchange,DHCAST128
Flags: SupportsCopyFile,SupportsServerMessages,SupportsServerSignature,
SupportsTCP/IP,SupportsSrvrNotifications,SupportsOpenDirectory,
SupportsUTF8Servername,SupportsSuperClient
Server name: Fire V480
Signature:
83 29 cc 60 83 29 cc 60 83 29 cc 60 83 29 cc 60  .).`.).`.).`.).`
                                                  
Network address: 192.168.21.1:10548 (TCP/IP address and port)
Network address: 65282.142 (ddp address)
UTF8 Servername: Fire V480
</pre>
</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Netatalk-devel list &lt;netatalk-devel [at] lists.sourceforge.net&gt;. </p>
<h2>Index</h2>
