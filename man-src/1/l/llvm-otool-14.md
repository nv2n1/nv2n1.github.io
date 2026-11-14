---
title: "llvm-otool-14(1)"
name: "llvm-otool-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-otool-14/"
description: "llvm-otool – Mach-O dumping tool"
---

<h2 class="name">NAME</h2>
<p> llvm-otool &#8211; Mach-O dumping tool </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-otool</code> [<i>option…</i>] <i>[file…]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-otool</code> is a tool for dumping Mach-O files. </p>
<p> It attempts to be command-line-compatible and output-compatible with macOS’s <code>otool</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-arch &lt;value&gt;</code></p>
<dd> Select slice of universal Mach-O file.</p>
<dt><code>-C</code></p>
<dd> Print linker optimization hints.</p>
<dt><code>-D</code></p>
<dd> Print shared library id.</p>
<dt><code>-d</code></p>
<dd> Print data section.</p>
<dt><code>-f</code></p>
<dd> Print universal headers.</p>
<dt><code>-G</code></p>
<dd> Print data-in-code table.</p>
<dt><code>&#8211;help-hidden</code></p>
<dd> Print help for hidden flags.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help.</p>
<dt><code>-h</code></p>
<dd> Print mach header.</p>
<dt><code>-I</code></p>
<dd> Print indirect symbol table.</p>
<dt><code>-j</code></p>
<dd> Print opcode bytes.</p>
<dt><code>-L</code></p>
<dd> Print used shared libraries.</p>
<dt><code>-l</code></p>
<dd> Print load commands.</p>
<dt><code>-mcpu=&lt;value&gt;</code></p>
<dd> Select cpu for disassembly.</p>
<dt><code>-o</code></p>
<dd> Print Objective-C segment.</p>
<dt><code>-P</code></p>
<dd> Print __TEXT,__info_plist section as strings.</p>
<dt><code>-p &lt;function name&gt;</code></p>
<dd> Start disassembly at &lt;function name&gt;.</p>
<dt><code>-r</code></p>
<dd> Print relocation entries.</p>
<dt><code>-s &lt;segname&gt; &lt;sectname&gt;</code></p>
<dd> Print contents of section.</p>
<dt><code>-t</code></p>
<dd> Print text section.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version.</p>
<dt><code>-V</code></p>
<dd> Symbolize disassembled operands (implies <i>-v</i>).</p>
<dt><code>-v</code></p>
<dd> Verbose output / disassemble when printing text sections.</p>
<dt><code>-X</code></p>
<dd> Omit leading addresses or headers.</p>
<dt><code>-x</code></p>
<dd> Print all text sections.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options and commands from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-otool</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-objdump/">https://github.com/llvm/llvm-project/labels/tools:llvm-objdump/</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-objdump/">llvm-objdump</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
