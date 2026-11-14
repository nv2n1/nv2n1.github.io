---
title: "gsl-config(1)"
name: "gsl-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsl-config/"
description: "gsl-config – script to get version number and compiler flags of the installed GSL library"
---

<h2>NAME</h2>
<p> gsl-config &#8211; script to get version number and compiler flags of the installed GSL library</p>
<h2>SYNOPSIS</h2>
<p> <code>gsl-config</code> [&#8211;prefix] [&#8211;version] [&#8211;libs] [&#8211;libs-without-cblas] [&#8211;cflags]</p>
<h2>DESCRIPTION</h2>
<p> <i>gsl-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>GSL</i>. It is also used internally to the .m4 macros for GNU autoconf that are included with <i>GSL</i>.</p>
<h2>OPTIONS</h2>
<p> <i>gsl-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>GSL</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>GSL</i> program, with cblas</p>
<dt><code>&#8211;libs-without-cblas</code></p>
<dd> Print the linker flags that are necessary to link a <i>GSL</i> program, without cblas</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>GSL</i> program.</p>
<dt><code>&#8211;prefix</code></p>
<dd> Show the GSL installation prefix.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtk-config/">gtk-config</a></code>(1), <code><a href="/docs/linux/man/1-gnome-config/">gnome-config</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Christopher R. Gabriel </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>Index</h2>
