---
title: "llvm-as(1)"
name: "llvm-as"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-as/"
description: "llvm-as – LLVM assembler"
---

<h2 class="name">NAME</h2>
<p> llvm-as &#8211; LLVM assembler </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-as</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-as</code> is the <font SIZE="-1">LLVM</font> assembler. It reads a file containing human-readable <font SIZE="-1">LLVM</font> assembly language, translates it to <font SIZE="-1">LLVM</font> bitcode, and writes the result into a file or to standard output. </p>
<p> If <i>filename</i> is omitted or is <tt>&quot;-&quot;</tt>, then <code>llvm-as</code> reads its input from standard input. </p>
<p> If an output file is not specified with the <code>-o</code> option, then <code>llvm-as</code> sends its output to a file or standard output by following these rules:</p>
<dl>
<dt>*</p>
<dd> If the input is standard input, then the output is standard output.</p>
<dt>*</p>
<dd> If the input is a file that ends with <tt>&quot;.ll&quot;</tt>, then the output file is of the same name, except that the suffix is changed to <tt>&quot;.bc&quot;</tt>.</p>
<dt>*</p>
<dd> If the input is a file that does not end with the <tt>&quot;.ll&quot;</tt> suffix, then the output file has the same name as the input file, except that the <tt>&quot;.bc&quot;</tt> suffix is appended.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>llvm-as</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-as</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output file name. If <i>filename</i> is <tt>&quot;-&quot;</tt>, then <code>llvm-as</code> sends its output to standard output.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-as</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> llvm-dis, gccas</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
