---
title: "unhide-tcp(8)"
name: "unhide-tcp"
section: "8"
letter: "u"
url: "/docs/linux/man/8-unhide-tcp/"
description: "unhide-tcp — forensic tool to find hidden TCP/UDP ports"
---

<p>unhide-tcp &#8212; forensic tool to find hidden TCP/UDP ports</p>
<h2>Synopsis</h2>
<p><code>unhide-tcp [options]</code></p>
<h2>Description</h2>
<p><code>unhide-tcp</code> is a forensic tool that identifies TCP/UDP ports that are listening but are not listed by /sbin/ss (or alternatively by /bin/netstat) through brute forcing of all TCP/UDP ports available.<br />
 Note1 : On FreeBSD ans OpenBSD, netstat is allways used as iproute2 doesn&#8217;t exist on these OS. In addition, on FreeBSD, sockstat is used instead of fuser. Note2 : If iproute2 is not available on the system, option -n or -s SHOULD be given on the command line. </p>
<h2>Options</h2>
<dl>
<dt><code>-h &#8211;help</code></p>
<dd>Display help</p>
<dt><code>&#8211;brief</code></p>
<dd>Don&#8217;t display warning messages, that&#8217;s the default behavior.</p>
<dt><code>-f &#8211;fuser</code></p>
<dd>Display fuser output (if available) for the hidden port On FreeBSD, instead of fuser command, displays the output of the sockstat command for the hidden port.</p>
<dt><code>-l &#8211;lsof</code></p>
<dd>Display lsof output (if available) for the hidden port</p>
<dt><code>-n &#8211;netstat</code></p>
<dd>Use /bin/netstat instead of /sbin/ss. On system with many opened ports, this can slow down the test dramatically.</p>
<dt><code>-s &#8211;server</code></p>
<dd>Use a very quick strategy of scanning. On system with a lot of opened ports, it is hundreds times faster than ss method and ten thousands times faster than netstat method.</p>
<dt><code>-o &#8211;log</code></p>
<dd>Write a log file (unhide-tcp-AAAA-MM-DD.log) in the current directory.</p>
<dt><code>-V &#8211;version</code></p>
<dd>Show version and exit</p>
<dt><code>-v &#8211;verbose</code></p>
<dd>Be verbose, display warning message (default : don&#8217;t display). This option may be repeated more than once.</dl>
<h3>Exit status:</h3>
<dl>
<dt>0</p>
<dd>if no hidden port is found,</p>
<dt>4</p>
<dd>if one or more hidden TCP port(s) is(are) found,</p>
<dt>8</p>
<dd>if one or more hidden UDP port(s) is(are) found,</p>
<dt>12</p>
<dd>if one or more hidden TCP and UDP ports are found.</dl>
<h2>See Also</h2>
<p>unhide (8).</p>
<h2>Author</h2>
<p>This manual page was written by Francois Marier francois [at] debian.org and Patrick Gouin. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or any later version published by the Free Software Foundation.</p>
<h2>License</h2>
<p>License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
