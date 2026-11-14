---
title: "cppunit-config(1)"
name: "cppunit-config"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cppunit-config/"
description: "cppunit-config – script to get information about the installed version of cppunit"
---

<h2>NAME</h2>
<p> cppunit-config &#8211; script to get information about the installed version of cppunit</p>
<h2>SYNOPSIS</h2>
<p> <code>cppunit-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags]</p>
<h2>DESCRIPTION</h2>
<p> <i>cppunit-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>cppunit</i>. It is also used internally to the .m4 macros for GNU autoconf that are included with <i>cppunit</i>.</p>
<h2>OPTIONS</h2>
<p> <i>cppunit-config</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the currently installed version of <i>cppunit</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print the linker flags that are necessary to link a <i>cppunit</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags that are necessary to compile a <i>cppunit</i> program.</p>
<dt><code>&#8211;prefix</code></p>
<dd> Print the prefix with which <i>cppunit</i> was compiled.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation prefix that <i>cppunit</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Print the exec-prefix with which <i>cppunit</i> was compiled.</p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd> If specified, use PREFIX instead of the installation exec prefix that <i>cppunit</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>COPYRIGHT</h2>
<p> cppunit Copyright &#169; 1996-2000 by Michael Feathers &lt;mfeathers [at] objectmentor.com&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>AUTHOR</h2>
<p> This manpage is an almost word-for-word copy of the gtk-config manpage, written by Owen Taylor. It was modified by E. Sommerlade &lt;eric [at] sommerla.de&gt;. </p>
<h2>Index</h2>
