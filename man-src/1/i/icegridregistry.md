---
title: "icegridregistry(1)"
name: "icegridregistry"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icegridregistry/"
description: "icegridregistry – The IceGrid registry server."
---

<h2 class="name">NAME</h2>
<p> icegridregistry &#8211; The IceGrid registry server.</p>
<h2>SYNOPSIS</h2>
<p> icegridregistry [options] [command&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The IceGrid registry is a centralized repository of information, including deployed applications and well-known objects. A registry can optionally be collocated with an IceGrid node, which conserves resources and can be convenient during development and testing. The registry server is implemented by the icegridregistry executable. Full documentation for icegridregistry is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/icegridregistry">http://doc.zeroc.com/display/Ice/icegridregistry</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Displays a help message. </p>
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
 Start the master registry in read-only mode. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icegridadmin/">icegridadmin</a></code>(1), <code><a href="/docs/linux/man/1-icegridnode/">icegridnode</a></code>(1) </p>
<h2>Index</h2>
