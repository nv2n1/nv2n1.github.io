---
title: "llvm-prof(1)"
name: "llvm-prof"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-prof/"
description: "llvm-prof – print execution profile of LLVM program"
---

<h2 class="name">NAME</h2>
<p> llvm-prof &#8211; print execution profile of LLVM program </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-prof</code> [<i>options</i>] [<i>bitcode file</i>] [<i>llvmprof.out</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-prof</code> tool reads in an <i>llvmprof.out</i> file (which can optionally use a specific file with the third program argument), a bitcode file for the program, and produces a human readable report, suitable for determining where the program hotspots are. </p>
<p> This program is often used in conjunction with the <i>utils/profile.pl</i> script. This script automatically instruments a program, runs it with the <font SIZE="-1">JIT</font>, then runs <code>llvm-prof</code> to format a report. To get more information about <i>utils/profile.pl</i>, execute it with the <code>-help</code> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;annotated-llvm</code> or <code>-A</code></p>
<dd> In addition to the normal report printed, print out the code for the program, annotated with execution frequency information. This can be particularly useful when trying to visualize how frequently basic blocks are executed. This is most useful with basic block profiling information or better.</p>
<dt><code>&#8211;print-all-code</code></p>
<dd> Using this option enables the <code>&#8211;annotated-llvm</code> option, but it prints the entire module, instead of just the most commonly executed functions.</p>
<dt><code>&#8211;time-passes</code></p>
<dd> Record the amount of time needed for each pass and print it to standard error.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-prof</code> returns 1 if it cannot load the bitcode file or the profile information. Otherwise, it exits with zero.</p>
<h2>AUTHOR</h2>
<p> <code>llvm-prof</code> is maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
