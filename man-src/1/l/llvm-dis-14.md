---
title: "llvm-dis-14(1)"
name: "llvm-dis-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-dis-14/"
description: "llvm-dis – LLVM disassembler"
---

<h2 class="name">NAME</h2>
<p> llvm-dis &#8211; LLVM disassembler </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-dis</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-dis</code> command is the LLVM disassembler. It takes an LLVM bitcode file and converts it into human-readable LLVM assembly language. </p>
<p> If filename is omitted or specified as <code>&#8211;</code>, <code>llvm-dis</code> reads its input from standard input. </p>
<p> If the input is being read from standard input, then <code>llvm-dis</code> will send its output to standard output by default. Otherwise, the output will be written to a file named after the input file, with a <code>.ll</code> suffix added (any existing <code>.bc</code> suffix will first be removed). You can override the choice of output file using the <code>-o</code> option.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code> Enable binary output on terminals. Normally, <code>llvm-dis</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-dis</code> will write raw bitcode regardless of the output device. </p>
<p> <code>-help</code> Print a summary of command line options. </p>
<p> <code>-o</code> <i>filename</i> Specify the output file name. If <i>filename</i> is -, then the output is sent to standard output.</p>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-dis</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-as/">llvm-as</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
