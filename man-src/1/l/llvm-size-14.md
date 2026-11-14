---
title: "llvm-size-14(1)"
name: "llvm-size-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-size-14/"
description: "llvm-size – manual page for llvm-size 14"
---

<h2 class="name">NAME</h2>
<p> llvm-size &#8211; manual page for llvm-size 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: LLVM object size dumper </p>
<p> USAGE: build-llvm/tools/clang/stage2-bins/bin/llvm-size [options] &lt;input object files&gt;</p>
<h3>OPTIONS:</h3>
<dl>
<dt><code>-A</code></p>
<dd> Alias for <code>&#8211;format</code></p>
<dt><code>-B</code></p>
<dd> Alias for <code>&#8211;format</code></p>
<dt><code>&#8211;common</code></p>
<dd> Print common symbols in the ELF file. When using Berkeley format, this is added to bss</p>
<dt><code>-d</code></p>
<dd> Alias for <code>&#8211;radix</code>=<i>,10/</i></p>
<dt> <code>&#8211;format=</code>&lt;value&gt; Specify output format</p>
<dt><code>&#8211;help</code></p>
<dd>
<dd>Display this help</p>
<dt><code>-h</code></p>
<dd> Alias for <code>&#8211;help</code></p>
<dt><code>-m</code></p>
<dd> Alias for <code>&#8211;format</code></p>
<dt><code>-o</code></p>
<dd> Alias for <code>&#8211;radix</code>=<i>,8/</i></p>
<dt><code>&#8211;radix=</code>&lt;value&gt;</p>
<dd> Print size in radix</p>
<dt><code>&#8211;totals</code></p>
<dd> Print totals of all objects &#8211; Berkeley format only</p>
<dt><code>-t</code></p>
<dd> Alias for <code>&#8211;totals</code></p>
<dt><code>&#8211;version</code></p>
<dd> Display the version</p>
<dt><code>-x</code></p>
<dd> Alias for <code>&#8211;radix</code>=<i>,16/</i></dl>
<h3>OPTIONS (Mach-O specific):</h3>
<dl>
<dt> <code>&#8211;arch=</code>&lt;value&gt; architecture(s) from a Mach-O file to dump</p>
<dt><code>-l</code></p>
<dd>
<dd>When format is darwin, use long format to include addresses and offsets</dl>
<p> Pass @FILE as argument to read options from FILE. </p>
<h2>Index</h2>
