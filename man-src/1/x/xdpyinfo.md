---
title: "xdpyinfo(1)"
name: "xdpyinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdpyinfo/"
description: "xdpyinfo – display information utility for X"
---

<h2 class="name">NAME</h2>
<p> xdpyinfo &#8211; display information utility for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xdpyinfo</code> [-display <i>displayname</i>] [-queryExtensions] [-ext <i>extension-name</i>] [-version]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xdpyinfo</i> is a utility for displaying information about an X server. It is used to examine the capabilities of a server, the predefined values for various parameters used in communicating between clients and the server, and the different types of screens and visuals that are available. </p>
<p> By default, numeric information (opcode, base event, base error) about protocol extensions is not displayed. This information can be obtained with the <code>-queryExtensions</code> option. Use of this option on servers that dynamically load extensions will likely cause all possible extensions to be loaded, which can be slow and can consume significant server resources. </p>
<p> Detailed information about a particular extension is displayed with the <code>-ext</code> <i>extensionName</i> option. If <i>extensionName</i> is <code>all</code>, information about all extensions supported by both <i>xdpyinfo</i> and the server is displayed. </p>
<p> If <code>-version</code> is specified, xdpyinfo prints its version and exits, without contacting the X server.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> To get the default host, display number, and screen.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-x/">X</a></i>(7), <i><a href="/docs/linux/man/1-xprop/">xprop</a></i>(1), <i><a href="/docs/linux/man/1-xrdb/">xrdb</a></i>(1), <i><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></i>(1), <i><a href="/docs/linux/man/1-xrandr/">xrandr</a></i>(1), <i><a href="/docs/linux/man/1-xdriinfo/">xdriinfo</a></i>(1), <i><a href="/docs/linux/man/1-xvinfo/">xvinfo</a></i>(1), <i><a href="/docs/linux/man/1-glxinfo/">glxinfo</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium<br />
 Support for the XFree86-VidModeExtension, XFree86-DGA, XFree86-Misc, and XKB extensions added by Joe Moss </p>
<h2>Index</h2>
