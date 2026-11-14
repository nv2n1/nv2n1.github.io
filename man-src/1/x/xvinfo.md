---
title: "xvinfo(1)"
name: "xvinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvinfo/"
description: "xvinfo – Print out X-Video extension adaptor information"
---

<h2 class="name">NAME</h2>
<p> xvinfo &#8211; Print out X-Video extension adaptor information </p>
<h2>SYNOPSIS</h2>
<p> <code>xvinfo</code> [-display <i>displayname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>xvinfo</code> prints out the capabilities of any video adaptors associated with the display that are accessible through the X-Video extension.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> This argument allows you to specify the server to query; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</p>
<dt><code>-short</code></p>
<dd> Output less details, to reduce the amount of text.</p>
<dt><code>-version</code></p>
<dd> Output program version, then exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> This variable may be used to specify the server to query. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a>(1), <a href="/docs/linux/man/1-xwininfo/">xwininfo</a>(1), <a href="/docs/linux/man/1-xdriinfo/">xdriinfo</a>(1), <a href="/docs/linux/man/1-glxinfo/">glxinfo</a>(1), <a href="/docs/linux/man/1-xprop/">xprop</a>(1)</p>
<h2>AUTHORS</h2>
<p> Mark Vojkovich </p>
<h2>Index</h2>
