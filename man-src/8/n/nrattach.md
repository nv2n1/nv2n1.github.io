---
title: "nrattach(8)"
name: "nrattach"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nrattach/"
description: "nrattach – Start a NET/ROM interface"
---

<p>nrattach &#8211; Start a NET/ROM interface</p>
<h2>Synopsis</h2>
<p><code>nrattach [-i inetaddr] [-m mtu] [-v] port</code></p>
<h2>Description</h2>
<p><code>Nrattach</code> takes many of the parameters for the port from the <a href="/docs/linux/man/5-nrports/">nrports</a>(5) file. The paclen parameter is used for the device mtu unless overridden by a value on the command line. The port argument is the name of a port as given in the <a href="/docs/linux/man/5-nrports/">nrports</a>(5) file. </p>
<p> <code>Nrattach</code> tries to find the first free NET/ROM device in the system. The devices checked are nr0, nr1, nr2 and nr3 in that order. If no free NET/ROM device is available an error is generated and the program terminates.</p>
<h2>Options</h2>
<dl>
<dt><code>-i inetaddr</code></p>
<dd>Set the internet address of the interface. This address may either be a dotted decimal address or a host name.</p>
<dt><code>-m mtu</code></p>
<dd>Sets the mtu of the interface. If this value is not given then the value is taken from the paclen parameter in nrports.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-nrparms/">nrparms</a></code>(4), <code><a href="/docs/linux/man/5-nrports/">nrports</a></code>(5), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8).</p>
<h2>Bugs</h2>
<p>The program can be run many times with the same arguments creating many instances of the same attributes on different devices. Not a good idea.</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
