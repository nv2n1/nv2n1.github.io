---
title: "ijs-config(1)"
name: "ijs-config"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ijs-config/"
description: "ijs-config – script to get information about the installed version of ijs"
---

<h2 class="name">NAME</h2>
<p> ijs-config &#8211; script to get information about the installed version of ijs </p>
<h2>SYNOPSIS</h2>
<p> <code>ijs-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags]</p>
<h2>DESCRIPTION</h2>
<p> <i>ijs-config</i> is a program that is used to determine the compiler and linker flags that should be used to compile and link programs that use <i>IJS</i>.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options. This may list additional advanced package configuration options not detailed in this manual page.</p>
<dt><code>&#8211;version</code></p>
<dd> Show installed libijs version.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link an <i>IJS</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile an <i>IJS</i> program.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that <i>IJS</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation exec prefix that <i>IJS</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gtk-config/">gtk-config</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Roger Leigh <i>&lt;rleigh [at] debian.org&gt;</i>, originally for the Debian GNU/Linux system. </p>
<h2>Index</h2>
