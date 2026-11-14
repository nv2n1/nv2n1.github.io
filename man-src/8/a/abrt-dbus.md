---
title: "abrt-dbus(8)"
name: "abrt-dbus"
section: "8"
letter: "a"
url: "/docs/linux/man/8-abrt-dbus/"
---

abrt-dbus - dbus server for querying problem data

<h2>Synopsis</h2>

<i>abrt-dbus</i> [-v[v]...] [-t NUM]

<h2>Description</h2>

<i>abrt-dbus</i> allows other programs to operate on problem data directories over D-Bus. 

 Normally <i>abrt-dbus</i> is started by D-Bus daemon on demand, and terminates after a timeout.

<h2>Options</h2>

-v
<dl><dd>Log more detailed debugging information.</dl>
 

 -t NUM
<dl><dd>Exit after NUM seconds of inactivity.</dl>

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5) 
