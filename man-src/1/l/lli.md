---

title: "lli(1)"
name: "lli"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lli/"
description: "lli – directly execute programs from LLVM bitcode"
---

<p> <code>lli</code> [<i>options</i>] [<i>filename</i>] [<i>program args</i>]</p>
<p> <code>lli</code> directly executes programs in <font SIZE="-1">LLVM</font> bitcode format. It takes a program in <font SIZE="-1">LLVM</font> bitcode format and executes it using a just-in-time compiler, if one is available for the current architecture, or an interpreter. <code>lli</code> takes all of the same code generator options as llc, but they are only effective when <code>lli</code> is using the just-in-time compiler. </p>
<p> If <i>filename</i> is not specified, then <code>lli</code> reads the <font SIZE="-1">LLVM</font> bitcode for the program from standard input. </p>
<p> The optional <i>args</i> specified on the command line are passed to the program as arguments.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-fake-argv0</code>=<i>executable</i></dt>
<dd> Override the <tt>&quot;argv[0]&quot;</tt> value passed into the executing program.</dd>
<dt><code>-force-interpreter</code>=<i>{false,true}</i></dt>
<dd> If set to true, use the interpreter even if a just-in-time compiler is available for this architecture. Defaults to false.</dd>
<dt><code>-help</code></dt>
<dd> Print a summary of command line options.</dd>
<dt><code>-load</code>=<i>puginfilename</i></dt>
<dd> Causes <code>lli</code> to load the plugin (shared object) named <i>pluginfilename</i> and use it for optimization.</dd>
<dt><code>-stats</code></dt>
<dd> Print statistics from the code-generation passes. This is only meaningful for the just-in-time compiler, at present.</dd>
<dt><code>-time-passes</code></dt>
<dd> Record the amount of time needed for each code-generation pass and print it to standard error.</dd>
<dt><code>-version</code></dt>
<dd> Print out the version of <code>lli</code> and exit without doing anything else.</dd></dl>
<h2>TARGET OPTIONS</h2>
<dl>
<dt><code>-mtriple</code>=<i>target triple</i></dt>
<dd> Override the target triple specified in the input bitcode file with the specified string. This may result in a crash if you pick an architecture which is not compatible with the current system.</dd>
<dt><code>-march</code>=<i>arch</i></dt>
<dd> Specify the architecture for which to generate assembly, overriding the target encoded in the bitcode file. See the output of <code>llc -help</code> for a list of valid architectures. By default this is inferred from the target triple or autodetected to the current architecture.</dd>
<dt><code>-mcpu</code>=<i>cpuname</i></dt>
<dd> Specify a specific chip in the current architecture to generate code for. By default this is inferred from the target triple and autodetected to the current architecture. For a list of available CPUs, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mcpu=help</code></dd>
<dt><code>-mattr</code>=<i>a1,+a2,-a3,&#8230;</i></dt>
<dd> Override or control specific attributes of the target, such as whether <font SIZE="-1">SIMD</font> operations are enabled or not. The default set of attributes is set by the current <font SIZE="-1">CPU</font>. For a list of available attributes, use: <code>llvm-as &lt; /dev/null | llc -march=xyz -mattr=help</code></dd></dl>
<h2>FLOATING POINT OPTIONS</h2>
<dl>
<dt><code>-disable-excess-fp-precision</code></dt>
<dd> Disable optimizations that may increase floating point precision.</dd>
<dt><code>-enable-finite-only-fp-math</code></dt>
<dd> Enable optimizations that assumes only finite floating point math. That is, there is no <font SIZE="-1">NAN</font> or Inf values.</dd>
<dt><code>-enable-unsafe-fp-math</code></dt>
<dd> Causes <code>lli</code> to enable optimizations that may decrease floating point precision.</dd>
<dt><code>-soft-float</code></dt>
<dd> Causes <code>lli</code> to generate software floating point library calls instead of equivalent hardware instructions.</dd></dl>
<h2>CODE GENERATION OPTIONS</h2>
<dl>
<dt><code>-code-model</code>=<i>model</i></dt>
<dd> Choose the code model from: </dd>
<pre>
    default: Target default code model
    small: Small code model
    kernel: Kernel code model
    medium: Medium code model
    large: Large code model
</pre>
<dt><code>-disable-post-RA-scheduler</code></dt>
<dd> Disable scheduling after register allocation.</dd>
<dt><code>-disable-spill-fusing</code></dt>
<dd> Disable fusing of spill code into instructions.</dd>
<dt><code>-enable-correct-eh-support</code></dt>
<dd> Make the -lowerinvoke pass insert expensive, but correct, <font SIZE="-1">EH</font> code.</dd>
<dt><code>-enable-eh</code></dt>
<dd> Exception handling should be emitted.</dd>
<dt><code>-join-liveintervals</code></dt>
<dd> Coalesce copies (default=true).</dd>
<dt><code>-nozero-initialized-in-bss</code> Don&#8217;t place zero-initialized symbols into the <font SIZE="-1">BSS</font> section.</dt>
<dd>
</dd><dt><code>-pre-RA-sched</code>=<i>scheduler</i></dt>
<dd> Instruction schedulers available (before register allocation): </dd>
<pre>
    =default: Best scheduler for the target 
    =none: No scheduling: breadth first sequencing 
    =simple: Simple two pass scheduling: minimize critical path and maximize processor utilization 
    =simple-noitin: Simple two pass scheduling: Same as simple except using generic latency 
    =list-burr: Bottom-up register reduction list scheduling 
    =list-tdrr: Top-down register reduction list scheduling 
    =list-td: Top-down list scheduler -print-machineinstrs - Print generated machine code
</pre>
<dt><code>-regalloc</code>=<i>allocator</i></dt>
<dd> Register allocator to use (default=linearscan) </dd>
<pre>
    =bigblock: Big-block register allocator 
    =linearscan: linear scan register allocator =local -   local register allocator 
    =simple: simple register allocator
</pre>
<dt><code>-relocation-model</code>=<i>model</i></dt>
<dd> Choose relocation model from: </dd>
<pre>
    =default: Target default relocation model 
    =static: Non-relocatable code =pic -   Fully relocatable, position independent code 
    =dynamic-no-pic: Relocatable external references, non-relocatable code
</pre>
<dt><code>-spiller</code></dt>
<dd> Spiller to use (default=local) </dd>
<pre>
    =simple: simple spiller 
    =local: local spiller
</pre>
<dt><code>-x86-asm-syntax</code>=<i>syntax</i></dt>
<dd> Choose style of code to emit from X86 backend: </dd>
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
