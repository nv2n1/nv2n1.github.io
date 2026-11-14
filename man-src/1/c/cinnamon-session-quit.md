---
title: "cinnamon-session-quit(1)"
name: "cinnamon-session-quit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cinnamon-session-quit/"
description: "cinnamon-session-quit – End the current GNOME session"
---

<h2>NAME</h2>
<p> cinnamon-session-quit &#8211; End the current GNOME session</p>
<h2>SYNOPSIS</h2>
<p> <code>cinnamon-session-quit [&#8211;logout|&#8211;power-off|&#8211;reboot] [&#8211;force] [&#8211;no-prompt]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>cinnamon-session-quit</i> program can be used to end a GNOME session.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>&#8211;logout</i></p>
<dd> Prompt the user to confirm logout. This is the default behavior.</p>
<dt><i>&#8211;power-off</i></p>
<dd> Prompt the user to confirm system power off.</p>
<dt><i>&#8211;reboot</i></p>
<dd> Prompt the user to confirm system reboot.</p>
<dt><i>&#8211;force</i></p>
<dd> Ignore any inhibitors.</p>
<dt><i>&#8211;no-prompt</i></p>
<dd> End the session without user interaction. This only works with <i>&#8211;logout</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cinnamon-session/">cinnamon-session</a>(1)</code> </p>
<h2>Index</h2>
