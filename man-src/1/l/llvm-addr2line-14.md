---
title: "llvm-addr2line-14(1)"
name: "llvm-addr2line-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-addr2line-14/"
description: "llvm-addr2line – a drop-in replacement for addr2line"
---

<h2 class="name">NAME</h2>
<p> llvm-addr2line &#8211; a drop-in replacement for addr2line </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-addr2line</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-addr2line</code> is an alias for the <code><a href="/docs/linux/man/1-llvm-symbolizer/">llvm-symbolizer</a>(1)</code> tool with different defaults. The goal is to make it a drop-in replacement for GNU’s <code>addr2line</code>. </p>
<p> Here are some of those differences:</p>
<dl>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> interprets all addresses as hexadecimal and ignores an optional <code>0x</code> prefix, whereas <code>llvm-symbolizer</code> attempts to determine the base from the literal’s prefix and defaults to decimal if there is no prefix.</p>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> defaults not to print function names. Use <i>-f</i> to enable that.</p>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> defaults not to demangle function names. Use <i>-C</i> to switch the demangling on.</p>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> defaults not to print inlined frames. Use <i>-i</i> to show inlined frames for a source code location in an inlined function.</p>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> uses <i>–output-style=GNU</i> by default.</p>
<dt>&bull;</p>
<dd> <code>llvm-addr2line</code> parses options from the environment variable <code>LLVM_ADDR2LINE_OPTS</code> instead of from <code>LLVM_SYMBOLIZER_OPTS</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-symbolizer/">llvm-symbolizer</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
