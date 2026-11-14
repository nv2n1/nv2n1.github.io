---
title: "nurbs-config(1)"
name: "nurbs-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nurbs-config/"
description: "nurbs++-config – script to get information about the installed version of nurbs++"
---

<p>nurbs++-config &#8211; script to get information about the installed version of nurbs++</p>
<h2>Synopsis</h2>
<p><code>nurbs++-config</code> [&#8211;prefix<i>[=DIR]</i>] [&#8211;exec-prefix<i>[=DIR]</i>] [&#8211;version] [&#8211;libs] [&#8211;cflags]</p>
<h2>Description</h2>
<p><i>nurbs++-config</i> is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use <i>nurbs++</i>. It is also used internally to the .m4 macros for GNU autoconf that are included with <i>nurbs++</i>.</p>
<h2>Options</h2>
<p><i>nurbs++-config</i> accepts the following options:</p>
<dl COMPACT>
<dt><code>&#8211;version</code></p>
<dd>Print the currently installed version of <i>nurbs++</i> on the standard output.</p>
<dt><code>&#8211;libs</code></p>
<dd>Print the linker flags that are necessary to link a <i>nurbs++</i> program.</p>
<dt><code>&#8211;cflags</code></p>
<dd>Print the compiler flags that are necessary to compile a <i>nurbs++</i> program.</p>
<dt><code>&#8211;prefix</code></p>
<dd>Print the prefix with which <i>nurbs++</i> was compiled.</p>
<dt><code>&#8211;prefix=PREFIX</code></p>
<dd>If specified, use PREFIX instead of the installation prefix that <i>nurbs++</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd>Print the exec-prefix with which <i>nurbs++</i> was compiled.</p>
<dt><code>&#8211;exec-prefix=PREFIX</code></p>
<dd>If specified, use PREFIX instead of the installation exec prefix that <i>nurbs++</i> was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</dl>
<h2>Copyright</h2>
<p>NURBS++ Copyright &#169; 1996-2002 by Philppe Lavoie &lt;philosophil [at] users.sourceforge.net&gt; </p>
<p> This software is under the LGPL. You can find a copy of the LGPL somewhere on the net, most likely at <a rel="nofollow" href="http://www.gnu.org.">http://www.gnu.org.</a></p>
<h2>Author</h2>
<p>This manpage is an almost word-for-word copy of the cppunit-config which in turn is an almost word-for-word copy of the gtk-config manpage, written by Owen Taylor. It was modified by Philippe Lavoie &lt;philosophil [at] users.sourceforge.net&gt;.</p>
