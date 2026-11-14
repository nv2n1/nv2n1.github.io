---
title: "m6pack(8)"
name: "m6pack"
section: "8"
letter: "m"
url: "/docs/linux/man/8-m6pack/"
description: "m6pack – Attach multiples 6PACK interfaces"
---

<p>m6pack &#8211; Attach multiples 6PACK interfaces</p>
<h2>Synopsis</h2>
<p><code>m6pack [-l] [-s speed] [-x n_ptmx] [-v] ttyinterface pty ..</code></p>
<h2>Description</h2>
<p><code>m6pack</code> allows multiple 6PACK TNCs sharing the same serial port to be used with the Linux AX.25 kernel software. The AX.25 softare has no support for multiple TNCs sharing the same serial line. The different ports are addressed by encoding the port number in the control byte of every 6pack frame. <code>m6pack</code> watches a serial port, and routes 6pack frames to/from the pseudo ttys. The other side of the pseudo ttys are then attached with <code>spattach</code> as normal. </p>
<p> Statistics about the operation of <code>m6pack</code> may be obtained by sending the SIGUSR1 signal to the running program. On reception of such a signal <code>m6pack</code> will print a set of statistics to the system log if logging has been enabled. </p>
<p> Although mention is made of using pseudo ttys as the last arguments, these devices may be normal serial ports. However <code>m6pack</code> provides no way in which to set their speed, the speed must therefore be set by some other method.</p>
<h2>Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>Enables system logging, the default is off.</p>
<dt><code>-s speed</code></p>
<dd>Set the speed of the serial port.</p>
<dt><code>-v</code></p>
<dd>Display the version.</p>
<dt><code>-x number</code></p>
<dd>This option is for Unix98 PTYs. It allocates &quot;number&quot; ptys; their names are written to stdout. When -x is used, the pty arguments are optional.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-spattach/">spattach</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1).</p>
<h2>Authors</h2>
<p>I�aki Arenaza EB2EBU &lt;iarenaza [at] escomposlinux.org&gt;, based in the work by:<br />
 Tomi Manninen OH2BNS &lt;oh2bns [at] sral.fi&gt;<br />
 Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;<br />
 Kevin Uhlir N0BEL &lt;kevinu [at] flochart.com&gt;</p>
