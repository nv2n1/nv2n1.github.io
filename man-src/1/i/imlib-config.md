---
title: "imlib-config(1)"
name: "imlib-config"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imlib-config/"
description: "imlib-config – Display Imlib and GDK-Imlib Library Configuration"
---

<h2>NAME</h2>
<p> imlib-config &#8211; Display Imlib and GDK-Imlib Library Configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>imlib-config </code> <i>OPTION </i> <code>[</code> <i>OPTION</i> <code>&#8230; ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>imlib-config</code> is a script that is used to display what compiler flags and libraries were used when Imlib and GDK-Imlib were built. </p>
<p> Note that <code>imlib-config</code> is not the same as the <code>imlib_config</code> program.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</dt>
<dd> Imlib/GDK-Imlib version information</dd>
<dt>&#8211;prefix</dt>
<dd> displays prefix of directory where Imlib and GDK-Imlib were installed.</dd>
<dt>&#8211;exec-prefix</dt>
<dd> displays exec-prefix of directory where Imlib and GDK-Imlib were installed.</dd>
<dt>&#8211;cflags</dt>
<dd> C pre-processor and compiler flags for use with Imlib.</dd>
<dt>&#8211;cflags-gdk</dt>
<dd> C pre-processor and compiler flags for use with GDK-Imlib</dd>
<dt>&#8211;libs</dt>
<dd> Imlib library linking information</dd>
<dt>&#8211;libs-gdk</dt>
<dd> GDK-Imlib library linking information</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-imlib_config/">imlib_config</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Ossama Othman &lt;ossama [at] debian.org&gt; </p>
<h2>Index</h2>
