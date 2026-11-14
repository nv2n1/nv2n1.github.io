---
title: "synclient(1)"
name: "synclient"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synclient/"
description: "synclient – commandline utility to query and modify Synaptics driver options."
---

<h2 class="name">NAME</h2>
<p> synclient &#8211; commandline utility to query and modify Synaptics driver options. </p>
<h2>SYNOPSIS</h2>
<p> synclient [<i>-lV?</i>] [var1=value1 [var2=value2] &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This program lets you change your Synaptics TouchPad driver for XOrg/XFree86 server parameters while X is running. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> List current user settings. This is the default if no option is given.</p>
<dt><code>-V</code></p>
<dd> Print version number and exit.</p>
<dt><code>-?</code></p>
<dd> Show the help message.</p>
<dt><code>var=value</code></p>
<dd> Set user parameter <i>var</i> to <i>value</i>. </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/X11/xorg.conf</i></p>
<h2>EXAMPLES</h2>
<p> To disable EdgeMotionMinSpeed: </p>
<p> synclient EdgeMotionMinSpeed=0</p>
<h2>AUTHORS</h2>
<p> Peter Osterlund &lt;petero2 [at] telia.com&gt; and many others.</p>
<dl>
<dt>This man page was written by Mattia Dongili &lt;malattia [at] debian.org&gt;</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/1-syndaemon/">syndaemon</a>(1), <a href="/docs/linux/man/4-synaptics/">synaptics</a>(4) </p>
<h2>Index</h2>
