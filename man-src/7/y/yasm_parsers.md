---
title: "yasm_parsers(7)"
name: "yasm_parsers"
section: "7"
letter: "y"
url: "/docs/linux/man/7-yasm_parsers/"
description: "yasm_parsers – Yasm Supported Parsers (Assembler Syntaxes)"
---

<p>yasm_parsers &#8211; Yasm Supported Parsers (Assembler Syntaxes)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>yasm</code> <code>-p&nbsp;<wbr></code><i>parser</i> [<code>-r&nbsp;<wbr></code><i>preproc</i>] <i>&#8230;</i></dl>
<h2>Description</h2>
<dd>The standard Yasm distribution includes a number of modules for different parsers (assembler syntaxes). </p>
<p> The parser is selected on the <code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1) command line by use of the <code>-p </code><i>parser</i> command line option.</p>
<h2>Nasm Parser</h2>
<p>NASM syntax, selected with <code>-p nasm</code>, is the most full-featured syntax supported by Yasm. Yasm is nearly 100% compatible with NASM for 16-bit and 32-bit x86 code. Yasm additionally supports 64-bit AMD64 code with Yasm extensions to the NASM syntax; see <code><a href="/docs/linux/man/7-yasm_arch/">yasm_arch</a></code>(7) for details. NASM syntax is the Yasm default.</p>
<h2>Gas Parser</h2>
<p>The GNU Assembler (GAS) is the de-facto cross-platform assembler for modern Unix systems, and is used as the backend for the GCC compiler. Yasm&#8217;s support for GAS syntax is moderately good, although immature: not all directives are supported, and only 32-bit x86 and AMD64 architectures are supported. Nearly all of the GAS preprocessor is also supported. Yasm&#8217;s GAS syntax support is good enough to handle essentially all x86 and AMD64 GCC compiler output. The GAS parser can be selected with <code>-p gas</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1), <code><a href="/docs/linux/man/7-yasm_arch/">yasm_arch</a></code>(7)</p>
<h2>Author</h2>
<p><code>Peter Johnson</code> &lt;peter [at] tortall.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Peter Johnson</p>
