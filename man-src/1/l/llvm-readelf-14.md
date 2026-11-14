---
title: "llvm-readelf-14(1)"
name: "llvm-readelf-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-readelf-14/"
description: "llvm-readelf – GNU-style LLVM Object Reader"
---

<h2 class="name">NAME</h2>
<p> llvm-readelf &#8211; GNU-style LLVM Object Reader </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-readelf</code> [<i>options</i>] [<i>input…</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-readelf</code> tool displays low-level format-specific information about one or more object files. </p>
<p> If <code>input</code> is “<code>&#8211;</code>”, <code>llvm-readelf</code> reads from standard input. Otherwise, it will read from the specified <code>filenames</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all, -a</code></p>
<dd> Equivalent to specifying all the main display options relevant to the file format.</p>
<dt><code>&#8211;addrsig</code></p>
<dd> Display the address-significance table.</p>
<dt><code>&#8211;arch-specific, -A</code></p>
<dd> Display architecture-specific information, e.g. the ARM attributes section on ARM.</p>
<dt><code>&#8211;bb-addr-map</code></p>
<dd> Display the contents of the basic block address map section(s), which contain the address of each function, along with the relative offset of each basic block.</p>
<dt><code>&#8211;demangle, -C</code></p>
<dd> Display demangled symbol names in the output.</p>
<dt><code>&#8211;dependent-libraries</code></p>
<dd> Display the dependent libraries section.</p>
<dt><code>&#8211;dyn-relocations</code></p>
<dd> Display the dynamic relocation entries.</p>
<dt><code>&#8211;dyn-symbols, &#8211;dyn-syms</code></p>
<dd> Display the dynamic symbol table.</p>
<dt><code>&#8211;dynamic-table, &#8211;dynamic, -d</code></p>
<dd> Display the dynamic table.</p>
<dt><code>&#8211;cg-profile</code></p>
<dd> Display the callgraph profile section.</p>
<dt><code>&#8211;histogram, -I</code></p>
<dd> Display a bucket list histogram for dynamic symbol hash tables.</p>
<dt><code>&#8211;elf-linker-options</code></p>
<dd> Display the linker options section.</p>
<dt><code>&#8211;elf-output-style=&lt;value&gt;</code></p>
<dd> Format ELF information in the specified style. Valid options are <code>LLVM</code>, <code>GNU</code>, and <code>JSON</code>. <code>LLVM</code> output is an expanded and structured format. <code>GNU</code> (the default) output mimics the equivalent GNU <code>readelf</code> output. <code>JSON</code> is JSON formatted output intended for machine consumption.</p>
<dt><code>&#8211;section-groups, -g</code></p>
<dd> Display section groups.</p>
<dt><code>&#8211;expand-relocs</code></p>
<dd> When used with <i>&#8211;relocations</i>, display each relocation in an expanded multi-line format.</p>
<dt><code>&#8211;file-header, -h</code></p>
<dd> Display file headers.</p>
<dt><code>&#8211;gnu-hash-table</code></p>
<dd> Display the GNU hash table for dynamic symbols.</p>
<dt><code>&#8211;hash-symbols</code></p>
<dd> Display the expanded hash table with dynamic symbol data.</p>
<dt><code>&#8211;hash-table</code></p>
<dd> Display the hash table for dynamic symbols.</p>
<dt><code>&#8211;headers, -e</code></p>
<dd> Equivalent to setting: <i>&#8211;file-header</i>, <i>&#8211;program-headers</i>, and <i>&#8211;sections</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a summary of command line options.</p>
<dt><code>&#8211;hex-dump=&lt;section[,section,&#8230;]&gt;, -x</code></p>
<dd> Display the specified section(s) as hexadecimal bytes. <code>section</code> may be a section index or section name.</p>
<dt><code>&#8211;needed-libs</code></p>
<dd> Display the needed libraries.</p>
<dt><code>&#8211;no-demangle</code></p>
<dd> Do not display demangled symbol names in the output. On by default.</p>
<dt><code>&#8211;notes, -n</code></p>
<dd> Display all notes.</p>
<dt><code>&#8211;pretty-print</code></p>
<dd> When used with <i>&#8211;elf-output-style</i>, JSON output will be formatted in a more readable format.</p>
<dt><code>&#8211;program-headers, &#8211;segments, -l</code></p>
<dd> Display the program headers.</p>
<dt><code>&#8211;raw-relr</code></p>
<dd> Do not decode relocations in RELR relocation sections when displaying them.</p>
<dt><code>&#8211;relocations, &#8211;relocs, -r</code></p>
<dd> Display the relocation entries in the file.</p>
<dt><code>&#8211;sections, &#8211;section-headers, -S</code></p>
<dd> Display all sections.</p>
<dt><code>&#8211;section-data</code></p>
<dd> When used with <i>&#8211;sections</i>, display section data for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;section-details, -t</code></p>
<dd> Display all section details. Used as an alternative to <i>&#8211;sections</i>.</p>
<dt><code>&#8211;section-mapping</code></p>
<dd> Display the section to segment mapping.</p>
<dt><code>&#8211;section-relocations</code></p>
<dd> When used with <i>&#8211;sections</i>, display relocations for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;section-symbols</code></p>
<dd> When used with <i>&#8211;sections</i>, display symbols for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;stackmap</code></p>
<dd> Display contents of the stackmap section.</p>
<dt><code>&#8211;stack-sizes</code></p>
<dd> Display the contents of the stack sizes section(s), i.e. pairs of function names and the size of their stack frames. Currently only implemented for GNU style output.</p>
<dt><code>&#8211;string-dump=&lt;section[,section,&#8230;]&gt;, -p</code></p>
<dd> Display the specified section(s) as a list of strings. <code>section</code> may be a section index or section name.</p>
<dt><code>&#8211;symbols, &#8211;syms, -s</code></p>
<dd> Display the symbol table. Also display the dynamic symbol table when using GNU output style for ELF.</p>
<dt><code>&#8211;unwind, -u</code></p>
<dd> Display unwind information.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the version of the <code>llvm-readelf</code> executable.</p>
<dt><code>&#8211;version-info, -V</code></p>
<dd> Display version sections.</p>
<dt><code>&#8211;wide, -W</code></p>
<dd> Ignored for GNU readelf compatibility. The output is already similar to when using -W with GNU readelf.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-readelf</code> returns 0 under normal operation. It returns a non-zero exit code if there were any errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-objdump/">llvm-objdump</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-readobj/">llvm-readobj</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
