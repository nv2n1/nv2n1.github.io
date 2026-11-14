---
title: "bing(8)"
name: "bing"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bing/"
description: "bing – compute point to point throughput using two sizes of ICMP ECHO_REQUEST packets to pairs of remote hosts."
---

<p><code>bing</code> &#8211; compute point to point throughput using two sizes of ICMP ECHO_REQUEST packets to pairs of remote hosts.</p>
<h2>Synopsis</h2>
<p><code>bing</code> [<code>dDnrRPvVwz</code>] [<code>-c</code> <i>count</i>] [<code>-e</code> <i>samples</i>] [<code>-f</code> <i>samplefile</i>] [<code>-i</code> <i>wait</i>] [<code>-p</code> <i>pattern</i>] [<code>-s</code> <i>small packetsize</i>] [<code>-S</code> <i>big packetsize</i>] <i>host1 host2</i> [<i>&#8230;</i>]</p>
<h2>Description</h2>
<p><code>Bing</code> determines bandwidth on a point-to-point link by sending ICMP ECHO_REQUEST packets and measuring their roundtrip times for different packet sizes on each end of the link. </p>
<p> <i>host1</i> is supposed to be the nearest end of the link, while <i>host2</i> is the other end. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-c</code> <i>count</i></p>
<dd>Stop after <i>count</i> resets of the stats. Useful only in conjunction with the <code>-e</code> option. Defaults to 1.</p>
<dt><code>-d</code></p>
<dd>Set the SO_DEBUG option on the socket being used.</p>
<dt><code>-D</code></p>
<dd>Display the measured throughput at every received packet. By default, it is displayed only when the computed value changes, which itself changes only when the minimum roundtrip time for one of the packet sizes changes.</p>
<dt><code>-e</code> <i>samples</i></p>
<dd>Reset stats after sending <i>samples</i> ECHO_REQUEST packets.</p>
<dt><code>-f</code> <i>samplefile</i></p>
<dd>Saves the bandwidth measurements to the file <i>samplefile</i>.</p>
<dt><code>-i</code> <i>wait</i></p>
<dd>Wait <i>wait</i> seconds <i>for each</i> ECHO_REPLY packet. The default is to wait for four seconds.</p>
<dt><code>-n</code></p>
<dd>Numeric output only. No attempt will be made to lookup symbolic names for host addresses.</p>
<dt><code>-P</code></p>
<dd>Be pedantic regarding round-trip times. </p>
<p> Normally, <code>bing</code> assumes that the roundtrip time for a small packet should always be smaller than the roundtrip time for a big packet to the same host, that for a given size the roundtrip time for <code>host1</code> should always be smaller than the roundtrip time for <code>host2</code>, and that the increase in the roundtrip time between <code>host1</code> and <code>host2</code> should always be bigger for big packets than for small packets. </p>
<p> <code>Bing</code> takes advantage of this to better determine the minimum roundtrip times. </p>
<p> Option <code>-P</code> disables this behaviour, in the unlikely event it could be of any use someday. Even IP/X25 links are not weird enough to require this, though.</p>
<dt><code>-p</code> <i>pattern</i></p>
<dd>You may specify up to 16 &#8220;pad&#8221; bytes to fill out the packet you send. This is useful for diagnosing data-dependent problems in a network. For example, &#8220;-p ff&#8221; will cause the sent packet to be filled with all ones.</p>
<dt><code>-R</code></p>
<dd>Record route. Includes the RECORD_ROUTE option in the ECHO_REQUEST packet and displays the route buffer on returned packets. Note that the IP header is only large enough for nine such routes. Many hosts ignore or discard this option.</p>
<dt><code>-r</code></p>
<dd>Bypass the normal routing tables and send directly to a host on an attached network. If the host is not on a directly-attached network, an error is returned. This option can be used to ping a local host through an interface that has no route through it (e.g., after the interface was dropped by <a href="/docs/linux/man/8-routed/">routed</a>(8)).</p>
<dt><code>-s</code> <i>small packetsize</i></p>
<dd>Specifies the number of data bytes to be sent in the small packets. The default and minimum value is 44.</p>
<dt><code>-S</code> <i>big packetsize</i></p>
<dd>Specifies the number of data bytes to be sent in the big packets. The default is 108. The size should be chosen so that big packet roundtrip times are long enough to be accurately measured (depending on clock resolution and number of hops).</p>
<dt><code>-u</code> <i>size increment</i></p>
<dd>Specifies that <code>bing</code> should start sending packets of the size of <i>small packetsize</i> and then increase the size by <i>size increment</i> until it reaches <i>big packetsize</i>.</p>
<dt><code>-v</code></p>
<dd>Verbose output. ICMP packets other than ECHO_RESPONSE that are received are listed.</p>
<dt><code>-V</code></p>
<dd>Very verbose output. The roundtrip time of each received echo is displayed.</p>
<dt><code>-w</code></p>
<dd>Display possible warnings about roundtrip times all the time. By default, warnings are printed only at the end.</p>
<dt><code>-z</code></p>
<dd>Fill packets with uncompressible (pseudo-random) data.</dl>
<p> Round-trip times and packet loss statistics are computed. If duplicate packets are received, they are not included in the packet loss calculation, although the round trip time of these packets is used in calculating the minimum/average/maximum round-trip time numbers. When the specified number of loops have been made or if the program is terminated with a SIGINT, a brief summary is displayed. </p>
<p> This program is intended for use in network testing, measurement and management. Because of the load it can impose on the network, it is unwise to use <code>bing</code> during normal operations or from automated scripts.</p>
<h2>Bugs</h2>
<p>Many Hosts and Gateways ignore the RECORD_ROUTE option. </p>
<p> The maximum IP header length is too small for options like RECORD_ROUTE to be completely useful. There&#8217;s not much that that can be done about this, however. </p>
<p> Some of the final stats (average throughputs) almost never give a even marginally correct result.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-netstat/">netstat</a>(1), <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8), <a href="/docs/linux/man/8-ping/">ping</a>(8), <a href="/docs/linux/man/8-routed/">routed</a>(8), <a href="/docs/linux/man/8-traceroute/">traceroute</a>(8)</p>
<h2>Author</h2>
<p>Pierre Beyssac &lt;pb [at] fasterix.freenix.fr&gt; </p>
<p> Port to Windows: Francois Gouget &lt;fgouget [at] mygale.org&gt;</p>
