---

title: "jv-convert(1)"
name: "jv-convert"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jv-convert/"
description: "jv-convert – Convert file from one encoding to another"
---

<p> jv-convert - Convert file from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>jv-convert</code> [<font SIZE="-1"><code>OPTION</code></font>] ... [<i></i><font SIZE="-1"><i>INPUTFILE</i></font><i></i> [<i></i><font SIZE="-1"><i>OUTPUTFILE</i></font><i></i>]]  </p>
<h2>DESCRIPTION</h2>
<p> <code>jv-convert</code> is a utility included with <code>&quot;libgcj&quot;</code> which converts a file from one encoding to another. It is similar to the Unix <code>iconv</code> utility. </p>
<p> The encodings supported by <code>jv-convert</code> are platform-dependent. Currently there is no way to get a list of all supported encodings.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>--encoding</code><i>name</i></dt>
<dd>  </dd>
<dt><code>--from</code><i>name</i></dt>
<dd> <p> Use <i>name</i> as the input encoding. The default is the current locale&#8217;s encoding. </p>
 </dd>
<dt><code>--to</code><i>name</i></dt>
<dd> <p> Use <i>name</i> as the output encoding. The default is the <code>&quot;JavaSrc&quot;</code> encoding; this is <font SIZE="-1">ASCII</font> with <code>\u</code> escapes for non-ASCII characters. </p>
 </dd>
<dt><code>-i</code><i>file</i></dt>
<dd> <p> Read from <i>file</i>. The default is to read from standard input. </p>
 </dd>
<dt><code>-o</code><i>file</i></dt>
<dd> <p> Write to <i>file</i>. The default is to write to standard output. </p>
 </dd>
<dt><code>--reverse</code></dt>
<dd> <p> Swap the input and output encodings. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Print a help message, then exit. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information, then exit. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the man page <i>gfdl</i>(7). </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre><code>     A GNU Manual
</code></pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre><code>     You have freedom to copy and modify this GNU Manual, like GNU
     software. Copies published by the Free Software Foundation raise
     funds for GNU development.
</code></pre>
