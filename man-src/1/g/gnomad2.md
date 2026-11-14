---
title: "gnomad2(1)"
name: "gnomad2"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnomad2/"
description: "gnomad2 – transfer files between a host and a Creative Labs Nomad Jukebox, Zen jukebox or Dell Digital Jukebox (DJ)."
---

<h2>NAME</h2>
<p> gnomad2 &#8211; transfer files between a host and a Creative Labs Nomad Jukebox, Zen jukebox or Dell Digital Jukebox (DJ).</p>
<h2>SYNOPSIS</h2>
<p> <code>gnomad2</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Gnomad 2 is a GUI built on top of GTK/GNOME 2, id3lib and libnjb that makes it possible to transfer tracks and files from/to a Creative Nomad Jukebox (all brands) and the Dell DJ. It is designed much like an ordinary graphical FTP program, in commander-style.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D</code>[<i>DEBUGLEVEL</i>]</p>
<dd> A debug level is a number between 1 and 15, identical to the debug level value of libnjb.</p>
<dt><code>&#8211;load-modules</code>=[<i>MODULE</i>]&#8230;</p>
<dd> Dynamic modules to load</dl>
<h3>Help options</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show this help message</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</dl>
<h3>GTK+</h3>
<dl>
<dt><code>&#8211;gdk-debug</code>=<i>FLAGS</i></p>
<dd> Gdk debugging flags to set</p>
<dt><code>&#8211;gdk-no-debug</code>=<i>FLAGS</i></p>
<dd> Gdk debugging flags to unset</p>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</p>
<dt><code>&#8211;screen</code>=<i>SCREEN</i></p>
<dd> X screen to use</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous</p>
<dt><code>&#8211;name</code>=<i>NAME</i></p>
<dd> Program name as used by the window manager</p>
<dt><code>&#8211;class</code>=<i>CLASS</i></p>
<dd> Program class as used by the window manager</p>
<dt><code>&#8211;gtk-debug</code>=<i>FLAGS</i></p>
<dd> Gtk+ debugging flags to set</p>
<dt><code>&#8211;gtk-no-debug</code>=<i>FLAGS</i></p>
<dd> Gtk+ debugging flags to unset</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd> Make all warnings fatal</p>
<dt><code>&#8211;gtk-module</code>=<i>MODULE</i></p>
<dd> Load an additional Gtk module</dl>
<h3>Bonobo activation support</h3>
<dl>
<dt><code>&#8211;oaf-ior-fd</code>=<i>FD</i></p>
<dd> File descriptor to print IOR on</p>
<dt><code>&#8211;oaf-activate-iid</code>=<i>IID</i></p>
<dd> IID to activate</p>
<dt><code>&#8211;oaf-private</code></p>
<dd> Prevent registering of server with OAF</dl>
<h3>GNOME Library</h3>
<dl>
<dt><code>&#8211;disable-sound</code></p>
<dd> Disable sound server usage</p>
<dt><code>&#8211;enable-sound</code></p>
<dd> Enable sound server usage</p>
<dt><code>&#8211;espeaker</code>=<i>HOSTNAME</i>:PORT</p>
<dd> Host:port on which the sound server to use is running</p>
<dt><code>&#8211;version</code></p>
<dd> 2.6.1.1</dl>
<h3>Session management</h3>
<dl>
<dt><code>&#8211;sm-client-id</code>=<i>ID</i></p>
<dd> Specify session management ID</p>
<dt><code>&#8211;sm-config-prefix</code>=<i>PREFIX</i></p>
<dd> Specify prefix of saved configuration</p>
<dt><code>&#8211;sm-disable</code></p>
<dd> Disable connection to session manager</dl>
<h3>GNOME GUI Library</h3>
<dl>
<dt><code>&#8211;disable-crash-dialog</code></p>
<dd> Disable crash dialog</dl>
<h2>AUTHOR</h2>
<p> Written by Linus Walleij. </p>
<p> This manual page was written by Shaun Jackman &lt;sjackman [at] debian.org&gt; for the Debian system.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to Linus Walleij &lt;triad [at] df.lth.se&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2003 Linus Walleij </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://gnomad2.sourceforge.net/">http://gnomad2.sourceforge.net/</a> </p>
<h2>Index</h2>
