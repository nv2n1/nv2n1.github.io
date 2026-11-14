---
title: "in-rshd(8)"
name: "in-rshd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in-rshd/"
description: "rshd – remote shell server"
---

<p><code>rshd</code> &#8211; remote shell server</p>
<h2>Synopsis</h2>
<p><code>rshd</code> [-<code>ahlnL</code> ]</p>
<h2>Description</h2>
<p>The <code>rshd</code> server is the server for the <a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) routine and, consequently, for the <a href="/docs/linux/man/1-rsh/">rsh</a>(1) program. The server provides remote execution facilities with authentication based on privileged port numbers from trusted hosts. </p>
<p> The <code>rshd</code> server listens for service requests at the port indicated in the &#8220;cmd&#8221; service specification; see <a href="/docs/linux/man/5-services/">services</a>(5). When a service request is received the following protocol is initiated: </p>
<ol>
<li> The server checks the client&#8217;s source port. If the port is not in the range 512-1023, the server aborts the connection.
<li> The server reads characters from the socket up to a null (`
