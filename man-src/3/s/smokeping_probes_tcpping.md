---
title: "smokeping_probes_tcpping(3)"
name: "smokeping_probes_tcpping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_tcpping/"
description: "Smokeping::probes::TCPPing – TCPPing Probe for SmokePing"
---

<p>Smokeping::probes::TCPPing &#8211; TCPPing Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +TCPPing
 binary = /usr/bin/tcpping # mandatory
 forks = 5
 offset = 50%
 step = 300
 tcptraceroute = -e &quot;sudo /bin/tcptraceroute&quot;
 timeout = 15
 # The following variables can be overridden in each target section
 pings = 5
 port = 80
 # [...]
 *** Targets ***
 probe = TCPPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = TCPPing # if the default probe is something else
 host = my.host
 pings = 5
 port = 80</pre>
<h2>Description</h2>
<p>Integrates TCPPing as a probe into smokeping. The variable <code>binary</code> must point to your copy of the TCPPing program. If it is not installed on your system yet, you can get it from <a rel="nofollow" href="http://www.vdberg.org/~richard/tcpping.">http://www.vdberg.org/~richard/tcpping.</a> You can also get it from <a rel="nofollow" href="http://www.darkskies.za.net/~norman/scripts/tcpping.">http://www.darkskies.za.net/~norman/scripts/tcpping.</a> </p>
<p> The (optional) port option lets you configure the port for the pings sent. The TCPPing manpage has the following to say on this topic: </p>
<p> The problem is that with the widespread use of firewalls on the modern Internet, many of the packets that <i><a href="/docs/linux/man/8-traceroute/">traceroute</a></i>(8) sends out end up being filtered, making it impossible to completely trace the path to the destination. However, in many cases, these firewalls will permit inbound <font SIZE="-1">TCP</font> packets to specific ports that hosts sitting behind the firewall are listening for connections on. By sending out <font SIZE="-1">TCP SYN</font> packets instead of <font SIZE="-1">UDP</font> or <font SIZE="-1">ICMP ECHO</font> packets, tcptraceroute is able to bypass the most common firewall filters. </p>
<p> It is worth noting that tcptraceroute never completely establishes a <font SIZE="-1">TCP</font> connection with the destination host. If the host is not listening for incoming connections, it will respond with an <font SIZE="-1">RST</font> indicating that the port is closed. If the host instead responds with a SYN|ACK, the port is known to be open, and an <font SIZE="-1">RST</font> is sent by the kernel tcptraceroute is running on to tear down the connection without completing three-way handshake. This is the same half-open scanning technique that <i><a href="/docs/linux/man/1-nmap/">nmap</a></i>(1) uses when passed the -sS flag.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>The location of your tcpping script. </p>
<p> Example value: /usr/bin/tcpping </p>
<p> This setting is mandatory.</p>
<dt>forks</p>
<dd>Run this many concurrent processes at maximum </p>
<p> Example value: 5 </p>
<p> Default value: 5</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</p>
<dt>tcptraceroute</p>
<dd>tcptraceroute Options to pass to tcpping. </p>
<p> Example value: -e &#8220;sudo /bin/tcptraceroute&#8221;</p>
<dt>timeout</p>
<dd>How long a single &#8216;ping&#8217; takes at maximum </p>
<p> Example value: 15 </p>
<p> Default value: 5</dl>
<p> Supported target-specific variables:</p>
<dl COMPACT>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 5</p>
<dt>port</p>
<dd>The <font SIZE="-1">TCP</font> port the probe should measure. </p>
<p> Example value: 80</dl>
<h2>Authors</h2>
<p>Norman Rasmussen &lt;norman [at] rasmussen.co.za&gt; Patched for Smokeping 2.x compatibility by Anton Chernev &lt;maznio [at] doom.bg&gt;</p>
