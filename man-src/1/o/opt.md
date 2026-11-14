---
title: "opt(1)"
name: "opt"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opt/"
description: "opt – LLVM optimizer"
---

<h2 class="name">NAME</h2>
<p> opt &#8211; LLVM optimizer </p>
<h2>SYNOPSIS</h2>
<p> <code>opt</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>opt</code> command is the modular <font SIZE="-1">LLVM</font> optimizer and analyzer. It takes <font SIZE="-1">LLVM</font> source files as input, runs the specified optimizations or analyses on it, and then outputs the optimized file or the analysis results. The function of <code>opt</code> depends on whether the <code>-analyze</code> option is given. </p>
<p> When <code>-analyze</code> is specified, <code>opt</code> performs various analyses of the input source. It will usually print the results on standard output, but in a few cases, it will print output to standard error or generate a file with the analysis output, which is usually done when the output is meant for another program. </p>
<p> While <code>-analyze</code> is <i>not</i> given, <code>opt</code> attempts to produce an optimized output file. The optimizations available via <code>opt</code> depend upon what libraries were linked into it as well as any additional libraries that have been loaded with the <code>-load</code> option. Use the <code>-help</code> option to determine what optimizations you can use. </p>
<p> If <i>filename</i> is omitted from the command line or is <i>&#8211;</i>, <code>opt</code> reads its input from standard input. Inputs can be in either the <font SIZE="-1">LLVM</font> assembly language format (.ll) or the <font SIZE="-1">LLVM</font> bitcode format (.bc). </p>
<p> If an output filename is not specified with the <code>-o</code> option, <code>opt</code> writes its output to the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Enable binary output on terminals. Normally, <code>opt</code> will refuse to write raw bitcode output if the output stream is a terminal. With this option, <code>opt</code> will write raw bitcode regardless of the output device.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o</code> <i>filename</i></p>
<dd> Specify the output filename.</p>
<dt><code>-S</code></p>
<dd> Write output in <font SIZE="-1">LLVM</font> intermediate language (instead of bitcode).</p>
<dt><code>-{passname}</code></p>
<dd> <code>opt</code> provides the ability to run any of <font SIZE="-1">LLVM</font>&#8216;s optimization or analysis passes in any order. The <code>-help</code> option lists all the passes available. The order in which the options occur on the command line are the order in which they are executed (within pass constraints).</p>
<dt><code>-std-compile-opts</code></p>
<dd> This is short hand for a standard list of <i>compile time optimization</i> passes. This is typically used to optimize the output from the llvm-gcc front end. It might be useful for other front end compilers as well. To discover the full set of options available, use the following command: </p>
<pre>
   llvm-as &lt; /dev/null | opt -std-compile-opts -disable-output -debug-pass=Arguments
</pre>
<dt><code>-disable-inlining</code></p>
<dd> This option is only meaningful when <code>-std-compile-opts</code> is given. It simply removes the inlining pass from the standard list.</p>
<dt><code>-disable-opt</code></p>
<dd> This option is only meaningful when <code>-std-compile-opts</code> is given. It disables most, but not all, of the <code>-std-compile-opts</code>. The ones that remain are <code>-verify</code>, <code>-lower-setjmp</code>, and <code>-funcresolve</code>.</p>
<dt><code>-strip-debug</code></p>
<dd> This option causes opt to strip debug information from the module before applying other optimizations. It is essentially the same as <code>-strip</code> but it ensures that stripping of debug information is done first.</p>
<dt><code>-verify-each</code></p>
<dd> This option causes opt to add a verify pass after every pass otherwise specified on the command line (including <code>-verify</code>). This is useful for cases where it is suspected that a pass is creating an invalid module but it is not clear which pass is doing it. The combination of <code>-std-compile-opts</code> and <code>-verify-each</code> can quickly track down this kind of problem.</p>
<dt><code>-profile-info-file</code> <i>filename</i></p>
<dd> Specify the name of the file loaded by the -profile-loader option.</p>
<dt><code>-stats</code></p>
<dd> Print statistics.</p>
<dt><code>-time-passes</code></p>
<dd> Record the amount of time needed for each pass and print it to standard error.</p>
<dt><code>-debug</code></p>
<dd> If this is a debug build, this option will enable debug printouts from passes which use the <i></i><font SIZE="-1"><i>DEBUG</i></font><i>()</i> macro. See the <font SIZE="-1"><code>LLVM</code></font><code> Programmer&#8217;s Manual</code>, section <i>#DEBUG</i> for more information.</p>
<dt><code>-load</code>=<i>plugin</i></p>
<dd> Load the dynamic object <i>plugin</i>. This object should register new optimization or analysis passes. Once loaded, the object will add new command line options to enable various optimizations or analyses. To see the new complete list of optimizations, use the <code>-help</code> and <code>-load</code> options together. For example: </p>
<pre>
   opt -load=plugin.so -help
</pre>
<dt><code>-p</code></p>
<dd> Print module after each transformation.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>opt</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
