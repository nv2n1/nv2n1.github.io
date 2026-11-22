---

title: "llvm-config(1)"
name: "llvm-config"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-config/"
description: "llvm-config – Print LLVM compilation options"
---

<p> llvm-config &#8211; Print LLVM compilation options </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-config</code> <i>option</i> [<i>components</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-config</code> makes it easier to build applications that use LLVM. It can print the compiler flags, linker flags and object libraries needed to link against LLVM.</p>
<h2>EXAMPLES</h2>
<p> To link against the JIT: </p>
<pre><code>
g++ `llvm - config-- cxxflags` - o HowToUseJIT.o - c HowToUseJIT.cpp g++ `llvm - config-- ldflags` - o HowToUseJIT HowToUseJIT.o \
      `llvm - config-- libs engine bcreader scalaropts`
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the version number of LLVM.</dd>
<dt><code>-help</code></dt>
<dd> Print a summary of <code>llvm-config</code> arguments.</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> Print the installation prefix for LLVM.</dd>
<dt><code>&#8211;src-root</code></dt>
<dd> Print the source root from which LLVM was built.</dd>
<dt><code>&#8211;obj-root</code></dt>
<dd> Print the object root used to build LLVM.</dd>
<dt><code>&#8211;bindir</code></dt>
<dd> Print the installation directory for LLVM binaries.</dd>
<dt><code>&#8211;includedir</code></dt>
<dd> Print the installation directory for LLVM headers.</dd>
<dt><code>&#8211;libdir</code></dt>
<dd> Print the installation directory for LLVM libraries.</dd>
<dt><code>&#8211;cxxflags</code></dt>
<dd> Print the C++ compiler flags needed to use LLVM headers.</dd>
<dt><code>&#8211;ldflags</code></dt>
<dd> Print the flags needed to link against LLVM libraries.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Print all the libraries needed to link against the specified LLVM <i>components</i>, including any dependencies.</dd>
<dt><code>&#8211;libnames</code></dt>
<dd> Similar to <code>&#8211;libs</code>, but prints the bare filenames of the libraries without <code>-l</code> or pathnames. Useful for linking against a not-yet-installed copy of LLVM.</dd>
<dt><code>&#8211;libfiles</code></dt>
<dd> Similar to <code>&#8211;libs</code>, but print the full path to each library file. This is useful when creating makefile dependencies, to ensure that a tool is relinked if any library it uses changes.</dd>
<dt><code>&#8211;components</code></dt>
<dd> Print all valid component names.</dd>
<dt><code>&#8211;targets-built</code></dt>
<dd> Print the component names for all targets supported by this copy of LLVM.</dd>
<dt><code>&#8211;build-mode</code></dt>
<dd> Print the build mode used when LLVM was built (e.g. Debug or Release)</dd></dl>
<h2>COMPONENTS</h2>
<p> To print a list of all available components, run <code>llvm-config &#8211;components</code>. In most cases, components correspond directly to LLVM libraries. Useful &#8220;virtual&#8221; components include:</p>
<dl>
<dt><code>all</code></dt>
<dd> Includes all LLVM libaries. The default if no components are specified.</dd>
<dt><code>backend</code></dt>
<dd> Includes either a native backend or the C backend.</dd>
<dt><code>engine</code></dt>
<dd> Includes either a native JIT or the bitcode interpreter.</dd></dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-config</code> succeeds, it will exit with 0. Otherwise, if an error occurs, it will exit with a non-zero value.</p>
<h2>AUTHORS</h2>
<p> Maintained by the LLVM Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
