---
title: "lto-dump-12(1)"
name: "lto-dump-12"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lto-dump-12/"
description: "lto-dump – Tool for dumping LTO object files"
---

<h2 class="name">NAME</h2>
<p> lto-dump &#8211; Tool for dumping LTO object files </p>
<h2>SYNOPSIS</h2>
<p> lto-dump [<code>-list</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-demangle</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-defined-only</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-print-value</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-name-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-size-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-reverse-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-no-sort</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-symbol=</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-objects</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-type-stats</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-tree-stats</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-gimple-stats</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-dump-level=</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-dump-body=</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-help</code>]&nbsp;<i>lto-dump</i></p>
<h2>DESCRIPTION</h2>
<p> <code>lto-dump</code> is a tool you can use in conjunction with <font SIZE="-1">GCC</font> to dump link time optimization object files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-list</code></p>
<dd> Dumps list of details of functions and variables.</p>
<dt><code>-demangle</code></p>
<dd> Dump the demangled output.</p>
<dt><code>-defined-only</code></p>
<dd> Dump only the defined symbols.</p>
<dt><code>-print-value</code></p>
<dd> Dump initial values of the variables.</p>
<dt><code>-name-sort</code></p>
<dd> Sort the symbols alphabetically.</p>
<dt><code>-size-sort</code></p>
<dd> Sort the symbols according to size.</p>
<dt><code>-reverse-sort</code></p>
<dd> Dump the symbols in reverse order.</p>
<dt><code>-no-sort</code></p>
<dd> Dump the symbols in order of occurrence.</p>
<dt><code>-symbol=</code></p>
<dd> Dump the details of specific symbol.</p>
<dt><code>-objects</code></p>
<dd> Dump the details of <font SIZE="-1">LTO</font> objects.</p>
<dt><code>-type-stats</code></p>
<dd> Dump the statistics of tree types.</p>
<dt><code>-tree-stats</code></p>
<dd> Dump the statistics of trees.</p>
<dt><code>-gimple-stats</code></p>
<dd> Dump the statistics of gimple statements.</p>
<dt><code>-dump-level=</code></p>
<dd> For deciding the optimization level of body.</p>
<dt><code>-dump-body=</code></p>
<dd> Dump the specific gimple body.</p>
<dt><code>-help</code></p>
<dd> Display the dump tool help.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2017-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <code><a href="/docs/linux/man/7-gfdl/">gfdl</a></code>(7) man page. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
<h2>Index</h2>
