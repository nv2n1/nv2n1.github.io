---
title: "llvm-readobj-14(1)"
name: "llvm-readobj-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-readobj-14/"
description: "llvm-readobj – LLVM Object Reader"
---

<h2 class="name">NAME</h2>
<p> llvm-readobj &#8211; LLVM Object Reader </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-readobj</code> [<i>options</i>] [<i>input…</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>llvm-readobj</code> tool displays low-level format-specific information about one or more object files. </p>
<p> If <code>input</code> is “<code>&#8211;</code>”, <code>llvm-readobj</code> reads from standard input. Otherwise, it will read from the specified <code>filenames</code>.</p>
<h2>DIFFERENCES TO LLVM-READELF</h2>
<p> <code>llvm-readelf</code> is an alias for the <code>llvm-readobj</code> tool with a slightly different command-line interface and output that is GNU compatible. Following is a list of differences between <code>llvm-readelf</code> and <code>llvm-readobj</code>:</p>
<dl>
<dt>&bull;</p>
<dd> <code>llvm-readelf</code> uses <i>GNU</i> for the <i>&#8211;elf-output-style</i> option by default. <code>llvm-readobj</code> uses <i>LLVM</i>.</p>
<dt>&bull;</p>
<dd> <code>llvm-readelf</code> allows single-letter grouped flags (e.g. <code>llvm-readelf -SW</code> is the same as <code>llvm-readelf -S -W</code>). <code>llvm-readobj</code> does not allow grouping.</p>
<dt>&bull;</p>
<dd> <code>llvm-readelf</code> provides <i>-s</i> as an alias for <i>&#8211;symbols</i>, for GNU <code>readelf</code> compatibility, whereas it is an alias for <i>&#8211;section-headers</i> in <code>llvm-readobj</code>.</p>
<dt>&bull;</p>
<dd> <code>llvm-readobj</code> provides <code>-t</code> as an alias for <i>&#8211;symbols</i>. <code>llvm-readelf</code> does not.</p>
<dt>&bull;</p>
<dd> <code>llvm-readobj</code> provides <code>&#8211;sr</code>, <code>&#8211;sd</code>, <code>&#8211;st</code> and <code>&#8211;dt</code> as aliases for <i>&#8211;section-relocations</i>, <i>&#8211;section-data</i>, <i>&#8211;section-symbols</i> and <i>&#8211;dyn-symbols</i> respectively. <code>llvm-readelf</code> does not provide these aliases, to avoid conflicting with grouped flags.</dl>
<h2>GENERAL AND MULTI-FORMAT OPTIONS</h2>
<p> These options are applicable to more than one file format, or are unrelated to file formats.</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd> Equivalent to specifying all the main display options relevant to the file format.</p>
<dt><code>&#8211;addrsig</code></p>
<dd> Display the address-significance table.</p>
<dt><code>&#8211;expand-relocs</code></p>
<dd> When used with <i>&#8211;relocs</i>, display each relocation in an expanded multi-line format.</p>
<dt><code>&#8211;file-header, -h</code></p>
<dd> Display file headers.</p>
<dt><code>&#8211;headers, -e</code></p>
<dd> Equivalent to setting: <i>&#8211;file-header</i>, <i>&#8211;program-headers</i>, and <i>&#8211;sections</i>.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a summary of command line options.</p>
<dt><code>&#8211;hex-dump=&lt;section[,section,&#8230;]&gt;, -x</code></p>
<dd> Display the specified section(s) as hexadecimal bytes. <code>section</code> may be a section index or section name.</p>
<dt><code>&#8211;needed-libs</code></p>
<dd> Display the needed libraries.</p>
<dt><code>&#8211;relocations, &#8211;relocs, -r</code></p>
<dd> Display the relocation entries in the file.</p>
<dt><code>&#8211;sections, &#8211;section-headers, -S</code></p>
<dd> Display all sections.</p>
<dt><code>&#8211;section-data, &#8211;sd</code></p>
<dd> When used with <i>&#8211;sections</i>, display section data for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;section-relocations, &#8211;sr</code></p>
<dd> When used with <i>&#8211;sections</i>, display relocations for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;section-symbols, &#8211;st</code></p>
<dd> When used with <i>&#8211;sections</i>, display symbols for each section shown. This option has no effect for GNU style output.</p>
<dt><code>&#8211;stackmap</code></p>
<dd> Display contents of the stackmap section.</p>
<dt><code>&#8211;string-dump=&lt;section[,section,&#8230;]&gt;, -p</code></p>
<dd> Display the specified section(s) as a list of strings. <code>section</code> may be a section index or section name.</p>
<dt><code>&#8211;string-table</code></p>
<dd> Display contents of the string table.</p>
<dt><code>&#8211;symbols, &#8211;syms, -s</code></p>
<dd> Display the symbol table.</p>
<dt><code>&#8211;unwind, -u</code></p>
<dd> Display unwind information.</p>
<dt><code>&#8211;version</code></p>
<dd> Display the version of the <code>llvm-readobj</code> executable.</p>
<dt><code>@&lt;FILE&gt;</code></p>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dl>
<h2>ELF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the ELF file format.</p>
<dl>
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
<dt><code>&#8211;dyn-symbols, &#8211;dyn-syms, &#8211;dt</code></p>
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
<dd> Format ELF information in the specified style. Valid options are <code>LLVM</code>, <code>GNU</code>, and <code>JSON</code>. <code>LLVM</code> output (the default) is an expanded and structured format. <code>GNU</code> output mimics the equivalent GNU <code>readelf</code> output. <code>JSON</code> is JSON formatted output intended for machine consumption.</p>
<dt><code>&#8211;section-groups, -g</code></p>
<dd> Display section groups.</p>
<dt><code>&#8211;gnu-hash-table</code></p>
<dd> Display the GNU hash table for dynamic symbols.</p>
<dt><code>&#8211;hash-symbols</code></p>
<dd> Display the expanded hash table with dynamic symbol data.</p>
<dt><code>&#8211;hash-table</code></p>
<dd> Display the hash table for dynamic symbols.</p>
<dt><code>&#8211;notes, -n</code></p>
<dd> Display all notes.</p>
<dt><code>&#8211;pretty-print</code></p>
<dd> When used with <i>&#8211;elf-output-style</i>, JSON output will be formatted in a more readable format.</p>
<dt><code>&#8211;program-headers, &#8211;segments, -l</code></p>
<dd> Display the program headers.</p>
<dt><code>&#8211;raw-relr</code></p>
<dd> Do not decode relocations in RELR relocation sections when displaying them.</p>
<dt><code>&#8211;section-mapping</code></p>
<dd> Display the section to segment mapping.</p>
<dt><code>&#8211;stack-sizes</code></p>
<dd> Display the contents of the stack sizes section(s), i.e. pairs of function names and the size of their stack frames. Currently only implemented for GNU style output.</p>
<dt><code>&#8211;version-info, -V</code></p>
<dd> Display version sections.</dl>
<h2>MACH-O SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the Mach-O file format.</p>
<dl>
<dt><code>&#8211;macho-data-in-code</code></p>
<dd> Display the Data in Code command.</p>
<dt><code>&#8211;macho-dsymtab</code></p>
<dd> Display the Dsymtab command.</p>
<dt><code>&#8211;macho-indirect-symbols</code></p>
<dd> Display indirect symbols.</p>
<dt><code>&#8211;macho-linker-options</code></p>
<dd> Display the Mach-O-specific linker options.</p>
<dt><code>&#8211;macho-segment</code></p>
<dd> Display the Segment command.</p>
<dt><code>&#8211;macho-version-min</code></p>
<dd> Display the version min command.</dl>
<h2>PE/COFF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the PE/COFF file format.</p>
<dl>
<dt><code>&#8211;codeview</code></p>
<dd> Display CodeView debug information.</p>
<dt><code>&#8211;codeview-ghash</code></p>
<dd> Enable global hashing for CodeView type stream de-duplication.</p>
<dt><code>&#8211;codeview-merged-types</code></p>
<dd> Display the merged CodeView type stream.</p>
<dt><code>&#8211;codeview-subsection-bytes</code></p>
<dd> Dump raw contents of CodeView debug sections and records.</p>
<dt><code>&#8211;coff-basereloc</code></p>
<dd> Display the .reloc section.</p>
<dt><code>&#8211;coff-debug-directory</code></p>
<dd> Display the debug directory.</p>
<dt><code>&#8211;coff-tls-directory</code></p>
<dd> Display the TLS directory.</p>
<dt><code>&#8211;coff-directives</code></p>
<dd> Display the .drectve section.</p>
<dt><code>&#8211;coff-exports</code></p>
<dd> Display the export table.</p>
<dt><code>&#8211;coff-imports</code></p>
<dd> Display the import table.</p>
<dt><code>&#8211;coff-load-config</code></p>
<dd> Display the load config.</p>
<dt><code>&#8211;coff-resources</code></p>
<dd> Display the .rsrc section.</dl>
<h2>XCOFF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the XCOFF file format.</p>
<dl>
<dt><code>&#8211;auxiliary-header</code></p>
<dd> Display XCOFF Auxiliary header.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-readobj</code> returns 0 under normal operation. It returns a non-zero exit code if there were any errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-objdump/">llvm-objdump</a>(1)</code>, <code><a href="/docs/linux/man/1-llvm-readelf/">llvm-readelf</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
