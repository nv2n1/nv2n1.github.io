---
title: "fcping(8)"
name: "fcping"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcping/"
description: "fcping – Fibre Channel Ping (ELS ECHO) tool"
---

<p>fcping &#8211; Fibre Channel Ping (ELS ECHO) tool</p>
<h2>Synopsis</h2>
<p><code>fcping</code> [-fqx] [ -i <i>interval</i> ] [ -c <i>count</i> ] [ -s <i>size</i> ] -h <i>source</i> <i>target</i> </p>
<p> source = <i>interface</i> | <i>MAC</i> | <i>WWPN</i> | <i>FC-ID</i> </p>
<p> target = -P <i>WWPN</i> | -N <i>WWPN</i> | -F <i>FC-ID</i></p>
<h2>Description</h2>
<p>The <code>fcping</code> command performs the Fibre Channel FC-LS-2 ECHO ELS command and displays the reply. The max payload for <code>fcping</code> is 2108 bytes. When no <code>-c</code> is given, <code>fcping</code> will continue until user interrupts.</p>
<h2>Options</h2>
<p><code>-f</code></p>
<dl>
<dd>Flood ping</dl>
<p> <code>-q</code></p>
<dl>
<dd>Quiet! just print summary</dl>
<p> <code>-x</code></p>
<dl>
<dd>Hex dump of responses</dl>
<p> <code>-i</code> <i>interval</i></p>
<dl>
<dd>Wait <i>interval</i> seconds between each ping</dl>
<p> <code>-c</code> <i>count</i></p>
<dl>
<dd>Stop after sending <i>count</i> pings</dl>
<p> <code>-h</code> <i>source</i></p>
<dl>
<dd>Source is <i>interface</i> like ethX, <i>MAC</i> address, <i>WWPN</i>, or <i>FC-ID</i></dl>
<p> <code>-s</code> <i>size</i></p>
<dl>
<dd>Byte-length of ping request payload (max 2108)</dl>
<p> <code>-F</code> <i>FC-ID</i></p>
<dl>
<dd>Destination port ID</dl>
<p> <code>-P</code> <i>WWPN</i></p>
<dl>
<dd>Destination world-wide port name</dl>
<p> <code>-N</code> <i>WWNN</i></p>
<dl>
<dd>Destination world-wide node name</dl>
<h2>Examples</h2>
<p>Sends ELS ECHO to Port FC-ID 0xbf0027 from interface n0.170 with max 3 pings. </p>
<dl>
<dd>
<pre>fcping -c 3 -h n0.170 -F 0xbf0027</pre>
</dl>
<dl>
<dd>
<pre>sending echo to 0xBF0027
echo 1 accepted 16.170 ms
echo 2 accepted 7.053 ms
echo 3 accepted 6.803 ms
3 frames sent, 3 received 0 errors, 0.000% loss, avg. rt time 10.009 ms</pre>
</dl>
<p> Sends ELS ECHO to WWNN 0x1000001B213C9DDA from interface n0.170 with max 3 pings and payload size 1500 bytes </p>
<dl>
<dd>
<pre>fcping -c 3 -h n0.170 -s 1500 -N 0x1000001B213C9DDA</pre>
</dl>
<dl>
<dd>
<pre>sending echo to 0xBF0027
echo 1 accepted 6.597 ms
echo 2 accepted 6.925 ms
echo 3 accepted 12.419 ms
3 frames sent, 3 received 0 errors, 0.000% loss, avg. rt time 8.647 ms</pre>
</dl>
<p> Sends ELS ECHO to WWNN 0x1000001B213C9DDA from interface n0.170 continuously with payload of 32 bytes and hex-dump the reply to the screen </p>
<dl>
<dd>
<pre>fcping -x -h n0.170 -s 32 -N 0x1000001B213C9DDA</pre>
</dl>
<dl>
<dd>
<pre>sending echo to 0xBF0027
echo 1 accepted 6.937 ms
response length 32
 0 02000000 00000001 00010203 04050607
 10 08090a0b 0c0d0e0f 10111213 14151617</pre>
</dl>
<dl>
<dd>
<pre>echo 2 accepted 6.923 ms
response length 32
 0 02000000 00000002 00010203 04050607
 10 08090a0b 0c0d0e0f 10111213 14151617</pre>
</dl>
<dl>
<dd>
<pre>echo 3 accepted 84.929 ms
response length 32
 0 02000000 00000003 00010203 04050607
 10 08090a0b 0c0d0e0f 10111213 14151617</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fcoeadm/">fcoeadm</a></code>(8)</p>
<h2>Support</h2>
<p><code>fcping</code> is part of the <i>fcoe-utils</i> package, maintained through the <i>Open-FCoE</i> project. Resources for both developers and users can be found at the <i>Open-FCoE</i> website <a rel="nofollow" href="http://open-fcoe.org/.">http://open-fcoe.org/.</a></p>
