---
title: "gate(1)"
name: "gate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gate/"
description: "gate – generate Ada applications from a GLADE XML file"
---

<h2>NAME</h2>
<p> gate &#8211; generate Ada applications from a GLADE XML file</p>
<h2>SYNOPSIS</h2>
<p> <code>gate</code> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <i>gate</i> is the static version of the program transforming a file produced by <i><a href="/docs/linux/man/1-glade/">glade</a>(1)</i>, the Gtk GUI builder, into an Ada program. It will generate a set of Ada files that, when compiled, will recreate the interface you just designed in <i><a href="/docs/linux/man/1-glade/">glade</a>(1)</i>. The most important file created by Gate is called <i>callback_</i><code>&lt;project_name&gt;</code><i>.adb</i> and contains stubs for all the callbacks you declared in Glade. </p>
<p> Note that you can easily go back to Glade any time, modify your interface, and have <i>gate</i> regenerate a set of files. All your modifications will be kept in the new files. For that, <i>gate</i> creates a directory <code>.gate</code> in the current directory. Please do not delete it if you want <i>gate</i> to be able to keep your changes from one version to the next. Also note that to be able to keep track of your modifications, gate relies on patch and diff being available on your system. If you don&#8217;t have a working set of diff/patch, configure will simply replace them by null operations.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtkada-config/">gtkada-config</a></code>(1), <code><a href="/docs/linux/man/1-dgate/">dgate</a></code>(1), <code><a href="/docs/linux/man/1-glade/">glade</a></code>(1)</p>
<h2>COPYRIGHT FOR THIS MAN PAGE</h2>
<p> This man page has been written by Samuel Tardieu for the Debian GNU/Linux distribution, from informations given by the GtkAda authors Emmanuel Briot, Joel Brobecker and Arnaud Charlet. </p>
<p> Permission to use, copy, modify, and distribute this documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>Index</h2>
