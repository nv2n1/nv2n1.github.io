---
title: "grmic(1)"
name: "grmic"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grmic/"
description: "grmic – Generate stubs for Remote Method Invocation"
---

<h2 class="name">NAME</h2>
<p> grmic &#8211; Generate stubs for Remote Method Invocation </p>
<h2>SYNOPSIS</h2>
<p> <code>grmic</code> [<font SIZE="-1"><code>OPTION</code></font>] &#8230; <i>class</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>grmic</code> is a utility included with <tt>&quot;libgcj&quot;</tt> which generates stubs for remote objects. </p>
<p> Note that this program isn&#8217;t yet fully compatible with the <font SIZE="-1">JDK</font> <code>grmic</code>. Some options, such as <code>-classpath</code>, are recognized but currently ignored. We have left these options undocumented for now. </p>
<p> Long options can also be given with a GNU-style leading <code>&#8212;</code>. For instance, <code>&#8211;help</code> is accepted.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-keep</code></p>
<dd>
<dt><code>-keepgenerated</code></p>
<dd> By default, <code>grmic</code> deletes intermediate files. Either of these options causes it not to delete such files.</p>
<dt><code>-v1.1</code></p>
<dd> Cause <code>grmic</code> to create stubs and skeletons for the 1.1 protocol version.</p>
<dt><code>-vcompat</code></p>
<dd> Cause <code>grmic</code> to create stubs and skeletons compatible with both the 1.1 and 1.2 protocol versions. This is the default.</p>
<dt><code>-v1.2</code></p>
<dd> Cause <code>grmic</code> to create stubs and skeletons for the 1.2 protocol version.</p>
<dt><code>-nocompile</code></p>
<dd> Don&#8217;t compile the generated files.</p>
<dt><code>-verbose</code></p>
<dd> Print information about what <code>grmic</code> is doing.</p>
<dt><code>-d</code> <i>directory</i></p>
<dd> Put output files in <i>directory</i>. By default the files are put in the current working directory.</p>
<dt><code>-help</code></p>
<dd> Print a help message, then exit.</p>
<dt><code>-version</code></p>
<dd> Print version information, then exit.</dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the man page <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7). </p>
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
