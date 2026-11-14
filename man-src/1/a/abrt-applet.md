---
title: "abrt-applet(1)"
name: "abrt-applet"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-applet/"
---

<h2 class="name">NAME</h2>
 

 abrt-applet - Applet which notifies user when new problems are detected by ABRT 

<h2>SYNOPSIS</h2>

 

 <i>abrt-applet</i> [-v]

<h2>DESCRIPTION</h2>

 

 This tool listens on <i>org.freedesktop.problems</i> D-Bus bus and waits for <i>Crash</i> signal. When the tool detects the signal, it notifies user about new problem over a desktop specific notification pop-up. 

 At start-up this tool checks for new problems which occurred while the tool was not running and if it finds any of such problem it notifies user over a desktop specific notification pop-up.

<h2>OPTIONS</h2>

 

 -v, --verbose
<dl>
<dt>
<dd> Be more verbose. Can be given multiple times.</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/8-abrt-dbus/">abrt-dbus</a>(8)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


