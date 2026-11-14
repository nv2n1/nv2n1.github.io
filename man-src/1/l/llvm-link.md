---
title: "llvm-link(1)"
name: "llvm-link"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-link/"
description: "llvm-link – LLVM linker"
---

<h2 class="name">NAME</h2>
<p> llvm-link &#8211; LLVM linker </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-link</code> [<i>options</i>] <i>filename &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-link</code> takes several <font SIZE="-1">LLVM</font> bitcode files and links them together into a single <font SIZE="-1">LLVM</font> bitcode file. It writes the output file to standard output, unless the <code>-o</code> option is used to specify a filename. </p>
<p> <code>llvm-link</code> attempts to load the input files from the current directory. If that fails, it looks for each file in each of the directories specified by the <code>-L</code> options on the command line. The library search paths are global; each one is searched for every input file if necessary. The directories are searched in the order they were specified on the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-L</code> <i>directory</i></p>
<dd> Add the specified <i>directory</i> to the library search path. When looking for libraries, <code>llvm-link</code> will look in path name for libraries. This option can be specified multiple times; <code>llvm-link</code> will search inside these directories in the order in which they were specified on the command line.</p>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>llvm-link</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-link</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output file name. If <i>filename</i> is <tt>&quot;-&quot;</tt>, then <code>llvm-link</code> will write its output to standard output.</p>
<dt><code>-S</code></p>
<dd> Write output in <font SIZE="-1">LLVM</font> intermediate language (instead of bitcode).</p>
<dt><code>-d</code></p>
<dd> If specified, <code>llvm-link</code> prints a human-readable version of the output bitcode file to standard error.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Print information about what <code>llvm-link</code> is doing. This typically includes a message for each bitcode file linked in and for each library found.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-link</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> gccld</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
