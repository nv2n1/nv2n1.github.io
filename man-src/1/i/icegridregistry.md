---

title: "icegridregistry(1)"
name: "icegridregistry"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icegridregistry/"
description: "icegridregistry – The IceGrid registry server."
---

<p> icegridregistry &#8211; The IceGrid registry server.</p>
<h2>SYNOPSIS</h2>
<p> icegridregistry [options] [command&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> The IceGrid registry is a centralized repository of information, including deployed applications and well-known objects. A registry can optionally be collocated with an IceGrid node, which conserves resources and can be convenient during development and testing. The registry server is implemented by the icegridregistry executable. Full documentation for icegridregistry is available online at:<br />
 &quot;<a rel="nofollow" href="http://doc.zeroc.com/display/Ice/icegridregistry">http://doc.zeroc.com/display/Ice/icegridregistry</a>&quot;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Displays a help message. </dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Displays the Ice version. </dd>
<dt><code>&#8211;daemon</code></dt>
<dd>
 Run as a daemon. </dd>
<dt><code>&#8211;pidfile</code> <code>FILE</code></dt>
<dd>
 Write process ID into FILE. </dd>
<dt><code>&#8211;noclose</code></dt>
<dd>
 Do not close open file descriptors. </dd>
<dt><code>&#8211;nochdir</code></dt>
<dd>
 Do not change the current working directory. </dd>
<dt><code>&#8211;nowarn</code></dt>
<dd>
 Do not print security warnings. </dd>
<dt><code>&#8211;readonly</code></dt>
<dd>
 Start the master registry in read-only mode. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-icegridadmin/">icegridadmin</a></code>(1), <code><a href="/docs/linux/man/1-icegridnode/">icegridnode</a></code>(1) </p>
