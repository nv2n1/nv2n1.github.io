---
title: "nwsfind(1)"
name: "nwsfind"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwsfind/"
description: "nwsfind – Find a NetWare Server"
---

<h2>NAME</h2>
<p> nwsfind &#8211; Find a NetWare Server</p>
<h2>SYNOPSIS</h2>
<p> <code>nwsfind</code> [ <code>-t</code> <i>type</i> ] [ <i>name</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>nwsfind</code> searches for a NetWare server and finds a route to this server. nwsfind was written to be setuid root. It is called from within the ncp library, so that it is possible that normal users use the utilities. </p>
<h2>OPTIONS</h2>
<p> <code>name</code></p>
<dl>
<dt>
<dd> If you look for a specific server, you should give nwsfind this argument. If you omit it, nwsfind looks for the server nearest to you.</dl>
<p> <code>-t</code> <i>type</i></p>
<dl>
<dt>
<dd> By default nwsfind looks for file servers. In case you want to look up another server type, you have to specify its numerical type as <code>type.</code></dl>
<h2>CREDITS</h2>
<p> nwsfind was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>Index</h2>
