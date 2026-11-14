---
title: "llvm-tli-checker-14(1)"
name: "llvm-tli-checker-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-tli-checker-14/"
description: "llvm-tli-checker – TargetLibraryInfo vs library checker"
---

<h2 class="name">NAME</h2>
<p> llvm-tli-checker &#8211; TargetLibraryInfo vs library checker </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-tli-checker</code> [<i>options</i>] [<i>library-file…</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-tli-checker</code> compares TargetLibraryInfo’s opinion of the availability of library functions against the set of functions exported by the specified library files, reporting any disagreements between TLI’s opinion and whether the function is actually present. This is primarily useful for vendors to ensure the TLI for their target is correct, and the compiler will not “optimize” some code sequence into a library call that is not actually available.</p>
<h2>EXAMPLE</h2>
<pre><code>
$ llvm-tli-checker --triple x86_64-scei-ps4 example.so
TLI knows 466 symbols, 235 available for 'x86_64-scei-ps4'
Looking for symbols in 'example.so'
Found 235 global function symbols in 'example.so'
Found a grand total of 235 library symbols
&lt;&lt; TLI yes SDK no:  '_ZdaPv' aka operator delete[](void*)
&gt;&gt; TLI no  SDK yes: '_ZdaPvj' aka operator delete[](void*, unsigned int)
&lt;&lt; Total TLI yes SDK no:  1
&gt;&gt; Total TLI no  SDK yes: 1
== Total TLI yes SDK yes: 234
FAIL: LLVM TLI doesn't match SDK libraries.
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;dump-tli</code></p>
<dd> Print “available”/”not available” for each library function, according to TargetLibraryInfo’s information for the specified triple, and exit. This option does not read any input files.</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a summary of command line options and exit.</p>
<dt><code>&#8211;libdir=&lt;directory&gt;</code></p>
<dd> A base directory to prepend to each library file path. This is handy when there are a number of library files all in the same directory, or a list of input filenames are kept in a response file.</p>
<dt><code>&#8211;report=&lt;level&gt;</code></p>
<dd> The amount of information to report. &lt;level&gt; can be summary, discrepancy, or full. A summary report gives only the count of matching and mis-matching symbols; discrepancy lists the mis-matching symbols; and full lists all symbols known to TLI, matching or mis-matching. The default is discrepancy.</p>
<dt><code>&#8211;separate</code></p>
<dd> Read and report a summary for each library file separately. This can be useful to identify library files that don’t contribute anything that TLI knows about. Implies –report=summary (can be overridden).</p>
<dt><code>&#8211;triple=&lt;triple&gt;</code></p>
<dd> The triple to use for initializing TargetLibraryInfo.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options and/or library names from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-tli-checker</code> returns 0 even if there are mismatches. It returns a non-zero exit code if there is an unrecognized option, or no input files are provided.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
