---
title: "mumble-overlay(1)"
name: "mumble-overlay"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mumble-overlay/"
description: "mumble-overlay – load OpenGL overlay for Mumble."
---

<h2>NAME</h2>
<p> mumble-overlay &#8211; load OpenGL overlay for Mumble.</p>
<h2>SYNOPSIS</h2>
<p> <code>mumble-overlay</code> executable</p>
<h2>DESCRIPTION</h2>
<p> This wrapper will load the OpenGL overlay for Mumble into the application of your choice. This allows you to easily see who is talking even in fullscreen games and applications. </p>
<p> Nothing will be shown unless you have Mumble running and it is currently connected to a server.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>MUMBLE_OVERLAY_DEBUG</code></p>
<dd> If this environment variable is set, extended debugging will be output to standard output. Only useful for debugging.</dl>
<h2>EXAMPLE</h2>
<p> To run glxgears with the mumble-overlay active:</p>
<dl>
<dt>
<dd> mumble-overlay glxgears</dl>
<h2>NOTES</h2>
<p> This will only work with OpenGL drivers which support the full OpenGL and GLX specifications.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mumble/">mumble</a></code>(1), <code><a href="/docs/linux/man/1-murmurd/">murmurd</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> mumble and murmurd was written by Thorvald Natvig &lt;slicer [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
