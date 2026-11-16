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
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display the help message.</dd>
<dt><code>&#8211;cfg</code> <i>SPEC</i></dt>
<dd> Configure the compilation environment.</dd>
<dt><code>-L</code> [<i>KIND</i>=]<i>PATH</i></dt>
<dd> Add a directory to the library search path. The optional <i>KIND</i> can be one of:</dd>
<dl>
<dl>
<dt><code>dependency</code></dt>
<dd> only lookup transitive dependencies here</dd>
<dt><code>crate</code></dt>
<dd> only lookup local `extern crate` directives here</dd>
<dt><code>native</code></dt>
<dd> only lookup native libraries here</dd>
<dt><code>framework</code></dt>
<dd> only look for OSX frameworks here</dd>
<dt><code>all</code></dt>
<dd> look for anything here (the default)</dd></dl>
</dl>
<dt><code>-l</code> [<i>KIND</i>=]<i>NAME</i></dt>
<dd> Link the generated crate(s) to the specified library <i>NAME</i>. The optional <i>KIND</i> can be one of <i>static</i>, <i>dylib</i>, or <i>framework</i>. If omitted, <i>dylib</i> is assumed.</dd>
<dt><code>&#8211;crate-type</code> [bin|lib|rlib|dylib|cdylib|staticlib]</dt>
<dd> Comma separated list of types of crates for the compiler to emit.</dd>
<dt><code>&#8211;crate-name</code> <i>NAME</i></dt>
<dd> Specify the name of the crate being built.</dd>
<dt><code>&#8211;emit</code> [asm|llvm-bc|llvm-ir|obj|link|dep-info|mir][=<i>PATH</i>]</dt>
<dd> Configure the output that <code>rustc</code> will produce. Each emission may also have an optional explicit output <i>PATH</i> specified for that particular emission kind. This path takes precedence over the <code>-o</code> option.</dd>
<dt><code>&#8211;print</code> [crate-name|file-names|sysroot]</dt>
<dd> Comma separated list of compiler information to print on stdout.</dd>
<dt><code>-g</code></dt>
<dd> Equivalent to <i>-C debuginfo=2</i>.</dd>
<dt><code>-O</code></dt>
<dd> Equivalent to <i>-C opt-level=2</i>.</dd>
<dt><code>-o</code> <i>FILENAME</i></dt>
<dd> Write output to <i>FILENAME</i>. Ignored if multiple <i>&#8211;emit</i> outputs are specified which don&#8217;t have an explicit path otherwise.</dd>
<dt><code>&#8211;out-dir</code> <i>DIR</i></dt>
<dd> Write output to compiler-chosen filename in <i>DIR</i>. Ignored if <i>-o</i> is specified. Defaults to the current directory.</dd>
<dt><code>&#8211;explain</code> <i>OPT</i></dt>
<dd> Provide a detailed explanation of an error message.</dd>
<dt><code>&#8211;test</code></dt>
<dd> Build a test harness.</dd>
<dt><code>&#8211;target</code> <i>TARGET</i></dt>
<dd> Target triple for which the code is compiled. This option defaults to the host’s target triple. The target triple has the general format &lt;arch&gt;&lt;sub&gt;-&lt;vendor&gt;-&lt;sys&gt;-&lt;abi&gt;, where:</dd>
<dl>
<dl>
<dt><code>&lt;arch&gt;</code></dt>
<dd> x86, arm, thumb, mips, etc.</dd>
<dt><code>&lt;sub&gt;</code></dt>
<dd> for example on ARM: v5, v6m, v7a, v7m, etc.</dd>
<dt><code>&lt;vendor&gt;</code></dt>
<dd> pc, apple, nvidia, ibm, etc.</dd>
<dt><code>&lt;sys&gt;</code></dt>
<dd> none, linux, win32, darwin, cuda, etc.</dd>
<dt><code>&lt;abi&gt;</code></dt>
<dd> eabi, gnu, android, macho, elf, etc.</dd></dl>
</dl>
<dt><code>-W help</code></dt>
<dd> Print &#8216;lint&#8217; options and default settings.</dd>
<dt><code>-W</code> <i>OPT</i>, <code>&#8211;warn</code> <i>OPT</i></dt>
<dd> Set lint warnings.</dd>
<dt><code>-A</code> <i>OPT</i>, <code>&#8211;allow</code> <i>OPT</i></dt>
<dd> Set lint allowed.</dd>
<dt><code>-D</code> <i>OPT</i>, <code>&#8211;deny</code> <i>OPT</i></dt>
<dd> Set lint denied.</dd>
<dt><code>-F</code> <i>OPT</i>, <code>&#8211;forbid</code> <i>OPT</i></dt>
<dd> Set lint forbidden.</dd>
<dt><code>-C</code> <i>FLAG</i>[=<i>VAL</i>], <code>&#8211;codegen</code> <i>FLAG</i>[=<i>VAL</i>]</dt>
<dd> Set a codegen-related flag to the value specified. Use <i>-C help</i> to print available flags. See CODEGEN OPTIONS below.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version info and exit.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Use verbose output.</dd>
<dt><code>&#8211;extern</code> <i>NAME</i>=<i>PATH</i></dt>
<dd> Specify where an external rust library is located. These should match <i>extern</i> declarations in the crate&#8217;s source code.</dd>
<dt><code>&#8211;sysroot</code> <i>PATH</i></dt>
<dd> Override the system root.</dd>
<dt><code>-Z</code> <i>FLAG</i></dt>
<dd> Set internal debugging options. Use <i>-Z help</i> to print available options.</dd>
<dt><code>&#8211;color</code> auto|always|never</dt>
<dd> Configure coloring of output:</dd>
<dl>
<dl>
<dt><code>auto</code></dt>
<dd> colorize, if output goes to a tty (default);</dd>
<dt><code>always</code></dt>
<dd> always colorize output;</dd>
<dt><code>never</code></dt>
<dd> never colorize output.</dd></dl>
</dl>
</dl>
<h2>CODEGEN OPTIONS</h2>
<dl>
<dt><code>ar</code>=<i>/path/to/ar</i></dt>
<dd> Path to the archive utility to use when assembling archives.</dd>
<dt><code>linker</code>=<i>/path/to/cc</i></dt>
<dd> Path to the linker utility to use when linking libraries, executables, and objects.</dd>
<dt><code>link-args</code>=&#8217;<i>-flag1 -flag2</i>&#8216;</dt>
<dd> A space-separated list of extra arguments to pass to the linker when the linker is invoked.</dd>
<dt><code>lto</code></dt>
<dd> Perform LLVM link-time optimizations.</dd>
<dt><code>target-cpu</code>=<i>help</i></dt>
<dd> Selects a target processor. If the value is &#8216;help&#8217;, then a list of available CPUs is printed.</dd>
<dt><code>target-feature</code>=&#8217;<i>+feature1</i>,<i>-feature2</i>&#8216;</dt>
<dd> A comma-separated list of features to enable or disable for the target. A preceding &#8216;+&#8217; enables a feature while a preceding &#8216;-&#8216; disables it. Available features can be discovered through <i>llc -mcpu=help</i>.</dd>
<dt><code>passes</code>=<i>val</i></dt>
<dd> A space-separated list of extra LLVM passes to run. A value of &#8216;list&#8217; will cause <code>rustc</code> to print all known passes and exit. The passes specified are appended at the end of the normal pass manager.</dd>
<dt><code>llvm-args</code>=&#8217;<i>-arg1</i> <i>-arg2</i>&#8216;</dt>
<dd> A space-separated list of arguments to pass through to LLVM.</dd>
<dt><code>save-temps</code></dt>
<dd> If specified, the compiler will save more files (.bc, .o, .no-opt.bc) generated throughout compilation in the output directory.</dd>
<dt><code>rpath</code></dt>
<dd> If specified, then the rpath value for dynamic libraries will be set in either dynamic library or executable outputs.</dd>
<dt><code>no-prepopulate-passes</code></dt>
<dd> Suppresses pre-population of the LLVM pass manager that is run over the module.</dd>
<dt><code>no-vectorize-loops</code></dt>
<dd> Suppresses running the loop vectorization LLVM pass, regardless of optimization level.</dd>
<dt><code>no-vectorize-slp</code></dt>
<dd> Suppresses running the LLVM SLP vectorization pass, regardless of optimization level.</dd>
<dt><code>soft-float</code></dt>
<dd> Generates software floating point library calls instead of hardware instructions.</dd>
<dt><code>prefer-dynamic</code></dt>
<dd> Prefers dynamic linking to static linking.</dd>
<dt><code>no-integrated-as</code></dt>
<dd> Force usage of an external assembler rather than LLVM&#8217;s integrated one.</dd>
<dt><code>no-redzone</code></dt>
<dd> Disable the use of the redzone.</dd>
<dt><code>relocation-model</code>=[pic,static,dynamic-no-pic]</dt>
<dd> The relocation model to use. (Default: <i>pic</i>)</dd>
<dt><code>code-model</code>=[small,kernel,medium,large]</dt>
<dd> Choose the code model to use.</dd>
<dt><code>metadata</code>=<i>val</i></dt>
<dd> Metadata to mangle symbol names with.</dd>
<dt><code>extra-filename</code>=<i>val</i></dt>
<dd> Extra data to put in each output filename.</dd>
<dt><code>codegen-units</code>=<i>n</i></dt>
<dd> Divide crate into <i>n</i> units to optimize in parallel.</dd>
<dt><code>remark</code>=<i>val</i></dt>
<dd> Print remarks for these optimization passes (space separated, or &quot;all&quot;).</dd>
<dt><code>no-stack-check</code></dt>
<dd> Disable checks for stack exhaustion (a memory-safety hazard!).</dd>
<dt><code>debuginfo</code>=<i>val</i></dt>
<dd> Debug info emission level:</dd>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> no debug info;</dd>
<dt><code>1</code></dt>
<dd> line-tables only (for stacktraces and breakpoints);</dd>
<dt><code>2</code></dt>
<dd> full debug info with variable and type information.</dd></dl>
</dl>
<dt><code>opt-level</code>=<i>VAL</i></dt>
<dd> Optimize with possible levels 0-3 </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> Some of these affect the output of the compiler, while others affect programs which link to the standard library. </p>
<dl>
<dt><code>RUST_TEST_THREADS</code></dt>
<dd> The test framework Rust provides executes tests in parallel. This variable sets the maximum number of threads used for this purpose. This setting is overridden by the &#8211;test-threads option. </dd>
<dt><code>RUST_TEST_NOCAPTURE</code></dt>
<dd> If set to a value other than &quot;0&quot;, a synonym for the &#8211;nocapture flag. </dd>
<dt><code>RUST_MIN_STACK</code></dt>
<dd> Sets the minimum stack size for new threads. </dd>
<dt><code>RUST_BACKTRACE</code></dt>
<dd> If set to a value different than &quot;0&quot;, produces a backtrace in the output of a program which panics. </dd>
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
