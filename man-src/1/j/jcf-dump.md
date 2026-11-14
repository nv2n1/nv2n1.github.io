---
title: "jcf-dump(1)"
name: "jcf-dump"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jcf-dump/"
description: "jcf-dump – print information about Java class files"
---

<h2 class="name">NAME</h2>
<p> jcf-dump &#8211; print information about Java class files </p>
<h2>SYNOPSIS</h2>
<p> jcf-dump [<code>-c</code>] [<code>&#8211;javap</code>]<br />
&nbsp;<wbr>[<code>&#8211;classpath</code>=<i>path</i>]&nbsp;<wbr>[<code>&#8211;CLASSPATH</code>=<i>path</i>]<br />
&nbsp;<wbr>[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>file</i>]<br />
&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>-v</code>]&nbsp;<wbr>[<code>&#8211;verbose</code>]<br />
&nbsp;<wbr><i>classname</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This is a class file examiner, similar to <tt>&quot;javap&quot;</tt>. It will print information about a number of classes, which are specified by class name or file name.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Disassemble method bodies. By default method bodies are not printed.</p>
<dt><code>&#8211;print-constants</code></p>
<dd> Print the constant pool. When printing a reference to a constant also print its index in the constant pool.</p>
<dt><code>&#8211;javap</code></p>
<dd> Generate output in <tt>&quot;javap&quot;</tt> format. The implementation of this feature is very incomplete.</p>
<dt><code>&#8211;classpath=</code><i>path</i></p>
<dd>
<dt><code>&#8211;CLASSPATH=</code><i>path</i></p>
<dd>
<dt><code>-I</code><i>directory</i></p>
<dd>
<dt><code>-o</code> <i>file</i></p>
<dd> These options as the same as the corresponding <code>gcj</code> options.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help, then exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version number, then exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print extra information while running. Implies <tt>&quot;--print-constants&quot;</tt>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-gcj/">gcj</a></i>(1), <i><a href="/docs/linux/man/1-gcjh/">gcjh</a></i>(1), <i><a href="/docs/linux/man/1-gij/">gij</a></i>(1), <i><a href="/docs/linux/man/1-jcf-dump/">jcf-dump</a></i>(1), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), and the Info entries for <i>gcj</i> and <i>gcc</i>.</p>
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
