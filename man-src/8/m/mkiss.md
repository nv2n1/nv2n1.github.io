---
title: "mkiss(8)"
name: "mkiss"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkiss/"
description: "mkiss – Attach a multi KISS interface"
---

<p>mkiss &#8211; Attach a multi KISS interface</p>
<h2>Synopsis</h2>
<p><code>mkiss [-c] [-f] [-h] [-l] [-s speed] [-p pollrate] [-v] [-x n_ptmx] ttyinterface pty ..</code></p>
<h2>Description</h2>
<p><code>Mkiss</code> allows dual port TNCs or multiple TNCs sharing the same serial port to be used with the Linux AX.25 kernel software. The AX.25 software has no support for dual port TNCs or multiple TNCs charing the same serial line. The different ports are addressed by encoding the port number in the control byte of every kiss frame. <code>Mkiss</code> watches a serial port, and routes kiss frames to/from the pseudo ttys. The other side of the pseudo ttys are then attached with <code>kissattach</code> as normal. </p>
<p> Statistics about the operation of <code>mkiss</code> may be obtained by sending the SIGUSR1 signal to the running program. On reception of such a signal <code>mkiss</code> will print a set of statistics to the system log if logging has been enabled. </p>
<p> Although mention is made of using pseudo ttys as the last arguments, these devices may be normal serial ports. However <code>mkiss</code> provides no way in which to set their speed, the speed must therefore be set by some other method.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></p>
<dd>This enables a one-byte checksum on each incoming and outgoing KISS frame on the serial port. This checksum is used by G8BPQ KISS roms to maintain the integrity of KISS frames.</p>
<dt><code>-f</code></p>
<dd>This enables a 16-bit checksum on each incoming and outgoing KISS frame on the serial port. This checksum is used by Flexnet Node and BayCom Mailbox to maintain the integrity of KISS frames.</p>
<dt><code>-h</code></p>
<dd>Enables hardware handshaking on the serial line to the TNC. The KISS specification states that no hardware flow control shall be used so the default is off. But some KISS implementations do use hardware flow control.</p>
<dt><code>-l</code></p>
<dd>Enables system logging, the default is off.</p>
<dt><code>-s speed</code></p>
<dd>Set the speed of the serial port.</p>
<dt><code>-p pollrate</code></p>
<dd>Enables polling. Polled mode is used by G8BPQ KISS roms to prevent contention on systems where multiple TNCs share the same serial line. Pollrate is interval between polls (in 100ms units).</p>
<dt><code>-v</code></p>
<dd>Display the version.</p>
<dt><code>-x number</code></p>
<dd>This option is for Unix98 PTYs. It allocates &quot;number&quot; ptys; their names are written to stdout. When -x is used, the pty arguments are optional.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1).</p>
<h2>Authors</h2>
<p>Tomi Manninen OH2BNS &lt;oh2bns [at] sral.fi&gt;<br />
 Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;<br />
 Kevin Uhlir N0BEL &lt;kevinu [at] flochart.com&gt;</p>
