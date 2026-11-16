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
<dt><code>-h &#8211;help</code></dt>
<dd>Display help</dd>
<dt><code>&#8211;brief</code></dt>
<dd>Don&#8217;t display warning messages, that&#8217;s the default behavior.</dd>
<dt><code>-f &#8211;fuser</code></dt>
<dd>Display fuser output (if available) for the hidden port On FreeBSD, instead of fuser command, displays the output of the sockstat command for the hidden port.</dd>
<dt><code>-l &#8211;lsof</code></dt>
<dd>Display lsof output (if available) for the hidden port</dd>
<dt><code>-n &#8211;netstat</code></dt>
<dd>Use /bin/netstat instead of /sbin/ss. On system with many opened ports, this can slow down the test dramatically.</dd>
<dt><code>-s &#8211;server</code></dt>
<dd>Use a very quick strategy of scanning. On system with a lot of opened ports, it is hundreds times faster than ss method and ten thousands times faster than netstat method.</dd>
<dt><code>-o &#8211;log</code></dt>
<dd>Write a log file (unhide-tcp-AAAA-MM-DD.log) in the current directory.</dd>
<dt><code>-V &#8211;version</code></dt>
<dd>Show version and exit</dd>
<dt><code>-v &#8211;verbose</code></dt>
<dd>Be verbose, display warning message (default : don&#8217;t display). This option may be repeated more than once.</dd></dl>
<h3>Exit status:</h3>
<dl>
<dt>0</dt>
<dd>if no hidden port is found,</dd>
<dt>4</dt>
<dd>if one or more hidden TCP port(s) is(are) found,</dd>
<dt>8</dt>
<dd>if one or more hidden UDP port(s) is(are) found,</dd>
<dt>12</dt>
<dd>if one or more hidden TCP and UDP ports are found.</dd></dl>
<h2>See Also</h2>
<p>unhide (8).</p>
<h2>Author</h2>
<p>This manual page was written by Francois Marier francois [at] debian.org and Patrick Gouin. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or any later version published by the Free Software Foundation.</p>
<h2>License</h2>
<p>License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
