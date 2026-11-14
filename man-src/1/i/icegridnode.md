---
title: "icegridnode(1)"
name: "icegridnode"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icegridnode/"
description: "icegridnode – The IceGrid node server."
---

<h2 class="name">NAME</h2>
<p> icegridnode &#8211; The IceGrid node server.</p>
<h2>SYNOPSIS</h2>
<p> icegridnode [options] </p>
<h2>DESCRIPTION</h2>
<p> An IceGrid node is a process that activates, monitors, and deactivates registered server processes. You can run any number of nodes in a domain, but typically there is one node per host. A node must be running on each host on which servers are activated automatically, and nodes cannot run without an IceGrid registry. The IceGrid node server is implemented by the icegridnode executable. If you wish to run a registry and node in one process, icegridnode is the executable you must use. Full documentation for icegridnode is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/icegridnode">http://doc.zeroc.com/display/Ice/icegridnode</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays help message. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays the Ice version. </p>
<dt><code>&#8211;daemon</code></p>
<dd>
 Run as a daemon. </p>
<dt><code>&#8211;pidfile</code> <code>FILE</code></p>
<dd>
 Write process ID into FILE. </p>
<dt><code>&#8211;noclose</code></p>
<dd>
 Do not close open file descriptors. </p>
<dt><code>&#8211;nochdir</code></p>
<dd>
 Do not change the current working directory. </p>
<dt><code>&#8211;nowarn</code></p>
<dd>
 Do not print security warnings. </p>
<dt><code>&#8211;readonly</code></p>
<dd>
 Start the collocated master registry in read-only mode. </p>
<dt><code>&#8211;deploy</code> <code>DESCRIPTOR</code> <code>[TARGET1</code> <code>[TARGET2</code> <code>&#8230;]]</code></p>
<dd>
 Add or update descriptor in file DESCRIPTOR, with optional targets. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icegridadmin/">icegridadmin</a></code>(1), <code><a href="/docs/linux/man/1-icegridregistry/">icegridregistry</a></code>(1) </p>
<h2>Index</h2>
