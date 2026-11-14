---
title: "ax25mond(8)"
name: "ax25mond"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ax25mond/"
description: "ax25mond – dump the AX.25 network traffic and and provide sockets where the received data will be retransmitted"
---

<p>ax25mond &#8211; dump the AX.25 network traffic and and provide sockets where the received data will be retransmitted</p>
<h2>Synopsis</h2>
<p><code>ax25mond [-v|&#8211;version]</code></p>
<h2>Description</h2>
<p><code>Ax25mond</code> will first read it&#8217;s configuration file /etc/ax25/ax25mond.conf. It will then wait for connects on the sockets specified in this file. When connected, it will transmit all data which it has received on the AX.25 monitor socket.</p>
<h2>Options</h2>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd>Displays the version number and some copyright information.</dl>
<h2>Author</h2>
<p>Johann Hanne, DH3MB &lt;jonny [at] baycom.org&gt;</p>
