---

title: "llvm-readobj-14(1)"
name: "llvm-readobj-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-readobj-14/"
description: "llvm-readobj – LLVM Object Reader"
---

<p> <code>llvm-readobj</code> [<i>options</i>] [<i>input…</i>]</p>
<p> The <code>llvm-readobj</code> tool displays low-level format-specific information about one or more object files. </p>
<p> If <code>input</code> is “<code>&#8211;</code>”, <code>llvm-readobj</code> reads from standard input. Otherwise, it will read from the specified <code>filenames</code>.</p>
<h2>DIFFERENCES TO LLVM-READELF</h2>
<p> <code>llvm-readelf</code> is an alias for the <code>llvm-readobj</code> tool with a slightly different command-line interface and output that is GNU compatible. Following is a list of differences between <code>llvm-readelf</code> and <code>llvm-readobj</code>:</p>
<dl>
<dt>&bull;</dt>
<dd> <code>llvm-readelf</code> uses <i>GNU</i> for the <i>&#8211;elf-output-style</i> option by default. <code>llvm-readobj</code> uses <i>LLVM</i>.</dd>
<dt>&bull;</dt>
<dd> <code>llvm-readelf</code> allows single-letter grouped flags (e.g. <code>llvm-readelf -SW</code> is the same as <code>llvm-readelf -S -W</code>). <code>llvm-readobj</code> does not allow grouping.</dd>
<dt>&bull;</dt>
<dd> <code>llvm-readelf</code> provides <i>-s</i> as an alias for <i>&#8211;symbols</i>, for GNU <code>readelf</code> compatibility, whereas it is an alias for <i>&#8211;section-headers</i> in <code>llvm-readobj</code>.</dd>
<dt>&bull;</dt>
<dd> <code>llvm-readobj</code> provides <code>-t</code> as an alias for <i>&#8211;symbols</i>. <code>llvm-readelf</code> does not.</dd>
<dt>&bull;</dt>
<dd> <code>llvm-readobj</code> provides <code>&#8211;sr</code>, <code>&#8211;sd</code>, <code>&#8211;st</code> and <code>&#8211;dt</code> as aliases for <i>&#8211;section-relocations</i>, <i>&#8211;section-data</i>, <i>&#8211;section-symbols</i> and <i>&#8211;dyn-symbols</i> respectively. <code>llvm-readelf</code> does not provide these aliases, to avoid conflicting with grouped flags.</dd></dl>
<h2>GENERAL AND MULTI-FORMAT OPTIONS</h2>
<p> These options are applicable to more than one file format, or are unrelated to file formats.</p>
<dl>
<dt><code>&#8211;all</code></dt>
<dd> Equivalent to specifying all the main display options relevant to the file format.</dd>
<dt><code>&#8211;addrsig</code></dt>
<dd> Display the address-significance table.</dd>
<dt><code>&#8211;expand-relocs</code></dt>
<dd> When used with <i>&#8211;relocs</i>, display each relocation in an expanded multi-line format.</dd>
<dt><code>&#8211;file-header, -h</code></dt>
<dd> Display file headers.</dd>
<dt><code>&#8211;headers, -e</code></dt>
<dd> Equivalent to setting: <i>&#8211;file-header</i>, <i>&#8211;program-headers</i>, and <i>&#8211;sections</i>.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a summary of command line options.</dd>
<dt><code>&#8211;hex-dump=&lt;section[,section,&#8230;]&gt;, -x</code></dt>
<dd> Display the specified section(s) as hexadecimal bytes. <code>section</code> may be a section index or section name.</dd>
<dt><code>&#8211;needed-libs</code></dt>
<dd> Display the needed libraries.</dd>
<dt><code>&#8211;relocations, &#8211;relocs, -r</code></dt>
<dd> Display the relocation entries in the file.</dd>
<dt><code>&#8211;sections, &#8211;section-headers, -S</code></dt>
<dd> Display all sections.</dd>
<dt><code>&#8211;section-data, &#8211;sd</code></dt>
<dd> When used with <i>&#8211;sections</i>, display section data for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;section-relocations, &#8211;sr</code></dt>
<dd> When used with <i>&#8211;sections</i>, display relocations for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;section-symbols, &#8211;st</code></dt>
<dd> When used with <i>&#8211;sections</i>, display symbols for each section shown. This option has no effect for GNU style output.</dd>
<dt><code>&#8211;stackmap</code></dt>
<dd> Display contents of the stackmap section.</dd>
<dt><code>&#8211;string-dump=&lt;section[,section,&#8230;]&gt;, -p</code></dt>
<dd> Display the specified section(s) as a list of strings. <code>section</code> may be a section index or section name.</dd>
<dt><code>&#8211;string-table</code></dt>
<dd> Display contents of the string table.</dd>
<dt><code>&#8211;symbols, &#8211;syms, -s</code></dt>
<dd> Display the symbol table.</dd>
<dt><code>&#8211;unwind, -u</code></dt>
<dd> Display unwind information.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Display the version of the <code>llvm-readobj</code> executable.</dd>
<dt><code>@&lt;FILE&gt;</code></dt>
<dd> Read command-line options from response file <i>&lt;FILE&gt;</i>.</dd></dl>
<h2>ELF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the ELF file format.</p>
<dl>
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
<dt><code>&#8211;dyn-symbols, &#8211;dyn-syms, &#8211;dt</code></dt>
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
<dd> Format ELF information in the specified style. Valid options are <code>LLVM</code>, <code>GNU</code>, and <code>JSON</code>. <code>LLVM</code> output (the default) is an expanded and structured format. <code>GNU</code> output mimics the equivalent GNU <code>readelf</code> output. <code>JSON</code> is JSON formatted output intended for machine consumption.</dd>
<dt><code>&#8211;section-groups, -g</code></dt>
<dd> Display section groups.</dd>
<dt><code>&#8211;gnu-hash-table</code></dt>
<dd> Display the GNU hash table for dynamic symbols.</dd>
<dt><code>&#8211;hash-symbols</code></dt>
<dd> Display the expanded hash table with dynamic symbol data.</dd>
<dt><code>&#8211;hash-table</code></dt>
<dd> Display the hash table for dynamic symbols.</dd>
<dt><code>&#8211;notes, -n</code></dt>
<dd> Display all notes.</dd>
<dt><code>&#8211;pretty-print</code></dt>
<dd> When used with <i>&#8211;elf-output-style</i>, JSON output will be formatted in a more readable format.</dd>
<dt><code>&#8211;program-headers, &#8211;segments, -l</code></dt>
<dd> Display the program headers.</dd>
<dt><code>&#8211;raw-relr</code></dt>
<dd> Do not decode relocations in RELR relocation sections when displaying them.</dd>
<dt><code>&#8211;section-mapping</code></dt>
<dd> Display the section to segment mapping.</dd>
<dt><code>&#8211;stack-sizes</code></dt>
<dd> Display the contents of the stack sizes section(s), i.e. pairs of function names and the size of their stack frames. Currently only implemented for GNU style output.</dd>
<dt><code>&#8211;version-info, -V</code></dt>
<dd> Display version sections.</dd></dl>
<h2>MACH-O SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the Mach-O file format.</p>
<dl>
<dt><code>&#8211;macho-data-in-code</code></dt>
<dd> Display the Data in Code command.</dd>
<dt><code>&#8211;macho-dsymtab</code></dt>
<dd> Display the Dsymtab command.</dd>
<dt><code>&#8211;macho-indirect-symbols</code></dt>
<dd> Display indirect symbols.</dd>
<dt><code>&#8211;macho-linker-options</code></dt>
<dd> Display the Mach-O-specific linker options.</dd>
<dt><code>&#8211;macho-segment</code></dt>
<dd> Display the Segment command.</dd>
<dt><code>&#8211;macho-version-min</code></dt>
<dd> Display the version min command.</dd></dl>
<h2>PE/COFF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the PE/COFF file format.</p>
<dl>
<dt><code>&#8211;codeview</code></dt>
<dd> Display CodeView debug information.</dd>
<dt><code>&#8211;codeview-ghash</code></dt>
<dd> Enable global hashing for CodeView type stream de-duplication.</dd>
<dt><code>&#8211;codeview-merged-types</code></dt>
<dd> Display the merged CodeView type stream.</dd>
<dt><code>&#8211;codeview-subsection-bytes</code></dt>
<dd> Dump raw contents of CodeView debug sections and records.</dd>
<dt><code>&#8211;coff-basereloc</code></dt>
<dd> Display the .reloc section.</dd>
<dt><code>&#8211;coff-debug-directory</code></dt>
<dd> Display the debug directory.</dd>
<dt><code>&#8211;coff-tls-directory</code></dt>
<dd> Display the TLS directory.</dd>
<dt><code>&#8211;coff-directives</code></dt>
<dd> Display the .drectve section.</dd>
<dt><code>&#8211;coff-exports</code></dt>
<dd> Display the export table.</dd>
<dt><code>&#8211;coff-imports</code></dt>
<dd> Display the import table.</dd>
<dt><code>&#8211;coff-load-config</code></dt>
<dd> Display the load config.</dd>
<dt><code>&#8211;coff-resources</code></dt>
<dd> Display the .rsrc section.</dd></dl>
<h2>XCOFF SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for the XCOFF file format.</p>
<dl>
<dt><code>&#8211;auxiliary-header</code></dt>
<dd> Display XCOFF Auxiliary header.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-readobj</code> returns 0 under normal operation. It returns a non-zero exit code if there were any errors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-nm/">llvm-nm</a>(1)</code>, <code>llvm-objdump(1)</code>, <code>llvm-readelf(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
