---
title: "objdump(1)"
name: "objdump"
section: "1"
letter: "o"
url: "/docs/linux/man/1-objdump/"
description: "objdump – display information from object files"
---

<h2 class="name">NAME</h2>
<p> objdump &#8211; display information from object files </p>
<h2>SYNOPSIS</h2>
<p> objdump [<code>-a</code>|<code>&#8211;archive-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-b</code>&nbsp;<i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-C</code>|<code>&#8211;demangle</code>[=<i>style</i>]&nbsp;]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-d</code>|<code>&#8211;disassemble</code>[=<i>symbol</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-D</code>|<code>&#8211;disassemble-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-z</code>|<code>&#8211;disassemble-zeroes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-EB</code>|<code>-EL</code>|<code>&#8211;endian=</code>{big | little&nbsp;}]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-f</code>|<code>&#8211;file-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-F</code>|<code>&#8211;file-offsets</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;file-start-context</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-g</code>|<code>&#8211;debugging</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-e</code>|<code>&#8211;debugging-tags</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;section-headers</code>|<code>&#8211;headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-i</code>|<code>&#8211;info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-j</code>&nbsp;<i>section</i>|<code>&#8211;section=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>&#8211;line-numbers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-S</code>|<code>&#8211;source</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;source-comment</code>[=<i>text</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-m</code>&nbsp;<i>machine</i>|<code>&#8211;architecture=</code><i>machine</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-M</code>&nbsp;<i>options</i>|<code>&#8211;disassembler-options=</code><i>options</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>|<code>&#8211;private-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-P</code>&nbsp;<i>options</i>|<code>&#8211;private=</code><i>options</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>&#8211;reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-R</code>|<code>&#8211;dynamic-reloc</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-s</code>|<code>&#8211;full-contents</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-W[lLiaprmfFsoORtUuTgAck]</code>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&#8211;dwarf</code>[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=str-offsets,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index,=addr,=cu_index,=links]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-WK</code>|<code>&#8211;dwarf=follow-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-WN</code>|<code>&#8211;dwarf=no-follow-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-L</code>|<code>&#8211;process-links</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-G</code>|<code>&#8211;stabs</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-t</code>|<code>&#8211;syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-T</code>|<code>&#8211;dynamic-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-x</code>|<code>&#8211;all-headers</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-w</code>|<code>&#8211;wide</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;start-address=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;stop-address=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;no-addresses</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;prefix-addresses</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;[no-]show-raw-insn</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;adjust-vma=</code><i>offset</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;dwarf-depth=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;dwarf-start=</code><i>n</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;ctf-parent=</code><i>section</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;no-recurse-limit</code>|<code>&#8211;recurse-limit</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;special-syms</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;prefix=</code><i>prefix</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;prefix-strip=</code><i>level</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;insn-width=</code><i>width</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;visualize-jumps[=color|=extended-color|=off]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-U</code>&nbsp;<i>method</i>]&nbsp;[<code>&#8211;unicode=</code><i>method</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-H</code>|<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>objfile</i>&#8230;</p>
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
<dt><code>&#8211;recurse-limit</code></p>
<dd>
<dt><code>&#8211;no-recurse-limit</code></p>
<dd>
<dt><code>&#8211;recursion-limit</code></p>
<dd>
<dt><code>&#8211;no-recursion-limit</code></p>
<dd> Enables or disables a limit on the amount of recursion performed whilst demangling strings. Since the name mangling formats allow for an infinite level of recursion it is possible to create strings whose decoding will exhaust the amount of stack space available on the host machine, triggering a memory fault. The limit tries to prevent this from happening by restricting recursion to 2048 levels of nesting. </p>
<p> The default is for this limit to be enabled, but disabling it may be necessary in order to demangle truly complicated names. Note however that if the recursion limit is disabled then stack exhaustion is possible and any bug reports about such an event will be rejected.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;debugging</code></p>
<dd> Display debugging information. This attempts to parse <font SIZE="-1">STABS</font> debugging format information stored in the file and print it out using a C like syntax. If no <font SIZE="-1">STABS</font> debugging was found this option falls back on the <code>-W</code> option to print any <font SIZE="-1">DWARF</font> information in the file.</p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;debugging-tags</code></p>
<dd> Like <code>-g</code>, but the information is generated in a format compatible with ctags tool.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;disassemble</code></p>
<dd>
<dt><code>&#8211;disassemble=</code><i>symbol</i></p>
<dd> Display the assembler mnemonics for the machine instructions from the input file. This option only disassembles those sections which are expected to contain instructions. If the optional <i>symbol</i> argument is given, then display the assembler mnemonics starting at <i>symbol</i>. If <i>symbol</i> is a function name then disassembly will stop at the end of the function, otherwise it will stop when the next symbol is encountered. If there are no matches for <i>symbol</i> then nothing will be displayed. </p>
<p> Note if the <code>&#8211;dwarf=follow-links</code> option is enabled then any symbol tables in linked debug info files will be read in and used when disassembling.</p>
<dt><code>-D</code></p>
<dd>
<dt><code>&#8211;disassemble-all</code></p>
<dd> Like <code>-d</code>, but disassemble the contents of all sections, not just those expected to contain instructions. </p>
<p> This option also has a subtle effect on the disassembly of instructions in code sections. When option <code>-d</code> is in effect objdump will assume that any symbols present in a code section occur on the boundary between instructions and it will refuse to disassemble across such a boundary. When option <code>-D</code> is in effect however this assumption is supressed. This means that it is possible for the output of <code>-d</code> and <code>-D</code> to differ if, for example, data is stored in code sections. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture this switch also has the effect of forcing the disassembler to decode pieces of data found in code sections as if they were instructions. </p>
<p> Note if the <code>&#8211;dwarf=follow-links</code> option is enabled then any symbol tables in linked debug info files will be read in and used when disassembling.</p>
<dt><code>&#8211;no-addresses</code></p>
<dd> When disassembling, don&#8217;t print addresses on each line or for symbols and relocation offsets. In combination with <code>&#8211;no-show-raw-insn</code> this may be useful for comparing compiler output.</p>
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
<p> File segments may be relocated to nonstandard addresses, for example by using the <code>-Ttext</code>, <code>-Tdata</code>, or <code>-Tbss</code> options to <code>ld</code>. However, some object file formats, such as a.out, do not store the starting address of the file segments. In those situations, although <code>ld</code> relocates the sections correctly, using <code>objdump -h</code> to list the file section headers cannot show the correct addresses. Instead, it shows the usual addresses, which are implicit for the target. </p>
<p> Note, in some cases it is possible for a section to have both the <font SIZE="-1">READONLY</font> and the <font SIZE="-1">NOREAD</font> attributes set. In such cases the <font SIZE="-1">NOREAD</font> attribute takes precedence, but <code>objdump</code> will report both since the exact setting of the flag bits might be important.</p>
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
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;process-links</code></p>
<dd> Display the contents of non-debug sections found in separate debuginfo files that are linked to the main file. This option automatically implies the <code>-WK</code> option, and only sections requested by other command line options will be displayed.</p>
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
<p> For <font SIZE="-1">ARC,</font> <code>dsp</code> controls the printing of <font SIZE="-1">DSP</font> instructions, <code>spfp</code> selects the printing of <font SIZE="-1">FPX</font> single precision <font SIZE="-1">FP</font> instructions, <code>dpfp</code> selects the printing of <font SIZE="-1">FPX</font> double precision <font SIZE="-1">FP</font> instructions, <code>quarkse_em</code> selects the printing of special QuarkSE-EM instructions, <code>fpuda</code> selects the printing of double precision assist instructions, <code>fpus</code> selects the printing of <font SIZE="-1">FPU</font> single precision <font SIZE="-1">FP</font> instructions, while <code>fpud</code> selects the printing of <font SIZE="-1">FPU</font> double precision <font SIZE="-1">FP</font> instructions. Additionally, one can choose to have all the immediates printed in hexadecimal using <code>hex</code>. By default, the short immediates are printed using the decimal representation, while the long immediate values are printed as hexadecimal. </p>
<p> <code>cpu=&#8230;</code> allows one to enforce a particular <font SIZE="-1">ISA</font> when disassembling instructions, overriding the <code>-m</code> value or whatever is in the <font SIZE="-1">ELF</font> file. This might be useful to select <font SIZE="-1">ARC EM</font> or <font SIZE="-1">HS ISA,</font> because architecture is same for those and disassembler relies on private <font SIZE="-1">ELF</font> header data to decide if code is for <font SIZE="-1">EM</font> or <font SIZE="-1">HS.</font> This option might be specified multiple times &#8211; only the latest value will be used. Valid values are same as for the assembler <code>-mcpu=&#8230;</code> option. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch can be used to select which register name set is used during disassembler. Specifying <code>-M reg-names-std</code> (the default) will select the register names as used in <font SIZE="-1">ARM</font>&#8216;s instruction set documentation, but with register 13 called &#8216;sp&#8217;, register 14 called &#8216;lr&#8217; and register 15 called &#8216;pc&#8217;. Specifying <code>-M reg-names-apcs</code> will select the name set used by the <font SIZE="-1">ARM</font> Procedure Call Standard, whilst specifying <code>-M reg-names-raw</code> will just use <code>r</code> followed by the register number. </p>
<p> There are also two variants on the <font SIZE="-1">APCS</font> register naming scheme enabled by <code>-M reg-names-atpcs</code> and <code>-M reg-names-special-atpcs</code> which use the ARM/Thumb Procedure Call Standard naming conventions. (Either with the normal register names or the special register names). </p>
<p> This option can also be used for <font SIZE="-1">ARM</font> architectures to force the disassembler to interpret all instructions as Thumb instructions by using the switch <code>&#8211;disassembler-options=force-thumb</code>. This can be useful when attempting to disassemble thumb code produced by other compilers. </p>
<p> For AArch64 targets this switch can be used to set whether instructions are disassembled as the most general instruction using the <code>-M no-aliases</code> option or whether instruction notes should be generated as comments in the disasssembly using <code>-M notes</code>. </p>
<p> For the x86, some of the options duplicate functions of the <code>-m</code> switch, but allow finer grained control.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;x86-64&quot;</p>
<dd>
<dt>&quot;i386&quot;</p>
<dd>
<dt>&quot;i8086&quot;</p>
<dd> Select disassembly for the given architecture.</p>
<dt>&quot;intel&quot;</p>
<dd>
<dt>&quot;att&quot;</p>
<dd> Select between intel syntax mode and <font SIZE="-1">AT&amp;T</font> syntax mode.</p>
<dt>&quot;amd64&quot;</p>
<dd>
<dt>&quot;intel64&quot;</p>
<dd> Select between <font SIZE="-1">AMD64 ISA</font> and Intel64 <font SIZE="-1">ISA.</font></p>
<dt>&quot;intel-mnemonic&quot;</p>
<dd>
<dt>&quot;att-mnemonic&quot;</p>
<dd> Select between intel mnemonic mode and <font SIZE="-1">AT&amp;T</font> mnemonic mode. Note: <tt>&quot;intel-mnemonic&quot;</tt> implies <tt>&quot;intel&quot;</tt> and <tt>&quot;att-mnemonic&quot;</tt> implies <tt>&quot;att&quot;</tt>.</p>
<dt>&quot;addr64&quot;</p>
<dd>
<dt>&quot;addr32&quot;</p>
<dd>
<dt>&quot;addr16&quot;</p>
<dd>
<dt>&quot;data32&quot;</p>
<dd>
<dt>&quot;data16&quot;</p>
<dd> Specify the default address size and operand size. These five options will be overridden if <tt>&quot;x86-64&quot;</tt>, <tt>&quot;i386&quot;</tt> or <tt>&quot;i8086&quot;</tt> appear later in the option string.</p>
<dt>&quot;suffix&quot;</p>
<dd> When in <font SIZE="-1">AT&amp;T</font> mode and also for a limited set of instructions when in Intel mode, instructs the disassembler to print a mnemonic suffix even when the suffix could be inferred by the operands or, for certain instructions, the execution mode&#8217;s defaults.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For PowerPC, the <code>-M</code> argument <code>raw</code> selects disasssembly of hardware insns rather than aliases. For example, you will see <tt>&quot;rlwinm&quot;</tt> rather than <tt>&quot;clrlwi&quot;</tt>, and <tt>&quot;addi&quot;</tt> rather than <tt>&quot;li&quot;</tt>. All of the <code>-m</code> arguments for <code>gas</code> that select a <font SIZE="-1">CPU</font> are supported. These are: <code>403</code>, <code>405</code>, <code>440</code>, <code>464</code>, <code>476</code>, <code>601</code>, <code>603</code>, <code>604</code>, <code>620</code>, <code>7400</code>, <code>7410</code>, <code>7450</code>, <code>7455</code>, <code>750cl</code>, <code>821</code>, <code>850</code>, <code>860</code>, <code>a2</code>, <code>booke</code>, <code>booke32</code>, <code>cell</code>, <code>com</code>, <code>e200z4</code>, <code>e300</code>, <code>e500</code>, <code>e500mc</code>, <code>e500mc64</code>, <code>e500x2</code>, <code>e5500</code>, <code>e6500</code>, <code>efs</code>, <code>power4</code>, <code>power5</code>, <code>power6</code>, <code>power7</code>, <code>power8</code>, <code>power9</code>, <code>power10</code>, <code>ppc</code>, <code>ppc32</code>, <code>ppc64</code>, <code>ppc64bridge</code>, <code>ppcps</code>, <code>pwr</code>, <code>pwr2</code>, <code>pwr4</code>, <code>pwr5</code>, <code>pwr5x</code>, <code>pwr6</code>, <code>pwr7</code>, <code>pwr8</code>, <code>pwr9</code>, <code>pwr10</code>, <code>pwrx</code>, <code>titan</code>, and <code>vle</code>. <code>32</code> and <code>64</code> modify the default or a prior <font SIZE="-1">CPU</font> selection, disabling and enabling 64-bit insns respectively. In addition, <code>altivec</code>, <code>any</code>, <code>htm</code>, <code>vsx</code>, and <code>spe</code> add capabilities to a previous <i>or later</i> <font SIZE="-1">CPU</font> selection. <code>any</code> will disassemble any opcode known to binutils, but in cases where an opcode has two different meanings or different arguments, you may not see the disassembly you expect. If you disassemble without giving a <font SIZE="-1">CPU</font> selection, a default will be chosen from information gleaned by <font SIZE="-1">BFD</font> from the object files headers, but the result again may not be as you expect. </p>
<p> For <font SIZE="-1">MIPS,</font> this option controls the printing of instruction mnemonic names and register names in disassembled instructions. Multiple selections from the following may be specified as a comma separated string, and invalid options are ignored:</p>
<dl>
<dt>&quot;no-aliases&quot;</p>
<dd> Print the &#8216;raw&#8217; instruction mnemonic instead of some pseudo instruction mnemonic. I.e., print &#8216;daddu&#8217; or &#8216;or&#8217; instead of &#8216;move&#8217;, &#8216;sll&#8217; instead of &#8216;nop&#8217;, etc.</p>
<dt>&quot;msa&quot;</p>
<dd> Disassemble <font SIZE="-1">MSA</font> instructions.</p>
<dt>&quot;virt&quot;</p>
<dd> Disassemble the virtualization <font SIZE="-1">ASE</font> instructions.</p>
<dt>&quot;xpa&quot;</p>
<dd> Disassemble the eXtended Physical Address (<font SIZE="-1">XPA</font>) <font SIZE="-1">ASE</font> instructions.</p>
<dt>&quot;gpr-names=<i>ABI</i>&quot;</p>
<dd> Print <font SIZE="-1">GPR</font> (general-purpose register) names as appropriate for the specified <font SIZE="-1">ABI.</font> By default, <font SIZE="-1">GPR</font> names are selected according to the <font SIZE="-1">ABI</font> of the binary being disassembled.</p>
<dt>&quot;fpr-names=<i>ABI</i>&quot;</p>
<dd> Print <font SIZE="-1">FPR</font> (floating-point register) names as appropriate for the specified <font SIZE="-1">ABI.</font> By default, <font SIZE="-1">FPR</font> numbers are printed rather than names.</p>
<dt>&quot;cp0-names=<i>ARCH</i>&quot;</p>
<dd> Print <font SIZE="-1">CP0</font> (system control coprocessor; coprocessor 0) register names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">CP0</font> register names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</p>
<dt>&quot;hwr-names=<i>ARCH</i>&quot;</p>
<dd> Print <font SIZE="-1">HWR</font> (hardware register, used by the <tt>&quot;rdhwr&quot;</tt> instruction) names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">HWR</font> names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</p>
<dt>&quot;reg-names=<i>ABI</i>&quot;</p>
<dd> Print <font SIZE="-1">GPR</font> and <font SIZE="-1">FPR</font> names as appropriate for the selected <font SIZE="-1">ABI.</font></p>
<dt>&quot;reg-names=<i>ARCH</i>&quot;</p>
<dd> Print CPU-specific register names (<font SIZE="-1">CP0</font> register and <font SIZE="-1">HWR</font> names) as appropriate for the selected <font SIZE="-1">CPU</font> or architecture.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For any of the options listed above, <i></i><font SIZE="-1"><i>ABI</i></font><i></i> or <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> may be specified as <code>numeric</code> to have numbers printed rather than names, for the selected types of registers. You can list the available values of <i></i><font SIZE="-1"><i>ABI</i></font><i></i> and <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> using the <code>&#8211;help</code> option. </p>
<p> For <font SIZE="-1">VAX,</font> you can specify function entry addresses with <code>-M entry:0xf00ba</code>. You can use this multiple times to properly disassemble <font SIZE="-1">VAX</font> binary files that don&#8217;t contain symbol tables (like <font SIZE="-1">ROM</font> dumps). In these cases, the function entry mask would otherwise be decoded as <font SIZE="-1">VAX</font> instructions, which would probably lead the rest of the function being wrongly disassembled.</dl>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;private-headers</code></p>
<dd> Print information that is specific to the object file format. The exact information printed depends upon the object file format. For some object file formats, no additional information is printed.</p>
<dt><code>-P</code> <i>options</i></p>
<dd>
<dt><code>&#8211;private=</code><i>options</i></p>
<dd> Print information that is specific to the object file format. The argument <i>options</i> is a comma separated list that depends on the format (the lists of options is displayed with the help). </p>
<p> For <font SIZE="-1">XCOFF,</font> the available options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;header&quot;</p>
<dd>
<dt>&quot;aout&quot;</p>
<dd>
<dt>&quot;sections&quot;</p>
<dd>
<dt>&quot;syms&quot;</p>
<dd>
<dt>&quot;relocs&quot;</p>
<dd>
<dt>&quot;lineno,&quot;</p>
<dd>
<dt>&quot;loader&quot;</p>
<dd>
<dt>&quot;except&quot;</p>
<dd>
<dt>&quot;typchk&quot;</p>
<dd>
<dt>&quot;traceback&quot;</p>
<dd>
<dt>&quot;toc&quot;</p>
<dd>
<dt>&quot;ldinfo&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Not all object formats support this option. In particular the <font SIZE="-1">ELF</font> format does not use it.</dl>
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
<dt><code>&#8211;source-comment[=</code><i>txt</i><code>]</code></p>
<dd> Like the <code>-S</code> option, but all source code lines are displayed with a prefix of <i>txt</i>. Typically <i>txt</i> will be a comment string which can be used to distinguish the assembler code from the source code. If <i>txt</i> is not provided then a default string of <i>&#8220;# &#8221;</i> (hash followed by a space), will be used.</p>
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
<dt><code>&#8211;visualize-jumps[=color|=extended-color|=off]</code></p>
<dd> Visualize jumps that stay inside a function by drawing <font SIZE="-1">ASCII</font> art between the start and target addresses. The optional <code>=color</code> argument adds color to the output using simple terminal colors. Alternatively the <code>=extended-color</code> argument will add color using 8bit colors, but these might not work on all terminals. </p>
<p> If it is necessary to disable the <code>visualize-jumps</code> option after it has previously been enabled then use <code>visualize-jumps=off</code>.</p>
<dt><code>-W[lLiaprmfFsoORtUuTgAckK]</code></p>
<dd>
<dt><code>&#8211;dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=str-offsets,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index,=addr,=cu_index,=links,=follow-links]</code></p>
<dd> Displays the contents of the <font SIZE="-1">DWARF</font> debug sections in the file, if any are present. Compressed debug sections are automatically decompressed (temporarily) before they are displayed. If one or more of the optional letters or words follows the switch then only those type(s) of data will be dumped. The letters and words refer to the following information:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;a&quot;</p>
<dd>
<dt>&quot;=abbrev&quot;</p>
<dd> Displays the contents of the <code>.debug_abbrev</code> section.</p>
<dt>&quot;A&quot;</p>
<dd>
<dt>&quot;=addr&quot;</p>
<dd> Displays the contents of the <code>.debug_addr</code> section.</p>
<dt>&quot;c&quot;</p>
<dd>
<dt>&quot;=cu_index&quot;</p>
<dd> Displays the contents of the <code>.debug_cu_index</code> and/or <code>.debug_tu_index</code> sections.</p>
<dt>&quot;f&quot;</p>
<dd>
<dt>&quot;=frames&quot;</p>
<dd> Display the raw contents of a <code>.debug_frame</code> section.</p>
<dt>&quot;F&quot;</p>
<dd>
<dt>&quot;=frames-interp&quot;</p>
<dd> Display the interpreted contents of a <code>.debug_frame</code> section.</p>
<dt>&quot;g&quot;</p>
<dd>
<dt>&quot;=gdb_index&quot;</p>
<dd> Displays the contents of the <code>.gdb_index</code> and/or <code>.debug_names</code> sections.</p>
<dt>&quot;i&quot;</p>
<dd>
<dt>&quot;=info&quot;</p>
<dd> Displays the contents of the <code>.debug_info</code> section. Note: the output from this option can also be restricted by the use of the <code>&#8211;dwarf-depth</code> and <code>&#8211;dwarf-start</code> options.</p>
<dt>&quot;k&quot;</p>
<dd>
<dt>&quot;=links&quot;</p>
<dd> Displays the contents of the <code>.gnu_debuglink</code>, <code>.gnu_debugaltlink</code> and <code>.debug_sup</code> sections, if any of them are present. Also displays any links to separate dwarf object files (dwo), if they are specified by the DW_AT_GNU_dwo_name or DW_AT_dwo_name attributes in the <code>.debug_info</code> section.</p>
<dt>&quot;K&quot;</p>
<dd>
<dt>&quot;=follow-links&quot;</p>
<dd> Display the contents of any selected debug sections that are found in linked, separate debug info file(s). This can result in multiple versions of the same debug section being displayed if it exists in more than one file. </p>
<p> In addition, when displaying <font SIZE="-1">DWARF</font> attributes, if a form is found that references the separate debug info file, then the referenced contents will also be displayed. </p>
<p> Note &#8211; in some distributions this option is enabled by default. It can be disabled via the <code>N</code> debug option. The default can be chosen when configuring the binutils via the <code>&#8211;enable-follow-debug-links=yes</code> or <code>&#8211;enable-follow-debug-links=no</code> options. If these are not used then the default is to enable the following of debug links.</p>
<dt>&quot;N&quot;</p>
<dd>
<dt>&quot;=no-follow-links&quot;</p>
<dd> Disables the following of links to separate debug info files.</p>
<dt>&quot;l&quot;</p>
<dd>
<dt>&quot;=rawline&quot;</p>
<dd> Displays the contents of the <code>.debug_line</code> section in a raw format.</p>
<dt>&quot;L&quot;</p>
<dd>
<dt>&quot;=decodedline&quot;</p>
<dd> Displays the interpreted contents of the <code>.debug_line</code> section.</p>
<dt>&quot;m&quot;</p>
<dd>
<dt>&quot;=macro&quot;</p>
<dd> Displays the contents of the <code>.debug_macro</code> and/or <code>.debug_macinfo</code> sections.</p>
<dt>&quot;o&quot;</p>
<dd>
<dt>&quot;=loc&quot;</p>
<dd> Displays the contents of the <code>.debug_loc</code> and/or <code>.debug_loclists</code> sections.</p>
<dt>&quot;O&quot;</p>
<dd>
<dt>&quot;=str-offsets&quot;</p>
<dd> Displays the contents of the <code>.debug_str_offsets</code> section.</p>
<dt>&quot;p&quot;</p>
<dd>
<dt>&quot;=pubnames&quot;</p>
<dd> Displays the contents of the <code>.debug_pubnames</code> and/or <code>.debug_gnu_pubnames</code> sections.</p>
<dt>&quot;r&quot;</p>
<dd>
<dt>&quot;=aranges&quot;</p>
<dd> Displays the contents of the <code>.debug_aranges</code> section.</p>
<dt>&quot;R&quot;</p>
<dd>
<dt>&quot;=Ranges&quot;</p>
<dd> Displays the contents of the <code>.debug_ranges</code> and/or <code>.debug_rnglists</code> sections.</p>
<dt>&quot;s&quot;</p>
<dd>
<dt>&quot;=str&quot;</p>
<dd> Displays the contents of the <code>.debug_str</code>, <code>.debug_line_str</code> and/or <code>.debug_str_offsets</code> sections.</p>
<dt>&quot;t&quot;</p>
<dd>
<dt>&quot;=pubtype&quot;</p>
<dd> Displays the contents of the <code>.debug_pubtypes</code> and/or <code>.debug_gnu_pubtypes</code> sections.</p>
<dt>&quot;T&quot;</p>
<dd>
<dt>&quot;=trace_aranges&quot;</p>
<dd> Displays the contents of the <code>.trace_aranges</code> section.</p>
<dt>&quot;u&quot;</p>
<dd>
<dt>&quot;=trace_abbrev&quot;</p>
<dd> Displays the contents of the <code>.trace_abbrev</code> section.</p>
<dt>&quot;U&quot;</p>
<dd>
<dt>&quot;=trace_info&quot;</p>
<dd> Displays the contents of the <code>.trace_info</code> section.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note: displaying the contents of <code>.debug_static_funcs</code>, <code>.debug_static_vars</code> and <code>debug_weaknames</code> sections is not currently supported.</dl>
<dt><code>&#8211;dwarf-depth=</code><i>n</i></p>
<dd> Limit the dump of the <tt>&quot;.debug_info&quot;</tt> section to <i>n</i> children. This is only useful with <code>&#8211;debug-dump=info</code>. The default is to print all DIEs; the special value 0 for <i>n</i> will also have this effect. </p>
<p> With a non-zero value for <i>n</i>, DIEs at or deeper than <i>n</i> levels will not be printed. The range for <i>n</i> is zero-based.</p>
<dt><code>&#8211;dwarf-start=</code><i>n</i></p>
<dd> Print only DIEs beginning with the <font SIZE="-1">DIE</font> numbered <i>n</i>. This is only useful with <code>&#8211;debug-dump=info</code>. </p>
<p> If specified, this option will suppress printing of any header information and all DIEs before the <font SIZE="-1">DIE</font> numbered <i>n</i>. Only siblings and children of the specified <font SIZE="-1">DIE</font> will be printed. </p>
<p> This can be used in conjunction with <code>&#8211;dwarf-depth</code>.</p>
<dt><code>&#8211;dwarf-check</code></p>
<dd> Enable additional checks for consistency of Dwarf information.</p>
<dt><code>&#8211;ctf[=</code><i>section</i><code>]</code></p>
<dd> Display the contents of the specified <font SIZE="-1">CTF</font> section. <font SIZE="-1">CTF</font> sections themselves contain many subsections, all of which are displayed in order. </p>
<p> By default, display the name of the section named <i>.ctf</i>, which is the name emitted by <code>ld</code>.</p>
<dt><code>&#8211;ctf-parent=</code><i>member</i></p>
<dd> If the <font SIZE="-1">CTF</font> section contains ambiguously-defined types, it will consist of an archive of many <font SIZE="-1">CTF</font> dictionaries, all inheriting from one dictionary containing unambiguous types. This member is by default named <i>.ctf</i>, like the section containing it, but it is possible to change this name using the <tt>&quot;ctf_link_set_memb_name_changer&quot;</tt> function at link time. When looking at <font SIZE="-1">CTF</font> archives that have been created by a linker that uses the name changer to rename the parent archive member, <code>&#8211;ctf-parent</code> can be used to specify the name used for the parent.</p>
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
<p> where the number inside the square brackets is the number of the entry in the symbol table, the <i>sec</i> number is the section number, the <i>fl</i> value are the symbol&#8217;s flag bits, the <i>ty</i> number is the symbol&#8217;s type, the <i>scl</i> number is the symbol&#8217;s storage class and the <i>nx</i> value is the number of auxiliary entries associated with the symbol. The last two fields are the symbol&#8217;s value and its name. </p>
<p> The other common output format, usually seen with <font SIZE="-1">ELF</font> based files, looks like this: </p>
<pre>
        00000000 l    d  .bss   00000000 .bss
        00000000 g       .text  00000000 fred
</pre>
<p> Here the first number is the symbol&#8217;s value (sometimes referred to as its address). The next field is actually a set of characters and spaces indicating the flag bits that are set on the symbol. These characters are described below. Next is the section with which the symbol is associated or <i>*ABS*</i> if the section is absolute (ie not connected with any section), or <i>*UND*</i> if the section is referenced in the file being dumped, but not defined there. </p>
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
<dd> Print the dynamic symbol table entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. This is similar to the information provided by the <code>nm</code> program when given the <code>-D</code> (<code>&#8211;dynamic</code>) option. </p>
<p> The output format is similar to that produced by the <code>&#8211;syms</code> option, except that an extra field is inserted before the symbol&#8217;s name, giving the version information associated with the symbol. If the version is the default version to be used when resolving unversioned references to the symbol then it&#8217;s displayed as is, otherwise it&#8217;s put into parentheses.</p>
<dt><code>&#8211;special-syms</code></p>
<dd> When displaying symbols include those which the target considers to be special in some way and which would not normally be of interest to the user.</p>
<dt><code>-U</code> <i>[d|i|l|e|x|h]</i></p>
<dd>
<dt><code>&#8211;unicode=</code><i>[default|invalid|locale|escape|hex|highlight]</i></p>
<dd> Controls the display of <font SIZE="-1">UTF-8</font> encoded multibyte characters in strings. The default (<code>&#8211;unicode=default</code>) is to give them no special treatment. The <code>&#8211;unicode=locale</code> option displays the sequence in the current locale, which may or may not support them. The options <code>&#8211;unicode=hex</code> and <code>&#8211;unicode=invalid</code> display them as hex byte sequences enclosed by either angle brackets or curly braces. </p>
<p> The <code>&#8211;unicode=escape</code> option displays them as escape sequences (<i>
