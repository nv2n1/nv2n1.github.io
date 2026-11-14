---
title: "slattach(8)"
name: "slattach"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slattach/"
description: "slattach – attach a network interface to a serial line"
---

<p>slattach &#8211; attach a network interface to a serial line</p>
<h2>Synopsis</h2>
<p><code>slattach [-dehlLmnqv] [-c command] [-p proto] [-s speed] [tty]</code></p>
<h2>Description</h2>
<p><code>Slattach</code> is a tiny little program that can be used to put a normal terminal (&quot;serial&quot;) line into one of several &quot;network&quot; modes, thus allowing you to use it for point-to-point links to other computers.</p>
<h2>Options</h2>
<dl>
<dt><code>tty</code></p>
<dd>Path to a serial device like <i>/dev/ttyS*</i>, <i>/dev/cua*</i> or <i>/dev/ptmx</i> to spawn a new pseudo tty.</p>
<dt><code>[-c command]</code></p>
<dd>Execute <code>command</code> when the line is hung up. This can be used to run scripts or re-establish connections when a link goes down.</p>
<dt><code>[-d]</code></p>
<dd>Enable debugging output. Useful when determining why a given setup doesn&#8217;t work.</p>
<dt><code>[-h]</code></p>
<dd>Exit when the carrier is lost. This works on both /dev/tty and /dev/cua devices by directly monitoring the carrier status every 15 seconds.</p>
<dt><code>[-v]</code></p>
<dd>Enable verbose output. Useful in shell scripts.</p>
<dt><code>[-q]</code></p>
<dd>Operate in quiet mode &#8211; no messages at all.</p>
<dt><code>[-l]</code></p>
<dd>Create an UUCP-style lockfile for the device in /var/lock.</p>
<dt><code>[-n]</code></p>
<dd>Equivalent to the &quot;mesg n&quot; command.</p>
<dt><code>[-m]</code></p>
<dd>Do <code>not</code> initialize the line into 8 bits raw mode.</p>
<dt><code>[-e]</code></p>
<dd>Exit right after initializing device, instead of waiting for the line to hang up.</p>
<dt><code>[-L]</code></p>
<dd>Enable 3 wire operation. The terminal is moved into CLOCAL mode, carrier watching is disabled.</p>
<dt><code>[-p proto]</code></p>
<dd>Set a specific kind of protocol to use on the line. The default is set to <code>cslip</code>, i.e. compressed SLIP. Other possible values are <code>slip</code> (normal SLIP), <code>adaptive</code> (adaptive CSLIP/SLIP), <code>ppp</code> (Point-to-Point Protocol) and <code>kiss</code> (a protocol used for communicating with AX.25 packet radio terminal node controllers). The special argument <code>tty</code> can be used to put the device back into normal serial operation. Using &#8216;ppp&#8217; mode is not normally useful as ppp requires an additional ppp daemon <code>pppd</code> to be active on the line. For kiss connections the <code>kissattach</code> program should be used.</p>
<dt><code>[-s speed]</code></p>
<dd>Set a specific line speed, other than the default.</dl>
<p> If no arguments are given, the current terminal line (usually: the login device) is used. Otherwise, an attempt is made to claim the indicated terminal port, lock it, and open it.</p>
<h2>Files</h2>
<p><i>/dev/cua* /var/lock/LCK.* /dev/ttyS* /dev/ptmx</i></p>
<h2>Bugs</h2>
<p>None known.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-kissattach/">kissattach</a>(8), <a href="/docs/linux/man/8-dip/">dip</a>(8) <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/8-sliplogin/">sliplogin</a>(8).</p>
<h2>Authors</h2>
<p>Fred N. van Kempen, &lt;waltje [at] uwalt.nl.mugnet.org&gt;<br />
 Alan Cox, &lt;Alan.Cox [at] linux.org&gt;<br />
 Miquel van Smoorenburg, &lt;miquels [at] drinkel.ow.org&gt;<br />
 George Shearer, &lt;gshearer [at] one.net&gt;<br />
 Yossi Gottlieb, &lt;yogo [at] math.tau.ac.il&gt;</p>
