---
title: "novnc_server(1)"
name: "novnc_server"
section: "1"
letter: "n"
url: "/docs/linux/man/1-novnc_server/"
description: "novnc_server | noVNC proxy server"
---

<h2 class="name">NAME</h2>
<p> novnc_server | noVNC proxy server </p>
<h2>SYNOPSIS</h2>
<p> <code>novnc_server [&#8211;listen PORT] [&#8211;vnc VNC_HOST:PORT] [&#8211;cert CERT]</code> </p>
<p> Starts the WebSockets proxy and a mini-webserver and provides a cut-and-paste URL to go to. </p>
<p>&nbsp;<wbr>&#8211;listen PORT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Port for proxy/webserver to listen on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Default: 6080<br />
&nbsp;<wbr>&#8211;vnc VNC_HOST:PORT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>VNC server host:port proxy target<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Default: localhost:5900<br />
&nbsp;<wbr>&#8211;cert CERT&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Path to combined cert/key file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Default: self.pem </p>
<h2>AUTHOR</h2>
<p> Joel Martin (github [at] martintribe.org) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-websockify/">websockify</a>(1) </p>
<h2>Index</h2>
