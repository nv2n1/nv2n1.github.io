---
title: "yasm_dbgfmts(7)"
name: "yasm_dbgfmts"
section: "7"
letter: "y"
url: "/docs/linux/man/7-yasm_dbgfmts/"
description: "yasm_dbgfmts – Yasm Supported Debugging Formats"
---

<p>yasm_dbgfmts &#8211; Yasm Supported Debugging Formats</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>yasm</code> <code>-g&nbsp;<wbr></code><i>dbgfmt</i> <i>&#8230;</i></dl>
<h2>Description</h2>
<dd>The standard Yasm distribution includes a number of modules for different debugging formats. The debugging information is embedded into the object file. Use of a non-&#8220;null&#8221; debug format also causes Yasm to output all symbols to the object file (including local symbols). </p>
<p> The debug format is selected on the <code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1) command line by use of the <code>-g </code><i>dbgfmt</i> command line option.</p>
<h2>Cv8</h2>
<p>The CV8 debug format is used by Microsoft Visual Studio 2005 (version 8.0) and is completely undocumented, although it bears strong similarities to earlier CodeView formats. Yasm&#8217;s support for the CV8 debug format is currently limited to generating assembly-level line number information (to allow some level of source-level debugging). The CV8 debug information is stored in the .debug$S and .debug$T sections of the Win64 object file.</p>
<h2>Dwarf2</h2>
<p>The DWARF 2 debug format is a complex, well-documented standard for debugging information. It was created to overcome shortcomings in STABS, allowing for much more detailed and compact descriptions of data structures, data variable movement, and complex language structures such as in C++. The debugging information is stored in sections (just like normal program sections) in the object file. Yasm supports full pass-through of DWARF2 debugging information (e.g. from a C++ compiler), and can also generate assembly-level line number information.</p>
<h2>Null</h2>
<p>The &#8220;null&#8221; debug format is a placeholder; it adds no debugging information to the output file.</p>
<h2>Stabs</h2>
<p>The STABS debug format is a poorly documented, semi-standard format for debugging information in COFF and ELF object files. The debugging information is stored as part of the object file&#8217;s symbol table and thus is limited in complexity and scope. Despite this, STABS is a common debugging format on older Unix and compatible systems, as well as DJGPP.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1), <code><a href="/docs/linux/man/7-yasm_objfmts/">yasm_objfmts</a></code>(7)</p>
<h2>Author</h2>
<p><code>Peter Johnson</code> &lt;peter [at] tortall.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 Peter Johnson</p>
