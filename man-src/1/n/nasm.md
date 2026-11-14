---
title: "nasm(1)"
name: "nasm"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nasm/"
description: "nasm – the Netwide Assembler, a portable 80×86 assembler"
---

<h2 class="name">NAME</h2>
<p> nasm &#8211; the Netwide Assembler, a portable 80&#215;86 assembler </p>
<h2>SYNOPSIS</h2>
<p> <code>nasm</code> [<code>-@</code> response file] [<code>-f</code> format] [<code>-o</code> outfile] [<code>-l</code> listfile] [<i>options</i>&#8230;] filename</p>
<h2>DESCRIPTION</h2>
<p> The <code>nasm</code> command assembles the file <i>filename</i> and directs output to the file <i>outfile</i> if specified. If <i>outfile</i> is not specified, <code>nasm</code> will derive a default output file name from the name of its input file, usually by appending &#8216;.o&#8217; or &#8216;.obj&#8217;, or by removing all extensions for a raw binary file. Failing that, the output file name will be &#8216;nasm.out&#8217;.</p>
<h2>OPTIONS</h2>
<p> <code>-@</code> <i>filename</i></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to process options from filename as if they were included on the command line.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to assemble the given input file without first applying the macro preprocessor.</dl>
<p> <code>-D</code>|<code>-d</code> <i>macro[=value]</i></p>
<dl>
<dt>
<dd> Pre-defines a single-line macro.</dl>
<p> <code>-E</code>|<code>-e</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to preprocess the given input file, and write the output to <i>stdout</i> (or the specified output file name), and not actually assemble anything.</dl>
<p> <code>-f</code> <i>format</i></p>
<dl>
<dt>
<dd> Specifies the output file format. To see a list of valid output formats, use the <code>-hf</code> option.</dl>
<p> <code>-F</code> <i>format</i></p>
<dl>
<dt>
<dd> Specifies the debug information format. To see a list of valid output formats, use the <code>-y</code> option (for example <code>-felf -y</code>).</dl>
<p> <code>-g</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to generate debug information in selected format.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to exit immediately, after giving a summary of its invocation options.</dl>
<p> <code>-hf</code></p>
<dl>
<dt>
<dd> Same as <code>-h</code> , but also lists all valid output formats.</dl>
<p> <code>-I</code>|<code>-i</code> <i>directory</i></p>
<dl>
<dt>
<dd> Adds a directory to the search path for include files. The directory specification must include the trailing slash, as it will be directly prepended to the name of the include file.</dl>
<p> <code>-l</code> <i>listfile</i></p>
<dl>
<dt>
<dd> Causes an assembly listing to be directed to the given file, in which the original source is displayed on the right hand side (plus the source for included files and the expansions of multi-line macros) and the generated code is shown in hex on the left.</dl>
<p> <code>-M</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to output Makefile-style dependencies to stdout; normal output is suppressed.</dl>
<p> <code>-MG</code> <i>file</i></p>
<dl>
<dt>
<dd> Same as <code>-M</code> but assumes that missing Makefile dependecies are generated and added to dependency list without a prefix.</dl>
<p> <code>-MF</code> <i>file</i></p>
<dl>
<dt>
<dd> Output Makefile-style dependencies to the specified file.</dl>
<p> <code>-MD</code> <i>file</i></p>
<dl>
<dt>
<dd> Same as a combination of <code>-M</code> and <code>-MF</code> options.</dl>
<p> <code>-MT</code> <i>file</i></p>
<dl>
<dt>
<dd> Override the default name of the dependency target dependency target name. This is normally the same as the output filename, specified by the <code>-o</code> option.</dl>
<p> <code>-MQ</code> <i>file</i></p>
<dl>
<dt>
<dd> The same as <code>-MT</code> except it tries to quote characters that have special meaning in Makefile syntax. This is not foolproof, as not all characters with special meaning are quotable in Make.</dl>
<p> <code>-MP</code></p>
<dl>
<dt>
<dd> Emit phony target.</dl>
<p> <code>-O</code> <i>number</i></p>
<dl>
<dt>
<dd> Optimize branch offsets. </p>
<dl>
<dt>
<dd> &bull; <code>-O0</code>: No optimization</dl>
<dl>
<dt>
<dd> &bull; <code>-O1</code>: Minimal optimization</dl>
<dl>
<dt>
<dd> &bull; <code>-Ox</code>: Multipass optimization (default)</dl>
</dl>
<p> <code>-o</code> <i>outfile</i></p>
<dl>
<dt>
<dd> Specifies a precise name for the output file, overriding <code>nasm</code>&#8216;s default means of determining it.</dl>
<p> <code>-P</code>|<code>-p</code> <i>file</i></p>
<dl>
<dt>
<dd> Specifies a file to be pre-included, before the main source file starts to be processed.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to send its error messages and/or help text to stdout instead of stderr.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to assemble in SciTech TASM compatible mode.</dl>
<p> <code>-U</code>|<code>-u</code> <i>macro</i></p>
<dl>
<dt>
<dd> Undefines a single-line macro.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to exit immediately, after displaying its version number.</dl>
<p> *-W[no-]foo&#8217;</p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to enable or disable certain classes of warning messages, in gcc-like style, for example <code>-Worphan-labels</code> or <code>-Wno-orphan-labels</code>.</dl>
<p> <code>-w</code><i>[+-]foo</i></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to enable or disable certain classes of warning messages, for example <code>-w+orphan-labels</code> or <code>-w-macro-params</code>.</dl>
<p> <code>-X</code> <i>format</i></p>
<dl>
<dt>
<dd> Specifies error reporting format (gnu or vc).</dl>
<p> <code>-y</code></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to list supported debug formats.</dl>
<p> <code>-Z</code> <i>filename</i></p>
<dl>
<dt>
<dd> Causes <code>nasm</code> to redirect error messages to <i>filename</i>. This option exists to support operating systems on which stderr is not easily redirected.</dl>
<p> &#8211;prefix, &#8211;postfix</p>
<dl>
<dt>
<dd> Prepend or append (respectively) the given argument to all global or extern variables.</dl>
<h2>SYNTAX</h2>
<p> This man page does not fully describe the syntax of <code>nasm</code>&#8216;s assembly language, but does give a summary of the differences from other assemblers. </p>
<p> <i>Registers</i> have no leading &#8216;%&#8217; sign, unlike <code>gas</code>, and floating-point stack registers are referred to as <i>st0</i>, <i>st1</i>, and so on. </p>
<p> <i>Floating-point instructions</i> may use either the single-operand form or the double. A <i>TO</i> keyword is provided; thus, one could either write </p>
<dl>
<dt>
<dd>
<pre>
fadd st0,st1
fadd st1,st0
</pre>
</dl>
<p> or one could use the alternative single-operand forms </p>
<dl>
<dt>
<dd>
<pre>
fadd st1
fadd to st1
</pre>
</dl>
<p> <i>Uninitialised storage</i> is reserved using the <i>RESB</i>, <i>RESW</i>, <i>RESD</i>, <i>RESQ</i>, <i>REST</i> and <i>RESO</i> pseudo-opcodes, each taking one parameter which gives the number of bytes, words, doublewords, quadwords or ten-byte words to reserve. </p>
<p> <i>Repetition</i> of data items is not done by the <i>DUP</i> keyword as seen in DOS assemblers, but by the use of the <i>TIMES</i> prefix, like this: </p>
<dl>
<dt>
<dd>
<pre>
message: times 3 db 'abc'
         times 64-$+message db 0
</pre>
</dl>
<p> which defines the string abcabcabc, followed by the right number of zero bytes to make the total length up to 64 bytes. </p>
<p> <i>Symbol references</i> are always understood to be immediate (i.e. the address of the symbol), unless square brackets are used, in which case the contents of the memory location are used. Thus: </p>
<dl>
<dt>
<dd>
<pre>
mov ax,wordvar
</pre>
</dl>
<p> loads AX with the address of the variable wordvar, whereas </p>
<dl>
<dt>
<dd>
<pre><code>
mov ax, [wordvar] mov ax, [wordvar + 1] mov ax, [es:wordvar + bx]
</code></pre>
</dl>
<p> all refer to the <i>contents</i> of memory locations. The syntaxes </p>
<dl>
<dt>
<dd>
mov ax, es : wordvar[bx] es mov ax, wordvar[1]
</dl>
<p> are not legal at all, although the use of a segment register name as an instruction prefix is valid, and can be used with instructions such as <i>LODSB</i> which can&#8217;t be overridden any other way. </p>
<p> <i>Constants</i> may be expressed numerically in most formats: a trailing H, Q or B denotes hex, octal or binary respectively, and a leading &#8216;0x&#8217; or &#8216;$&#8217; denotes hex as well. Leading zeros are not treated specially at all. Character constants may be enclosed in single or double quotes; there is no escape character. The ordering is little-endian (reversed), so that the character constant <i>&#8216;abcd</i>&#8216; denotes 0x64636261 and not 0x61626364. </p>
<p> Local labels begin with a period, and their &#8216;locality&#8217; is granted by the assembler prepending the name of the previous non-local symbol. Thus declaring a label &#8216;.loop&#8217; after a label &#8216;label&#8217; has actually defined a symbol called &#8216;label.loop&#8217;.</p>
<h2>DIRECTIVES</h2>
<p> <i>SECTION</i> <i>name</i> or <i>SEGMENT</i> <i>name</i> causes <code>nasm</code> to direct all following code to the named section. Section names vary with output file format, although most formats support the names <i>.text</i>, <i>.data</i> and <i>.bss</i>. (The exception is the <i>obj</i> format, in which all segments are user-definable.) </p>
<p> <i>ABSOLUTE</i> <i>address</i> causes <code>nasm</code> to position its notional assembly point at an absolute address: so no code or data may be generated, but you can use <i>RESB</i>, <i>RESW</i> and <i>RESD</i> to move the assembly point further on, and you can define labels. So this directive may be used to define data structures. When you have finished doing absolute assembly, you must issue another <i>SECTION</i> directive to return to normal assembly. </p>
<p> <i>BITS</i> <i>16</i>, <i>BITS</i> <i>32</i> or <i>BITS</i> <i>64</i> switches the default processor mode for which <code>nasm</code> is generating code: it is equivalent to <i>USE16</i> or <i>USE32</i> in DOS assemblers. </p>
<p> <i>EXTERN</i> <i>symbol</i> and <i>GLOBAL</i> <i>symbol</i> import and export symbol definitions, respectively, from and to other modules. Note that the <i>GLOBAL</i> directive must appear before the definition of the symbol it refers to. </p>
<p> <i>STRUC</i> <i>strucname</i> and <i>ENDSTRUC</i>, when used to bracket a number of <i>RESB</i>, <i>RESW</i> or similar instructions, define a data structure. In addition to defining the offsets of the structure members, the construct also defines a symbol for the size of the structure, which is simply the structure name with <i>size</i> tacked on to the end.</p>
<h2>FORMAT-SPECIFIC DIRECTIVES</h2>
<p> <i>ORG</i> <i>address</i> is used by the <i>bin</i> flat-form binary output format, and specifies the address at which the output code will eventually be loaded. </p>
<p> <i>GROUP</i> <i>grpname</i> <i>seg1</i> <i>seg2</i>&#8230; is used by the obj (Microsoft 16-bit) output format, and defines segment groups. This format also uses <i>UPPERCASE</i>, which directs that all segment, group and symbol names output to the object file should be in uppercase. Note that the actual assembly is still case sensitive. </p>
<p> <i>LIBRARY</i> <i>libname</i> is used by the <i>rdf</i> output format, and causes a dependency record to be written to the output file which indicates that the program requires a certain library in order to run.</p>
<h2>MACRO PREPROCESSOR</h2>
<p> Single-line macros are defined using the <i>%define</i> or <i>%idefine</i> commands, in a similar fashion to the C preprocessor. They can be overloaded with respect to number of parameters, although defining a macro with no parameters prevents the definition of any macro with the same name taking parameters, and vice versa. <i>%define</i> defines macros whose names match case-sensitively, whereas <i>%idefine</i> defines case-insensitive macros. </p>
<p> Multi-line macros are defined using <i>%macro</i> and <i>%imacro</i> (the distinction is the same as that between <i>%define</i> and <i>%idefine</i>), whose syntax is as follows </p>
<dl>
<dt>
<dd>
<pre><code>
% macro name minprm[-maxprm][+][.nolist][defaults]&lt;some lines of macro expansion text&gt; % endmacro
</code></pre>
</dl>
<p> Again, these macros may be overloaded. The trailing plus sign indicates that any parameters after the last one get subsumed, with their separating commas, into the last parameter. The <i>defaults</i> part can be used to specify defaults for unspecified macro parameters after <i>minparam</i>. <i>%endm</i> is a valid synonym for <i>%endmacro</i>. </p>
<p> To refer to the macro parameters within a macro expansion, you use <i>%1</i>, <i>%2</i> and so on. You can also enforce that a macro parameter should contain a condition code by using <i>%+1</i>, and you can invert the condition code by using <i>%-1</i>. You can also define a label specific to a macro invocation by prefixing it with a double &#8216;%&#8217; sign. </p>
<p> Files can be included using the <i>%include</i> directive, which works like C. </p>
<p> The preprocessor has a &#8216;context stack&#8217;, which may be used by one macro to store information that a later one will retrieve. You can push a context on the stack using <i>%push</i>, remove one using <i>%pop</i>, and change the name of the top context (without disturbing any associated definitions) using <i>%repl</i>. Labels and <i>%define</i> macros specific to the top context may be defined by prefixing their names with %$, and things specific to the next context down with %$$, and so on. </p>
<p> Conditional assembly is done by means of <i>%ifdef</i>, <i>%ifndef</i>, <i>%else</i> and <i>%endif</i> as in C. (Except that <i>%ifdef</i> can accept several putative macro names, and will evaluate TRUE if any of them is defined.) In addition, the directives <i>%ifctx</i> and <i>%ifnctx</i> can be used to condition on the name of the top context on the context stack. The obvious set of &#8216;else-if&#8217; directives, <i>%elifdef</i>, <i>%elifndef</i>, <i>%elifctx</i> and <i>%elifnctx</i> are also supported.</p>
<h2>BUGS</h2>
<p> Please report bugs through the bug tracker function at m[blue]<code><a rel="nofollow" href="http://nasm.us">http://nasm.us</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-as/">as</a></code>(1), <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1). </p>
<h2>Index</h2>
