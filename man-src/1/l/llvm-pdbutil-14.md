---
title: "llvm-pdbutil-14(1)"
name: "llvm-pdbutil-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-pdbutil-14/"
description: "llvm-pdbutil – PDB File forensics and diagnostics"
---

<h2 class="name">NAME</h2>
<p> llvm-pdbutil &#8211; PDB File forensics and diagnostics</p>
<dl>
<dt>&bull;</p>
<dd> <i>Synopsis</i></p>
<dt>&bull;</p>
<dd> <i>Description</i></p>
<dt>&bull;</p>
<dd> <i>Subcommands</i></p>
<dt>&bull;</p>
<dd> <i>pretty</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>Filtering and Sorting Options</i></p>
<dt>&bull;</p>
<dd> <i>Symbol Type Options</i></p>
<dt>&bull;</p>
<dd> <i>Other Options</i></p>
<dt>&bull;</p>
<dd> <i>dump</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>MSF Container Options</i></p>
<dt>&bull;</p>
<dd> <i>Module &amp; File Options</i></p>
<dt>&bull;</p>
<dd> <i>Symbol Options</i></p>
<dt>&bull;</p>
<dd> <i>Type Record Options</i></p>
<dt>&bull;</p>
<dd> <i>Miscellaneous Options</i></p>
<dt>&bull;</p>
<dd> <i>bytes</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>MSF File Options</i></p>
<dt>&bull;</p>
<dd> <i>PDB Stream Options</i></p>
<dt>&bull;</p>
<dd> <i>DBI Stream Options</i></p>
<dt>&bull;</p>
<dd> <i>Module Options</i></p>
<dt>&bull;</p>
<dd> <i>Type Record Options</i></p>
<dt>&bull;</p>
<dd> <i>pdb2yaml</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>yaml2pdb</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></p>
<dt>&bull;</p>
<dd> <i>merge</i></p>
<dt>&bull;</p>
<dd> <i>Summary</i></p>
<dt>&bull;</p>
<dd> <i>Options</i></dl>
<h2>SYNOPSIS</h2>
<p> <code>llvm-pdbutil</code> [<i>subcommand</i>] [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Display types, symbols, CodeView records, and other information from a PDB file, as well as manipulate and create PDB files. <code>llvm-pdbutil</code> is normally used by FileCheck-based tests to test LLVM’s PDB reading and writing functionality, but can also be used for general PDB file investigation and forensics, or as a replacement for cvdump.</p>
<h2>SUBCOMMANDS</h2>
<p> <code>llvm-pdbutil</code> is separated into several subcommands each tailored to a different purpose. A brief summary of each command follows, with more detail in the sections that follow.</p>
<dl>
<dt>&bull;</p>
<dd> <i>pretty</i> &#8211; Dump symbol and type information in a format that tries to look as much like the original source code as possible.</p>
<dt>&bull;</p>
<dd> <i>dump</i> &#8211; Dump low level types and structures from the PDB file, including CodeView records, hash tables, PDB streams, etc.</p>
<dt>&bull;</p>
<dd> <i>bytes</i> &#8211; Dump data from the PDB file’s streams, records, types, symbols, etc as raw bytes.</p>
<dt>&bull;</p>
<dd> <i>yaml2pdb</i> &#8211; Given a yaml description of a PDB file, produce a valid PDB file that matches that description.</p>
<dt>&bull;</p>
<dd> <i>pdb2yaml</i> &#8211; For a given PDB file, produce a YAML description of some or all of the file in a way that the PDB can be reconstructed.</p>
<dt>&bull;</p>
<dd> <i>merge</i> &#8211; Given two PDBs, produce a third PDB that is the result of merging the two input PDBs.</dl>
<h3>pretty</h3>
<p> <code>IMPORTANT:</code> The <code>pretty</code> subcommand is built on the Windows DIA SDK, and as such is not supported on non-Windows platforms. </p>
<p> USAGE: <code>llvm-pdbutil</code> pretty [<i>options</i>] &lt;input PDB file&gt;</p>
<h3>Summary</h3>
<p> The <i>pretty</i> subcommand displays a very high level representation of your program’s debug info. Since it is built on the Windows DIA SDK which is the standard API that Windows tools and debuggers query debug information, it presents a more authoritative view of how a debugger is going to interpret your debug information than a mode which displays low-level CodeView records.</p>
<h3>Options</h3>
<h3>Filtering and Sorting Options</h3>
<p> <code>NOTE:</code> <i>exclude</i> filters take priority over <i>include</i> filters. So if a filter matches both an include and an exclude rule, then it is excluded.</p>
<dl>
<dt><code>-exclude-compilands=&lt;string&gt;</code></p>
<dd> When dumping compilands, compiland source-file contributions, or per-compiland symbols, this option instructs <code>llvm-pdbutil</code> to omit any compilands that match the specified regular expression.</p>
<dt><code>-exclude-symbols=&lt;string&gt;</code></p>
<dd> When dumping global, public, or per-compiland symbols, this option instructs <code>llvm-pdbutil</code> to omit any symbols that match the specified regular expression.</p>
<dt><code>-exclude-types=&lt;string&gt;</code></p>
<dd> When dumping types, this option instructs <code>llvm-pdbutil</code> to omit any types that match the specified regular expression.</p>
<dt><code>-include-compilands=&lt;string&gt;</code></p>
<dd> When dumping compilands, compiland source-file contributions, or per-compiland symbols, limit the initial search to only those compilands that match the specified regular expression.</p>
<dt><code>-include-symbols=&lt;string&gt;</code></p>
<dd> When dumping global, public, or per-compiland symbols, limit the initial search to only those symbols that match the specified regular expression.</p>
<dt><code>-include-types=&lt;string&gt;</code></p>
<dd> When dumping types, limit the initial search to only those types that match the specified regular expression.</p>
<dt><code>-min-class-padding=&lt;uint&gt;</code></p>
<dd> Only display types that have at least the specified amount of alignment padding, accounting for padding in base classes and aggregate field members.</p>
<dt><code>-min-class-padding-imm=&lt;uint&gt;</code></p>
<dd> Only display types that have at least the specified amount of alignment padding, ignoring padding in base classes and aggregate field members.</p>
<dt><code>-min-type-size=&lt;uint&gt;</code></p>
<dd> Only display types T where sizeof(T) is greater than or equal to the specified amount.</p>
<dt><code>-no-compiler-generated</code></p>
<dd> Don’t show compiler generated types and symbols</p>
<dt><code>-no-enum-definitions</code></p>
<dd> When dumping an enum, don’t show the full enum (e.g. the individual enumerator values).</p>
<dt><code>-no-system-libs</code></p>
<dd> Don’t show symbols from system libraries</dl>
<h3>Symbol Type Options</h3>
<dl>
<dt><code>-all</code></p>
<dd> Implies all other options in this category.</p>
<dt><code>-class-definitions=&lt;format&gt;</code></p>
<dd> Displays class definitions in the specified format. </p>
<pre>
=all      - Display all class members including data, constants, typedefs, functions, etc (default)
=layout   - Only display members that contribute to class size.
=none     - Don't display class definitions (e.g. only display the name and base list)
</pre>
<dt><code>-class-order</code></p>
<dd> Displays classes in the specified order. </p>
<pre>
=none            - Undefined / no particular sort order (default)
=name            - Sort classes by name
=size            - Sort classes by size
=padding         - Sort classes by amount of padding
=padding-pct     - Sort classes by percentage of space consumed by padding
=padding-imm     - Sort classes by amount of immediate padding
=padding-pct-imm - Sort classes by percentage of space consumed by immediate padding
</pre>
<dt><code>-class-recurse-depth=&lt;uint&gt;</code></p>
<dd> When dumping class definitions, stop after recursing the specified number of times. The default is 0, which is no limit.</p>
<dt><code>-classes</code></p>
<dd> Display classes</p>
<dt><code>-compilands</code></p>
<dd> Display compilands (e.g. object files)</p>
<dt><code>-enums</code></p>
<dd> Display enums</p>
<dt><code>-externals</code></p>
<dd> Dump external (e.g. exported) symbols</p>
<dt><code>-globals</code></p>
<dd> Dump global symbols</p>
<dt><code>-lines</code></p>
<dd> Dump the mappings between source lines and code addresses.</p>
<dt><code>-module-syms</code></p>
<dd> Display symbols (variables, functions, etc) for each compiland</p>
<dt><code>-sym-types=&lt;types&gt;</code></p>
<dd> Type of symbols to dump when -globals, -externals, or -module-syms is specified. (default all) </p>
<pre>
=thunks - Display thunk symbols
=data   - Display data symbols
=funcs  - Display function symbols
=all    - Display all symbols (default)
</pre>
<dt><code>-symbol-order=&lt;order&gt;</code></p>
<dd> For symbols dumped via the -module-syms, -globals, or -externals options, sort the results in specified order. </p>
<pre>
=none - Undefined / no particular sort order
=name - Sort symbols by name
=size - Sort symbols by size
</pre>
<dt><code>-typedefs</code></p>
<dd> Display typedef types</p>
<dt><code>-types</code></p>
<dd> Display all types (implies -classes, -enums, -typedefs)</dl>
<h3>Other Options</h3>
<dl>
<dt><code>-color-output</code></p>
<dd> Force color output on or off. By default, color if used if outputting to a terminal.</p>
<dt><code>-load-address=&lt;uint&gt;</code></p>
<dd> When displaying relative virtual addresses, assume the process is loaded at the given address and display what would be the absolute address.</dl>
<h3>dump</h3>
<p> USAGE: <code>llvm-pdbutil</code> dump [<i>options</i>] &lt;input PDB file&gt;</p>
<h3>Summary</h3>
<p> The <code>dump</code> subcommand displays low level information about the structure of a PDB file. It is used heavily by LLVM’s testing infrastructure, but can also be used for PDB forensics. It serves a role similar to that of Microsoft’s <i>cvdump</i> tool. </p>
<p> <code>NOTE:</code> The <code>dump</code> subcommand exposes internal details of the file format. As such, the reader should be familiar with /PDB/index before using this command.</p>
<h3>Options</h3>
<h3>MSF Container Options</h3>
<dl>
<dt><code>-streams</code></p>
<dd> dump a summary of all of the streams in the PDB file.</p>
<dt><code>-stream-blocks</code></p>
<dd> In conjunction with <i>-streams</i>, add information to the output about what blocks the specified stream occupies.</p>
<dt><code>-summary</code></p>
<dd> Dump MSF and PDB header information.</dl>
<h3>Module &amp; File Options</h3>
<dl>
<dt><code>-modi=&lt;uint&gt;</code></p>
<dd> For all options that dump information from each module/compiland, limit to the specified module.</p>
<dt><code>-files</code></p>
<dd> Dump the source files that contribute to each displayed module.</p>
<dt><code>-il</code></p>
<dd> Dump inlinee line information (DEBUG_S_INLINEELINES CodeView subsection)</p>
<dt><code>-l</code></p>
<dd> Dump line information (DEBUG_S_LINES CodeView subsection)</p>
<dt><code>-modules</code></p>
<dd> Dump compiland information</p>
<dt><code>-xme</code></p>
<dd> Dump cross module exports (DEBUG_S_CROSSSCOPEEXPORTS CodeView subsection)</p>
<dt><code>-xmi</code></p>
<dd> Dump cross module imports (DEBUG_S_CROSSSCOPEIMPORTS CodeView subsection)</dl>
<h3>Symbol Options</h3>
<dl>
<dt><code>-globals</code></p>
<dd> dump global symbol records</p>
<dt><code>-global-extras</code></p>
<dd> dump additional information about the globals, such as hash buckets and hash values.</p>
<dt><code>-publics</code></p>
<dd> dump public symbol records</p>
<dt><code>-public-extras</code></p>
<dd> dump additional information about the publics, such as hash buckets and hash values.</p>
<dt><code>-symbols</code></p>
<dd> dump symbols (functions, variables, etc) for each module dumped.</p>
<dt><code>-sym-data</code></p>
<dd> For each symbol record dumped as a result of the <i>-symbols</i> option, display the full bytes of the record in binary as well.</dl>
<h3>Type Record Options</h3>
<dl>
<dt><code>-types</code></p>
<dd> Dump CodeView type records from TPI stream</p>
<dt><code>-type-extras</code></p>
<dd> Dump additional information from the TPI stream, such as hashes and the type index offsets array.</p>
<dt><code>-type-data</code></p>
<dd> For each type record dumped, display the full bytes of the record in binary as well.</p>
<dt><code>-type-index=&lt;uint&gt;</code></p>
<dd> Only dump types with the specified type index.</p>
<dt><code>-ids</code></p>
<dd> Dump CodeView type records from IPI stream.</p>
<dt><code>-id-extras</code></p>
<dd> Dump additional information from the IPI stream, such as hashes and the type index offsets array.</p>
<dt><code>-id-data</code></p>
<dd> For each ID record dumped, display the full bytes of the record in binary as well.</p>
<dt><code>-id-index=&lt;uint&gt;</code></p>
<dd> only dump ID records with the specified hexadecimal type index.</p>
<dt><code>-dependents</code></p>
<dd> When used in conjunction with <i>-type-index</i> or <i>-id-index</i>, dumps the entire dependency graph for the specified index instead of just the single record with the specified index. For example, if type index 0x4000 is a function whose return type has index 0x3000, and you specify <i>-dependents=0x4000</i>, then this would dump both records (as well as any other dependents in the tree).</dl>
<h3>Miscellaneous Options</h3>
<dl>
<dt><code>-all</code></p>
<dd> Implies most other options.</p>
<dt><code>-section-contribs</code></p>
<dd> Dump section contributions.</p>
<dt><code>-section-headers</code></p>
<dd> Dump image section headers.</p>
<dt><code>-section-map</code></p>
<dd> Dump section map.</p>
<dt><code>-string-table</code></p>
<dd> Dump PDB string table.</dl>
<h3>bytes</h3>
<p> USAGE: <code>llvm-pdbutil</code> bytes [<i>options</i>] &lt;input PDB file&gt;</p>
<h3>Summary</h3>
<p> Like the <code>dump</code> subcommand, the <code>bytes</code> subcommand displays low level information about the structure of a PDB file, but it is used for even deeper forensics. The <code>bytes</code> subcommand finds various structures in a PDB file based on the command line options specified, and dumps them in hex. Someone working on support for emitting PDBs would use this heavily, for example, to compare one PDB against another PDB to ensure byte-for-byte compatibility. It is not enough to simply compare the bytes of an entire file, or an entire stream because it’s perfectly fine for the same structure to exist at different locations in two different PDBs, and “finding” the structure is half the battle.</p>
<h3>Options</h3>
<h3>MSF File Options</h3>
<dl>
<dt><code>-block-range=&lt;start[-end]&gt;</code></p>
<dd> Dump binary data from specified range of MSF file blocks.</p>
<dt><code>-byte-range=&lt;start[-end]&gt;</code></p>
<dd> Dump binary data from specified range of bytes in the file.</p>
<dt><code>-fpm</code></p>
<dd> Dump the MSF free page map.</p>
<dt><code>-stream-data=&lt;string&gt;</code></p>
<dd> Dump binary data from the specified streams. Format is SN[:Start][@Size]. For example, <i>-stream-data=7:3@12</i> dumps 12 bytes from stream 7, starting at offset 3 in the stream.</dl>
<h3>PDB Stream Options</h3>
<dl>
<dt><code>-name-map</code></p>
<dd> Dump bytes of PDB Name Map</dl>
<h3>DBI Stream Options</h3>
<dl>
<dt><code>-ec</code></p>
<dd> Dump the edit and continue map substream of the DBI stream.</p>
<dt><code>-files</code></p>
<dd> Dump the file info substream of the DBI stream.</p>
<dt><code>-modi</code></p>
<dd> Dump the modi substream of the DBI stream.</p>
<dt><code>-sc</code></p>
<dd> Dump section contributions substream of the DBI stream.</p>
<dt><code>-sm</code></p>
<dd> Dump the section map from the DBI stream.</p>
<dt><code>-type-server</code></p>
<dd> Dump the type server map from the DBI stream.</dl>
<h3>Module Options</h3>
<dl>
<dt><code>-mod=&lt;uint&gt;</code></p>
<dd> Limit all options in this category to the specified module index. By default, options in this category will dump bytes from all modules.</p>
<dt><code>-chunks</code></p>
<dd> Dump the bytes of each module’s C13 debug subsection.</p>
<dt><code>-split-chunks</code></p>
<dd> When specified with <i>-chunks</i>, split the C13 debug subsection into a separate chunk for each subsection type, and dump them separately.</p>
<dt><code>-syms</code></p>
<dd> Dump the symbol record substream from each module.</dl>
<h3>Type Record Options</h3>
<dl>
<dt><code>-id=&lt;uint&gt;</code></p>
<dd> Dump the record from the IPI stream with the given type index.</p>
<dt><code>-type=&lt;uint&gt;</code></p>
<dd> Dump the record from the TPI stream with the given type index.</dl>
<h3>pdb2yaml</h3>
<p> USAGE: <code>llvm-pdbutil</code> pdb2yaml [<i>options</i>] &lt;input PDB file&gt;</p>
<h3>Summary</h3>
<h3>Options</h3>
<h3>yaml2pdb</h3>
<p> USAGE: <code>llvm-pdbutil</code> yaml2pdb [<i>options</i>] &lt;input YAML file&gt;</p>
<h3>Summary</h3>
<p> Generate a PDB file from a YAML description. The YAML syntax is not described here. Instead, use <i>llvm-pdbutil pdb2yaml</i> and examine the output for an example starting point.</p>
<h3>Options</h3>
<dl>
<dt><code>-pdb=&lt;file-name&gt;</code></p>
<dd>
<p> Write the resulting PDB to the specified file.</dl>
<h3>merge</h3>
<p> USAGE: <code>llvm-pdbutil</code> merge [<i>options</i>] &lt;input PDB file 1&gt; &lt;input PDB file 2&gt;</p>
<h3>Summary</h3>
<p> Merge two PDB files into a single file.</p>
<h3>Options</h3>
<dl>
<dt><code>-pdb=&lt;file-name&gt;</code></p>
<dd>
<p> Write the resulting PDB to the specified file.</dl>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
