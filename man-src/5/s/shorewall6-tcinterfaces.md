---
title: "shorewall6-tcinterfaces(5)"
name: "shorewall6-tcinterfaces"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shorewall6-tcinterfaces/"
description: "tcinterfaces – Shorewall6 file"
---

<p>tcinterfaces &#8211; Shorewall6 file</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/etc/shorewall6/tcinterfaces</code></dl>
<h2>Description</h2>
<dd>This file lists the interfaces that are subject to simple traffic shaping. Simple traffic shaping is enabled by setting TC_ENABLED=Simple in m[blue]<code>shorewall6.conf</code>m[]<font SIZE="-2">[1]</font>(5). </p>
<p> A note on the <i>bandwidth</i> definition used in this file: </p>
<dl>
<dd>&bull; don&#8217;t use a space between the integer value and the unit: 30kbit is valid while 30 kbit is not.</dl>
<dl>
<dd>&bull; you can use one of the following units: </p>
<p> <code>kbps</code></p>
<dl>
<dd>Kilobytes per second.</dl>
<p> <code>mbps</code></p>
<dl>
<dd>Megabytes per second.</dl>
<p> <code>kbit</code></p>
<dl>
<dd>Kilobits per second.</dl>
<p> <code>mbit</code></p>
<dl>
<dd>Megabits per second.</dl>
<p> <code>bps</code> or <code>number</code></p>
<dl>
<dd>Bytes per second.</dl>
<p> k or kb</p>
<dl>
<dd>Kilo bytes.</dl>
<p> m or mb</p>
<dl>
<dd>Megabytes.</dl>
</dl>
<dl>
<dd>&bull; Only whole integers are allowed.</dl>
<p> The columns in the file are as follows (where the column name is followed by a different name in parentheses, the different name is used in the alternate specification syntax). </p>
<p> <code>INTERFACE</code></p>
<dl>
<dd>The logical name of an interface. If you run both IPv4 and IPv6 Shorewall firewalls, a given interface should only be listed in one of the two configurations.</dl>
<p> <code>TYPE</code> &#8211; [<code>external</code>|<code>internal</code>]</p>
<dl>
<dd>Optional. If given specifies whether the interface is <code>external</code> (facing toward the Internet) or <code>internal</code> (facing toward a local network) and enables SFQ flow classification.</dl>
<p> <code>IN-BANDWIDTH (in_bandwidth)</code> &#8211; {-|<i>bandwidth</i>[:<i>burst</i>]|~<i>bandwidth</i>[:<i>interval</i>:<i>decay_interval</i>]}</p>
<dl>
<dd>The incoming <i>bandwidth</i> of that interface. Please note that you are not able to do traffic shaping on incoming traffic, as the traffic is already received before you could do so. But this allows you to define the maximum traffic allowed for this interface in total, if the rate is exceeded, the packets are dropped. You want this mainly if you have a DSL or Cable connection to avoid queuing at your providers side. </p>
<p> If you don&#8217;t want any traffic to be dropped, set this to a value to zero in which case Shorewall will not create an ingress qdisc. Must be set to zero if the REDIRECTED INTERFACES column is non-empty. </p>
<p> The optional burst option was added in Shorewall 4.4.18. The default <i>burst</i> is 10kb. A larger <i>burst</i> can help make the <i>bandwidth</i> more accurate; often for fast lines, the enforced rate is well below the specified <i>bandwidth</i>. </p>
<p> What is described above creates a rate/burst policing filter. Beginning with Shorewall 4.4.25, a rate-estimated policing filter may be configured instead. Rate-estimated filters should be used with Ethernet adapters that have Generic Receive Offload enabled by default. See m[blue]<code>Shorewall FAQ 97a</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> To create a rate-estimated filter, precede the bandwidth with a tilde (&quot;~&quot;). The optional interval and decay_interval determine how often the rate is estimated and how many samples are retained for estimating. Please see m[blue]<code><a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt">http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt</a></code>m[] for details.</dl>
<p> OUT-BANDWIDTH (out_bandwidth) &#8211; [<i>rate</i>[:[<i>burst</i>][:[<i>latency</i>][:[<i>peek</i>][:[<i>minburst</i>]]]]]]</p>
<dl>
<dd>Added in Shorewall 4.4.13. The terms are defined in <a href="/docs/linux/man/8-tc-tbf/">tc-tbf</a>(8). </p>
<p> Shorewall provides defaults as follows:</p>
<dl>
<dd><i>burst</i> &#8211; 10kb</dl>
<dl>
<dd><i>latency</i> &#8211; 200ms</dl>
<p> The remaining options are defaulted by <a href="/docs/linux/man/8-tc/">tc</a>(8).</dl>
<h2>Files</h2>
<p>/etc/shorewall6/tcinterfaces.</p>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/doc/sch_tbf.txt">http://ace-host.stuart.id.au/russell/files/tc/doc/sch_tbf.txt</a></code>m[] </p>
<p> m[blue]<code><a rel="nofollow" href="http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt">http://ace-host.stuart.id.au/russell/files/tc/doc/estimators.txt</a></code>m[] </p>
<p> <a href="/docs/linux/man/8-shorewall6/">shorewall6</a>(8), <a href="/docs/linux/man/5-shorewall6-accounting/">shorewall6-accounting</a>(5), <a href="/docs/linux/man/5-shorewall6-actions/">shorewall6-actions</a>(5), <a href="/docs/linux/man/5-shorewall6-blacklist/">shorewall6-blacklist</a>(5), <a href="/docs/linux/man/5-shorewall6-hosts/">shorewall6-hosts</a>(5), <a href="/docs/linux/man/5-shorewall6-maclist/">shorewall6-maclist</a>(5), <a href="/docs/linux/man/5-shorewall6-netmap/">shorewall6-netmap</a>(5),<a href="/docs/linux/man/5-shorewall6-params/">shorewall6-params</a>(5), <a href="/docs/linux/man/5-shorewall6-policy/">shorewall6-policy</a>(5), <a href="/docs/linux/man/5-shorewall6-providers/">shorewall6-providers</a>(5), <a href="/docs/linux/man/5-shorewall6-rtrules/">shorewall6-rtrules</a>(5), <a href="/docs/linux/man/5-shorewall6-routestopped/">shorewall6-routestopped</a>(5), <a href="/docs/linux/man/5-shorewall6-rules/">shorewall6-rules</a>(5), <a href="/docs/linux/man/5-shorewall6-conf/">shorewall6.conf</a>(5), <a href="/docs/linux/man/5-shorewall6-secmarks/">shorewall6-secmarks</a>(5), shorewall6-tcpri, <a href="/docs/linux/man/5-shorewall6-tos/">shorewall6-tos</a>(5), <a href="/docs/linux/man/5-shorewall6-tunnels/">shorewall6-tunnels</a>(5), <a href="/docs/linux/man/5-shorewall6-zones/">shorewall6-zones</a>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>shorewall6.conf</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/manpages6/shorewall6.conf.html">http://www.shorewall.net/manpages6/shorewall6.conf.html</a></dl>
<dt> 2.</p>
<dd>Shorewall FAQ 97a</p>
<dl>
<dd><a rel="nofollow" href="http://www.shorewall.net/FAQ.htm#faq97a">http://www.shorewall.net/FAQ.htm#faq97a</a></dl>
