---
title: "arm-gp2x-linux-ld(1)"
name: "arm-gp2x-linux-ld"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-ld/"
description: "ld – Using LD, the GNU linker"
---

<h2>NAME</h2>
<p> ld &#8211; Using LD, the GNU linker</p>
<h2>SYNOPSIS</h2>
<p> ld [<code>options</code>] <i>objfile</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>ld</code> combines a number of object and archive files, relocates their data and ties up symbol references. Usually the last step in compiling a program is to run <code>ld</code>. </p>
<p> <code>ld</code> accepts Linker Command Language files written in a superset of <font SIZE="-1">AT&amp;T</font>&#8216;s Link Editor Command Language syntax, to provide explicit and total control over the linking process. </p>
<p> This man page does not describe the command language; see the <code>ld</code> entry in <tt>&quot;info&quot;</tt>, or the manual ld: the <font SIZE="-1">GNU</font> linker, for full details on the command language and on other aspects of the <font SIZE="-1">GNU</font> linker. </p>
<p> This version of <code>ld</code> uses the general purpose <font SIZE="-1">BFD</font> libraries to operate on object files. This allows <code>ld</code> to read, combine, and write object files in many different formats&#8212;for example, <font SIZE="-1">COFF</font> or <tt>&quot;a.out&quot;</tt>. Different formats may be linked together to produce any available kind of object file. </p>
<p> Aside from its flexibility, the <font SIZE="-1">GNU</font> linker is more helpful than other linkers in providing diagnostic information. Many linkers abandon execution immediately upon encountering an error; whenever possible, <code>ld</code> continues executing, allowing you to identify other errors (or, in some cases, to get an output file in spite of the error). </p>
<p> The <font SIZE="-1">GNU</font> linker <code>ld</code> is meant to cover a broad range of situations, and to be as compatible as possible with other linkers. As a result, you have many choices to control its behavior.</p>
<h2>OPTIONS</h2>
<p> The linker supports a plethora of command-line options, but in actual practice few of them are used in any particular context. For instance, a frequent use of <code>ld</code> is to link standard Unix object files on a standard, supported Unix system. On such a system, to link a file <tt>&quot;hello.o&quot;</tt>: </p>
<pre>
        ld -o &lt;output&gt; /lib/crt0.o hello.o -lc
</pre>
<p> This tells <code>ld</code> to produce a file called <i>output</i> as the result of linking the file <tt>&quot;/lib/crt0.o&quot;</tt> with <tt>&quot;hello.o&quot;</tt> and the library <tt>&quot;libc.a&quot;</tt>, which will come from the standard search directories. (See the discussion of the <code>-l</code> option below.) </p>
<p> Some of the command-line options to <code>ld</code> may be specified at any point in the command line. However, options which refer to files, such as <code>-l</code> or <code>-T</code>, cause the file to be read at the point at which the option appears in the command line, relative to the object files and other file options. Repeating non-file options with a different argument will either have no further effect, or override prior occurrences (those further to the left on the command line) of that option. Options which may be meaningfully specified more than once are noted in the descriptions below. </p>
<p> Non-option arguments are object files or archives which are to be linked together. They may follow, precede, or be mixed in with command-line options, except that an object file argument may not be placed between an option and its argument. </p>
<p> Usually the linker is invoked with at least one object file, but you can specify other forms of binary input files using <code>-l</code>, <code>-R</code>, and the script command language. If <i>no</i> binary input files at all are specified, the linker does not produce any output, and issues the message <code>No input files</code>. </p>
<p> If the linker cannot recognize the format of an object file, it will assume that it is a linker script. A script specified in this way augments the main linker script used for the link (either the default linker script or the one specified by using <code>-T</code>). This feature permits the linker to link against a file which appears to be an object or an archive, but actually merely defines some symbol values, or uses <tt>&quot;INPUT&quot;</tt> or <tt>&quot;GROUP&quot;</tt> to load other objects. Note that specifying a script in this way merely augments the main linker script; use the <code>-T</code> option to replace the default linker script entirely. </p>
<p> For options whose names are a single letter, option arguments must either follow the option letter without intervening whitespace, or be given as separate arguments immediately following the option that requires them. </p>
<p> For options whose names are multiple letters, either one dash or two can precede the option name; for example, <code>-trace-symbol</code> and <code>&#8211;trace-symbol</code> are equivalent. Note&#8212;there is one exception to this rule. Multiple letter options that start with a lower case &#8216;o&#8217; can only be preceeded by two dashes. This is to reduce confusion with the <code>-o</code> option. So for example <code>-omagic</code> sets the output file name to <code>magic</code> whereas <code>&#8211;omagic</code> sets the <font SIZE="-1">NMAGIC</font> flag on the output. </p>
<p> Arguments to multiple-letter options must either be separated from the option name by an equals sign, or be given as separate arguments immediately following the option that requires them. For example, <code>&#8211;trace-symbol foo</code> and <code>&#8211;trace-symbol=foo</code> are equivalent. Unique abbreviations of the names of multiple-letter options are accepted. </p>
<p> Note&#8212;if the linker is being invoked indirectly, via a compiler driver (e.g. <code>gcc</code>) then all the linker command line options should be prefixed by <code>-Wl,</code> (or whatever is appropriate for the particular compiler driver) like this: </p>
<pre>
          gcc -Wl,--startgroup foo.o bar.o -Wl,--endgroup
</pre>
<p> This is important, because otherwise the compiler driver program may silently drop the linker options, resulting in a bad link. </p>
<p> Here is a table of the generic command line switches accepted by the <font SIZE="-1">GNU</font> linker:</p>
<dl>
<dt><code>-a</code><i>keyword</i></p>
<dd> This option is supported for <font SIZE="-1">HP/UX</font> compatibility. The <i>keyword</i> argument must be one of the strings <code>archive</code>, <code>shared</code>, or <code>default</code>. <code>-aarchive</code> is functionally equivalent to <code>-Bstatic</code>, and the other two keywords are functionally equivalent to <code>-Bdynamic</code>. This option may be used any number of times.</p>
<dt><code>-A</code><i>architecture</i></p>
<dd>
<dt><code>&#8211;architecture=</code><i>architecture</i></p>
<dd> In the current release of <code>ld</code>, this option is useful only for the Intel 960 family of architectures. In that <code>ld</code> configuration, the <i>architecture</i> argument identifies the particular architecture in the 960 family, enabling some safeguards and modifying the archive-library search path. </p>
<p> Future releases of <code>ld</code> may support similar functionality for other architecture families.</p>
<dt><code>-b</code> <i>input-format</i></p>
<dd>
<dt><code>&#8211;format=</code><i>input-format</i></p>
<dd> <code>ld</code> may be configured to support more than one kind of object file. If your <code>ld</code> is configured this way, you can use the <code>-b</code> option to specify the binary format for input object files that follow this option on the command line. Even when <code>ld</code> is configured to support alternative object formats, you don&#8217;t usually need to specify this, as <code>ld</code> should be configured to expect as a default input format the most usual format on each machine. <i>input-format</i> is a text string, the name of a particular format supported by the <font SIZE="-1">BFD</font> libraries. (You can list the available binary formats with <code>objdump -i</code>.) </p>
<p> You may want to use this option if you are linking files with an unusual binary format. You can also use <code>-b</code> to switch formats explicitly (when linking object files of different formats), by including <code>-b</code> <i>input-format</i> before each group of object files in a particular format. </p>
<p> The default format is taken from the environment variable <tt>&quot;GNUTARGET&quot;</tt>. </p>
<p> You can also define the input format from a script, using the command <tt>&quot;TARGET&quot;</tt>;</p>
<dt><code>-c</code> <i>MRI-commandfile</i></p>
<dd>
<dt><code>&#8211;mri-script=</code><i>MRI-commandfile</i></p>
<dd> For compatibility with linkers produced by <font SIZE="-1">MRI</font>, <code>ld</code> accepts script files written in an alternate, restricted command language, described in the <font SIZE="-1">MRI</font> Compatible Script Files section of <font SIZE="-1">GNU</font> ld documentation. Introduce <font SIZE="-1">MRI</font> script files with the option <code>-c</code>; use the <code>-T</code> option to run linker scripts written in the general-purpose <code>ld</code> scripting language. If <i>MRI-cmdfile</i> does not exist, <code>ld</code> looks for it in the directories specified by any <code>-L</code> options.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>-dc</code></p>
<dd>
<dt><code>-dp</code></p>
<dd> These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even if a relocatable output file is specified (with <code>-r</code>). The script command <tt>&quot;FORCE_COMMON_ALLOCATION&quot;</tt> has the same effect.</p>
<dt><code>-e</code> <i>entry</i></p>
<dd>
<dt><code>&#8211;entry=</code><i>entry</i></p>
<dd> Use <i>entry</i> as the explicit symbol for beginning execution of your program, rather than the default entry point. If there is no symbol named <i>entry</i>, the linker will try to parse <i>entry</i> as a number, and use that as the entry address (the number will be interpreted in base 10; you may use a leading <code>0x</code> for base 16, or a leading <code>0</code> for base 8).</p>
<dt><code>&#8211;exclude-libs</code> <i>lib</i><code>,</code><i>lib</i><code>,&#8230;</code></p>
<dd> Specifies a list of archive libraries from which symbols should not be automatically exported. The library names may be delimited by commas or colons. Specifying <tt>&quot;--exclude-libs ALL&quot;</tt> excludes symbols in all archive libraries from automatic export. This option is available only for the i386 <font SIZE="-1">PE</font> targeted port of the linker and for <font SIZE="-1">ELF</font> targeted ports. For i386 <font SIZE="-1">PE</font>, symbols explicitly listed in a .def file are still exported, regardless of this option. For <font SIZE="-1">ELF</font> targeted ports, symbols affected by this option will be treated as hidden.</p>
<dt><code>-E</code></p>
<dd>
<dt><code>&#8211;export-dynamic</code></p>
<dd> When creating a dynamically linked executable, add all symbols to the dynamic symbol table. The dynamic symbol table is the set of symbols which are visible from dynamic objects at run time. </p>
<p> If you do not use this option, the dynamic symbol table will normally contain only those symbols which are referenced by some dynamic object mentioned in the link. </p>
<p> If you use <tt>&quot;dlopen&quot;</tt> to load a dynamic object which needs to refer back to the symbols defined by the program, rather than some other dynamic object, then you will probably need to use this option when linking the program itself. </p>
<p> You can also use the version script to control what symbols should be added to the dynamic symbol table if the output format supports it. See the description of <code>&#8211;version-script</code> in <tt>@ref</tt>{<font SIZE="-1">VERSION</font>}.</p>
<dt><code>-EB</code></p>
<dd> Link big-endian objects. This affects the default output format.</p>
<dt><code>-EL</code></p>
<dd> Link little-endian objects. This affects the default output format.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;auxiliary</code> <i>name</i></p>
<dd> When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_AUXILIARY</font> field to the specified name. This tells the dynamic linker that the symbol table of the shared object should be used as an auxiliary filter on the symbol table of the shared object <i>name</i>. </p>
<p> If you later link a program against this filter object, then, when you run the program, the dynamic linker will see the <font SIZE="-1">DT_AUXILIARY</font> field. If the dynamic linker resolves any symbols from the filter object, it will first check whether there is a definition in the shared object <i>name</i>. If there is one, it will be used instead of the definition in the filter object. The shared object <i>name</i> need not exist. Thus the shared object <i>name</i> may be used to provide an alternative implementation of certain functions, perhaps for debugging or for machine specific performance. </p>
<p> This option may be specified more than once. The <font SIZE="-1">DT_AUXILIARY</font> entries will be created in the order in which they appear on the command line.</p>
<dt><code>-F</code> <i>name</i></p>
<dd>
<dt><code>&#8211;filter</code> <i>name</i></p>
<dd> When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_FILTER</font> field to the specified name. This tells the dynamic linker that the symbol table of the shared object which is being created should be used as a filter on the symbol table of the shared object <i>name</i>. </p>
<p> If you later link a program against this filter object, then, when you run the program, the dynamic linker will see the <font SIZE="-1">DT_FILTER</font> field. The dynamic linker will resolve symbols according to the symbol table of the filter object as usual, but it will actually link to the definitions found in the shared object <i>name</i>. Thus the filter object can be used to select a subset of the symbols provided by the object <i>name</i>. </p>
<p> Some older linkers used the <code>-F</code> option throughout a compilation toolchain for specifying object-file format for both input and output object files. The <font SIZE="-1">GNU</font> linker uses other mechanisms for this purpose: the <code>-b</code>, <code>&#8211;format</code>, <code>&#8211;oformat</code> options, the <tt>&quot;TARGET&quot;</tt> command in linker scripts, and the <tt>&quot;GNUTARGET&quot;</tt> environment variable. The <font SIZE="-1">GNU</font> linker will ignore the <code>-F</code> option when not creating an <font SIZE="-1">ELF</font> shared object.</p>
<dt><code>-fini</code> <i>name</i></p>
<dd> When creating an <font SIZE="-1">ELF</font> executable or shared object, call <font SIZE="-1">NAME</font> when the executable or shared object is unloaded, by setting <font SIZE="-1">DT_FINI</font> to the address of the function. By default, the linker uses <tt>&quot;_fini&quot;</tt> as the function to call.</p>
<dt><code>-g</code></p>
<dd> Ignored. Provided for compatibility with other tools.</p>
<dt><code>-G</code><i>value</i></p>
<dd>
<dt><code>&#8211;gpsize=</code><i>value</i></p>
<dd> Set the maximum size of objects to be optimized using the <font SIZE="-1">GP</font> register to <i>size</i>. This is only meaningful for object file formats such as <font SIZE="-1">MIPS</font> <font SIZE="-1">ECOFF</font> which supports putting large and small objects into different sections. This is ignored for other object file formats.</p>
<dt><code>-h</code><i>name</i></p>
<dd>
<dt><code>-soname=</code><i>name</i></p>
<dd> When creating an <font SIZE="-1">ELF</font> shared object, set the internal <font SIZE="-1">DT_SONAME</font> field to the specified name. When an executable is linked with a shared object which has a <font SIZE="-1">DT_SONAME</font> field, then when the executable is run the dynamic linker will attempt to load the shared object specified by the <font SIZE="-1">DT_SONAME</font> field rather than the using the file name given to the linker.</p>
<dt><code>-i</code></p>
<dd> Perform an incremental link (same as option <code>-r</code>).</p>
<dt><code>-init</code> <i>name</i></p>
<dd> When creating an <font SIZE="-1">ELF</font> executable or shared object, call <font SIZE="-1">NAME</font> when the executable or shared object is loaded, by setting <font SIZE="-1">DT_INIT</font> to the address of the function. By default, the linker uses <tt>&quot;_init&quot;</tt> as the function to call.</p>
<dt><code>-l</code><i>archive</i></p>
<dd>
<dt><code>&#8211;library=</code><i>archive</i></p>
<dd> Add archive file <i>archive</i> to the list of files to link. This option may be used any number of times. <code>ld</code> will search its path-list for occurrences of <tt>&quot;lib</tt>archive<tt>.a&quot;</tt> for every <i>archive</i> specified. </p>
<p> On systems which support shared libraries, <code>ld</code> may also search for libraries with extensions other than <tt>&quot;.a&quot;</tt>. Specifically, on <font SIZE="-1">ELF</font> and SunOS systems, <code>ld</code> will search a directory for a library with an extension of <tt>&quot;.so&quot;</tt> before searching for one with an extension of <tt>&quot;.a&quot;</tt>. By convention, a <tt>&quot;.so&quot;</tt> extension indicates a shared library. </p>
<p> The linker will search an archive only once, at the location where it is specified on the command line. If the archive defines a symbol which was undefined in some object which appeared before the archive on the command line, the linker will include the appropriate file(s) from the archive. However, an undefined symbol in an object appearing later on the command line will not cause the linker to search the archive again. </p>
<p> See the <code>-(</code> option for a way to force the linker to search archives multiple times. </p>
<p> You may list the same archive multiple times on the command line. </p>
<p> This type of archive searching is standard for Unix linkers. However, if you are using <code>ld</code> on <font SIZE="-1">AIX</font>, note that it is different from the behaviour of the <font SIZE="-1">AIX</font> linker.</p>
<dt><code>-L</code><i>searchdir</i></p>
<dd>
<dt><code>&#8211;library-path=</code><i>searchdir</i></p>
<dd> Add path <i>searchdir</i> to the list of paths that <code>ld</code> will search for archive libraries and <code>ld</code> control scripts. You may use this option any number of times. The directories are searched in the order in which they are specified on the command line. Directories specified on the command line are searched before the default directories. All <code>-L</code> options apply to all <code>-l</code> options, regardless of the order in which the options appear. </p>
<p> If <i>searchdir</i> begins with <tt>&quot;=&quot;</tt>, then the <tt>&quot;=&quot;</tt> will be replaced by the <i>sysroot prefix</i>, a path specified when the linker is configured. </p>
<p> The default set of paths searched (without being specified with <code>-L</code>) depends on which emulation mode <code>ld</code> is using, and in some cases also on how it was configured. </p>
<p> The paths can also be specified in a link script with the <tt>&quot;SEARCH_DIR&quot;</tt> command. Directories specified this way are searched at the point in which the linker script appears in the command line.</p>
<dt><code>-m</code><i>emulation</i></p>
<dd> Emulate the <i>emulation</i> linker. You can list the available emulations with the <code>&#8211;verbose</code> or <code>-V</code> options. </p>
<p> If the <code>-m</code> option is not used, the emulation is taken from the <tt>&quot;LDEMULATION&quot;</tt> environment variable, if that is defined. </p>
<p> Otherwise, the default emulation depends upon how the linker was configured.</p>
<dt><code>-M</code></p>
<dd>
<dt><code>&#8211;print-map</code></p>
<dd> Print a link map to the standard output. A link map provides information about the link, including the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Where object files and symbols are mapped into memory.</p>
<dt>*</p>
<dd> How common symbols are allocated.</p>
<dt>*</p>
<dd> All archive members included in the link, with a mention of the symbol which caused the archive member to be brought in.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;nmagic</code></p>
<dd> Turn off page alignment of sections, and mark the output as <tt>&quot;NMAGIC&quot;</tt> if possible.</p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;omagic</code></p>
<dd> Set the text and data sections to be readable and writable. Also, do not page-align the data segment, and disable linking against shared libraries. If the output format supports Unix style magic numbers, mark the output as <tt>&quot;OMAGIC&quot;</tt>. Note: Although a writable text section is allowed for PE-COFF targets, it does not conform to the format specification published by Microsoft.</p>
<dt><code>&#8211;no-omagic</code></p>
<dd> This option negates most of the effects of the <code>-N</code> option. It sets the text section to be read-only, and forces the data segment to be page-aligned. Note &#8211; this option does not enable linking against shared libraries. Use <code>-Bdynamic</code> for this.</p>
<dt><code>-o</code> <i>output</i></p>
<dd>
<dt><code>&#8211;output=</code><i>output</i></p>
<dd> Use <i>output</i> as the name for the program produced by <code>ld</code>; if this option is not specified, the name <i>a.out</i> is used by default. The script command <tt>&quot;OUTPUT&quot;</tt> can also specify the output file name.</p>
<dt><code>-O</code> <i>level</i></p>
<dd> If <i>level</i> is a numeric values greater than zero <code>ld</code> optimizes the output. This might take significantly longer and therefore probably should only be enabled for the final binary.</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;emit-relocs</code></p>
<dd> Leave relocation sections and contents in fully linked exececutables. Post link analysis and optimization tools may need this information in order to perform correct modifications of executables. This results in larger executables. </p>
<p> This option is currently only supported on <font SIZE="-1">ELF</font> platforms.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;relocatable</code></p>
<dd> Generate relocatable output&#8212;i.e., generate an output file that can in turn serve as input to <code>ld</code>. This is often called <i>partial linking</i>. As a side effect, in environments that support standard Unix magic numbers, this option also sets the output file&#8217;s magic number to <tt>&quot;OMAGIC&quot;</tt>. If this option is not specified, an absolute file is produced. When linking C<font SIZE="-2">++</font> programs, this option <i>will not</i> resolve references to constructors; to do that, use <code>-Ur</code>. </p>
<p> When an input file does not have the same format as the output file, partial linking is only supported if that input file does not contain any relocations. Different output formats can have further restrictions; for example some <tt>&quot;a.out&quot;</tt>-based formats do not support partial linking with input files in other formats at all. </p>
<p> This option does the same thing as <code>-i</code>.</p>
<dt><code>-R</code> <i>filename</i></p>
<dd>
<dt><code>&#8211;just-symbols=</code><i>filename</i></p>
<dd> Read symbol names and their addresses from <i>filename</i>, but do not relocate it or include it in the output. This allows your output file to refer symbolically to absolute locations of memory defined in other programs. You may use this option more than once. </p>
<p> For compatibility with other <font SIZE="-1">ELF</font> linkers, if the <code>-R</code> option is followed by a directory name, rather than a file name, it is treated as the <code>-rpath</code> option.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;strip-all</code></p>
<dd> Omit all symbol information from the output file.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;strip-debug</code></p>
<dd> Omit debugger symbol information (but not all symbols) from the output file.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;trace</code></p>
<dd> Print the names of the input files as <code>ld</code> processes them.</p>
<dt><code>-T</code> <i>scriptfile</i></p>
<dd>
<dt><code>&#8211;script=</code><i>scriptfile</i></p>
<dd> Use <i>scriptfile</i> as the linker script. This script replaces <code>ld</code>&#8216;s default linker script (rather than adding to it), so <i>commandfile</i> must specify everything necessary to describe the output file. If <i>scriptfile</i> does not exist in the current directory, <tt>&quot;ld&quot;</tt> looks for it in the directories specified by any preceding <code>-L</code> options. Multiple <code>-T</code> options accumulate.</p>
<dt><code>-u</code> <i>symbol</i></p>
<dd>
<dt><code>&#8211;undefined=</code><i>symbol</i></p>
<dd> Force <i>symbol</i> to be entered in the output file as an undefined symbol. Doing this may, for example, trigger linking of additional modules from standard libraries. <code>-u</code> may be repeated with different option arguments to enter additional undefined symbols. This option is equivalent to the <tt>&quot;EXTERN&quot;</tt> linker script command.</p>
<dt><code>-Ur</code></p>
<dd> For anything other than C<font SIZE="-2">++</font> programs, this option is equivalent to <code>-r</code>: it generates relocatable output&#8212;i.e., an output file that can in turn serve as input to <code>ld</code>. When linking C<font SIZE="-2">++</font> programs, <code>-Ur</code> <i>does</i> resolve references to constructors, unlike <code>-r</code>. It does not work to use <code>-Ur</code> on files that were themselves linked with <code>-Ur</code>; once the constructor table has been built, it cannot be added to. Use <code>-Ur</code> only for the last partial link, and <code>-r</code> for the others.</p>
<dt><code>&#8211;unique[=</code><i></i><font SIZE="-1"><i>SECTION</i></font><i></i><code>]</code></p>
<dd> Creates a separate output section for every input section matching <i></i><font SIZE="-1"><i>SECTION</i></font><i></i>, or if the optional wildcard <i></i><font SIZE="-1"><i>SECTION</i></font><i></i> argument is missing, for every orphan input section. An orphan section is one not specifically mentioned in a linker script. You may use this option multiple times on the command line; It prevents the normal merging of input sections with the same name, overriding output section assignments in a linker script.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>
<dt><code>-V</code></p>
<dd> Display the version number for <code>ld</code>. The <code>-V</code> option also lists the supported emulations.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;discard-all</code></p>
<dd> Delete all local symbols.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;discard-locals</code></p>
<dd> Delete all temporary local symbols. For most targets, this is all local symbols whose names begin with <code>L</code>.</p>
<dt><code>-y</code> <i>symbol</i></p>
<dd>
<dt><code>&#8211;trace-symbol=</code><i>symbol</i></p>
<dd> Print the name of each linked file in which <i>symbol</i> appears. This option may be given any number of times. On many systems it is necessary to prepend an underscore. </p>
<p> This option is useful when you have an undefined symbol in your link but don&#8217;t know where the reference is coming from.</p>
<dt><code>-Y</code> <i>path</i></p>
<dd> Add <i>path</i> to the default library search path. This option exists for Solaris compatibility.</p>
<dt><code>-z</code> <i>keyword</i></p>
<dd> The recognized keywords are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>combreloc</code></p>
<dd> Combines multiple reloc sections and sorts them to make dynamic symbol lookup caching possible.</p>
<dt><code>defs</code></p>
<dd> Disallows undefined symbols in object files. Undefined symbols in shared libraries are still allowed.</p>
<dt><code>initfirst</code></p>
<dd> This option is only meaningful when building a shared object. It marks the object so that its runtime initialization will occur before the runtime initialization of any other objects brought into the process at the same time. Similarly the runtime finalization of the object will occur after the runtime finalization of any other objects.</p>
<dt><code>interpose</code></p>
<dd> Marks the object that its symbol table interposes before all symbols but the primary executable.</p>
<dt><code>loadfltr</code></p>
<dd> Marks the object that its filters be processed immediately at runtime.</p>
<dt><code>muldefs</code></p>
<dd> Allows multiple definitions.</p>
<dt><code>nocombreloc</code></p>
<dd> Disables multiple reloc sections combining.</p>
<dt><code>nocopyreloc</code></p>
<dd> Disables production of copy relocs.</p>
<dt><code>nodefaultlib</code></p>
<dd> Marks the object that the search for dependencies of this object will ignore any default library search paths.</p>
<dt><code>nodelete</code></p>
<dd> Marks the object shouldn&#8217;t be unloaded at runtime.</p>
<dt><code>nodlopen</code></p>
<dd> Marks the object not available to <tt>&quot;dlopen&quot;</tt>.</p>
<dt><code>nodump</code></p>
<dd> Marks the object can not be dumped by <tt>&quot;dldump&quot;</tt>.</p>
<dt><code>now</code></p>
<dd> When generating an executable or shared library, mark it to tell the dynamic linker to resolve all symbols when the program is started, or when the shared library is linked to using dlopen, instead of deferring function call resolution to the point when the function is first called.</p>
<dt><code>origin</code></p>
<dd> Marks the object may contain <tt>$ORIGIN</tt>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Other keywords are ignored for Solaris compatibility.</dl>
<dt><code>-(</code> <i>archives</i> <code>-)</code></p>
<dd>
<dt><code>&#8211;start-group</code> <i>archives</i> <code>&#8211;end-group</code></p>
<dd> The <i>archives</i> should be a list of archive files. They may be either explicit file names, or <code>-l</code> options. </p>
<p> The specified archives are searched repeatedly until no new undefined references are created. Normally, an archive is searched only once in the order that it is specified on the command line. If a symbol in that archive is needed to resolve an undefined symbol referred to by an object in an archive that appears later on the command line, the linker would not be able to resolve that reference. By grouping the archives, they all be searched repeatedly until all possible references are resolved. </p>
<p> Using this option has a significant performance cost. It is best to use it only when there are unavoidable circular references between two or more archives.</p>
<dt><code>&#8211;accept-unknown-input-arch</code></p>
<dd>
<dt><code>&#8211;no-accept-unknown-input-arch</code></p>
<dd> Tells the linker to accept input files whose architecture cannot be recognised. The assumption is that the user knows what they are doing and deliberately wants to link in these unknown input files. This was the default behaviour of the linker, before release 2.14. The default behaviour from release 2.14 onwards is to reject such input files, and so the <code>&#8211;accept-unknown-input-arch</code> option has been added to restore the old behaviour.</p>
<dt><code>&#8211;as-needed</code></p>
<dd>
<dt><code>&#8211;no-as-needed</code></p>
<dd> This option affects <font SIZE="-1">ELF</font> <font SIZE="-1">DT_NEEDED</font> tags for dynamic libraries mentioned on the command line after the <code>&#8211;as-needed</code> option. Normally, the linker will add a <font SIZE="-1">DT_NEEDED</font> tag for each dynamic library mentioned on the command line, regardless of whether the library is actually needed. <code>&#8211;as-needed</code> causes <font SIZE="-1">DT_NEEDED</font> tags to only be emitted for libraries that satisfy some symbol reference from regular objects which is undefined at the point that the library was linked. <code>&#8211;no-as-needed</code> restores the default behaviour.</p>
<dt><code>&#8211;add-needed</code></p>
<dd>
<dt><code>&#8211;no-add-needed</code></p>
<dd> This option affects the treatment of dynamic libraries from <font SIZE="-1">ELF</font> <font SIZE="-1">DT_NEEDED</font> tags in dynamic libraries mentioned on the command line after the <code>&#8211;no-add-needed</code> option. Normally, the linker will add a <font SIZE="-1">DT_NEEDED</font> tag for each dynamic library from <font SIZE="-1">DT_NEEDED</font> tags. <code>&#8211;no-add-needed</code> causes <font SIZE="-1">DT_NEEDED</font> tags will never be emitted for those libraries from <font SIZE="-1">DT_NEEDED</font> tags. <code>&#8211;add-needed</code> restores the default behaviour.</p>
<dt><code>-assert</code> <i>keyword</i></p>
<dd> This option is ignored for SunOS compatibility.</p>
<dt><code>-Bdynamic</code></p>
<dd>
<dt><code>-dy</code></p>
<dd>
<dt><code>-call_shared</code></p>
<dd> Link against dynamic libraries. This is only meaningful on platforms for which shared libraries are supported. This option is normally the default on such platforms. The different variants of this option are for compatibility with various systems. You may use this option multiple times on the command line: it affects library searching for <code>-l</code> options which follow it.</p>
<dt><code>-Bgroup</code></p>
<dd> Set the <tt>&quot;DF_1_GROUP&quot;</tt> flag in the <tt>&quot;DT_FLAGS_1&quot;</tt> entry in the dynamic section. This causes the runtime linker to handle lookups in this object and its dependencies to be performed only inside the group. <code>&#8211;unresolved-symbols=report-all</code> is implied. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>-Bstatic</code></p>
<dd>
<dt><code>-dn</code></p>
<dd>
<dt><code>-non_shared</code></p>
<dd>
<dt><code>-static</code></p>
<dd> Do not link against shared libraries. This is only meaningful on platforms for which shared libraries are supported. The different variants of this option are for compatibility with various systems. You may use this option multiple times on the command line: it affects library searching for <code>-l</code> options which follow it. This option also implies <code>&#8211;unresolved-symbols=report-all</code>.</p>
<dt><code>-Bsymbolic</code></p>
<dd> When creating a shared library, bind references to global symbols to the definition within the shared library, if any. Normally, it is possible for a program linked against a shared library to override the definition within the shared library. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>&#8211;check-sections</code></p>
<dd>
<dt><code>&#8211;no-check-sections</code></p>
<dd> Asks the linker <i>not</i> to check section addresses after they have been assigned to see if there any overlaps. Normally the linker will perform this check, and if it finds any overlaps it will produce suitable error messages. The linker does know about, and does make allowances for sections in overlays. The default behaviour can be restored by using the command line switch <code>&#8211;check-sections</code>.</p>
<dt><code>&#8211;cref</code></p>
<dd> Output a cross reference table. If a linker map file is being generated, the cross reference table is printed to the map file. Otherwise, it is printed on the standard output. </p>
<p> The format of the table is intentionally simple, so that it may be easily processed by a script if necessary. The symbols are printed out, sorted by name. For each symbol, a list of file names is given. If the symbol is defined, the first file listed is the location of the definition. The remaining files contain references to the symbol.</p>
<dt><code>&#8211;no-define-common</code></p>
<dd> This option inhibits the assignment of addresses to common symbols. The script command <tt>&quot;INHIBIT_COMMON_ALLOCATION&quot;</tt> has the same effect. </p>
<p> The <code>&#8211;no-define-common</code> option allows decoupling the decision to assign addresses to Common symbols from the choice of the output file type; otherwise a non-Relocatable output type forces assigning addresses to Common symbols. Using <code>&#8211;no-define-common</code> allows Common symbols that are referenced from a shared library to be assigned addresses only in the main program. This eliminates the unused duplicate space in the shared library, and also prevents any possible confusion over resolving to the wrong duplicate when there are many dynamic modules with specialized search paths for runtime symbol resolution.</p>
<dt><code>&#8211;defsym</code> <i>symbol</i><code>=</code><i>expression</i></p>
<dd> Create a global symbol in the output file, containing the absolute address given by <i>expression</i>. You may use this option as many times as necessary to define multiple symbols in the command line. A limited form of arithmetic is supported for the <i>expression</i> in this context: you may give a hexadecimal constant or the name of an existing symbol, or use <tt>&quot;+&quot;</tt> and <tt>&quot;-&quot;</tt> to add or subtract hexadecimal constants or symbols. If you need more elaborate expressions, consider using the linker command language from a script. <i>Note:</i> there should be no white space between <i>symbol</i>, the equals sign (&#8220;<code>=</code>&#8221;), and <i>expression</i>.</p>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd>
<dt><code>&#8211;no-demangle</code></p>
<dd> These options control whether to demangle symbol names in error messages and other output. When the linker is told to demangle, it tries to present symbol names in a readable fashion: it strips leading underscores if they are used by the object file format, and converts C<font SIZE="-2">++</font> mangled symbol names into user readable names. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler. The linker will demangle by default unless the environment variable <font SIZE="-1"><code>COLLECT_NO_DEMANGLE</code></font> is set. These options may be used to override the default.</p>
<dt><code>&#8211;dynamic-linker</code> <i>file</i></p>
<dd> Set the name of the dynamic linker. This is only meaningful when generating dynamically linked <font SIZE="-1">ELF</font> executables. The default dynamic linker is normally correct; don&#8217;t use this unless you know what you are doing.</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd> Treat all warnings as errors.</p>
<dt><code>&#8211;force-exe-suffix</code></p>
<dd> Make sure that an output file has a .exe suffix. </p>
<p> If a successfully built fully linked output file does not have a <tt>&quot;.exe&quot;</tt> or <tt>&quot;.dll&quot;</tt> suffix, this option forces the linker to copy the output file to one of the same name with a <tt>&quot;.exe&quot;</tt> suffix. This option is useful when using unmodified Unix makefiles on a Microsoft Windows host, since some versions of Windows won&#8217;t run an image unless it ends in a <tt>&quot;.exe&quot;</tt> suffix.</p>
<dt><code>&#8211;no-gc-sections</code></p>
<dd>
<dt><code>&#8211;gc-sections</code></p>
<dd> Enable garbage collection of unused input sections. It is ignored on targets that do not support this option. This option is not compatible with <code>-r</code>. The default behaviour (of not performing this garbage collection) can be restored by specifying <code>&#8211;no-gc-sections</code> on the command line.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command-line options on the standard output and exit.</p>
<dt><code>&#8211;target-help</code></p>
<dd> Print a summary of all target specific options on the standard output and exit.</p>
<dt><code>-Map</code> <i>mapfile</i></p>
<dd> Print a link map to the file <i>mapfile</i>. See the description of the <code>-M</code> option, above.</p>
<dt><code>&#8211;no-keep-memory</code></p>
<dd> <code>ld</code> normally optimizes for speed over memory usage by caching the symbol tables of input files in memory. This option tells <code>ld</code> to instead optimize for memory usage, by rereading the symbol tables as necessary. This may be required if <code>ld</code> runs out of memory space while linking a large executable.</p>
<dt><code>&#8211;no-undefined</code></p>
<dd>
<dt><code>-z defs</code></p>
<dd> Report unresolved symbol references from regular object files. This is done even if the linker is creating a non-symbolic shared library. The switch <code>&#8211;[no-]allow-shlib-undefined</code> controls the behaviour for reporting unresolved references found in shared libraries being linked in.</p>
<dt><code>&#8211;allow-multiple-definition</code></p>
<dd>
<dt><code>-z muldefs</code></p>
<dd> Normally when a symbol is defined multiple times, the linker will report a fatal error. These options allow multiple definitions and the first definition will be used.</p>
<dt><code>&#8211;allow-shlib-undefined</code></p>
<dd>
<dt><code>&#8211;no-allow-shlib-undefined</code></p>
<dd> Allows (the default) or disallows undefined symbols in shared libraries. This switch is similar to <code>&#8211;no-undefined</code> except that it determines the behaviour when the undefined symbols are in a shared library rather than a regular object file. It does not affect how undefined symbols in regular object files are handled. </p>
<p> The reason that <code>&#8211;allow-shlib-undefined</code> is the default is that the shared library being specified at link time may not be the same as the one that is available at load time, so the symbols might actually be resolvable at load time. Plus there are some systems, (eg BeOS) where undefined symbols in shared libraries is normal. (The kernel patches them at load time to select which function is most appropriate for the current architecture. This is used for example to dynamically select an appropriate memset function). Apparently it is also normal for <font SIZE="-1">HPPA</font> shared libraries to have undefined symbols.</p>
<dt><code>&#8211;no-undefined-version</code></p>
<dd> Normally when a symbol has an undefined version, the linker will ignore it. This option disallows symbols with undefined version and a fatal error will be issued instead.</p>
<dt><code>&#8211;default-symver</code></p>
<dd> Create and use a default symbol version (the soname) for unversioned exported symbols.</p>
<dt><code>&#8211;default-imported-symver</code></p>
<dd> Create and use a default symbol version (the soname) for unversioned imported symbols.</p>
<dt><code>&#8211;no-warn-mismatch</code></p>
<dd> Normally <code>ld</code> will give an error if you try to link together input files that are mismatched for some reason, perhaps because they have been compiled for different processors or for different endiannesses. This option tells <code>ld</code> that it should silently permit such possible errors. This option should only be used with care, in cases when you have taken some special action that ensures that the linker errors are inappropriate.</p>
<dt><code>&#8211;no-whole-archive</code></p>
<dd> Turn off the effect of the <code>&#8211;whole-archive</code> option for subsequent archive files.</p>
<dt><code>&#8211;noinhibit-exec</code></p>
<dd> Retain the executable output file whenever it is still usable. Normally, the linker will not produce an output file if it encounters errors during the link process; it exits without writing an output file when it issues any error whatsoever.</p>
<dt><code>-nostdlib</code></p>
<dd> Only search library directories explicitly specified on the command line. Library directories specified in linker scripts (including linker scripts specified on the command line) are ignored.</p>
<dt><code>&#8211;oformat</code> <i>output-format</i></p>
<dd> <code>ld</code> may be configured to support more than one kind of object file. If your <code>ld</code> is configured this way, you can use the <code>&#8211;oformat</code> option to specify the binary format for the output object file. Even when <code>ld</code> is configured to support alternative object formats, you don&#8217;t usually need to specify this, as <code>ld</code> should be configured to produce as a default output format the most usual format on each machine. <i>output-format</i> is a text string, the name of a particular format supported by the <font SIZE="-1">BFD</font> libraries. (You can list the available binary formats with <code>objdump -i</code>.) The script command <tt>&quot;OUTPUT_FORMAT&quot;</tt> can also specify the output format, but this option overrides it.</p>
<dt><code>-pie</code></p>
<dd>
<dt><code>&#8211;pic-executable</code></p>
<dd> Create a position independent executable. This is currently only supported on <font SIZE="-1">ELF</font> platforms. Position independent executables are similar to shared libraries in that they are relocated by the dynamic linker to the virtual address the <font SIZE="-1">OS</font> chooses for them (which can vary between invocations). Like normal dynamically linked executables they can be executed and symbols defined in the executable cannot be overridden by shared libraries.</p>
<dt><code>-qmagic</code></p>
<dd> This option is ignored for Linux compatibility.</p>
<dt><code>-Qy</code></p>
<dd> This option is ignored for <font SIZE="-1">SVR4</font> compatibility.</p>
<dt><code>&#8211;relax</code></p>
<dd> An option with machine dependent effects. This option is only supported on a few targets. </p>
<p> On some platforms, the <code>&#8211;relax</code> option performs global optimizations that become possible when the linker resolves addressing in the program, such as relaxing address modes and synthesizing new instructions in the output object file. </p>
<p> On some platforms these link time global optimizations may make symbolic debugging of the resulting executable impossible. This is known to be the case for the Matsushita <font SIZE="-1">MN10200</font> and <font SIZE="-1">MN10300</font> family of processors. </p>
<p> On platforms where this is not supported, <code>&#8211;relax</code> is accepted, but ignored.</p>
<dt><code>&#8211;retain-symbols-file</code> <i>filename</i></p>
<dd> Retain <i>only</i> the symbols listed in the file <i>filename</i>, discarding all others. <i>filename</i> is simply a flat file, with one symbol name per line. This option is especially useful in environments (such as VxWorks) where a large global symbol table is accumulated gradually, to conserve run-time memory. </p>
<p> <code>&#8211;retain-symbols-file</code> does <i>not</i> discard undefined symbols, or symbols needed for relocations. </p>
<p> You may only specify <code>&#8211;retain-symbols-file</code> once in the command line. It overrides <code>-s</code> and <code>-S</code>.</p>
<dt><code>-rpath</code> <i>dir</i></p>
<dd> Add a directory to the runtime library search path. This is used when linking an <font SIZE="-1">ELF</font> executable with shared objects. All <code>-rpath</code> arguments are concatenated and passed to the runtime linker, which uses them to locate shared objects at runtime. The <code>-rpath</code> option is also used when locating shared objects which are needed by shared objects explicitly included in the link; see the description of the <code>-rpath-link</code> option. If <code>-rpath</code> is not used when linking an <font SIZE="-1">ELF</font> executable, the contents of the environment variable <tt>&quot;LD_RUN_PATH&quot;</tt> will be used if it is defined. </p>
<p> The <code>-rpath</code> option may also be used on SunOS. By default, on SunOS, the linker will form a runtime search patch out of all the <code>-L</code> options it is given. If a <code>-rpath</code> option is used, the runtime search path will be formed exclusively using the <code>-rpath</code> options, ignoring the <code>-L</code> options. This can be useful when using gcc, which adds many <code>-L</code> options which may be on <font SIZE="-1">NFS</font> mounted filesystems. </p>
<p> For compatibility with other <font SIZE="-1">ELF</font> linkers, if the <code>-R</code> option is followed by a directory name, rather than a file name, it is treated as the <code>-rpath</code> option.</p>
<dt><code>-rpath-link</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> When using <font SIZE="-1">ELF</font> or SunOS, one shared library may require another. This happens when an <tt>&quot;ld -shared&quot;</tt> link includes a shared library as one of the input files. </p>
<p> When the linker encounters such a dependency when doing a non-shared, non-relocatable link, it will automatically try to locate the required shared library and include it in the link, if it is not included explicitly. In such a case, the <code>-rpath-link</code> option specifies the first set of directories to search. The <code>-rpath-link</code> option may specify a sequence of directory names either by specifying a list of names separated by colons, or by appearing multiple times. </p>
<p> This option should be used with caution as it overrides the search path that may have been hard compiled into a shared library. In such a case it is possible to use unintentionally a different search path than the runtime linker would do. </p>
<p> The linker uses the following search paths to locate required shared libraries.</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Any directories specified by <code>-rpath-link</code> options.</p>
<dt>2.</p>
<dd> Any directories specified by <code>-rpath</code> options. The difference between <code>-rpath</code> and <code>-rpath-link</code> is that directories specified by <code>-rpath</code> options are included in the executable and used at runtime, whereas the <code>-rpath-link</code> option is only effective at link time. It is for the native linker only.</p>
<dt>3.</p>
<dd> On an <font SIZE="-1">ELF</font> system, if the <code>-rpath</code> and <tt>&quot;rpath-link&quot;</tt> options were not used, search the contents of the environment variable <tt>&quot;LD_RUN_PATH&quot;</tt>. It is for the native linker only.</p>
<dt>4.</p>
<dd> On SunOS, if the <code>-rpath</code> option was not used, search any directories specified using <code>-L</code> options.</p>
<dt>5.</p>
<dd> For a native linker, the contents of the environment variable <tt>&quot;LD_LIBRARY_PATH&quot;</tt>.</p>
<dt>6.</p>
<dd> For a native <font SIZE="-1">ELF</font> linker, the directories in <tt>&quot;DT_RUNPATH&quot;</tt> or <tt>&quot;DT_RPATH&quot;</tt> of a shared library are searched for shared libraries needed by it. The <tt>&quot;DT_RPATH&quot;</tt> entries are ignored if <tt>&quot;DT_RUNPATH&quot;</tt> entries exist.</p>
<dt>7.</p>
<dd> The default directories, normally <i>/lib</i> and <i>/usr/lib</i>.</p>
<dt>8.</p>
<dd> For a native linker on an <font SIZE="-1">ELF</font> system, if the file <i>/etc/ld.so.conf</i> exists, the list of directories found in that file.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If the required shared library is not found, the linker will issue a warning and continue with the link.</dl>
<dt><code>-shared</code></p>
<dd>
<dt><code>-Bshareable</code></p>
<dd> Create a shared library. This is currently only supported on <font SIZE="-1">ELF</font>, <font SIZE="-1">XCOFF</font> and SunOS platforms. On SunOS, the linker will automatically create a shared library if the <code>-e</code> option is not used and there are undefined symbols in the link.</p>
<dt><code>&#8211;sort-common</code></p>
<dd> This option tells <code>ld</code> to sort the common symbols by size when it places them in the appropriate output sections. First come all the one byte symbols, then all the two byte, then all the four byte, and then everything else. This is to prevent gaps between symbols due to alignment constraints.</p>
<dt><code>&#8211;sort-section name</code></p>
<dd> This option will apply <tt>&quot;SORT_BY_NAME&quot;</tt> to all wildcard section patterns in the linker script.</p>
<dt><code>&#8211;sort-section alignment</code></p>
<dd> This option will apply <tt>&quot;SORT_BY_ALIGNMENT&quot;</tt> to all wildcard section patterns in the linker script.</p>
<dt><code>&#8211;split-by-file [</code><i>size</i><code>]</code></p>
<dd> Similar to <code>&#8211;split-by-reloc</code> but creates a new output section for each input file when <i>size</i> is reached. <i>size</i> defaults to a size of 1 if not given.</p>
<dt><code>&#8211;split-by-reloc [</code><i>count</i><code>]</code></p>
<dd> Tries to creates extra sections in the output file so that no single output section in the file contains more than <i>count</i> relocations. This is useful when generating huge relocatable files for downloading into certain real time kernels with the <font SIZE="-1">COFF</font> object file format; since <font SIZE="-1">COFF</font> cannot represent more than 65535 relocations in a single section. Note that this will fail to work with object file formats which do not support arbitrary sections. The linker will not split up individual input sections for redistribution, so if a single input section contains more than <i>count</i> relocations one output section will contain that many relocations. <i>count</i> defaults to a value of 32768.</p>
<dt><code>&#8211;stats</code></p>
<dd> Compute and display statistics about the operation of the linker, such as execution time and memory usage.</p>
<dt><code>&#8211;sysroot=</code><i>directory</i></p>
<dd> Use <i>directory</i> as the location of the sysroot, overriding the configure-time default. This option is only supported by linkers that were configured using <code>&#8211;with-sysroot</code>.</p>
<dt><code>&#8211;traditional-format</code></p>
<dd> For some targets, the output of <code>ld</code> is different in some ways from the output of some existing linker. This switch requests <code>ld</code> to use the traditional format instead. </p>
<p> For example, on SunOS, <code>ld</code> combines duplicate entries in the symbol string table. This can reduce the size of an output file with full debugging information by over 30 percent. Unfortunately, the SunOS <tt>&quot;dbx&quot;</tt> program can not read the resulting program (<tt>&quot;gdb&quot;</tt> has no trouble). The <code>&#8211;traditional-format</code> switch tells <code>ld</code> to not combine duplicate entries.</p>
<dt><code>&#8211;section-start</code> <i>sectionname</i><code>=</code><i>org</i></p>
<dd> Locate a section in the output file at the absolute address given by <i>org</i>. You may use this option as many times as necessary to locate multiple sections in the command line. <i>org</i> must be a single hexadecimal integer; for compatibility with other linkers, you may omit the leading <code>0x</code> usually associated with hexadecimal values. <i>Note:</i> there should be no white space between <i>sectionname</i>, the equals sign (&#8220;<code>=</code>&#8221;), and <i>org</i>.</p>
<dt><code>-Tbss</code> <i>org</i></p>
<dd>
<dt><code>-Tdata</code> <i>org</i></p>
<dd>
<dt><code>-Ttext</code> <i>org</i></p>
<dd> Same as &#8211;section-start, with <tt>&quot;.bss&quot;</tt>, <tt>&quot;.data&quot;</tt> or <tt>&quot;.text&quot;</tt> as the <i>sectionname</i>.</p>
<dt><code>&#8211;unresolved-symbols=</code><i>method</i></p>
<dd> Determine how to handle unresolved symbols. There are four possible values for <code>method</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>ignore-all</code></p>
<dd> Do not report any unresolved symbols.</p>
<dt><code>report-all</code></p>
<dd> Report all unresolved symbols. This is the default.</p>
<dt><code>ignore-in-object-files</code></p>
<dd> Report unresolved symbols that are contained in shared libraries, but ignore them if they come from regular object files.</p>
<dt><code>ignore-in-shared-libs</code></p>
<dd> Report unresolved symbols that come from regular object files, but ignore them if they come from shared libraries. This can be useful when creating a dynamic binary and it is known that all the shared libraries that it should be referencing are included on the linker&#8217;s command line.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The behaviour for shared libraries on their own can also be controlled by the <code>&#8211;[no-]allow-shlib-undefined</code> option. </p>
<p> Normally the linker will generate an error message for each reported unresolved symbol but the option <code>&#8211;warn-unresolved-symbols</code> can change this to a warning.</dl>
<dt><code>&#8211;dll-verbose</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Display the version number for <code>ld</code> and list the linker emulations supported. Display which input files can and cannot be opened. Display the linker script being used by the linker.</p>
<dt><code>&#8211;version-script=</code><i>version-scriptfile</i></p>
<dd> Specify the name of a version script to the linker. This is typically used when creating shared libraries to specify additional information about the version hierarchy for the library being created. This option is only meaningful on <font SIZE="-1">ELF</font> platforms which support shared libraries.</p>
<dt><code>&#8211;warn-common</code></p>
<dd> Warn when a common symbol is combined with another common symbol or with a symbol definition. Unix linkers allow this somewhat sloppy practise, but linkers on some other operating systems do not. This option allows you to find potential problems from combining global symbols. Unfortunately, some C libraries use this practise, so you may get some warnings about symbols in the libraries as well as in your programs. </p>
<p> There are three kinds of global symbols, illustrated here by C examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>int i = 1;</code></p>
<dd> A definition, which goes in the initialized data section of the output file.</p>
<dt><code>extern int i;</code></p>
<dd> An undefined reference, which does not allocate space. There must be either a definition or a common symbol for the variable somewhere.</p>
<dt><code>int i;</code></p>
<dd> A common symbol. If there are only (one or more) common symbols for a variable, it goes in the uninitialized data area of the output file. The linker merges multiple common symbols for the same variable into a single symbol. If they are of different sizes, it picks the largest size. The linker turns a common symbol into a declaration, if there is a definition of the same variable.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The <code>&#8211;warn-common</code> option can produce five kinds of warnings. Each warning consists of a pair of lines: the first describes the symbol just encountered, and the second describes the previous symbol encountered with the same name. One or both of the two symbols will be a common symbol.</p>
<dl>
<dt>1.</p>
<dd> Turning a common symbol into a reference, because there is already a definition for the symbol. </p>
<pre>
        &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
           overridden by definition
        &lt;file&gt;(&lt;section&gt;): warning: defined here
</pre>
<dt>2.</p>
<dd> Turning a common symbol into a reference, because a later definition for the symbol is encountered. This is the same as the previous case, except that the symbols are encountered in a different order. </p>
<pre>
        &lt;file&gt;(&lt;section&gt;): warning: definition of `&lt;symbol&gt;'
           overriding common
        &lt;file&gt;(&lt;section&gt;): warning: common is here
</pre>
<dt>3.</p>
<dd> Merging a common symbol with a previous same-sized common symbol. </p>
<pre>
        &lt;file&gt;(&lt;section&gt;): warning: multiple common
           of `&lt;symbol&gt;'
        &lt;file&gt;(&lt;section&gt;): warning: previous common is here
</pre>
<dt>4.</p>
<dd> Merging a common symbol with a previous larger common symbol. </p>
<pre>
        &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
           overridden by larger common
        &lt;file&gt;(&lt;section&gt;): warning: larger common is here
</pre>
<dt>5.</p>
<dd> Merging a common symbol with a previous smaller common symbol. This is the same as the previous case, except that the symbols are encountered in a different order. </p>
<pre>
        &lt;file&gt;(&lt;section&gt;): warning: common of `&lt;symbol&gt;'
           overriding smaller common
        &lt;file&gt;(&lt;section&gt;): warning: smaller common is here
</pre>
</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;warn-constructors</code></p>
<dd> Warn if any global constructors are used. This is only useful for a few object file formats. For formats like <font SIZE="-1">COFF</font> or <font SIZE="-1">ELF</font>, the linker can not detect the use of global constructors.</p>
<dt><code>&#8211;warn-multiple-gp</code></p>
<dd> Warn if multiple global pointer values are required in the output file. This is only meaningful for certain processors, such as the Alpha. Specifically, some processors put large-valued constants in a special section. A special register (the global pointer) points into the middle of this section, so that constants can be loaded efficiently via a base-register relative addressing mode. Since the offset in base-register relative mode is fixed and relatively small (e.g., 16 bits), this limits the maximum size of the constant pool. Thus, in large programs, it is often necessary to use multiple global pointer values in order to be able to address all possible constants. This option causes a warning to be issued whenever this case occurs.</p>
<dt><code>&#8211;warn-once</code></p>
<dd> Only warn once for each undefined symbol, rather than once per module which refers to it.</p>
<dt><code>&#8211;warn-section-align</code></p>
<dd> Warn if the address of an output section is changed because of alignment. Typically, the alignment will be set by an input section. The address will only be changed if it not explicitly specified; that is, if the <tt>&quot;SECTIONS&quot;</tt> command does not specify a start address for the section.</p>
<dt><code>&#8211;warn-shared-textrel</code></p>
<dd> Warn if the linker adds a <font SIZE="-1">DT_TEXTREL</font> to a shared object.</p>
<dt><code>&#8211;warn-unresolved-symbols</code></p>
<dd> If the linker is going to report an unresolved symbol (see the option <code>&#8211;unresolved-symbols</code>) it will normally generate an error. This option makes it generate a warning instead.</p>
<dt><code>&#8211;error-unresolved-symbols</code></p>
<dd> This restores the linker&#8217;s default behaviour of generating errors when it is reporting unresolved symbols.</p>
<dt><code>&#8211;whole-archive</code></p>
<dd> For each archive mentioned on the command line after the <code>&#8211;whole-archive</code> option, include every object file in the archive in the link, rather than searching the archive for the required object files. This is normally used to turn an archive file into a shared library, forcing every object to be included in the resulting shared library. This option may be used more than once. </p>
<p> Two notes when using this option from gcc: First, gcc doesn&#8217;t know about this option, so you have to use <code>-Wl,-whole-archive</code>. Second, don&#8217;t forget to use <code>-Wl,-no-whole-archive</code> after your list of archives, because gcc will add its own list of archives to your link and you may not want this flag to affect those as well.</p>
<dt><code>&#8211;wrap</code> <i>symbol</i></p>
<dd> Use a wrapper function for <i>symbol</i>. Any undefined reference to <i>symbol</i> will be resolved to <tt>&quot;__wrap_</tt>symbol<tt>&quot;</tt>. Any undefined reference to <tt>&quot;__real_</tt>symbol<tt>&quot;</tt> will be resolved to <i>symbol</i>. </p>
<p> This can be used to provide a wrapper for a system function. The wrapper function should be called <tt>&quot;__wrap_</tt>symbol<tt>&quot;</tt>. If it wishes to call the system function, it should call <tt>&quot;__real_</tt>symbol<tt>&quot;</tt>. </p>
<p> Here is a trivial example: </p>
<pre><code>
void *
__wrap_malloc(size_t c)
{
    printf("malloc called with %zu
", c);
    return __real_malloc(c);
}
</code></pre>
<p> If you link other code with this file using <code>&#8211;wrap malloc</code>, then all calls to <tt>&quot;malloc&quot;</tt> will call the function <tt>&quot;__wrap_malloc&quot;</tt> instead. The call to <tt>&quot;__real_malloc&quot;</tt> in <tt>&quot;__wrap_malloc&quot;</tt> will call the real <tt>&quot;malloc&quot;</tt> function. </p>
<p> You may wish to provide a <tt>&quot;__real_malloc&quot;</tt> function as well, so that links without the <code>&#8211;wrap</code> option will succeed. If you do this, you should not put the definition of <tt>&quot;__real_malloc&quot;</tt> in the same file as <tt>&quot;__wrap_malloc&quot;</tt>; if you do, the assembler may resolve the call before the linker has a chance to wrap it to <tt>&quot;malloc&quot;</tt>.</p>
<dt><code>&#8211;enable-new-dtags</code></p>
<dd>
<dt><code>&#8211;disable-new-dtags</code></p>
<dd> This linker can create the new dynamic tags in <font SIZE="-1">ELF</font>. But the older <font SIZE="-1">ELF</font> systems may not understand them. If you specify <code>&#8211;enable-new-dtags</code>, the dynamic tags will be created as needed. If you specify <code>&#8211;disable-new-dtags</code>, no new dynamic tags will be created. By default, the new dynamic tags are not created. Note that those options are only available for <font SIZE="-1">ELF</font> systems.</p>
<dt><code>&#8211;hash-size=</code><i>number</i></p>
<dd> Set the default size of the linker&#8217;s hash tables to a prime number close to <i>number</i>. Increasing this value can reduce the length of time it takes the linker to perform its tasks, at the expense of increasing the linker&#8217;s memory requirements. Similarly reducing this value can reduce the memory requirements at the expense of speed.</p>
<dt><code>&#8211;reduce-memory-overheads</code></p>
<dd> This option reduces memory requirements at ld runtime, at the expense of linking speed. This was introduced to to select the old O(n^2) algorithm for link map file generation, rather than the new <a href="/docs/linux/man/n-o/">O</a>(n) algorithm which uses about 40% more memory for symbol storage. </p>
<p> Another affect of the switch is to set the default hash table size to 1021, which again saves memory at the cost of lengthening the linker&#8217;s run time. This is not done however if the <code>&#8211;hash-size</code> switch has been used. </p>
<p> The <code>&#8211;reduce-memory-overheads</code> switch may be also be used to enable other tradeoffs in future versions of the linker.</dl>
<p> The i386 <font SIZE="-1">PE</font> linker supports the <code>-shared</code> option, which causes the output to be a dynamically linked library (<font SIZE="-1">DLL</font>) instead of a normal executable. You should name the output <tt>&quot;*.dll&quot;</tt> when you use this option. In addition, the linker fully supports the standard <tt>&quot;*.def&quot;</tt> files, which may be specified on the linker command line like an object file (in fact, it should precede archives it exports symbols from, to ensure that they get linked in, just like a normal object file). </p>
<p> In addition to the options common to all targets, the i386 <font SIZE="-1">PE</font> linker support additional command line options that are specific to the i386 <font SIZE="-1">PE</font> target. Options that take values may be separated from their values by either a space or an equals sign.</p>
<dl>
<dt><code>&#8211;add-stdcall-alias</code></p>
<dd> If given, symbols with a stdcall suffix (@<i>nn</i>) will be exported as-is and also with the suffix stripped. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;base-file</code> <i>file</i></p>
<dd> Use <i>file</i> as the name of a file in which to save the base addresses of all the relocations needed for generating DLLs with <i>dlltool</i>. [This is an i386 <font SIZE="-1">PE</font> specific option]</p>
<dt><code>&#8211;dll</code></p>
<dd> Create a <font SIZE="-1">DLL</font> instead of a regular executable. You may also use <code>-shared</code> or specify a <tt>&quot;LIBRARY&quot;</tt> in a given <tt>&quot;.def&quot;</tt> file. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-stdcall-fixup</code></p>
<dd>
<dt><code>&#8211;disable-stdcall-fixup</code></p>
<dd> If the link finds a symbol that it cannot resolve, it will attempt to do &#8220;fuzzy linking&#8221; by looking for another defined symbol that differs only in the format of the symbol name (cdecl vs stdcall) and will resolve that symbol by linking to the match. For example, the undefined symbol <tt>&quot;_foo&quot;</tt> might be linked to the function <tt>&quot;_foo@12&quot;</tt>, or the undefined symbol <tt>&quot;_bar@16&quot;</tt> might be linked to the function <tt>&quot;_bar&quot;</tt>. When the linker does this, it prints a warning, since it normally should have failed to link, but sometimes import libraries generated from third-party dlls may need this feature to be usable. If you specify <code>&#8211;enable-stdcall-fixup</code>, this feature is fully enabled and warnings are not printed. If you specify <code>&#8211;disable-stdcall-fixup</code>, this feature is disabled and such mismatches are considered to be errors. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;export-all-symbols</code></p>
<dd> If given, all global symbols in the objects used to build a <font SIZE="-1">DLL</font> will be exported by the <font SIZE="-1">DLL</font>. Note that this is the default if there otherwise wouldn&#8217;t be any exported symbols. When symbols are explicitly exported via <font SIZE="-1">DEF</font> files or implicitly exported via function attributes, the default is to not export anything else unless this option is given. Note that the symbols <tt>&quot;DllMain@12&quot;</tt>, <tt>&quot;DllEntryPoint@0&quot;</tt>, <tt>&quot;DllMainCRTStartup@12&quot;</tt>, and <tt>&quot;impure_ptr&quot;</tt> will not be automatically exported. Also, symbols imported from other DLLs will not be re-exported, nor will symbols specifying the <font SIZE="-1">DLL</font>&#8216;s internal layout such as those beginning with <tt>&quot;_head_&quot;</tt> or ending with <tt>&quot;_iname&quot;</tt>. In addition, no symbols from <tt>&quot;libgcc&quot;</tt>, <tt>&quot;libstd++&quot;</tt>, <tt>&quot;libmingw32&quot;</tt>, or <tt>&quot;crtX.o&quot;</tt> will be exported. Symbols whose names begin with <tt>&quot;__rtti_&quot;</tt> or <tt>&quot;__builtin_&quot;</tt> will not be exported, to help with C<font SIZE="-2">++</font> DLLs. Finally, there is an extensive list of cygwin-private symbols that are not exported (obviously, this applies on when building DLLs for cygwin targets). These cygwin-excludes are: <tt>&quot;_cygwin_dll_entry@12&quot;</tt>, <tt>&quot;_cygwin_crt0_common@8&quot;</tt>, <tt>&quot;_cygwin_noncygwin_dll_entry@12&quot;</tt>, <tt>&quot;_fmode&quot;</tt>, <tt>&quot;_impure_ptr&quot;</tt>, <tt>&quot;cygwin_attach_dll&quot;</tt>, <tt>&quot;cygwin_premain0&quot;</tt>, <tt>&quot;cygwin_premain1&quot;</tt>, <tt>&quot;cygwin_premain2&quot;</tt>, <tt>&quot;cygwin_premain3&quot;</tt>, and <tt>&quot;environ&quot;</tt>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;exclude-symbols</code> <i>symbol</i><code>,</code><i>symbol</i><code>,&#8230;</code></p>
<dd> Specifies a list of symbols which should not be automatically exported. The symbol names may be delimited by commas or colons. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;file-alignment</code></p>
<dd> Specify the file alignment. Sections in the file will always begin at file offsets which are multiples of this number. This defaults to 512. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;heap</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;heap</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd> Specify the amount of memory to reserve (and optionally commit) to be used as heap for this program. The default is 1Mb reserved, 4K committed. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;image-base</code> <i>value</i></p>
<dd> Use <i>value</i> as the base address of your program or dll. This is the lowest memory location that will be used when your program or dll is loaded. To reduce the need to relocate and improve performance of your dlls, each should have a unique base address and not overlap any other dlls. The default is 0x400000 for executables, and 0x10000000 for dlls. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;kill-at</code></p>
<dd> If given, the stdcall suffixes (@<i>nn</i>) will be stripped from symbols before they are exported. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;large-address-aware</code></p>
<dd> If given, the appropriate bit in the &#8220;Charateristics&#8221; field of the <font SIZE="-1">COFF</font> header is set to indicate that this executable supports virtual addresses greater than 2 gigabytes. This should be used in conjuction with the /3GB or /USERVA=<i>value</i> megabytes switch in the &#8220;[operating systems]&#8221; section of the <font SIZE="-1">BOOT</font>.INI. Otherwise, this bit has no effect. [This option is specific to <font SIZE="-1">PE</font> targeted ports of the linker]</p>
<dt><code>&#8211;major-image-version</code> <i>value</i></p>
<dd> Sets the major number of the &#8220;image version&#8221;. Defaults to 1. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;major-os-version</code> <i>value</i></p>
<dd> Sets the major number of the &#8220;os version&#8221;. Defaults to 4. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;major-subsystem-version</code> <i>value</i></p>
<dd> Sets the major number of the &#8220;subsystem version&#8221;. Defaults to 4. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-image-version</code> <i>value</i></p>
<dd> Sets the minor number of the &#8220;image version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-os-version</code> <i>value</i></p>
<dd> Sets the minor number of the &#8220;os version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;minor-subsystem-version</code> <i>value</i></p>
<dd> Sets the minor number of the &#8220;subsystem version&#8221;. Defaults to 0. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;output-def</code> <i>file</i></p>
<dd> The linker will create the file <i>file</i> which will contain a <font SIZE="-1">DEF</font> file corresponding to the <font SIZE="-1">DLL</font> the linker is generating. This <font SIZE="-1">DEF</font> file (which should be called <tt>&quot;*.def&quot;</tt>) may be used to create an import library with <tt>&quot;dlltool&quot;</tt> or may be used as a reference to automatically or implicitly exported symbols. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;out-implib</code> <i>file</i></p>
<dd> The linker will create the file <i>file</i> which will contain an import lib corresponding to the <font SIZE="-1">DLL</font> the linker is generating. This import lib (which should be called <tt>&quot;*.dll.a&quot;</tt> or <tt>&quot;*.a&quot;</tt> may be used to link clients against the generated <font SIZE="-1">DLL</font>; this behaviour makes it possible to skip a separate <tt>&quot;dlltool&quot;</tt> import library creation step. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-auto-image-base</code></p>
<dd> Automatically choose the image base for DLLs, unless one is specified using the <tt>&quot;--image-base&quot;</tt> argument. By using a hash generated from the dllname to create unique image bases for each <font SIZE="-1">DLL</font>, in-memory collisions and relocations which can delay program execution are avoided. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;disable-auto-image-base</code></p>
<dd> Do not automatically generate a unique image base. If there is no user-specified image base (<tt>&quot;--image-base&quot;</tt>) then use the platform default. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;dll-search-prefix</code> <i>string</i></p>
<dd> When linking dynamically to a dll without an import library, search for <tt>&quot;&lt;string&gt;&lt;basename&gt;.dll&quot;</tt> in preference to <tt>&quot;lib&lt;basename&gt;.dll&quot;</tt>. This behaviour allows easy distinction between DLLs built for the various &#8220;subplatforms&#8221;: native, cygwin, uwin, pw, etc. For instance, cygwin DLLs typically use <tt>&quot;--dll-search-prefix=cyg&quot;</tt>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-auto-import</code></p>
<dd> Do sophisticated linking of <tt>&quot;_symbol&quot;</tt> to <tt>&quot;__imp__symbol&quot;</tt> for <font SIZE="-1">DATA</font> imports from DLLs, and create the necessary thunking symbols when building the import libraries with those <font SIZE="-1">DATA</font> exports. Note: Use of the &#8216;auto-import&#8217; extension will cause the text section of the image file to be made writable. This does not conform to the PE-COFF format specification published by Microsoft. </p>
<p> Using &#8216;auto-import&#8217; generally will &#8216;just work&#8217; &#8212; but sometimes you may see this message: </p>
<p> &quot;variable &#8216;&lt;var&gt;&#8217; can&#8217;t be auto-imported. Please read the documentation for ld&#8217;s <tt>&quot;--enable-auto-import&quot;</tt> for details.&quot; </p>
<p> This message occurs when some (sub)expression accesses an address ultimately given by the sum of two constants (Win32 import tables only allow one). Instances where this may occur include accesses to member fields of struct variables imported from a <font SIZE="-1">DLL</font>, as well as using a constant index into an array variable imported from a <font SIZE="-1">DLL</font>. Any multiword variable (arrays, structs, long long, etc) may trigger this error condition. However, regardless of the exact data type of the offending exported variable, ld will always detect it, issue the warning, and exit. </p>
<p> There are several ways to address this difficulty, regardless of the data type of the exported variable: </p>
<p> One way is to use &#8211;enable-runtime-pseudo-reloc switch. This leaves the task of adjusting references in your client code for runtime environment, so this method works only when runtime environment supports this feature. </p>
<p> A second solution is to force one of the &#8216;constants&#8217; to be a variable &#8212; that is, unknown and un-optimizable at compile time. For arrays, there are two possibilities: a) make the indexee (the array&#8217;s address) a variable, or b) make the &#8216;constant&#8217; index a variable. Thus: </p>
<p>extern type extern_array[];<br />
extern_array[1]&#8211; &gt;<br />
{<br />
    volatile type *t = extern_array;<br />
    t[1]<br />
}</p>
<p> or </p>
<p>extern type extern_array[];<br />
extern_array[1]&#8211; &gt;<br />
{<br />
    volatile int t = 1;<br />
    extern_array[t]<br />
}</p>
<p> For structs (and most other multiword data types) the only option is to make the struct itself (or the long long, or the &#8230;) variable: </p>
<p>extern struct s extern_struct;<br />
extern_struct.field&#8211; &gt;<br />
{<br />
    volatile struct s *t = &amp;extern_struct;<br />
    t-&gt;field<br />
}</p>
<p> or </p>
<p>extern long long extern_ll;<br />
extern_ll&#8211; &gt;<br />
{<br />
    volatile long long *local_ll = &amp;extern_ll;<br />
    *local_ll<br />
}</p>
<p> A third method of dealing with this difficulty is to abandon &#8216;auto-import&#8217; for the offending symbol and mark it with <tt>&quot;__declspec(dllimport)&quot;</tt>. However, in practise that requires using compile-time #defines to indicate whether you are building a <font SIZE="-1">DLL</font>, building client code that will link to the <font SIZE="-1">DLL</font>, or merely building/linking to a static library. In making the choice between the various methods of resolving the &#8216;direct address with constant offset&#8217; problem, you should consider typical real-world usage: </p>
<p> Original: </p>
<p>&#8211;foo.h extern int arr[];<br />
&#8211;foo.c<br />
#include &#8220;foo.h&#8221;<br />
  void<br />
  main(int argc, char **argv)<br />
{<br />
    printf(&#8220;%d
&#8221;, arr[1]);<br />
}</p>
<p> Solution 1: </p>
<p>&#8211;foo.h extern int arr[];<br />
&#8211;foo.c<br />
#include &#8220;foo.h&#8221;<br />
  void<br />
  main(int argc, char **argv)<br />
{<br />
    /* This workaround is for win32 and cygwin; do not &#8220;optimize&#8221; */<br />
    volatile int *parr = arr;<br />
    printf(&#8220;%d
&#8221;, parr[1]);<br />
}</p>
<p> Solution 2: </p>
<pre><code>
--foo.h
/* Note: auto-export is assumed (no __declspec(dllexport)) */
#if (defined(_WIN32) || defined(__CYGWIN__)) &amp;&amp; \
    !(defined(FOO_BUILD_DLL) || defined(FOO_STATIC))
#define FOO_IMPORT __declspec(dllimport)
#else
#define FOO_IMPORT
#endif
  extern FOO_IMPORT int arr[];
--foo.c
#include "foo.h"
  void
  main(int argc, char **argv)
{
    printf("%d
", arr[1]);
}
</code></pre>
<p> A fourth way to avoid this problem is to re-code your library to use a functional interface rather than a data interface for the offending variables (e.g. <i>set_foo()</i> and <i>get_foo()</i> accessor functions). [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;disable-auto-import</code></p>
<dd> Do not attempt to do sophisticated linking of <tt>&quot;_symbol&quot;</tt> to <tt>&quot;__imp__symbol&quot;</tt> for <font SIZE="-1">DATA</font> imports from DLLs. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-runtime-pseudo-reloc</code></p>
<dd> If your code contains expressions described in &#8211;enable-auto-import section, that is, <font SIZE="-1">DATA</font> imports from <font SIZE="-1">DLL</font> with non-zero offset, this switch will create a vector of &#8216;runtime pseudo relocations&#8217; which can be used by runtime environment to adjust references to such data in your client code. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;disable-runtime-pseudo-reloc</code></p>
<dd> Do not create pseudo relocations for non-zero offset <font SIZE="-1">DATA</font> imports from DLLs. This is the default. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;enable-extra-pe-debug</code></p>
<dd> Show additional debug info related to auto-import symbol thunking. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;section-alignment</code></p>
<dd> Sets the section alignment. Sections in memory will always begin at addresses which are a multiple of this number. Defaults to 0x1000. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;stack</code> <i>reserve</i></p>
<dd>
<dt><code>&#8211;stack</code> <i>reserve</i><code>,</code><i>commit</i></p>
<dd> Specify the amount of memory to reserve (and optionally commit) to be used as stack for this program. The default is 2Mb reserved, 4K committed. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</p>
<dt><code>&#8211;subsystem</code> <i>which</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i></p>
<dd>
<dt><code>&#8211;subsystem</code> <i>which</i><code>:</code><i>major</i><code>.</code><i>minor</i></p>
<dd> Specifies the subsystem under which your program will execute. The legal values for <i>which</i> are <tt>&quot;native&quot;</tt>, <tt>&quot;windows&quot;</tt>, <tt>&quot;console&quot;</tt>, <tt>&quot;posix&quot;</tt>, and <tt>&quot;xbox&quot;</tt>. You may optionally set the subsystem version also. Numeric values are also accepted for <i>which</i>. [This option is specific to the i386 <font SIZE="-1">PE</font> targeted port of the linker]</dl>
<p> The 68HC11 and 68HC12 linkers support specific options to control the memory bank switching mapping and trampoline code generation.</p>
<dl>
<dt><code>&#8211;no-trampoline</code></p>
<dd> This option disables the generation of trampoline. By default a trampoline is generated for each far function which is called using a <tt>&quot;jsr&quot;</tt> instruction (this happens when a pointer to a far function is taken).</p>
<dt><code>&#8211;bank-window</code> <i>name</i></p>
<dd> This option indicates to the linker the name of the memory region in the <font SIZE="-1"><code>MEMORY</code></font> specification that describes the memory bank window. The definition of such region is then used by the linker to compute paging and addresses within the memory window.</dl>
<h2>ENVIRONMENT</h2>
<p> You can change the behaviour of <code>ld</code> with the environment variables <tt>&quot;GNUTARGET&quot;</tt>, <tt>&quot;LDEMULATION&quot;</tt> and <tt>&quot;COLLECT_NO_DEMANGLE&quot;</tt>. </p>
<p> <tt>&quot;GNUTARGET&quot;</tt> determines the input-file object format if you don&#8217;t use <code>-b</code> (or its synonym <code>&#8211;format</code>). Its value should be one of the <font SIZE="-1">BFD</font> names for an input format. If there is no <tt>&quot;GNUTARGET&quot;</tt> in the environment, <code>ld</code> uses the natural format of the target. If <tt>&quot;GNUTARGET&quot;</tt> is set to <tt>&quot;default&quot;</tt> then <font SIZE="-1">BFD</font> attempts to discover the input format by examining binary input files; this method often succeeds, but there are potential ambiguities, since there is no method of ensuring that the magic number used to specify object-file formats is unique. However, the configuration procedure for <font SIZE="-1">BFD</font> on each system places the conventional format for that system first in the search-list, so ambiguities are resolved in favor of convention. </p>
<p> <tt>&quot;LDEMULATION&quot;</tt> determines the default emulation if you don&#8217;t use the <code>-m</code> option. The emulation can affect various aspects of linker behaviour, particularly the default linker script. You can list the available emulations with the <code>&#8211;verbose</code> or <code>-V</code> options. If the <code>-m</code> option is not used, and the <tt>&quot;LDEMULATION&quot;</tt> environment variable is not defined, the default emulation depends upon how the linker was configured. </p>
<p> Normally, the linker will default to demangling symbols. However, if <tt>&quot;COLLECT_NO_DEMANGLE&quot;</tt> is set in the environment, then it will default to not demangling symbols. This environment variable is used in a similar fashion by the <tt>&quot;gcc&quot;</tt> linker wrapper program. The default may be overridden by the <code>&#8211;demangle</code> and <code>&#8211;no-demangle</code> options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), <i><a href="/docs/linux/man/1-objcopy/">objcopy</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1) and the Info entries for <i>binutils</i> and <i>ld</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 92, 93, 94, 95, 96, 97, 98, 99, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
