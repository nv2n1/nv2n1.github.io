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
<dt><code>&#8211;all, -a</code></dt>
<dd> Equivalent to specifying all the main display options relevant to the file format.</dd>
<dt><code>&#8211;addrsig</code></dt>
<dd> Display the address-significance table.</dd>
<dt><code>&#8211;arch-specific, -A</code></dt>
<dd> Display architecture-specific information, e.g. the ARM attributes section on ARM.</dd>
<dt><code>&#8211;bb-addr-map</code></dt>
<dd> Display the contents of the basic block address map section(s), which contain the address of each function, along with the relative offset of each basic block.</dd>
<dt><code>&#8211;demangle, -C</code></dt>
<dd> Display demangled symbol names in the output.</dd>
<dt><code>&#8211;dependent-libraries</code></dt>
<dd> Display the dependent libraries section.</dd>
<dt><code>&#8211;dyn-relocations</code></dt>
<dd> Display the dynamic relocation entries.</dd>
<dt><code>&#8211;dyn-symbols, &#8211;dyn-syms</code></dt>
<dd> Display the dynamic symbol table.</dd>
<dt><code>&#8211;dynamic-table, &#8211;dynamic, -d</code></dt>
<dd> Display the dynamic table.</dd>
<dt><code>&#8211;cg-profile</code></dt>
<dd> Display the callgraph profile section.</dd>
<dt><code>&#8211;histogram, -I</code></dt>
<dd> Display a bucket list histogram for dynamic symbol hash tables.</dd>
<dt><code>&#8211;elf-linker-options</code></dt>
<dd> Display the linker options section.</dd>
<dt><code>&#8211;elf-output-style=&lt;value&gt;</code></dt>
<dd> Format ELF information in the specified style. Valid options are <code>LLVM</code>, <code>GNU</code>, and <code>JSON</code>. <code>LLVM</code> output is an expanded and structured format. <code>GNU</code> (the default) output mimics the equivalent GNU <code>readelf</code> output. <code>JSON</code> is JSON formatted output intended for machine consumption.</dd>
<dt><code>&#8211;section-groups, -g</code></dt>
<dd> Display section groups.</dd>
<dt><code>&#8211;expand-relocs</code></dt>
<dd> When used with <i>&#8211;relocations</i>, display each relocation in an expanded multi-line format.</dd>
<dt><code>&#8211;file-header, -h</code></dt>
<dd> Display file headers.</dd>
<dt><code>&#8211;gnu-hash-table</code></dt>
<dd> Display the GNU hash table for dynamic symbols.</dd>
<dt><code>&#8211;hash-symbols</code></dt>
<dd> Display the expanded hash table with dynamic symbol data.</dd>
<dt><code>&#8211;hash-table</code></dt>
<dd> Display the hash table for dynamic symbols.</dd>
<dt><code>&#8211;headers, -e</code></dt>
<dd> Equivalent to setting: <i>&#8211;file-header</i>, <i>&#8211;program-headers</i>, and <i>&#8211;sections</i>.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a summary of command line options.</dd>
<dt><code>&#8211;hex-dump=&lt;section[,section,&#8230;]&gt;, -x</code></dt>
<dd> Display the specified section(s) as hexadecimal bytes. <code>section</code> may be a section index or section name.</dd>
<dt><code>&#8211;needed-libs</code></dt>
<dd> Display the needed libraries.</dd>
<dt><code>&#8211;no-demangle</code></dt>
<dd> Do not display demangled symbol names in the output. On by default.</dd>
<dt><code>&#8211;notes, -n</code></dt>
<dd> Display all notes.</dd>
<dt><code>&#8211;pretty-print</code></dt>
<dd> When used with <i>&#8211;elf-output-style</i>, JSON output will be formatted in a more readable format.</dd>
<dt><code>&#8211;program-headers, &#8211;segments, -l</code></dt>
<dd> Display the program headers.</dd>
<dt><code>&#8211;raw-relr</code></dt>
<dd> Do not decode relocations in RELR relocation sections when displaying them.</dd>
<dt><code>&#8211;relocations, &#8211;relocs, -r</code></dt>
<dd> Display the relocation entries in the file.</dd>
<dt><code>&#8211;sections, &#8211;section-headers, -S</code></dt>
<dd> Display all sections.</dd>
<dt><code>&#8211;section-data</code></dt>
<dd> When used with <i>&#8211;sections</i>, display section data for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;section-details, -t</code></dt>
<dd> Display all section details. Used as an alternative to <i>&#8211;sections</i>.</dd>
<dt><code>&#8211;section-mapping</code></dt>
<dd> Display the section to segment mapping.</dd>
<dt><code>&#8211;section-relocations</code></dt>
<dd> When used with <i>&#8211;sections</i>, display relocations for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;section-symbols</code></dt>
<dd> When used with <i>&#8211;sections</i>, display symbols for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;stackmap</code></dt>
<dd> Display contents of the stackmap section.</dd>
<dt><code>&#8211;stack-sizes</code></dt>
<dd> Display the contents of the stack sizes section(s), i.e. pairs of function names and the size of their stack frames. Currently only implemented for GNU style output.</dd>
<dt><code>&#8211;string-dump=&lt;section[,section,&#8230;]&gt;, -p</code></dt>
<dd> Display the specified section(s) as a list of strings. <code>section</code> may be a section index or section name.</dd>
<dt><code>&#8211;symbols, &#8211;syms, -s</code></dt>
<dd> Display the symbol table. Also display the dynamic symbol table when using GNU output style for ELF.</dd>
<dt><code>&#8211;unwind, -u</code></dt>
<dd> Display unwind information.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the version of the <code>llvm-readelf</code> executable.</dd>
<dt><code>&#8211;version-info, -V</code></dt>
<dd> Display version sections.</dd>
<dt><code>&#8211;wide, -W</code></dt>
<dd> Ignored for GNU readelf compatibility. The output is already similar to when using -W with GNU readelf.</dd>
<dt><code>@&lt;FILE&gt;</code></dt>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-readelf</code> returns 0 under normal operation. It returns a non-zero exit code if there were any errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code>llvm-objdump(1)</code>, <code>llvm-readobj(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
