---
title: "check-module(1)"
name: "check-module"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check-module/"
description: "check-module – program to check gnulib modules."
---

<h2 class="name">NAME</h2>
<p> check-module &#8211; program to check gnulib modules.</p>
<h2>SYNOPSIS</h2>
<p> <code>check-module [OPTIONS] FILE&#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> The GNU portability library is a macro system and C declarations and definitions for commonly-used API elements and abstracted system behaviors. It can be used to improve portability and other functionality in your programs. </p>
<p> <code>check-module</code> reads a module description file and derives the set of files included directly by any .c or .h file listed in the `Files:&#8217; section. First, it takes the union of all such sets for any dependent modules. Then, it compares that set with the set derived from the names listed in the various Files: sections. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;bug-gnulib [at] gnu.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnulib/">gnulib</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> check-module was written by the Free Software Foundation and others (sources of various origins). </p>
<p> This manual page was written by Daniel Baumann &lt;daniel [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
