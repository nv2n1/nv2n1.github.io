---
title: "spattach(8)"
name: "spattach"
section: "8"
letter: "s"
url: "/docs/linux/man/8-spattach/"
description: "kissattach, spattach – Attach a KISS or 6PACK interface"
---

<p>kissattach, spattach &#8211; Attach a KISS or 6PACK interface</p>
<h2>Synopsis</h2>
<p><code>kissattach [-b] [-6] [-l] [-m mtu] [-v] tty port [inetaddr]</code> </p>
<p> <code>spattach [-b] [-l] [-m mtu] [-v] tty port [inetaddr]</code></p>
<h2>Description</h2>
<p>Attach a KISS or a 6PACK interface to what is normally a tty line connected to a TNC in KISS or 6PACK mode. This program will turn itself into a background process. To down an interface send its attach process a SIGTERM. </p>
<p> <code>Kissattach</code> takes many of the parameters for the port from the <a href="/docs/linux/man/5-axports/">axports</a>(5) file. If the speed parameter in the file is not equal to zero then it is used for the serial port speed, a zero value means that no speed is set. The paclen parameter is used for the device mtu unless overridden by a value on the command line. </p>
<p> The tty argument will typically be that of a serial port with a KISS or 6PACK TNC attached, although it could be a pseudo tty or a KISS port emulator such as an SCC card. Kissattach supports BSD-style pseudo-terminals as well as the Unix98 pty&#8217;s. If the tty argument is &quot;/dev/ptmx&quot;, then Unix98 behaviour will automaticaly take effekt. With Unix98 pty&#8217;s, the slave tty name could not be forseen. That&#8217;s why kissattach will print the corresponding slave pty name as a separate line on stdout. </p>
<p> The port argument is the name of a port as given in the <a href="/docs/linux/man/5-axports/">axports</a>(5) file. </p>
<p> The optional inetaddr argument is the IP address of the new interface. Some time it was mandatory argument (although due to historical reasons this restriction is lifted if the old -i option is used). But there&#8217;s really not a need for the interface to have an IP address assigned to.</p>
<h2>Options</h2>
<dl>
<dt><code>-6</code></p>
<dd>Use the 6PACK line discipline instead of KISS. This is the default if the program is called as spattach.</p>
<dt><code>-i inetaddr</code></p>
<dd>Set the internet address of the interface. This address may either be a dotted decimal address or a host name. This option is now depreciated and the program will complain about it, though still work.</p>
<dt><code>-l</code></p>
<dd>Log messages to the system log, the default is not to.</p>
<dt><code>-b</code></p>
<dd>Allow broadcasts on the interface (default no &#8211; because for e.g. samba broadcasts are a pain..)</p>
<dt><code>-m mtu</code></p>
<dd>Sets the mtu of the interface. If this value is not given then the value is taken from the paclen parameter in axports.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-axparms/">axparms</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8).</p>
<h2>Author</h2>
<pre>Alan Cox GW4PTS &lt;alan [at] cymru.net&gt;
<br>
Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</pre>
