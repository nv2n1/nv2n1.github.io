---
title: "rustc(1)"
name: "rustc"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rustc/"
description: "rustc – The Rust compiler"
---

<h2>NAME</h2>
<p> rustc &#8211; The Rust compiler</p>
<h2>SYNOPSIS</h2>
<p> <code>rustc</code> [<i>OPTIONS</i>] <i>INPUT</i> </p>
<h2>DESCRIPTION</h2>
<p> This program is a compiler for the Rust language, available at <a rel="nofollow" href="https://www.rust-lang.org.">https://www.rust-lang.org.</a> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display the help message.</p>
<dt><code>&#8211;cfg</code> <i>SPEC</i></p>
<dd> Configure the compilation environment.</p>
<dt><code>-L</code> [<i>KIND</i>=]<i>PATH</i></p>
<dd> Add a directory to the library search path. The optional <i>KIND</i> can be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>dependency</code></p>
<dd> only lookup transitive dependencies here</p>
<dt><code>crate</code></p>
<dd> only lookup local `extern crate` directives here</p>
<dt><code>native</code></p>
<dd> only lookup native libraries here</p>
<dt><code>framework</code></p>
<dd> only look for OSX frameworks here</p>
<dt><code>all</code></p>
<dd> look for anything here (the default)</dl>
</dl>
<dt><code>-l</code> [<i>KIND</i>=]<i>NAME</i></p>
<dd> Link the generated crate(s) to the specified library <i>NAME</i>. The optional <i>KIND</i> can be one of <i>static</i>, <i>dylib</i>, or <i>framework</i>. If omitted, <i>dylib</i> is assumed.</p>
<dt><code>&#8211;crate-type</code> [bin|lib|rlib|dylib|cdylib|staticlib]</p>
<dd> Comma separated list of types of crates for the compiler to emit.</p>
<dt><code>&#8211;crate-name</code> <i>NAME</i></p>
<dd> Specify the name of the crate being built.</p>
<dt><code>&#8211;emit</code> [asm|llvm-bc|llvm-ir|obj|link|dep-info|mir][=<i>PATH</i>]</p>
<dd> Configure the output that <code>rustc</code> will produce. Each emission may also have an optional explicit output <i>PATH</i> specified for that particular emission kind. This path takes precedence over the <code>-o</code> option.</p>
<dt><code>&#8211;print</code> [crate-name|file-names|sysroot]</p>
<dd> Comma separated list of compiler information to print on stdout.</p>
<dt><code>-g</code></p>
<dd> Equivalent to <i>-C debuginfo=2</i>.</p>
<dt><code>-O</code></p>
<dd> Equivalent to <i>-C opt-level=2</i>.</p>
<dt><code>-o</code> <i>FILENAME</i></p>
<dd> Write output to <i>FILENAME</i>. Ignored if multiple <i>&#8211;emit</i> outputs are specified which don&#8217;t have an explicit path otherwise.</p>
<dt><code>&#8211;out-dir</code> <i>DIR</i></p>
<dd> Write output to compiler-chosen filename in <i>DIR</i>. Ignored if <i>-o</i> is specified. Defaults to the current directory.</p>
<dt><code>&#8211;explain</code> <i>OPT</i></p>
<dd> Provide a detailed explanation of an error message.</p>
<dt><code>&#8211;test</code></p>
<dd> Build a test harness.</p>
<dt><code>&#8211;target</code> <i>TARGET</i></p>
<dd> Target triple for which the code is compiled. This option defaults to the host’s target triple. The target triple has the general format &lt;arch&gt;&lt;sub&gt;-&lt;vendor&gt;-&lt;sys&gt;-&lt;abi&gt;, where:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&lt;arch&gt;</code></p>
<dd> x86, arm, thumb, mips, etc.</p>
<dt><code>&lt;sub&gt;</code></p>
<dd> for example on ARM: v5, v6m, v7a, v7m, etc.</p>
<dt><code>&lt;vendor&gt;</code></p>
<dd> pc, apple, nvidia, ibm, etc.</p>
<dt><code>&lt;sys&gt;</code></p>
<dd> none, linux, win32, darwin, cuda, etc.</p>
<dt><code>&lt;abi&gt;</code></p>
<dd> eabi, gnu, android, macho, elf, etc.</dl>
</dl>
<dt><code>-W help</code></p>
<dd> Print &#8216;lint&#8217; options and default settings.</p>
<dt><code>-W</code> <i>OPT</i>, <code>&#8211;warn</code> <i>OPT</i></p>
<dd> Set lint warnings.</p>
<dt><code>-A</code> <i>OPT</i>, <code>&#8211;allow</code> <i>OPT</i></p>
<dd> Set lint allowed.</p>
<dt><code>-D</code> <i>OPT</i>, <code>&#8211;deny</code> <i>OPT</i></p>
<dd> Set lint denied.</p>
<dt><code>-F</code> <i>OPT</i>, <code>&#8211;forbid</code> <i>OPT</i></p>
<dd> Set lint forbidden.</p>
<dt><code>-C</code> <i>FLAG</i>[=<i>VAL</i>], <code>&#8211;codegen</code> <i>FLAG</i>[=<i>VAL</i>]</p>
<dd> Set a codegen-related flag to the value specified. Use <i>-C help</i> to print available flags. See CODEGEN OPTIONS below.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version info and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Use verbose output.</p>
<dt><code>&#8211;extern</code> <i>NAME</i>=<i>PATH</i></p>
<dd> Specify where an external rust library is located. These should match <i>extern</i> declarations in the crate&#8217;s source code.</p>
<dt><code>&#8211;sysroot</code> <i>PATH</i></p>
<dd> Override the system root.</p>
<dt><code>-Z</code> <i>FLAG</i></p>
<dd> Set internal debugging options. Use <i>-Z help</i> to print available options.</p>
<dt><code>&#8211;color</code> auto|always|never</p>
<dd> Configure coloring of output:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>auto</code></p>
<dd> colorize, if output goes to a tty (default);</p>
<dt><code>always</code></p>
<dd> always colorize output;</p>
<dt><code>never</code></p>
<dd> never colorize output.</dl>
</dl>
</dl>
<h2>CODEGEN OPTIONS</h2>
<dl>
<dt><code>ar</code>=<i>/path/to/ar</i></p>
<dd> Path to the archive utility to use when assembling archives.</p>
<dt><code>linker</code>=<i>/path/to/cc</i></p>
<dd> Path to the linker utility to use when linking libraries, executables, and objects.</p>
<dt><code>link-args</code>=&#8217;<i>-flag1 -flag2</i>&#8216;</p>
<dd> A space-separated list of extra arguments to pass to the linker when the linker is invoked.</p>
<dt><code>lto</code></p>
<dd> Perform LLVM link-time optimizations.</p>
<dt><code>target-cpu</code>=<i>help</i></p>
<dd> Selects a target processor. If the value is &#8216;help&#8217;, then a list of available CPUs is printed.</p>
<dt><code>target-feature</code>=&#8217;<i>+feature1</i>,<i>-feature2</i>&#8216;</p>
<dd> A comma-separated list of features to enable or disable for the target. A preceding &#8216;+&#8217; enables a feature while a preceding &#8216;-&#8216; disables it. Available features can be discovered through <i>llc -mcpu=help</i>.</p>
<dt><code>passes</code>=<i>val</i></p>
<dd> A space-separated list of extra LLVM passes to run. A value of &#8216;list&#8217; will cause <code>rustc</code> to print all known passes and exit. The passes specified are appended at the end of the normal pass manager.</p>
<dt><code>llvm-args</code>=&#8217;<i>-arg1</i> <i>-arg2</i>&#8216;</p>
<dd> A space-separated list of arguments to pass through to LLVM.</p>
<dt><code>save-temps</code></p>
<dd> If specified, the compiler will save more files (.bc, .o, .no-opt.bc) generated throughout compilation in the output directory.</p>
<dt><code>rpath</code></p>
<dd> If specified, then the rpath value for dynamic libraries will be set in either dynamic library or executable outputs.</p>
<dt><code>no-prepopulate-passes</code></p>
<dd> Suppresses pre-population of the LLVM pass manager that is run over the module.</p>
<dt><code>no-vectorize-loops</code></p>
<dd> Suppresses running the loop vectorization LLVM pass, regardless of optimization level.</p>
<dt><code>no-vectorize-slp</code></p>
<dd> Suppresses running the LLVM SLP vectorization pass, regardless of optimization level.</p>
<dt><code>soft-float</code></p>
<dd> Generates software floating point library calls instead of hardware instructions.</p>
<dt><code>prefer-dynamic</code></p>
<dd> Prefers dynamic linking to static linking.</p>
<dt><code>no-integrated-as</code></p>
<dd> Force usage of an external assembler rather than LLVM&#8217;s integrated one.</p>
<dt><code>no-redzone</code></p>
<dd> Disable the use of the redzone.</p>
<dt><code>relocation-model</code>=[pic,static,dynamic-no-pic]</p>
<dd> The relocation model to use. (Default: <i>pic</i>)</p>
<dt><code>code-model</code>=[small,kernel,medium,large]</p>
<dd> Choose the code model to use.</p>
<dt><code>metadata</code>=<i>val</i></p>
<dd> Metadata to mangle symbol names with.</p>
<dt><code>extra-filename</code>=<i>val</i></p>
<dd> Extra data to put in each output filename.</p>
<dt><code>codegen-units</code>=<i>n</i></p>
<dd> Divide crate into <i>n</i> units to optimize in parallel.</p>
<dt><code>remark</code>=<i>val</i></p>
<dd> Print remarks for these optimization passes (space separated, or &quot;all&quot;).</p>
<dt><code>no-stack-check</code></p>
<dd> Disable checks for stack exhaustion (a memory-safety hazard!).</p>
<dt><code>debuginfo</code>=<i>val</i></p>
<dd> Debug info emission level:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> no debug info;</p>
<dt><code>1</code></p>
<dd> line-tables only (for stacktraces and breakpoints);</p>
<dt><code>2</code></p>
<dd> full debug info with variable and type information.</dl>
</dl>
<dt><code>opt-level</code>=<i>VAL</i></p>
<dd> Optimize with possible levels 0-3 </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> Some of these affect the output of the compiler, while others affect programs which link to the standard library. </p>
<dl>
<dt><code>RUST_TEST_THREADS</code></p>
<dd> The test framework Rust provides executes tests in parallel. This variable sets the maximum number of threads used for this purpose. This setting is overridden by the &#8211;test-threads option. </p>
<dt><code>RUST_TEST_NOCAPTURE</code></p>
<dd> If set to a value other than &quot;0&quot;, a synonym for the &#8211;nocapture flag. </p>
<dt><code>RUST_MIN_STACK</code></p>
<dd> Sets the minimum stack size for new threads. </p>
<dt><code>RUST_BACKTRACE</code></p>
<dd> If set to a value different than &quot;0&quot;, produces a backtrace in the output of a program which panics. </p>
</dl>
<h2>EXAMPLES</h2>
<p> To build an executable from a source file with a main function:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustc -o hello hello.rs </p>
<p> To build a library from a source file:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustc &#8211;crate-type=lib hello-lib.rs </p>
<p> To build either with a crate (.rs) file:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustc hello.rs </p>
<p> To build an executable with debug info:<br />
&nbsp;<wbr>$&nbsp;<wbr>rustc -g -o hello hello.rs </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rustdoc/">rustdoc</a></code>(1) </p>
<h2>BUGS</h2>
<p> See <a rel="nofollow" href="https://github.com/rust-lang/rust/issues">https://github.com/rust-lang/rust/issues</a> for issues. </p>
<h2>AUTHOR</h2>
<p> See <a rel="nofollow" href="https://github.com/rust-lang/rust/graphs/contributors">https://github.com/rust-lang/rust/graphs/contributors</a> or use `git log &#8211;all &#8211;format=&#8217;%cN &lt;%cE&gt;&#8217; | sort -u` in the rust source distribution. </p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See <i>COPYRIGHT</i> file in the rust source distribution. </p>
<h2>Index</h2>
