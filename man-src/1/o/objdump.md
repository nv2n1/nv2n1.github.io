---

title: "objdump(1)"
name: "objdump"
section: "1"
letter: "o"
url: "/docs/linux/man/1-objdump/"
description: "objdump – display information from object files"
---

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
<p> <code>objdump</code> displays information about one or more object files. The options control what particular information to display. This information is mostly useful to programmers who are working on the compilation tools, as opposed to programmers who just want their program to compile and work. </p>
<p> <i>objfile</i>&#8230; are the object files to be examined. When you specify archives, <code>objdump</code> shows information on each of the member object files.</p>
<h2>OPTIONS</h2>
<p> The long and short forms of options, shown here as alternatives, are equivalent. At least one option from the list <code>-a,-d,-D,-e,-f,-g,-G,-h,-H,-p,-P,-r,-R,-s,-S,-t,-T,-V,-x</code> must be given.</p>
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
<dt><code>&#8211;recurse-limit</code></dt>
<dd>
</dd><dt><code>&#8211;no-recurse-limit</code></dt>
<dd>
</dd><dt><code>&#8211;recursion-limit</code></dt>
<dd>
</dd><dt><code>&#8211;no-recursion-limit</code></dt>
<dd> Enables or disables a limit on the amount of recursion performed whilst demangling strings. Since the name mangling formats allow for an infinite level of recursion it is possible to create strings whose decoding will exhaust the amount of stack space available on the host machine, triggering a memory fault. The limit tries to prevent this from happening by restricting recursion to 2048 levels of nesting. </dd>
<p> The default is for this limit to be enabled, but disabling it may be necessary in order to demangle truly complicated names. Note however that if the recursion limit is disabled then stack exhaustion is possible and any bug reports about such an event will be rejected.</p>
<dt><code>-g</code></dt>
<dd>
</dd><dt><code>&#8211;debugging</code></dt>
<dd> Display debugging information. This attempts to parse <font SIZE="-1">STABS</font> debugging format information stored in the file and print it out using a C like syntax. If no <font SIZE="-1">STABS</font> debugging was found this option falls back on the <code>-W</code> option to print any <font SIZE="-1">DWARF</font> information in the file.</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>&#8211;debugging-tags</code></dt>
<dd> Like <code>-g</code>, but the information is generated in a format compatible with ctags tool.</dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble=</code><i>symbol</i></dt>
<dd> Display the assembler mnemonics for the machine instructions from the input file. This option only disassembles those sections which are expected to contain instructions. If the optional <i>symbol</i> argument is given, then display the assembler mnemonics starting at <i>symbol</i>. If <i>symbol</i> is a function name then disassembly will stop at the end of the function, otherwise it will stop when the next symbol is encountered. If there are no matches for <i>symbol</i> then nothing will be displayed. </dd>
<p> Note if the <code>&#8211;dwarf=follow-links</code> option is enabled then any symbol tables in linked debug info files will be read in and used when disassembling.</p>
<dt><code>-D</code></dt>
<dd>
</dd><dt><code>&#8211;disassemble-all</code></dt>
<dd> Like <code>-d</code>, but disassemble the contents of all sections, not just those expected to contain instructions. </dd>
<p> This option also has a subtle effect on the disassembly of instructions in code sections. When option <code>-d</code> is in effect objdump will assume that any symbols present in a code section occur on the boundary between instructions and it will refuse to disassemble across such a boundary. When option <code>-D</code> is in effect however this assumption is supressed. This means that it is possible for the output of <code>-d</code> and <code>-D</code> to differ if, for example, data is stored in code sections. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture this switch also has the effect of forcing the disassembler to decode pieces of data found in code sections as if they were instructions. </p>
<p> Note if the <code>&#8211;dwarf=follow-links</code> option is enabled then any symbol tables in linked debug info files will be read in and used when disassembling.</p>
<dt><code>&#8211;no-addresses</code></dt>
<dd> When disassembling, don&#8217;t print addresses on each line or for symbols and relocation offsets. In combination with <code>&#8211;no-show-raw-insn</code> this may be useful for comparing compiler output.</dd>
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
<dt><code>-F</code></dt>
<dd>
</dd><dt><code>&#8211;file-offsets</code></dt>
<dd> When disassembling sections, whenever a symbol is displayed, also display the file offset of the region of data that is about to be dumped. If zeroes are being skipped, then when disassembly resumes, tell the user how many zeroes were skipped and the file offset of the location from where the disassembly resumes. When dumping sections, display the file offset of the location from where the dump starts.</dd>
<dt><code>&#8211;file-start-context</code></dt>
<dd> Specify that when displaying interlisted source code/disassembly (assumes <code>-S</code>) from a file that has not yet been displayed, extend the context to the start of the file.</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;section-headers</code></dt>
<dd>
</dd><dt><code>&#8211;headers</code></dt>
<dd> Display summary information from the section headers of the object file. </dd>
<p> File segments may be relocated to nonstandard addresses, for example by using the <code>-Ttext</code>, <code>-Tdata</code>, or <code>-Tbss</code> options to <code>ld</code>. However, some object file formats, such as a.out, do not store the starting address of the file segments. In those situations, although <code>ld</code> relocates the sections correctly, using <code>objdump -h</code> to list the file section headers cannot show the correct addresses. Instead, it shows the usual addresses, which are implicit for the target. </p>
<p> Note, in some cases it is possible for a section to have both the <font SIZE="-1">READONLY</font> and the <font SIZE="-1">NOREAD</font> attributes set. In such cases the <font SIZE="-1">NOREAD</font> attribute takes precedence, but <code>objdump</code> will report both since the exact setting of the flag bits might be important.</p>
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
<dt><code>-L</code></dt>
<dd>
</dd><dt><code>&#8211;process-links</code></dt>
<dd> Display the contents of non-debug sections found in separate debuginfo files that are linked to the main file. This option automatically implies the <code>-WK</code> option, and only sections requested by other command line options will be displayed.</dd>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>&#8211;line-numbers</code></dt>
<dd> Label the display (using debugging information) with the filename and source line numbers corresponding to the object code or relocs shown. Only useful with <code>-d</code>, <code>-D</code>, or <code>-r</code>.</dd>
<dt><code>-m</code> <i>machine</i></dt>
<dd>
</dd><dt><code>&#8211;architecture=</code><i>machine</i></dt>
<dd> Specify the architecture to use when disassembling object files. This can be useful when disassembling object files which do not describe architecture information, such as S-records. You can list the available architectures with the <code>-i</code> option. </dd>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch has an additional effect. It restricts the disassembly to only those instructions supported by the architecture specified by <i>machine</i>. If it is necessary to use this switch because the input file does not contain any architecture information, but it is also desired to disassemble all the instructions use <code>-marm</code>.</p>
<dt><code>-M</code> <i>options</i></dt>
<dd>
</dd><dt><code>&#8211;disassembler-options=</code><i>options</i></dt>
<dd> Pass target specific information to the disassembler. Only supported on some targets. If it is necessary to specify more than one disassembler option then multiple <code>-M</code> options can be used or can be placed together into a comma separated list. </dd>
<p> For <font SIZE="-1">ARC,</font> <code>dsp</code> controls the printing of <font SIZE="-1">DSP</font> instructions, <code>spfp</code> selects the printing of <font SIZE="-1">FPX</font> single precision <font SIZE="-1">FP</font> instructions, <code>dpfp</code> selects the printing of <font SIZE="-1">FPX</font> double precision <font SIZE="-1">FP</font> instructions, <code>quarkse_em</code> selects the printing of special QuarkSE-EM instructions, <code>fpuda</code> selects the printing of double precision assist instructions, <code>fpus</code> selects the printing of <font SIZE="-1">FPU</font> single precision <font SIZE="-1">FP</font> instructions, while <code>fpud</code> selects the printing of <font SIZE="-1">FPU</font> double precision <font SIZE="-1">FP</font> instructions. Additionally, one can choose to have all the immediates printed in hexadecimal using <code>hex</code>. By default, the short immediates are printed using the decimal representation, while the long immediate values are printed as hexadecimal. </p>
<p> <code>cpu=&#8230;</code> allows one to enforce a particular <font SIZE="-1">ISA</font> when disassembling instructions, overriding the <code>-m</code> value or whatever is in the <font SIZE="-1">ELF</font> file. This might be useful to select <font SIZE="-1">ARC EM</font> or <font SIZE="-1">HS ISA,</font> because architecture is same for those and disassembler relies on private <font SIZE="-1">ELF</font> header data to decide if code is for <font SIZE="-1">EM</font> or <font SIZE="-1">HS.</font> This option might be specified multiple times &#8211; only the latest value will be used. Valid values are same as for the assembler <code>-mcpu=&#8230;</code> option. </p>
<p> If the target is an <font SIZE="-1">ARM</font> architecture then this switch can be used to select which register name set is used during disassembler. Specifying <code>-M reg-names-std</code> (the default) will select the register names as used in <font SIZE="-1">ARM</font>&#8216;s instruction set documentation, but with register 13 called &#8216;sp&#8217;, register 14 called &#8216;lr&#8217; and register 15 called &#8216;pc&#8217;. Specifying <code>-M reg-names-apcs</code> will select the name set used by the <font SIZE="-1">ARM</font> Procedure Call Standard, whilst specifying <code>-M reg-names-raw</code> will just use <code>r</code> followed by the register number. </p>
<p> There are also two variants on the <font SIZE="-1">APCS</font> register naming scheme enabled by <code>-M reg-names-atpcs</code> and <code>-M reg-names-special-atpcs</code> which use the ARM/Thumb Procedure Call Standard naming conventions. (Either with the normal register names or the special register names). </p>
<p> This option can also be used for <font SIZE="-1">ARM</font> architectures to force the disassembler to interpret all instructions as Thumb instructions by using the switch <code>&#8211;disassembler-options=force-thumb</code>. This can be useful when attempting to disassemble thumb code produced by other compilers. </p>
<p> For AArch64 targets this switch can be used to set whether instructions are disassembled as the most general instruction using the <code>-M no-aliases</code> option or whether instruction notes should be generated as comments in the disasssembly using <code>-M notes</code>. </p>
<p> For the x86, some of the options duplicate functions of the <code>-m</code> switch, but allow finer grained control.</p>
<dl>
<dl>
<dt>&quot;x86-64&quot;</dt>
<dd>
</dd><dt>&quot;i386&quot;</dt>
<dd>
</dd><dt>&quot;i8086&quot;</dt>
<dd> Select disassembly for the given architecture.</dd>
<dt>&quot;intel&quot;</dt>
<dd>
</dd><dt>&quot;att&quot;</dt>
<dd> Select between intel syntax mode and <font SIZE="-1">AT&amp;T</font> syntax mode.</dd>
<dt>&quot;amd64&quot;</dt>
<dd>
</dd><dt>&quot;intel64&quot;</dt>
<dd> Select between <font SIZE="-1">AMD64 ISA</font> and Intel64 <font SIZE="-1">ISA.</font></dd>
<dt>&quot;intel-mnemonic&quot;</dt>
<dd>
</dd><dt>&quot;att-mnemonic&quot;</dt>
<dd> Select between intel mnemonic mode and <font SIZE="-1">AT&amp;T</font> mnemonic mode. Note: <tt>&quot;intel-mnemonic&quot;</tt> implies <tt>&quot;intel&quot;</tt> and <tt>&quot;att-mnemonic&quot;</tt> implies <tt>&quot;att&quot;</tt>.</dd>
<dt>&quot;addr64&quot;</dt>
<dd>
</dd><dt>&quot;addr32&quot;</dt>
<dd>
</dd><dt>&quot;addr16&quot;</dt>
<dd>
</dd><dt>&quot;data32&quot;</dt>
<dd>
</dd><dt>&quot;data16&quot;</dt>
<dd> Specify the default address size and operand size. These five options will be overridden if <tt>&quot;x86-64&quot;</tt>, <tt>&quot;i386&quot;</tt> or <tt>&quot;i8086&quot;</tt> appear later in the option string.</dd>
<dt>&quot;suffix&quot;</dt>
<dd> When in <font SIZE="-1">AT&amp;T</font> mode and also for a limited set of instructions when in Intel mode, instructs the disassembler to print a mnemonic suffix even when the suffix could be inferred by the operands or, for certain instructions, the execution mode&#8217;s defaults.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For PowerPC, the <code>-M</code> argument <code>raw</code> selects disasssembly of hardware insns rather than aliases. For example, you will see <tt>&quot;rlwinm&quot;</tt> rather than <tt>&quot;clrlwi&quot;</tt>, and <tt>&quot;addi&quot;</tt> rather than <tt>&quot;li&quot;</tt>. All of the <code>-m</code> arguments for <code>gas</code> that select a <font SIZE="-1">CPU</font> are supported. These are: <code>403</code>, <code>405</code>, <code>440</code>, <code>464</code>, <code>476</code>, <code>601</code>, <code>603</code>, <code>604</code>, <code>620</code>, <code>7400</code>, <code>7410</code>, <code>7450</code>, <code>7455</code>, <code>750cl</code>, <code>821</code>, <code>850</code>, <code>860</code>, <code>a2</code>, <code>booke</code>, <code>booke32</code>, <code>cell</code>, <code>com</code>, <code>e200z4</code>, <code>e300</code>, <code>e500</code>, <code>e500mc</code>, <code>e500mc64</code>, <code>e500x2</code>, <code>e5500</code>, <code>e6500</code>, <code>efs</code>, <code>power4</code>, <code>power5</code>, <code>power6</code>, <code>power7</code>, <code>power8</code>, <code>power9</code>, <code>power10</code>, <code>ppc</code>, <code>ppc32</code>, <code>ppc64</code>, <code>ppc64bridge</code>, <code>ppcps</code>, <code>pwr</code>, <code>pwr2</code>, <code>pwr4</code>, <code>pwr5</code>, <code>pwr5x</code>, <code>pwr6</code>, <code>pwr7</code>, <code>pwr8</code>, <code>pwr9</code>, <code>pwr10</code>, <code>pwrx</code>, <code>titan</code>, and <code>vle</code>. <code>32</code> and <code>64</code> modify the default or a prior <font SIZE="-1">CPU</font> selection, disabling and enabling 64-bit insns respectively. In addition, <code>altivec</code>, <code>any</code>, <code>htm</code>, <code>vsx</code>, and <code>spe</code> add capabilities to a previous <i>or later</i> <font SIZE="-1">CPU</font> selection. <code>any</code> will disassemble any opcode known to binutils, but in cases where an opcode has two different meanings or different arguments, you may not see the disassembly you expect. If you disassemble without giving a <font SIZE="-1">CPU</font> selection, a default will be chosen from information gleaned by <font SIZE="-1">BFD</font> from the object files headers, but the result again may not be as you expect. </p>
<p> For <font SIZE="-1">MIPS,</font> this option controls the printing of instruction mnemonic names and register names in disassembled instructions. Multiple selections from the following may be specified as a comma separated string, and invalid options are ignored:</p>
</dd><dl>
<dt>&quot;no-aliases&quot;</dt>
<dd> Print the &#8216;raw&#8217; instruction mnemonic instead of some pseudo instruction mnemonic. I.e., print &#8216;daddu&#8217; or &#8216;or&#8217; instead of &#8216;move&#8217;, &#8216;sll&#8217; instead of &#8216;nop&#8217;, etc.</dd>
<dt>&quot;msa&quot;</dt>
<dd> Disassemble <font SIZE="-1">MSA</font> instructions.</dd>
<dt>&quot;virt&quot;</dt>
<dd> Disassemble the virtualization <font SIZE="-1">ASE</font> instructions.</dd>
<dt>&quot;xpa&quot;</dt>
<dd> Disassemble the eXtended Physical Address (<font SIZE="-1">XPA</font>) <font SIZE="-1">ASE</font> instructions.</dd>
<dt>&quot;gpr-names=<i>ABI</i>&quot;</dt>
<dd> Print <font SIZE="-1">GPR</font> (general-purpose register) names as appropriate for the specified <font SIZE="-1">ABI.</font> By default, <font SIZE="-1">GPR</font> names are selected according to the <font SIZE="-1">ABI</font> of the binary being disassembled.</dd>
<dt>&quot;fpr-names=<i>ABI</i>&quot;</dt>
<dd> Print <font SIZE="-1">FPR</font> (floating-point register) names as appropriate for the specified <font SIZE="-1">ABI.</font> By default, <font SIZE="-1">FPR</font> numbers are printed rather than names.</dd>
<dt>&quot;cp0-names=<i>ARCH</i>&quot;</dt>
<dd> Print <font SIZE="-1">CP0</font> (system control coprocessor; coprocessor 0) register names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">CP0</font> register names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</dd>
<dt>&quot;hwr-names=<i>ARCH</i>&quot;</dt>
<dd> Print <font SIZE="-1">HWR</font> (hardware register, used by the <tt>&quot;rdhwr&quot;</tt> instruction) names as appropriate for the <font SIZE="-1">CPU</font> or architecture specified by <i></i><font SIZE="-1"><i>ARCH</i></font><i></i>. By default, <font SIZE="-1">HWR</font> names are selected according to the architecture and <font SIZE="-1">CPU</font> of the binary being disassembled.</dd>
<dt>&quot;reg-names=<i>ABI</i>&quot;</dt>
<dd> Print <font SIZE="-1">GPR</font> and <font SIZE="-1">FPR</font> names as appropriate for the selected <font SIZE="-1">ABI.</font></dd>
<dt>&quot;reg-names=<i>ARCH</i>&quot;</dt>
<dd> Print CPU-specific register names (<font SIZE="-1">CP0</font> register and <font SIZE="-1">HWR</font> names) as appropriate for the selected <font SIZE="-1">CPU</font> or architecture.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> For any of the options listed above, <i></i><font SIZE="-1"><i>ABI</i></font><i></i> or <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> may be specified as <code>numeric</code> to have numbers printed rather than names, for the selected types of registers. You can list the available values of <i></i><font SIZE="-1"><i>ABI</i></font><i></i> and <i></i><font SIZE="-1"><i>ARCH</i></font><i></i> using the <code>&#8211;help</code> option. </p>
<p> For <font SIZE="-1">VAX,</font> you can specify function entry addresses with <code>-M entry:0xf00ba</code>. You can use this multiple times to properly disassemble <font SIZE="-1">VAX</font> binary files that don&#8217;t contain symbol tables (like <font SIZE="-1">ROM</font> dumps). In these cases, the function entry mask would otherwise be decoded as <font SIZE="-1">VAX</font> instructions, which would probably lead the rest of the function being wrongly disassembled.</dd></dl>
<dt><code>-p</code></dt>
<dd>
</dd><dt><code>&#8211;private-headers</code></dt>
<dd> Print information that is specific to the object file format. The exact information printed depends upon the object file format. For some object file formats, no additional information is printed.</dd>
<dt><code>-P</code> <i>options</i></dt>
<dd>
</dd><dt><code>&#8211;private=</code><i>options</i></dt>
<dd> Print information that is specific to the object file format. The argument <i>options</i> is a comma separated list that depends on the format (the lists of options is displayed with the help). </dd>
<p> For <font SIZE="-1">XCOFF,</font> the available options are:</p>
<dl>
<dl>
<dt>&quot;header&quot;</dt>
<dd>
</dd><dt>&quot;aout&quot;</dt>
<dd>
</dd><dt>&quot;sections&quot;</dt>
<dd>
</dd><dt>&quot;syms&quot;</dt>
<dd>
</dd><dt>&quot;relocs&quot;</dt>
<dd>
</dd><dt>&quot;lineno,&quot;</dt>
<dd>
</dd><dt>&quot;loader&quot;</dt>
<dd>
</dd><dt>&quot;except&quot;</dt>
<dd>
</dd><dt>&quot;typchk&quot;</dt>
<dd>
</dd><dt>&quot;traceback&quot;</dt>
<dd>
</dd><dt>&quot;toc&quot;</dt>
<dd>
</dd><dt>&quot;ldinfo&quot;</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Not all object formats support this option. In particular the <font SIZE="-1">ELF</font> format does not use it.</dd></dl>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;reloc</code></dt>
<dd> Print the relocation entries of the file. If used with <code>-d</code> or <code>-D</code>, the relocations are printed interspersed with the disassembly.</dd>
<dt><code>-R</code></dt>
<dd>
</dd><dt><code>&#8211;dynamic-reloc</code></dt>
<dd> Print the dynamic relocation entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. As for <code>-r</code>, if used with <code>-d</code> or <code>-D</code>, the relocations are printed interspersed with the disassembly.</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;full-contents</code></dt>
<dd> Display the full contents of any sections requested. By default all non-empty sections are displayed.</dd>
<dt><code>-S</code></dt>
<dd>
</dd><dt><code>&#8211;source</code></dt>
<dd> Display source code intermixed with disassembly, if possible. Implies <code>-d</code>.</dd>
<dt><code>&#8211;source-comment[=</code><i>txt</i><code>]</code></dt>
<dd> Like the <code>-S</code> option, but all source code lines are displayed with a prefix of <i>txt</i>. Typically <i>txt</i> will be a comment string which can be used to distinguish the assembler code from the source code. If <i>txt</i> is not provided then a default string of <i>&#8220;# &#8221;</i> (hash followed by a space), will be used.</dd>
<dt><code>&#8211;prefix=</code><i>prefix</i></dt>
<dd> Specify <i>prefix</i> to add to the absolute paths when used with <code>-S</code>.</dd>
<dt><code>&#8211;prefix-strip=</code><i>level</i></dt>
<dd> Indicate how many initial directory names to strip off the hardwired absolute paths. It has no effect without <code>&#8211;prefix=</code><i>prefix</i>.</dd>
<dt><code>&#8211;show-raw-insn</code></dt>
<dd> When disassembling instructions, print the instruction in hex as well as in symbolic form. This is the default except when <code>&#8211;prefix-addresses</code> is used.</dd>
<dt><code>&#8211;no-show-raw-insn</code></dt>
<dd> When disassembling instructions, do not print the instruction bytes. This is the default when <code>&#8211;prefix-addresses</code> is used.</dd>
<dt><code>&#8211;insn-width=</code><i>width</i></dt>
<dd> Display <i>width</i> bytes on a single line when disassembling instructions.</dd>
<dt><code>&#8211;visualize-jumps[=color|=extended-color|=off]</code></dt>
<dd> Visualize jumps that stay inside a function by drawing <font SIZE="-1">ASCII</font> art between the start and target addresses. The optional <code>=color</code> argument adds color to the output using simple terminal colors. Alternatively the <code>=extended-color</code> argument will add color using 8bit colors, but these might not work on all terminals. </dd>
<p> If it is necessary to disable the <code>visualize-jumps</code> option after it has previously been enabled then use <code>visualize-jumps=off</code>.</p>
<dt><code>-W[lLiaprmfFsoORtUuTgAckK]</code></dt>
<dd>
</dd><dt><code>&#8211;dwarf[=rawline,=decodedline,=info,=abbrev,=pubnames,=aranges,=macro,=frames,=frames-interp,=str,=str-offsets,=loc,=Ranges,=pubtypes,=trace_info,=trace_abbrev,=trace_aranges,=gdb_index,=addr,=cu_index,=links,=follow-links]</code></dt>
<dd> Displays the contents of the <font SIZE="-1">DWARF</font> debug sections in the file, if any are present. Compressed debug sections are automatically decompressed (temporarily) before they are displayed. If one or more of the optional letters or words follows the switch then only those type(s) of data will be dumped. The letters and words refer to the following information:</dd>
<dl>
<dl>
<dt>&quot;a&quot;</dt>
<dd>
</dd><dt>&quot;=abbrev&quot;</dt>
<dd> Displays the contents of the <code>.debug_abbrev</code> section.</dd>
<dt>&quot;A&quot;</dt>
<dd>
</dd><dt>&quot;=addr&quot;</dt>
<dd> Displays the contents of the <code>.debug_addr</code> section.</dd>
<dt>&quot;c&quot;</dt>
<dd>
</dd><dt>&quot;=cu_index&quot;</dt>
<dd> Displays the contents of the <code>.debug_cu_index</code> and/or <code>.debug_tu_index</code> sections.</dd>
<dt>&quot;f&quot;</dt>
<dd>
</dd><dt>&quot;=frames&quot;</dt>
<dd> Display the raw contents of a <code>.debug_frame</code> section.</dd>
<dt>&quot;F&quot;</dt>
<dd>
</dd><dt>&quot;=frames-interp&quot;</dt>
<dd> Display the interpreted contents of a <code>.debug_frame</code> section.</dd>
<dt>&quot;g&quot;</dt>
<dd>
</dd><dt>&quot;=gdb_index&quot;</dt>
<dd> Displays the contents of the <code>.gdb_index</code> and/or <code>.debug_names</code> sections.</dd>
<dt>&quot;i&quot;</dt>
<dd>
</dd><dt>&quot;=info&quot;</dt>
<dd> Displays the contents of the <code>.debug_info</code> section. Note: the output from this option can also be restricted by the use of the <code>&#8211;dwarf-depth</code> and <code>&#8211;dwarf-start</code> options.</dd>
<dt>&quot;k&quot;</dt>
<dd>
</dd><dt>&quot;=links&quot;</dt>
<dd> Displays the contents of the <code>.gnu_debuglink</code>, <code>.gnu_debugaltlink</code> and <code>.debug_sup</code> sections, if any of them are present. Also displays any links to separate dwarf object files (dwo), if they are specified by the DW_AT_GNU_dwo_name or DW_AT_dwo_name attributes in the <code>.debug_info</code> section.</dd>
<dt>&quot;K&quot;</dt>
<dd>
</dd><dt>&quot;=follow-links&quot;</dt>
<dd> Display the contents of any selected debug sections that are found in linked, separate debug info file(s). This can result in multiple versions of the same debug section being displayed if it exists in more than one file. </dd>
<p> In addition, when displaying <font SIZE="-1">DWARF</font> attributes, if a form is found that references the separate debug info file, then the referenced contents will also be displayed. </p>
<p> Note &#8211; in some distributions this option is enabled by default. It can be disabled via the <code>N</code> debug option. The default can be chosen when configuring the binutils via the <code>&#8211;enable-follow-debug-links=yes</code> or <code>&#8211;enable-follow-debug-links=no</code> options. If these are not used then the default is to enable the following of debug links.</p>
<dt>&quot;N&quot;</dt>
<dd>
</dd><dt>&quot;=no-follow-links&quot;</dt>
<dd> Disables the following of links to separate debug info files.</dd>
<dt>&quot;l&quot;</dt>
<dd>
</dd><dt>&quot;=rawline&quot;</dt>
<dd> Displays the contents of the <code>.debug_line</code> section in a raw format.</dd>
<dt>&quot;L&quot;</dt>
<dd>
</dd><dt>&quot;=decodedline&quot;</dt>
<dd> Displays the interpreted contents of the <code>.debug_line</code> section.</dd>
<dt>&quot;m&quot;</dt>
<dd>
</dd><dt>&quot;=macro&quot;</dt>
<dd> Displays the contents of the <code>.debug_macro</code> and/or <code>.debug_macinfo</code> sections.</dd>
<dt>&quot;o&quot;</dt>
<dd>
</dd><dt>&quot;=loc&quot;</dt>
<dd> Displays the contents of the <code>.debug_loc</code> and/or <code>.debug_loclists</code> sections.</dd>
<dt>&quot;O&quot;</dt>
<dd>
</dd><dt>&quot;=str-offsets&quot;</dt>
<dd> Displays the contents of the <code>.debug_str_offsets</code> section.</dd>
<dt>&quot;p&quot;</dt>
<dd>
</dd><dt>&quot;=pubnames&quot;</dt>
<dd> Displays the contents of the <code>.debug_pubnames</code> and/or <code>.debug_gnu_pubnames</code> sections.</dd>
<dt>&quot;r&quot;</dt>
<dd>
</dd><dt>&quot;=aranges&quot;</dt>
<dd> Displays the contents of the <code>.debug_aranges</code> section.</dd>
<dt>&quot;R&quot;</dt>
<dd>
</dd><dt>&quot;=Ranges&quot;</dt>
<dd> Displays the contents of the <code>.debug_ranges</code> and/or <code>.debug_rnglists</code> sections.</dd>
<dt>&quot;s&quot;</dt>
<dd>
</dd><dt>&quot;=str&quot;</dt>
<dd> Displays the contents of the <code>.debug_str</code>, <code>.debug_line_str</code> and/or <code>.debug_str_offsets</code> sections.</dd>
<dt>&quot;t&quot;</dt>
<dd>
</dd><dt>&quot;=pubtype&quot;</dt>
<dd> Displays the contents of the <code>.debug_pubtypes</code> and/or <code>.debug_gnu_pubtypes</code> sections.</dd>
<dt>&quot;T&quot;</dt>
<dd>
</dd><dt>&quot;=trace_aranges&quot;</dt>
<dd> Displays the contents of the <code>.trace_aranges</code> section.</dd>
<dt>&quot;u&quot;</dt>
<dd>
</dd><dt>&quot;=trace_abbrev&quot;</dt>
<dd> Displays the contents of the <code>.trace_abbrev</code> section.</dd>
<dt>&quot;U&quot;</dt>
<dd>
</dd><dt>&quot;=trace_info&quot;</dt>
<dd> Displays the contents of the <code>.trace_info</code> section.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Note: displaying the contents of <code>.debug_static_funcs</code>, <code>.debug_static_vars</code> and <code>debug_weaknames</code> sections is not currently supported.</dd></dl>
<dt><code>&#8211;dwarf-depth=</code><i>n</i></dt>
<dd> Limit the dump of the <tt>&quot;.debug_info&quot;</tt> section to <i>n</i> children. This is only useful with <code>&#8211;debug-dump=info</code>. The default is to print all DIEs; the special value 0 for <i>n</i> will also have this effect. </dd>
<p> With a non-zero value for <i>n</i>, DIEs at or deeper than <i>n</i> levels will not be printed. The range for <i>n</i> is zero-based.</p>
<dt><code>&#8211;dwarf-start=</code><i>n</i></dt>
<dd> Print only DIEs beginning with the <font SIZE="-1">DIE</font> numbered <i>n</i>. This is only useful with <code>&#8211;debug-dump=info</code>. </dd>
<p> If specified, this option will suppress printing of any header information and all DIEs before the <font SIZE="-1">DIE</font> numbered <i>n</i>. Only siblings and children of the specified <font SIZE="-1">DIE</font> will be printed. </p>
<p> This can be used in conjunction with <code>&#8211;dwarf-depth</code>.</p>
<dt><code>&#8211;dwarf-check</code></dt>
<dd> Enable additional checks for consistency of Dwarf information.</dd>
<dt><code>&#8211;ctf[=</code><i>section</i><code>]</code></dt>
<dd> Display the contents of the specified <font SIZE="-1">CTF</font> section. <font SIZE="-1">CTF</font> sections themselves contain many subsections, all of which are displayed in order. </dd>
<p> By default, display the name of the section named <i>.ctf</i>, which is the name emitted by <code>ld</code>.</p>
<dt><code>&#8211;ctf-parent=</code><i>member</i></dt>
<dd> If the <font SIZE="-1">CTF</font> section contains ambiguously-defined types, it will consist of an archive of many <font SIZE="-1">CTF</font> dictionaries, all inheriting from one dictionary containing unambiguous types. This member is by default named <i>.ctf</i>, like the section containing it, but it is possible to change this name using the <tt>&quot;ctf_link_set_memb_name_changer&quot;</tt> function at link time. When looking at <font SIZE="-1">CTF</font> archives that have been created by a linker that uses the name changer to rename the parent archive member, <code>&#8211;ctf-parent</code> can be used to specify the name used for the parent.</dd>
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
<dd> Print the symbol table entries of the file. This is similar to the information provided by the <code>nm</code> program, although the display format is different. The format of the output depends upon the format of the file being dumped, but there are two main types. One looks like this: </dd>
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
<dl>
<dt>&quot;l&quot;</dt>
<dd>
</dd><dt>&quot;g&quot;</dt>
<dd>
</dd><dt>&quot;u&quot;</dt>
<dd>
</dd><dt>&quot;!&quot;</dt>
<dd> The symbol is a local (l), global (g), unique global (u), neither global nor local (a space) or both global and local (!). A symbol can be neither local or global for a variety of reasons, e.g., because it is used for debugging, but it is probably an indication of a bug if it is ever both local and global. Unique global symbols are a <font SIZE="-1">GNU</font> extension to the standard set of <font SIZE="-1">ELF</font> symbol bindings. For such a symbol the dynamic linker will make sure that in the entire process there is just one symbol with this name and type in use.</dd>
<dt>&quot;w&quot;</dt>
<dd> The symbol is weak (w) or strong (a space).</dd>
<dt>&quot;C&quot;</dt>
<dd> The symbol denotes a constructor (C) or an ordinary symbol (a space).</dd>
<dt>&quot;W&quot;</dt>
<dd> The symbol is a warning (W) or a normal symbol (a space). A warning symbol&#8217;s name is a message to be displayed if the symbol following the warning symbol is ever referenced.</dd>
<dt>&quot;I&quot;</dt>
<dd>
</dd><dt>&quot;i&quot;</dt>
<dd> The symbol is an indirect reference to another symbol (I), a function to be evaluated during reloc processing (i) or a normal symbol (a space).</dd>
<dt>&quot;d&quot;</dt>
<dd>
</dd><dt>&quot;D&quot;</dt>
<dd> The symbol is a debugging symbol (d) or a dynamic symbol (D) or a normal symbol (a space).</dd>
<dt>&quot;F&quot;</dt>
<dd>
</dd><dt>&quot;f&quot;</dt>
<dd>
</dd><dt>&quot;O&quot;</dt>
<dd> The symbol is the name of a function (F) or a file (f) or an object (O) or just a normal symbol (a space).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-T</code></dt>
<dd>
</dd><dt><code>&#8211;dynamic-syms</code></dt>
<dd> Print the dynamic symbol table entries of the file. This is only meaningful for dynamic objects, such as certain types of shared libraries. This is similar to the information provided by the <code>nm</code> program when given the <code>-D</code> (<code>&#8211;dynamic</code>) option. </dd>
<p> The output format is similar to that produced by the <code>&#8211;syms</code> option, except that an extra field is inserted before the symbol&#8217;s name, giving the version information associated with the symbol. If the version is the default version to be used when resolving unversioned references to the symbol then it&#8217;s displayed as is, otherwise it&#8217;s put into parentheses.</p>
<dt><code>&#8211;special-syms</code></dt>
<dd> When displaying symbols include those which the target considers to be special in some way and which would not normally be of interest to the user.</dd>
<dt><code>-U</code> <i>[d|i|l|e|x|h]</i></dt>
<dd>
</dd><dt><code>&#8211;unicode=</code><i>[default|invalid|locale|escape|hex|highlight]</i></dt>
<dd> Controls the display of <font SIZE="-1">UTF-8</font> encoded multibyte characters in strings. The default (<code>&#8211;unicode=default</code>) is to give them no special treatment. The <code>&#8211;unicode=locale</code> option displays the sequence in the current locale, which may or may not support them. The options <code>&#8211;unicode=hex</code> and <code>&#8211;unicode=invalid</code> display them as hex byte sequences enclosed by either angle brackets or curly braces. </dd>
<p> The <code>&#8211;unicode=escape</code> option displays them as escape sequences (<i>
</p></dl>