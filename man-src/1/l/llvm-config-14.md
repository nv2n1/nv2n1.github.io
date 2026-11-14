---
title: "llvm-config-14(1)"
name: "llvm-config-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-config-14/"
description: "llvm-config – Print LLVM compilation options"
---

<h2 class="name">NAME</h2>
<p> llvm-config &#8211; Print LLVM compilation options </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-config</code> <i>option</i> [<i>components</i>…]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-config</code> makes it easier to build applications that use LLVM. It can print the compiler flags, linker flags and object libraries needed to link against LLVM.</p>
<h2>EXAMPLES</h2>
<p> To link against the JIT: </p>
<pre><code>
g++ `llvm - config-- cxxflags` - o HowToUseJIT.o - c HowToUseJIT.cpp g++ `llvm - config-- ldflags` - o HowToUseJIT HowToUseJIT.o \
    `llvm - config-- libs engine bcreader scalaropts`
</code></pre>
<h2>OPTIONS</h2>
<p> <code>–version</code> Print the version number of LLVM. </p>
<p> <code>-help</code> Print a summary of <code>llvm-config</code> arguments. </p>
<p> <code>–prefix</code> Print the installation prefix for LLVM. </p>
<p> <code>–src-root</code> Print the source root from which LLVM was built. </p>
<p> <code>–obj-root</code> Print the object root used to build LLVM. </p>
<p> <code>–bindir</code> Print the installation directory for LLVM binaries. </p>
<p> <code>–includedir</code> Print the installation directory for LLVM headers. </p>
<p> <code>–libdir</code> Print the installation directory for LLVM libraries. </p>
<p> <code>–cxxflags</code> Print the C++ compiler flags needed to use LLVM headers. </p>
<p> <code>–ldflags</code> Print the flags needed to link against LLVM libraries. </p>
<p> <code>–libs</code> Print all the libraries needed to link against the specified LLVM <i>components</i>, including any dependencies. </p>
<p> <code>–libnames</code> Similar to <code>–libs</code>, but prints the bare filenames of the libraries without <code>-l</code> or pathnames. Useful for linking against a not-yet-installed copy of LLVM. </p>
<p> <code>–libfiles</code> Similar to <code>–libs</code>, but print the full path to each library file. This is useful when creating makefile dependencies, to ensure that a tool is relinked if any library it uses changes. </p>
<p> <code>–components</code> Print all valid component names. </p>
<p> <code>–targets-built</code> Print the component names for all targets supported by this copy of LLVM. </p>
<p> <code>–build-mode</code> Print the build mode used when LLVM was built (e.g. Debug or Release)</p>
<h2>COMPONENTS</h2>
<p> To print a list of all available components, run <code>llvm-config –components</code>. In most cases, components correspond directly to LLVM libraries. Useful “virtual” components include: </p>
<p> <code>all</code> Includes all LLVM libraries. The default if no components are specified. </p>
<p> <code>backend</code> Includes either a native backend or the C backend. </p>
<p> <code>engine</code> Includes either a native JIT or the bitcode interpreter.</p>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-config</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
