---
title: "lli(1)"
name: "lli"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lli/"
description: "lli – directly execute programs from LLVM bitcode"
---

<h2 class="name">NAME</h2>
<p> lli &#8211; directly execute programs from LLVM bitcode </p>
<h2>SYNOPSIS</h2>
<p> <code>lli</code> [<i>options</i>] [<i>filename</i>] [<i>program args</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lli</code> directly executes programs in <font SIZE="-1">LLVM</font> bitcode format. It takes a program in <font SIZE="-1">LLVM</font> bitcode format and executes it using a just-in-time compiler, if one is available for the current architecture, or an interpreter. <code>lli</code> takes all of the same code generator options as llc, but they are only effective when <code>lli</code> is using the just-in-time compiler. </p>
<p> If <i>filename</i> is not specified, then <code>lli</code> reads the <font SIZE="-1">LLVM</font> bitcode for the program from standard input. </p>
<p> The optional <i>args</i> specified on the command line are passed to the program as arguments.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-fake-argv0</code>=<i>executable</i></p>
<dd> Override the <tt>&quot;argv[0]&quot;</tt> value passed into the executing program.</p>
<dt><code>-force-interpreter</code>=<i>{false,true}</i></p>
<dd> If set to true, use the interpreter even if a just-in-time compiler is available for this architecture. Defaults to false.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-load</code>=<i>puginfilename</i></p>
<dd> Causes <code>lli</code> to load the plugin (shared object) named <i>pluginfilename</i> and use it for optimization.</p>
<dt><code>-stats</code></p>
<dd> Print statistics from the code-generation passes. This is only meaningful for the just-in-time compiler, at present.</p>
<dt><code>-time-passes</code></p>
<dd> Record the amount of time needed for each code-generation pass and print it to standard error.</p>
<dt><code>-version</code></p>
<dd> Print out the version of <code>lli</code> and exit without doing anything else.</dl>
<h2>TARGET OPTIONS</h2>
<dl>
<dt><code>-mtriple</code>=<i>target triple</i></p>
<dd> Override the target triple specified in the input bitcode file with the specified string. This may result in a crash if you pick an architecture which is not compatible with the current system.</p>
<dt><code>-march</code>=<i>arch</i></p>
<dd> Specify the architecture for which to generate assembly, overriding the target encoded in the bitcode file. See the output of <code>llc -help</code> for a list of valid architectures. By default this is inferred from the target triple or autodetected to the current architecture.</p>
<dt><code>-mcpu</code>=<i>cpuname</i></p>
<dd> Specify a specific chip in the current architecture to generate code for. By default this is inferred from the target triple and autodetected to the current architecture. For a list of available CPUs, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mcpu=help</code></p>
<dt><code>-mattr</code>=<i>a1,+a2,-a3,&#8230;</i></p>
<dd> Override or control specific attributes of the target, such as whether <font SIZE="-1">SIMD</font> operations are enabled or not. The default set of attributes is set by the current <font SIZE="-1">CPU</font>. For a list of available attributes, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mattr=help</code></dl>
<h2>FLOATING POINT OPTIONS</h2>
<dl>
<dt><code>-disable-excess-fp-precision</code></p>
<dd> Disable optimizations that may increase floating point precision.</p>
<dt><code>-enable-finite-only-fp-math</code></p>
<dd> Enable optimizations that assumes only finite floating point math. That is, there is no <font SIZE="-1">NAN</font> or Inf values.</p>
<dt><code>-enable-unsafe-fp-math</code></p>
<dd> Causes <code>lli</code> to enable optimizations that may decrease floating point precision.</p>
<dt><code>-soft-float</code></p>
<dd> Causes <code>lli</code> to generate software floating point library calls instead of equivalent hardware instructions.</dl>
<h2>CODE GENERATION OPTIONS</h2>
<dl>
<dt><code>-code-model</code>=<i>model</i></p>
<dd> Choose the code model from: </p>
<pre>
    default: Target default code model
    small: Small code model
    kernel: Kernel code model
    medium: Medium code model
    large: Large code model
</pre>
<dt><code>-disable-post-RA-scheduler</code></p>
<dd> Disable scheduling after register allocation.</p>
<dt><code>-disable-spill-fusing</code></p>
<dd> Disable fusing of spill code into instructions.</p>
<dt><code>-enable-correct-eh-support</code></p>
<dd> Make the -lowerinvoke pass insert expensive, but correct, <font SIZE="-1">EH</font> code.</p>
<dt><code>-enable-eh</code></p>
<dd> Exception handling should be emitted.</p>
<dt><code>-join-liveintervals</code></p>
<dd> Coalesce copies (default=true).</p>
<dt><code>-nozero-initialized-in-bss</code> Don&#8217;t place zero-initialized symbols into the <font SIZE="-1">BSS</font> section.</p>
<dd>
<dt><code>-pre-RA-sched</code>=<i>scheduler</i></p>
<dd> Instruction schedulers available (before register allocation): </p>
<pre>
    =default: Best scheduler for the target 
    =none: No scheduling: breadth first sequencing 
    =simple: Simple two pass scheduling: minimize critical path and maximize processor utilization 
    =simple-noitin: Simple two pass scheduling: Same as simple except using generic latency 
    =list-burr: Bottom-up register reduction list scheduling 
    =list-tdrr: Top-down register reduction list scheduling 
    =list-td: Top-down list scheduler -print-machineinstrs - Print generated machine code
</pre>
<dt><code>-regalloc</code>=<i>allocator</i></p>
<dd> Register allocator to use (default=linearscan) </p>
<pre>
    =bigblock: Big-block register allocator 
    =linearscan: linear scan register allocator =local -   local register allocator 
    =simple: simple register allocator
</pre>
<dt><code>-relocation-model</code>=<i>model</i></p>
<dd> Choose relocation model from: </p>
<pre>
    =default: Target default relocation model 
    =static: Non-relocatable code =pic -   Fully relocatable, position independent code 
    =dynamic-no-pic: Relocatable external references, non-relocatable code
</pre>
<dt><code>-spiller</code></p>
<dd> Spiller to use (default=local) </p>
<pre>
    =simple: simple spiller 
    =local: local spiller
</pre>
<dt><code>-x86-asm-syntax</code>=<i>syntax</i></p>
<dd> Choose style of code to emit from X86 backend: </p>
<pre>
    =att: Emit AT&amp;T-style assembly 
    =intel: Emit Intel-style assembly
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> If <code>lli</code> fails to load the program, it will exit with an exit code of 1. Otherwise, it will return the exit code of the program it executes.</p>
<h2>SEE ALSO</h2>
<p> llc</p>
<h2>AUTHOR</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
