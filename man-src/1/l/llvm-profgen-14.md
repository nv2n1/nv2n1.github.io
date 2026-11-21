---
title: "llvm-profgen-14(1)"
name: "llvm-profgen-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-profgen-14/"
description: "llvm-profgen – LLVM SPGO profile generation tool"
---

<h2 class="name">NAME</h2>
<p> llvm-profgen &#8211; LLVM SPGO profile generation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-profgen</code> [<i>commands</i>] [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-profgen</code> utility generates a profile data file from given perf script data files for sample-based profile guided optimization(SPGO).</p>
<h2>COMMANDS</h2>
<p> At least one of the following commands are required:</p>
<dl>
<dt><code>&#8211;perfscript=&lt;string[,string,&#8230;]&gt;</code></dt>
<dd> Path of perf-script trace created by Linux perf tool with <i>script</i> command(the raw perf.data should be profiled with -b).</dd>
<dt><code>&#8211;binary=&lt;string[,string,&#8230;]&gt;</code></dt>
<dd> Path of the input profiled binary files.</dd>
<dt><code>&#8211;output=&lt;string&gt;</code></dt>
<dd> Path of the output profile file.</dd></dl>
<h2>OPTIONS</h2>
<p> <code>llvm-profgen</code> supports the following options:</p>
<dl>
<dt><code>&#8211;format=[text|binary|extbinary|compbinary|gcc]</code></dt>
<dd> Specify the format of the generated profile. Supported &lt;format&gt; are <i>text</i>, <i>binary</i>, <i>extbinary</i>, <i>compbinary</i>, <i>gcc</i>, see <i>llvm-profdata</i> for more descriptions of the format.</dd>
<dt><code>&#8211;show-mmap-events</code></dt>
<dd> Print mmap events.</dd>
<dt><code>&#8211;show-disassembly</code></dt>
<dd> Print disassembled code.</dd>
<dt><code>&#8211;x86-asm-syntax=[att|intel]</code></dt>
<dd> Specify whether to print assembly code in AT&amp;T syntax (the default) or Intel syntax.</dd></dl>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
