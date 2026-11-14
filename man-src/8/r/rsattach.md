---
title: "rsattach(8)"
name: "rsattach"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rsattach/"
description: "rsattach – Start a Rose interface"
---

<p>rsattach &#8211; Start a Rose interface</p>
<h2>Synopsis</h2>
<p><code>rsattach [-i inetaddr] [-v] port</code></p>
<h2>Description</h2>
<p><code>Rsattach</code> takes many of the parameters for the port from the <a href="/docs/linux/man/5-rsports/">rsports</a>(5) file. The port argument is the name of a port as given in the <a href="/docs/linux/man/5-rsports/">rsports</a>(5) file. </p>
<p> <code>Rsattach</code> tries to find the free Rose device in the system. The device name checked is rose0. If no free Rose device is available an error is generated and the program terminates.</p>
<h2>Options</h2>
<dl>
<dt><code>-i inetaddr</code></p>
<dd>Set the internet address of the interface. This address may either be a dotted decimal address or a host name.</p>
<dt><code>-v</code></p>
<dd>Display the version.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/4-rsparms/">rsparms</a></code>(4), <code><a href="/docs/linux/man/5-rsports/">rsports</a></code>(5), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8).</p>
<h2>Bugs</h2>
<p>The program can be run many times with the same arguments creating many instances of the same attributes on different devices. Not a good idea.</p>
<h2>Author</h2>
<p>Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;</p>
