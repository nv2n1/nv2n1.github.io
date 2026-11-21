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
<dt><code>-A</code></dt>
<dd> Alias for <code>&#8211;format</code></dd>
<dt><code>-B</code></dt>
<dd> Alias for <code>&#8211;format</code></dd>
<dt><code>&#8211;common</code></dt>
<dd> Print common symbols in the ELF file. When using Berkeley format, this is added to bss</dd>
<dt><code>-d</code></dt>
<dd> Alias for <code>&#8211;radix</code>=<i>,10/</i></dd>
<dt> <code>&#8211;format=</code>&lt;value&gt; Specify output format</dt>
<dt><code>&#8211;help</code></dt>
<dd>
</dd><dd>Display this help</dd>
<dt><code>-h</code></dt>
<dd> Alias for <code>&#8211;help</code></dd>
<dt><code>-m</code></dt>
<dd> Alias for <code>&#8211;format</code></dd>
<dt><code>-o</code></dt>
<dd> Alias for <code>&#8211;radix</code>=<i>,8/</i></dd>
<dt><code>&#8211;radix=</code>&lt;value&gt;</dt>
<dd> Print size in radix</dd>
<dt><code>&#8211;totals</code></dt>
<dd> Print totals of all objects &#8211; Berkeley format only</dd>
<dt><code>-t</code></dt>
<dd> Alias for <code>&#8211;totals</code></dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the version</dd>
<dt><code>-x</code></dt>
<dd> Alias for <code>&#8211;radix</code>=<i>,16/</i></dd></dl>
<h3>OPTIONS (Mach-O specific):</h3>
<dl>
<dt> <code>&#8211;arch=</code>&lt;value&gt; architecture(s) from a Mach-O file to dump</dt>
<dt><code>-l</code></dt>
<dd>
</dd><dd>When format is darwin, use long format to include addresses and offsets</dd></dl>
<p> Pass @FILE as argument to read options from FILE. </p>
