---
title: "llc(1)"
name: "llc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llc/"
description: "llc – LLVM static compiler"
---

<h2 class="name">NAME</h2>
<p> llc &#8211; LLVM static compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>llc</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llc</code> command compiles <font SIZE="-1">LLVM</font> source inputs into assembly language for a specified architecture. The assembly language output can then be passed through a native assembler and linker to generate a native executable. </p>
<p> The choice of architecture for the output assembly code is automatically determined from the input file, unless the <code>-march</code> option is used to override the default.</p>
<h2>OPTIONS</h2>
<p> If <i>filename</i> is &#8211; or omitted, <code>llc</code> reads from standard input. Otherwise, it will from <i>filename</i>. Inputs can be in either the <font SIZE="-1">LLVM</font> assembly language format (.ll) or the <font SIZE="-1">LLVM</font> bitcode format (.bc). </p>
<p> If the <code>-o</code> option is omitted, then <code>llc</code> will send its output to standard output if the input is from standard input. If the <code>-o</code> option specifies -, then the output will also be sent to standard output. </p>
<p> If no <code>-o</code> option is specified and an input file other than &#8211; is specified, then <code>llc</code> creates the output filename by taking the input filename, removing any existing <i>.bc</i> extension, and adding a <i>.s</i> suffix. </p>
<p> Other <code>llc</code> options are as follows:</p>
<h2>End-user Options</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-O</code>=<i>uint</i></p>
<dd> Generate code at different optimization levels. These correspond to the <i>-O0</i>, <i>-O1</i>, <i>-O2</i>, <i>-O3</i>, and <i>-O4</i> optimization levels used by <code>llvm-gcc</code> and <code>clang</code>.</p>
<dt><code>-mtriple</code>=<i>target triple</i></p>
<dd> Override the target triple specified in the input file with the specified string.</p>
<dt><code>-march</code>=<i>arch</i></p>
<dd> Specify the architecture for which to generate assembly, overriding the target encoded in the input file. See the output of <code>llc -help</code> for a list of valid architectures. By default this is inferred from the target triple or autodetected to the current architecture.</p>
<dt><code>-mcpu</code>=<i>cpuname</i></p>
<dd> Specify a specific chip in the current architecture to generate code for. By default this is inferred from the target triple and autodetected to the current architecture. For a list of available CPUs, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mcpu=help</code></p>
<dt><code>-mattr</code>=<i>a1,+a2,-a3,&#8230;</i></p>
<dd> Override or control specific attributes of the target, such as whether <font SIZE="-1">SIMD</font> operations are enabled or not. The default set of attributes is set by the current <font SIZE="-1">CPU</font>. For a list of available attributes, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mattr=help</code></p>
<dt><code>&#8211;disable-fp-elim</code></p>
<dd> Disable frame pointer elimination optimization.</p>
<dt><code>&#8211;disable-excess-fp-precision</code></p>
<dd> Disable optimizations that may produce excess precision for floating point. Note that this option can dramatically slow down code on some systems (e.g. X86).</p>
<dt><code>&#8211;enable-unsafe-fp-math</code></p>
<dd> Enable optimizations that make unsafe assumptions about <font SIZE="-1">IEEE</font> math (e.g. that addition is associative) or may not work for all input ranges. These optimizations allow the code generator to make use of some instructions which would otherwise not be usable (such as fsin on X86).</p>
<dt><code>&#8211;enable-correct-eh-support</code></p>
<dd> Instruct the <code>lowerinvoke</code> pass to insert code for correct exception handling support. This is expensive and is by default omitted for efficiency.</p>
<dt><code>&#8211;stats</code></p>
<dd> Print statistics recorded by code-generation passes.</p>
<dt><code>&#8211;time-passes</code></p>
<dd> Record the amount of time needed for each pass and print a report to standard error.</p>
<dt><code>&#8211;load</code>=<i>dso_path</i></p>
<dd> Dynamically load <i>dso_path</i> (a path to a dynamically shared object) that implements an <font SIZE="-1">LLVM</font> target. This will permit the target name to be used with the <code>-march</code> option so that code can be generated for that target.</dl>
<h2>Tuning/Configuration Options</h2>
<dl>
<dt><code>&#8211;print-machineinstrs</code></p>
<dd> Print generated machine code between compilation phases (useful for debugging).</p>
<dt><code>&#8211;regalloc</code>=<i>allocator</i></p>
<dd> Specify the register allocator to use. The default <i>allocator</i> is <i>local</i>. Valid register allocators are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>simple</i></p>
<dd> Very simple &#8220;always spill&#8221; register allocator</p>
<dt><i>local</i></p>
<dd> Local register allocator</p>
<dt><i>linearscan</i></p>
<dd> Linear scan global register allocator</p>
<dt><i>iterativescan</i></p>
<dd> Iterative scan global register allocator</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;spiller</code>=<i>spiller</i></p>
<dd> Specify the spiller to use for register allocators that support it. Currently this option is used only by the linear scan register allocator. The default <i>spiller</i> is <i>local</i>. Valid spillers are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>simple</i></p>
<dd> Simple spiller</p>
<dt><i>local</i></p>
<dd> Local spiller</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Intel IA-32-specific Options</h2>
<dl>
<dt><code>&#8211;x86-asm-syntax=att|intel</code></p>
<dd> Specify whether to emit assembly code in <font SIZE="-1">AT&amp;T</font> syntax (the default) or intel syntax.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llc</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> lli</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
