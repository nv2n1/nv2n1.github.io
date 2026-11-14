---
title: "llvm-cxxfilt-14(1)"
name: "llvm-cxxfilt-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-cxxfilt-14/"
description: "llvm-cxxfilt – LLVM symbol name demangler"
---

<h2 class="name">NAME</h2>
<p> llvm-cxxfilt &#8211; LLVM symbol name demangler </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-cxxfilt</code> [<i>options</i>] [<i>mangled names…</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-cxxfilt</code> is a symbol demangler that can be used as a replacement for the GNU <code>c++filt</code> tool. It takes a series of symbol names and prints their demangled form on the standard output stream. If a name cannot be demangled, it is simply printed as is. </p>
<p> If no names are specified on the command-line, names are read interactively from the standard input stream. When reading names from standard input, each input line is split on characters that are not part of valid Itanium name manglings, i.e. characters that are not alphanumeric, ‘.’, ‘$’, or ‘_’. Separators between names are copied to the output as is.</p>
<h2>EXAMPLE</h2>
<pre>
$ llvm-cxxfilt _Z3foov _Z3bari not_mangled
foo()
bar(int)
not_mangled
$ cat input.txt
| _Z3foov *** _Z3bari *** not_mangled |
$ llvm-cxxfilt &lt; input.txt
| foo() *** bar(int) *** not_mangled |
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;format=&lt;value&gt;, -s</code></p>
<dd> Mangling scheme to assume. Valid values are <code>auto</code> (default, auto-detect the style) and <code>gnu</code> (assume GNU/Itanium style).</p>
<dt><code>&#8211;help, -h</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>&#8211;no-strip-underscore, -n</code></p>
<dd> Do not strip a leading underscore. This is the default for all platforms except Mach-O based hosts.</p>
<dt><code>&#8211;strip-underscore, -_</code></p>
<dd> Strip a single leading underscore, if present, from each input name before demangling. On by default on Mach-O based platforms.</p>
<dt><code>&#8211;types, -t</code></p>
<dd> Attempt to demangle names as type names as well as function names.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the version of the <code>llvm-cxxfilt</code> executable.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-cxxfilt</code> returns 0 unless it encounters a usage error, in which case a non-zero exit code is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
