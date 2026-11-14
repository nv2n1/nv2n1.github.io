---
title: "gccgo(1)"
name: "gccgo"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gccgo/"
description: "gccgo – A GCC-based compiler for the Go language"
---

<h2 class="name">NAME</h2>
<p> gccgo &#8211; A GCC-based compiler for the Go language </p>
<h2>SYNOPSIS</h2>
<p> gccgo [<code>-c</code>|<code>-S</code>]<br />
[<code>-g</code>]&nbsp;<wbr>[<code>-pg</code>]&nbsp;<wbr>[<code>-O</code><i>level</i>]<br />
[<code>-I</code><i>dir</i>&#8230;]&nbsp;<wbr>[<code>-L</code><i>dir</i>&#8230;]<br />
[<code>-o</code>&nbsp;<wbr><i>outfile</i>]&nbsp;<wbr><i>infile</i>&#8230; </p>
<p> Only the most useful options are listed here; see below for the remainder.</p>
<h2>DESCRIPTION</h2>
<p> The <code>gccgo</code> command is a frontend to <code>gcc</code> and supports many of the same options. This manual only documents the options specific to <code>gccgo</code>. </p>
<p> The <code>gccgo</code> command may be used to compile Go source code into an object file, link a collection of object files together, or do both in sequence. </p>
<p> Go source code is compiled as packages. A package consists of one or more Go source files. All the files in a single package must be compiled together, by passing all the files as arguments to <code>gccgo</code>. A single invocation of <code>gccgo</code> may only compile a single package. </p>
<p> One Go package may <tt>&quot;import&quot;</tt> a different Go package. The imported package must have already been compiled; <code>gccgo</code> will read the import data directly from the compiled package. When this package is later linked, the compiled form of the package must be included in the link command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-I</code><i>dir</i></p>
<dd> Specify a directory to use when searching for an import package at compile time.</p>
<dt><code>-L</code><i>dir</i></p>
<dd> When linking, specify a library search directory, as with <code>gcc</code>.</p>
<dt><code>-fgo-pkgpath=</code><i>string</i></p>
<dd> Set the package path to use. This sets the value returned by the PkgPath method of reflect.Type objects. It is also used for the names of globally visible symbols. The argument to this option should normally be the string that will be used to import this package after it has been installed; in other words, a pathname within the directories specified by the <code>-I</code> option.</p>
<dt><code>-fgo-prefix=</code><i>string</i></p>
<dd> An alternative to <code>-fgo-pkgpath</code>. The argument will be combined with the package name from the source file to produce the package path. If <code>-fgo-pkgpath</code> is used, <code>-fgo-prefix</code> will be ignored. </p>
<p> Go permits a single program to include more than one package with the same name in the <tt>&quot;package&quot;</tt> clause in the source file, though obviously the two packages must be imported using different pathnames. In order for this to work with <code>gccgo</code>, either <code>-fgo-pkgpath</code> or <code>-fgo-prefix</code> must be specified when compiling a package. </p>
<p> Using either <code>-fgo-pkgpath</code> or <code>-fgo-prefix</code> disables the special treatment of the <tt>&quot;main&quot;</tt> package and permits that package to be imported like any other.</p>
<dt><code>-fgo-relative-import-path=</code><i>dir</i></p>
<dd> A relative import is an import that starts with <i>./</i> or <i>../</i>. If this option is used, <code>gccgo</code> will use <i>dir</i> as a prefix for the relative import when searching for it.</p>
<dt><code>-frequire-return-statement</code></p>
<dd>
<dt><code>-fno-require-return-statement</code></p>
<dd> By default <code>gccgo</code> will warn about functions which have one or more return parameters but lack an explicit <tt>&quot;return&quot;</tt> statement. This warning may be disabled using <code>-fno-require-return-statement</code>.</p>
<dt><code>-fgo-check-divide-zero</code></p>
<dd> Add explicit checks for division by zero. In Go a division (or modulos) by zero causes a panic. On Unix systems this is detected in the runtime by catching the <tt>&quot;SIGFPE&quot;</tt> signal. Some processors, such as PowerPC, do not generate a <font SIZE="-1">SIGFPE</font> on division by zero. Some runtimes do not generate a signal that can be caught. On those systems, this option may be used. Or the checks may be removed via <code>-fno-go-check-divide-zero</code>. This option is currently on by default, but in the future may be off by default on systems that do not require it.</p>
<dt><code>-fgo-check-divide-overflow</code></p>
<dd> Add explicit checks for division overflow. For example, division overflow occurs when computing <tt>&quot;INT_MIN / -1&quot;</tt>. In Go this should be wrapped, to produce <tt>&quot;INT_MIN&quot;</tt>. Some processors, such as x86, generate a trap on division overflow. On those systems, this option may be used. Or the checks may be removed via <code>-fno-go-check-divide-overflow</code>. This option is currently on by default, but in the future may be off by default on systems that do not require it.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-gpl/">gpl</a></i>(7), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), <i><a href="/docs/linux/man/7-fsf-funding/">fsf-funding</a></i>(7), <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) and the Info entries for <i>gccgo</i> and <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2010-2013 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the man page <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7). </p>
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
