---
title: "arm-gp2x-linux-cfilt(1)"
name: "arm-gp2x-linux-cfilt"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-cfilt/"
description: "c++filt – Demangle C++ and Java symbols."
---

<p>c++filt &#8211; Demangle C++ and Java symbols.</p>
<h2>Synopsis</h2>
<p>c++filt [<code>-_</code>|<code>&#8211;strip-underscores</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-j</code>|<code>&#8211;java</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-n</code>|<code>&#8211;no-strip-underscores</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;no-params</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>-s</code>&nbsp;<wbr><i>format</i>|<code>&#8211;format=</code><i>format</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>&nbsp;<wbr>[<i>symbol</i>&#8230;]</p>
<h2>Description</h2>
<p>The C++ and Java languages provides function overloading, which means that you can write many functions with the same name (providing each takes parameters of different types). All C++ and Java function names are encoded into a low-level assembly label (this process is known as <i>mangling</i>). The <code>c++filt</code> [1] program does the inverse mapping: it decodes (<i>demangles</i>) low-level names into user-level names so that the linker can keep these overloaded functions from clashing. </p>
<p> Every alphanumeric word (consisting of letters, digits, underscores, dollars, or periods) seen in the input is a potential label. If the label decodes into a C++ name, the C++ name replaces the low-level name in the output. </p>
<p> You can use <code>c++filt</code> to decipher individual symbols: </p>
<pre> c++filt &lt;symbol&gt;</pre>
<p>If no <i>symbol</i> arguments are given, <code>c++filt</code> reads symbol names from the standard input and writes the demangled names to the standard output. All results are printed on the standard output.</p>
<h2>Options</h2>
<dl>
<dt><code>-_</code></dt>
<dd>
</dd><dt><code>&#8211;strip-underscores</code></dt>
<dd>On some systems, both the C and C++ compilers put an underscore in front of every name. For example, the C name <tt>&quot;foo&quot;</tt> gets the low-level name <tt>&quot;_foo&quot;</tt>. This option removes the initial underscore. Whether <code>c++filt</code> removes the underscore by default is target dependent.</dd>
<dt><code>-j</code></dt>
<dd>
</dd><dt><code>&#8211;java</code></dt>
<dd>Prints demangled names using Java syntax. The default is to use C++ syntax.</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;no-strip-underscores</code></dt>
<dd>Do not remove the initial underscore.</dd>
<dt><code>-p</code></dt>
<dd>
</dd><dt><code>&#8211;no-params</code></dt>
<dd>When demangling the name of a function, do not display the types of the function&#8217;s parameters.</dd>
<dt><code>-s</code> <i>format</i></dt>
<dd>
</dd><dt><code>&#8211;format=</code><i>format</i></dt>
<dd><code>c++filt</code> can decode various methods of mangling, used by different compilers. The argument to this option selects which method it uses:</dd>
<dl>
<dd>
</dd><dl>
<dt>auto</dt>
<dd>Automatic selection based on executable (the default method)</dd>
<dt>gnu</dt>
<dd>the one used by the GNU C++ compiler (g++)</dd>
<dt>lucid</dt>
<dd>the one used by the Lucid compiler (lcc)</dd>
<dt>arm</dt>
<dd>the one specified by the C++ Annotated Reference Manual</dd>
<dt>hp</dt>
<dd>the one used by the HP compiler (aCC)</dd>
<dt>edg</dt>
<dd>the one used by the EDG compiler</dd>
<dt>gnu-v3</dt>
<dd>the one used by the GNU C++ compiler (g++) with the V3 ABI.</dd>
<dt>java</dt>
<dd>the one used by the GNU Java compiler (gcj)</dd>
<dt>gnat</dt>
<dd>the one used by the GNU Ada compiler (GNAT).</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>&#8211;help</code></dt>
<dd>Print a summary of the options to <code>c++filt</code> and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print the version number of <code>c++filt</code> and exit.</dd></dl>
<h2>Footnotes</h2>
<dl>
<dt>1.</dt>
<dd>MS-DOS does not allow <tt>&quot;+&quot;</tt> characters in file names, so on MS-DOS this program is named <code>CXXFILT</code>.</dd></dl>
<h2>See Also</h2>
<p>the Info entries for <i>binutils</i>.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;GNU Free Documentation License&#8221;.</p>
