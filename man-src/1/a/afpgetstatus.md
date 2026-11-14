---
title: "afpgetstatus(1)"
name: "afpgetstatus"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afpgetstatus/"
description: "afpgetstatus – Get simple status information from an AFP server without logging into it."
---

<h2>NAME</h2>
<p> afpgetstatus &#8211; Get simple status information from an AFP server without logging into it.</p>
<h2>SYNOPSIS</h2>
<p> <i>afpgetstatus [afp_url|ipaddress[:port]]R </p>
<p> </i></p>
<h2>DESCRIPTION</h2>
<p> afpcmd is a command-line tool that parses and prints the status information of an AFP server. It does this without having to login to a server. </p>
<p> It is a response to the DSI GetStatus request (which is the same as the AFP FPGetSrvrInfo). </p>
<p> It only handles IPv4 addresses. </p>
<h2>OPTIONS</h2>
<p> <code>afp_url</code> an AFP url in the form of <i><a href="afp://servername:port/">afp://servername:port/</a></i>. Any other AFP url fields (username, volume name, etc) are ignored. </p>
<p> <code>ipaddress</code> the IP address of the server </p>
<p> <code>port</code> the TCP port to connect to (optional) </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the afpfs-ng-devel [at] sf.net mailing list.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afpcmd/">afpcmd</a></code>(1) </p>
<h2>Index</h2>
