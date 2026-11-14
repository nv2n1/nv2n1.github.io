---
title: "feathers(1)"
name: "feathers"
section: "1"
letter: "f"
url: "/docs/linux/man/1-feathers/"
description: "feathers – a simple source-level debugger for CHICKEN Scheme"
---

<h2 class="name">NAME</h2>
<p> feathers &#8211; a simple source-level debugger for CHICKEN Scheme</p>
<h2>SYNOPSIS</h2>
<p> feathers [OPTION &#8230;] [PROGRAM ARGUMENTS &#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <i>feathers</i> runs a program compiled with CHICKEN Scheme and allows basic source-level debugging like setting breakpoints, single-stepping and inspection of procedure arguments and global variables. </p>
<p> The Scheme code must be compiled with debug-level 3 for debugging to be possible. Communication with the debugger takes place by exchanging messages over a TCP socket, the address and port being given by the environment variable <code>CHICKEN_DEBUGGER</code> which holds a connection address of the form <code>&lt;ADDRESS&gt;:&lt;PORT&gt;</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Shows a list of supported command-line options. </p>
<dt><code>-n</code></p>
<dd> Do not load the default startup file <code>.feathers</code> </p>
<dt><code>-port PORT</code></p>
<dd> Select a different TCP port than the default (9999) </p>
<dt><code>-dir DIRECTORY</code></p>
<dd> Add <code>DIRECTORY</code> to the list of searched paths for locating source files </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CHICKEN_DEBUGGER</code></p>
<dd> Should hold a TCP server address and port where the debugger is listening. This variable is set by the debugger when a program is run from it, and defaults to <code>localhost:9999</code> </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> More information can be found in the <i>CHICKEN User&#8217;s Manual</i> </p>
<h2>BUGS</h2>
<p> Submit bug reports by e-mail to <i>chicken-janitors [at] nongnu.org</i> , preferrably using the <code>chicken-bug</code> tool. </p>
<h2>AUTHORS</h2>
<p> The CHICKEN Team </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chicken-uninstall/">chicken-uninstall</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-status/">chicken-status</a>(1)</code> <code><a href="/docs/linux/man/1-chicken/">chicken</a>(1)</code> <code><a href="/docs/linux/man/1-csc/">csc</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-bug/">chicken-bug</a>(1)</code> </p>
<h2>Index</h2>
