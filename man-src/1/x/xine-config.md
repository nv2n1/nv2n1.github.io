---
title: "xine-config(1)"
name: "xine-config"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xine-config/"
description: "xine-config – script to get information about the installed version of libxine"
---

<h2>NAME</h2>
<p> xine-config &#8211; script to get information about the installed version of libxine</p>
<h2>SYNOPSIS</h2>
<p> <code>xine-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags] [&#8211;objcflags] [&#8211;plugindir] [&#8211;datadir] [&#8211;scriptdir] [&#8211;localedir]</p>
<h2>DESCRIPTION</h2>
<p> <i>xine-config is DEPRECATED. Use pkg-config instead.</i> </p>
<p> <i>xine-config</i> is a tool that is used to determine the compiler and linker flags that should be used to compile and link programs that use <i>libxine</i>. It can also be used to determine the directories where <i>libxine</i> expects plugins.</p>
<h2>OPTIONS</h2>
<p> <i>xine-config</i> accepts the following options, passing them on (possibly modified) to <i>pkg-config libxine</i>:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> &#8211;modversion<br />
 Print the currently installed version of <i>libxine</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd>
<dt> <code>&#8211;cflags</code> </p>
<dt> <code>&#8211;objcflags</code></p>
<dd>Passed on unmodified.<br />
 Print the compiler flags (for C and Objective C, respectively) that are necessary to compile a program that uses <i>libxine</i>.</p>
<dt><code>&#8211;bindir</code></p>
<dd>
<dt> <code>&#8211;plugindir</code> </p>
<dt> <code>&#8211;datadir</code> </p>
<dt> <code>&#8211;scriptdir</code> </p>
<dt> <code>&#8211;localedir</code> &#8211;variable=&#8230;</p>
<dd>
<dd>Print the directory where, respectively, <i>libxine</i> binaries, plugins, data files, scripts and locale data are stored/expected.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> &#8211;define-variable=prefix=PREFIX<br />
 If specified, use PREFIX instead of the installation prefix that <i>xine-lib</i> was built with. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. </p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd> &#8211;define-variable=exec_prefix=PREFIX<br />
 If specified, use PREFIX instead of the installation exec prefix that <i>xine-lib</i> was built with.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-xine-lib/">xine-lib</a></code>(3), <code><a href="/docs/linux/man/1-xine/">xine</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Siggi Langauf, &#169; 2001-2008 the xine project. Based on the man page for gtk-config, &#169; 1998 Owen Taylor. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. </p>
<h2>Index</h2>
