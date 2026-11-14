---
title: "llvm-extract(1)"
name: "llvm-extract"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-extract/"
description: "llvm-extract – extract a function from an LLVM module"
---

<h2 class="name">NAME</h2>
<p> llvm-extract &#8211; extract a function from an LLVM module </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-extract</code> [<i>options</i>] <code>&#8211;func</code> <i>function-name</i> [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-extract</code> command takes the name of a function and extracts it from the specified <font SIZE="-1">LLVM</font> bitcode file. It is primarily used as a debugging tool to reduce test cases from larger programs that are triggering a bug. </p>
<p> In addition to extracting the bitcode of the specified function, <code>llvm-extract</code> will also remove unreachable global variables, prototypes, and unused types. </p>
<p> The <code>llvm-extract</code> command reads its input from standard input if filename is omitted or if filename is -. The output is always written to standard output, unless the <code>-o</code> option is specified (see below).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>llvm-extract</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-extract</code> will write raw bitcode regardless of the output device.</p>
<dt><code>&#8211;func</code> <i>function-name</i></p>
<dd> Extract the function named <i>function-name</i> from the <font SIZE="-1">LLVM</font> bitcode. May be specified multiple times to extract multiple functions at once.</p>
<dt><code>&#8211;glob</code> <i>global-name</i></p>
<dd> Extract the global variable named <i>global-name</i> from the <font SIZE="-1">LLVM</font> bitcode. May be specified multiple times to extract multiple global variables at once.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output filename. If filename is &#8220;-&#8221; (the default), then <code>llvm-extract</code> sends its output to standard output.</p>
<dt><code>-S</code></p>
<dd> Write output in <font SIZE="-1">LLVM</font> intermediate language (instead of bitcode).</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-extract</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> bugpoint</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
