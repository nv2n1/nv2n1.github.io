---
title: "llvm-cxxmap-14(1)"
name: "llvm-cxxmap-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-cxxmap-14/"
description: "llvm-cxxmap – Mangled name remapping tool"
---

<h2 class="name">NAME</h2>
<p> llvm-cxxmap &#8211; Mangled name remapping tool </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-cxxmap</code> [<i>options</i>] <i>symbol-file-1</i> <i>symbol-file-2</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-cxxmap</code> tool performs fuzzy matching of C++ mangled names, based on a file describing name components that should be considered equivalent. </p>
<p> The symbol files should contain a list of C++ mangled names (one per line). Blank lines and lines starting with <code>#</code> are ignored. The output is a list of pairs of equivalent symbols, one per line, of the form </p>
<pre>
&lt;symbol-1&gt; &lt;symbol-2&gt;
</pre>
<p> where <code>&lt;symbol-1&gt;</code> is a symbol from <i>symbol-file-1</i> and <code>&lt;symbol-2&gt;</code> is a symbol from <i>symbol-file-2</i>. Mappings for which the two symbols are identical are omitted.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-remapping-file=file, -r=file</code></p>
<dd> Specify a file containing a list of equivalence rules that should be used to determine whether two symbols are equivalent. Required. See <i>REMAPPING FILE</i>.</p>
<dt><code>-output=file, -o=file</code></p>
<dd> Specify a file to write the list of matched names to. If unspecified, the list will be written to stdout.</p>
<dt><code>-Wambiguous</code></p>
<dd> Produce a warning if there are multiple equivalent (but distinct) symbols in <i>symbol-file-2</i>.</p>
<dt><code>-Wincomplete</code></p>
<dd> Produce a warning if <i>symbol-file-1</i> contains a symbol for which there is no equivalent symbol in <i>symbol-file-2</i>.</dl>
<h2>REMAPPING FILE</h2>
<p> The remapping file is a text file containing lines of the form </p>
<pre>
fragmentkind fragment1 fragment2
</pre>
<p> where <code>fragmentkind</code> is one of <code>name</code>, <code>type</code>, or <code>encoding</code>, indicating whether the following mangled name fragments are &lt;<i>name</i>&gt;s, &lt;<i>type</i>&gt;s, or &lt;<i>encoding</i>&gt;s, respectively. Blank lines and lines starting with <code>#</code> are ignored. </p>
<p> Unmangled C names can be expressed as an <code>encoding</code> that is a (length-prefixed) &lt;<i>source-name</i>&gt;: </p>
<pre>
# C function &quot;void foo_bar()&quot; is remapped to C++ function &quot;void foo::bar()&quot;.
encoding 7foo_bar _Z3foo3barv
</pre>
<p> For convenience, built-in &lt;substitution&gt;s such as <code>St</code> and <code>Ss</code> are accepted as &lt;name&gt;s (even though they technically are not &lt;name&gt;s). </p>
<p> For example, to specify that <code>absl::string_view</code> and <code>std::string_view</code> should be treated as equivalent, the following remapping file could be used: </p>
<pre>
# absl::string_view is considered equivalent to std::string_view
type N4absl11string_viewE St17basic_string_viewIcSt11char_traitsIcEE
# std:: might be std::__1:: in libc++ or std::__cxx11:: in libstdc++
name St St3__1
name St St7__cxx11
</pre>
<p> <code>NOTE:</code> Symbol remapping is currently only supported for C++ mangled names following the Itanium C++ ABI mangling scheme. This covers all C++ targets supported by Clang other than Windows targets.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
