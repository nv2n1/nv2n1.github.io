---
title: "xa(1)"
name: "xa"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xa/"
description: "xa – 6502/R65C02/65816 cross-assembler"
---

<h2 class="name">NAME</h2>
<p> xa &#8211; 6502/R65C02/65816 cross-assembler</p>
<h2>SYNOPSIS</h2>
<p> <code>xa</code> [<i>OPTION</i>]&#8230; <i>FILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xa</code> is a multi-pass cross-assembler for the 8-bit processors in the 6502 series (such as the 6502, 65C02, 6504, 6507, 6510, 7501, 8500, 8501 and 8502), the Rockwell R65C02, and the 16-bit 65816 processor. For a description of syntax, see <code>ASSEMBLER SYNTAX</code> further in this manual page. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Verbose output.</p>
<dt><code>-x</code></p>
<dd> Use old filename behaviour (overrides <code>-o</code>, <code>-e</code> and <code>-l</code>). This option is now deprecated.</p>
<dt><code>-C</code></p>
<dd> No CMOS opcodes (default is to allow R65C02 opcodes)</p>
<dt><code>-W</code></p>
<dd> No 65816 opcodes (default).</p>
<dt><code>-w</code></p>
<dd> Allow 65816 opcodes.</p>
<dt><code>-B</code></p>
<dd> Show lines with block open/close (see <code>PSEUDO-OPS</code>).</p>
<dt><code>-c</code></p>
<dd> Produce o65 object files instead of executable files (no linking performed); files may contain undefined references.</p>
<dt><code>-o filename</code></p>
<dd> Set output filename. The default is <code>a.o65</code>; use the special filename <code>&#8211;</code> to output to standard output.</p>
<dt><code>-e filename</code></p>
<dd> Set errorlog filename, default is none.</p>
<dt><code>-l filename</code></p>
<dd> Set labellist filename, default is none. This is the symbol table and can be used by disassemblers such as <code><a href="/docs/linux/man/1-dxa/">dxa</a></code>(1) to reconstruct source.</p>
<dt><code>-r</code></p>
<dd> Add cross-reference list to labellist (requires <code>-l</code>).</p>
<dt><code>-M</code></p>
<dd> Allow colons to appear in comments; for MASM compatibility. This does not affect colon interpretation elsewhere.</p>
<dt><code>-R</code></p>
<dd> Start assembler in relocating mode.</p>
<dt><code>-Llabel</code></p>
<dd> Defines <code>label</code> as an absolute (but undefined) label even when linking.</p>
<dt><code>-b? addr</code></p>
<dd> Set segment base for segment <code>?</code> to address <code>addr</code>. <code>?</code> should be t, d, b or z for text, data, bss or zero segments, respectively.</p>
<dt><code>-A addr</code></p>
<dd> Make text segment start at an address such that when the file starts at address <code>addr</code>, relocation is not necessary. Overrides <code>-bt</code>; other segments still have to be taken care of with <code>-b</code>. </p>
<dt><code>-G</code></p>
<dd> Suppress list of exported globals.</p>
<dt><code>-DDEF=TEXT</code></p>
<dd> Define a preprocessor macro on the command line (see <code>PREPROCESSOR</code>).</p>
<dt><code>-I dir</code></p>
<dd> Add directory <code>dir</code> to the include path (before <code>XAINPUT</code>; see <code>ENVIRONMENT</code>).</p>
<dt><code>-O charset </code></p>
<dd> Define the output charset for character strings. Currently supported are ASCII (default), PETSCII (Commodore ASCII), PETSCREEN (Commodore screen codes) and HIGH (set high bit on all characters).</p>
<dt><code>-p?</code></p>
<dd> Set the alternative preprocessor character to <code>?</code>. This is useful when you wish to use <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) and the built-in preprocessor at the same time (see <code>PREPROCESSOR</code>). Characters may need to be quoted for your shell (example: <code>-p&#8217;~&#8217;</code> ).</p>
<dt><code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>ASSEMBLER SYNTAX</h2>
<p> An introduction to 6502 assembly language programming and mnemonics is beyond the scope of this manual page. We invite you to investigate any number of the excellent books on the subject; one useful title is &quot;Machine Language For Beginners&quot; by Richard Mansfield (COMPUTE!), covering the Atari, Commodore and Apple 8-bit systems, and is widely available on the used market. </p>
<p> <code>xa</code> supports both the standard NMOS 6502 opcodes as well as the Rockwell CMOS opcodes used in the 65C02 (R65C02). With the <code>-w</code> option, <code>xa</code> will also accept opcodes for the 65816. NMOS 6502 undocumented opcodes are intentionally not supported, and should be entered manually using the <code>.byte</code> pseudo-op (see <code>PSEUDO-OPS</code>). Due to conflicts between the R65C02 and 65816 instruction sets and undocumented instructions on the NMOS 6502, their use is discouraged. </p>
<p> In general, <code>xa</code> accepts the more-or-less standard 6502 assembler format as popularised by MASM and TurboAssembler. Values and addresses can be expressed either as literals, or as expressions; to wit,</p>
<dl>
<dt><code>123</code></p>
<dd> decimal value</p>
<dt><code>$234</code></p>
<dd> hexadecimal value</p>
<dt><code>&amp;123</code></p>
<dd> octal</p>
<dt><code>%010110</code></p>
<dd> binary</p>
<dt><code>*</code></p>
<dd> current value of the program counter</dl>
<p> The ASCII value of any quoted character is inserted directly into the program text (example: <code>A</code> inserts the byte &quot;A&quot; into the output stream); see also the <code>PSEUDO-OPS</code> section. This is affected by the currently selected character set, if any. </p>
<p> <code>Labels</code> define locations within the program text, just as in other multi-pass assemblers. A label is defined by anything that is not an opcode; for example, a line such as</p>
<dl>
<dt>
<dd> <code>label1 lda #0</code></dl>
<p> defines <code>label1</code> to be the current location of the program counter (thus the address of the <code>LDA</code> opcode). A label can be explicitly defined by assigning it the value of an expression, such as</p>
<dl>
<dt>
<dd> <code>label2 = $d000</code></dl>
<p> which defines <code>label2</code> to be the address $d000, namely, the start of the VIC-II register block on Commodore 64 computers. The program counter <code>*</code> is considered to be a special kind of label, and can be assigned to with statements such as</p>
<dl>
<dt>
<dd> <code>* = $c000</code></dl>
<p> which sets the program counter to decimal location 49152. With the exception of the program counter, labels cannot be assigned multiple times. To explicitly declare redefinition of a label, place a &#8211; (dash) before it, e.g.,</p>
<dl>
<dt>
<dd> <code>-label2 = $d020</code></dl>
<p> which sets <code>label2</code> to the Commodore 64 border colour register. The scope of a label is affected by the block it resides within (see <code>PSEUDO-OPS</code> for block instructions). A label may also be hard-specified with the <code>-L</code> command line option. </p>
<p> For those instructions where the accumulator is the implied argument (such as <code>asl </code> and <code>lsr</code>; <code>inc</code> and <code>dec</code> on R65C02; etc.), the idiom of explicitly specifying the accumulator with <code>a</code> is unnecessary as the proper form will be selected if there is no explicit argument. In fact, for consistency with label handing, if there is a label named <code>a</code>, this will actually generate code referencing that label as a memory location and not the accumulator. Otherwise, the assembler will complain. </p>
<p> Labels and opcodes may take <code>expressions</code> as their arguments to allow computed values, and may themselves reference other labels and/or the program counter. An expression such as <code>lab1+1</code> (which operates on the current value of label <code>lab1</code> and increments it by one) may use the following operands, given from highest to lowest priority:</p>
<dl>
<dt><code>*</code></p>
<dd> multiplication (priority 10)</p>
<dt><code>/</code></p>
<dd> integer division (priority 10)</p>
<dt><code>+</code></p>
<dd> addition (priority 9)</p>
<dt><code>&#8211;</code></p>
<dd> subtraction (9)</p>
<dt><code>&lt;&lt;</code></p>
<dd> shift left (8)</p>
<dt><code>&gt;&gt;</code></p>
<dd> shift right (8)</p>
<dt><code>&gt;= =&gt;</code></p>
<dd> greater than or equal to (7)</p>
<dt><code>&lt;</code></p>
<dd> greater than (7)</p>
<dt><code>&lt;= =&lt;</code></p>
<dd> less than or equal to (7)</p>
<dt><code>&lt;</code></p>
<dd> less than (7)</p>
<dt><code>=</code></p>
<dd> equal to (6)</p>
<dt><code>&lt;&gt; &gt;&lt;</code></p>
<dd> does not equal (6)</p>
<dt><code>&amp;</code></p>
<dd> bitwise AND (5)</p>
<dt><code>^</code></p>
<dd> bitwise XOR (4)</p>
<dt><code>|</code></p>
<dd> bitwise OR (3)</p>
<dt><code>&amp;&amp;</code></p>
<dd> logical AND (2)</p>
<dt><code>||</code></p>
<dd> logical OR (1)</dl>
<p> Parentheses are valid. When redefining a label, combining arithmetic or bitwise operators with the = (equals) operator such as <code>+=</code> and so on are valid, e.g.,</p>
<dl>
<dt>
<dd> <code>-redeflabel += (label12/4)</code></dl>
<p> Normally, <code>xa</code> attempts to ascertain the value of the operand and (when referring to a memory location) use zero page, 16-bit or (for 65816) 24-bit addressing where appropriate and where supported by the particular opcode. This generates smaller and faster code, and is almost always preferable. </p>
<p> Nevertheless, you can use these prefix operators to force a particular rendering of the operand. Those that generate an eight bit result can also be used in 8-bit addressing modes, such as immediate and zero page.</p>
<dl>
<dt><code>&lt;</code></p>
<dd> low byte of expression, e.g., <code>lda #&lt;vector</code></p>
<dt><code>&gt;</code></p>
<dd> high byte of expression</p>
<dt><code>!</code></p>
<dd> in situations where the expression could be understood as either an absolute or zero page value, do not attempt to optimize to a zero page argument for those opcodes that support it (i.e., keep as 16 bit word)</p>
<dt><code>@</code></p>
<dd> render as 24-bit quantity for 65816 (must specify <code>-w</code> command-line option). <code>This is required to specify any</code> <code>24-bit quantity!</code></p>
<dt><code>`</code></p>
<dd> force further optimization, even if the length of the instruction cannot be reliably determined (see <code>NOTES&#8217;N&#8217;BUGS</code>)</dl>
<p> Expressions can occur as arguments to opcodes or within the preprocessor (see <code>PREPROCESSOR</code> for syntax). For example,</p>
<dl>
<dt>
<dd> <code>lda label2+1</code></dl>
<p> takes the value at <code>label2+1</code> (using our previous label&#8217;s value, this would be $d021), and will be assembled as <code>$ad $21 $d0</code> to disk. Similarly,</p>
<dl>
<dt>
<dd> <code>lda #&lt;label2 </code></dl>
<p> will take the lowest 8 bits of <code>label2</code> (i.e., $20), and assign them to the accumulator (assembling the instruction as <code>$a9 $20</code> to disk). </p>
<p> Comments are specified with a semicolon (;), such as</p>
<dl>
<dt>
<dd> <code>;this is a comment</code></dl>
<p> They can also be specified in the C language style, using <code>/* */</code> and <code>//</code> which are understood at the <code>PREPROCESSOR</code> level (q.v.). </p>
<p> Normally, the colon (:) separates statements, such as</p>
<dl>
<dt>
<dd> <code>label4 lda #0:sta $d020</code></dl>
<p> or</p>
<dl>
<dt>
<dd> <code>label2: lda #2</code></dl>
<p> (note the use of a colon for specifying a label, similar to some other assemblers, which <code>xa</code> also understands with or without the colon). This also applies to semicolon comments, such that</p>
<dl>
<dt>
<dd> <code>; a comment:lda #0</code></dl>
<p> is understood as a comment followed by an opcode. To defeat this, use the <code>-M</code> command line option to allow colons within comments. This does not apply to <code>/* */</code> and <code>//</code> comments, which are dealt with at the preprocessor level (q.v.). </p>
<h2>PSEUDO-OPS</h2>
<p> <code>Pseudo-ops</code> are false opcodes used by the assembler to denote meta- or inlined commands. Like most assemblers, <code>xa</code> has a rich set.</p>
<dl>
<dt><code>.byt value1,value2,value3,&#8230;</code></p>
<dd> Specifies a string of bytes to be directly placed into the assembled object. The arguments may be expressions. Any number of bytes can be specified.</p>
<dt><code>.asc text1,text2,&#8230;</code></p>
<dd> Specifies a character string which will be inserted into the assembled object. Strings are understood according to the currently specified character set; for example, if ASCII is specified, they will be rendered as ASCII, and if PETSCII is specified, they will be translated into the equivalent Commodore ASCII equivalent. Other non-standard ASCIIs such as ATASCII for Atari computers should use the ASCII equivalent characters; graphic and control characters should be specified explicitly using <code>.byt</code> for the precise character you want. Note that when specifying the argument of an opcode, <code>.asc</code> is not necessary; the quoted character can simply be inserted (e.g., <code>lda #A</code> ), and is also affected by the current character set. Any number of character strings can be specified.</dl>
<p> <code>.byt</code> and <code>.asc</code> are synonymous, so you can mix things such as <code>.byt $43, 22, a character string</code> and get the expected result. The string is subject to the current character set, but the remaining bytes are inserted wtihout modification.</p>
<dl>
<dt><code>.aasc text1,text2,&#8230;</code></p>
<dd> Specifies a character string that is <code>always</code> rendered in true ASCII regardless of the current character set. Like <code>.asc</code>, it is synonymous with <code>.byt</code>.</p>
<dt><code>.word value1,value2,value3&#8230;</code></p>
<dd> Specifies a string of 16-bit words to be placed into the assembled object in 6502 little-endian format (that is, low-byte/high-byte). The arguments may be expressions. Any number of words can be specified.</p>
<dt><code>.dsb length,fillbyte</code></p>
<dd> Specifies a data block; a total of <code>length</code> repetitions of <code>fillbyte</code> will be inserted into the assembled object. For example, <code>.dsb 5,$10</code> will insert five bytes, each being 16 decimal, into the object. The arguments may be expressions.</p>
<dt><code>.bin offset,length,filename</code></p>
<dd> Inlines a binary file without further interpretation specified by <code>filename</code> from offset <code>offset</code> to length <code>length</code>. This allows you to insert data such as a previously assembled object file or an image or other binary data structure, inlined directly into this file&#8217;s object. If <code>length</code> is zero, then the length of <code>filename</code>, minus the offset, is used instead. The arguments may be expressions.</p>
<dt><code>.(</code></p>
<dd> Opens a new block for scoping. Within a block, all labels defined are local to that block and any sub-blocks, and go out of scope as soon as the enclosing block is closed (i.e., lexically scoped). All labels defined outside of the block are still visible within it. To explicitly declare a global label within a block, precede the label with <code>+</code> or precede it with <code>&amp;</code> to declare it within the previous level only (or globally if you are only one level deep). Sixteen levels of scoping are permitted.</p>
<dt><code>.)</code></p>
<dd> Closes a block.</p>
<dt><code>.as .al .xs .xl</code></p>
<dd> Only relevant in 65816 mode (with the <code>-w</code> option specified). These pseudo-ops set what size accumulator and X/Y-register should be used for future instructions; <code>.as</code> and <code>.xs</code> set 8-bit operands for the accumulator and index registers, respectively, and <code>.al</code> and <code>.xl</code> set 16-bit operands. These pseudo-ops on purpose do not automatically issue <code>sep</code> and <code>rep</code> instructions to set the specified width in the CPU; set the processor bits as you need, or consider constructing a macro. <code>.al</code> and <code>.xl</code> generate errors if <code>-w</code> is not specified.</dl>
<p> The following pseudo-ops apply primarily to relocatable .o65 objects. A full discussion of the relocatable format is beyond the scope of this manpage, as it is currently a format in flux. Documentation on the proposed v1.2 format is in <code>doc/fileformat.txt</code> within the <code>xa</code> installation directory.</p>
<dl>
<dt><code>.text .data .bss .zero</code></p>
<dd> These pseudo-ops switch between the different segments, .text being the actual code section, .data being the data segment, .bss being uninitialized label space for allocation and .zero being uninitialized zero page space for allocation. In .bss and .zero, only labels are evaluated. These pseudo-ops are valid in relative and absolute modes.</p>
<dt><code>.align value</code></p>
<dd> Aligns the current segment to a byte boundary (2, 4 or 256) as specified by <code>value</code> (and places it in the header when relative mode is enabled). Other values generate an error.</p>
<dt><code>.fopt type,value1,value2,value3,&#8230;</code></p>
<dd> Acts like <code>.byt/.asc</code> except that the values are embedded into the object file as file options. The argument <code>type</code> is used to specify the file option being referenced. A table of these options is in the relocatable o65 file format description. The remainder of the options are interpreted as values to insert. Any number of values may be specified, and may also be strings. </p>
</dl>
<h2>PREPROCESSOR</h2>
<p> <code>xa</code> implements a preprocessor very similar to that of the C-language preprocessor <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) and many oddiments apply to both. For example, as in C, the use of <code>/* */</code> for comment delimiters is also supported in <code>xa</code>, and so are comments using the double slash <code>//</code>. The preprocessor also supports continuation lines, i.e., lines ending with a backslash (\); the following line is then appended to it as if there were no dividing newline. This too is handled at the preprocessor level. </p>
<p> For reasons of memory and complexity, the full breadth of the <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) syntax is not fully supported. In particular, macro definitions may not be forward-defined (i.e., a macro definition can only reference a previously defined macro definition), except for macro functions, where recursive evaluation is supported; e.g., to <code>#define WW AA</code> , <code>AA</code> must have already been defined. Certain other directives are not supported, nor are most standard pre-defined macros, and there are other limits on evaluation and line length. Because the maintainers of <code>xa</code> recognize that some files will require more complicated preparsing than the built-in preprocessor can supply, the preprocessor will accept <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1)-style line/filename/flags output. When these lines are seen in the input file, <code>xa</code> will treat them as <code>cc</code> would, except that flags are ignored. <code>xa</code> does not accept files on standard input for parsing reasons, so you should dump your <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) output to an intermediate temporary file, such as</p>
<dl>
<dt>
<dd> <code>cc -E test.s &gt; test.xa</code><br />
 <code>xa test.xa</code></dl>
<p> No special arguments need to be passed to <code>xa</code>; the presence of <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) output is detected automatically. </p>
<p> Note that passing your file through <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) may interfere with <code>xa</code>&#8216;s own preprocessor directives. In this case, to mask directives from <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1), use the <code>-p</code> option to specify an alternative character instead of <code>#</code>, such as the tilde (e.g., <code>-p&#8217;~&#8217;</code> ). With this option and argument specified, then instead of <code>#include</code>, for example, you can also use <code>~include</code>, in addition to <code>#include </code> (which will also still be accepted by the <code>xa</code> preprocessor, assuming any survive <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1)). Any character can be used, although frankly pathologic choices may lead to amusing and frustrating glitches during parsing. You can also use this option to defer preprocessor directives that <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) may interpret too early until the file actually gets to <code>xa</code> itself for processing. </p>
<p> The following preprocessor directives are supported. </p>
<dl>
<dt><code>#include filename</code></p>
<dd> Inserts the contents of file <code>filename</code> at this position. If the file is not found, it is searched using paths specified by the <code>-I</code> command line option or the environment variable <code>XAINPUT</code> (q.v.). When inserted, the file will also be parsed for preprocessor directives.</p>
<dt><code>#echo comment</code></p>
<dd> Inserts comment <code>comment</code> into the errorlog file, specified with the <code>-e</code> command line option.</p>
<dt><code>#print expression</code></p>
<dd> Computes the value of expression <code>expression</code> and prints it into the errorlog file.</p>
<dt><code>#define DEFINE text</code></p>
<dd> Equates macro <code>DEFINE</code> with text <code>text</code> such that wherever <code>DEFINE</code> appears in the assembly source, <code>text</code> is substituted in its place (just like <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) would do). In addition, <code>#define</code> can specify macro functions like <code><a href="/docs/linux/man/1-cpp/">cpp</a></code>(1) such that a directive like <code>#define mult(a,b) ((a)*(b))</code> would generate the expected result wherever an expression of the form <code>mult(a,b)</code> appears in the source. This can also be specified on the command line with the <code>-D</code> option. The arguments of a macro function may be recursively evaluated, unlike other <code>#define</code>s; the preprocessor will attempt to re-evaluate any argument refencing another preprocessor definition up to ten times before complaining.</dl>
<p> The following directives are conditionals. If the conditional is not satisfied, then the source code between the directive and its terminating <code>#endif</code> are expunged and not assembled. Up to fifteen levels of nesting are supported.</p>
<dl>
<dt><code>#endif</code></p>
<dd> Closes a conditional block.</p>
<dt><code>#else</code></p>
<dd> Implements alternate path for a conditional block.</p>
<dt><code>#ifdef DEFINE</code></p>
<dd> True only if macro <code>DEFINE</code> is defined.</p>
<dt><code>#ifndef DEFINE</code></p>
<dd> The opposite; true only if macro <code>DEFINE</code> has not been previously defined.</p>
<dt><code>#if expression</code></p>
<dd> True if expression <code>expression</code> evaluates to non-zero. <code>expression</code> may reference other macros.</p>
<dt><code>#iflused label</code></p>
<dd> True if label <code>label</code> has been used (but not necessarily instantiated with a value). <i>This works on labels, not macros!</i></p>
<dt><code>#ifldef label</code></p>
<dd> True if label <code>label</code> is defined <i>and</i> assigned with a value. <i>This works on labels, not macros!</i></dl>
<p> Unclosed conditional blocks at the end of included files generate warnings; unclosed conditional blocks at the end of assembly generate an error. </p>
<p> <code>#iflused</code> and <code>#ifldef</code> are useful for building up a library based on labels. For example, you might use something like this in your library&#8217;s code:</p>
<dl>
<dt>
<dd> <code>#iflused label</code><br />
 <code>#ifldef label</code><br />
 <code>#echo label already defined, library function label cannot be inserted</code><br />
 <code>#else</code><br />
 <code>label /* your code */</code><br />
 <code>#endif</code><br />
 <code>#endif</code> </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> <code>xa</code> utilises the following environment variables, if they exist: </p>
<dl>
<dt><code>XAINPUT</code></p>
<dd> Include file path; components should be separated by `,&#8217;.</p>
<dt><code>XAOUTPUT</code></p>
<dd> Output file path. </p>
</dl>
<h2>NOTES&#8217;N&#8217;BUGS</h2>
<p> The R65C02 instructions <code>ina</code> (often rendered <code>inc</code> <code>a</code>) and <code>dea</code> (<code>dec</code> <code>a</code>) must be rendered as bare <code>inc</code> and <code>dec</code> instructions respectively. </p>
<p> The 65816 instructions <code>mvn</code> and <code>mvp</code> use two eight bit parameters, the only instructions in the entire instruction set to do so. Older versions of <code>xa</code> took a single 16-bit absolute value. Since 2.3.7, the standard syntax is now accepted and the old syntax is deprecated (a warning will be generated). </p>
<p> Forward-defined labels &#8212; that is, labels that are defined after the current instruction is processed &#8212; cannot be optimized into zero page instructions even if the label does end up being defined as a zero page location, because the assembler does not know the value of the label in advance during the first pass when the length of an instruction is computed. On the second pass, a warning will be issued when an instruction that could have been optimized can&#8217;t be because of this limitation. (Obviously, this does not apply to branching or jumping instructions because they&#8217;re not optimizable anyhow, and those instructions that can <i>only</i> take an 8-bit parameter will always be casted to an 8-bit quantity.) If the label cannot otherwise be defined ahead of the instruction, the backtick prefix <code>`</code> may be used to force further optimization no matter where the label is defined as long as the instruction supports it. Indiscriminately forcing the issue can be fraught with peril, however, and is not recommended; to discourage this, the assembler will complain about its use in addressing mode situations where no ambiguity exists, such as indirect indexed, branching and so on. </p>
<p> Also, as a further consequence of the way optimization is managed, we repeat that <code>all</code> 24-bit quantities and labels that reference a 24-bit quantity in 65816 mode, anteriorly declared or otherwise, <code>MUST</code> be prepended with the <code>@</code> prefix. Otherwise, the assembler will attempt to optimize to 16 bits, which may be undesirable. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file65/">file65</a></code>(1), <code><a href="/docs/linux/man/1-ldo65/">ldo65</a></code>(1), <code><a href="/docs/linux/man/1-printcbm/">printcbm</a></code>(1), <code><a href="/docs/linux/man/1-reloc65/">reloc65</a></code>(1), <code><a href="/docs/linux/man/1-uncpk/">uncpk</a></code>(1), <code><a href="/docs/linux/man/1-dxa/">dxa</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by David Weinehall &lt;tao [at] acc.umu.se&gt;, Andre Fachat &lt;fachat [at] web.de&gt; and Cameron Kaiser &lt;ckaiser [at] floodgap.com&gt;. Original xa package (C)1989-1997 Andre Fachat. Additional changes (C)1989-2015 Andre Fachat, Jolse Maginnis, David Weinehall, Cameron Kaiser. The official maintainer is Cameron Kaiser. </p>
<h2>WEBSITE</h2>
<p> <a rel="nofollow" href="http://www.floodgap.com/retrotech/xa/">http://www.floodgap.com/retrotech/xa/</a> </p>
<h2>Index</h2>
