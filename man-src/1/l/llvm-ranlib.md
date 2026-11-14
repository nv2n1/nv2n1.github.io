---
title: "llvm-ranlib(1)"
name: "llvm-ranlib"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-ranlib/"
description: "llvm-ranlib – Generate index for LLVM archive"
---

<h2 class="name">NAME</h2>
<p> llvm-ranlib &#8211; Generate index for LLVM archive </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-ranlib</code> [&#8211;version] [-help] &lt;archive-file&gt;</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-ranlib</code> command is similar to the common Unix utility, <tt>&quot;ranlib&quot;</tt>. It adds or updates the symbol table in an <font SIZE="-1">LLVM</font> archive file. Note that using the <code>llvm-ar</code> modifier <i>s</i> is usually more efficient than running <code>llvm-ranlib</code> which is only provided only for completness and compatibility. Unlike other implementations of <tt>&quot;ranlib&quot;</tt>, <code>llvm-ranlib</code> indexes <font SIZE="-1">LLVM</font> bitcode files, not native object modules. You can list the contents of the symbol table with the <tt>&quot;llvm-nm -s&quot;</tt> command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>archive-file</i></p>
<dd> Specifies the archive-file to which the symbol table is added or updated.</p>
<dt><i>&#8211;version</i></p>
<dd> Print the version of <code>llvm-ranlib</code> and exit without building a symbol table.</p>
<dt><i>-help</i></p>
<dd> Print usage help for <code>llvm-ranlib</code> and exit without building a symbol table.</dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvm-ranlib</code> succeeds, it will exit with 0. If an error occurs, a non-zero exit code will be returned.</p>
<h2>SEE ALSO</h2>
<p> llvm-ar, <i><a href="/docs/linux/man/1-ranlib/">ranlib</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
<h2>Index</h2>
