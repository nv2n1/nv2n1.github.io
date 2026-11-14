---
title: "yasm_objfmts(7)"
name: "yasm_objfmts"
section: "7"
letter: "y"
url: "/docs/linux/man/7-yasm_objfmts/"
description: "yasm_objfmts – Yasm Supported Object Formats"
---

<p>yasm_objfmts &#8211; Yasm Supported Object Formats</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>yasm</code> <code>-f&nbsp;<wbr></code><i>objfmt</i> <i>&#8230;</i></dl>
<h2>Description</h2>
<dd>The standard Yasm distribution includes a number of modules for different object formats (Yasm&#8217;s primary output). </p>
<p> The object format is selected on the <code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1) command line by use of the <code>-f </code><i>objfmt</i> command line option.</p>
<h2>Bin</h2>
<p>The &#8220;bin&#8221; object format produces a flat-format, non-relocatable binary file. It is appropriate for producing DOS .COM executables or things like boot blocks. It supports only 3 sections and those sections are written in a predefined order to the output file.</p>
<h2>Coff</h2>
<p>The COFF object format is an older relocatable object format used on older Unix and compatible systems, and also (more recently) on the DJGPP development system for DOS.</p>
<h2>Dbg</h2>
<p>The &#8220;dbg&#8221; object format is not a &#8220;real&#8221; object format; the output file it creates simply describes the sequence of calls made to it by Yasm and the final object and symbol table information in a human-readable text format (that in a normal object format would get processed into that object format&#8217;s particular binary representation). This object format is not intended for real use, but rather for debugging Yasm&#8217;s internals.</p>
<h2>Elf</h2>
<p>The ELF object format really comes in two flavors: &#8220;elf32&#8221; (for 32-bit targets) and &#8220;elf64&#8221; (for 64-bit targets). ELF is a standard object format in common use on modern Unix and compatible systems (e.g. Linux, FreeBSD). ELF has complex support for relocatable and shared objects.</p>
<h2>Macho</h2>
<p>The Mach-O object format really comes in two flavors: &#8220;macho32&#8221; (for 32-bit targets) and &#8220;macho64&#8221; (for 64-bit targets). Mach-O is used as the object format on MacOS X. As Yasm currently only supports x86 and AMD64 instruction sets, it can only generate Mach-O objects for Intel-based Macs.</p>
<h2>Rdf</h2>
<p>The RDOFF2 object format is a simple multi-section format originally designed for NASM. It supports segment references but not WRT references. It was designed primarily for simplicity and has minimalistic headers for ease of loading and linking. A complete toolchain (linker, librarian, and loader) is distributed with NASM.</p>
<h2>Win32</h2>
<p>The Win32 object format produces object files compatible with Microsoft compilers (such as Visual C++) that target the 32-bit x86 Windows platform. The object format itself is an extended version of COFF.</p>
<h2>Win64</h2>
<p>The Win64 object format produces object files compatible with Microsoft compilers that target the 64-bit &#8220;x64&#8221; Windows platform. This format is very similar to the win32 object format, but produces 64-bit objects.</p>
<h2>Xdf</h2>
<p>The XDF object format is essentially a simplified version of COFF. It&#8217;s a multi-section relocatable format that supports 64-bit physical and virtual addresses.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1), <code><a href="/docs/linux/man/7-yasm_arch/">yasm_arch</a></code>(7)</p>
<h2>Author</h2>
<p><code>Peter Johnson</code> &lt;peter [at] tortall.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Peter Johnson</p>
