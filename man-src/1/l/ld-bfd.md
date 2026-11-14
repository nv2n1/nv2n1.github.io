---
title: "ld-bfd(1)"
name: "ld-bfd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ld-bfd/"
description: "ld – The GNU linker"
---

<p>ld &#8211; The GNU linker </p>
<h2>Synopsis</h2>
<p>ld [<code>options</code>] <i>objfile</i> &#8230;</p>
<h2>Description</h2>
<p><code>ld</code> combines a number of object and archive files, relocates their data and ties up symbol references. Usually the last step in compiling a program is to run <code>ld</code>. </p>
<p> <code>ld</code> accepts Linker Command Language files written in a superset of <font SIZE="-1">AT&amp;T</font>&#8216;s Link Editor Command Language syntax, to provide explicit and total control over the linking process. </p>
<p> This man page does not describe the command language; see the <code>ld</code> entry in <tt>&quot;info&quot;</tt> for full details on the command language and on other aspects of the <font SIZE="-1">GNU</font> linker. </p>
<p> This version of <code>ld</code> uses the general purpose <font SIZE="-1">BFD</font> libraries to operate on object files. This allows <code>ld</code> to read, combine, and write object files in many different formats&#8212;for example, <font SIZE="-1">COFF</font> or <tt>&quot;a.out&quot;</tt>. Different formats may be linked together to produce any available kind of object file. </p>
<p> Aside from its flexibility, the <font SIZE="-1">GNU</font> linker is more helpful than other linkers in providing diagnostic information. Many linkers abandon execution immediately upon encountering an error; whenever possible, <code>ld</code> continues executing, allowing you to identify other errors (or, in some cases, to get an output file in spite of the error). </p>
<p> The <font SIZE="-1">GNU</font> linker <code>ld</code> is meant to cover a broad range of situations, and to be as compatible as possible with other linkers. As a result, you have many choices to control its behavior.</p>
<h2>Options</h2>
<p>The linker supports a plethora of command-line options, but in actual practice few of them are used in any particular context. For instance, a frequent use of <code>ld</code> is to link standard Unix object files on a standard, supported Unix system. On such a system, to link a file <tt>&quot;hello.o&quot;</tt>: </p>
<pre> ld -o &lt;output&gt; /lib/crt0.o hello.o -lc</pre>
<p>This tells <code>ld</code> to produce a file called <i>output</i> as the result of linking the file <tt>&quot;/lib/crt0.o&quot;</tt> with <tt>&quot;hello.o&quot;</tt> and the library <tt>&quot;libc.a&quot;</tt>, which will come from the standard search directories. (See the discussion of the <code>-l</code> option below.) </p>
<p> Some of the command-line options to <code>ld</code> may be specified at any point in the command line. However, options which refer to files, such as <code>-l</code> or <code>-T</code>, cause the file to be read at the point at which the option appears in the command line, relative to the object files and other file options. Repeating non-file options with a different argument will either have no further effect, or override prior occurrences (those further to the left on the command line) of that option. Options which may be meaningfully specified more than once are noted in the descriptions below. </p>
<p> Non-option arguments are object files or archives which are to be linked together. They may follow, precede, or be mixed in with command-line options, except that an object file argument may not be placed between an option and its argument. </p>
<p> Usually the linker is invoked with at least one object file, but you can specify other forms of binary input files using <code>-l</code>, <code>-R</code>, and the script command language. If <i>no</i> binary input files at all are specified, the linker does not produce any output, and issues the message <code>No input files</code>. </p>
<p> If the linker cannot recognize the format of an object file, it will assume that it is a linker script. A script specified in this way augments the main linker script used for the link (either the default linker script or the one specified by using <code>-T</code>). This feature permits the linker to link against a file which appears to be an object or an archive, but actually merely defines some symbol values, or uses <tt>&quot;INPUT&quot;</tt> or <tt>&quot;GROUP&quot;</tt> to load other objects. Specifying a script in this way merely augments the main linker script, with the extra commands placed after the main script; use the <code>-T</code> option to replace the default linker script entirely, but note the effect of the <tt>&quot;INSERT&quot;</tt> command. </p>
<p> For options whose names are a single letter, option arguments must either follow the option letter without intervening whitespace, or be given as separate arguments immediately following the option that requires them. </p>
<p> For options whose names are multiple letters, either one dash or two can precede the option name; for example, <code>-trace-symbol</code> and <code>&#8211;trace-symbol</code> are equivalent. Note&#8212;there is one exception to this rule. Multiple letter options that start with a lower case &#8216;o&#8217; can only be preceded by two dashes. This is to reduce confusion with the <code>-o</code> option. So for example <code>-omagic</code> sets the output file name to <code>magic</code> whereas <code>&#8211;omagic</code> sets the <font SIZE="-1">NMAGIC</font> flag on the output. </p>
<p> Arguments to multiple-letter options must either be separated from the option name by an equals sign, or be given as separate arguments immediately following the option that requires them. For example, <code>&#8211;trace-symbol foo</code> and <code>&#8211;trace-symbol=foo</code> are equivalent. Unique abbreviations of the names of multiple-letter options are accepted. </p>
<p> Note&#8212;if the linker is being invoked indirectly, via a compiler driver (e.g. <code>gcc</code>) then all the linker command-line options should be prefixed by <code>-Wl,</code> (or whatever is appropriate for the particular compiler driver) like this: </p>
<pre> gcc -Wl,--start-group foo.o bar.o -Wl,--end-group</pre>
<p>This is important, because otherwise the compiler driver program may silently drop the linker options, resulting in a bad link. Confusion may also arise when passing options that require values through a driver, as the use of a space between option and argument acts as a separator, and causes the driver to pass only the option to the linker and the argument to the compiler. In this case, it is simplest to use the joined forms of both single- and multiple-letter options, such as: </p>
<pre> gcc foo.o bar.o -Wl,-eENTRY -Wl,-Map=a.map</pre>
<p>Here is a table of the generic command-line switches accepted by the <font SIZE="-1">GNU</font> linker:</p>
<dl>
<dt><code>@</code><i>file</i></p>
<dd>Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</p>
<dt><code>-a</code> <i>keyword</i></p>
<dd>This option is supported for <font SIZE="-1">HP/UX</font> compatibility. The <i>keyword</i> argument must be one of the strings <code>archive</code>, <code>shared</code>, or <code>default</code>. <code>-aarchive</code> is functionally equivalent to <code>-Bstatic</code>, and the other two keywords are functionally equivalent to <code>-Bdynamic</code>. This option may be used any number of times.</p>
<dt><code>&#8211;audit</code> <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i></p>
<dd>Adds <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i> to the <tt>&quot;DT_AUDIT&quot;</tt> entry of the dynamic section. <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i> is not checked for existence, nor will it use the <font SIZE="-1">DT_SONAME</font> specified in the library. If specified multiple times <tt>&quot;DT_AUDIT&quot;</tt> will contain a colon separated list of audit interfaces to use. If the linker finds an object with an audit entry while searching for shared libraries, it will add a corresponding <tt>&quot;DT_DEPAUDIT&quot;</tt> entry in the output file. This option is only meaningful on <font SIZE="-1">ELF</font> platforms supporting the rtld-audit interface.</p>
<dt><code>-b</code> <i>input-format</i></p>
<dd>
<dt><code>&#8211;format=</code><i>input-format</i></p>
<dd><code>ld</code> may be configured to support more than one kind of object file. If your <code>ld</code> is configured this way, you can use the <code>-b</code> option to specify the binary format for input object files that follow this option on the command line. Even when <code>ld</code> is configured to support alternative object formats, you don&#8217;t usually need to specify this, as <code>ld</code> should be configured to expect as a default input format the most usual format on each machine. <i>input-format</i> is a text string, the name of a particular format supported by the <font SIZE="-1">BFD</font> libraries. (You can list the available binary formats with <code>objdump -i</code>.) </p>
<p> You may want to use this option if you are linking files with an unusual binary format. You can also use <code>-b</code> to switch formats explicitly (when linking object files of different formats), by including <code>-b</code> <i>input-format</i> before each group of object files in a particular format. </p>
<p> The default format is taken from the environment variable <tt>&quot;GNUTARGET&quot;</tt>. </p>
<p> You can also define the input format from a script, using the command <tt>&quot;TARGET&quot;</tt>;</p>
<dt><code>-c</code> <i>MRI-commandfile</i></p>
<dd>
<dt><code>&#8211;mri-script=</code><i>MRI-commandfile</i></p>
<dd>For compatibility with linkers produced by <font SIZE="-1">MRI,</font> <code>ld</code> accepts script files written in an alternate, restricted command language, described in the <font SIZE="-1">MRI</font> Compatible Script Files section of <font SIZE="-1">GNU</font> ld documentation. Introduce <font SIZE="-1">MRI</font> script files with the option <code>-c</code>; use the <code>-T</code> option to run linker scripts written in the general-purpose <code>ld</code> scripting language. If <i>MRI-cmdfile</i> does not exist, <code>ld</code> looks for it in the directories specified by any <code>-L</code> options.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>-dc</code></p>
<dd>
<dt><code>-dp</code></p>
<dd>These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even if a relocatable output file is specified (with <code>-r</code>). The script command <tt>&quot;FORCE_COMMON_ALLOCATION&quot;</tt> has the same effect.</p>
<dt><code>&#8211;depaudit</code> <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i></p>
<dd>
<dt><code>-P</code> <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i></p>
<dd>Adds <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i> to the <tt>&quot;DT_DEPAUDIT&quot;</tt> entry of the dynamic section. <i></i><font SIZE="-1"><i>AUDITLIB</i></font><i></i> is not checked for existence, nor will it use the <font SIZE="-1">DT_SONAME</font> specified in the library. If specified multiple times <tt>&quot;DT_DEPAUDIT&quot;</tt> will contain a colon separated list of audit interfaces to use. This option is only meaningful on <font SIZE="-1">ELF</font> platforms supporting the rtld-audit interface. The -P option is provided for Solaris compatibility.</p>
<dt><code>&#8211;enable-non-contiguous-regions</code></p>
<dd>This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input section to subseque nt matching output sections, and generates an error only if no output section is large enough. This is useful when several non-contiguous memory regions are available and the input section does not require a particular one. The order in which input sections are evaluated does not change, for instance: </p>
<pre> MEMORY {
 MEM1 (rwx) : ORIGIN : 0x1000, LENGTH = 0x14
 MEM2 (rwx) : ORIGIN : 0x1000, LENGTH = 0x40
 MEM3 (rwx) : ORIGIN : 0x2000, LENGTH = 0x40
 }
 SECTIONS {
 mem1 : { *(.data.*); } &gt; MEM1
 mem2 : { *(.data.*); } &gt; MEM2
 mem3 : { *(.data.*); } &gt; MEM2
 }
 
 with input sections:
 .data.1: size 8
 .data.2: size 0x10
 .data.3: size 4
 
 results in .data.1 affected to mem1, and .data.2 and .data.3
 affected to mem2, even though .data.3 would fit in mem3.</pre>
<p>This option is incompatible with <font SIZE="-1">INSERT</font> statements because it changes the way input sections are mapped to output sections.</p>
<dt><code>&#8211;enable-non-contiguous-regions-warnings</code></p>
<dd>This option enables warnings when <tt>&quot;--enable-non-contiguous-regions&quot;</tt> allows possibly unexpected matches in sections mapping, potentially leading to silently discarding a section instead of failing because it does not fit any output region.</p>
<dt><code>-e</code> <i>entry</i></p>
<dd>
<dt><code>&#8211;entry=</code><i>entry</i></p>
<dd>Use <i>entry</i> as the explicit symbol for beginning execution of your program, rather than the default entry point. If there is no symbol named <i>entry</i>, the linker will try to parse <i>entry</i> as a number, and use that as the entry address (the number will be interpreted in base 10; you may use a leading <code>0x</code> for base 16, or a leading <code>0</code> for base 8).</p>
<dt><code>&#8211;exclude-libs</code> <i>lib</i><code>,</code><i>lib</i><code>,&#8230;</code></p>
<dd>Specifies a list of archive libraries from which symbols should not be automatically exported. The library names may be delimited by commas or colons. Specifying <tt>&quot;--exclude-libs ALL&quot;</tt> excludes symbols in all archive libraries from automatic export. This option is available only for the i386 <font SIZE="-1">PE</font> targeted port of the linker and for <font SIZE="-1">ELF</font> targeted ports. For i386 <font SIZE="-1">PE,</font> symbols explicitly listed in a .def file are still exported, regardless of this option. For <font SIZE="-1">ELF</font> targeted ports, symbols affected by this option will be treated as hidden.</p>
<dt><code>&#8211;exclude-modules-for-implib</code> <i>module</i><code>,</code><i>module</i><code>,&#8230;</code></p>
<dd>Specifies a list of object files or archive members, from which symbols should not be automatically exported, but which should be copied wholesale into the import library being generated during the link. The module names may be delimited by commas or colons, and must match exactly the filenames used by <code>ld</code> to open the files; for archive members, this is simply the member name, but for object files the name listed must include and match precisely any path used to specify the input file on the linker&#8217;s command-line. This option is available only for the i386 <font SIZE="-1">PE</font> targeted port of the linker. Symbols explicitly listed in a .def file are still exported, regardless of this option.</p>
<dt><code>-E</code></p>
<dd>
<dt><code>&#8211;export-dynamic</code></p>
<dd>
<dt><code>&#8211;no-export-dynamic</code></p>
<dd>When creating a dynamically linked executable, using the <code>-E</code> option or the <code>&#8211;export-dynamic</code> option causes the linker to add all symbols to the dynamic symbol table. The dynamic symbol table is the set of symbols which are visible from dynamic objects at run time. </p>
<p> If you do not use either of these options (or use the <code>&#8211;no-export-dynamic</code> option to restore the default behavior), the dynamic symbol table will normally contain only those symbols which are referenced by some dynamic object mentioned in the link. </p>
<p> If you use <tt>&quot;dlopen&quot;</tt> to load a dynamic object which needs to refer back to the symbols defined by the program, rather than some other dynamic object, then you will probably need to use this option when linking the program itself. </p>
<p> You can also use the dynamic list to control what symbols should be added to the dynamic symbol table if the output format supports it. See the description of <code>&#8211;dynamic-list</code>. </p>
<p> Note that this option is specific to <font SIZE="-1">ELF</font> targeted ports. <font SIZE="-1">PE</font> targets support a similar function to export all symbols from a <font SIZE="-1">DLL</font> or <font SIZE="-1">EXE</font>; see the description of <code>&#8211;export-all-symbols</code> below.</p>
<dt><code>&#8211;export-dynamic-symbol=</code><i>glob</i></p>
<dd>When creating a dynamically linked executable, symbols matching <i>glob</i> will be added to the dynamic symbol table. When creating a shared library, references to symbols matching <i>glob</i> will not be bound to the definitions within the shared library. This option is a no-op when creating a shared library and <code>-Bsymbolic</code> or <code>&#8211;dynamic-list</code> are not specified. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>&#8211;export-dynamic-symbol-list=</code><i>file</i></p>
<dd>Specify a <code>&#8211;export-dynamic-symbol</code> for each pattern in the file. The format of the file is the same as the version node without scope and node name. See <font SIZE="-1"><code>VERSION</code></font> for more information.</p>
<dt><code>-EB</code></p>
<dd>Link big-endian objects. This affects the default output format.</p>
<dt><code>-EL</code></p>
<dd>Link little-endian objects. This affects the default output format.</p>
<dt><code>-f</code> <i>name</i></p>
<dd>
<dt><code>&#8211;auxiliary=</code><i>name</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_AUXILIARY</font> field to the specified name. This tells the dynamic linker that the symbol table of the shared object should be used as an auxiliary filter on the symbol table of the shared object <i>name</i>. </p>
<p> If you later link a program against this filter object, then, when you run the program, the dynamic linker will see the <font SIZE="-1">DT_AUXILIARY</font> field. If the dynamic linker resolves any symbols from the filter object, it will first check whether there is a definition in the shared object <i>name</i>. If there is one, it will be used instead of the definition in the filter object. The shared object <i>name</i> need not exist. Thus the shared object <i>name</i> may be used to provide an alternative implementation of certain functions, perhaps for debugging or for machine-specific performance. </p>
<p> This option may be specified more than once. The <font SIZE="-1">DT_AUXILIARY</font> entries will be created in the order in which they appear on the command line.</p>
<dt><code>-F</code> <i>name</i></p>
<dd>
<dt><code>&#8211;filter=</code><i>name</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_FILTER</font> field to the specified name. This tells the dynamic linker that the symbol table of the shared object which is being created should be used as a filter on the symbol table of the shared object <i>name</i>. </p>
<p> If you later link a program against this filter object, then, when you run the program, the dynamic linker will see the <font SIZE="-1">DT_FILTER</font> field. The dynamic linker will resolve symbols according to the symbol table of the filter object as usual, but it will actually link to the definitions found in the shared object <i>name</i>. Thus the filter object can be used to select a subset of the symbols provided by the object <i>name</i>. </p>
<p> Some older linkers used the <code>-F</code> option throughout a compilation toolchain for specifying object-file format for both input and output object files. The <font SIZE="-1">GNU</font> linker uses other mechanisms for this purpose: the <code>-b</code>, <code>&#8211;format</code>, <code>&#8211;oformat</code> options, the <tt>&quot;TARGET&quot;</tt> command in linker scripts, and the <tt>&quot;GNUTARGET&quot;</tt> environment variable. The <font SIZE="-1">GNU</font> linker will ignore the <code>-F</code> option when not creating an <font SIZE="-1">ELF</font> shared object.</p>
<dt><code>-fini=</code><i>name</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> executable or shared object, call <font SIZE="-1">NAME</font> when the executable or shared object is unloaded, by setting <font SIZE="-1">DT_FINI</font> to the address of the function. By default, the linker uses <tt>&quot;_fini&quot;</tt> as the function to call.</p>
<dt><code>-g</code></p>
<dd>Ignored. Provided for compatibility with other tools.</p>
<dt><code>-G</code> <i>value</i></p>
<dd>
<dt><code>&#8211;gpsize=</code><i>value</i></p>
<dd>Set the maximum size of objects to be optimized using the <font SIZE="-1">GP</font> register to <i>size</i>. This is only meaningful for object file formats such as <font SIZE="-1">MIPS ELF</font> that support putting large and small objects into different sections. This is ignored for other object file formats.</p>
<dt><code>-h</code> <i>name</i></p>
<dd>
<dt><code>-soname=</code><i>name</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_SONAME</font> field to the specified name. When an executable is linked with a shared object which has a <font SIZE="-1">DT_SONAME</font> field, then when the executable is run the dynamic linker will attempt to load the shared object specified by the <font SIZE="-1">DT_SONAME</font> field rather than using the file name given to the linker.</p>
<dt><code>-i</code></p>
<dd>Perform an incremental link (same as option <code>-r</code>).</p>
<dt><code>-init=</code><i>name</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> executable or shared object, call <font SIZE="-1">NAME</font> when the executable or shared object is loaded, by setting <font SIZE="-1">DT_INIT</font> to the address of the function. By default, the linker uses <tt>&quot;_init&quot;</tt> as the function to call.</p>
<dt><code>-l</code> <i>namespec</i></p>
<dd>
<dt><code>&#8211;library=</code><i>namespec</i></p>
<dd>Add the archive or object file specified by <i>namespec</i> to the list of files to link. This option may be used any number of times. If <i>namespec</i> is of the form <i>:filename</i>, <code>ld</code> will search the library path for a file called <i>filename</i>, otherwise it will search the library path for a file called <i>libnamespec.a</i>. </p>
<p> On systems which support shared libraries, <code>ld</code> may also search for files other than <i>libnamespec.a</i>. Specifically, on <font SIZE="-1">ELF</font> and SunOS systems, <code>ld</code> will search a directory for a library called <i>libnamespec.so</i> before searching for one called <i>libnamespec.a</i>. (By convention, a <tt>&quot;.so&quot;</tt> extension indicates a shared library.) Note that this behavior does not apply to <i>:filename</i>, which always specifies a file called <i>filename</i>. </p>
<p> The linker will search an archive only once, at the location where it is specified on the command line. If the archive defines a symbol which was undefined in some object which appeared before the archive on the command line, the linker will include the appropriate file(s) from the archive. However, an undefined symbol in an object appearing later on the command line will not cause the linker to search the archive again. </p>
<p> See the <code>-(</code> option for a way to force the linker to search archives multiple times. </p>
<p> You may list the same archive multiple times on the command line. </p>
<p> This type of archive searching is standard for Unix linkers. However, if you are using <code>ld</code> on <font SIZE="-1">AIX,</font> note that it is different from the behaviour of the <font SIZE="-1">AIX</font> linker.</p>
<dt><code>-L</code> <i>searchdir</i></p>
<dd>
<dt><code>&#8211;library-path=</code><i>searchdir</i></p>
<dd>Add path <i>searchdir</i> to the list of paths that <code>ld</code> will search for archive libraries and <code>ld</code> control scripts. You may use this option any number of times. The directories are searched in the order in which they are specified on the command line. Directories specified on the command line are searched before the default directories. All <code>-L</code> options apply to all <code>-l</code> options, regardless of the order in which the options appear. <code>-L</code> options do not affect how <code>ld</code> searches for a linker script unless <code>-T</code> option is specified. </p>
<p> If <i>searchdir</i> begins with <tt>&quot;=&quot;</tt> or <tt>$SYSROOT</tt>, then this prefix will be replaced by the <i>sysroot prefix</i>, controlled by the <code>&#8211;sysroot</code> option, or specified when the linker is configured. </p>
<p> The default set of paths searched (without being specified with <code>-L</code>) depends on which emulation mode <code>ld</code> is using, and in some cases also on how it was configured. </p>
<p> The paths can also be specified in a link script with the <tt>&quot;SEARCH_DIR&quot;</tt> command. Directories specified this way are searched at the point in which the linker script appears in the command line.</p>
<dt><code>-m</code> <i>emulation</i></p>
<dd>Emulate the <i>emulation</i> linker. You can list the available emulations with the <code>&#8211;verbose</code> or <code>-V</code> options. </p>
<p> If the <code>-m</code> option is not used, the emulation is taken from the <tt>&quot;LDEMULATION&quot;</tt> environment variable, if that is defined. </p>
<p> Otherwise, the default emulation depends upon how the linker was configured.</p>
<dt><code>-M</code></p>
<dd>
<dt><code>&#8211;print-map</code></p>
<dd>Print a link map to the standard output. A link map provides information about the link, including the following:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Where object files are mapped into memory.</p>
<dt>&bull;</p>
<dd>How common symbols are allocated.</p>
<dt>&bull;</p>
<dd>All archive members included in the link, with a mention of the symbol which caused the archive member to be brought in.</p>
<dt>&bull;</p>
<dd>The values assigned to symbols. </p>
<p> Note &#8211; symbols whose values are computed by an expression which involves a reference to a previous value of the same symbol may not have correct result displayed in the link map. This is because the linker discards intermediate results and only retains the final value of an expression. Under such circumstances the linker will display the final value enclosed by square brackets. Thus for example a linker script containing: </p>
<pre> foo = 1
 foo = foo * 4
 foo = foo + 8</pre>
<p>will produce the following output in the link map if the <code>-M</code> option is used: </p>
<pre> 0x00000001 foo = 0x1
 [0x0000000c] foo = (foo * 0x4)
 [0x0000000c] foo = (foo + 0x8)</pre>
<p>See <code>Expressions</code> for more information about expressions in linker scripts.</p>
<dt>&bull;</p>
<dd>How <font SIZE="-1">GNU</font> properties are merged. </p>
<p> When the linker merges input .note.gnu.property sections into one output .note.gnu.property section, some properties are removed or updated. These actions are reported in the link map. For example: </p>
<pre> Removed property 0xc0000002 to merge foo.o (0x1) and bar.o (not found)</pre>
<p>This indicates that property 0xc0000002 is removed from output when merging properties in <i>foo.o</i>, whose property 0xc0000002 value is 0x1, and <i>bar.o</i>, which doesn&#8217;t have property 0xc0000002. </p>
<pre> Updated property 0xc0010001 (0x1) to merge foo.o (0x1) and bar.o (0x1)</pre>
<p>This indicates that property 0xc0010001 value is updated to 0x1 in output when merging properties in <i>foo.o</i>, whose 0xc0010001 property value is 0x1, and <i>bar.o</i>, whose 0xc0010001 property value is 0x1.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;print-map-discarded</code></p>
<dd>
<dt><code>&#8211;no-print-map-discarded</code></p>
<dd>Print (or do not print) the list of discarded and garbage collected sections in the link map. Enabled by default.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;nmagic</code></p>
<dd>Turn off page alignment of sections, and disable linking against shared libraries. If the output format supports Unix style magic numbers, mark the output as <tt>&quot;NMAGIC&quot;</tt>.</p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;omagic</code></p>
<dd>Set the text and data sections to be readable and writable. Also, do not page-align the data segment, and disable linking against shared libraries. If the output format supports Unix style magic numbers, mark the output as <tt>&quot;OMAGIC&quot;</tt>. Note: Although a writable text section is allowed for PE-COFF targets, it does not conform to the format specification published by Microsoft.</p>
<dt><code>&#8211;no-omagic</code></p>
<dd>This option negates most of the effects of the <code>-N</code> option. It sets the text section to be read-only, and forces the data segment to be page-aligned. Note &#8211; this option does not enable linking against shared libraries. Use <code>-Bdynamic</code> for this.</p>
<dt><code>-o</code> <i>output</i></p>
<dd>
<dt><code>&#8211;output=</code><i>output</i></p>
<dd>Use <i>output</i> as the name for the program produced by <code>ld</code>; if this option is not specified, the name <i>a.out</i> is used by default. The script command <tt>&quot;OUTPUT&quot;</tt> can also specify the output file name.</p>
<dt><code>&#8211;dependency-file=</code><i>depfile</i></p>
<dd>Write a <i>dependency file</i> to <i>depfile</i>. This file contains a rule suitable for <tt>&quot;make&quot;</tt> describing the output file and all the input files that were read to produce it. The output is similar to the compiler&#8217;s output with <code>-M -MP</code>. Note that there is no option like the compiler&#8217;s <code>-MM</code>, to exclude &#8220;system files&#8221; (which is not a well-specified concept in the linker, unlike &#8220;system headers&#8221; in the compiler). So the output from <code>&#8211;dependency-file</code> is always specific to the exact state of the installation where it was produced, and should not be copied into distributed makefiles without careful editing.</p>
<dt><code>-O</code> <i>level</i></p>
<dd>If <i>level</i> is a numeric values greater than zero <code>ld</code> optimizes the output. This might take significantly longer and therefore probably should only be enabled for the final binary. At the moment this option only affects <font SIZE="-1">ELF</font> shared library generation. Future releases of the linker may make more use of this option. Also currently there is no difference in the linker&#8217;s behaviour for different non-zero values of this option. Again this may change with future releases.</p>
<dt><code>-plugin</code> <i>name</i></p>
<dd>Involve a plugin in the linking process. The <i>name</i> parameter is the absolute filename of the plugin. Usually this parameter is automatically added by the complier, when using link time optimization, but users can also add their own plugins if they so wish. </p>
<p> Note that the location of the compiler originated plugins is different from the place where the <code>ar</code>, <code>nm</code> and <code>ranlib</code> programs search for their plugins. In order for those commands to make use of a compiler based plugin it must first be copied into the <i>${libdir}/bfd-plugins</i> directory. All gcc based linker plugins are backward compatible, so it is sufficient to just copy in the newest one.</p>
<dt><code>&#8211;push-state</code></p>
<dd>The <code>&#8211;push-state</code> allows one to preserve the current state of the flags which govern the input file handling so that they can all be restored with one corresponding <code>&#8211;pop-state</code> option. </p>
<p> The option which are covered are: <code>-Bdynamic</code>, <code>-Bstatic</code>, <code>-dn</code>, <code>-dy</code>, <code>-call_shared</code>, <code>-non_shared</code>, <code>-static</code>, <code>-N</code>, <code>-n</code>, <code>&#8211;whole-archive</code>, <code>&#8211;no-whole-archive</code>, <code>-r</code>, <code>-Ur</code>, <code>&#8211;copy-dt-needed-entries</code>, <code>&#8211;no-copy-dt-needed-entries</code>, <code>&#8211;as-needed</code>, <code>&#8211;no-as-needed</code>, and <code>-a</code>. </p>
<p> One target for this option are specifications for <i>pkg-config</i>. When used with the <code>&#8211;libs</code> option all possibly needed libraries are listed and then possibly linked with all the time. It is better to return something as follows: </p>
<pre> -Wl,--push-state,--as-needed -libone -libtwo -Wl,--pop-state</pre>
<dt><code>&#8211;pop-state</code></p>
<dd>Undoes the effect of &#8211;push-state, restores the previous values of the flags governing input file handling.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;emit-relocs</code></p>
<dd>Leave relocation sections and contents in fully linked executables. Post link analysis and optimization tools may need this information in order to perform correct modifications of executables. This results in larger executables. </p>
<p> This option is currently only supported on <font SIZE="-1">ELF</font> platforms.</p>
<dt><code>&#8211;force-dynamic</code></p>
<dd>Force the output file to have dynamic sections. This option is specific to VxWorks targets.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;relocatable</code></p>
<dd>Generate relocatable output&#8212;i.e., generate an output file that can in turn serve as input to <code>ld</code>. This is often called <i>partial linking</i>. As a side effect, in environments that support standard Unix magic numbers, this option also sets the output file&#8217;s magic number to <tt>&quot;OMAGIC&quot;</tt>. If this option is not specified, an absolute file is produced. When linking C<font SIZE="-2">++</font> programs, this option <i>will not</i> resolve references to constructors; to do that, use <code>-Ur</code>. </p>
<p> When an input file does not have the same format as the output file, partial linking is only supported if that input file does not contain any relocations. Different output formats can have further restrictions; for example some <tt>&quot;a.out&quot;</tt>-based formats do not support partial linking with input files in other formats at all. </p>
<p> This option does the same thing as <code>-i</code>.</p>
<dt><code>-R</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;just-symbols=</code><i>filename</i></p>
<dd>Read symbol names and their addresses from <i>filename</i>, but do not relocate it or include it in the output. This allows your output file to refer symbolically to absolute locations of memory defined in other programs. You may use this option more than once. </p>
<p> For compatibility with other <font SIZE="-1">ELF</font> linkers, if the <code>-R</code> option is followed by a directory name, rather than a file name, it is treated as the <code>-rpath</code> option.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;strip-all</code></p>
<dd>Omit all symbol information from the output file.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;strip-debug</code></p>
<dd>Omit debugger symbol information (but not all symbols) from the output file.</p>
<dt><code>&#8211;strip-discarded</code></p>
<dd>
<dt><code>&#8211;no-strip-discarded</code></p>
<dd>Omit (or do not omit) global symbols defined in discarded sections. Enabled by default.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;trace</code></p>
<dd>Print the names of the input files as <code>ld</code> processes them. If <code>-t</code> is given twice then members within archives are also printed. <code>-t</code> output is useful to generate a list of all the object files and scripts involved in linking, for example, when packaging files for a linker bug report.</p>
<dt><code>-T</code> <i>scriptfile</i></p>
<dd>
<dt><code>&#8211;script=</code><i>scriptfile</i></p>
<dd>Use <i>scriptfile</i> as the linker script. This script replaces <code>ld</code>&#8216;s default linker script (rather than adding to it), so <i>commandfile</i> must specify everything necessary to describe the output file. If <i>scriptfile</i> does not exist in the current directory, <tt>&quot;ld&quot;</tt> looks for it in the directories specified by any preceding <code>-L</code> options. Multiple <code>-T</code> options accumulate.</p>
<dt><code>-dT</code> <i>scriptfile</i></p>
<dd>
<dt><code>&#8211;default-script=</code><i>scriptfile</i></p>
<dd>Use <i>scriptfile</i> as the default linker script. </p>
<p> This option is similar to the <code>&#8211;script</code> option except that processing of the script is delayed until after the rest of the command line has been processed. This allows options placed after the <code>&#8211;default-script</code> option on the command line to affect the behaviour of the linker script, which can be important when the linker command line cannot be directly controlled by the user. (eg because the command line is being constructed by another tool, such as <code>gcc</code>).</p>
<dt><code>-u</code> <i>symbol</i></p>
<dd>
<dt><code>&#8211;undefined=</code><i>symbol</i></p>
<dd>Force <i>symbol</i> to be entered in the output file as an undefined symbol. Doing this may, for example, trigger linking of additional modules from standard libraries. <code>-u</code> may be repeated with different option arguments to enter additional undefined symbols. This option is equivalent to the <tt>&quot;EXTERN&quot;</tt> linker script command. </p>
<p> If this option is being used to force additional modules to be pulled into the link, and if it is an error for the symbol to remain undefined, then the option <code>&#8211;require-defined</code> should be used instead.</p>
<dt><code>&#8211;require-defined=</code><i>symbol</i></p>
<dd>Require that <i>symbol</i> is defined in the output file. This option is the same as option <code>&#8211;undefined</code> except that if <i>symbol</i> is not defined in the output file then the linker will issue an error and exit. The same effect can be achieved in a linker script by using <tt>&quot;EXTERN&quot;</tt>, <tt>&quot;ASSERT&quot;</tt> and <tt>&quot;DEFINED&quot;</tt> together. This option can be used multiple times to require additional symbols.</p>
<dt><code>-Ur</code></p>
<dd>For anything other than C<font SIZE="-2">++</font> programs, this option is equivalent to <code>-r</code>: it generates relocatable output&#8212;i.e., an output file that can in turn serve as input to <code>ld</code>. When linking C<font SIZE="-2">++</font> programs, <code>-Ur</code> <i>does</i> resolve references to constructors, unlike <code>-r</code>. It does not work to use <code>-Ur</code> on files that were themselves linked with <code>-Ur</code>; once the constructor table has been built, it cannot be added to. Use <code>-Ur</code> only for the last partial link, and <code>-r</code> for the others.</p>
<dt><code>&#8211;orphan-handling=</code><i></i><font SIZE="-1"><i>MODE</i></font><i></i></p>
<dd>Control how orphan sections are handled. An orphan section is one not specifically mentioned in a linker script. </p>
<p> <i></i><font SIZE="-1"><i>MODE</i></font><i></i> can have any of the following values:</p>
<dl>
<dd>
<dl>
<dt>&quot;place&quot;</p>
<dd>Orphan sections are placed into a suitable output section following the strategy described in <code>Orphan Sections</code>. The option <code>&#8211;unique</code> also affects how sections are placed.</p>
<dt>&quot;discard&quot;</p>
<dd>All orphan sections are discarded, by placing them in the <code>/DISCARD/</code> section.</p>
<dt>&quot;warn&quot;</p>
<dd>The linker will place the orphan section as for <tt>&quot;place&quot;</tt> and also issue a warning.</p>
<dt>&quot;error&quot;</p>
<dd>The linker will exit with an error if any orphan section is found.</dl>
</dl>
<dl>
<dd>The default if <code>&#8211;orphan-handling</code> is not given is <tt>&quot;place&quot;</tt>.</dl>
<dt><code>&#8211;unique[=</code><i></i><font SIZE="-1"><i>SECTION</i></font><i></i><code>]</code></p>
<dd>Creates a separate output section for every input section matching <i></i><font SIZE="-1"><i>SECTION</i></font><i></i>, or if the optional wildcard <i></i><font SIZE="-1"><i>SECTION</i></font><i></i> argument is missing, for every orphan input section. An orphan section is one not specifically mentioned in a linker script. You may use this option multiple times on the command line; It prevents the normal merging of input sections with the same name, overriding output section assignments in a linker script.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>-V</code></p>
<dd>Display the version number for <code>ld</code>. The <code>-V</code> option also lists the supported emulations.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;discard-all</code></p>
<dd>Delete all local symbols.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;discard-locals</code></p>
<dd>Delete all temporary local symbols. (These symbols start with system-specific local label prefixes, typically <code>.L</code> for <font SIZE="-1">ELF</font> systems or <code>L</code> for traditional a.out systems.)</p>
<dt><code>-y</code> <i>symbol</i></p>
<dd>
<dt><code>&#8211;trace-symbol=</code><i>symbol</i></p>
<dd>Print the name of each linked file in which <i>symbol</i> appears. This option may be given any number of times. On many systems it is necessary to prepend an underscore. </p>
<p> This option is useful when you have an undefined symbol in your link but don&#8217;t know where the reference is coming from.</p>
<dt><code>-Y</code> <i>path</i></p>
<dd>Add <i>path</i> to the default library search path. This option exists for Solaris compatibility.</p>
<dt><code>-z</code> <i>keyword</i></p>
<dd>The recognized keywords are:</p>
<dl>
<dd>
<dl>
<dt><code>bndplt</code></p>
<dd>Always generate <font SIZE="-1">BND</font> prefix in <font SIZE="-1">PLT</font> entries. Supported for Linux/x86_64.</p>
<dt><code>call-nop=prefix-addr</code></p>
<dd>
<dt><code>call-nop=suffix-nop</code></p>
<dd>
<dt><code>call-nop=prefix-</code><i>byte</i></p>
<dd>
<dt><code>call-nop=suffix-</code><i>byte</i></p>
<dd>Specify the 1-byte <tt>&quot;NOP&quot;</tt> padding when transforming indirect call to a locally defined function, foo, via its <font SIZE="-1">GOT</font> slot. <code>call-nop=prefix-addr</code> generates <tt>&quot;0x67 call foo&quot;</tt>. <code>call-nop=suffix-nop</code> generates <tt>&quot;call foo 0x90&quot;</tt>. <code>call-nop=prefix-</code><i>byte</i> generates <tt>&quot;</tt>byte<tt> call foo&quot;</tt>. <code>call-nop=suffix-</code><i>byte</i> generates <tt>&quot;call foo </tt>byte<tt>&quot;</tt>. Supported for i386 and x86_64.</p>
<dt><code>cet-report=none</code></p>
<dd>
<dt><code>cet-report=warning</code></p>
<dd>
<dt><code>cet-report=error</code></p>
<dd>Specify how to report the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_IBT</font> and <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_SHSTK</font> properties in input .note.gnu.property section. <code>cet-report=none</code>, which is the default, will make the linker not report missing properties in input files. <code>cet-report=warning</code> will make the linker issue a warning for missing properties in input files. <code>cet-report=error</code> will make the linker issue an error for missing properties in input files. Note that <code>ibt</code> will turn off the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_IBT</font> property report and <code>shstk</code> will turn off the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_SHSTK</font> property report. Supported for Linux/i386 and Linux/x86_64.</p>
<dt><code>combreloc</code></p>
<dd>
<dt><code>nocombreloc</code></p>
<dd>Combine multiple dynamic relocation sections and sort to improve dynamic symbol lookup caching. Do not do this if <code>nocombreloc</code>.</p>
<dt><code>common</code></p>
<dd>
<dt><code>nocommon</code></p>
<dd>Generate common symbols with <font SIZE="-1">STT_COMMON</font> type during a relocatable link. Use <font SIZE="-1">STT_OBJECT</font> type if <code>nocommon</code>.</p>
<dt><code>common-page-size=</code><i>value</i></p>
<dd>Set the page size most commonly used to <i>value</i>. Memory image layout will be optimized to minimize memory pages if the system is using pages of this size.</p>
<dt><code>defs</code></p>
<dd>Report unresolved symbol references from regular object files. This is done even if the linker is creating a non-symbolic shared library. This option is the inverse of <code>-z undefs</code>.</p>
<dt><code>dynamic-undefined-weak</code></p>
<dd>
<dt><code>nodynamic-undefined-weak</code></p>
<dd>Make undefined weak symbols dynamic when building a dynamic object, if they are referenced from a regular object file and not forced local by symbol visibility or versioning. Do not make them dynamic if <code>nodynamic-undefined-weak</code>. If neither option is given, a target may default to either option being in force, or make some other selection of undefined weak symbols dynamic. Not all targets support these options.</p>
<dt><code>execstack</code></p>
<dd>Marks the object as requiring executable stack.</p>
<dt><code>global</code></p>
<dd>This option is only meaningful when building a shared object. It makes the symbols defined by this shared object available for symbol resolution of subsequently loaded libraries.</p>
<dt><code>globalaudit</code></p>
<dd>This option is only meaningful when building a dynamic executable. This option marks the executable as requiring global auditing by setting the <tt>&quot;DF_1_GLOBAUDIT&quot;</tt> bit in the <tt>&quot;DT_FLAGS_1&quot;</tt> dynamic tag. Global auditing requires that any auditing library defined via the <code>&#8211;depaudit</code> or <code>-P</code> command-line options be run for all dynamic objects loaded by the application.</p>
<dt><code>ibtplt</code></p>
<dd>Generate Intel Indirect Branch Tracking (<font SIZE="-1">IBT</font>) enabled <font SIZE="-1">PLT</font> entries. Supported for Linux/i386 and Linux/x86_64.</p>
<dt><code>ibt</code></p>
<dd>Generate <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_IBT</font> in .note.gnu.property section to indicate compatibility with <font SIZE="-1">IBT.</font> This also implies <code>ibtplt</code>. Supported for Linux/i386 and Linux/x86_64.</p>
<dt><code>indirect-extern-access</code></p>
<dd>
<dt><code>noindirect-extern-access</code></p>
<dd>Generate <font SIZE="-1">GNU_PROPERTY_1_NEEDED_INDIRECT_EXTERN_ACCESS</font> in .note.gnu.property section to indicate that object file requires canonical function pointers and cannot be used with copy relocation. This option also implies <code>noextern-protected-data</code> and <code>nocopyreloc</code>. Supported for i386 and x86-64. </p>
<p> <code>noindirect-extern-access</code> removes <font SIZE="-1">GNU_PROPERTY_1_NEEDED_INDIRECT_EXTERN_ACCESS</font> from .note.gnu.property section.</p>
<dt><code>initfirst</code></p>
<dd>This option is only meaningful when building a shared object. It marks the object so that its runtime initialization will occur before the runtime initialization of any other objects brought into the process at the same time. Similarly the runtime finalization of the object will occur after the runtime finalization of any other objects.</p>
<dt><code>interpose</code></p>
<dd>Specify that the dynamic loader should modify its symbol search order so that symbols in this shared library interpose all other shared libraries not so marked.</p>
<dt><code>unique</code></p>
<dd>
<dt><code>nounique</code></p>
<dd>When generating a shared library or other dynamically loadable <font SIZE="-1">ELF</font> object mark it as one that should (by default) only ever be loaded once, and only in the main namespace (when using <tt>&quot;dlmopen&quot;</tt>). This is primarily used to mark fundamental libraries such as libc, libpthread et al which do not usually function correctly unless they are the sole instances of themselves. This behaviour can be overridden by the <tt>&quot;dlmopen&quot;</tt> caller and does not apply to certain loading mechanisms (such as audit libraries).</p>
<dt><code>lam-u48</code></p>
<dd>Generate <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U48</font> in .note.gnu.property section to indicate compatibility with Intel <font SIZE="-1">LAM_U48.</font> Supported for Linux/x86_64.</p>
<dt><code>lam-u57</code></p>
<dd>Generate <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U57</font> in .note.gnu.property section to indicate compatibility with Intel <font SIZE="-1">LAM_U57.</font> Supported for Linux/x86_64.</p>
<dt><code>lam-u48-report=none</code></p>
<dd>
<dt><code>lam-u48-report=warning</code></p>
<dd>
<dt><code>lam-u48-report=error</code></p>
<dd>Specify how to report the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U48</font> property in input .note.gnu.property section. <code>lam-u48-report=none</code>, which is the default, will make the linker not report missing properties in input files. <code>lam-u48-report=warning</code> will make the linker issue a warning for missing properties in input files. <code>lam-u48-report=error</code> will make the linker issue an error for missing properties in input files. Supported for Linux/x86_64.</p>
<dt><code>lam-u57-report=none</code></p>
<dd>
<dt><code>lam-u57-report=warning</code></p>
<dd>
<dt><code>lam-u57-report=error</code></p>
<dd>Specify how to report the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U57</font> property in input .note.gnu.property section. <code>lam-u57-report=none</code>, which is the default, will make the linker not report missing properties in input files. <code>lam-u57-report=warning</code> will make the linker issue a warning for missing properties in input files. <code>lam-u57-report=error</code> will make the linker issue an error for missing properties in input files. Supported for Linux/x86_64.</p>
<dt><code>lam-report=none</code></p>
<dd>
<dt><code>lam-report=warning</code></p>
<dd>
<dt><code>lam-report=error</code></p>
<dd>Specify how to report the missing <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U48</font> and <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_LAM_U57</font> properties in input .note.gnu.property section. <code>lam-report=none</code>, which is the default, will make the linker not report missing properties in input files. <code>lam-report=warning</code> will make the linker issue a warning for missing properties in input files. <code>lam-report=error</code> will make the linker issue an error for missing properties in input files. Supported for Linux/x86_64.</p>
<dt><code>lazy</code></p>
<dd>When generating an executable or shared library, mark it to tell the dynamic linker to defer function call resolution to the point when the function is called (lazy binding), rather than at load time. Lazy binding is the default.</p>
<dt><code>loadfltr</code></p>
<dd>Specify that the object&#8217;s filters be processed immediately at runtime.</p>
<dt><code>max-page-size=</code><i>value</i></p>
<dd>Set the maximum memory page size supported to <i>value</i>.</p>
<dt><code>muldefs</code></p>
<dd>Allow multiple definitions.</p>
<dt><code>nocopyreloc</code></p>
<dd>Disable linker generated .dynbss variables used in place of variables defined in shared libraries. May result in dynamic text relocations.</p>
<dt><code>nodefaultlib</code></p>
<dd>Specify that the dynamic loader search for dependencies of this object should ignore any default library search paths.</p>
<dt><code>nodelete</code></p>
<dd>Specify that the object shouldn&#8217;t be unloaded at runtime.</p>
<dt><code>nodlopen</code></p>
<dd>Specify that the object is not available to <tt>&quot;dlopen&quot;</tt>.</p>
<dt><code>nodump</code></p>
<dd>Specify that the object can not be dumped by <tt>&quot;dldump&quot;</tt>.</p>
<dt><code>noexecstack</code></p>
<dd>Marks the object as not requiring executable stack.</p>
<dt><code>noextern-protected-data</code></p>
<dd>Don&#8217;t treat protected data symbols as external when building a shared library. This option overrides the linker backend default. It can be used to work around incorrect relocations against protected data symbols generated by compiler. Updates on protected data symbols by another module aren&#8217;t visible to the resulting shared library. Supported for i386 and x86-64.</p>
<dt><code>noreloc-overflow</code></p>
<dd>Disable relocation overflow check. This can be used to disable relocation overflow check if there will be no dynamic relocation overflow at run-time. Supported for x86_64.</p>
<dt><code>now</code></p>
<dd>When generating an executable or shared library, mark it to tell the dynamic linker to resolve all symbols when the program is started, or when the shared library is loaded by dlopen, instead of deferring function call resolution to the point when the function is first called.</p>
<dt><code>origin</code></p>
<dd>Specify that the object requires $ORIGIN handling in paths.</p>
<dt><code>pack-relative-relocs</code></p>
<dd>
<dt><code>nopack-relative-relocs</code></p>
<dd>Generate compact relative relocation in position-independent executable and shared library. It adds <tt>&quot;DT_RELR&quot;</tt>, <tt>&quot;DT_RELRSZ&quot;</tt> and <tt>&quot;DT_RELRENT&quot;</tt> entries to the dynamic section. It is ignored when building position-dependent executable and relocatable output. <code>nopack-relative-relocs</code> is the default, which disables compact relative relocation. When linked against the <font SIZE="-1">GNU C</font> Library, a <font SIZE="-1">GLIBC_ABI_DT_RELR</font> symbol version dependency on the shared C Library is added to the output. Supported for i386 and x86-64.</p>
<dt><code>relro</code></p>
<dd>
<dt><code>norelro</code></p>
<dd>Create an <font SIZE="-1">ELF</font> <tt>&quot;PT_GNU_RELRO&quot;</tt> segment header in the object. This specifies a memory segment that should be made read-only after relocation, if supported. Specifying <code>common-page-size</code> smaller than the system page size will render this protection ineffective. Don&#8217;t create an <font SIZE="-1">ELF</font> <tt>&quot;PT_GNU_RELRO&quot;</tt> segment if <code>norelro</code>.</p>
<dt><code>report-relative-reloc</code></p>
<dd>Report dynamic relative relocations generated by linker. Supported for Linux/i386 and Linux/x86_64.</p>
<dt><code>separate-code</code></p>
<dd>
<dt><code>noseparate-code</code></p>
<dd>Create separate code <tt>&quot;PT_LOAD&quot;</tt> segment header in the object. This specifies a memory segment that should contain only instructions and must be in wholly disjoint pages from any other data. Don&#8217;t create separate code <tt>&quot;PT_LOAD&quot;</tt> segment if <code>noseparate-code</code> is used.</p>
<dt><code>shstk</code></p>
<dd>Generate <font SIZE="-1">GNU_PROPERTY_X86_FEATURE_1_SHSTK</font> in .note.gnu.property section to indicate compatibility with Intel Shadow Stack. Supported for Linux/i386 and Linux/x86_64.</p>
<dt><code>stack-size=</code><i>value</i></p>
<dd>Specify a stack size for an <font SIZE="-1">ELF</font> <tt>&quot;PT_GNU_STACK&quot;</tt> segment. Specifying zero will override any default non-zero sized <tt>&quot;PT_GNU_STACK&quot;</tt> segment creation.</p>
<dt><code>start-stop-gc</code></p>
<dd>
<dt><code>nostart-stop-gc</code></p>
<dd>When <code>&#8211;gc-sections</code> is in effect, a reference from a retained section to <tt>&quot;__start_SECNAME&quot;</tt> or <tt>&quot;__stop_SECNAME&quot;</tt> causes all input sections named <tt>&quot;SECNAME&quot;</tt> to also be retained, if <tt>&quot;SECNAME&quot;</tt> is representable as a C identifier and either <tt>&quot;__start_SECNAME&quot;</tt> or <tt>&quot;__stop_SECNAME&quot;</tt> is synthesized by the linker. <code>-z start-stop-gc</code> disables this effect, allowing sections to be garbage collected as if the special synthesized symbols were not defined. <code>-z start-stop-gc</code> has no effect on a definition of <tt>&quot;__start_SECNAME&quot;</tt> or <tt>&quot;__stop_SECNAME&quot;</tt> in an object file or linker script. Such a definition will prevent the linker providing a synthesized <tt>&quot;__start_SECNAME&quot;</tt> or <tt>&quot;__stop_SECNAME&quot;</tt> respectively, and therefore the special treatment by garbage collection for those references.</p>
<dt><code>start-stop-visibility=</code><i>value</i></p>
<dd>Specify the <font SIZE="-1">ELF</font> symbol visibility for synthesized <tt>&quot;__start_SECNAME&quot;</tt> and <tt>&quot;__stop_SECNAME&quot;</tt> symbols. <i>value</i> must be exactly <code>default</code>, <code>internal</code>, <code>hidden</code>, or <code>protected</code>. If no <code>-z start-stop-visibility</code> option is given, <code>protected</code> is used for compatibility with historical practice. However, it&#8217;s highly recommended to use <code>-z start-stop-visibility=hidden</code> in new programs and shared libraries so that these symbols are not exported between shared objects, which is not usually what&#8217;s intended.</p>
<dt><code>text</code></p>
<dd>
<dt><code>notext</code></p>
<dd>
<dt><code>textoff</code></p>
<dd>Report an error if <font SIZE="-1">DT_TEXTREL</font> is set, i.e., if the position-independent or shared object has dynamic relocations in read-only sections. Don&#8217;t report an error if <code>notext</code> or <code>textoff</code>.</p>
<dt><code>undefs</code></p>
<dd>Do not report unresolved symbol references from regular object files, either when creating an executable, or when creating a shared library. This option is the inverse of <code>-z defs</code>.</p>
<dt><code>unique-symbol</code></p>
<dd>
<dt><code>nounique-symbol</code></p>
<dd>Avoid duplicated local symbol names in the symbol string table. Append &quot;.<tt>&quot;number&quot;</tt>&quot; to duplicated local symbol names if <code>unique-symbol</code> is used. <code>nounique-symbol</code> is the default.</p>
<dt><code>x86-64-baseline</code></p>
<dd>
<dt><code>x86-64-v2</code></p>
<dd>
<dt><code>x86-64-v3</code></p>
<dd>
<dt><code>x86-64-v4</code></p>
<dd>Specify the x86-64 <font SIZE="-1">ISA</font> level needed in .note.gnu.property section. <code>x86-64-baseline</code> generates <tt>&quot;GNU_PROPERTY_X86_ISA_1_BASELINE&quot;</tt>. <code>x86-64-v2</code> generates <tt>&quot;GNU_PROPERTY_X86_ISA_1_V2&quot;</tt>. <code>x86-64-v3</code> generates <tt>&quot;GNU_PROPERTY_X86_ISA_1_V3&quot;</tt>. <code>x86-64-v4</code> generates <tt>&quot;GNU_PROPERTY_X86_ISA_1_V4&quot;</tt>. Supported for Linux/i386 and Linux/x86_64.</dl>
</dl>
<dl>
<dd>Other keywords are ignored for Solaris compatibility.</dl>
<dt><code>-(</code> <i>archives</i> <code>-)</code></p>
<dd>
<dt><code>&#8211;start-group</code> <i>archives</i> <code>&#8211;end-group</code></p>
<dd>The <i>archives</i> should be a list of archive files. They may be either explicit file names, or <code>-l</code> options. </p>
<p> The specified archives are searched repeatedly until no new undefined references are created. Normally, an archive is searched only once in the order that it is specified on the command line. If a symbol in that archive is needed to resolve an undefined symbol referred to by an object in an archive that appears later on the command line, the linker would not be able to resolve that reference. By grouping the archives, they will all be searched repeatedly until all possible references are resolved. </p>
<p> Using this option has a significant performance cost. It is best to use it only when there are unavoidable circular references between two or more archives.</p>
<dt><code>&#8211;accept-unknown-input-arch</code></p>
<dd>
<dt><code>&#8211;no-accept-unknown-input-arch</code></p>
<dd>Tells the linker to accept input files whose architecture cannot be recognised. The assumption is that the user knows what they are doing and deliberately wants to link in these unknown input files. This was the default behaviour of the linker, before release 2.14. The default behaviour from release 2.14 onwards is to reject such input files, and so the <code>&#8211;accept-unknown-input-arch</code> option has been added to restore the old behaviour.</p>
<dt><code>&#8211;as-needed</code></p>
<dd>
<dt><code>&#8211;no-as-needed</code></p>
<dd>This option affects <font SIZE="-1">ELF DT_NEEDED</font> tags for dynamic libraries mentioned on the command line after the <code>&#8211;as-needed</code> option. Normally the linker will add a <font SIZE="-1">DT_NEEDED</font> tag for each dynamic library mentioned on the command line, regardless of whether the library is actually needed or not. <code>&#8211;as-needed</code> causes a <font SIZE="-1">DT_NEEDED</font> tag to only be emitted for a library that <i>at that point in the link</i> satisfies a non-weak undefined symbol reference from a regular object file or, if the library is not found in the <font SIZE="-1">DT_NEEDED</font> lists of other needed libraries, a non-weak undefined symbol reference from another needed dynamic library. Object files or libraries appearing on the command line <i>after</i> the library in question do not affect whether the library is seen as needed. This is similar to the rules for extraction of object files from archives. <code>&#8211;no-as-needed</code> restores the default behaviour. </p>
<p> Note: On Linux based systems the <code>&#8211;as-needed</code> option also has an affect on the behaviour of the <code>&#8211;rpath</code> and <code>&#8211;rpath-link</code> options. See the description of <code>&#8211;rpath-link</code> for more details.</p>
<dt><code>&#8211;add-needed</code></p>
<dd>
<dt><code>&#8211;no-add-needed</code></p>
<dd>These two options have been deprecated because of the similarity of their names to the <code>&#8211;as-needed</code> and <code>&#8211;no-as-needed</code> options. They have been replaced by <code>&#8211;copy-dt-needed-entries</code> and <code>&#8211;no-copy-dt-needed-entries</code>.</p>
<dt><code>-assert</code> <i>keyword</i></p>
<dd>This option is ignored for SunOS compatibility.</p>
<dt><code>-Bdynamic</code></p>
<dd>
<dt><code>-dy</code></p>
<dd>
<dt><code>-call_shared</code></p>
<dd>Link against dynamic libraries. This is only meaningful on platforms for which shared libraries are supported. This option is normally the default on such platforms. The different variants of this option are for compatibility with various systems. You may use this option multiple times on the command line: it affects library searching for <code>-l</code> options which follow it.</p>
<dt><code>-Bgroup</code></p>
<dd>Set the <tt>&quot;DF_1_GROUP&quot;</tt> flag in the <tt>&quot;DT_FLAGS_1&quot;</tt> entry in the dynamic section. This causes the runtime linker to handle lookups in this object and its dependencies to be performed only inside the group. <code>&#8211;unresolved-symbols=report-all</code> is implied. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>-Bstatic</code></p>
<dd>
<dt><code>-dn</code></p>
<dd>
<dt><code>-non_shared</code></p>
<dd>
<dt><code>-static</code></p>
<dd>Do not link against shared libraries. This is only meaningful on platforms for which shared libraries are supported. The different variants of this option are for compatibility with various systems. You may use this option multiple times on the command line: it affects library searching for <code>-l</code> options which follow it. This option also implies <code>&#8211;unresolved-symbols=report-all</code>. This option can be used with <code>-shared</code>. Doing so means that a shared library is being created but that all of the library&#8217;s external references must be resolved by pulling in entries from static libraries.</p>
<dt><code>-Bsymbolic</code></p>
<dd>When creating a shared library, bind references to global symbols to the definition within the shared library, if any. Normally, it is possible for a program linked against a shared library to override the definition within the shared library. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>-Bsymbolic-functions</code></p>
<dd>When creating a shared library, bind references to global function symbols to the definition within the shared library, if any. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>-Bno-symbolic</code></p>
<dd>This option can cancel previously specified <code>-Bsymbolic</code> and <code>-Bsymbolic-functions</code>.</p>
<dt><code>&#8211;dynamic-list=</code><i>dynamic-list-file</i></p>
<dd>Specify the name of a dynamic list file to the linker. This is typically used when creating shared libraries to specify a list of global symbols whose references shouldn&#8217;t be bound to the definition within the shared library, or creating dynamically linked executables to specify a list of symbols which should be added to the symbol table in the executable. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries. </p>
<p> The format of the dynamic list is the same as the version node without scope and node name. See <font SIZE="-1"><code>VERSION</code></font> for more information.</p>
<dt><code>&#8211;dynamic-list-data</code></p>
<dd>Include all global data symbols to the dynamic list.</p>
<dt><code>&#8211;dynamic-list-cpp-new</code></p>
<dd>Provide the builtin dynamic list for C<font SIZE="-2">++</font> operator new and delete. It is mainly useful for building shared libstdc++.</p>
<dt><code>&#8211;dynamic-list-cpp-typeinfo</code></p>
<dd>Provide the builtin dynamic list for C<font SIZE="-2">++</font> runtime type identification.</p>
<dt><code>&#8211;check-sections</code></p>
<dd>
<dt><code>&#8211;no-check-sections</code></p>
<dd>Asks the linker <i>not</i> to check section addresses after they have been assigned to see if there are any overlaps. Normally the linker will perform this check, and if it finds any overlaps it will produce suitable error messages. The linker does know about, and does make allowances for sections in overlays. The default behaviour can be restored by using the command-line switch <code>&#8211;check-sections</code>. Section overlap is not usually checked for relocatable links. You can force checking in that case by using the <code>&#8211;check-sections</code> option.</p>
<dt><code>&#8211;copy-dt-needed-entries</code></p>
<dd>
<dt><code>&#8211;no-copy-dt-needed-entries</code></p>
<dd>This option affects the treatment of dynamic libraries referred to by <font SIZE="-1">DT_NEEDED</font> tags <i>inside</i> <font SIZE="-1">ELF</font> dynamic libraries mentioned on the command line. Normally the linker won&#8217;t add a <font SIZE="-1">DT_NEEDED</font> tag to the output binary for each library mentioned in a <font SIZE="-1">DT_NEEDED</font> tag in an input dynamic library. With <code>&#8211;copy-dt-needed-entries</code> specified on the command line however any dynamic libraries that follow it will have their <font SIZE="-1">DT_NEEDED</font> entries added. The default behaviour can be restored with <code>&#8211;no-copy-dt-needed-entries</code>. </p>
<p> This option also has an effect on the resolution of symbols in dynamic libraries. With <code>&#8211;copy-dt-needed-entries</code> dynamic libraries mentioned on the command line will be recursively searched, following their <font SIZE="-1">DT_NEEDED</font> tags to other libraries, in order to resolve symbols required by the output binary. With the default setting however the searching of dynamic libraries that follow it will stop with the dynamic library itself. No <font SIZE="-1">DT_NEEDED</font> links will be traversed to resolve symbols.</p>
<dt><code>&#8211;cref</code></p>
<dd>Output a cross reference table. If a linker map file is being generated, the cross reference table is printed to the map file. Otherwise, it is printed on the standard output. </p>
<p> The format of the table is intentionally simple, so that it may be easily processed by a script if necessary. The symbols are printed out, sorted by name. For each symbol, a list of file names is given. If the symbol is defined, the first file listed is the location of the definition. If the symbol is defined as a common value then any files where this happens appear next. Finally any files that reference the symbol are listed.</p>
<dt><code>&#8211;ctf-variables</code></p>
<dd>
<dt><code>&#8211;no-ctf-variables</code></p>
<dd>The <font SIZE="-1">CTF</font> debuginfo format supports a section which encodes the names and types of variables found in the program which do not appear in any symbol table. These variables clearly cannot be looked up by address by conventional debuggers, so the space used for their types and names is usually wasted: the types are usually small but the names are often not. <code>&#8211;ctf-variables</code> causes the generation of such a section. The default behaviour can be restored with <code>&#8211;no-ctf-variables</code>.</p>
<dt><code>&#8211;ctf-share-types=</code><i>method</i></p>
<dd>Adjust the method used to share types between translation units in <font SIZE="-1">CTF.</font></p>
<dl>
<dd>
<dl>
<dt><code>share-unconflicted</code></p>
<dd>Put all types that do not have ambiguous definitions into the shared dictionary, where debuggers can easily access them, even if they only occur in one translation unit. This is the default.</p>
<dt><code>share-duplicated</code></p>
<dd>Put only types that occur in multiple translation units into the shared dictionary: types with only one definition go into per-translation-unit dictionaries. Types with ambiguous definitions in multiple translation units always go into per-translation-unit dictionaries. This tends to make the <font SIZE="-1">CTF</font> larger, but may reduce the amount of <font SIZE="-1">CTF</font> in the shared dictionary. For very large projects this may speed up opening the <font SIZE="-1">CTF</font> and save memory in the <font SIZE="-1">CTF</font> consumer at runtime.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;no-define-common</code></p>
<dd>This option inhibits the assignment of addresses to common symbols. The script command <tt>&quot;INHIBIT_COMMON_ALLOCATION&quot;</tt> has the same effect. </p>
<p> The <code>&#8211;no-define-common</code> option allows decoupling the decision to assign addresses to Common symbols from the choice of the output file type; otherwise a non-Relocatable output type forces assigning addresses to Common symbols. Using <code>&#8211;no-define-common</code> allows Common symbols that are referenced from a shared library to be assigned addresses only in the main program. This eliminates the unused duplicate space in the shared library, and also prevents any possible confusion over resolving to the wrong duplicate when there are many dynamic modules with specialized search paths for runtime symbol resolution.</p>
<dt><code>&#8211;force-group-allocation</code></p>
<dd>This option causes the linker to place section group members like normal input sections, and to delete the section groups. This is the default behaviour for a final link but this option can be used to change the behaviour of a relocatable link (<code>-r</code>). The script command <tt>&quot;FORCE_GROUP_ALLOCATION&quot;</tt> has the same effect.</p>
<dt><code>&#8211;defsym=</code><i>symbol</i><code>=</code><i>expression</i></p>
<dd>Create a global symbol in the output file, containing the absolute address given by <i>expression</i>. You may use this option as many times as necessary to define multiple symbols in the command line. A limited form of arithmetic is supported for the <i>expression</i> in this context: you may give a hexadecimal constant or the name of an existing symbol, or use <tt>&quot;+&quot;</tt> and <tt>&quot;-&quot;</tt> to add or subtract hexadecimal constants or symbols. If you need more elaborate expressions, consider using the linker command language from a script. <i>Note:</i> there should be no white space between <i>symbol</i>, the equals sign (&quot;<code>=</code>&quot;), and <i>expression</i>. </p>
<p> The linker processes <code>&#8211;defsym</code> arguments and <code>-T</code> arguments in order, placing <code>&#8211;defsym</code> before <code>-T</code> will define the symbol before the linker script from <code>-T</code> is processed, while placing <code>&#8211;defsym</code> after <code>-T</code> will define the symbol after the linker script has been processed. This difference has consequences for expressions within the linker script that use the <code>&#8211;defsym</code> symbols, which order is correct will depend on what you are trying to achieve.</p>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd>
<dt><code>&#8211;no-demangle</code></p>
<dd>These options control whether to demangle symbol names in error messages and other output. When the linker is told to demangle, it tries to present symbol names in a readable fashion: it strips leading underscores if they are used by the object file format, and converts C<font SIZE="-2">++</font> mangled symbol names into user readable names. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler. The linker will demangle by default unless the environment variable <font SIZE="-1"><code>COLLECT_NO_DEMANGLE</code></font> is set. These options may be used to override the default.</p>
<dt><code>-I</code><i>file</i></p>
<dd>
<dt><code>&#8211;dynamic-linker=</code><i>file</i></p>
<dd>Set the name of the dynamic linker. This is only meaningful when generating dynamically linked <font SIZE="-1">ELF</font> executables. The default dynamic linker is normally correct; don&#8217;t use this unless you know what you are doing.</p>
<dt><code>&#8211;no-dynamic-linker</code></p>
<dd>When producing an executable file, omit the request for a dynamic linker to be used at load-time. This is only meaningful for <font SIZE="-1">ELF</font> executables that contain dynamic relocations, and usually requires entry point code that is capable of processing these relocations.</p>
<dt><code>&#8211;embedded-relocs</code></p>
<dd>This option is similar to the <code>&#8211;emit-relocs</code> option except that the relocs are stored in a target-specific section. This option is only supported by the <font SIZE="-1"><code>BFIN</code></font>, <font SIZE="-1"><code>CR16</code></font> and <i>M68K</i> targets.</p>
<dt><code>&#8211;disable-multiple-abs-defs</code></p>
<dd>Do not allow multiple definitions with symbols included in filename invoked by -R or &#8211;just-symbols</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd>
<dt><code>&#8211;no-fatal-warnings</code></p>
<dd>Treat all warnings as errors. The default behaviour can be restored with the option <code>&#8211;no-fatal-warnings</code>.</p>
<dt><code>&#8211;force-exe-suffix</code></p>
<dd>Make sure that an output file has a .exe suffix. </p>
<p> If a successfully built fully linked output file does not have a <tt>&quot;.exe&quot;</tt> or <tt>&quot;.dll&quot;</tt> suffix, this option forces the linker to copy the output file to one of the same name with a <tt>&quot;.exe&quot;</tt> suffix. This option is useful when using unmodified Unix makefiles on a Microsoft Windows host, since some versions of Windows won&#8217;t run an image unless it ends in a <tt>&quot;.exe&quot;</tt> suffix.</p>
<dt><code>&#8211;gc-sections</code></p>
<dd>
<dt><code>&#8211;no-gc-sections</code></p>
<dd>Enable garbage collection of unused input sections. It is ignored on targets that do not support this option. The default behaviour (of not performing this garbage collection) can be restored by specifying <code>&#8211;no-gc-sections</code> on the command line. Note that garbage collection for <font SIZE="-1">COFF</font> and <font SIZE="-1">PE</font> format targets is supported, but the implementation is currently considered to be experimental. </p>
<p> <code>&#8211;gc-sections</code> decides which input sections are used by examining symbols and relocations. The section containing the entry symbol and all sections containing symbols undefined on the command-line will be kept, as will sections containing symbols referenced by dynamic objects. Note that when building shared libraries, the linker must assume that any visible symbol is referenced. Once this initial set of sections has been determined, the linker recursively marks as used any section referenced by their relocations. See <code>&#8211;entry</code>, <code>&#8211;undefined</code>, and <code>&#8211;gc-keep-exported</code>. </p>
<p> This option can be set when doing a partial link (enabled with option <code>-r</code>). In this case the root of symbols kept must be explicitly specified either by one of the options <code>&#8211;entry</code>, <code>&#8211;undefined</code>, or <code>&#8211;gc-keep-exported</code> or by a <tt>&quot;ENTRY&quot;</tt> command in the linker script. </p>
<p> As a <font SIZE="-1">GNU</font> extension, <font SIZE="-1">ELF</font> input sections marked with the <tt>&quot;SHF_GNU_RETAIN&quot;</tt> flag will not be garbage collected.</p>
<dt><code>&#8211;print-gc-sections</code></p>
<dd>
<dt><code>&#8211;no-print-gc-sections</code></p>
<dd>List all sections removed by garbage collection. The listing is printed on stderr. This option is only effective if garbage collection has been enabled via the <code>&#8211;gc-sections</code>) option. The default behaviour (of not listing the sections that are removed) can be restored by specifying <code>&#8211;no-print-gc-sections</code> on the command line.</p>
<dt><code>&#8211;gc-keep-exported</code></p>
<dd>When <code>&#8211;gc-sections</code> is enabled, this option prevents garbage collection of unused input sections that contain global symbols having default or protected visibility. This option is intended to be used for executables where unreferenced sections would otherwise be garbage collected regardless of the external visibility of contained symbols. Note that this option has no effect when linking shared objects since it is already the default behaviour. This option is only supported for <font SIZE="-1">ELF</font> format targets.</p>
<dt><code>&#8211;print-output-format</code></p>
<dd>Print the name of the default output format (perhaps influenced by other command-line options). This is the string that would appear in an <tt>&quot;OUTPUT_FORMAT&quot;</tt> linker script command.</p>
<dt><code>&#8211;print-memory-usage</code></p>
<dd>Print used size, total size and used size of memory regions created with the <font SIZE="-1"><code>MEMORY</code></font> command. This is useful on embedded targets to have a quick view of amount of free memory. The format of the output has one headline and one line per region. It is both human readable and easily parsable by tools. Here is an example of an output: </p>
<pre> Memory region Used Size Region Size %age Used
 ROM: 256 KB 1 MB 25.00%
 RAM: 32 B 2 GB 0.00%</pre>
<dt><code>&#8211;help</code></p>
<dd>Print a summary of the command-line options on the standard output and exit.</p>
<dt><code>&#8211;target-help</code></p>
<dd>Print a summary of all target-specific options on the standard output and exit.</p>
<dt><code>-Map=</code><i>mapfile</i></p>
<dd>Print a link map to the file <i>mapfile</i>. See the description of the <code>-M</code> option, above. If <i>mapfile</i> is just the character <tt>&quot;-&quot;</tt> then the map will be written to stdout. </p>
<p> Specifying a directory as <i>mapfile</i> causes the linker map to be written as a file inside the directory. Normally name of the file inside the directory is computed as the basename of the <i>output</i> file with <tt>&quot;.map&quot;</tt> appended. If however the special character <tt>&quot;%&quot;</tt> is used then this will be replaced by the full path of the output file. Additionally if there are any characters after the <i>%</i> symbol then <tt>&quot;.map&quot;</tt> will no longer be appended. </p>
<pre> -o foo.exe -Map=bar [Creates ./bar]
 -o ../dir/foo.exe -Map=bar [Creates ./bar]
 -o foo.exe -Map=../dir [Creates ../dir/foo.exe.map]
 -o ../dir2/foo.exe -Map=../dir [Creates ../dir/foo.exe.map]
 -o foo.exe -Map=% [Creates ./foo.exe.map]
 -o ../dir/foo.exe -Map=% [Creates ../dir/foo.exe.map]
 -o foo.exe -Map=%.bar [Creates ./foo.exe.bar]
 -o ../dir/foo.exe -Map=%.bar [Creates ../dir/foo.exe.bar]
 -o ../dir2/foo.exe -Map=../dir/% [Creates ../dir/../dir2/foo.exe.map]
 -o ../dir2/foo.exe -Map=../dir/%.bar [Creates ../dir/../dir2/foo.exe.bar]</pre>
<p>It is an error to specify more than one <tt>&quot;%&quot;</tt> character. </p>
<p> If the map file already exists then it will be overwritten by this operation.</p>
<dt><code>&#8211;no-keep-memory</code></p>
<dd><code>ld</code> normally optimizes for speed over memory usage by caching the symbol tables of input files in memory. This option tells <code>ld</code> to instead optimize for memory usage, by rereading the symbol tables as necessary. This may be required if <code>ld</code> runs out of memory space while linking a large executable.</p>
<dt><code>&#8211;no-undefined</code></p>
<dd>
<dt><code>-z defs</code></p>
<dd>Report unresolved symbol references from regular object files. This is done even if the linker is creating a non-symbolic shared library. The switch <code>&#8211;[no-]allow-shlib-undefined</code> controls the behaviour for reporting unresolved references found in shared libraries being linked in. </p>
<p> The effects of this option can be reverted by using <tt>&quot;-z undefs&quot;</tt>.</p>
<dt><code>&#8211;allow-multiple-definition</code></p>
<dd>
<dt><code>-z muldefs</code></p>
<dd>Normally when a symbol is defined multiple times, the linker will report a fatal error. These options allow multiple definitions and the first definition will be used.</p>
<dt><code>&#8211;allow-shlib-undefined</code></p>
<dd>
<dt><code>&#8211;no-allow-shlib-undefined</code></p>
<dd>Allows or disallows undefined symbols in shared libraries. This switch is similar to <code>&#8211;no-undefined</code> except that it determines the behaviour when the undefined symbols are in a shared library rather than a regular object file. It does not affect how undefined symbols in regular object files are handled. </p>
<p> The default behaviour is to report errors for any undefined symbols referenced in shared libraries if the linker is being used to create an executable, but to allow them if the linker is being used to create a shared library. </p>
<p> The reasons for allowing undefined symbol references in shared libraries specified at link time are that:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A shared library specified at link time may not be the same as the one that is available at load time, so the symbol might actually be resolvable at load time.</p>
<dt>&bull;</p>
<dd>There are some operating systems, eg BeOS and <font SIZE="-1">HPPA,</font> where undefined symbols in shared libraries are normal. </p>
<p> The BeOS kernel for example patches shared libraries at load time to select whichever function is most appropriate for the current architecture. This is used, for example, to dynamically select an appropriate memset function.</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;error-handling-script=</code><i>scriptname</i></p>
<dd>If this option is provided then the linker will invoke <i>scriptname</i> whenever an error is encountered. Currently however only two kinds of error are supported: missing symbols and missing libraries. Two arguments will be passed to script: the keyword &#8220;undefined-symbol&#8221; or `missing-lib&quot; and the <i>name</i> of the undefined symbol or missing library. The intention is that the script will provide suggestions to the user as to where the symbol or library might be found. After the script has finished then the normal linker error message will be displayed. </p>
<p> The availability of this option is controlled by a configure time switch, so it may not be present in specific implementations.</p>
<dt><code>&#8211;no-undefined-version</code></p>
<dd>Normally when a symbol has an undefined version, the linker will ignore it. This option disallows symbols with undefined version and a fatal error will be issued instead.</p>
<dt><code>&#8211;default-symver</code></p>
<dd>Create and use a default symbol version (the soname) for unversioned exported symbols.</p>
<dt><code>&#8211;default-imported-symver</code></p>
<dd>Create and use a default symbol version (the soname) for unversioned imported symbols.</p>
<dt><code>&#8211;no-warn-mismatch</code></p>
<dd>Normally <code>ld</code> will give an error if you try to link together input files that are mismatched for some reason, perhaps because they have been compiled for different processors or for different endiannesses. This option tells <code>ld</code> that it should silently permit such possible errors. This option should only be used with care, in cases when you have taken some special action that ensures that the linker errors are inappropriate.</p>
<dt><code>&#8211;no-warn-search-mismatch</code></p>
<dd>Normally <code>ld</code> will give a warning if it finds an incompatible library during a library search. This option silences the warning.</p>
<dt><code>&#8211;no-whole-archive</code></p>
<dd>Turn off the effect of the <code>&#8211;whole-archive</code> option for subsequent archive files.</p>
<dt><code>&#8211;noinhibit-exec</code></p>
<dd>Retain the executable output file whenever it is still usable. Normally, the linker will not produce an output file if it encounters errors during the link process; it exits without writing an output file when it issues any error whatsoever.</p>
<dt><code>-nostdlib</code></p>
<dd>Only search library directories explicitly specified on the command line. Library directories specified in linker scripts (including linker scripts specified on the command line) are ignored.</p>
<dt><code>&#8211;oformat=</code><i>output-format</i></p>
<dd><code>ld</code> may be configured to support more than one kind of object file. If your <code>ld</code> is configured this way, you can use the <code>&#8211;oformat</code> option to specify the binary format for the output object file. Even when <code>ld</code> is configured to support alternative object formats, you don&#8217;t usually need to specify this, as <code>ld</code> should be configured to produce as a default output format the most usual format on each machine. <i>output-format</i> is a text string, the name of a particular format supported by the <font SIZE="-1">BFD</font> libraries. (You can list the available binary formats with <code>objdump -i</code>.) The script command <tt>&quot;OUTPUT_FORMAT&quot;</tt> can also specify the output format, but this option overrides it.</p>
<dt><code>&#8211;out-implib</code> <i>file</i></p>
<dd>Create an import library in <i>file</i> corresponding to the executable the linker is generating (eg. a <font SIZE="-1">DLL</font> or <font SIZE="-1">ELF</font> program). This import library (which should be called <tt>&quot;*.dll.a&quot;</tt> or <tt>&quot;*.a&quot;</tt> for DLLs) may be used to link clients against the generated executable; this behaviour makes it possible to skip a separate import library creation step (eg. <tt>&quot;dlltool&quot;</tt> for DLLs). This option is only available for the i386 <font SIZE="-1">PE</font> and <font SIZE="-1">ELF</font> targetted ports of the linker.</p>
<dt><code>-pie</code></p>
<dd>
<dt><code>&#8211;pic-executable</code></p>
<dd>Create a position independent executable. This is currently only supported on <font SIZE="-1">ELF</font> platforms. Position independent executables are similar to shared libraries in that they are relocated by the dynamic linker to the virtual address the <font SIZE="-1">OS</font> chooses for them (which can vary between invocations). Like normal dynamically linked executables they can be executed and symbols defined in the executable cannot be overridden by shared libraries.</p>
<dt><code>-no-pie</code></p>
<dd>Create a position dependent executable. This is the default.</p>
<dt><code>-qmagic</code></p>
<dd>This option is ignored for Linux compatibility.</p>
<dt><code>-Qy</code></p>
<dd>This option is ignored for <font SIZE="-1">SVR4</font> compatibility.</p>
<dt><code>&#8211;relax</code></p>
<dd>
<dt><code>&#8211;no-relax</code></p>
<dd>An option with machine dependent effects. This option is only supported on a few targets. </p>
<p> On some platforms the <code>&#8211;relax</code> option performs target specific, global optimizations that become possible when the linker resolves addressing in the program, such as relaxing address modes, synthesizing new instructions, selecting shorter version of current instructions, and combining constant values. </p>
<p> On some platforms these link time global optimizations may make symbolic debugging of the resulting executable impossible. This is known to be the case for the Matsushita <font SIZE="-1">MN10200</font> and <font SIZE="-1">MN10300</font> family of processors. </p>
<p> On platforms where the feature is supported, the option <code>&#8211;no-relax</code> will disable it. </p>
<p> On platforms where the feature is not supported, both <code>&#8211;relax</code> and <code>&#8211;no-relax</code> are accepted, but ignored.</p>
<dt><code>&#8211;retain-symbols-file=</code><i>filename</i></p>
<dd>Retain <i>only</i> the symbols listed in the file <i>filename</i>, discarding all others. <i>filename</i> is simply a flat file, with one symbol name per line. This option is especially useful in environments (such as VxWorks) where a large global symbol table is accumulated gradually, to conserve run-time memory. </p>
<p> <code>&#8211;retain-symbols-file</code> does <i>not</i> discard undefined symbols, or symbols needed for relocations. </p>
<p> You may only specify <code>&#8211;retain-symbols-file</code> once in the command line. It overrides <code>-s</code> and <code>-S</code>.</p>
<dt><code>-rpath=</code><i>dir</i></p>
<dd>Add a directory to the runtime library search path. This is used when linking an <font SIZE="-1">ELF</font> executable with shared objects. All <code>-rpath</code> arguments are concatenated and passed to the runtime linker, which uses them to locate shared objects at runtime. </p>
<p> The <code>-rpath</code> option is also used when locating shared objects which are needed by shared objects explicitly included in the link; see the description of the <code>-rpath-link</code> option. Searching <code>-rpath</code> in this way is only supported by native linkers and cross linkers which have been configured with the <code>&#8211;with-sysroot</code> option. </p>
<p> If <code>-rpath</code> is not used when linking an <font SIZE="-1">ELF</font> executable, the contents of the environment variable <tt>&quot;LD_RUN_PATH&quot;</tt> will be used if it is defined. </p>
<p> The <code>-rpath</code> option may also be used on SunOS. By default, on SunOS, the linker will form a runtime search path out of all the <code>-L</code> options it is given. If a <code>-rpath</code> option is used, the runtime search path will be formed exclusively using the <code>-rpath</code> options, ignoring the <code>-L</code> options. This can be useful when using gcc, which adds many <code>-L</code> options which may be on <font SIZE="-1">NFS</font> mounted file systems. </p>
<p> For compatibility with other <font SIZE="-1">ELF</font> linkers, if the <code>-R</code> option is followed by a directory name, rather than a file name, it is treated as the <code>-rpath</code> option.</p>
<dt><code>-rpath-link=</code><i>dir</i></p>
<dd>When using <font SIZE="-1">ELF</font> or SunOS, one shared library may require another. This happens when an <tt>&quot;ld -shared&quot;</tt> link includes a shared library as one of the input files. </p>
<p> When the linker encounters such a dependency when doing a non-shared, non-relocatable link, it will automatically try to locate the required shared library and include it in the link, if it is not included explicitly. In such a case, the <code>-rpath-link</code> option specifies the first set of directories to search. The <code>-rpath-link</code> option may specify a sequence of directory names either by specifying a list of names separated by colons, or by appearing multiple times. </p>
<p> The tokens <i></i>$ORIGIN<i></i> and <i></i>$LIB<i></i> can appear in these search directories. They will be replaced by the full path to the directory containing the program or shared object in the case of <i></i>$ORIGIN<i></i> and either <code>lib</code> &#8211; for 32-bit binaries &#8211; or <code>lib64</code> &#8211; for 64-bit binaries &#8211; in the case of <i></i>$LIB<i></i>. </p>
<p> The alternative form of these tokens &#8211; <i>${</i><font SIZE="-1"><i>ORIGIN</i></font><i>}</i> and <i>${</i><font SIZE="-1"><i>LIB</i></font><i>}</i> can also be used. The token <i></i>$PLATFORM<i></i> is not supported. </p>
<p> This option should be used with caution as it overrides the search path that may have been hard compiled into a shared library. In such a case it is possible to use unintentionally a different search path than the runtime linker would do. </p>
<p> The linker uses the following search paths to locate required shared libraries:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>Any directories specified by <code>-rpath-link</code> options.</p>
<dt>2.</p>
<dd>Any directories specified by <code>-rpath</code> options. The difference between <code>-rpath</code> and <code>-rpath-link</code> is that directories specified by <code>-rpath</code> options are included in the executable and used at runtime, whereas the <code>-rpath-link</code> option is only effective at link time. Searching <code>-rpath</code> in this way is only supported by native linkers and cross linkers which have been configured with the <code>&#8211;with-sysroot</code> option.</p>
<dt>3.</p>
<dd>On an <font SIZE="-1">ELF</font> system, for native linkers, if the <code>-rpath</code> and <code>-rpath-link</code> options were not used, search the contents of the environment variable <tt>&quot;LD_RUN_PATH&quot;</tt>.</p>
<dt>4.</p>
<dd>On SunOS, if the <code>-rpath</code> option was not used, search any directories specified using <code>-L</code> options.</p>
<dt>5.</p>
<dd>For a native linker, search the contents of the environment variable <tt>&quot;LD_LIBRARY_PATH&quot;</tt>.</p>
<dt>6.</p>
<dd>For a native <font SIZE="-1">ELF</font> linker, the directories in <tt>&quot;DT_RUNPATH&quot;</tt> or <tt>&quot;DT_RPATH&quot;</tt> of a shared library are searched for shared libraries needed by it. The <tt>&quot;DT_RPATH&quot;</tt> entries are ignored if <tt>&quot;DT_RUNPATH&quot;</tt> entries exist.</p>
<dt>7.</p>
<dd>For a linker for a Linux system, if the file <i>/etc/ld.so.conf</i> exists, the list of directories found in that file. Note: the path to this file is prefixed with the <tt>&quot;sysroot&quot;</tt> value, if that is defined, and then any <tt>&quot;prefix&quot;</tt> string if the linker was configured with the <code>&#8211;prefix=&lt;path&gt;</code> option.</p>
<dt>8.</p>
<dd>For a native linker on a FreeBSD system, any directories specified by the <tt>&quot;_PATH_ELF_HINTS&quot;</tt> macro defined in the <i>elf-hints.h</i> header file.</p>
<dt>9.</p>
<dd>Any directories specified by a <tt>&quot;SEARCH_DIR&quot;</tt> command in a linker script given on the command line, including scripts specified by <code>-T</code> (but not <code>-dT</code>).</p>
<dt>10.</p>
<dd>The default directories, normally <i>/lib</i> and <i>/usr/lib</i>.</p>
<dt>11.</p>
<dd>Any directories specified by a plugin <font SIZE="-1">LDPT_SET_EXTRA_LIBRARY_PATH.</font></p>
<dt>12.</p>
<dd>Any directories specified by a <tt>&quot;SEARCH_DIR&quot;</tt> command in a default linker script.</dl>
</dl>
<dl>
<dd>Note however on Linux based systems there is an additional caveat: If the <code>&#8211;as-needed</code> option is active <i>and</i> a shared library is located which would normally satisfy the search <i>and</i> this library does not have <font SIZE="-1">DT_NEEDED</font> tag for <i>libc.so</i> <i>and</i> there is a shared library later on in the set of search directories which also satisfies the search <i>and</i> this second shared library does have a <font SIZE="-1">DT_NEEDED</font> tag for <i>libc.so</i> <i>then</i> the second library will be selected instead of the first. </p>
<p> If the required shared library is not found, the linker will issue a warning and continue with the link.</dl>
<dt><code>-shared</code></p>
<dd>
<dt><code>-Bshareable</code></p>
<dd>Create a shared library. This is currently only supported on <font SIZE="-1">ELF, XCOFF</font> and SunOS platforms. On SunOS, the linker will automatically create a shared library if the <code>-e</code> option is not used and there are undefined symbols in the link.</p>
<dt><code>&#8211;sort-common</code></p>
<dd>
<dt><code>&#8211;sort-common=ascending</code></p>
<dd>
<dt><code>&#8211;sort-common=descending</code></p>
<dd>This option tells <code>ld</code> to sort the common symbols by alignment in ascending or descending order when it places them in the appropriate output sections. The symbol alignments considered are sixteen-byte or larger, eight-byte, four-byte, two-byte, and one-byte. This is to prevent gaps between symbols due to alignment constraints. If no sorting order is specified, then descending order is assumed.</p>
<dt><code>&#8211;sort-section=name</code></p>
<dd>This option will apply <tt>&quot;SORT_BY_NAME&quot;</tt> to all wildcard section patterns in the linker script.</p>
<dt><code>&#8211;sort-section=alignment</code></p>
<dd>This option will apply <tt>&quot;SORT_BY_ALIGNMENT&quot;</tt> to all wildcard section patterns in the linker script.</p>
<dt><code>&#8211;spare-dynamic-tags=</code><i>count</i></p>
<dd>This option specifies the number of empty slots to leave in the .dynamic section of <font SIZE="-1">ELF</font> shared objects. Empty slots may be needed by post processing tools, such as the prelinker. The default is 5.</p>
<dt><code>&#8211;split-by-file[=</code><i>size</i><code>]</code></p>
<dd>Similar to <code>&#8211;split-by-reloc</code> but creates a new output section for each input file when <i>size</i> is reached. <i>size</i> defaults to a size of 1 if not given.</p>
<dt><code>&#8211;split-by-reloc[=</code><i>count</i><code>]</code></p>
<dd>Tries to creates extra sections in the output file so that no single output section in the file contains more than <i>count</i> relocations. This is useful when generating huge relocatable files for downloading into certain real time kernels with the <font SIZE="-1">COFF</font> object file format; since <font SIZE="-1">COFF</font> cannot represent more than 65535 relocations in a single section. Note that this will fail to work with object file formats which do not support arbitrary sections. The linker will not split up individual input sections for redistribution, so if a single input section contains more than <i>count</i> relocations one output section will contain that many relocations. <i>count</i> defaults to a value of 32768.</p>
<dt><code>&#8211;stats</code></p>
<dd>Compute and display statistics about the operation of the linker, such as execution time and memory usage.</p>
<dt><code>&#8211;sysroot=</code><i>directory</i></p>
<dd>Use <i>directory</i> as the location of the sysroot, overriding the configure-time default. This option is only supported by linkers that were configured using <code>&#8211;with-sysroot</code>.</p>
<dt><code>&#8211;task-link</code></p>
<dd>This is used by <font SIZE="-1">COFF/PE</font> based targets to create a task-linked object file where all of the global symbols have been converted to statics.</p>
<dt><code>&#8211;traditional-format</code></p>
<dd>For some targets, the output of <code>ld</code> is different in some ways from the output of some existing linker. This switch requests <code>ld</code> to use the traditional format instead. </p>
<p> For example, on SunOS, <code>ld</code> combines duplicate entries in the symbol string table. This can reduce the size of an output file with full debugging information by over 30 percent. Unfortunately, the SunOS <tt>&quot;dbx&quot;</tt> program can not read the resulting program (<tt>&quot;gdb&quot;</tt> has no trouble). The <code>&#8211;traditional-format</code> switch tells <code>ld</code> to not combine duplicate entries.</p>
<dt><code>&#8211;section-start=</code><i>sectionname</i><code>=</code><i>org</i></p>
<dd>Locate a section in the output file at the absolute address given by <i>org</i>. You may use this option as many times as necessary to locate multiple sections in the command line. <i>org</i> must be a single hexadecimal integer; for compatibility with other linkers, you may omit the leading <code>0x</code> usually associated with hexadecimal values. <i>Note:</i> there should be no white space between <i>sectionname</i>, the equals sign (&quot;<code>=</code>&quot;), and <i>org</i>.</p>
<dt><code>-Tbss=</code><i>org</i></p>
<dd>
<dt><code>-Tdata=</code><i>org</i></p>
<dd>
<dt><code>-Ttext=</code><i>org</i></p>
<dd>Same as <code>&#8211;section-start</code>, with <tt>&quot;.bss&quot;</tt>, <tt>&quot;.data&quot;</tt> or <tt>&quot;.text&quot;</tt> as the <i>sectionname</i>.</p>
<dt><code>-Ttext-segment=</code><i>org</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> executable, it will set the address of the first byte of the text segment.</p>
<dt><code>-Trodata-segment=</code><i>org</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> executable or shared object for a target where the read-only data is in its own segment separate from the executable text, it will set the address of the first byte of the read-only data segment.</p>
<dt><code>-Tldata-segment=</code><i>org</i></p>
<dd>When creating an <font SIZE="-1">ELF</font> executable or shared object for x86-64 medium memory model, it will set the address of the first byte of the ldata segment.</p>
<dt><code>&#8211;unresolved-symbols=</code><i>method</i></p>
<dd>Determine how to handle unresolved symbols. There are four possible values for <code>method</code>:</p>
<dl>
<dd>
<dl>
<dt><code>ignore-all</code></p>
<dd>Do not report any unresolved symbols.</p>
<dt><code>report-all</code></p>
<dd>Report all unresolved symbols. This is the default.</p>
<dt><code>ignore-in-object-files</code></p>
<dd>Report unresolved symbols that are contained in shared libraries, but ignore them if they come from regular object files.</p>
<dt><code>ignore-in-shared-libs</code></p>
<dd>Report unresolved symbols that come from regular object files, but ignore them if they come from shared libraries. This can be useful when creating a dynamic binary and it is known that all the shared libraries that it should be referencing are included on the linker&#8217;s command line.</dl>
</dl>
<dl>
<dd>The behaviour for shared libraries on their own can also be controlled by the <code>&#8211;[no-]allow-shlib-undefined</code> option. </p>
<p> Normally the linker will generate an error message for each reported unresolved symbol but the option <code>&#8211;warn-unresolved-symbols</code> can change this to a warning.</dl>
<dt><code>&#8211;dll-verbose</code></p>
<dd>
<dt><code>&#8211;verbose[=</code><i></i><font SIZE="-1"><i>NUMBER</i></font><i></i><code>]</code></p>
<dd>Display the version number for <code>ld</code> and list the linker emulations supported. Display which input files can and cannot be opened. Display the linker script being used by the linker. If the optional <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i> argument &gt; 1, plugin symbol status will also be displayed.</p>
<dt><code>&#8211;version-script=</code><i>version-scriptfile</i></p>
<dd>Specify the name of a version script to the linker. This is typically used when creating shared libraries to specify additional information about the version hierarchy for the library being created. This option is only fully supported on <font SIZE="-1">ELF</font> platforms which support shared libraries; see <font SIZE="-1"><code>VERSION</code></font>. It is partially supported on <font SIZE="-1">PE</font> platforms, which can use version scripts to filter symbol visibility in auto-export mode: any symbols marked <code>local</code> in the version script will not be exported.</p>
<dt><code>&#8211;warn-common</code></p>
<dd>Warn when a common symbol is combined with another common symbol or with a symbol definition. Unix linkers allow this somewhat sloppy practice, but linkers on some other operating systems do not. This option allows you to find potential problems from combining global symbols. Unfortunately, some C libraries use this practice, so you may get some warnings about symbols in the libraries as well as in your programs. </p>
<p> There are three kinds of global symbols, illustrated here by C examples:</p>
<dl>
<dd>
<dl>
<dt><code>int i = 1;</code></p>
<dd>A definition, which goes in the initialized data section of the output file.</p>
<dt><code>extern int i;</code></p>
<dd>An undefined reference, which does not allocate space. There must be either a definition or a common symbol for the variable somewhere.</p>
<dt><code>int i;</code></p>
<dd>A common symbol. If there are only (one or more) common symbols for a variable, it goes in the uninitialized data area of the output file. The linker merges multiple common symbols for the same variable into a single symbol. If they are of different sizes, it picks the largest size. The linker turns a common symbol into a declaration, if there is a definition of the same variable.</dl>
</dl>
<dl>
<dd>The <code>&#8211;warn-common</code> option can produce five kinds of warnings. Each warning consists of a pair of lines: the first describes the symbol just encountered, and the second describes the previous symbol encountered with the same name. One or both of the two symbols will be a common symbol.</p>
<dl>
<dt>1.</p>
<dd>Turning a common symbol into a reference, because there is already a definition for the symbol. </p>
<pre> &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
 overridden by definition
 &lt;file&gt;(&lt;section&gt;): warning: defined here</pre>
<dt>2.</p>
<dd>Turning a common symbol into a reference, because a later definition for the symbol is encountered. This is the same as the previous case, except that the symbols are encountered in a different order. </p>
<pre> &lt;file&gt;(&lt;section&gt;): warning: definition of `&lt;symbol&gt;'
 overriding common
 &lt;file&gt;(&lt;section&gt;): warning: common is here</pre>
<dt>3.</p>
<dd>Merging a common symbol with a previous same-sized common symbol. </p>
<pre> &lt;file&gt;(&lt;section&gt;): warning: multiple common
 of `&lt;symbol&gt;'
 &lt;file&gt;(&lt;section&gt;): warning: previous common is here</pre>
<dt>4.</p>
<dd>Merging a common symbol with a previous larger common symbol. </p>
<pre> &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
 overridden by larger common
 &lt;file&gt;(&lt;section&gt;): warning: larger common is here</pre>
<dt>5.</p>
<dd>Merging a common symbol with a previous smaller common symbol. This is the same as the previous case, except that the symbols are encountered in a different order. </p>
<pre> &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
 overriding smaller common
 &lt;file&gt;(&lt;section&gt;): warning: smaller common is here</pre>
</dl>
</dl>
<dl>
<dd></dl>
<dt><code>&#8211;warn-constructors</code></p>
<dd>Warn if any global constructors are used. This is only useful for a few object file formats. For formats like <font SIZE="-1">COFF</font> or <font SIZE="-1">ELF,</font> the linker can not detect the use of global constructors.</p>
<dt><code>&#8211;warn-multiple-gp</code></p>
<dd>Warn if multiple global pointer values are required in the output file. This is only meaningful for certain processors, such as the Alpha. Specifically, some processors put large-valued constants in a special section. A special register (the global pointer) points into the middle of this section, so that constants can be loaded efficiently via a base-register relative addressing mode. Since the offset in base-register relative mode is fixed and relatively small (e.g., 16 bits), this limits the maximum size of the constant pool. Thus, in large programs, it is often necessary to use multiple global pointer values in order to be able to address all possible constants. This option causes a warning to be issued whenever this case occurs.</p>
<dt><code>&#8211;warn-once</code></p>
<dd>Only warn once for each undefined symbol, rather than once per module which refers to it.</p>
<dt><code>&#8211;warn-section-align</code></p>
<dd>Warn if the address of an output section is changed because of alignment. Typically, the alignment will be set by an input section. The address will only be changed if it not explicitly specified; that is, if the <tt>&quot;SECTIONS&quot;</tt> command does not specify a start address for the section.</p>
<dt><code>&#8211;warn-textrel</code></p>
<dd>Warn if the linker adds <font SIZE="-1">DT_TEXTREL</font> to a position-independent executable or shared object.</p>
<dt><code>&#8211;warn-alternate-em</code></p>
<dd>Warn if an object has alternate <font SIZE="-1">ELF</font> machine code.</p>
<dt><code>&#8211;warn-unresolved-symbols</code></p>
<dd>If the linker is going to report an unresolved symbol (see the option <code>&#8211;unresolved-symbols</code>) it will normally generate an error. This option makes it generate a warning instead.</p>
<dt><code>&#8211;error-unresolved-symbols</code></p>
<dd>This restores the linker&#8217;s default behaviour of generating errors when it is reporting unresolved symbols.</p>
<dt><code>&#8211;whole-archive</code></p>
<dd>For each archive mentioned on the command line after the <code>&#8211;whole-archive</code> option, include every object file in the archive in the link, rather than searching the archive for the required object files. This is normally used to turn an archive file into a shared library, forcing every object to be included in the resulting shared library. This option may be used more than once. </p>
<p> Two notes when using this option from gcc: First, gcc doesn&#8217;t know about this option, so you have to use <code>-Wl,-whole-archive</code>. Second, don&#8217;t forget to use <code>-Wl,-no-whole-archive</code> after your list of archives, because gcc will add its own list of archives to your link and you may not want this flag to affect those as well.</p>
<dt><code>&#8211;wrap=</code><i>symbol</i></p>
<dd>Use a wrapper function for <i>symbol</i>. Any undefined reference to <i>symbol</i> will be resolved to <tt>&quot;__wrap_</tt>symbol<tt>&quot;</tt>. Any undefined reference to <tt>&quot;__real_</tt>symbol<tt>&quot;</tt> will be resolved to <i>symbol</i>. </p>
<p> This can be used to provide a wrapper for a system function. The wrapper function should be called <tt>&quot;__wrap_</tt>symbol<tt>&quot;</tt>. If it wishes to call the system function, it should call <tt>&quot;__real_</tt>symbol<tt>&quot;</tt>. </p>
<p> Here is a trivial example: </p>
<pre> void *
 __wrap_malloc (size_t c)
 {
 printf (&quot;malloc called with %zu
&quot;, c);
 return __real_malloc (c);
 }</pre>
<p>If you link other code with this file using <code>&#8211;wrap malloc</code>, then all calls to <tt>&quot;malloc&quot;</tt> will call the function <tt>&quot;__wrap_malloc&quot;</tt> instead. The call to <tt>&quot;__real_malloc&quot;</tt> in <tt>&quot;__wrap_malloc&quot;</tt> will call the real <tt>&quot;malloc&quot;</tt> function. </p>
<p> You may wish to provide a <tt>&quot;__real_malloc&quot;</tt> function as well, so that links without the <code>&#8211;wrap</code> option will succeed. If you do this, you should not put the definition of <tt>&quot;__real_malloc&quot;</tt> in the same file as <tt>&quot;__wrap_malloc&quot;</tt>; if you do, the assembler may resolve the call before the linker has a chance to wrap it to <tt>&quot;malloc&quot;</tt>. </p>
<p> Only undefined references are replaced by the linker. So, translation unit internal references to <i>symbol</i> are not resolved to <tt>&quot;__wrap_</tt>symbol<tt>&quot;</tt>. In the next example, the call to <tt>&quot;f&quot;</tt> in <tt>&quot;g&quot;</tt> is not resolved to <tt>&quot;__wrap_f&quot;</tt>. </p>
<pre> int
 f (void)
 {
 return 123;
 }
 
 int
 g (void)
 {
 return f();
 }</pre>
<dt><code>&#8211;eh-frame-hdr</code></p>
<dd>
<dt><code>&#8211;no-eh-frame-hdr</code></p>
<dd>Request (<code>&#8211;eh-frame-hdr</code>) or suppress (<code>&#8211;no-eh-frame-hdr</code>) the creation of <tt>&quot;.eh_frame_hdr&quot;</tt> section and <font SIZE="-1">ELF</font> <tt>&quot;PT_GNU_EH_FRAME&quot;</tt> segment header.</p>
<dt><code>&#8211;no-ld-generated-unwind-info</code></p>
<dd>Request creation of <tt>&quot;.eh_frame&quot;</tt> unwind info for linker generated code sections like <font SIZE="-1">PLT.</font> This option is on by default if linker generated unwind info is supported.</p>
<dt><code>&#8211;enable-new-dtags</code></p>
<dd>
<dt><code>&#8211;disable-new-dtags</code></p>
<dd>This linker can create the new dynamic tags in <font SIZE="-1">ELF.</font> But the older <font SIZE="-1">ELF</font> systems may not understand them. If you specify <code>&#8211;enable-new-dtags</code>, the new dynamic tags will be created as needed and older dynamic tags will be omitted. If you specify <code>&#8211;disable-new-dtags</code>, no new dynamic tags will be created. By default, the new dynamic tags are not created. Note that those options are only available for <font SIZE="-1">ELF</font> systems.</p>
<dt><code>&#8211;hash-size=</code><i>number</i></p>
<dd>Set the default size of the linker&#8217;s hash tables to a prime number close to <i>number</i>. Increasing this value can reduce the length of time it takes the linker to perform its tasks, at the expense of increasing the linker&#8217;s memory requirements. Similarly reducing this value can reduce the memory requirements at the expense of speed.</p>
<dt><code>&#8211;hash-style=</code><i>style</i></p>
<dd>Set the type of linker&#8217;s hash table(s). <i>style</i> can be either <tt>&quot;sysv&quot;</tt> for classic <font SIZE="-1">ELF</font> <tt>&quot;.hash&quot;</tt> section, <tt>&quot;gnu&quot;</tt> for new style <font SIZE="-1">GNU</font> <tt>&quot;.gnu.hash&quot;</tt> section or <tt>&quot;both&quot;</tt> for both the classic <font SIZE="-1">ELF</font> <tt>&quot;.hash&quot;</tt> and new style <font SIZE="-1">GNU</font> <tt>&quot;.gnu.hash&quot;</tt> hash tables. The default depends upon how the linker was configured, but for most Linux based systems it will be <tt>&quot;both&quot;</tt>.</p>
<dt><code>&#8211;compress-debug-sections=none</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib-gnu</code></p>
<dd>
<dt><code>&#8211;compress-debug-sections=zlib-gabi</code></p>
<dd>On <font SIZE="-1">ELF</font> platforms, these options control how <font SIZE="-1">DWARF</font> debug sections are compressed using zlib. </p>
<p> <code>&#8211;compress-debug-sections=none</code> doesn&#8217;t compress <font SIZE="-1">DWARF</font> debug sections. <code>&#8211;compress-debug-sections=zlib-gnu</code> compresses <font SIZE="-1">DWARF</font> debug sections and renames them to begin with <code>.zdebug</code> instead of <code>.debug</code>. <code>&#8211;compress-debug-sections=zlib-gabi</code> also compresses <font SIZE="-1">DWARF</font> debug sections, but rather than renaming them it sets the <font SIZE="-1">SHF_COMPRESSED</font> flag in the sections&#8217; headers. </p>
<p> The <code>&#8211;compress-debug-sections=zlib</code> option is an alias for <code>&#8211;compress-debug-sections=zlib-gabi</code>. </p>
<p> Note that this option overrides any compression in input debug sections, so if a binary is linked with <code>&#8211;compress-debug-sections=none</code> for example, then any compressed debug sections in input files will be uncompressed before they are copied into the output binary. </p>
<p> The default compression behaviour varies depending upon the target involved and the configure options used to build the toolchain. The default can be determined by examining the output from the linker&#8217;s <code>&#8211;help</code> option.</p>
<dt><code>&#8211;reduce-memory-overheads</code></p>
<dd>This option reduces memory requirements at ld runtime, at the expense of linking speed. This was introduced to select the old O(n^2) algorithm for link map file generation, rather than the new <a href="/docs/linux/man/n-o/">O</a>(n) algorithm which uses about 40% more memory for symbol storage. </p>
<p> Another effect of the switch is to set the default hash table size to 1021, which again saves memory at the cost of lengthening the linker&#8217;s run time. This is not done however if the <code>&#8211;hash-size</code> switch has been used. </p>
<p> The <code>&#8211;reduce-memory-overheads</code> switch may be also be used to enable other tradeoffs in future versions of the linker.</p>
<dt><code>&#8211;max-cache-size=</code><i>size</i></p>
<dd><code>ld</code> normally caches the relocation information and symbol tables of input files in memory with the unlimited size. This option sets the maximum cache size to <i>size</i>.</p>
<dt><code>&#8211;build-id</code></p>
<dd>
<dt><code>&#8211;build-id=</code><i>style</i></p>
<dd>Request the creation of a <tt>&quot;.note.gnu.build-id&quot;</tt> <font SIZE="-1">ELF</font> note section or a <tt>&quot;.buildid&quot;</tt> <font SIZE="-1">COFF</font> section. The contents of the note are unique bits identifying this linked file. <i>style</i> can be <tt>&quot;uuid&quot;</tt> to use 128 random bits, <tt>&quot;sha1&quot;</tt> to use a 160-bit <font SIZE="-1">SHA1</font> hash on the normative parts of the output contents, <tt>&quot;md5&quot;</tt> to use a 128-bit <font SIZE="-1">MD5</font> hash on the normative parts of the output contents, or <tt>&quot;0x</tt>hexstring<tt>&quot;</tt> to use a chosen bit string specified as an even number of hexadecimal digits (<tt>&quot;-&quot;</tt> and <tt>&quot;:&quot;</tt> characters between digit pairs are ignored). If <i>style</i> is omitted, <tt>&quot;sha1&quot;</tt> is used. </p>
<p> The <tt>&quot;md5&quot;</tt> and <tt>&quot;sha1&quot;</tt> styles produces an identifier that is always the same in an identical output file, but will be unique among all nonidentical output files. It is not intended to be compared as a checksum for the file&#8217;s contents. A linked file may be changed later by other tools, but the build <font SIZE="-1">ID</font> bit string identifying the original linked file does not change. </p>
<p> Passing <tt>&quot;none&quot;</tt> for <i>style</i> disables the setting from any <tt>&quot;--build-id&quot;</tt> options earlier on the command line.</dl>
<p> The i386 <font SIZE="-1">PE</font> linker supports the <code>-shared</code> option, which causes the output to be a dynamically linked library (<font SIZE="-1">DLL</font>) instead of a normal executable. You should name the output <tt>&quot;*.dll&quot;</tt> when you use this option. In addition, the linker fully supports the standard <tt>&quot;*.def&quot;</tt> files, which may be specified on the linker command line like an object file (in fact, it should precede archives it exports symbols from, to ensure that they get linked in, just like a normal object file). </p>
<p> In addition to the options common to all targets, the i386 <font SIZE="-1">PE</font> linker support additional command-line options that are specific to the i386 <font SIZE="-1">PE</font> target. Options that take values may be separated from their values by either a space or an equals sign.</p>
<dl>
<dt><code>&#8211;add-stdcall-alias</code></p>
<dd>If given, symbols with a stdcall suffix (@<i>nn</i>) will be exported as-is and also with the suffix stripped. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;base-file</code> <i>file</i></p>
<dd>Use <i>file</i> as the name of a file in which to save the base addresses of all the relocations needed for generating DLLs with <i>dlltool</i>. [This is an i386 <font SIZE="-1">PE</font> specific option]</p>
<dt><code>&#8211;dll</code></p>
<dd>Create a <font SIZE="-1">DLL</font> instead of a regular executable. You may also use <code>-shared</code> or specify a <tt>&quot;LIBRARY&quot;</tt> in a given <tt>&quot;.def&quot;</tt> file. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-long-section-names</code></p>
<dd>
<dt><code>&#8211;disable-long-section-names</code></p>
<dd>The <font SIZE="-1">PE</font> variants of the <font SIZE="-1">COFF</font> object format add an extension that permits the use of section names longer than eight characters, the normal limit for <font SIZE="-1">COFF.</font> By default, these names are only allowed in object files, as fully-linked executable images do not carry the <font SIZE="-1">COFF</font> string table required to support the longer names. As a <font SIZE="-1">GNU</font> extension, it is possible to allow their use in executable images as well, or to (probably pointlessly!) disallow it in object files, by using these two options. Executable images generated with these long section names are slightly non-standard, carrying as they do a string table, and may generate confusing output when examined with non-GNU PE-aware tools, such as file viewers and dumpers. However, <font SIZE="-1">GDB</font> relies on the use of <font SIZE="-1">PE</font> long section names to find Dwarf-2 debug information sections in an executable image at runtime, and so if neither option is specified on the command-line, <code>ld</code> will enable long section names, overriding the default and technically correct behaviour, when it finds the presence of debug information while linking an executable image and not stripping symbols. [This option is valid for all <font SIZE="-1">PE</font> targeted ports of the linker]</p>
<dt><code>&#8211;enable-stdcall-fixup</code></p>
<dd>
<dt><code>&#8211;disable-stdcall-fixup</code></p>
<dd>If the link finds a symbol that it cannot resolve, it will attempt to do &#8220;fuzzy linking&#8221; by looking for another defined symbol that differs only in the format of the symbol name (cdecl vs stdcall) and will resolve that symbol by linking to the match. For example, the undefined symbol <tt>&quot;_foo&quot;</tt> might be linked to the function <tt>&quot;_foo@12&quot;</tt>, or the undefined symbol <tt>&quot;_bar@16&quot;</tt> might be linked to the function <tt>&quot;_bar&quot;</tt>. When the linker does this, it prints a warning, since it normally should have failed to link, but sometimes import libraries generated from third-party dlls may need this feature to be usable. If you specify <code>&#8211;enable-stdcall-fixup</code>, this feature is fully enabled and warnings are not printed. If you specify <code>&#8211;disable-stdcall-fixup</code>, this feature is disabled and such mismatches are considered to be errors. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;leading-underscore</code></p>
<dd>
<dt><code>&#8211;no-leading-underscore</code></p>
<dd>For most targets default symbol-prefix is an underscore and is defined in target&#8217;s description. By this option it is possible to disable/enable the default underscore symbol-prefix.</p>
<dt><code>&#8211;export-all-symbols</code></p>
<dd>If given, all global symbols in the objects used to build a <font SIZE="-1">DLL</font> will be exported by the <font SIZE="-1">DLL.</font> Note that this is the default if there otherwise wouldn&#8217;t be any exported symbols. When symbols are explicitly exported via <font SIZE="-1">DEF</font> files or implicitly exported via function attributes, the default is to not export anything else unless this option is given. Note that the symbols <tt>&quot;DllMain@12&quot;</tt>, <tt>&quot;DllEntryPoint@0&quot;</tt>, <tt>&quot;DllMainCRTStartup@12&quot;</tt>, and <tt>&quot;impure_ptr&quot;</tt> will not be automatically exported. Also, symbols imported from other DLLs will not be re-exported, nor will symbols specifying the <font SIZE="-1">DLL</font>&#8216;s internal layout such as those beginning with <tt>&quot;_head_&quot;</tt> or ending with <tt>&quot;_iname&quot;</tt>. In addition, no symbols from <tt>&quot;libgcc&quot;</tt>, <tt>&quot;libstd++&quot;</tt>, <tt>&quot;libmingw32&quot;</tt>, or <tt>&quot;crtX.o&quot;</tt> will be exported. Symbols whose names begin with <tt>&quot;__rtti_&quot;</tt> or <tt>&quot;__builtin_&quot;</tt> will not be exported, to help with C<font SIZE="-2">++</font> DLLs. Finally, there is an extensive list of cygwin-private symbols that are not exported (obviously, this applies on when building DLLs for cygwin targets). These cygwin-excludes are: <tt>&quot;_cygwin_dll_entry@12&quot;</tt>, <tt>&quot;_cygwin_crt0_common@8&quot;</tt>, <tt>&quot;_cygwin_noncygwin_dll_entry@12&quot;</tt>, <tt>&quot;_fmode&quot;</tt>, <tt>&quot;_impure_ptr&quot;</tt>, <tt>&quot;cygwin_attach_dll&quot;</tt>, <tt>&quot;cygwin_premain0&quot;</tt>, <tt>&quot;cygwin_premain1&quot;</tt>, <tt>&quot;cygwin_premain2&quot;</tt>, <tt>&quot;cygwin_premain3&quot;</tt>, and <tt>&quot;environ&quot;</tt>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;exclude-symbols</code> <i>symbol</i><code>,</code><i>symbol</i><code>,&#8230;</code></p>
<dd>Specifies a list of symbols which should not be automatically exported. The symbol names may be delimited by commas or colons. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;exclude-all-symbols</code></p>
<dd>Specifies no symbols should be automatically exported. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;file-alignment</code></p>
<dd>Specify the file alignment. Sections in the file will always begin at file offsets which are multiples of this number. This defaults to 512. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;heap</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;heap</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd>Specify the number of bytes of memory to reserve (and optionally commit) to be used as heap for this program. The default is 1MB reserved, 4K committed. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;image-base</code> <i>value</i></p>
<dd>Use <i>value</i> as the base address of your program or dll. This is the lowest memory location that will be used when your program or dll is loaded. To reduce the need to relocate and improve performance of your dlls, each should have a unique base address and not overlap any other dlls. The default is 0x400000 for executables, and 0x10000000 for dlls. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;kill-at</code></p>
<dd>If given, the stdcall suffixes (@<i>nn</i>) will be stripped from symbols before they are exported. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;large-address-aware</code></p>
<dd>If given, the appropriate bit in the &#8220;Characteristics&#8221; field of the <font SIZE="-1">COFF</font> header is set to indicate that this executable supports virtual addresses greater than 2 gigabytes. This should be used in conjunction with the /3GB or /USERVA=<i>value</i> megabytes switch in the &#8220;[operating systems]&#8221; section of the <font SIZE="-1">BOOT.INI.</font> Otherwise, this bit has no effect. [This option is specific to <font SIZE="-1">PE</font> targeted ports of the linker]</p>
<dt><code>&#8211;disable-large-address-aware</code></p>
<dd>Reverts the effect of a previous <code>&#8211;large-address-aware</code> option. This is useful if <code>&#8211;large-address-aware</code> is always set by the compiler driver (e.g. Cygwin gcc) and the executable does not support virtual addresses greater than 2 gigabytes. [This option is specific to <font SIZE="-1">PE</font> targeted ports of the linker]</p>
<dt><code>&#8211;major-image-version</code> <i>value</i></p>
<dd>Sets the major number of the &#8220;image version&#8221;. Defaults to 1. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;major-os-version</code> <i>value</i></p>
<dd>Sets the major number of the &#8220;os version&#8221;. Defaults to 4. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;major-subsystem-version</code> <i>value</i></p>
<dd>Sets the major number of the &#8220;subsystem version&#8221;. Defaults to 4. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-image-version</code> <i>value</i></p>
<dd>Sets the minor number of the &#8220;image version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-os-version</code> <i>value</i></p>
<dd>Sets the minor number of the &#8220;os version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-subsystem-version</code> <i>value</i></p>
<dd>Sets the minor number of the &#8220;subsystem version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;output-def</code> <i>file</i></p>
<dd>The linker will create the file <i>file</i> which will contain a <font SIZE="-1">DEF</font> file corresponding to the <font SIZE="-1">DLL</font> the linker is generating. This <font SIZE="-1">DEF</font> file (which should be called <tt>&quot;*.def&quot;</tt>) may be used to create an import library with <tt>&quot;dlltool&quot;</tt> or may be used as a reference to automatically or implicitly exported symbols. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-auto-image-base</code></p>
<dd>
<dt><code>&#8211;enable-auto-image-base=</code><i>value</i></p>
<dd>Automatically choose the image base for DLLs, optionally starting with base <i>value</i>, unless one is specified using the <tt>&quot;--image-base&quot;</tt> argument. By using a hash generated from the dllname to create unique image bases for each <font SIZE="-1">DLL,</font> in-memory collisions and relocations which can delay program execution are avoided. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;disable-auto-image-base</code></p>
<dd>Do not automatically generate a unique image base. If there is no user-specified image base (<tt>&quot;--image-base&quot;</tt>) then use the platform default. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;dll-search-prefix</code> <i>string</i></p>
<dd>When linking dynamically to a dll without an import library, search for <tt>&quot;&lt;string&gt;&lt;basename&gt;.dll&quot;</tt> in preference to <tt>&quot;lib&lt;basename&gt;.dll&quot;</tt>. This behaviour allows easy distinction between DLLs built for the various &#8220;subplatforms&#8221;: native, cygwin, uwin, pw, etc. For instance, cygwin DLLs typically use <tt>&quot;--dll-search-prefix=cyg&quot;</tt>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-auto-import</code></p>
<dd>Do sophisticated linking of <tt>&quot;_symbol&quot;</tt> to <tt>&quot;__imp__symbol&quot;</tt> for <font SIZE="-1">DATA</font> imports from DLLs, thus making it possible to bypass the dllimport mechanism on the user side and to reference unmangled symbol names. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker] </p>
<p> The following remarks pertain to the original implementation of the feature and are obsolete nowadays for Cygwin and MinGW targets. </p>
<p> Note: Use of the &#8216;auto-import&#8217; extension will cause the text section of the image file to be made writable. This does not conform to the PE-COFF format specification published by Microsoft. </p>
<p> Note &#8211; use of the &#8216;auto-import&#8217; extension will also cause read only data which would normally be placed into the .rdata section to be placed into the .data section instead. This is in order to work around a problem with consts that is described here: <a rel="nofollow" href="http://www.cygwin.com/ml/cygwin/2004-09/msg01101.html">http://www.cygwin.com/ml/cygwin/2004-09/msg01101.html</a> </p>
<p> Using &#8216;auto-import&#8217; generally will &#8216;just work&#8217; &#8212; but sometimes you may see this message: </p>
<p> &quot;variable &#8216;&lt;var&gt;&#8217; can&#8217;t be auto-imported. Please read the documentation for ld&#8217;s <tt>&quot;--enable-auto-import&quot;</tt> for details.&quot; </p>
<p> This message occurs when some (sub)expression accesses an address ultimately given by the sum of two constants (Win32 import tables only allow one). Instances where this may occur include accesses to member fields of struct variables imported from a <font SIZE="-1">DLL,</font> as well as using a constant index into an array variable imported from a <font SIZE="-1">DLL.</font> Any multiword variable (arrays, structs, long long, etc) may trigger this error condition. However, regardless of the exact data type of the offending exported variable, ld will always detect it, issue the warning, and exit. </p>
<p> There are several ways to address this difficulty, regardless of the data type of the exported variable: </p>
<p> One way is to use &#8211;enable-runtime-pseudo-reloc switch. This leaves the task of adjusting references in your client code for runtime environment, so this method works only when runtime environment supports this feature. </p>
<p> A second solution is to force one of the &#8216;constants&#8217; to be a variable &#8212; that is, unknown and un-optimizable at compile time. For arrays, there are two possibilities: a) make the indexee (the array&#8217;s address) a variable, or b) make the &#8216;constant&#8217; index a variable. Thus: </p>
<pre> extern type extern_array[];
 extern_array[1] --&gt;
 { volatile type *t=extern_array; t[1] }</pre>
<p>or </p>
<pre> extern type extern_array[];
 extern_array[1] --&gt;
 { volatile int t=1; extern_array[t] }</pre>
<p>For structs (and most other multiword data types) the only option is to make the struct itself (or the long long, or the &#8230;) variable: </p>
<pre> extern struct s extern_struct;
 extern_struct.field --&gt;
 { volatile struct s *t=&amp;extern_struct; t-&gt;field }</pre>
<p>or </p>
<pre> extern long long extern_ll;
 extern_ll --&gt;
 { volatile long long * local_ll=&amp;extern_ll; *local_ll }</pre>
<p>A third method of dealing with this difficulty is to abandon &#8216;auto-import&#8217; for the offending symbol and mark it with <tt>&quot;__declspec(dllimport)&quot;</tt>. However, in practice that requires using compile-time #defines to indicate whether you are building a <font SIZE="-1">DLL,</font> building client code that will link to the <font SIZE="-1">DLL,</font> or merely building/linking to a static library. In making the choice between the various methods of resolving the &#8216;direct address with constant offset&#8217; problem, you should consider typical real-world usage: </p>
<p> Original: </p>
<pre> --foo.h
 extern int arr[];
 --foo.c
 #include &quot;foo.h&quot;
 void main(int argc, char **argv){
 printf(&quot;%d
&quot;,arr[1]);
 }</pre>
<p>Solution 1: </p>
<pre> --foo.h
 extern int arr[];
 --foo.c
 #include &quot;foo.h&quot;
 void main(int argc, char **argv){
 /* This workaround is for win32 and cygwin; do not &quot;optimize&quot; */
 volatile int *parr = arr;
 printf(&quot;%d
&quot;,parr[1]);
 }</pre>
<p>Solution 2: </p>
<pre> --foo.h
 /* Note: auto-export is assumed (no __declspec(dllexport)) */
 #if (defined(_WIN32) || defined(__CYGWIN__)) &amp;&amp; \
 !(defined(FOO_BUILD_DLL) || defined(FOO_STATIC))
 #define FOO_IMPORT __declspec(dllimport)
 #else
 #define FOO_IMPORT
 #endif
 extern FOO_IMPORT int arr[];
 --foo.c
 #include &quot;foo.h&quot;
 void main(int argc, char **argv){
 printf(&quot;%d
&quot;,arr[1]);
 }</pre>
<p>A fourth way to avoid this problem is to re-code your library to use a functional interface rather than a data interface for the offending variables (e.g. <code>set_foo()</code> and <code>get_foo()</code> accessor functions).</p>
<dt><code>&#8211;disable-auto-import</code></p>
<dd>Do not attempt to do sophisticated linking of <tt>&quot;_symbol&quot;</tt> to <tt>&quot;__imp__symbol&quot;</tt> for <font SIZE="-1">DATA</font> imports from DLLs. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-runtime-pseudo-reloc</code></p>
<dd>If your code contains expressions described in &#8211;enable-auto-import section, that is, <font SIZE="-1">DATA</font> imports from <font SIZE="-1">DLL</font> with non-zero offset, this switch will create a vector of &#8216;runtime pseudo relocations&#8217; which can be used by runtime environment to adjust references to such data in your client code. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;disable-runtime-pseudo-reloc</code></p>
<dd>Do not create pseudo relocations for non-zero offset <font SIZE="-1">DATA</font> imports from DLLs. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-extra-pe-debug</code></p>
<dd>Show additional debug info related to auto-import symbol thunking. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;section-alignment</code></p>
<dd>Sets the section alignment. Sections in memory will always begin at addresses which are a multiple of this number. Defaults to 0x1000. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;stack</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;stack</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd>Specify the number of bytes of memory to reserve (and optionally commit) to be used as stack for this program. The default is 2MB reserved, 4K committed. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;subsystem</code> <i>which</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i><code>.</code><i>minor</i></p>
<dd>Specifies the subsystem under which your program will execute. The legal values for <i>which</i> are <tt>&quot;native&quot;</tt>, <tt>&quot;windows&quot;</tt>, <tt>&quot;console&quot;</tt>, <tt>&quot;posix&quot;</tt>, and <tt>&quot;xbox&quot;</tt>. You may optionally set the subsystem version also. Numeric values are also accepted for <i>which</i>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker] </p>
<p> The following options set flags in the <tt>&quot;DllCharacteristics&quot;</tt> field of the <font SIZE="-1">PE</font> file header: [These options are specific to <font SIZE="-1">PE</font> targeted ports of the linker]</p>
<dt><code>&#8211;high-entropy-va</code></p>
<dd>
<dt><code>&#8211;disable-high-entropy-va</code></p>
<dd>Image is compatible with 64-bit address space layout randomization (<font SIZE="-1">ASLR</font>). This option is enabled by default for 64-bit <font SIZE="-1">PE</font> images. </p>
<p> This option also implies <code>&#8211;dynamicbase</code> and <code>&#8211;enable-reloc-section</code>.</p>
<dt><code>&#8211;dynamicbase</code></p>
<dd>
<dt><code>&#8211;disable-dynamicbase</code></p>
<dd>The image base address may be relocated using address space layout randomization (<font SIZE="-1">ASLR</font>). This feature was introduced with <font SIZE="-1">MS</font> Windows Vista for i386 <font SIZE="-1">PE</font> targets. This option is enabled by default but can be disabled via the <code>&#8211;disable-dynamicbase</code> option. This option also implies <code>&#8211;enable-reloc-section</code>.</p>
<dt><code>&#8211;forceinteg</code></p>
<dd>
<dt><code>&#8211;disable-forceinteg</code></p>
<dd>Code integrity checks are enforced. This option is disabled by default.</p>
<dt><code>&#8211;nxcompat</code></p>
<dd>
<dt><code>&#8211;disable-nxcompat</code></p>
<dd>The image is compatible with the Data Execution Prevention. This feature was introduced with <font SIZE="-1">MS</font> Windows <font SIZE="-1">XP SP2</font> for i386 <font SIZE="-1">PE</font> targets. The option is enabled by default.</p>
<dt><code>&#8211;no-isolation</code></p>
<dd>
<dt><code>&#8211;disable-no-isolation</code></p>
<dd>Although the image understands isolation, do not isolate the image. This option is disabled by default.</p>
<dt><code>&#8211;no-seh</code></p>
<dd>
<dt><code>&#8211;disable-no-seh</code></p>
<dd>The image does not use <font SIZE="-1">SEH.</font> No <font SIZE="-1">SE</font> handler may be called from this image. This option is disabled by default.</p>
<dt><code>&#8211;no-bind</code></p>
<dd>
<dt><code>&#8211;disable-no-bind</code></p>
<dd>Do not bind this image. This option is disabled by default.</p>
<dt><code>&#8211;wdmdriver</code></p>
<dd>
<dt><code>&#8211;disable-wdmdriver</code></p>
<dd>The driver uses the <font SIZE="-1">MS</font> Windows Driver Model. This option is disabled by default.</p>
<dt><code>&#8211;tsaware</code></p>
<dd>
<dt><code>&#8211;disable-tsaware</code></p>
<dd>The image is Terminal Server aware. This option is disabled by default.</p>
<dt><code>&#8211;insert-timestamp</code></p>
<dd>
<dt><code>&#8211;no-insert-timestamp</code></p>
<dd>Insert a real timestamp into the image. This is the default behaviour as it matches legacy code and it means that the image will work with other, proprietary tools. The problem with this default is that it will result in slightly different images being produced each time the same sources are linked. The option <code>&#8211;no-insert-timestamp</code> can be used to insert a zero value for the timestamp, this ensuring that binaries produced from identical sources will compare identically.</p>
<dt><code>&#8211;enable-reloc-section</code></p>
<dd>
<dt><code>&#8211;disable-reloc-section</code></p>
<dd>Create the base relocation table, which is necessary if the image is loaded at a different image base than specified in the <font SIZE="-1">PE</font> header. This option is enabled by default.</dl>
<p> The C6X uClinux target uses a binary format called <font SIZE="-1">DSBT</font> to support shared libraries. Each shared library in the system needs to have a unique index; all executables use an index of 0.</p>
<dl>
<dt><code>&#8211;dsbt-size</code> <i>size</i></p>
<dd>This option sets the number of entries in the <font SIZE="-1">DSBT</font> of the current executable or shared library to <i>size</i>. The default is to create a table with 64 entries.</p>
<dt><code>&#8211;dsbt-index</code> <i>index</i></p>
<dd>This option sets the <font SIZE="-1">DSBT</font> index of the current executable or shared library to <i>index</i>. The default is 0, which is appropriate for generating executables. If a shared library is generated with a <font SIZE="-1">DSBT</font> index of 0, the <tt>&quot;R_C6000_DSBT_INDEX&quot;</tt> relocs are copied into the output file. </p>
<p> The <code>&#8211;no-merge-exidx-entries</code> switch disables the merging of adjacent exidx entries in frame unwind info.</p>
<dt><code>&#8211;branch-stub</code></p>
<dd>This option enables linker branch relaxation by inserting branch stub sections when needed to extend the range of branches. This option is usually not required since C-SKY supports branch and call instructions that can access the full memory range and branch relaxation is normally handled by the compiler or assembler.</p>
<dt><code>&#8211;stub-group-size=</code><i>N</i></p>
<dd>This option allows finer control of linker branch stub creation. It sets the maximum size of a group of input sections that can be handled by one stub section. A negative value of <i>N</i> locates stub sections after their branches, while a positive value allows stub sections to appear either before or after the branches. Values of <code>1</code> or <code>-1</code> indicate that the linker should choose suitable defaults.</dl>
<p> The 68HC11 and 68HC12 linkers support specific options to control the memory bank switching mapping and trampoline code generation.</p>
<dl>
<dt><code>&#8211;no-trampoline</code></p>
<dd>This option disables the generation of trampoline. By default a trampoline is generated for each far function which is called using a <tt>&quot;jsr&quot;</tt> instruction (this happens when a pointer to a far function is taken).</p>
<dt><code>&#8211;bank-window</code> <i>name</i></p>
<dd>This option indicates to the linker the name of the memory region in the <font SIZE="-1"><code>MEMORY</code></font> specification that describes the memory bank window. The definition of such region is then used by the linker to compute paging and addresses within the memory window.</dl>
<p> The following options are supported to control handling of <font SIZE="-1">GOT</font> generation when linking for 68K targets.</p>
<dl>
<dt><code>&#8211;got=</code><i>type</i></p>
<dd>This option tells the linker which <font SIZE="-1">GOT</font> generation scheme to use. <i>type</i> should be one of <code>single</code>, <code>negative</code>, <code>multigot</code> or <code>target</code>. For more information refer to the Info entry for <i>ld</i>.</dl>
<p> The following options are supported to control microMIPS instruction generation and branch relocation checks for <font SIZE="-1">ISA</font> mode transitions when linking for <font SIZE="-1">MIPS</font> targets.</p>
<dl>
<dt><code>&#8211;insn32</code></p>
<dd>
<dt><code>&#8211;no-insn32</code></p>
<dd>These options control the choice of microMIPS instructions used in code generated by the linker, such as that in the <font SIZE="-1">PLT</font> or lazy binding stubs, or in relaxation. If <code>&#8211;insn32</code> is used, then the linker only uses 32-bit instruction encodings. By default or if <code>&#8211;no-insn32</code> is used, all instruction encodings are used, including 16-bit ones where possible.</p>
<dt><code>&#8211;ignore-branch-isa</code></p>
<dd>
<dt><code>&#8211;no-ignore-branch-isa</code></p>
<dd>These options control branch relocation checks for invalid <font SIZE="-1">ISA</font> mode transitions. If <code>&#8211;ignore-branch-isa</code> is used, then the linker accepts any branch relocations and any <font SIZE="-1">ISA</font> mode transition required is lost in relocation calculation, except for some cases of <tt>&quot;BAL&quot;</tt> instructions which meet relaxation conditions and are converted to equivalent <tt>&quot;JALX&quot;</tt> instructions as the associated relocation is calculated. By default or if <code>&#8211;no-ignore-branch-isa</code> is used a check is made causing the loss of an <font SIZE="-1">ISA</font> mode transition to produce an error.</p>
<dt><code>&#8211;compact-branches</code></p>
<dd>
<dt><code>&#8211;no-compact-branches</code></p>
<dd>These options control the generation of compact instructions by the linker in the <font SIZE="-1">PLT</font> entries for <font SIZE="-1">MIPS R6.</font></dl>
<p> For the pdp11-aout target, three variants of the output format can be produced as selected by the following options. The default variant for pdp11-aout is the <code>&#8211;omagic</code> option, whereas for other targets <code>&#8211;nmagic</code> is the default. The <code>&#8211;imagic</code> option is defined only for the pdp11-aout target, while the others are described here as they apply to the pdp11-aout target.</p>
<dl>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;omagic</code></p>
<dd>Mark the output as <tt>&quot;OMAGIC&quot;</tt> (0407) in the <i>a.out</i> header to indicate that the text segment is not to be write-protected and shared. Since the text and data sections are both readable and writable, the data section is allocated immediately contiguous after the text segment. This is the oldest format for <font SIZE="-1">PDP11</font> executable programs and is the default for <code>ld</code> on <font SIZE="-1">PDP11</font> Unix systems from the beginning through 2.11BSD.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;nmagic</code></p>
<dd>Mark the output as <tt>&quot;NMAGIC&quot;</tt> (0410) in the <i>a.out</i> header to indicate that when the output file is executed, the text portion will be read-only and shareable among all processes executing the same file. This involves moving the data areas up to the first possible 8K byte page boundary following the end of the text. This option creates a <i>pure executable</i> format.</p>
<dt><code>-z</code></p>
<dd>
<dt><code>&#8211;imagic</code></p>
<dd>Mark the output as <tt>&quot;IMAGIC&quot;</tt> (0411) in the <i>a.out</i> header to indicate that when the output file is executed, the program text and data areas will be loaded into separate address spaces using the split instruction and data space feature of the memory management unit in larger models of the <font SIZE="-1">PDP11.</font> This doubles the address space available to the program. The text segment is again pure, write-protected, and shareable. The only difference in the output format between this option and the others, besides the magic number, is that both the text and data sections start at location 0. The <code>-z</code> option selected this format in 2.11BSD. This option creates a <i>separate executable</i> format.</p>
<dt><code>&#8211;no-omagic</code></p>
<dd>Equivalent to <code>&#8211;nmagic</code> for pdp11-aout.</dl>
<h2>Environment</h2>
<p>You can change the behaviour of <code>ld</code> with the environment variables <tt>&quot;GNUTARGET&quot;</tt>, <tt>&quot;LDEMULATION&quot;</tt> and <tt>&quot;COLLECT_NO_DEMANGLE&quot;</tt>. </p>
<p> <tt>&quot;GNUTARGET&quot;</tt> determines the input-file object format if you don&#8217;t use <code>-b</code> (or its synonym <code>&#8211;format</code>). Its value should be one of the <font SIZE="-1">BFD</font> names for an input format. If there is no <tt>&quot;GNUTARGET&quot;</tt> in the environment, <code>ld</code> uses the natural format of the target. If <tt>&quot;GNUTARGET&quot;</tt> is set to <tt>&quot;default&quot;</tt> then <font SIZE="-1">BFD</font> attempts to discover the input format by examining binary input files; this method often succeeds, but there are potential ambiguities, since there is no method of ensuring that the magic number used to specify object-file formats is unique. However, the configuration procedure for <font SIZE="-1">BFD</font> on each system places the conventional format for that system first in the search-list, so ambiguities are resolved in favor of convention. </p>
<p> <tt>&quot;LDEMULATION&quot;</tt> determines the default emulation if you don&#8217;t use the <code>-m</code> option. The emulation can affect various aspects of linker behaviour, particularly the default linker script. You can list the available emulations with the <code>&#8211;verbose</code> or <code>-V</code> options. If the <code>-m</code> option is not used, and the <tt>&quot;LDEMULATION&quot;</tt> environment variable is not defined, the default emulation depends upon how the linker was configured. </p>
<p> Normally, the linker will default to demangling symbols. However, if <tt>&quot;COLLECT_NO_DEMANGLE&quot;</tt> is set in the environment, then it will default to not demangling symbols. This environment variable is used in a similar fashion by the <tt>&quot;gcc&quot;</tt> linker wrapper program. The default may be overridden by the <code>&#8211;demangle</code> and <code>&#8211;no-demangle</code> options.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ar/">ar</a></code>(1), <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1), <code><a href="/docs/linux/man/1-objcopy/">objcopy</a></code>(1), <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), <code><a href="/docs/linux/man/1-readelf/">readelf</a></code>(1) and the Info entries for <i>binutils</i> and <i>ld</i>.</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;.</p>
