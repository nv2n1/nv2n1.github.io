---
title: "llvm-extract-14(1)"
name: "llvm-extract-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-extract-14/"
description: "llvm-extract – extract a function from an LLVM module"
---

<h2 class="name">NAME</h2>
<p> llvm-extract &#8211; extract a function from an LLVM module </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-extract</code> [<i>options</i>] <code>–func</code> <i>function-name</i> [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-extract</code> command takes the name of a function and extracts it from the specified LLVM bitcode file. It is primarily used as a debugging tool to reduce test cases from larger programs that are triggering a bug. </p>
<p> In addition to extracting the bitcode of the specified function, <code>llvm-extract</code> will also remove unreachable global variables, prototypes, and unused types. </p>
<p> The <code>llvm-extract</code> command reads its input from standard input if filename is omitted or if filename is <code>&#8211;</code>. The output is always written to standard output, unless the <code>-o</code> option is specified (see below).</p>
<h2>OPTIONS</h2>
<p> <code>–alias</code> <i>alias-name</i> Extract the alias named <i>function-name</i> from the LLVM bitcode. May be specified multiple times to extract multiple alias at once. </p>
<p> <code>–ralias</code> <i>alias-regular-expr</i> Extract the alias matching <i>alias-regular-expr</i> from the LLVM bitcode. All alias matching the regular expression will be extracted. May be specified multiple times. </p>
<p> <code>–bb</code> <i>basic-block-specifier</i> Extract basic blocks(s) specified in <i>basic-block-specifier</i>. May be specified multiple times. Each &lt;function:bb[;bb]&gt; specifier pair will create a function. If multiple basic blocks are specified in one pair, the first block in the sequence should dominate the rest. </p>
<p> <code>–delete</code> Delete specified Globals from Module. </p>
<p> <code>-f</code> Enable binary output on terminals. Normally, <code>llvm-extract</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>llvm-extract</code> will write raw bitcode regardless of the output device. </p>
<p> <code>–func</code> <i>function-name</i> Extract the function named <i>function-name</i> from the LLVM bitcode. May be specified multiple times to extract multiple functions at once. </p>
<p> <code>–rfunc</code> <i>function-regular-expr</i> Extract the function(s) matching <i>function-regular-expr</i> from the LLVM bitcode. All functions matching the regular expression will be extracted. May be specified multiple times. </p>
<p> <code>–glob</code> <i>global-name</i> Extract the global variable named <i>global-name</i> from the LLVM bitcode. May be specified multiple times to extract multiple global variables at once. </p>
<p> <code>–rglob</code> <i>glob-regular-expr</i> Extract the global variable(s) matching <i>global-regular-expr</i> from the LLVM bitcode. All global variables matching the regular expression will be extracted. May be specified multiple times. </p>
<p> <code>–keep-const-init</code> Preserve the values of constant globals. </p>
<p> <code>–recursive</code> Recursively extract all called functions </p>
<p> <code>-help</code> Print a summary of command line options. </p>
<p> <code>-o</code> <i>filename</i> Specify the output filename. If filename is “-” (the default), then <code>llvm-extract</code> sends its output to standard output. </p>
<p> <code>-S</code> Write output in LLVM intermediate language (instead of bitcode).</p>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-extract</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bugpoint/">bugpoint</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
