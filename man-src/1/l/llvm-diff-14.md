---
title: "llvm-diff-14(1)"
name: "llvm-diff-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-diff-14/"
description: "llvm-diff – LLVM structural ‘diff’"
---

<h2 class="name">NAME</h2>
<p> llvm-diff &#8211; LLVM structural &#8216;diff&#8217; </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-diff</code> [<i>options</i>] <i>module 1</i> <i>module 2</i> [<i>global name …</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-diff</code> compares the structure of two LLVM modules, primarily focusing on differences in function definitions. Insignificant differences, such as changes in the ordering of globals or in the names of local values, are ignored. </p>
<p> An input module will be interpreted as an assembly file if its name ends in ‘.ll’; otherwise it will be read in as a bitcode file. </p>
<p> If a list of global names is given, just the values with those names are compared; otherwise, all global values are compared, and diagnostics are produced for globals which only appear in one module or the other. </p>
<p> <code>llvm-diff</code> compares two functions by comparing their basic blocks, beginning with the entry blocks. If the terminators seem to match, then the corresponding successors are compared; otherwise they are ignored. This algorithm is very sensitive to changes in control flow, which tend to stop any downstream changes from being detected. </p>
<p> <code>llvm-diff</code> is intended as a debugging tool for writers of LLVM passes and frontends. It does not have a stable output format.</p>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-diff</code> finds no differences between the modules, it will exit with 0 and produce no output. Otherwise it will exit with a non-zero value.</p>
<h2>BUGS</h2>
<p> Many important differences, like changes in linkage or function attributes, are not diagnosed. </p>
<p> Changes in memory behavior (for example, coalescing loads) can cause massive detected differences in blocks.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
