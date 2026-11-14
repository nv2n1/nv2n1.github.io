---
title: "gtkada-config(1)"
name: "gtkada-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtkada-config/"
description: "gtkada-config – script to get information about the installed version of GTKADA"
---

<h2>NAME</h2>
<p> gtkada-config &#8211; script to get information about the installed version of GTKADA</p>
<h2>SYNOPSIS</h2>
<p> <code>gtkada-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags] [&#8211;static]</p>
<h2>DESCRIPTION</h2>
<p> <i>gtkada-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>GTKADA</i>.</p>
<h2>OPTIONS</h2>
<p> <i>gtkada-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>GTKADA</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>GTKADA</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>GTKADA</i> program.</p>
<dt><code>&#8211;static</code></p>
<dd> Print the flags that are necessary to statically build a <i>GTKADA</i> program.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that <i>GTKADA</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gate/">gate</a></code>(1), <code><a href="/docs/linux/man/1-dgate/">dgate</a></code>(1), <code><a href="/docs/linux/man/1-glade/">glade</a></code>(1)</p>
<h2>COPYRIGHT FOR THIS MAN PAGE</h2>
<p> This man page has been written by Samuel Tardieu for the Debian GNU/Linux distribution, from informations given by the GtkAda authors Emmanuel Briot, Joel Brobecker and Arnaud Charlet. </p>
<p> Permission to use, copy, modify, and distribute this documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>Index</h2>
