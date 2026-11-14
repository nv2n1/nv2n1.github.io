---
title: "quota_nld(8)"
name: "quota_nld"
section: "8"
letter: "q"
url: "/docs/linux/man/8-quota_nld/"
description: "quota_nld – quota netlink message daemon"
---

<p>quota_nld &#8211; quota netlink message daemon</p>
<h2>Synopsis</h2>
<p><code>quota_nld</code> [[ <code>-D</code> | <code>-C</code> ][ <code>-F</code> ][ <code>-b</code> ]]</p>
<h2>Description</h2>
<p><code>quota_nld</code> listens on netlink socket and processes received quota warnings. By default <code>quota_nld</code> forwards warning messages to both the system&#8217;s DBUS (so that the desktop manager can display a dialog) and the last-accessed terminal of the user to whom each warning is directed. Either of these destinations can be disabled with the <code>-D</code> and <code>-C</code> options, respectively. In the case of the user&#8217;s terminal, quota messages about falling below the hard and soft limits are not sent unless the <code>-b</code> option is specified. In the case of the DBUS, all quota messages are sent. Note, that you have to enable the kernel support for sending quota messages over netlink (in Filesystems-&gt;Quota menu). </p>
<h2>Options</h2>
<dl>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version of quota tools and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a usage message and exit.</p>
<dt><code>-D, &#8211;no-dbus</code></p>
<dd>Do not forward quota warnings to DBUS.</p>
<dt><code>-C, &#8211;no-console</code></p>
<dd>Do not print quota warnings to the user&#8217;s last-accessed terminal.</p>
<dt><code>-b, &#8211;print-below</code></p>
<dd>If quota warnings are printed to users&#8217; terminals, include messages about falling below their hard and soft limits.</p>
<dt><code>-F, &#8211;foreground</code></p>
<dd>Run daemon in foreground (may be useful for debugging purposes). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), <code>dbus.freedesktop.org</code> </p>
