---
title: "llvm-config(1)"
name: "llvm-config"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-config/"
description: "llvm-config – Print LLVM compilation options"
---

<h2 class="name">NAME</h2>
<p> llvm-config &#8211; Print LLVM compilation options </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-config</code> <i>option</i> [<i>components</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-config</code> makes it easier to build applications that use <font SIZE="-1">LLVM</font>. It can print the compiler flags, linker flags and object libraries needed to link against <font SIZE="-1">LLVM</font>.</p>
<h2>EXAMPLES</h2>
<p> To link against the <font SIZE="-1">JIT:</font> </p>
<pre><code>
g++ `llvm - config-- cxxflags` - o HowToUseJIT.o - c HowToUseJIT.cpp g++ `llvm - config-- ldflags` - o HowToUseJIT HowToUseJIT.o \
      `llvm - config-- libs engine bcreader scalaropts`
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <font SIZE="-1">LLVM</font>.</p>
<dt><code>-help</code></p>
<dd> Print a summary of <code>llvm-config</code> arguments.</p>
<dt><code>&#8211;prefix</code></p>
<dd> Print the installation prefix for <font SIZE="-1">LLVM</font>.</p>
<dt><code>&#8211;src-root</code></p>
<dd> Print the source root from which <font SIZE="-1">LLVM</font> was built.</p>
<dt><code>&#8211;obj-root</code></p>
<dd> Print the object root used to build <font SIZE="-1">LLVM</font>.</p>
<dt><code>&#8211;bindir</code></p>
<dd> Print the installation directory for <font SIZE="-1">LLVM</font> binaries.</p>
<dt><code>&#8211;includedir</code></p>
<dd> Print the installation directory for <font SIZE="-1">LLVM</font> headers.</p>
<dt><code>&#8211;libdir</code></p>
<dd> Print the installation directory for <font SIZE="-1">LLVM</font> libraries.</p>
<dt><code>&#8211;cxxflags</code></p>
<dd> Print the C<font SIZE="-2">++</font> compiler flags needed to use <font SIZE="-1">LLVM</font> headers.</p>
<dt><code>&#8211;ldflags</code></p>
<dd> Print the flags needed to link against <font SIZE="-1">LLVM</font> libraries.</p>
<dt><code>&#8211;libs</code></p>
<dd> Print all the libraries needed to link against the specified <font SIZE="-1">LLVM</font> <i>components</i>, including any dependencies.</p>
<dt><code>&#8211;libnames</code></p>
<dd> Similar to <code>&#8211;libs</code>, but prints the bare filenames of the libraries without <code>-l</code> or pathnames. Useful for linking against a not-yet-installed copy of <font SIZE="-1">LLVM</font>.</p>
<dt><code>&#8211;libfiles</code></p>
<dd> Similar to <code>&#8211;libs</code>, but print the full path to each library file. This is useful when creating makefile dependencies, to ensure that a tool is relinked if any library it uses changes.</p>
<dt><code>&#8211;components</code></p>
<dd> Print all valid component names.</p>
<dt><code>&#8211;targets-built</code></p>
<dd> Print the component names for all targets supported by this copy of <font SIZE="-1">LLVM</font>.</p>
<dt><code>&#8211;build-mode</code></p>
<dd> Print the build mode used when <font SIZE="-1">LLVM</font> was built (e.g. Debug or Release)</dl>
<h2>COMPONENTS</h2>
<p> To print a list of all available components, run <code>llvm-config &#8211;components</code>. In most cases, components correspond directly to <font SIZE="-1">LLVM</font> libraries. Useful &#8220;virtual&#8221; components include:</p>
<dl>
<dt><code>all</code></p>
<dd> Includes all <font SIZE="-1">LLVM</font> libaries. The default if no components are specified.</p>
<dt><code>backend</code></p>
<dd> Includes either a native backend or the C backend.</p>
<dt><code>engine</code></p>
<dd> Includes either a native <font SIZE="-1">JIT</font> or the bitcode interpreter.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-config</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
