---
title: "airserv-ng(1)"
name: "airserv-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airserv-ng/"
description: "airserv-ng – a wireless card server"
---

<h2 class="name">NAME</h2>
<p> airserv-ng &#8211; a wireless card server </p>
<h2>SYNOPSIS</h2>
<p> <code>airserv-ng</code> &lt;options&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>airserv-ng</code> is a wireless card server which allows multiple wireless application programs to independently use a wireless card via a client-server TCP network connection. All operating system and wireless card driver specific code is incorporated into the server. This eliminates the need for each wireless application to contain the complex wireless card and driver logic. It is also supports multiple operating systems.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Shows the help screen.</p>
<dt><i>-p &lt;port&gt;</i></p>
<dd> TCP port to listen on (by default: 666).</p>
<dt><i>-d &lt;iface&gt;</i></p>
<dd> Wifi interface to use.</p>
<dt><i>-c &lt;chan&gt;</i></p>
<dd> Lock interface to this channel.</p>
<dt><i>-v &lt;level&gt;</i></p>
<dd> Debug level. There are 3 debug levels. Debug level of 1 shows client connection/disconnection (default). Debug level of 2 shows channel change requests and invalid client command requests in addition to the debug level 1 messages. Debug level of 3 displays a message each time a packet (and its length) is sent to the client. It also include messages from level 2 (and 1).</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airodump-ng/">airodump-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airtun-ng/">airtun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
<h2>Index</h2>
