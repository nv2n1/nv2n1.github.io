---
title: "opt-14(1)"
name: "opt-14"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opt-14/"
description: "opt – LLVM optimizer"
---

<h2 class="name">NAME</h2>
<p> opt &#8211; LLVM optimizer </p>
<h2>SYNOPSIS</h2>
<p> <code>opt</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>opt</code> command is the modular LLVM optimizer and analyzer. It takes LLVM source files as input, runs the specified optimizations or analyses on it, and then outputs the optimized file or the analysis results. The function of <code>opt</code> depends on whether the <i>-analyze</i> option is given. </p>
<p> When <i>-analyze</i> is specified, <code>opt</code> performs various analyses of the input source. It will usually print the results on standard output, but in a few cases, it will print output to standard error or generate a file with the analysis output, which is usually done when the output is meant for another program. </p>
<p> While <i>-analyze</i> is <i>not</i> given, <code>opt</code> attempts to produce an optimized output file. The optimizations available via <code>opt</code> depend upon what libraries were linked into it as well as any additional libraries that have been loaded with the <i>-load</i> option. Use the <i>-help</i> option to determine what optimizations you can use. </p>
<p> If <code>filename</code> is omitted from the command line or is “<code>&#8211;</code>”, <code>opt</code> reads its input from standard input. Inputs can be in either the LLVM assembly language format (<code>.ll</code>) or the LLVM bitcode format (<code>.bc</code>). </p>
<p> If an output filename is not specified with the <i>-o</i> option, <code>opt</code> writes its output to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>opt</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>opt</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o &lt;filename&gt;</code></p>
<dd> Specify the output filename.</p>
<dt><code>-S</code></p>
<dd> Write output in LLVM intermediate language (instead of bitcode).</p>
<dt><code>-{passname}</code></p>
<dd> <code>opt</code> provides the ability to run any of LLVM’s optimization or analysis passes in any order. The <i>-help</i> option lists all the passes available. The order in which the options occur on the command line are the order in which they are executed (within pass constraints).</p>
<dt><code>-strip-debug</code></p>
<dd> This option causes opt to strip debug information from the module before applying other optimizations. It is essentially the same as <i>-strip</i> but it ensures that stripping of debug information is done first.</p>
<dt><code>-verify-each</code></p>
<dd> This option causes opt to add a verify pass after every pass otherwise specified on the command line (including <i>-verify</i>). This is useful for cases where it is suspected that a pass is creating an invalid module but it is not clear which pass is doing it.</p>
<dt><code>-stats</code></p>
<dd> Print statistics.</p>
<dt><code>-time-passes</code></p>
<dd> Record the amount of time needed for each pass and print it to standard error.</p>
<dt><code>-debug</code></p>
<dd> If this is a debug build, this option will enable debug printouts from passes which use the <code>LLVM_DEBUG()</code> macro. See the <i>LLVM Programmer’s Manual</i>, section <code>#DEBUG</code> for more information.</p>
<dt><code>-load=&lt;plugin&gt;</code></p>
<dd> Load the dynamic object <code>plugin</code>. This object should register new optimization or analysis passes. Once loaded, the object will add new command line options to enable various optimizations or analyses. To see the new complete list of optimizations, use the <i>-help</i> and <i>-load</i> options together. For example: </p>
<pre>
opt -load=plugin.so -help
</pre>
<dt><code>-print-passes</code></p>
<dd> Print all available passes and exit.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>opt</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
