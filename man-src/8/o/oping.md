---
title: "oping(8)"
name: "oping"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oping/"
description: "oping – send ICMP ECHO_REQUEST to network hosts"
---

<p>oping &#8211; send ICMP ECHO_REQUEST to network hosts</p>
<h2>Synopsis</h2>
<p><code>oping</code> [<code>-4</code> | <code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-i</code> <i>interval</i>] <i>host</i> [<i>host</i> [<i>host</i> &#8230;]] </p>
<p> <code>oping</code> [<code>-4</code> | <code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-i</code> <i>interval</i>] <code>-f</code> <i>filename</i> </p>
<p> <code>noping</code> [<code>-4</code> | <code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-i</code> <i>interval</i>] <i>host</i> [<i>host</i> [<i>host</i> &#8230;]] </p>
<p> <code>noping</code> [<code>-4</code> | <code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-i</code> <i>interval</i>] <code>-f</code> <i>filename</i></p>
<h2>Description</h2>
<p><code>oping</code> uses ICMPv4 or ICMPv6 <font SIZE="-1">ECHO_REQUEST</font> packets to measure a hosts reachability and the network latency. In contrast to the original <i><a href="/docs/linux/man/8-ping/">ping</a></i>(8) utility <code>oping</code> can send <font SIZE="-1">ICMP</font> packets to multiple hosts in parallel and wait for all <font SIZE="-1">ECHO_RESPONSE</font> packets to arrive. In contrast to the <code>fping</code> utility (<font SIZE="-1">URL</font> is listed in &#8220;<font SIZE="-1">SEE</font> <font SIZE="-1">ALSO</font>&#8221;) <code>oping</code> can use both, IPv4 and IPv6 transparently and side by side. </p>
<p> <code>noping</code> is an ncurses-based front-end to <i>liboping</i> which displays ping statistics online and highlights aberrant round-trip times if the terminal supports colors.</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code></p>
<dd>Force the use of IPv4.</p>
<dt><code>-6</code></p>
<dd>Force the use of IPv6.</p>
<dt><code>-c</code> <i>count</i></p>
<dd>Send (and receive) <i>count</i> <font SIZE="-1">ICMP</font> packets, then stop and exit.</p>
<dt><code>-i</code> <i>interval</i></p>
<dd>Send one <font SIZE="-1">ICMP</font> packet (per host) each <i>interval</i> seconds. This can be a floating-point number to specify sub-second precision.</p>
<dt><code>-t</code> <i>ttl</i></p>
<dd>Set the <font SIZE="-1">IP</font> Time to Live to <i>ttl</i>. This must be a number between (and including) 1 and 255. If omitted, the value <code>64</code> is used.</p>
<dt><code>-I</code> <i>address</i></p>
<dd>Set the source address to use. You may either specify an <font SIZE="-1">IP</font> number or a hostname. You <code>cannot</code> pass the interface name, as you can with <font SIZE="-1">GNU</font>&#8216;s <i><a href="/docs/linux/man/8-ping/">ping</a></i>(8) &#8211; use the <code>-D</code> option for that purpose.</p>
<dt><code>-D</code> <i>interface name</i></p>
<dd>Set the outgoing network device to use.</p>
<dt><code>-f</code> <i>filename</i></p>
<dd>Instead of specifying hostnames on the command line, read them from <i>filename</i>. If <i>filename</i> is <code>&#8211;</code>, read from <tt>&quot;STDIN&quot;</tt>. </p>
<p> If <i>oping</i> is installed with the SetUID-bit, it will set the effective <font SIZE="-1">UID</font> to the real <font SIZE="-1">UID</font> before opening the file. In the special (but common) case that <i>oping</i> is owned by the super-user (<font SIZE="-1">UID</font>&nbsp;<wbr>0), this means that privileges are temporarily dropped before opening the file, in order to prevent users from reading arbitrary files on the system. </p>
<p> If your system doesn&#8217;t provide <i>saved set-user IDs</i> (this was an optional feature before <font SIZE="-1">POSIX</font>&nbsp;<wbr>2001), the behavior is different because it is not possible to <i>temporarily</i> drop privileges. The alternative behavior is: If the real user <font SIZE="-1">ID</font> (as returned by <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2)) and the effective user <font SIZE="-1">ID</font> (as returned by <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2)) differ, the only argument allowed for this option is &#8220;-&#8221; (i.e. standard input).</p>
<dt><code>-Q</code> <i>qos</i></p>
<dd>Specify the <i>Quality of Service</i> (QoS) for outgoing packets. This is a somewhat tricky option, since the meaning of the bits in the IPv4 header has been revised several times. </p>
<p> The currently recommended method is <i>Differentiated Services</i> which is used in IPv6 headers as well. There are shortcuts for various predefined <i>per-hop behaviors</i> (PHBs):</p>
<dl>
<dd>
<dl>
<dt><code>be</code></p>
<dd>Selects the <i>Best Effort</i> behavior. This is the default behavior.</p>
<dt><code>ef</code></p>
<dd>Selects the <i>Expedited Forwarding</i> (<font SIZE="-1">EF</font>) per-hop behavior, as defined in <i></i><font SIZE="-1"><i>RFC</i></font><i>&nbsp;<wbr>3246</i>. This <font SIZE="-1">PHB</font> is characterised by low delay, low loss and low jitter, i.e. high priority traffic.</p>
<dt><code>va</code></p>
<dd>Selects the <i>Voice Admitted</i> (<font SIZE="-1">VA</font>) per-hop behavior, as defined in <i></i><font SIZE="-1"><i>RFC</i></font><i>&nbsp;<wbr>5865</i>. This traffic class is meant for <i>Voice over </i><font SIZE="-1"><i>IP</i></font><i></i> (VoIP) traffic which uses <i>Call Admission Control</i> (<font SIZE="-1">CAC</font>) for reserving network capacity.</p>
<dt><code>af</code><i>c</i><i>p</i></p>
<dd>Selects one of 12 differentiated services code points (DSCPs), which are organized in four <i>classes</i> with three <i>priorities</i> each. Therefore, <i>c</i> must be a number between 1 through 4 and <i>p</i> must be a number between 1 through 3, for example &#8220;af13&#8221;, &#8220;af22&#8221; and &#8220;af41&#8221;. In each class, the lower priority number takes precedence over the higher priority number.</p>
<dt><code>cs</code><i>n</i></p>
<dd>Selects one of the eight <i>Class Selector</i> PHBs. <i>n</i> is a number between 0 through 7. The class selectors have been defined to be compatible to the <i>Precedence</i> field in the IPv4 header as defined in <i></i><font SIZE="-1"><i>RFC</i></font><i>&nbsp;<wbr>791</i>. Please note that &#8220;cs0&#8221; is synonymous to &#8220;be&#8221;.</dl>
</dl>
<dl>
<dd>The old definition of the same bits in the IPv4 header was as <i>Type of Service</i> (ToS) field, specified in <i></i><font SIZE="-1"><i>RFC</i></font><i>&nbsp;<wbr>1349</i>. It defined four possible values which have appropriate aliases. Please note that this use of the bits is <code>deprecated</code> and the meaning is limited to IPv4!</p>
<dl>
<dt><code>lowdelay</code></p>
<dd>Minimize delay</p>
<dt><code>throughput</code></p>
<dd>Maximize throughput</p>
<dt><code>reliability</code></p>
<dd>Maximize reliability</p>
<dt><code>mincost</code></p>
<dd>Minimize monetary cost</dl>
</dl>
<dl>
<dd>Alternatively, you can also specify the byte manually. You can use either a decimal number (0-255), a hexadecimal number (0x00-0xff) or an octal number (00-0377) using the usual &#8220;0x&#8221; and &#8220;0&#8221; prefixes for hexadecimal and octal respectively. </p>
<p> The printed lines will contain information about the QoS field of received packets if either a non-standard QoS setting was used on outgoing packets or if the QoS byte of incoming packets is not zero. In other words, the QoS information is omitted if both, the outgoing and the incoming QoS bytes are zero. The received byte is always interpreted as <i>Differentiated Services Code Point</i> (<font SIZE="-1">DSCP</font>) and <i>Explicit Congestion Notification</i> (<font SIZE="-1">ECN</font>), even if the deprecated <i>Type of Service</i> (ToS) aliases were used to specify the bits of outgoing packets.</dl>
</dl>
<h2>Colors</h2>
<p>If supported by the terminal, <i>noping</i> will highlight the round-trip times (<font SIZE="-1">RTT</font>) using the colors green, yellow and red. Green signals RTTs that are in the &#8220;expected&#8221; range, yellow marks moderately unusual times and times that differ a lot from the expected value are printed in red. </p>
<p> The information used to categorize round-trip times is the <i>average</i> round-trip time and the <i>standard deviation</i>. RTTs that differ from the average by less than the standard deviation are considered to be &#8220;normal&#8221; and are printed in green. Times that differ from the average more than the standard deviation but less than twice the standard deviation are considered &#8220;moderately unusual&#8221; and are printed in yellow. Times differing more than twice the standard deviation from the average are considered to be &#8220;unusual&#8221; and are printed in red.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ping/">ping</a></i>(8), &lt;<a rel="nofollow" href="http://www.fping.com/">http://www.fping.com/</a>&gt;, <i><a href="/docs/linux/man/3-liboping/">liboping</a></i>(3)</p>
<h2>Author</h2>
<p>liboping is written by Florian &#8220;octo&#8221; Forster &lt;ff at octo.it&gt;. Its homepage can be found at &lt;<a rel="nofollow" href="http://verplant.org/liboping/">http://verplant.org/liboping/</a>&gt;. </p>
<p> Copyright (c) 2005-2011 by Florian &#8220;octo&#8221; Forster.</p>
