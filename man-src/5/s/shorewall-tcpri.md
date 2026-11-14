---
title: "shorewall-tcpri(5)"
name: "shorewall-tcpri"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall-tcpri/"
description: "tcpri – Shorewall file"
---

<p>tcpri &#8211; Shorewall file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall/tcpri</code></dl>
<h2>Description</h2>
<dd>This file is used to specify the priority of traffic for simple traffic shaping (TC_ENABLED=Simple in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5)). The priority band of each packet is determined by the <code>last</code> entry that the packet matches. If a packet doesn&#8217;t match any entry in this file, then its priority will be determined by its TOS field. The default mapping is as follows but can be changed by setting the TC_PRIOMAP option in m[blue]<code>shorewall.conf</code>m[]<font SIZE="-2">[1]</font>(5).</p>
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
<dd>Classifies matching traffic as High Priority (1), Medium Priority (2) or Low Priority (3). For those interfaces listed in m[blue]<code>shorewall-tcinterfaces</code>m[]<font SIZE="-2">[2]</font>(5), Priority 2 traffic will be deferred so long and there is Priority 1 traffic queued and Priority 3 traffic will be deferred so long as there is Priority 1 or Priority 2 traffic to send.</dl>
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
<p>/etc/shorewall/tcpri</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></code>m[]<font SIZE="-2">[3]</font> </p>
<p> <a href="/docs/linux/man/8-prio/">prio</a>(8), <a href="/docs/linux/man/8-shorewall/">shorewall</a>(8), <a href="/docs/linux/man/5-shorewall-accounting/">shorewall-accounting</a>(5), <a href="/docs/linux/man/5-shorewall-actions/">shorewall-actions</a>(5), <a href="/docs/linux/man/5-shorewall-blacklist/">shorewall-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall-hosts/">shorewall-hosts</a>(5), <a href="/docs/linux/man/5-shorewall_interfaces/">shorewall_interfaces</a>(5), <a href="/docs/linux/man/5-shorewall-ipsets/">shorewall-ipsets</a>(5), <a href="/docs/linux/man/5-shorewall-maclist/">shorewall-maclist</a>(5), <a href="/docs/linux/man/5-shorewall-masq/">shorewall-masq</a>(5), <a href="/docs/linux/man/5-shorewall-nat/">shorewall-nat</a>(5), <a href="/docs/linux/man/5-shorewall-netmap/">shorewall-netmap</a>(5), <a href="/docs/linux/man/5-shorewall-params/">shorewall-params</a>(5), <a href="/docs/linux/man/5-shorewall-policy/">shorewall-policy</a>(5), <a href="/docs/linux/man/5-shorewall-providers/">shorewall-providers</a>(5), <a href="/docs/linux/man/5-shorewall-proxyarp/">shorewall-proxyarp</a>(5), <a href="/docs/linux/man/5-shorewall-rtrules/">shorewall-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall-routestopped/">shorewall-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall-rules/">shorewall-rules</a>(5), <a href="/docs/linux/man/5-shorewall-conf/">shorewall.conf</a>(5), <a href="/docs/linux/man/5-shorewall-secmarks/">shorewall-secmarks</a>(5), <a href="/docs/linux/man/5-shorewall-tcclasses/">shorewall-tcclasses</a>(5), <a href="/docs/linux/man/5-shorewall-tcdevices/">shorewall-tcdevices</a>(5), <a href="/docs/linux/man/5-shorewall-mangle/">shorewall-mangle</a>(5), <a href="/docs/linux/man/5-shorewall-tos/">shorewall-tos</a>(5), <a href="/docs/linux/man/5-shorewall-tunnels/">shorewall-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall-zones/">shorewall-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall.conf.html">http://www.shorewall.net/manpages/shorewall.conf.html</a></dl>
<dt> 2.</p>
<dd>shorewall-tcinterfaces</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages/shorewall-tcinterfaces.html">http://www.shorewall.net/manpages/shorewall-tcinterfaces.html</a></dl>
<dt> 3.</p>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/configuration_file_basics.htm#Pairs">http://www.shorewall.net/configuration_file_basics.htm#Pairs</a></dl>
