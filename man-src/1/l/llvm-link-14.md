---
title: "llvm-link-14(1)"
name: "llvm-link-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-link-14/"
description: "llvm-link – LLVM bitcode linker"
---

<h2 class="name">NAME</h2>
<p> llvm-link &#8211; LLVM bitcode linker </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-link</code> [<i>options</i>] <i>filename …</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-link</code> takes several LLVM bitcode files and links them together into a single LLVM bitcode file. It writes the output file to standard output, unless the <i>-o</i> option is used to specify a filename.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>llvm-link</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-link</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-o filename</code></p>
<dd> Specify the output file name. If <code>filename</code> is “<code>&#8211;</code>”, then <code>llvm-link</code> will write its output to standard output.</p>
<dt><code>-S</code></p>
<dd> Write output in LLVM intermediate language (instead of bitcode).</p>
<dt><code>-d</code></p>
<dd> If specified, <code>llvm-link</code> prints a human-readable version of the output bitcode file to standard error.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Print information about what <code>llvm-link</code> is doing. This typically includes a message for each bitcode file linked in and for each library found.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-link</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
