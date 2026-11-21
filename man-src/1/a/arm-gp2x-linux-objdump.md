---
title: "arm-gp2x-linux-objdump(1)"
name: "arm-gp2x-linux-objdump"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-objdump/"
description: "objdump – display information from object files."
---

<h2>NAME</h2>
<p> objdump &#8211; display information from object files.</p>
<h2>SYNOPSIS</h2>
<p> objdump [<code>-a</code>|<code>&#8211;archive-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>&#8211;disassemble</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code>|<code>&#8211;disassemble-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-z</code>|<code>&#8211;disassemble-zeroes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-EB</code>|<code>-EL</code>|<code>&#8211;endian=</code>{big | little&nbsp;<wbr>}]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-f</code>|<code>&#8211;file-headers</code>]<br />
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
&nbsp;<wbr>&nbsp;<wbr>[<code>-r</code>|<code>&#8211;reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-R</code>|<code>&#8211;dynamic-reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-s</code>|<code>&#8211;full-contents</code>]<br />
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
&nbsp;<wbr>&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-H</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>objfile</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>objdump</code> displays information about one or more object files. The options control what particular information to display. This information is mostly useful to programmers who are working on the compilation tools, as opposed to programmers who just want their program to compile and work. </p>
<p> <i>objfile</i>&#8230; are the object files to be examined. When you specify archives, <code>objdump</code> shows information on each of the member object files.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one option from the list <code>-a,-d,-D,-e,-f,-g,-G,-h,-H,-p,-r,-R,-s,-S,-t,-T,-V,-x</code> must be given.</p>
<dl>
<dt><code>-a</code></dt>
<dd>
</dd><dt><code>&#8211;archive-header</code></dt>
<dd> If any of the <i>objfile</i> files are archives, display the archive header information (in a format similar to <code>ls -l</code>). Besides the information you could list with <code>ar tv</code>, <code>objdump -a</code> shows the object file format of each archive member.</dd>
<dt><code>&#8211;adjust-vma=</code><i>offset</i></dt>
<dd> When dumping information, first add <i>offset</i> to all the section addresses. This is useful if the section addresses do not correspond to the symbol table, which can happen when putting sections at particular addresses when using a format which can not represent section addresses, such as a.out.</dd>
<dt><code>-b</code> <i>bfdname</i></dt>
<dd>
</dd><dt><code>&#8211;target=</code><i>bfdname</i></dt>
<dd> Specify that the object-code format for the object files is <i>bfdname</i>. This option may not be necessary; <i>objdump</i> can automatically recognize many formats. </dd>
<p> For example, </p>
<pre>
        objdump -b oasys -m vax -h fu.o
</pre>
<p> displays summary information from the section headers (<code>-h</code>) of <i>fu.o</i>, which is explicitly identified (<code>-m</code>) as a <font SIZE="-1">VAX</font> object file in the format produced by Oasys compilers. You can list the formats available with the <code>-i</code> option.</p>
<dt><code>-C</code></dt>
<dd>
</dd><dt><code>&#8211;demangle[=</code><i>style</i><code>]</code></dt>
<dd> Decode (<i>demangle</i>) low-level symbol names into user-level names. Besides removing any initial underscore prepended by the system, this makes C<font SIZE="-2">++</font> function names readable. Different compilers have different mangling styles. The optional demangling style argument can be used to choose an appropriate demangling style for your compiler.</dd>
<dt><code>-g</code></dt>
<dd>
</dd><dt><code>&#8211;debugging</code></dt>
<dd> Display debugging information. This attempts to parse debugging information stored in the file and print it out using a C like syntax. Only certain types of debugging information have been implemented. Some other types are supported by <code>readelf -w</code>.</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>&#8211;debugging-tags</code></dt>
<dd> Like <code>-g</code>, but the information is generated in a format compatible with ctags tool.</dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble</code></dt>
<dd> Display the assembler mnemonics for the machine instructions from <i>objfile</i>. This option only disassembles those sections which are expected to contain instructions.</dd>
<dt><code>-D</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble-all</code></dt>
<dd> Like <code>-d</code>, but disassemble the contents of all sections, not just those expected to contain instructions.</dd>
<dt><code>&#8211;prefix-addresses</code></dt>
<dd> When disassembling, print the complete address on each line. This is the older disassembly format.</dd>
<dt><code>-EB</code></dt>
<dd>
</dd><dt><code>-EL</code></dt>
<dd>
</dd><dt><code>&#8211;endian={big|little}</code></dt>
<dd> Specify the endianness of the object files. This only affects disassembly. This can be useful when disassembling a file format which does not describe endianness information, such as S-records.</dd>
<dt><code>-f</code></dt>
<dd>
</dd><dt><code>&#8211;file-headers</code></dt>
<dd> Display summary information from the overall header of each of the <i>objfile</i> files.</dd>
<dt><code>&#8211;file-start-context</code></dt>
<dd> Specify that when displaying interlisted source code/disassembly (assumes <code>-S</code>) from a file that has not yet been displayed, extend the context to the start of the file.</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;section-headers</code></dt>
<dd>
</dd><dt><code>&#8211;headers</code></dt>
<dd> Display summary information from the section headers of the object file. </dd>
<p> File segments may be relocated to nonstandard addresses, for example by using the <code>-Ttext</code>, <code>-Tdata</code>, or <code>-Tbss</code> options to <code>ld</code>. However, some object file formats, such as a.out, do not store the starting address of the file segments. In those situations, although <code>ld</code> relocates the sections correctly, using <code>objdump -h</code> to list the file section headers cannot show the correct addresses. Instead, it shows the usual addresses, which are implicit for the target.</p>
<dt><code>-H</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Print a summary of the options to <code>objdump</code> and exit.</dd>
<dt><code>-i</code></dt>
<dd>
</dd><dt><code>&#8211;info</code></dt>
<dd> Display a list showing all architectures and object formats available for specification with <code>-b</code> or <code>-m</code>.</dd>
<dt><code>-j</code> <i>name</i></dt>
<dd>
</dd><dt><code>&#8211;section=</code><i>name</i></dt>
<dd> Display information only for section <i>name</i>.</dd>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>&#8211;line-numbers</code></dt>
<dd> Label the display (using debugging information) with the filename and source line numbers corresponding to the object code or relocs shown. Only useful with <code>-d</code>, <code>-D</code>, or <code>-r</code>.</dd>
<dt><code>-m</code> <i>machine</i></dt>
<dd>
</dd><dt><code>&#8211;architecture=</code><i>machine</i></dt>
<dd> Specify the architecture to use when disassembling object files. This can be useful when disassembling object files which do not describe architecture information, such as S-records. You can list the available architectures with the <code>-i</code> option.</dd>
<dt><code>-M</code> <i>options</i></dt>
<dd>
</dd><dt><code>&#8211;disassembler-options=</code><i>options</i></dt>
<dd> Pass target specific information to the disassembler. Only supported on some targets. If it is necessary to specify more than one disassembler option then multiple <code>-M</code> options can be used or can be placed together into a comma separated list. </dd>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch can be used to select which register name set is used during disassembler. Specifying <code>-M reg-name-std</code> (the default) will select the register names as used in <font SIZE="-1">ARM</font>&#8216;s instruction set documentation, but with register 13 called &#8216;sp&#8217;, register 14 called &#8216;lr&#8217; and register 15 called &#8216;pc&#8217;. Specifying <code>-M reg-names-apcs</code> will select the name set used by the <font SIZE="-1">ARM</font> Procedure Call Standard, whilst specifying <code>-M reg-names-raw</code> will just use <code>r</code> followed by the register number. </p>
<p> There are also two variants on the <font SIZE="-1">APCS</font> register naming scheme enabled by <code>-M reg-names-atpcs</code> and <code>-M reg-names-special-atpcs</code> which use the ARM/Thumb Procedure Call Standard naming conventions. (Either with the normal register names or the special register names). </p>
<p> This option can also be used for <font SIZE="-1">ARM</font> architectures to force the disassembler to interpret all instructions as Thumb instructions by using the switch <code>&#8211;disassembler-options=force-thumb</code>. This can be useful when attempting to disassemble thumb code produced by other compilers. </p>
<p> For the x86, some of the options duplicate functions of the <code>-m</code> switch, but allow finer grained control. Multiple selections from the following may be specified as a comma separated string. <code>x86-64</code>, <code>i386</code> and <code>i8086</code> select disassembly for the given architecture. <code>intel</code> and <code>att</code> select between intel syntax mode and <font SIZE="-1">AT&amp;T</font> syntax mode. <code>addr32</code>, <code>addr16</code>, <code>data32</code> and <code>data16</code> specify the default address size and operand size. These four options will be overridden if <code>x86-64</code>, <code>i386</code> or <code>i8086</code> appear later in the option string. Lastly, <code>suffix</code>, when in <font SIZE="-1">AT&amp;T</font> mode, instructs the disassembler to print a mnemonic suffix even when the suffix could be inferred by the operands. </p>
<p> For <font SIZE="-1">PPC</font>, <code>booke</code>, <code>booke32</code> and <code>booke64</code> select disassembly of BookE instructions. <code>32</code> and <code>64</code> select PowerPC and PowerPC64 disassembly, respectively. </p>
<p> For <font SIZE="-1">MIPS</font>, this option controls the printing of instruction mneumonic names and register names in disassembled instructions. Multiple selections from the following may be specified as a comma separated string, and invalid options are ignored:</p>
<dl>
<dl>
<dt>no-aliases</dt>
<dd> Print the &#8216;raw&#8217; instruction mneumonic instead of some pseudo instruction mneumonic. I.E. print &#8216;daddu&#8217; or &#8216;or&#8217; instead of &#8216;move&#8217;, &#8216;sll&#8217; instead of &#8216;nop&#8217;, etc.</dd>
<dt>gpr-names=<font SIZE="-1">ABI</font><tt></dt>
<dd> Print </tt><font SIZE="-1"><tt>GPR</tt></font><tt> (general-purpose register) names as appropriate for the specified </tt><font SIZE="-1"><tt>ABI</tt></font><tt>. By default, </tt><font SIZE="-1"><tt>GPR</tt></font><tt> names are selected according to the </tt><font SIZE="-1"><tt>ABI</tt></font><tt> of the binary being disassembled.</dd>
<dt>fpr-names=</tt><font SIZE="-1">ABI</font><tt></dt>
<dd> Print </tt><font SIZE="-1"><tt>FPR</tt></font><tt> (floating-point register) names as appropriate for the specified </tt><font SIZE="-1"><tt>ABI</tt></font><tt>. By default, </tt><font SIZE="-1"><tt>FPR</tt></font><tt> numbers are printed rather than names.</dd>
<dt>cp0-names=</tt><font SIZE="-1">ARCH</font><tt></dt>
<dd> Print </tt><font SIZE="-1"><tt>CP0</tt></font><tt> (system control coprocessor; coprocessor 0) register names as appropriate for the </tt><font SIZE="-1"><tt>CPU</tt></font><tt> or architecture specified by </tt><i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">CP0</font> register names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</dd>
<dt>hwr-names=<font SIZE="-1">ARCH</font><tt></dt>
<dd> Print </tt><font SIZE="-1"><tt>HWR</tt></font><tt> (hardware register, used by the &quot;rdhwr&quot;</tt> instruction) names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">HWR</font> names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</dd>
<dt>reg-names=<font SIZE="-1">ABI</font><tt></dt>
<dd> Print </tt><font SIZE="-1"><tt>GPR</tt></font><tt> and </tt><font SIZE="-1"><tt>FPR</tt></font><tt> names as appropriate for the selected </tt><font SIZE="-1"><tt>ABI</tt></font><tt>.</dd>
<dt>reg-names=</tt><font SIZE="-1">ARCH</font><tt></dt>
<dd> Print CPU-specific register names (</tt><font SIZE="-1"><tt>CP0</tt></font><tt> register and </tt><font SIZE="-1"><tt>HWR</tt></font><tt> names) as appropriate for the selected </tt><font SIZE="-1"><tt>CPU</tt></font><tt> or architecture.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For any of the options listed above, </tt><i></i><font SIZE="-1"><i>ABI</i></font><i></i> or <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> may be specified as <code>numeric</code> to have numbers printed rather than names, for the selected types of registers. You can list the available values of <i></i><font SIZE="-1"><i>ABI</i></font><i></i> and <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> using the <code>&#8211;help</code> option.</dd></dl>
<dt><code>-p</code></dt>
<dd>
</dd><dt><code>&#8211;private-headers</code></dt>
<dd> Print information that is specific to the object file format. The exact information printed depends upon the object file format. For some object file formats, no additional information is printed.</dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;reloc</code></dt>
<dd> Print the relocation entries of the file. If used with <code>-d</code> or <code>-D</code>, the relocations are printed interspersed with the disassembly.</dd>
<dt><code>-R</code></dt>
<dd>
</dd><dt><code>&#8211;dynamic-reloc</code></dt>
<dd> Print the dynamic relocation entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries.</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;full-contents</code></dt>
<dd> Display the full contents of any sections requested. By default all non-empty sections are displayed.</dd>
<dt><code>-S</code></dt>
<dd>
</dd><dt><code>&#8211;source</code></dt>
<dd> Display source code intermixed with disassembly, if possible. Implies <code>-d</code>.</dd>
<dt><code>&#8211;show-raw-insn</code></dt>
<dd> When disassembling instructions, print the instruction in hex as well as in symbolic form. This is the default except when <code>&#8211;prefix-addresses</code> is used.</dd>
<dt><code>&#8211;no-show-raw-insn</code></dt>
<dd> When disassembling instructions, do not print the instruction bytes. This is the default when <code>&#8211;prefix-addresses</code> is used.</dd>
<dt><code>-G</code></dt>
<dd>
</dd><dt><code>&#8211;stabs</code></dt>
<dd> Display the full contents of any sections requested. Display the contents of the .stab and .stab.index and .stab.excl sections from an <font SIZE="-1">ELF</font> file. This is only useful on systems (such as Solaris 2.0) in which <tt>&quot;.stab&quot;</tt> debugging symbol-table entries are carried in an <font SIZE="-1">ELF</font> section. In most other file formats, debugging symbol-table entries are interleaved with linkage symbols, and are visible in the <code>&#8211;syms</code> output.</dd>
<dt><code>&#8211;start-address=</code><i>address</i></dt>
<dd> Start displaying data at the specified address. This affects the output of the <code>-d</code>, <code>-r</code> and <code>-s</code> options.</dd>
<dt><code>&#8211;stop-address=</code><i>address</i></dt>
<dd> Stop displaying data at the specified address. This affects the output of the <code>-d</code>, <code>-r</code> and <code>-s</code> options.</dd>
<dt><code>-t</code></dt>
<dd>
</dd><dt><code>&#8211;syms</code></dt>
<dd> Print the symbol table entries of the file. This is similar to the information provided by the <code>nm</code> program.</dd>
<dt><code>-T</code></dt>
<dd>
</dd><dt><code>&#8211;dynamic-syms</code></dt>
<dd> Print the dynamic symbol table entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. This is similar to the information provided by the <code>nm</code> program when given the <code>-D</code> (<code>&#8211;dynamic</code>) option.</dd>
<dt><code>&#8211;special-syms</code></dt>
<dd> When displaying symbols include those which the target considers to be special in some way and which would not normally be of interest to the user.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Print the version number of <code>objdump</code> and exit.</dd>
<dt><code>-x</code></dt>
<dd>
</dd><dt><code>&#8211;all-headers</code></dt>
<dd> Display all available header information, including the symbol table and relocation entries. Using <code>-x</code> is equivalent to specifying all of <code>-a -f -h -p -r -t</code>.</dd>
<dt><code>-w</code></dt>
<dd>
</dd><dt><code>&#8211;wide</code></dt>
<dd> Format some lines for output devices that have more than 80 columns. Also do not truncate symbol names when they are displayed.</dd>
<dt><code>-z</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble-zeroes</code></dt>
<dd> Normally the disassembly output will skip blocks of zeroes. This option directs the disassembler to disassemble those blocks, just like any other data.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
