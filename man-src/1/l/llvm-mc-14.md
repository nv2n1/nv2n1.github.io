---
title: "llvm-mc-14(1)"
name: "llvm-mc-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-mc-14/"
description: "llvm-mc – manual page for llvm-mc 14"
---

<h2 class="name">NAME</h2>
<p> llvm-mc &#8211; manual page for llvm-mc 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: llvm machine code playground </p>
<p> USAGE: llvm-mc [options] &lt;input file&gt; </p>
<p> OPTIONS: </p>
<p> Color Options:</p>
<dl>
<dt> <code>&#8211;color</code> &#8211; Use colors in output (default=autodetect)</dl>
<dd>Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</p>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</p>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dl>
<dd>MC Options:</p>
<dl>
<dt> <code>-I=</code>&lt;directory&gt; &#8211; Directory of include files</p>
<dt> <code>-M=</code>&lt;string&gt; &#8211; Disassembler options</p>
<dt> <code>&#8211;arch=</code>&lt;string&gt; &#8211; Target arch to assemble for, see <code>-version</code> for available targets</p>
<dt>
<dd>
<dd>Action to perform:</p>
<dt> <code>&#8211;as-lex</code> &#8211; Lex tokens from a .s file</p>
<dt> <code>&#8211;assemble</code> &#8211; Assemble a .s file (default)</p>
<dt> <code>&#8211;disassemble</code> &#8211; Disassemble strings of hex bytes</p>
<dt> <code>&#8211;mdis</code> &#8211; Marked up disassembly of strings of hex bytes</p>
<dt> <code>&#8211;compress-debug-sections=</code>&lt;value&gt; &#8211; Choose DWARF debug sections compression:</p>
<dt>=none</p>
<dd> &#8211; No compression</p>
<dt>=zlib</p>
<dd> &#8211; Use zlib compression</p>
<dt>=zlib-gnu</p>
<dd> &#8211; Use zlib-gnu compression (deprecated)</p>
<dt> <code>&#8211;defsym=</code>&lt;string&gt; &#8211; Defines a symbol to be an integer constant</p>
<dt> <code>&#8211;fdebug-compilation-dir=</code>&lt;string&gt; &#8211; Specifies the debug info&#8217;s compilation dir</p>
<dt> <code>&#8211;fdebug-prefix-map=</code>&lt;= separated key-value pairs&gt; &#8211; Map file source paths in debug info</p>
<dt> <code>&#8211;filetype=</code>&lt;value&gt; &#8211; Choose an output file type:</p>
<dt>=asm</p>
<dd> &#8211; Emit an assembly (&#8216;.s&#8217;) file</p>
<dt>=null</p>
<dd> &#8211; Don&#8217;t emit anything (for timing purposes)</p>
<dt>=obj</p>
<dd> &#8211; Emit a native object (&#8216;.o&#8217;) file</p>
<dt> <code>-g</code> &#8211; Generate dwarf debugging info for assembly source files</p>
<dt> <code>&#8211;large-code-model</code> &#8211; Create cfi directives that assume the code might be more than 2gb away</p>
<dt> <code>&#8211;main-file-name=</code>&lt;string&gt; &#8211; Specifies the name we should consider the input file</p>
<dt> <code>&#8211;masm-hexfloats</code> &#8211; Enable MASM-style hex float initializers (3F800000r)</p>
<dt> <code>&#8211;masm-integers</code> &#8211; Enable binary and hex masm integers (0b110 and 0ABCh)</p>
<dt> <code>&#8211;mattr=</code>&lt;a1,+a2,-a3,&#8230;&gt; &#8211; Target specific attributes (<code>-mattr</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;mcpu=</code>&lt;cpu-name&gt; &#8211; Target a specific cpu type (<code>-mcpu</code>=<i>,help/</i> for details)</p>
<dt> <code>&#8211;motorola-integers</code> &#8211; Enable binary and hex Motorola integers (%110 and $ABC)</p>
<dt> <code>-n</code> &#8211; Don&#8217;t assume assembly file starts in the text section</p>
<dt> <code>&#8211;no-exec-stack</code> &#8211; File doesn&#8217;t need an exec stack</p>
<dt> <code>-o=</code>&lt;filename&gt; &#8211; Output filename</p>
<dt> <code>&#8211;output-asm-variant=</code>&lt;uint&gt; &#8211; Syntax variant to use for output printing</p>
<dt> <code>&#8211;position-independent</code> &#8211; Position independent</p>
<dt> <code>&#8211;preserve-comments</code> &#8211; Preserve Comments in outputted assembly</p>
<dt> <code>&#8211;print-imm-hex</code> &#8211; Prefer hex format for immediate values</p>
<dt> <code>&#8211;relax-relocations</code> &#8211; Emit R_X86_64_GOTPCRELX instead of R_X86_64_GOTPCREL</p>
<dt> <code>&#8211;save-temp-labels</code> &#8211; Don&#8217;t discard temporary labels</p>
<dt> <code>&#8211;show-encoding</code> &#8211; Show instruction encodings</p>
<dt> <code>&#8211;show-inst</code> &#8211; Show internal instruction representation</p>
<dt> <code>&#8211;show-inst-operands</code> &#8211; Show instructions operands as parsed</p>
<dt> <code>&#8211;split-dwarf-file=</code>&lt;filename&gt; &#8211; DWO output filename</p>
<dt> <code>&#8211;triple=</code>&lt;string&gt; &#8211; Target triple to assemble for, see <code>-version</code> for available targets </p>
</dl>
<h2>Index</h2>
