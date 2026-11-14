---
title: "shorewall6-tcpri(5)"
name: "shorewall6-tcpri"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-tcpri/"
description: "tcpri – Shorewall6 file"
---

<p>tcpri &#8211; Shorewall6 file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/tcpri</code></dl>
<h2>Description</h2>
<dd>This file is used to specify the priority band of traffic for simple traffic shaping (TC_ENABLED=Simple in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[1]</font>(5)). The priority band of each packet is determined by the <code>last</code> entry that the packet matches. If a packet doesn&#8217;t match any entry in this file, then its priority will be determined by its TOS field. The default mapping is as follows but can be changed by setting the TC_PRIOMAP option in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[1]</font>(5).</p>
<dl>
<dd>
<pre>TOS Bits Means Linux Priority BAND
------------------------------------------------------------
0x0 0 Normal Service 0 Best Effort 2
0x2 1 Minimize Monetary Cost 1 Filler 3
0x4 2 Maximize Reliability 0 Best Effort 2
0x6 3 mmc+mr 0 Best Effort 2
0x8 4 Maximize Throughput 2 Bulk 3
0xa 5 mmc+mt 2 Bulk 3
0xc 6 mr+mt 2 Bulk 3
0xe 7 mmc+mr+mt 2 Bulk 3
0x10 8 Minimize Delay 6 Interactive 1
0x12 9 mmc+md 6 Interactive 1
0x14 10 mr+md 6 Interactive 1
0x16 11 mmc+mr+md 6 Interactive 1
0x18 12 mt+md 4 Int. Bulk 2
0x1a 13 mmc+mt+md 4 Int. Bulk 2
0x1c 14 mr+mt+md 4 Int. Bulk 2
0x1e 15 mmc+mr+mt+md 4 Int. Bulk 2</pre>
</dl>
<p> The columns in the file are as follows. <code>BAND</code> &#8211; {<code>1</code>|<code>2</code>|<code>3</code>}</p>
<dl>
<dd>Classifies matching traffic as High Priority (1), Medium Priority (2) or Low Priority (3). For those interfaces listed in m[blue]<code>shorewall6-tcinterfaces</code>m[]<font SIZE="-2">[2]</font>(5), Priority 2 traffic will be deferred so long and there is Priority 1 traffic queued and Priority 3 traffic will be deferred so long as there is Priority 1 or Priority 2 traffic to send.</dl>
<p> <code>PROTO</code> &#8211; <i>protocol</i>[,&#8230;]</p>
<dl>
<dd>Optional. The name or number of an IPv4 <i>protocol</i>. Beginning with Shorewall 4.5.12, this column can accept a comma-separated list of protocols.</dl>
<p> PORT(S) &#8211; <i>port</i> [,&#8230;]</p>
<dl>
<dd>Optional. May only be given if the the PROTO is TCP (6), UDP (17), DCCP (33), SCTP (132) or UDPLITE (136). A list of one or more port numbers or service names from /etc/services. Port ranges of the form <i>lowport</i>:<i>highport</i> may also be included.</dl>
<p> ADDRESS &#8211; [<i>address</i>]</p>
<dl>
<dd>Optional. The IP or MAC address that the traffic originated from. MAC addresses must be given in Shorewall format. If this column contains an address, then the PROTO, PORT(S) and INTERFACE column must be empty (&quot;-&quot;).</dl>
<p> INTERFACE &#8211; [<i>interface</i>]</p>
<dl>
<dd>Optional. The logical name of an <i>interface</i> that traffic arrives from. If given, the PROTO, PORT(S) and ADDRESS columns must be empty (&quot;-&quot;).</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 INTERFACE classification of packets occurs before classification by PROTO/PORT(S)/ADDRESS. So it is highly recommended to place entries that specify INTERFACE at the top of the file so that the rule about <i>last entry matches</i> is preserved.  <code>HELPER</code> &#8211; [<i>helper</i>]</p>
<dl>
<dd>Optional. Names a Netfilter protocol helper module such as ftp, sip, amanda, etc. A packet will match if it was accepted by the named helper module. You can also append &quot;-&quot; and a port number to the helper module name (e.g., ftp-21) to specify the port number that the original connection was made on.</dl>
<h2>Files</h2>
<p>/etc/shorewall6/tcpri</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-prio/">PRIO</a>(8), <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall6-tcinterfaces/">shorewall6-tcinterfaces</a>(5), <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
<dt> 2.</p>
<dd>shorewall6-tcinterfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6-tcinterfaces.html">http://www.shorewall.net/manpages6/shorewall6-tcinterfaces.html</a></dl>
