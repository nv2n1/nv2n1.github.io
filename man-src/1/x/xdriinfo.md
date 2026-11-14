---
title: "xdriinfo(1)"
name: "xdriinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdriinfo/"
description: "xdriinfo – query configuration information of DRI drivers"
---

<h2 class="name">NAME</h2>
<p> xdriinfo &#8211; query configuration information of DRI drivers </p>
<h2>SYNOPSIS</h2>
<p> <code>xdriinfo</code> [-display <i>displayname</i>] [-version] [command]</p>
<h2>DESCRIPTION</h2>
<p> <i>xdriinfo</i> can be used to query configuration information of direct rendering drivers. If no command argument is specified it lists the names of the direct rendering drivers for all screens. </p>
<p> Valid options are:</p>
<dl>
<dt><code>-display</code></p>
<dd> Specifies X server to connect to.</p>
<dt><code>-version</code></p>
<dd> Print the program version and exit.</dl>
<p> Valid commands are:</p>
<dl>
<dt><code>nscreens</code></p>
<dd> Print the number of screens.</p>
<dt><code>driver </code><i>screen</i></p>
<dd> Print the name of the direct rendering driver for <i>screen</i>.</p>
<dt><code>options </code><i>screen|driver</i></p>
<dd> Print the XML document describing the configuration options of a driver. The driver can be specified directly by <i>driver</i> name or indirectly by <i>screen</i> number. If the driver name is specified directly then no X connection is needed.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> The default display.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-xdpyinfo/">xdpyinfo</a></i>(1), <i><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></i>(1), <i><a href="/docs/linux/man/1-xvinfo/">xvinfo</a></i>(1), <i><a href="/docs/linux/man/1-glxinfo/">glxinfo</a></i>(1), <i><a href="/docs/linux/man/1-xprop/">xprop</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Felix Kuehling </p>
<h2>Index</h2>
