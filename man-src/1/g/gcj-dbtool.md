---
title: "gcj-dbtool(1)"
name: "gcj-dbtool"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcj-dbtool/"
description: "gcj-dbtool – Manipulate class file mapping databases for libgcj"
---

<h2 class="name">NAME</h2>
<p> gcj-dbtool &#8211; Manipulate class file mapping databases for libgcj </p>
<h2>SYNOPSIS</h2>
<p> gcj-dbtool <font SIZE="-1"><code>OPTION</code></font> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i> [<font SIZE="-1"><code>MORE</code></font>] &#8230; </p>
<p> gcj-dbtool [<code>-0</code>] [<code>&#8211;</code>] [<code>-n</code>] [<code>-a</code>] [<code>-f</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-t</code>]&nbsp;<wbr>[<code>-l</code>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr>[<i></i><font SIZE="-1"><i>LIBDIR</i></font><i></i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>]&nbsp;<wbr>[<code>-m</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>&#8211;help</code>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;gcj-dbtool&quot;</tt> is a tool for creating and manipulating class file mapping databases. <tt>&quot;libgcj&quot;</tt> can use these databases to find a shared library corresponding to the bytecode representation of a class. This functionality is useful for ahead-of-time compilation of a program that has no knowledge of <tt>&quot;gcj&quot;</tt>. </p>
<p> <tt>&quot;gcj-dbtool&quot;</tt> works best if all the jar files added to it are compiled using <tt>&quot;-findirect-dispatch&quot;</tt>. </p>
<p> Note that <tt>&quot;gcj-dbtool&quot;</tt> is currently available as &#8220;preview technology&#8221;. We believe it is a reasonable way to allow application-transparent ahead-of-time compilation, but this is an unexplored area. We welcome your comments.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i> <code>[</code><i></i><font SIZE="-1"><i>SIZE</i></font><i></i><code>]</code></p>
<dd> This creates a new database. Currently, databases cannot be resized; you can choose a larger initial size if desired. The default size is 32,749.</p>
<dt><code>-a</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i><i></i><font SIZE="-1"><i>JARFILE</i></font><i></i><i></i><font SIZE="-1"><i>LIB</i></font><i></i></p>
<dd>
<dt><code>-f</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i><i></i><font SIZE="-1"><i>JARFILE</i></font><i></i><i></i><font SIZE="-1"><i>LIB</i></font><i></i></p>
<dd> This adds a jar file to the database. For each class file in the jar, a cryptographic signature of the bytecode representation of the class is recorded in the database. At runtime, a class is looked up by its signature and the compiled form of the class is looked for in the corresponding shared library. The <code>-a</code> option will verify that <i></i><font SIZE="-1"><i>LIB</i></font><i></i> exists before adding it to the database; <code>-f</code> skips this check.</p>
<dt><code>[</code><code>&#8211;</code><code>][</code><code>-0</code><code>] -m</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i><i></i><font SIZE="-1"><i>DBFILE</i></font><i></i><code>,[</code><i></i><font SIZE="-1"><i>DBFILE</i></font><i></i><code>]</code></p>
<dd> Merge a number of databases. The output database overwrites any existing database. To add databases into an existing database, include the destination in the list of sources. </p>
<p> If <code>&#8211;</code> or <code>-0</code> are used, the list of files to read is taken from standard input instead of the command line. For <code>-0</code>, Input filenames are terminated by a null character instead of by whitespace. Useful when arguments might contain white space. The <font SIZE="-1">GNU</font> find -print0 option produces input suitable for this mode.</p>
<dt><code>-t</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i></p>
<dd> Test a database.</p>
<dt><code>-l</code> <i></i><font SIZE="-1"><i>DBFILE</i></font><i></i></p>
<dd> List the contents of a database.</p>
<dt><code>-p</code></p>
<dd> Print the name of the default database. If there is no default database, this prints a blank line. If <i></i><font SIZE="-1"><i>LIBDIR</i></font><i></i> is specified, use it instead of the default library directory component of the database name.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message, then exit.</p>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>-v</code></p>
<dd> Print version information, then exit.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-gcj/">gcj</a></i>(1), <i><a href="/docs/linux/man/1-gcjh/">gcjh</a></i>(1), <i><a href="/docs/linux/man/1-jcf-dump/">jcf-dump</a></i>(1), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), and the Info entries for <i>gcj</i> and <i>gcc</i>.</p>
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
