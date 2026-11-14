---
title: "xml2-config(1)"
name: "xml2-config"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xml2-config/"
description: "xml-config – script to get information about the installed version of GNOME-XML"
---

<h2 class="name">NAME</h2>
<p> xml-config &#8211; script to get information about the installed version of GNOME-XML </p>
<h2>SYNOPSIS</h2>
<p> <code>xml-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;libs] [&#8211;cflags] [&#8211;version] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> <i>xml-config</i> is a tool that is used to determine the compile and linker flags that should be used to compile and link programs that use <i>GNOME-XML</i>.</p>
<h2>OPTIONS</h2>
<p> <i>xml-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>GNOME-XML</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>GNOME-XML</i> program. Add &#8211;dynamic after &#8211;libs to print only shared library linking information.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>GNOME-XML</i> program.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that <i>GNOME-XML</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Fredrik Hallenberg &lt;hallon [at] lysator.liu.se&gt;, for the Debian GNU/linux system (but may be used by others). </p>
<h2>Index</h2>
