---
title: "kissnetd(8)"
name: "kissnetd"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kissnetd/"
description: "kissnetd – Create a virtual network."
---

<p>kissnetd &#8211; Create a virtual network.</p>
<h2>Synopsis</h2>
<p><code>kissnetd [-f size] [-v] [-p &lt;num&gt; | tty&#8230; ]</code></p>
<h2>Description</h2>
<p><code>Kissnetd</code> allows the creation of a virtual network of AX.25 systems that use the KISS protocol. Each tty named on the command line is opened and any KISS frames received on tty is copied to the other ttys. This allows a number of AX.25 systems to share the same packets.</p>
<h2>Options</h2>
<dl>
<dt><code>-p num</code></p>
<dd>Automaticaly allocate num Unix98 slave pty&#8217;s via /dev/ptmx. These are written to stdout and could be parsed by your startup scripts.</p>
<dt><code>-f size</code></p>
<dd>This sets the maximum KISS frame size that the program will handle. The default is 512 bytes which will be adequate under most circumstances.</p>
<dt><code>-v</code></p>
<dd>Enables verbose mode, tracing of data passed is sent to standard output.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8), <code><a href="/docs/linux/man/8-kissparms/">kissparms</a></code>(8), <code><a href="/docs/linux/man/8-mkiss/">mkiss</a></code>(8).</p>
<h2>Author</h2>
<p>Frederic Rible F1OAT &lt;frible [at] teaser.fr&gt;</p>
