---
title: "gsi(1)"
name: "gsi"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsi/"
description: "gsi – Gambit-C Scheme Interpreter and Compiler"
---

<h2 class="name">NAME</h2>
<p> gsi &#8211; Gambit-C Scheme Interpreter and Compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>gsi </code> [ &#8211;<code>:</code><i>arg</i>,&#8230; ] [ <code>-f</code> ] [ <code>-v</code> ] [[-] [ <code>-e</code> ] [ <i>file</i> ]]&#8230;<br />
 <code>gsc </code> [<i>options</i>] [<i>files</i>] </p>
<p> <code>gsc-script, gsi-script, scheme-ieee-1178-1990, scheme-r4rs, scheme-srfi-0, six</code>, and <code>six-script</code>: currently synonyms for <code>gsi</code>. </p>
<p> <code>scheme-r5rs</code> is registered in the Debian alternatives system and can be configured to point at <code>gsi</code>. </p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>gsi</code> and <code>gsc</code> commands. </p>
<p> The <code>Gambit-C</code> programming system is a full implementation of the Scheme language which conforms to the R4RS, R5RS, and IEEE Scheme standards. It consists of two main programs: <code>gsi</code>, the Gambit Scheme interpreter, and <code>gsc</code>, the Gambit Scheme compiler. The interpreter provides an interactive environment with a debugger, while the compiler can produce stand-alone executables or modules which can be linked or loaded at run time. Interpreted code and compiled code can be freely mixed. C modules can be linked with Scheme modules. </p>
<p> The interpreter is executed in <code>interactive mode</code> when no file or `-&#8216; or `-e&#8217; option is given on the command line. When at least one file or `-&#8216; or `-e&#8217; option is present the interpreter is executed in <code>batch mode</code>. </p>
<p> Entering <code>,q</code> or (exit) at the interpreter&#8217;s command prompt will exit the interpreter. </p>
<p> Entering <code>,?</code> at the interpreter&#8217;s command prompt will display a list of special commands. </p>
<p> In <code>batch mode</code> the command line arguments denote files to be loaded, REPL interactions to start (`-&#8216; option), and expressions to be evaluated (`-e&#8217; option). Note that the `-&#8216; and `-e&#8217; options can be interspersed with the files on the command line and can occur multiple times. The interpreter processes the command line arguments from left to right, loading files with the `load&#8217; procedure and evaluating expressions with the `eval&#8217; procedure in the global interaction environment. After this processing the interpreter exits. </p>
<p> <code>gsc-cc-o.bat</code> is a script called by <code>gsc</code> to generate object files during compilation. It takes its data from environment variables and is not intended for user interaction. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the Info files.</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> Initiate a REPL at this point. (Continue by issuing a <code>,c</code> command at the interpreter prompt)</p>
<dt><code>-:</code></p>
<dd> Comma separated list of run-time options</p>
<dt><code>-e</code></p>
<dd> Evaluate an expression.</p>
<dt><code>-f</code></p>
<dd> Skip initialization file.</p>
<dt><code>-v</code></p>
<dd> Show version of program.</dl>
<h2>SEE ALSO</h2>
<p> The documentation for these programs is arguably too extensive to cover with man pages. Only the common command line options are given here. The programs are documented fully in <code>Gambit-C</code>, available on-line at the Gambit-C Homepage. Once package gambc-doc is installed, this 200+ page document is available via the Info system (info gambit-c), in html via doc-base, or as files in /usr/share/doc/gambc (html, pdf, txt). </p>
<p> The Debian package r5rs-doc provides the <a href="/docs/linux/man/5-revised/">Revised</a>(5) Report on the Algorithmic Language Scheme in several formats. That document is the defining description of the programming language Scheme. </p>
<p> <code><a href="/docs/linux/man/1-dhelp/">dhelp</a>(1), <a href="/docs/linux/man/1-gcc/">gcc</a>(1), <a href="/docs/linux/man/8-update-alternatives/">update-alternatives</a>(8)</code></p>
<h2>COPYRIGHT</h2>
<p> Gambit-C is Copyright (c) 1994-2009 by Marc Feeley, all rights reserved. </p>
<p> Gambit-C is released under a dual LGPL and Apache 2 license.<br />
 For further information refer to /usr/share/doc/gambc/copyright. </p>
<p> This manual page is<br />
 Copyright (c) 2006-2009 Marc Feeley and Kurt B. Kaiser &lt;kbk [at] shore.net&gt;<br />
 Released under the same license as Gambit-C. </p>
<h2>AUTHOR</h2>
<p> Gambit-C was written by Marc Feeley &lt;gambit [at] iro.umontreal.ca&gt;. </p>
<p> Homepage: <a rel="nofollow" href="http://gambit.iro.umontreal.ca">http://gambit.iro.umontreal.ca</a> </p>
<h2>Index</h2>
