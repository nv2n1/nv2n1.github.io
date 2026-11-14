---
title: "gnome-open(1)"
name: "gnome-open"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-open/"
description: "gnome-open – Open files and URLs using the GNOME file handlers"
---

<h2 class="name">NAME</h2>
<p> gnome-open &#8211; Open files and URLs using the GNOME file handlers </p>
<h2>SYNOPSIS</h2>
<p> <code>gnome-open</code> [OPTION]&#8230; [URL]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This program opens files using file handlers configured in GNOME.</p>
<h2>OPTIONS</h2>
<p> Usage: gnome-open [OPTION&#8230;] </p>
<p> <code>Dynamic Modules</code> </p>
<p> <code>&#8211;load-modules=MODULE1,MODULE2,&#8230;</code></p>
<dl>
<dt>
<dd> Dynamic modules to load</dl>
<p> <code>Help Options</code> </p>
<p> <code>-?, &#8211;help</code></p>
<dl>
<dt>
<dd> Show a brief help message</dl>
<p> <code>&#8211;usage</code></p>
<dl>
<dt>
<dd> Display a brief usage message</dl>
<p> <code>Bonobo activation Support</code> </p>
<p> <code>&#8211;oaf-ior-fd=FD</code></p>
<dl>
<dt>
<dd> File descriptor to print IOR on</dl>
<p> <code>&#8211;oaf-activate-iid=IID</code></p>
<dl>
<dt>
<dd> IID to activate</dl>
<p> <code>&#8211;oaf-private</code></p>
<dl>
<dt>
<dd> Prevent registering of server with OAF</dl>
<p> <code>GNOME Library</code> </p>
<p> <code>&#8211;disable-sound</code></p>
<dl>
<dt>
<dd> Disable sound server usage</dl>
<p> <code>&#8211;enable-sound</code></p>
<dl>
<dt>
<dd> Enable sound server usage</dl>
<p> <code>&#8211;espeaker=HOSTNAME:PORT</code></p>
<dl>
<dt>
<dd> Host:port on which the sound server to use is running</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints the version number</dl>
<h2>EXAMPLES</h2>
<p> <code>Open a web page</code></p>
<dl>
<dt>
<dd> gnome-open <a rel="nofollow" href="http://www.gnome.org">www.gnome.org</a></dl>
<p> <code>Open an OpenOffice.org document</code></p>
<dl>
<dt>
<dd> gnome-open Spinach.odf</dl>
<p> <code>Open a directory in Nautilus</code></p>
<dl>
<dt>
<dd> gnome-open ~</dl>
<p> <code>Send an e-mail</code></p>
<dl>
<dt>
<dd> gnome-open mailto:gnome-list [at] mail.gnome.org</dl>
<p> <code>Possible useless use of gnome-open</code></p>
<dl>
<dt>
<dd> gnome-open /usr/share/applications/gedit.desktop</dl>
<h2>REPORTING BUGS</h2>
<p> Please report bugs at <a rel="nofollow" href="http://bugzilla.gnome.org/">http://bugzilla.gnome.org/</a> </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jonathan Carter &lt;jonathan [at] ubuntu.com&gt; </p>
<h2>Index</h2>
