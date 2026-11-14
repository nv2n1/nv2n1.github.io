---
title: "x86_64-w64-mingw32-objdump(1)"
name: "x86_64-w64-mingw32-objdump"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-w64-mingw32-objdump/"
description: "objdump – display information from object files."
---

<h2 class="name">NAME</h2>
<p> objdump &#8211; display information from object files. </p>
<h2>SYNOPSIS</h2>
<p> objdump [<code>-a</code>|<code>&#8211;archive-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>&#8211;disassemble</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code>|<code>&#8211;disassemble-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-z</code>|<code>&#8211;disassemble-zeroes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-EB</code>|<code>-EL</code>|<code>&#8211;endian=</code>{big | little&nbsp;<wbr>}]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;file-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-F</code>|<code>&#8211;file-offsets</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;file-start-context</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>|<code>&#8211;debugging</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-e</code>|<code>&#8211;debugging-tags</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-h</code>|<code>&#8211;section-headers</code>|<code>&#8211;headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>|<code>&#8211;info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-j</code>&nbsp;<wbr><i>section</i>|<code>&#8211;section=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-l</code>|<code>&#8211;line-numbers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>|<code>&#8211;source</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-m</code>&nbsp;<wbr><i>machine</i>|<code>&#8211;architecture=</code><i>machine</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-M</code>&nbsp;<wbr><i>options</i>|<code>&#8211;disassembler-options=</code><i>options</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;private-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-P</code>&nbsp;<wbr><i>options</i>|<code>&#8211;private=</code><i>options</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-r</code>|<code>&#8211;reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-R</code>|<code>&#8211;dynamic-reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-s</code>|<code>&#8211;full-contents</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-W[lLiaprmfFsoRt]</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;dwarf</code>[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-G</code>|<code>&#8211;stabs</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-t</code>|<code>&#8211;syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-T</code>|<code>&#8211;dynamic-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-x</code>|<code>&#8211;all-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w</code>|<code>&#8211;wide</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;start-address=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;stop-address=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-addresses</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;[no-]show-raw-insn</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;adjust-vma=</code><i>offset</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;special-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix=</code><i>prefix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-strip=</code><i>level</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;insn-width=</code><i>width</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-H</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>objfile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>objdump</code> displays information about one or more object files. The options control what particular information to display. This information is mostly useful to programmers who are working on the compilation tools, as opposed to programmers who just want their program to compile and work. </p>
<p> <i>objfile</i>&#8230; are the object files to be examined. When you specify archives, <code>objdump</code> shows information on each of the member object files.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one option from the list <code>-a,-d,-D,-e,-f,-g,-G,-h,-H,-p,-P,-r,-R,-s,-S,-t,-T,-V,-x</code> must be given.</p>
<dl>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;archive-header</code></p>
<dd> If any of the <i>objfile</i> files are archives, display the archive header information (in a format similar to <code>ls -l</code>). Besides the information you could list with <code>ar tv</code>, <code>objdump -a</code> shows the object file format of each archive member.</p>
<dt><code>&#8211;adjust-vma=</code><i>offset</i></p>
<dd> When dumping information, first add <i>offset</i> to all the section addresses. This is useful if the section addresses do not correspond to the symbol table, which can happen when putting sections at particular addresses when using a format which can not represent section addresses, such as a.out.</p>
<dt><code>-b</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Specify that the object-code format for the object files is <i>bfdname</i>. This option may not be necessary; <i>objdump</i> can automatically recognize many formats. </p>
<p> For example, </p>
<pre>
        objdump -b oasys -m vax -h fu.o
</pre>
<p> displays summary information from the section headers (<code>-h</code>) of <i>fu.o</i>, which is explicitly identified (<code>-m</code>) as a <font SIZE="-1">VAX</font> object file in the format produced by Oasys compilers. You can list the formats available with the <code>-i</code> option.</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></p>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;debugging</code></p>
<dd> Display debugging information. This attempts to parse <font SIZE="-1">STABS</font> and <font SIZE="-1">IEEE</font> debugging format information stored in the file and print it out using a C like syntax. If neither of these formats are found this option falls back on the <code>-W</code> option to print any <font SIZE="-1">DWARF</font> information in the file.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;debugging-tags</code></p>
<dd> Like <code>-g</code>, but the information is generated in a format compatible with ctags tool.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;disassemble</code></p>
<dd> Display the assembler mnemonics for the machine instructions from <i>objfile</i>. This option only disassembles those sections which are expected to contain instructions.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;disassemble-all</code></p>
<dd> Like <code>-d</code>, but disassemble the contents of all sections, not just those expected to contain instructions. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture this switch also has the effect of forcing the disassembler to decode pieces of data found in code sections as if they were instructions.</p>
<dt><code>&#8211;prefix-addresses</code></p>
<dd> When disassembling, print the complete address on each line. This is the older disassembly format.</p>
<dt><code>-EB</code></p>
<dd>
<dt><code>-EL</code></p>
<dd>
<dt><code>&#8211;endian={big|little}</code></p>
<dd> Specify the endianness of the object files. This only affects disassembly. This can be useful when disassembling a file format which does not describe endianness information, such as S-records.</p>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;file-headers</code></p>
<dd> Display summary information from the overall header of each of the <i>objfile</i> files.</p>
<dt><code>-F</code></p>
<dd>
<dt><code>&#8211;file-offsets</code></p>
<dd> When disassembling sections, whenever a symbol is displayed, also display the file offset of the region of data that is about to be dumped. If zeroes are being skipped, then when disassembly resumes, tell the user how many zeroes were skipped and the file offset of the location from where the disassembly resumes. When dumping sections, display the file offset of the location from where the dump starts.</p>
<dt><code>&#8211;file-start-context</code></p>
<dd> Specify that when displaying interlisted source code/disassembly (assumes <code>-S</code>) from a file that has not yet been displayed, extend the context to the start of the file.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;section-headers</code></p>
<dd>
<dt><code>&#8211;headers</code></p>
<dd> Display summary information from the section headers of the object file. </p>
<p> File segments may be relocated to nonstandard addresses, for example by using the <code>-Ttext</code>, <code>-Tdata</code>, or <code>-Tbss</code> options to <code>ld</code>. However, some object file formats, such as a.out, do not store the starting address of the file segments. In those situations, although <code>ld</code> relocates the sections correctly, using <code>objdump -h</code> to list the file section headers cannot show the correct addresses. Instead, it shows the usual addresses, which are implicit for the target.</p>
<dt><code>-H</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the options to <code>objdump</code> and exit.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>&#8211;info</code></p>
<dd> Display a list showing all architectures and object formats available for specification with <code>-b</code> or <code>-m</code>.</p>
<dt><code>-j</code> <i>name</i></p>
<dd>
<dt><code>&#8211;section=</code><i>name</i></p>
<dd> Display information only for section <i>name</i>.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>&#8211;line-numbers</code></p>
<dd> Label the display (using debugging information) with the filename and source line numbers corresponding to the object code or relocs shown. Only useful with <code>-d</code>, <code>-D</code>, or <code>-r</code>.</p>
<dt><code>-m</code> <i>machine</i></p>
<dd>
<dt><code>&#8211;architecture=</code><i>machine</i></p>
<dd> Specify the architecture to use when disassembling object files. This can be useful when disassembling object files which do not describe architecture information, such as S-records. You can list the available architectures with the <code>-i</code> option. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch has an additional effect. It restricts the disassembly to only those instructions supported by the architecture specified by <i>machine</i>. If it is necessary to use this switch because the input file does not contain any architecture information, but it is also desired to disassemble all the instructions use <code>-marm</code>.</p>
<dt><code>-M</code> <i>options</i></p>
<dd>
<dt><code>&#8211;disassembler-options=</code><i>options</i></p>
<dd> Pass target specific information to the disassembler. Only supported on some targets. If it is necessary to specify more than one disassembler option then multiple <code>-M</code> options can be used or can be placed together into a comma separated list. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch can be used to select which register name set is used during disassembler. Specifying <code>-M reg-names-std</code> (the default) will select the register names as used in <font SIZE="-1">ARM</font>&#8216;s instruction set documentation, but with register 13 called &#8216;sp&#8217;, register 14 called &#8216;lr&#8217; and register 15 called &#8216;pc&#8217;. Specifying <code>-M reg-names-apcs</code> will select the name set used by the <font SIZE="-1">ARM</font> Procedure Call Standard, whilst specifying <code>-M reg-names-raw</code> will just use <code>r</code> followed by the register number. </p>
<p> There are also two variants on the <font SIZE="-1">APCS</font> register naming scheme enabled by <code>-M reg-names-atpcs</code> and <code>-M reg-names-special-atpcs</code> which use the ARM/Thumb Procedure Call Standard naming conventions. (Either with the normal register names or the special register names). </p>
<p> This option can also be used for <font SIZE="-1">ARM</font> architectures to force the disassembler to interpret all instructions as Thumb instructions by using the switch <code>&#8211;disassembler-options=force-thumb</code>. This can be useful when attempting to disassemble thumb code produced by other compilers. </p>
<p> For the x86, some of the options duplicate functions of the <code>-m</code> switch, but allow finer grained control. Multiple selections from the following may be specified as a comma separated string. <code>x86-64</code>, <code>i386</code> and <code>i8086</code> select disassembly for the given architecture. <code>intel</code> and <code>att</code> select between intel syntax mode and <font SIZE="-1">AT&amp;T</font> syntax mode. <code>intel-mnemonic</code> and <code>att-mnemonic</code> select between intel mnemonic mode and <font SIZE="-1">AT&amp;T</font> mnemonic mode. <code>intel-mnemonic</code> implies <code>intel</code> and <code>att-mnemonic</code> implies <code>att</code>. <code>addr64</code>, <code>addr32</code>, <code>addr16</code>, <code>data32</code> and <code>data16</code> specify the default address size and operand size. These four options will be overridden if <code>x86-64</code>, <code>i386</code> or <code>i8086</code> appear later in the option string. Lastly, <code>suffix</code>, when in <font SIZE="-1">AT&amp;T</font> mode, instructs the disassembler to print a mnemonic suffix even when the suffix could be inferred by the operands. </p>
<p> For PowerPC, <code>booke</code> controls the disassembly of BookE instructions. <code>32</code> and <code>64</code> select PowerPC and PowerPC64 disassembly, respectively. <code>e300</code> selects disassembly for the e300 family. <code>440</code> selects disassembly for the PowerPC 440. <code>ppcps</code> selects disassembly for the paired single instructions of the <font SIZE="-1">PPC750CL.</font> </p>
<p> For <font SIZE="-1">MIPS,</font> this option controls the printing of instruction mnemonic names and register names in disassembled instructions. Multiple selections from the following may be specified as a comma separated string, and invalid options are ignored:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;no-aliases&quot;</p>
<dd> Print the &#8216;raw&#8217; instruction mnemonic instead of some pseudo instruction mnemonic. I.e., print &#8216;daddu&#8217; or &#8216;or&#8217; instead of &#8216;move&#8217;, &#8216;sll&#8217; instead of &#8216;nop&#8217;, etc.</p>
<dt>&quot;msa&quot;</p>
<dd> Disassemble <font SIZE="-1">MSA</font> instructions.</p>
<dt>&quot;virt&quot;</p>
<dd> Disassemble the virtualization <font SIZE="-1">ASE</font> instructions.</p>
<dt>&quot;xpa&quot;</p>
<dd> Disassemble the eXtended Physical Address (<font SIZE="-1">XPA</font>) <font SIZE="-1">ASE</font> instructions.</p>
<dt>&quot;gpr-names=ABI<tt>&quot;</p>
<dd> Print </tt><font SIZE="-1"><tt>GPR </tt></font><tt>(general-purpose register) names as appropriate for the specified </tt><font SIZE="-1"><tt>ABI. </tt></font><tt> By default, </tt><font SIZE="-1"><tt>GPR</tt></font><tt> names are selected according to the </tt><font SIZE="-1"><tt>ABI</tt></font><tt> of the binary being disassembled.</p>
<dt>&quot;fpr-names=</tt>ABI<tt>&quot;</p>
<dd> Print </tt><font SIZE="-1"><tt>FPR </tt></font><tt>(floating-point register) names as appropriate for the specified </tt><font SIZE="-1"><tt>ABI. </tt></font><tt> By default, </tt><font SIZE="-1"><tt>FPR</tt></font><tt> numbers are printed rather than names.</p>
<dt>&quot;cp0-names=</tt>ARCH<tt>&quot;</p>
<dd> Print </tt><font SIZE="-1"><tt>CP0 </tt></font><tt>(system control coprocessor; coprocessor 0) register names as appropriate for the </tt><font SIZE="-1"><tt>CPU</tt></font><tt> or architecture specified by </tt><i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">CP0</font> register names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</p>
<dt>&quot;hwr-names=ARCH<tt>&quot;</p>
<dd> Print </tt><font SIZE="-1"><tt>HWR </tt></font><tt>(hardware register, used by the &quot;rdhwr&quot;</tt> instruction) names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">HWR</font> names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</p>
<dt>&quot;reg-names=ABI<tt>&quot;</p>
<dd> Print </tt><font SIZE="-1"><tt>GPR</tt></font><tt> and </tt><font SIZE="-1"><tt>FPR</tt></font><tt> names as appropriate for the selected </tt><font SIZE="-1"><tt>ABI.</tt></font><tt></p>
<dt>&quot;reg-names=</tt>ARCH<tt>&quot;</p>
<dd> Print CPU-specific register names (</tt><font SIZE="-1"><tt>CP0</tt></font><tt> register and </tt><font SIZE="-1"><tt>HWR</tt></font><tt> names) as appropriate for the selected </tt><font SIZE="-1"><tt>CPU</tt></font><tt> or architecture.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For any of the options listed above, </tt><i></i><font SIZE="-1"><i>ABI</i></font><i></i> or <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> may be specified as <code>numeric</code> to have numbers printed rather than names, for the selected types of registers. You can list the available values of <i></i><font SIZE="-1"><i>ABI</i></font><i></i> and <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> using the <code>&#8211;help</code> option. </p>
<p> For <font SIZE="-1">VAX,</font> you can specify function entry addresses with <code>-M entry:0xf00ba</code>. You can use this multiple times to properly disassemble <font SIZE="-1">VAX</font> binary files that don&#8217;t contain symbol tables (like <font SIZE="-1">ROM</font> dumps). In these cases, the function entry mask would otherwise be decoded as <font SIZE="-1">VAX</font> instructions, which would probably lead the rest of the function being wrongly disassembled.</dl>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;private-headers</code></p>
<dd> Print information that is specific to the object file format. The exact information printed depends upon the object file format. For some object file formats, no additional information is printed.</p>
<dt><code>-P</code> <i>options</i></p>
<dd>
<dt><code>&#8211;private=</code><i>options</i></p>
<dd> Print information that is specific to the object file format. The argument <i>options</i> is a comma separated list that depends on the format (the lists of options is displayed with the help). </p>
<p> For <font SIZE="-1">XCOFF,</font> the available options are: <code>header</code>, <code>aout</code>, <code>sections</code>, <code>syms</code>, <code>relocs</code>, <code>lineno</code>, <code>loader</code>, <code>except</code>, <code>typchk</code>, <code>traceback</code>, <code>toc</code> and <code>ldinfo</code>.</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;reloc</code></p>
<dd> Print the relocation entries of the file. If used with <code>-d</code> or <code>-D</code>, the relocations are printed interspersed with the disassembly.</p>
<dt><code>-R</code></p>
<dd>
<dt><code>&#8211;dynamic-reloc</code></p>
<dd> Print the dynamic relocation entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. As for <code>-r</code>, if used with <code>-d</code> or <code>-D</code>, the relocations are printed interspersed with the disassembly.</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;full-contents</code></p>
<dd> Display the full contents of any sections requested. By default all non-empty sections are displayed.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;source</code></p>
<dd> Display source code intermixed with disassembly, if possible. Implies <code>-d</code>.</p>
<dt><code>&#8211;prefix=</code><i>prefix</i></p>
<dd> Specify <i>prefix</i> to add to the absolute paths when used with <code>-S</code>.</p>
<dt><code>&#8211;prefix-strip=</code><i>level</i></p>
<dd> Indicate how many initial directory names to strip off the hardwired absolute paths. It has no effect without <code>&#8211;prefix=</code><i>prefix</i>.</p>
<dt><code>&#8211;show-raw-insn</code></p>
<dd> When disassembling instructions, print the instruction in hex as well as in symbolic form. This is the default except when <code>&#8211;prefix-addresses</code> is used.</p>
<dt><code>&#8211;no-show-raw-insn</code></p>
<dd> When disassembling instructions, do not print the instruction bytes. This is the default when <code>&#8211;prefix-addresses</code> is used.</p>
<dt><code>&#8211;insn-width=</code><i>width</i></p>
<dd> Display <i>width</i> bytes on a single line when disassembling instructions.</p>
<dt><code>-W[lLiaprmfFsoRt]</code></p>
<dd>
<dt><code>&#8211;dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index]</code></p>
<dd> Displays the contents of the debug sections in the file, if any are present. If one of the optional letters or words follows the switch then only data found in those specific sections will be dumped. </p>
<p> Note that there is no single letter option to display the content of trace sections or .gdb_index. </p>
<p> Note: the output from the <code>=info</code> option can also be affected by the options <code>&#8211;dwarf-depth</code>, the <code>&#8211;dwarf-start</code> and the <code>&#8211;dwarf-check</code>.</p>
<dt><code>&#8211;dwarf-depth=</code><i>n</i></p>
<dd> Limit the dump of the <tt>&quot;.debug_info&quot;</tt> section to <i>n</i> children. This is only useful with <code>&#8211;dwarf=info</code>. The default is to print all DIEs; the special value 0 for <i>n</i> will also have this effect. </p>
<p> With a non-zero value for <i>n</i>, DIEs at or deeper than <i>n</i> levels will not be printed. The range for <i>n</i> is zero-based.</p>
<dt><code>&#8211;dwarf-start=</code><i>n</i></p>
<dd> Print only DIEs beginning with the <font SIZE="-1">DIE</font> numbered <i>n</i>. This is only useful with <code>&#8211;dwarf=info</code>. </p>
<p> If specified, this option will suppress printing of any header information and all DIEs before the <font SIZE="-1">DIE</font> numbered <i>n</i>. Only siblings and children of the specified <font SIZE="-1">DIE</font> will be printed. </p>
<p> This can be used in conjunction with <code>&#8211;dwarf-depth</code>.</p>
<dt><code>&#8211;dwarf-check</code></p>
<dd> Enable additional checks for consistency of Dwarf information.</p>
<dt><code>-G</code></p>
<dd>
<dt><code>&#8211;stabs</code></p>
<dd> Display the full contents of any sections requested. Display the contents of the .stab and .stab.index and .stab.excl sections from an <font SIZE="-1">ELF</font> file. This is only useful on systems (such as Solaris 2.0) in which <tt>&quot;.stab&quot;</tt> debugging symbol-table entries are carried in an <font SIZE="-1">ELF</font> section. In most other file formats, debugging symbol-table entries are interleaved with linkage symbols, and are visible in the <code>&#8211;syms</code> output.</p>
<dt><code>&#8211;start-address=</code><i>address</i></p>
<dd> Start displaying data at the specified address. This affects the output of the <code>-d</code>, <code>-r</code> and <code>-s</code> options.</p>
<dt><code>&#8211;stop-address=</code><i>address</i></p>
<dd> Stop displaying data at the specified address. This affects the output of the <code>-d</code>, <code>-r</code> and <code>-s</code> options.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;syms</code></p>
<dd> Print the symbol table entries of the file. This is similar to the information provided by the <code>nm</code> program, although the display format is different. The format of the output depends upon the format of the file being dumped, but there are two main types. One looks like this: </p>
<pre><code>
[4](sec 3)(fl 0x00)(ty 0)(scl 3)(nx 1)0x00000000.bss
    [6](sec 1)(fl 0x00)(ty 0)(scl 2)(nx 0)0x00000000 fred
</code></pre>
<p> where the number inside the square brackets is the number of the entry in the symbol table, the <i>sec</i> number is the section number, the <i>fl</i> value are the symbol&#8217;s flag bits, the <i>ty</i> number is the symbol&#8217;s type, the <i>scl</i> number is the symbol&#8217;s storage class and the <i>nx</i> value is the number of auxilary entries associated with the symbol. The last two fields are the symbol&#8217;s value and its name. </p>
<p> The other common output format, usually seen with <font SIZE="-1">ELF</font> based files, looks like this: </p>
<pre>
        00000000 l    d  .bss   00000000 .bss
        00000000 g       .text  00000000 fred
</pre>
<p> Here the first number is the symbol&#8217;s value (sometimes refered to as its address). The next field is actually a set of characters and spaces indicating the flag bits that are set on the symbol. These characters are described below. Next is the section with which the symbol is associated or <i>*ABS*</i> if the section is absolute (ie not connected with any section), or <i>*UND*</i> if the section is referenced in the file being dumped, but not defined there. </p>
<p> After the section name comes another field, a number, which for common symbols is the alignment and for other symbol is the size. Finally the symbol&#8217;s name is displayed. </p>
<p> The flag characters are divided into 7 groups as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;l&quot;</p>
<dd>
<dt>&quot;g&quot;</p>
<dd>
<dt>&quot;u&quot;</p>
<dd>
<dt>&quot;!&quot;</p>
<dd> The symbol is a local (l), global (g), unique global (u), neither global nor local (a space) or both global and local (!). A symbol can be neither local or global for a variety of reasons, e.g., because it is used for debugging, but it is probably an indication of a bug if it is ever both local and global. Unique global symbols are a <font SIZE="-1">GNU</font> extension to the standard set of <font SIZE="-1">ELF</font> symbol bindings. For such a symbol the dynamic linker will make sure that in the entire process there is just one symbol with this name and type in use.</p>
<dt>&quot;w&quot;</p>
<dd> The symbol is weak (w) or strong (a space).</p>
<dt>&quot;C&quot;</p>
<dd> The symbol denotes a constructor (C) or an ordinary symbol (a space).</p>
<dt>&quot;W&quot;</p>
<dd> The symbol is a warning (W) or a normal symbol (a space). A warning symbol&#8217;s name is a message to be displayed if the symbol following the warning symbol is ever referenced.</p>
<dt>&quot;I&quot;</p>
<dd>
<dt>&quot;i&quot;</p>
<dd> The symbol is an indirect reference to another symbol (I), a function to be evaluated during reloc processing (i) or a normal symbol (a space).</p>
<dt>&quot;d&quot;</p>
<dd>
<dt>&quot;D&quot;</p>
<dd> The symbol is a debugging symbol (d) or a dynamic symbol (D) or a normal symbol (a space).</p>
<dt>&quot;F&quot;</p>
<dd>
<dt>&quot;f&quot;</p>
<dd>
<dt>&quot;O&quot;</p>
<dd> The symbol is the name of a function (F) or a file (f) or an object (O) or just a normal symbol (a space).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-T</code></p>
<dd>
<dt><code>&#8211;dynamic-syms</code></p>
<dd> Print the dynamic symbol table entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. This is similar to the information provided by the <code>nm</code> program when given the <code>-D</code> (<code>&#8211;dynamic</code>) option.</p>
<dt><code>&#8211;special-syms</code></p>
<dd> When displaying symbols include those which the target considers to be special in some way and which would not normally be of interest to the user.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Print the version number of <code>objdump</code> and exit.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;all-headers</code></p>
<dd> Display all available header information, including the symbol table and relocation entries. Using <code>-x</code> is equivalent to specifying all of <code>-a -f -h -p -r -t</code>.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;wide</code></p>
<dd> Format some lines for output devices that have more than 80 columns. Also do not truncate symbol names when they are displayed.</p>
<dt><code>-z</code></p>
<dd>
<dt><code>&#8211;disassemble-zeroes</code></p>
<dd> Normally the disassembly output will skip blocks of zeroes. This option directs the disassembler to disassemble those blocks, just like any other data.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991-2014 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
