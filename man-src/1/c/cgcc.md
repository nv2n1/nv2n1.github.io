---
title: "cgcc(1)"
name: "cgcc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cgcc/"
description: "cgcc – Compiler wrapper to run Sparse after compiling"
---

<h2>NAME</h2>
<p> cgcc &#8211; Compiler wrapper to run Sparse after compiling</p>
<h2>SYNOPSIS</h2>
<p> <code>cgcc</code> [<i>SPARSE OPTIONS</i>]&#8230; [<i>COMPILER OPTIONS</i>]&#8230; [<i>INPUT FILES</i>]&#8230;<br />
 <code>make CC=cgcc</code></p>
<h2>DESCRIPTION</h2>
<p> <code>cgcc</code> provides a wrapper around a C compiler (<code>cc</code> by default) which also invokes the Sparse static analysis tool. </p>
<p> <code>cgcc</code> accepts all Sparse command-line options, such as warning options, and passes all other options through to the compiler. </p>
<p> By providing the same interface as the C compiler, <code>cgcc</code> allows projects to run Sparse as part of their build without modifying their build system, by using <code>cgcc</code> as the compiler. For many projects, setting <code>CC=cgcc</code> on the <code>make</code> command-line will work.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>REAL_CC</code></p>
<dd> If set, <code>cgcc</code> will use this as the compiler to invoke, rather than the default <code>cc</code>.</p>
<dt><code>CHECK</code></p>
<dd> If set, <code>cgcc</code> will use this as the Sparse program to invoke, rather than the default <code>sparse</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sparse/">sparse</a></code>(1) </p>
<h2>Index</h2>
