---
title: "xkbkeycodetokeysym(3)"
name: "xkbkeycodetokeysym"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeycodetokeysym/"
description: "XkbKeycodeToKeysym – Finds the keysym bound to a particular key at a specified group and shift level"
---

<p>XkbKeycodeToKeysym &#8211; Finds the keysym bound to a particular key at a specified group and shift level </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>KeySym XkbKeycodeToKeysym</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>KeyCode </code><i>kc</i><code>,</code> <code>unsigned int </code><i>group</i><code>,</code> <code>unsigned int </code><i>level</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; kc</i></p>
<dd>key of interest</p>
<dt><i>&#8211; group</i></p>
<dd>group of interest</p>
<dt><i>&#8211; level</i></p>
<dd>shift level of interest</dl>
<h2>Description</h2>
<p><i>XkbKeycodeToKeysym </i> returns the keysym bound to a particular group and shift level for a particular key on the core keyboard. If <i>kc </i> is not a legal keycode for the core keyboard, or if <i>group </i> or <i>level </i> are out of range for the specified key, <i>XkbKeycodeToKeysym </i> returns NoSymbol.</p>
