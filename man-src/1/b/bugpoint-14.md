---
title: "bugpoint-14(1)"
name: "bugpoint-14"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bugpoint-14/"
description: "bugpoint – automatic test case reduction tool"
---

<h2 class="name">NAME</h2>
<p> bugpoint &#8211; automatic test case reduction tool </p>
<h2>SYNOPSIS</h2>
<p> <code>bugpoint</code> [<i>options</i>] [<i>input LLVM ll/bc files</i>] [<i>LLVM passes</i>] <code>–args</code> <i>program arguments</i></p>
<h2>DESCRIPTION</h2>
<p> <code>bugpoint</code> narrows down the source of problems in LLVM tools and passes. It can be used to debug three types of failures: optimizer crashes, miscompilations by optimizers, or bad native code generation (including problems in the static and JIT compilers). It aims to reduce large test cases to small, useful ones. For more information on the design and inner workings of <code>bugpoint</code>, as well as advice for using bugpoint, see /Bugpoint in the LLVM distribution.</p>
<h2>OPTIONS</h2>
<p> <code>–additional-so</code> <i>library</i> Load the dynamic shared object <i>library</i> into the test program whenever it is run. This is useful if you are debugging programs which depend on non-LLVM libraries (such as the X or curses libraries) to run. </p>
<p> <code>–append-exit-code</code>=<i>{true,false}</i> Append the test programs exit code to the output file so that a change in exit code is considered a test failure. Defaults to false. </p>
<p> <code>–args</code> <i>program args</i> Pass all arguments specified after <code>–args</code> to the test program whenever it runs. Note that if any of the <i>program args</i> start with a “<code>&#8211;</code>”, you should use: </p>
<pre><code>
bugpoint[bugpoint args]-- args-- [program args]
</code></pre>
<p> The “<code>&#8212;</code>” right after the <code>–args</code> option tells <code>bugpoint</code> to consider any options starting with “<code>&#8211;</code>” to be part of the <code>–args</code> option, not as options to <code>bugpoint</code> itself. </p>
<p> <code>–tool-args</code> <i>tool args</i> Pass all arguments specified after <code>–tool-args</code> to the LLVM tool under test (<code>llc</code>, <code>lli</code>, etc.) whenever it runs. You should use this option in the following way: </p>
<pre><code>
bugpoint[bugpoint args]-- tool - args-- [tool args]
</code></pre>
<p> The “<code>&#8212;</code>” right after the <code>–tool-args</code> option tells <code>bugpoint</code> to consider any options starting with “<code>&#8211;</code>” to be part of the <code>–tool-args</code> option, not as options to <code>bugpoint</code> itself. (See <code>–args</code>, above.) </p>
<p> <code>–safe-tool-args</code> <i>tool args</i> Pass all arguments specified after <code>–safe-tool-args</code> to the “safe” execution tool. </p>
<p> <code>–gcc-tool-args</code> <i>gcc tool args</i> Pass all arguments specified after <code>–gcc-tool-args</code> to the invocation of <code>gcc</code>. </p>
<p> <code>–opt-args</code> <i>opt args</i> Pass all arguments specified after <code>–opt-args</code> to the invocation of <code>opt</code>. </p>
<p> <code>–disable-{dce,simplifycfg}</code> Do not run the specified passes to clean up and reduce the size of the test program. By default, <code>bugpoint</code> uses these passes internally when attempting to reduce test programs. If you’re trying to find a bug in one of these passes, <code>bugpoint</code> may crash. </p>
<p> <code>–enable-valgrind</code> Use valgrind to find faults in the optimization phase. This will allow bugpoint to find otherwise asymptomatic problems caused by memory mis-management. </p>
<p> <code>-find-bugs</code> Continually randomize the specified passes and run them on the test program until a bug is found or the user kills <code>bugpoint</code>. </p>
<p> <code>-help</code> Print a summary of command line options. </p>
<p> <code>–input</code> <i>filename</i> Open <i>filename</i> and redirect the standard input of the test program, whenever it runs, to come from that file. </p>
<p> <code>–load</code> <i>plugin</i> Load the dynamic object <i>plugin</i> into <code>bugpoint</code> itself. This object should register new optimization passes. Once loaded, the object will add new command line options to enable various optimizations. To see the new complete list of optimizations, use the <code>-help</code> and <code>–load</code> options together; for example: </p>
<pre>
bugpoint --load myNewPass.so -help
</pre>
<p> <code>–mlimit</code> <i>megabytes</i> Specifies an upper limit on memory usage of the optimization and codegen. Set to zero to disable the limit. </p>
<p> <code>–output</code> <i>filename</i> Whenever the test program produces output on its standard output stream, it should match the contents of <i>filename</i> (the “reference output”). If you do not use this option, <code>bugpoint</code> will attempt to generate a reference output by compiling the program with the “safe” backend and running it. </p>
<p> <code>–run-{int,jit,llc,custom}</code> Whenever the test program is compiled, <code>bugpoint</code> should generate code for it using the specified code generator. These options allow you to choose the interpreter, the JIT compiler, the static native code compiler, or a custom command (see <code>–exec-command</code>) respectively. </p>
<p> <code>–safe-{llc,custom}</code> When debugging a code generator, <code>bugpoint</code> should use the specified code generator as the “safe” code generator. This is a known-good code generator used to generate the “reference output” if it has not been provided, and to compile portions of the program that as they are excluded from the testcase. These options allow you to choose the static native code compiler, or a custom command, (see <code>–exec-command</code>) respectively. The interpreter and the JIT backends cannot currently be used as the “safe” backends. </p>
<p> <code>–exec-command</code> <i>command</i> This option defines the command to use with the <code>–run-custom</code> and <code>–safe-custom</code> options to execute the bitcode testcase. This can be useful for cross-compilation. </p>
<p> <code>–compile-command</code> <i>command</i> This option defines the command to use with the <code>–compile-custom</code> option to compile the bitcode testcase. The command should exit with a failure exit code if the file is “interesting” and should exit with a success exit code (i.e. 0) otherwise (this is the same as if it crashed on “interesting” inputs). </p>
<p> This can be useful for testing compiler output without running any link or execute stages. To generate a reduced unit test, you may add CHECK directives to the testcase and pass the name of an executable compile-command script in this form: </p>
<pre>
#!/bin/sh
llc &quot;$@&quot;
not FileCheck [bugpoint input file].ll &lt; bugpoint-test-program.s
</pre>
<p> This script will “fail” as long as FileCheck passes. So the result will be the minimum bitcode that passes FileCheck. </p>
<p> <code>–safe-path</code> <i>path</i> This option defines the path to the command to execute with the <code>–safe-{int,jit,llc,custom}</code> option. </p>
<p> <code>–verbose-errors</code>=<i>{true,false}</i> The default behavior of bugpoint is to print “&lt;crash&gt;” when it finds a reduced test that crashes compilation. This flag prints the output of the crashing program to stderr. This is useful to make sure it is the same error being tracked down and not a different error that happens to crash the compiler as well. Defaults to false.</p>
<h2>EXIT STATUS</h2>
<p> If <code>bugpoint</code> succeeds in finding a problem, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-opt/">opt</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
