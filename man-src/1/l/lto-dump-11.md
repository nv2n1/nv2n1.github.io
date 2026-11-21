---
title: "lto-dump-11(1)"
name: "lto-dump-11"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lto-dump-11/"
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
<dt><code>-list</code></dt>
<dd> Dumps list of details of functions and variables.</dd>
<dt><code>-demangle</code></dt>
<dd> Dump the demangled output.</dd>
<dt><code>-defined-only</code></dt>
<dd> Dump only the defined symbols.</dd>
<dt><code>-print-value</code></dt>
<dd> Dump initial values of the variables.</dd>
<dt><code>-name-sort</code></dt>
<dd> Sort the symbols alphabetically.</dd>
<dt><code>-size-sort</code></dt>
<dd> Sort the symbols according to size.</dd>
<dt><code>-reverse-sort</code></dt>
<dd> Dump the symbols in reverse order.</dd>
<dt><code>-no-sort</code></dt>
<dd> Dump the symbols in order of occurrence.</dd>
<dt><code>-symbol=</code></dt>
<dd> Dump the details of specific symbol.</dd>
<dt><code>-objects</code></dt>
<dd> Dump the details of <font SIZE="-1">LTO</font> objects.</dd>
<dt><code>-type-stats</code></dt>
<dd> Dump the statistics of tree types.</dd>
<dt><code>-tree-stats</code></dt>
<dd> Dump the statistics of trees.</dd>
<dt><code>-gimple-stats</code></dt>
<dd> Dump the statistics of gimple statements.</dd>
<dt><code>-dump-level=</code></dt>
<dd> For deciding the optimization level of body.</dd>
<dt><code>-dump-body=</code></dt>
<dd> Dump the specific gimple body.</dd>
<dt><code>-help</code></dt>
<dd> Display the dump tool help.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2017-2021 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i>gfdl</i>(7) man page. </p>
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
