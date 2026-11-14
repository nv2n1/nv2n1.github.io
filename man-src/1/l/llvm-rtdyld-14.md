---
title: "llvm-rtdyld-14(1)"
name: "llvm-rtdyld-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-rtdyld-14/"
description: "llvm-rtdyld – manual page for llvm-rtdyld 14"
---

<h2 class="name">NAME</h2>
<p> llvm-rtdyld &#8211; manual page for llvm-rtdyld 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm MC-JIT tool </p>
<p> USAGE: llvm-rtdyld [options] &lt;input files&gt; <code>&#8211;args</code> &lt;program arguments&gt;&#8230; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dl>
<dd>Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dl>
<dd>RTDyld Options:</p>
<dl>
<dt> <code>&#8211;args</code> &lt;string&gt;&#8230; &#8211; &lt;program arguments&gt;&#8230;</p>
<dt> <code>&#8211;check=</code>&lt;string&gt; &#8211; File containing RuntimeDyld verifier checks.</p>
<dt> <code>&#8211;dylib=</code>&lt;string&gt; &#8211; Add library.</p>
<dt> <code>&#8211;entry=</code>&lt;string&gt; &#8211; Function to call as entry point.</p>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;preallocate=</code>&lt;ulong&gt; &#8211; Allocate memory upfront rather than on-demand</p>
<dt> <code>&#8211;show-times</code> &#8211; Show times for llvm-rtdyld phases</p>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple for disassembler</p>
<dt>
<dd>
<dd>Action to perform:</p>
<dt> <code>&#8211;execute</code> &#8211; Load, link, and execute the inputs.</p>
<dt> <code>&#8211;printline</code> &#8211; Load, link, and print line information for each function.</p>
<dt> <code>&#8211;printdebugline</code> &#8211; Load, link, and print line information for each function using the debug object</p>
<dt> <code>&#8211;printobjline</code> &#8211; Like <code>-printlineinfo</code> but does not load the object first</p>
<dt> <code>&#8211;verify</code> &#8211; Load, link and verify the resulting memory image. </p>
</dl>
<h2>Index</h2>
