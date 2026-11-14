---
title: "llvm-dis(1)"
name: "llvm-dis"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-dis/"
description: "llvm-dis – LLVM disassembler"
---

<h2 class="name">NAME</h2>
<p> llvm-dis &#8211; LLVM disassembler </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-dis</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-dis</code> command is the <font SIZE="-1">LLVM</font> disassembler. It takes an <font SIZE="-1">LLVM</font> bitcode file and converts it into human-readable <font SIZE="-1">LLVM</font> assembly language. </p>
<p> If filename is omitted or specified as <tt>&quot;-&quot;</tt>, <code>llvm-dis</code> reads its input from standard input. </p>
<p> If the input is being read from standard input, then <code>llvm-dis</code> will send its output to standard output by default. Otherwise, the output will be written to a file named after the input file, with a <tt>&quot;.ll&quot;</tt> suffix added (any existing <tt>&quot;.bc&quot;</tt> suffix will first be removed). You can override the choice of output file using the <code>-o</code> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>llvm-dis</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-dis</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output file name. If <i>filename</i> is -, then the output is sent to standard output.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-dis</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> llvm-as</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
