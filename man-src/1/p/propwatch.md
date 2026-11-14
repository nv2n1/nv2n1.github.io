---
title: "propwatch(1)"
name: "propwatch"
section: "1"
letter: "p"
url: "/docs/linux/man/1-propwatch/"
description: "propwatch – a tool to monitor X11 properties"
---

<h2>NAME</h2>
<p> propwatch &#8211; a tool to monitor X11 properties</p>
<h2>SYNOPSIS</h2>
<p> <code>propwatch [ options ] property-name &#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>propwatch</code> is a tool to monitor window properties of root and application windows. Nice for debugging property-based IPC of X11 programs.</p>
<h2>OPTIONS</h2>
<p> <code>propwatch</code> uses the Athena Widgets and accepts the usual toolkit options like -display and -geometry. </p>
<p> Additional options are:</p>
<dl>
<dt><code>-watch display</code></p>
<dd> Display to monitor the windows on. By default the display specified in the DISPLAY environment variable or via -display is used, but it is possible to watch another display instead.</p>
<dt><code>-verbose</code></p>
<dd> be verbose.</p>
<dt><code>-proplog</code></p>
<dd> Log property changes to stdout.</p>
<dt><code>-kbdlog</code></p>
<dd> Log keystrokes to stdout.</dl>
<p> All remaining command line arguments are assumed to be property names which should be monitored. If no property names are specified, a build in default (WM_COMMAND) will be used.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> specifies the display to use for the propwatch window.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xprop/">xprop</a>(1), <a href="/docs/linux/man/1-xhost/">xhost</a>(1), <a href="/docs/linux/man/1-xauth/">xauth</a>(1), <a href="/docs/linux/man/1-xwd/">xwd</a>(1)</p>
<h2>AUTHOR</h2>
<p> Gerd Knorr &lt;kraxel [at] bytesex.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1997-2003 Gerd Knorr<br />
 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
