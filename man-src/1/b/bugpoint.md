---
title: "bugpoint(1)"
name: "bugpoint"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bugpoint/"
description: "bugpoint – automatic test case reduction tool"
---

<h2 class="name">NAME</h2>
<p> bugpoint &#8211; automatic test case reduction tool </p>
<h2>SYNOPSIS</h2>
<p> <code>bugpoint</code> [<i>options</i>] [<i>input </i><font SIZE="-1"><i>LLVM</i></font><i> ll/bc files</i>] [<i></i><font SIZE="-1"><i>LLVM</i></font><i> passes</i>] <code>&#8211;args</code> <i>program arguments</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bugpoint</code> narrows down the source of problems in <font SIZE="-1">LLVM</font> tools and passes. It can be used to debug three types of failures: optimizer crashes, miscompilations by optimizers, or bad native code generation (including problems in the static and <font SIZE="-1">JIT</font> compilers). It aims to reduce large test cases to small, useful ones. For more information on the design and inner workings of <code>bugpoint</code>, as well as advice for using bugpoint, see <i>llvm/docs/Bugpoint.html</i> in the <font SIZE="-1">LLVM</font> distribution.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;additional-so</code> <i>library</i></p>
<dd> Load the dynamic shared object <i>library</i> into the test program whenever it is run. This is useful if you are debugging programs which depend on non-LLVM libraries (such as the X or curses libraries) to run.</p>
<dt><code>&#8211;append-exit-code</code>=<i>{true,false}</i></p>
<dd> Append the test programs exit code to the output file so that a change in exit code is considered a test failure. Defaults to false.</p>
<dt><code>&#8211;args</code> <i>program args</i></p>
<dd> Pass all arguments specified after -args to the test program whenever it runs. Note that if any of the <i>program args</i> start with a &#8216;-&#8216;, you should use: </p>
<pre><code>
bugpoint[bugpoint args]-- args-- [program args]
</code></pre>
<p> The &#8220;&#8211;&#8221; right after the <code>&#8211;args</code> option tells <code>bugpoint</code> to consider any options starting with <tt>&quot;-&quot;</tt> to be part of the <code>&#8211;args</code> option, not as options to <code>bugpoint</code> itself.</p>
<dt><code>&#8211;tool-args</code> <i>tool args</i></p>
<dd> Pass all arguments specified after &#8211;tool-args to the <font SIZE="-1">LLVM</font> tool under test (<code>llc</code>, <code>lli</code>, etc.) whenever it runs. You should use this option in the following way: </p>
<pre><code>
bugpoint[bugpoint args]-- tool - args-- [tool args]
</code></pre>
<p> The &#8220;&#8211;&#8221; right after the <code>&#8211;tool-args</code> option tells <code>bugpoint</code> to consider any options starting with <tt>&quot;-&quot;</tt> to be part of the <code>&#8211;tool-args</code> option, not as options to <code>bugpoint</code> itself. (See <code>&#8211;args</code>, above.)</p>
<dt><code>&#8211;safe-tool-args</code> <i>tool args</i></p>
<dd> Pass all arguments specified after <code>&#8211;safe-tool-args</code> to the &#8220;safe&#8221; execution tool.</p>
<dt><code>&#8211;gcc-tool-args</code> <i>gcc tool args</i></p>
<dd> Pass all arguments specified after <code>&#8211;gcc-tool-args</code> to the invocation of <code>gcc</code>.</p>
<dt><code>&#8211;disable-{dce,simplifycfg}</code></p>
<dd> Do not run the specified passes to clean up and reduce the size of the test program. By default, <code>bugpoint</code> uses these passes internally when attempting to reduce test programs. If you&#8217;re trying to find a bug in one of these passes, <code>bugpoint</code> may crash.</p>
<dt><code>&#8211;enable-valgrind</code></p>
<dd> Use valgrind to find faults in the optimization phase. This will allow bugpoint to find otherwise asymptomatic problems caused by memory mis-management.</p>
<dt><code>-find-bugs</code></p>
<dd> Continually randomize the specified passes and run them on the test program until a bug is found or the user kills <code>bugpoint</code>.</p>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>&#8211;input</code> <i>filename</i></p>
<dd> Open <i>filename</i> and redirect the standard input of the test program, whenever it runs, to come from that file.</p>
<dt><code>&#8211;load</code> <i>plugin</i></p>
<dd> Load the dynamic object <i>plugin</i> into <code>bugpoint</code> itself. This object should register new optimization passes. Once loaded, the object will add new command line options to enable various optimizations. To see the new complete list of optimizations, use the <code>-help</code> and <code>&#8211;load</code> options together; for example: </p>
<pre>
    bugpoint --load myNewPass.so -help
</pre>
<dt><code>&#8211;mlimit</code> <i>megabytes</i></p>
<dd> Specifies an upper limit on memory usage of the optimization and codegen. Set to zero to disable the limit.</p>
<dt><code>&#8211;output</code> <i>filename</i></p>
<dd> Whenever the test program produces output on its standard output stream, it should match the contents of <i>filename</i> (the &#8220;reference output&#8221;). If you do not use this option, <code>bugpoint</code> will attempt to generate a reference output by compiling the program with the &#8220;safe&#8221; backend and running it.</p>
<dt><code>&#8211;profile-info-file</code> <i>filename</i></p>
<dd> Profile file loaded by <code>&#8211;profile-loader</code>.</p>
<dt><code>&#8211;run-{int,jit,llc,cbe,custom}</code></p>
<dd> Whenever the test program is compiled, <code>bugpoint</code> should generate code for it using the specified code generator. These options allow you to choose the interpreter, the <font SIZE="-1">JIT</font> compiler, the static native code compiler, the C backend, or a custom command (see <code>&#8211;exec-command</code>) respectively.</p>
<dt><code>&#8211;safe-{llc,cbe,custom}</code></p>
<dd> When debugging a code generator, <code>bugpoint</code> should use the specified code generator as the &#8220;safe&#8221; code generator. This is a known-good code generator used to generate the &#8220;reference output&#8221; if it has not been provided, and to compile portions of the program that as they are excluded from the testcase. These options allow you to choose the static native code compiler, the C backend, or a custom command, (see <code>&#8211;exec-command</code>) respectively. The interpreter and the <font SIZE="-1">JIT</font> backends cannot currently be used as the &#8220;safe&#8221; backends.</p>
<dt><code>&#8211;exec-command</code> <i>command</i></p>
<dd> This option defines the command to use with the <code>&#8211;run-custom</code> and <code>&#8211;safe-custom</code> options to execute the bitcode testcase. This can be useful for cross-compilation.</p>
<dt><code>&#8211;safe-path</code> <i>path</i></p>
<dd> This option defines the path to the command to execute with the <code>&#8211;safe-{int,jit,llc,cbe,custom}</code> option.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>bugpoint</code> succeeds in finding a problem, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> opt</p>
<h2>AUTHOR</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
