---
title: "in-rexecd(8)"
name: "in-rexecd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-rexecd/"
description: "rexecd – remote execution server"
---

<p><code>rexecd</code> &#8211; remote execution server</p>
<h2>Synopsis</h2>
<p><code>rexecd</code> [ <code>-D</code> ]</p>
<h2>Options</h2>
<p><code>Rexec</code> accepts one option: </p>
<dl>
<dt><code>-D</code></p>
<dd>Disable reverse DNS look up and in the log will be used client IP addresses.</dl>
</dl>
<h2>Description</h2>
<p><code>Rexecd</code> is the server for the <a href="/docs/linux/man/3-rexec/">rexec</a>(3) routine. The server provides remote execution facilities with authentication based on user names and passwords. <code>Rexecd</code> listens for service requests at the port indicated in the &#8220;exec&#8221; service specification; see <a href="/docs/linux/man/5-services/">services</a>(5). When a service request is received the following protocol is initiated: </p>
<ol>
<li> The server reads characters from the socket up to a NUL (`
