---
title: "nullmodem(1)"
name: "nullmodem"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nullmodem/"
description: "nullmodem – a Utility to loopback Pseudo-Terminals"
---

<h2>NAME</h2>
<p> nullmodem &#8211; a Utility to loopback Pseudo-Terminals</p>
<h2>SYNOPSIS</h2>
<p> <code>nullmodem [-F] [-V] [-q] [-r] [-m] tty&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nullmodem</code> creates a virtual network of Pseudo-Terminals. It can be used as an adapter to connect two programs that normally need serial interface cards. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F, &#8211;foreground</code></dt>
<dd> Unlike normal operation, nullmodem will not detach from the terminal when given this option. Some debugging informations will be visible. </dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Start quietly &#8211; for init scripts. </dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Print debug info. </dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print the version number and exit. </dd>
<dt><code>-r, &#8211;realtime</code></dt>
<dd> Start with realtime priority (i.e. use the round-robin scheduler). This requires nullmodem to run with root privileges. </dd>
<dt><code>-m, &#8211;memorylock</code></dt>
<dd> Lock the executable of nullmodem to RAM. This keeps nullmodem from being swapped out. </dd>
<dt><code>&#8211;setuid n</code></dt>
<dd> Set the UserID (UID) of the pseudo terminal spacial files to n. </dd>
<dt><code>&#8211;setgid n</code></dt>
<dd> Set the GroupID (GID) of the pseudo terminal spacial files to n. </dd>
<dt><code>&#8211;blocking</code></dt>
<dd> Use blocking IO to handle the interfaces (default: NONBLOCKing). </dd>
</dl>
<h2>AUTHOR</h2>
<p> Juergen Rinas &lt;jrinas [at] gmx.de&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-kissnetd/">kissnetd</a></code>(8), <code><a href="/docs/linux/man/3-openpty/">openpty</a></code>(3) </p>
<h2>Index</h2>
