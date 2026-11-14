---
title: "llvm-size-10(1)"
name: "llvm-size-10"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-size-10/"
description: "llvm-size – manual page for llvm-size 10"
---

<h2 class="name">NAME</h2>
<p> llvm-size &#8211; manual page for llvm-size 10 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm object size dumper </p>
<p> USAGE: llvm-size [options] &lt;input files&gt; </p>
<p> OPTIONS: </p>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dl>
<dd>llvm-size Options:</p>
<dl>
<dt>
<dd> Specify output format</p>
<dt> <code>-A</code> &#8211; System V format</p>
<dt> <code>-B</code> &#8211; Berkeley format</p>
<dt> <code>-m</code> &#8211; Darwin <code>-m</code> format</p>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; architecture(s) from a Mach-O file to dump</p>
<dt><code>&#8211;common</code> &#8211; Print common symbols in the ELF file.</p>
<dd>
<dd>When using Berkeley format, this is added to bss.</p>
<dt> <code>&#8211;format=</code>&lt;value&gt; &#8211; Specify output format</p>
<dt>=sysv</p>
<dd> &#8211; System V format</p>
<dt>=berkeley</p>
<dd> &#8211; Berkeley format</p>
<dt>=darwin</p>
<dd> &#8211; Darwin <code>-m</code> format</p>
<dt> <code>-l</code> &#8211; When format is darwin, use long format to include addresses and offsets.</p>
<dt> <code>&#8211;radix=</code>&lt;value&gt; &#8211; Print size in radix</p>
<dt>=8</p>
<dd> &#8211; Print size in octal</p>
<dt>=10</p>
<dd> &#8211; Print size in decimal</p>
<dt>=16</p>
<dd> &#8211; Print size in hexadecimal</p>
<dt> <code>&#8211;totals</code> &#8211; Print totals of all objects &#8211; Berkeley format only</p>
<dt>
<dd>
<dd>Print size in radix:</p>
<dt> <code>-o</code> &#8211; Print size in octal</p>
<dt> <code>-d</code> &#8211; Print size in decimal</p>
<dt> <code>-x</code> &#8211; Print size in hexadecimal</dl>
<dd>Pass @FILE as argument to read options from FILE. </p>
<h2>Index</h2>
