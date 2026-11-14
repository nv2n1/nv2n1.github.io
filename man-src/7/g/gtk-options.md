---
title: "gtk-options(7)"
name: "gtk-options"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gtk-options/"
description: "gtk-options – Standard Command Line Options for GTK Programs"
---

<p>gtk-options &#8211; Standard Command Line Options for GTK Programs</p>
<h2>Synopsis</h2>
<p><i>program </i>[<i>standard options</i>] [<i>specific options</i>] <i>arguments</i></p>
<h2>Description</h2>
<p>This manual page describes the command line options, which are common to all GTK based applications.</p>
<h2>Options</h2>
<h3>Gtk Options</h3>
<dl>
<dt><code>&#8211;gtk-module</code>=<i>MODULE</i></p>
<dd>Load an additional Gtk module.</p>
<dt><code>&#8211;gtk-debug</code>=<i>FLAGS</i></p>
<dd>A colon separated list of GTK debugging flags to set. Valid flags are <i>objects</i>, <i>misc</i>, <i>signals</i>, <i>dnd</i>, and <i>plugsocket</i>. The special value <i>all</i> enables all flags.</p>
<dt><code>&#8211;gtk-no-debug</code>=<i>FLAGS</i></p>
<dd>GTK debugging flags to unset. Use this options to override the <i>GTK_DEBUG</i> environment variable.</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd>Make all warnings fatal.</dl>
<h3>Gdk Options</h3>
<dl>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd>Set the X display to use. Use this option to override the <i>DISPLAY</i> environment variable.</p>
<dt><code>&#8211;screen</code>=<i>SCREEN</i></p>
<dd>X screen to use. Use this options to override the screen part of the <i>DISPLAY</i> environment variable (see the <i>DISPLAY NAMES</i> section of the <i><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a></i>(7x) manual page).</p>
<dt><code>&#8211;sync</code></p>
<dd>Make X calls synchronous. This slows down the program considerably, but may be useful for debugging purposes.</p>
<dt><code>&#8211;no-xshm</code></p>
<dd>Do not use the X server&#8217;s XSHM shared memory extension. This slows down the program.</p>
<dt><code>&#8211;name</code>=<i>NAME</i></p>
<dd>Program name as used by the window manager.</p>
<dt><code>&#8211;class</code>=<i>CLASS</i></p>
<dd>Program class as used by the window manager.</p>
<dt> <code>&#8211;gxid_host</code>=<i>HOST</i></p>
<dt> <code>&#8211;gxid_port</code>=<i>PORT</i></p>
<dt> <code>&#8211;xim-preedit</code></p>
<dt><code>&#8211;xim-status</code></p>
<dd>
<dd>Control the X input method.</p>
<dt><code>&#8211;gdk-debug</code>=<i>FLAGS</i></p>
<dd>A colon-separated list of GDK debugging flags to set. This only works if your GDK library was compile with debugging support. Valid flags are <i>events</i>, <i>misc</i>, <i>dnd</i>, <i>color-context</i>, and <i>xim</i>. The special value <i>all</i> enables all valid flags.</p>
<dt><code>&#8211;gdk-no-debug</code>=<i>FLAGS</i></p>
<dd>A colon-separated list of GDK debugging flags to unset. Use this options to override the <i>GDK_DEBUG</i> environment variable.</dl>
<h2>See Also</h2>
<p><code><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a></code>(7x), the GTK documentation, and the GDK documentation. </p>
<p> For most GTK programs there will be additional command line options, which are specific to the program. These will be explained in the application&#8217;s documentation.</p>
<h2>Author</h2>
<p>This manual page was written by Jochen Voss &lt;voss [at] debian.org&gt;.</p>
