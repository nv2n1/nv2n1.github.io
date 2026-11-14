---
title: "llvm-lib-14(1)"
name: "llvm-lib-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-lib-14/"
description: "llvm-lib – LLVM lib.exe compatible library tool"
---

<h2 class="name">NAME</h2>
<p> llvm-lib &#8211; LLVM lib.exe compatible library tool </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-lib</code> [/libpath:&lt;path&gt;] [/out:&lt;output&gt;] [/llvmlibthin] [/ignore] [/machine] [/nologo] [files…]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-lib</code> command is intended to be a <code>lib.exe</code> compatible tool. See <i><a rel="nofollow" href="https://msdn.microsoft.com/en-us/library/7ykb2k5f">https://msdn.microsoft.com/en-us/library/7ykb2k5f</a></i> for the general description. </p>
<p> <code>llvm-lib</code> has the following extensions:</p>
<dl>
<dt>&bull;</p>
<dd> Bitcode files in symbol tables. <code>llvm-lib</code> includes symbols from both bitcode files and regular object files in the symbol table.</p>
<dt>&bull;</p>
<dd> Creating thin archives. The /llvmlibthin option causes <code>llvm-lib</code> to create thin archive that contain only the symbol table and the header for the various members. These files are much smaller, but are not compatible with link.exe (lld can handle them).</dl>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
