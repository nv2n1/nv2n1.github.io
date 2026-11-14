---
title: "nrsdrv(8)"
name: "nrsdrv"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nrsdrv/"
description: "nrsdrv – KISS to NET/ROM serial converter"
---

<p>nrsdrv &#8211; KISS to NET/ROM serial converter</p>
<h2>Synopsis</h2>
<p><code>nrsdrv [-f] [-l] [-s speed] [-v] kissdev nrsdev</code></p>
<h2>Description</h2>
<p><code>Nrsdrv</code> is a program designed to convert from the KISS protocol to the NET/ROM serial protocol used by real NET/ROM&#8217;s and TheNet&#8217;s. The protocols are fairly similar, although the NET/ROM serial protocol does include a one byte checksum which KISS does not. </p>
<p> Typically <code>nrsdrv</code> will be attached to one end of a pseudo-tty of which the other end has been attached to a KISS capable program. The NET/ROM device will probably be a real serial port attached to a TNC or a Hexipus. The full specification of the NET/ROM serial protocol can be found in the original Software 2000 documentation that accompanied NET/ROMs.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Flow control enabled for use with a Hexipus, the default is disabled. See the file hexipus.txt in the source distribution for wiring details. </p>
<dt><code>-l</code></p>
<dd>Log messages to the system log, the default is not to.</p>
<dt><code>-s speed</code></p>
<dd>Sets the speed of both interfaces. If no value is specified then no speed will be set.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>Bugs</h2>
<p>None known.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4).</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
