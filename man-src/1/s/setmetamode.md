---
title: "setmetamode(1)"
name: "setmetamode"
section: "1"
letter: "s"
url: "/docs/linux/man/1-setmetamode/"
description: "setmetamode – define the keyboard meta key handling"
---

<h2 class="name">NAME</h2>
<p> setmetamode &#8211; define the keyboard meta key handling </p>
<h2>SYNOPSIS</h2>
<p> <code>setmetamode</code> [ <i>options</i> ] [ <i>argument</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Without argument, <code>setmetamode</code> prints the current Meta key mode. With argument, it sets the Meta key mode as indicated. The setting before and after the change are reported. </p>
<p> The Meta key mode is specific for each VT (and the VT corresponding to stdin is used). One might use <code>setmetamode</code> in /etc/rc to define the initial state of the Meta key mode, e.g. by </p>
<p> INITTY=/dev/tty[1-8]<br />
 for tty in $INITTY; do<br />
 setmetamode escprefix &lt; $tty<br />
 done</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>esc</code>, <code>prefix</code>, <code>escprefix</code></p>
<dd> The Meta key sends an Escape prefix.</p>
<dt><code>meta</code>, <code>bit</code>, <code>metabit</code></p>
<dd> The Meta key sets the high order bit of the character.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-C</code>, <code>&#8211;console</code>=<i>,DEV/</i></p>
<dd> the console device to be used;</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print version number;</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print this usage message.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/1-kbdinfo/">kbdinfo</a></code>(1) </p>
<h2>Index</h2>
