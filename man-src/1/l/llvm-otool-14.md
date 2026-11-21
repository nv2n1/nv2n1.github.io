---

title: "llvm-otool-14(1)"
name: "llvm-otool-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-otool-14/"
description: "llvm-otool – Mach-O dumping tool"
---

<p> <code>llvm-otool</code> [<i>option…</i>] <i>[file…]</i></p>
<p> <code>llvm-otool</code> is a tool for dumping Mach-O files. </p>
<p> It attempts to be command-line-compatible and output-compatible with macOS’s <code>otool</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-arch &lt;value&gt;</code></dt>
<dd> Select slice of universal Mach-O file.</dd>
<dt><code>-C</code></dt>
<dd> Print linker optimization hints.</dd>
<dt><code>-D</code></dt>
<dd> Print shared library id.</dd>
<dt><code>-d</code></dt>
<dd> Print data section.</dd>
<dt><code>-f</code></dt>
<dd> Print universal headers.</dd>
<dt><code>-G</code></dt>
<dd> Print data-in-code table.</dd>
<dt><code>&#8211;help-hidden</code></dt>
<dd> Print help for hidden flags.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print help.</dd>
<dt><code>-h</code></dt>
<dd> Print mach header.</dd>
<dt><code>-I</code></dt>
<dd> Print indirect symbol table.</dd>
<dt><code>-j</code></dt>
<dd> Print opcode bytes.</dd>
<dt><code>-L</code></dt>
<dd> Print used shared libraries.</dd>
<dt><code>-l</code></dt>
<dd> Print load commands.</dd>
<dt><code>-mcpu=&lt;value&gt;</code></dt>
<dd> Select cpu for disassembly.</dd>
<dt><code>-o</code></dt>
<dd> Print Objective-C segment.</dd>
<dt><code>-P</code></dt>
<dd> Print __TEXT,__info_plist section as strings.</dd>
<dt><code>-p &lt;function name&gt;</code></dt>
<dd> Start disassembly at &lt;function name&gt;.</dd>
<dt><code>-r</code></dt>
<dd> Print relocation entries.</dd>
<dt><code>-s &lt;segname&gt; &lt;sectname&gt;</code></dt>
<dd> Print contents of section.</dd>
<dt><code>-t</code></dt>
<dd> Print text section.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version.</dd>
<dt><code>-V</code></dt>
<dd> Symbolize disassembled operands (implies <i>-v</i>).</dd>
<dt><code>-v</code></dt>
<dd> Verbose output / disassemble when printing text sections.</dd>
<dt><code>-X</code></dt>
<dd> Omit leading addresses or headers.</dd>
<dt><code>-x</code></dt>
<dd> Print all text sections.</dd>
<dt><code>@&lt;FILE&gt;</code></dt>
<dd> Read command-line options and commands from response file <i>&lt;FILE&gt;</i>.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-otool</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-objdump/">https://github.com/llvm/llvm-project/labels/tools:llvm-objdump/</a></i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code>llvm-objdump(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
