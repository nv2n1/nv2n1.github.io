---
title: "llc-14(1)"
name: "llc-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llc-14/"
description: "llc – LLVM static compiler"
---

<h2 class="name">NAME</h2>
<p> llc &#8211; LLVM static compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>llc</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llc</code> command compiles LLVM source inputs into assembly language for a specified architecture. The assembly language output can then be passed through a native assembler and linker to generate a native executable. </p>
<p> The choice of architecture for the output assembly code is automatically determined from the input file, unless the <i>-march</i> option is used to override the default.</p>
<h2>OPTIONS</h2>
<p> If <code>filename</code> is “<code>&#8211;</code>” or omitted, <code>llc</code> reads from standard input. Otherwise, it will from <code>filename</code>. Inputs can be in either the LLVM assembly language format (<code>.ll</code>) or the LLVM bitcode format (<code>.bc</code>). </p>
<p> If the <i>-o</i> option is omitted, then <code>llc</code> will send its output to standard output if the input is from standard input. If the <i>-o</i> option specifies “<code>&#8211;</code>”, then the output will also be sent to standard output. </p>
<p> If no <i>-o</i> option is specified and an input file other than “<code>&#8211;</code>” is specified, then <code>llc</code> creates the output filename by taking the input filename, removing any existing <code>.bc</code> extension, and adding a <code>.s</code> suffix. </p>
<p> Other <code>llc</code> options are described below.</p>
<h3>End-user Options</h3>
<dl>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-o &lt;filename&gt;</code></p>
<dd> Use <code>&lt;filename&gt;</code> as the output filename. See the summary above for more details.</p>
<dt><code>-O=uint</code></p>
<dd> Generate code at different optimization levels. These correspond to the <code>-O0</code>, <code>-O1</code>, <code>-O2</code>, and <code>-O3</code> optimization levels used by <code>clang</code>.</p>
<dt><code>-mtriple=&lt;target triple&gt;</code></p>
<dd> Override the target triple specified in the input file with the specified string.</p>
<dt><code>-march=&lt;arch&gt;</code></p>
<dd> Specify the architecture for which to generate assembly, overriding the target encoded in the input file. See the output of <code>llc -help</code> for a list of valid architectures. By default this is inferred from the target triple or autodetected to the current architecture.</p>
<dt><code>-mcpu=&lt;cpuname&gt;</code></p>
<dd> Specify a specific chip in the current architecture to generate code for. By default this is inferred from the target triple and autodetected to the current architecture. For a list of available CPUs, use: </p>
<pre>
llvm-as &lt; /dev/null | llc -march=xyz -mcpu=help
</pre>
<dt><code>-filetype=&lt;output file type&gt;</code></p>
<dd> Specify what kind of output <code>llc</code> should generated. Options are: <code>asm</code> for textual assembly ( <code>&#8216;.s&#8217;</code>), <code>obj</code> for native object files (<code>&#8216;.o&#8217;</code>) and <code>null</code> for not emitting anything (for performance testing). </p>
<p> Note that not all targets support all options.</p>
<dt><code>-mattr=a1,+a2,-a3,&#8230;</code></p>
<dd> Override or control specific attributes of the target, such as whether SIMD operations are enabled or not. The default set of attributes is set by the current CPU. For a list of available attributes, use: </p>
<pre>
llvm-as &lt; /dev/null | llc -march=xyz -mattr=help
</pre>
<dt><code>&#8211;frame-pointer</code></p>
<dd> Specify effect of frame pointer elimination optimization (all,non-leaf,none).</p>
<dt><code>&#8211;disable-excess-fp-precision</code></p>
<dd> Disable optimizations that may produce excess precision for floating point. Note that this option can dramatically slow down code on some systems (e.g. X86).</p>
<dt><code>&#8211;enable-no-infs-fp-math</code></p>
<dd> Enable optimizations that assume no Inf values.</p>
<dt><code>&#8211;enable-no-nans-fp-math</code></p>
<dd> Enable optimizations that assume no NAN values.</p>
<dt><code>&#8211;enable-no-signed-zeros-fp-math</code></p>
<dd> Enable FP math optimizations that assume the sign of 0 is insignificant.</p>
<dt><code>&#8211;enable-no-trapping-fp-math</code></p>
<dd> Enable setting the FP exceptions build attribute not to use exceptions.</p>
<dt><code>&#8211;enable-unsafe-fp-math</code></p>
<dd> Enable optimizations that make unsafe assumptions about IEEE math (e.g. that addition is associative) or may not work for all input ranges. These optimizations allow the code generator to make use of some instructions which would otherwise not be usable (such as <code>fsin</code> on X86).</p>
<dt><code>&#8211;stats</code></p>
<dd> Print statistics recorded by code-generation passes.</p>
<dt><code>&#8211;time-passes</code></p>
<dd> Record the amount of time needed for each pass and print a report to standard error.</p>
<dt><code>&#8211;load=&lt;dso_path&gt;</code></p>
<dd> Dynamically load <code>dso_path</code> (a path to a dynamically shared object) that implements an LLVM target. This will permit the target name to be used with the <i>-march</i> option so that code can be generated for that target.</p>
<dt><code>-meabi=[default|gnu|4|5]</code></p>
<dd> Specify which EABI version should conform to. Valid EABI versions are <i>gnu</i>, <i>4</i> and <i>5</i>. Default value (<i>default</i>) depends on the triple.</p>
<dt><code>-stack-size-section</code></p>
<dd> Emit the .stack_sizes section which contains stack size metadata. The section contains an array of pairs of function symbol values (pointer size) and stack sizes (unsigned LEB128). The stack size values only include the space allocated in the function prologue. Functions with dynamic stack allocations are not included.</p>
<dt><code>-remarks-section</code></p>
<dd> Emit the __remarks (MachO) section which contains metadata about remark diagnostics.</dl>
<h3>Tuning/Configuration Options</h3>
<dl>
<dt><code>&#8211;print-after-isel</code></p>
<dd> Print generated machine code after instruction selection (useful for debugging).</p>
<dt><code>&#8211;regalloc=&lt;allocator&gt;</code></p>
<dd> Specify the register allocator to use. Valid register allocators are: </p>
<p> <i>basic</i> Basic register allocator. </p>
<p> <i>fast</i> Fast register allocator. It is the default for unoptimized code. </p>
<p> <i>greedy</i> Greedy register allocator. It is the default for optimized code. </p>
<p> <i>pbqp</i> Register allocator based on ‘Partitioned Boolean Quadratic Programming’.</p>
<dt><code>&#8211;spiller=&lt;spiller&gt;</code></p>
<dd> Specify the spiller to use for register allocators that support it. Currently this option is used only by the linear scan register allocator. The default <code>spiller</code> is <i>local</i>. Valid spillers are: </p>
<p> <i>simple</i> Simple spiller </p>
<p> <i>local</i> Local spiller</dl>
<h3>Intel IA-32-specific Options</h3>
<dl>
<dt><code>&#8211;x86-asm-syntax=[att|intel]</code></p>
<dd> Specify whether to emit assembly code in AT&amp;T syntax (the default) or Intel syntax.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llc</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lli/">lli</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
