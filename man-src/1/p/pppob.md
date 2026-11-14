---
title: "pppob(1)"
name: "pppob"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pppob/"
description: "pppob – Barry Project’s program to access the Blackberry modem for pppd"
---

<h2 class="name">NAME</h2>
<p> <code>pppob</code> &#8211; Barry Project&#8217;s program to access the Blackberry modem for pppd </p>
<h2>SYNOPSIS</h2>
<p> <code>pppob</code> [-l filename][-p pin][-P password][-s][-v]</p>
<h2>DESCRIPTION</h2>
<p> <code>pppob</code> is a program suitable for use in pppd&#8217;s pty option file. It talks to an available Blackberry and provides modem access on stdin and stdout.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l filename</code></p>
<dd> Causes verbose debug output from the -v switch to be written to filename instead of stderr.</p>
<dt><code>-p pin</code></p>
<dd> PIN of device to talk with. Only needed if you have more than one Blackberry connected at once.</p>
<dt><code>-P password</code></p>
<dd> Simplistic method to specify device password. In a real application, this would be done using a more secure prompt.</p>
<dt><code>-s</code></p>
<dd> Use Serial mode instead of the default IpModem mode. Older Blackberries used a serial mode based on a similar protocol to what database access uses for retrieving data. Each packet had a size and socket number prepended to the actual modem data. Newer Blackberries have dedicated USB endpoints that behave as read/write points, and do not bother with this size/socket format, and therefore transfer less data across the USB bus. By default, pppob tries to use IpModem mode if proper endpoints are detected, and otherwise falls back to Serial mode. This switch skips IpModem mode entirely and tries Serial mode immediately.</p>
<dt><code>-v</code></p>
<dd> Dump verbose protocol data to stderr during operation. </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>pppob</code> is part of the Barry project.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
