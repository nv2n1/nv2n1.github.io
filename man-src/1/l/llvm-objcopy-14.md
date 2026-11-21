---
title: "llvm-objcopy-14(1)"
name: "llvm-objcopy-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-objcopy-14/"
description: "llvm-objcopy – object copying and editing tool"
---

<h2>SYNOPSIS</h2>
<p> <code>llvm-objcopy</code> [<i>options</i>] <i>input</i> [<i>output</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-objcopy</code> is a tool to copy and manipulate objects. In basic usage, it makes a semantic copy of the input to the output. If any options are specified, the output may be modified along the way, e.g. by removing sections. </p>
<p> If no output file is specified, the input file is modified in-place. If “-” is specified for the input file, the input is read from the program’s standard input stream. If “-” is specified for the output file, the output is written to the standard output stream of the program. </p>
<p> If the input is an archive, any requested operations will be applied to each archive member individually. </p>
<p> The tool is still in active development, but in most scenarios it works as a drop-in replacement for GNU’s <code>objcopy</code>.</p>
<h2>GENERIC AND CROSS-PLATFORM OPTIONS</h2>
<p> The following options are either agnostic of the file format, or apply to multiple file formats.</p>
<dl>
<dt><code>&#8211;add-gnu-debuglink &lt;debug-file&gt;</code></dt>
<dd> Add a .gnu_debuglink section for <code>&lt;debug-file&gt;</code> to the output.</dd>
<dt><code>&#8211;add-section &lt;section=file&gt;</code></dt>
<dd> Add a section named <code>&lt;section&gt;</code> with the contents of <code>&lt;file&gt;</code> to the output. For ELF objects the section will be of type <i>SHT_NOTE</i>, if the name starts with “.note”. Otherwise, it will have type <i>SHT_PROGBITS</i>. Can be specified multiple times to add multiple sections. </dd>
<p> For MachO objects, <code>&lt;section&gt;</code> must be formatted as <code>&lt;segment name&gt;,&lt;section name&gt;</code>.</p>
<dt><code>&#8211;binary-architecture &lt;arch&gt;, -B</code></dt>
<dd> Ignored for compatibility.</dd>
<dt><code>&#8211;disable-deterministic-archives, -U</code></dt>
<dd> Use real values for UIDs, GIDs and timestamps when updating archive member headers.</dd>
<dt><code>&#8211;discard-all, -x</code></dt>
<dd> Remove most local symbols from the output. Different file formats may limit this to a subset of the local symbols. For example, file and section symbols in ELF objects will not be discarded. Additionally, remove all debug sections.</dd>
<dt><code>&#8211;dump-section &lt;section&gt;=&lt;file&gt;</code></dt>
<dd> Dump the contents of section <code>&lt;section&gt;</code> into the file <code>&lt;file&gt;</code>. Can be specified multiple times to dump multiple sections to different files. <code>&lt;file&gt;</code> is unrelated to the input and output files provided to <code>llvm-objcopy</code> and as such the normal copying and editing operations will still be performed. No operations are performed on the sections prior to dumping them. </dd>
<p> For MachO objects, <code>&lt;section&gt;</code> must be formatted as <code>&lt;segment name&gt;,&lt;section name&gt;</code>.</p>
<dt><code>&#8211;enable-deterministic-archives, -D</code></dt>
<dd> Enable deterministic mode when copying archives, i.e. use 0 for archive member header UIDs, GIDs and timestamp fields. On by default.</dd>
<dt><code>&#8211;help, -h</code></dt>
<dd> Print a summary of command line options.</dd>
<dt><code>&#8211;only-keep-debug</code></dt>
<dd> Produce a debug file as the output that only preserves contents of sections useful for debugging purposes. </dd>
<p> For ELF objects, this removes the contents of <i>SHF_ALLOC</i> sections that are not <i>SHT_NOTE</i> by making them <i>SHT_NOBITS</i> and shrinking the program headers where possible.</p>
<dt><code>&#8211;only-section &lt;section&gt;, -j</code></dt>
<dd> Remove all sections from the output, except for sections named <code>&lt;section&gt;</code>. Can be specified multiple times to keep multiple sections. </dd>
<p> For MachO objects, <code>&lt;section&gt;</code> must be formatted as <code>&lt;segment name&gt;,&lt;section name&gt;</code>.</p>
<dt><code>&#8211;redefine-sym &lt;old&gt;=&lt;new&gt;</code></dt>
<dd> Rename symbols called <code>&lt;old&gt;</code> to <code>&lt;new&gt;</code> in the output. Can be specified multiple times to rename multiple symbols.</dd>
<dt><code>&#8211;redefine-syms &lt;filename&gt;</code></dt>
<dd> Rename symbols in the output as described in the file <code>&lt;filename&gt;</code>. In the file, each line represents a single symbol to rename, with the old name and new name separated by whitespace. Leading and trailing whitespace is ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;regex</code></dt>
<dd> If specified, symbol and section names specified by other switches are treated as extended POSIX regular expression patterns.</dd>
<dt><code>&#8211;remove-section &lt;section&gt;, -R</code></dt>
<dd> Remove the specified section from the output. Can be specified multiple times to remove multiple sections simultaneously. </dd>
<p> For MachO objects, <code>&lt;section&gt;</code> must be formatted as <code>&lt;segment name&gt;,&lt;section name&gt;</code>.</p>
<dt><code>&#8211;set-section-alignment &lt;section&gt;=&lt;align&gt;</code></dt>
<dd> Set the alignment of section <code>&lt;section&gt;</code> to <i>&lt;align&gt;`</i>. Can be specified multiple times to update multiple sections.</dd>
<dt><code>&#8211;set-section-flags &lt;section&gt;=&lt;flag&gt;[,&lt;flag&gt;,&#8230;]</code></dt>
<dd> Set section properties in the output of section <code>&lt;section&gt;</code> based on the specified <code>&lt;flag&gt;</code> values. Can be specified multiple times to update multiple sections. </dd>
<p> Supported flag names are <i>alloc</i>, <i>load</i>, <i>noload</i>, <i>readonly</i>, <i>exclude</i>, <i>debug</i>, <i>code</i>, <i>data</i>, <i>rom</i>, <i>share</i>, <i>contents</i>, <i>merge</i> and <i>strings</i>. Not all flags are meaningful for all object file formats. </p>
<p> For ELF objects, the flags have the following effects:</p>
<dt>&bull;</dt>
<dd> <i>alloc</i> = add the <i>SHF_ALLOC</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>load</i> = if the section has <i>SHT_NOBITS</i> type, mark it as a <i>SHT_PROGBITS</i> section.</dd>
<dt>&bull;</dt>
<dd> <i>readonly</i> = if this flag is not specified, add the <i>SHF_WRITE</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>exclude</i> = add the <i>SHF_EXCLUDE</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>code</i> = add the <i>SHF_EXECINSTR</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>merge</i> = add the <i>SHF_MERGE</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>strings</i> = add the <i>SHF_STRINGS</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>contents</i> = if the section has <i>SHT_NOBITS</i> type, mark it as a <i>SHT_PROGBITS</i> section. </dd>
<p> For COFF objects, the flags have the following effects:</p>
<dt>&bull;</dt>
<dd> <i>alloc</i> = add the <i>IMAGE_SCN_CNT_UNINITIALIZED_DATA</i> and <i>IMAGE_SCN_MEM_READ</i> flags, unless the <i>load</i> flag is specified.</dd>
<dt>&bull;</dt>
<dd> <i>noload</i> = add the <i>IMAGE_SCN_LNK_REMOVE</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt>&bull;</dt>
<dd> <i>readonly</i> = if this flag is not specified, add the <i>IMAGE_SCN_MEM_WRITE</i> flag.</dd>
<dt>&bull;</dt>
<dd> <i>exclude</i> = add the <i>IMAGE_SCN_LNK_REMOVE</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt>&bull;</dt>
<dd> <i>debug</i> = add the <i>IMAGE_SCN_CNT_INITIALIZED_DATA</i>, <i>IMAGE_SCN_MEM_DISCARDABLE</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt>&bull;</dt>
<dd> <i>code</i> = add the <i>IMAGE_SCN_CNT_CODE</i>, <i>IMAGE_SCN_MEM_EXECUTE</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt>&bull;</dt>
<dd> <i>data</i> = add the <i>IMAGE_SCN_CNT_INITIALIZED_DATA</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt>&bull;</dt>
<dd> <i>share</i> = add the <i>IMAGE_SCN_MEM_SHARED</i> and <i>IMAGE_SCN_MEM_READ</i> flags.</dd>
<dt><code>&#8211;strip-all-gnu</code></dt>
<dd> Remove all symbols, debug sections and relocations from the output. This option is equivalent to GNU <code>objcopy</code>’s <code>&#8211;strip-all</code> switch.</dd>
<dt><code>&#8211;strip-all, -S</code></dt>
<dd> For ELF objects, remove from the output all symbols and non-alloc sections not within segments, except for .gnu.warning, .ARM.attribute sections and the section name table. </dd>
<p> For COFF and Mach-O objects, remove all symbols, debug sections, and relocations from the output.</p>
<dt><code>&#8211;strip-debug, -g</code></dt>
<dd> Remove all debug sections from the output.</dd>
<dt><code>&#8211;strip-symbol &lt;symbol&gt;, -N</code></dt>
<dd> Remove all symbols named <code>&lt;symbol&gt;</code> from the output. Can be specified multiple times to remove multiple symbols.</dd>
<dt><code>&#8211;strip-symbols &lt;filename&gt;</code></dt>
<dd> Remove all symbols whose names appear in the file <code>&lt;filename&gt;</code>, from the output. In the file, each line represents a single symbol name, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;strip-unneeded-symbol &lt;symbol&gt;</code></dt>
<dd> Remove from the output all symbols named <code>&lt;symbol&gt;</code> that are local or undefined and are not required by any relocation.</dd>
<dt><code>&#8211;strip-unneeded-symbols &lt;filename&gt;</code></dt>
<dd> Remove all symbols whose names appear in the file <code>&lt;filename&gt;</code>, from the output, if they are local or undefined and are not required by any relocation. In the file, each line represents a single symbol name, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;strip-unneeded</code></dt>
<dd> Remove from the output all local or undefined symbols that are not required by relocations. Also remove all debug sections.</dd>
<dt><code>&#8211;version, -V</code></dt>
<dd> Display the version of the <code>llvm-objcopy</code> executable.</dd>
<dt><code>&#8211;wildcard, -w</code></dt>
<dd> Allow wildcard syntax for symbol-related flags. On by default for section-related flags. Incompatible with –regex. </dd>
<p> Wildcard syntax allows the following special symbols: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> Character </td>
<td> Meaning </td>
<td> Equivalent
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>*</code> </td>
<td> Any number of characters </td>
<td> <code>.*</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>?</code> </td>
<td> Any single character </td>
<td> <code>.</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>\</code> </td>
<td> Escape the next character </td>
<td> <code>\</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>[a-z]</code> </td>
<td> Character class </td>
<td> <code>[a-z]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>[!a-z]</code>, <code>[^a-z]</code> </td>
<td> Negated character class </td>
<td> <code>[^a-z]</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p></center> </p>
<p> Additionally, starting a wildcard with ‘!’ will prevent a match, even if another flag matches. For example <code>-w -N &#8216;*&#8217; -N &#8216;!x&#8217;</code> will strip all symbols except for <code>x</code>. </p>
<p> The order of wildcards does not matter. For example, <code>-w -N &#8216;*&#8217; -N &#8216;!x&#8217;</code> is the same as <code>-w -N &#8216;!x&#8217; -N &#8216;*&#8217;</code>.</p>
<dt><code>@&lt;FILE&gt;</code></dt>
<dd> Read command-line options and commands from response file <i>&lt;FILE&gt;</i>.</dd></dl>
<h2>ELF-SPECIFIC OPTIONS</h2>
<p> The following options are implemented only for ELF objects. If used with other objects, <code>llvm-objcopy</code> will either emit an error or silently ignore them.</p>
<dl>
<dt><code>&#8211;add-symbol &lt;name&gt;=[&lt;section&gt;:]&lt;value&gt;[,&lt;flags&gt;]</code></dt>
<dd> Add a new symbol called <code>&lt;name&gt;</code> to the output symbol table, in the section named <code>&lt;section&gt;</code>, with value <code>&lt;value&gt;</code>. If <code>&lt;section&gt;</code> is not specified, the symbol is added as an absolute symbol. The <code>&lt;flags&gt;</code> affect the symbol properties. Accepted values are:</dd>
<dt>&bull;</dt>
<dd> <i>global</i> = the symbol will have global binding.</dd>
<dt>&bull;</dt>
<dd> <i>local</i> = the symbol will have local binding.</dd>
<dt>&bull;</dt>
<dd> <i>weak</i> = the symbol will have weak binding.</dd>
<dt>&bull;</dt>
<dd> <i>default</i> = the symbol will have default visibility.</dd>
<dt>&bull;</dt>
<dd> <i>hidden</i> = the symbol will have hidden visibility.</dd>
<dt>&bull;</dt>
<dd> <i>protected</i> = the symbol will have protected visibility.</dd>
<dt>&bull;</dt>
<dd> <i>file</i> = the symbol will be an <i>STT_FILE</i> symbol.</dd>
<dt>&bull;</dt>
<dd> <i>section</i> = the symbol will be an <i>STT_SECTION</i> symbol.</dd>
<dt>&bull;</dt>
<dd> <i>object</i> = the symbol will be an <i>STT_OBJECT</i> symbol.</dd>
<dt>&bull;</dt>
<dd> <i>function</i> = the symbol will be an <i>STT_FUNC</i> symbol.</dd>
<dt>&bull;</dt>
<dd> <i>indirect-function</i> = the symbol will be an <i>STT_GNU_IFUNC</i> symbol. </dd>
<p> Additionally, the following flags are accepted but ignored: <i>debug</i>, <i>constructor</i>, <i>warning</i>, <i>indirect</i>, <i>synthetic</i>, <i>unique-object</i>, <i>before</i>. </p>
<p> Can be specified multiple times to add multiple symbols.</p>
<dt><code>&#8211;allow-broken-links</code></dt>
<dd> Allow <code>llvm-objcopy</code> to remove sections even if it would leave invalid section references. Any invalid sh_link fields will be set to zero.</dd>
<dt><code>&#8211;change-start &lt;incr&gt;, &#8211;adjust-start</code></dt>
<dd> Add <code>&lt;incr&gt;</code> to the program’s start address. Can be specified multiple times, in which case the values will be applied cumulatively.</dd>
<dt><code>&#8211;compress-debug-sections [&lt;style&gt;]</code></dt>
<dd> Compress DWARF debug sections in the output, using the specified style. Supported styles are <i>zlib-gnu</i> and <i>zlib</i>. Defaults to <i>zlib</i> if no style is specified.</dd>
<dt><code>&#8211;decompress-debug-sections</code></dt>
<dd> Decompress any compressed DWARF debug sections in the output.</dd>
<dt><code>&#8211;discard-locals, -X</code></dt>
<dd> Remove local symbols starting with “.L” from the output.</dd>
<dt><code>&#8211;extract-dwo</code></dt>
<dd> Remove all sections that are not DWARF .dwo sections from the output.</dd>
<dt><code>&#8211;extract-main-partition</code></dt>
<dd> Extract the main partition from the output.</dd>
<dt><code>&#8211;extract-partition &lt;name&gt;</code></dt>
<dd> Extract the named partition from the output.</dd>
<dt><code>&#8211;globalize-symbol &lt;symbol&gt;</code></dt>
<dd> Mark any defined symbols named <code>&lt;symbol&gt;</code> as global symbols in the output. Can be specified multiple times to mark multiple symbols.</dd>
<dt><code>&#8211;globalize-symbols &lt;filename&gt;</code></dt>
<dd> Read a list of names from the file <code>&lt;filename&gt;</code> and mark defined symbols with those names as global in the output. In the file, each line represents a single symbol, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;input-target &lt;format&gt;, -I</code></dt>
<dd> Read the input as the specified format. See <i>SUPPORTED FORMATS</i> for a list of valid <code>&lt;format&gt;</code> values. If unspecified, <code>llvm-objcopy</code> will attempt to determine the format automatically.</dd>
<dt><code>&#8211;keep-file-symbols</code></dt>
<dd> Keep symbols of type <i>STT_FILE</i>, even if they would otherwise be stripped.</dd>
<dt><code>&#8211;keep-global-symbol &lt;symbol&gt;, -G</code></dt>
<dd> Make all symbols local in the output, except for symbols with the name <code>&lt;symbol&gt;</code>. Can be specified multiple times to ignore multiple symbols.</dd>
<dt><code>&#8211;keep-global-symbols &lt;filename&gt;</code></dt>
<dd> Make all symbols local in the output, except for symbols named in the file <code>&lt;filename&gt;</code>. In the file, each line represents a single symbol, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;keep-section &lt;section&gt;</code></dt>
<dd> When removing sections from the output, do not remove sections named <code>&lt;section&gt;</code>. Can be specified multiple times to keep multiple sections.</dd>
<dt><code>&#8211;keep-symbol &lt;symbol&gt;, -K</code></dt>
<dd> When removing symbols from the output, do not remove symbols named <code>&lt;symbol&gt;</code>. Can be specified multiple times to keep multiple symbols.</dd>
<dt><code>&#8211;keep-symbols &lt;filename&gt;</code></dt>
<dd> When removing symbols from the output do not remove symbols named in the file <code>&lt;filename&gt;</code>. In the file, each line represents a single symbol, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;localize-hidden</code></dt>
<dd> Make all symbols with hidden or internal visibility local in the output.</dd>
<dt><code>&#8211;localize-symbol &lt;symbol&gt;, -L</code></dt>
<dd> Mark any defined non-common symbol named <code>&lt;symbol&gt;</code> as a local symbol in the output. Can be specified multiple times to mark multiple symbols as local.</dd>
<dt><code>&#8211;localize-symbols &lt;filename&gt;</code></dt>
<dd> Read a list of names from the file <code>&lt;filename&gt;</code> and mark defined non-common symbols with those names as local in the output. In the file, each line represents a single symbol, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;new-symbol-visibility &lt;visibility&gt;</code></dt>
<dd> Specify the visibility of the symbols automatically created when using binary input or <i>&#8211;add-symbol</i>. Valid options are:</dd>
<dt>&bull;</dt>
<dd> <i>default</i></dd>
<dt>&bull;</dt>
<dd> <i>hidden</i></dd>
<dt>&bull;</dt>
<dd> <i>internal</i></dd>
<dt>&bull;</dt>
<dd> <i>protected</i> </dd>
<p> The default is <i>default</i>.</p>
<dt><code>&#8211;output-target &lt;format&gt;, -O</code></dt>
<dd> Write the output as the specified format. See <i>SUPPORTED FORMATS</i> for a list of valid <code>&lt;format&gt;</code> values. If unspecified, the output format is assumed to be the same as the value specified for <i>&#8211;input-target</i> or the input file’s format if that option is also unspecified.</dd>
<dt><code>&#8211;prefix-alloc-sections &lt;prefix&gt;</code></dt>
<dd> Add <code>&lt;prefix&gt;</code> to the front of the names of all allocatable sections in the output.</dd>
<dt><code>&#8211;prefix-symbols &lt;prefix&gt;</code></dt>
<dd> Add <code>&lt;prefix&gt;</code> to the front of every symbol name in the output.</dd>
<dt><code>&#8211;preserve-dates, -p</code></dt>
<dd> Preserve access and modification timestamps in the output.</dd>
<dt><code>&#8211;rename-section &lt;old&gt;=&lt;new&gt;[,&lt;flag&gt;,&#8230;]</code></dt>
<dd> Rename sections called <code>&lt;old&gt;</code> to <code>&lt;new&gt;</code> in the output, and apply any specified <code>&lt;flag&gt;</code> values. See <i>&#8211;set-section-flags</i> for a list of supported flags. Can be specified multiple times to rename multiple sections.</dd>
<dt><code>&#8211;set-start-addr &lt;addr&gt;</code></dt>
<dd> Set the start address of the output to <code>&lt;addr&gt;</code>. Overrides any previously specified <i>&#8211;change-start</i> or <i>&#8211;adjust-start</i> options.</dd>
<dt><code>&#8211;split-dwo &lt;dwo-file&gt;</code></dt>
<dd> Equivalent to running <code>llvm-objcopy</code> with <i>&#8211;extract-dwo</i> and <code>&lt;dwo-file&gt;</code> as the output file and no other options, and then with <i>&#8211;strip-dwo</i> on the input file.</dd>
<dt><code>&#8211;strip-dwo</code></dt>
<dd> Remove all DWARF .dwo sections from the output.</dd>
<dt><code>&#8211;strip-non-alloc</code></dt>
<dd> Remove from the output all non-allocatable sections that are not within segments.</dd>
<dt><code>&#8211;strip-sections</code></dt>
<dd> Remove from the output all section headers and all section data not within segments. Note that many tools will not be able to use an object without section headers.</dd>
<dt><code>&#8211;target &lt;format&gt;, -F</code></dt>
<dd> Equivalent to <i>&#8211;input-target</i> and <i>&#8211;output-target</i> for the specified format. See <i>SUPPORTED FORMATS</i> for a list of valid <code>&lt;format&gt;</code> values.</dd>
<dt><code>&#8211;weaken-symbol &lt;symbol&gt;, -W</code></dt>
<dd> Mark any global symbol named <code>&lt;symbol&gt;</code> as a weak symbol in the output. Can be specified multiple times to mark multiple symbols as weak.</dd>
<dt><code>&#8211;weaken-symbols &lt;filename&gt;</code></dt>
<dd> Read a list of names from the file <code>&lt;filename&gt;</code> and mark global symbols with those names as weak in the output. In the file, each line represents a single symbol, with leading and trailing whitespace ignored, as is anything following a ‘#’. Can be specified multiple times to read names from multiple files.</dd>
<dt><code>&#8211;weaken</code></dt>
<dd> Mark all defined global symbols as weak in the output.</dd></dl>
<h2>MACH-O-SPECIFIC OPTIONS</h2>
<dl>
<dt><code>&#8211;keep-undefined</code></dt>
<dd> Keep undefined symbols, even if they would otherwise be stripped.</dd></dl>
<h2>COFF-SPECIFIC OPTIONS</h2>
<dl>
<dt><code>&#8211;subsystem &lt;name&gt;[:&lt;version&gt;]</code></dt>
<dd> Set the PE subsystem, and optionally subsystem version.</dd></dl>
<h2>SUPPORTED FORMATS</h2>
<p> The following values are currently supported by <code>llvm-objcopy</code> for the <i>&#8211;input-target</i>, <i>&#8211;output-target</i>, and <i>&#8211;target</i> options. For GNU <code>objcopy</code> compatibility, the values are all bfdnames.</p>
<dl>
<dt>&bull;</dt>
<dd> <i>binary</i></dd>
<dt>&bull;</dt>
<dd> <i>ihex</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-i386</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-x86-64</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-x86-64</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-iamcu</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-littlearm</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-aarch64</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-littleaarch64</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-littleriscv</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-littleriscv</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-powerpc</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-powerpcle</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-powerpc</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-powerpcle</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-bigmips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-ntradbigmips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-ntradlittlemips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-tradbigmips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-tradlittlemips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-tradbigmips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf64-tradlittlemips</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-sparc</i></dd>
<dt>&bull;</dt>
<dd> <i>elf32-sparcel</i> </dd>
<p> Additionally, all targets except <i>binary</i> and <i>ihex</i> can have <i>-freebsd</i> as a suffix.</dl>
<h2>BINARY INPUT AND OUTPUT</h2>
<p> If <i>binary</i> is used as the value for <i>&#8211;input-target</i>, the input file will be embedded as a data section in an ELF relocatable object, with symbols <code>_binary_&lt;file_name&gt;_start</code>, <code>_binary_&lt;file_name&gt;_end</code>, and <code>_binary_&lt;file_name&gt;_size</code> representing the start, end and size of the data, where <code>&lt;file_name&gt;</code> is the path of the input file as specified on the command line with non-alphanumeric characters converted to <code>_</code>. </p>
<p> If <i>binary</i> is used as the value for <i>&#8211;output-target</i>, the output file will be a raw binary file, containing the memory image of the input file. Symbols and relocation information will be discarded. The image will start at the address of the first loadable section in the output.</p>
<h2>EXIT STATUS</h2>
<p> <code>llvm-objcopy</code> exits with a non-zero exit code if there is an error. Otherwise, it exits with code 0.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy/strip/">https://github.com/llvm/llvm-project/labels/tools:llvm-objcopy/strip/</a></i>&gt;. </p>
<p> There is a known issue with <i>&#8211;input-target</i> and <i>&#8211;target</i> causing only <code>binary</code> and <code>ihex</code> formats to have any effect. Other values will be ignored and <code>llvm-objcopy</code> will attempt to guess the input format.</p>
<h2>SEE ALSO</h2>
<p> <code>llvm-strip(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
