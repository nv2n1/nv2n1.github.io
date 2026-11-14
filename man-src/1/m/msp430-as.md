---
title: "msp430-as(1)"
name: "msp430-as"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-as/"
description: "AS – the portable GNU assembler."
---

<h2>NAME</h2>
<p> AS &#8211; the portable GNU assembler.</p>
<h2>SYNOPSIS</h2>
<p> as [<code>-a</code>[<code>cdghlns</code>][=<i>file</i>]] [<code>&#8211;alternate</code>] [<code>-D</code>]<br />
&nbsp;<wbr>[<code>&#8211;debug-prefix-map</code>&nbsp;<wbr><i>old</i>=<i>new</i>]<br />
&nbsp;<wbr>[<code>&#8211;defsym</code>&nbsp;<wbr><i>sym</i>=<i>val</i>]&nbsp;<wbr>[<code>-f</code>]&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>&#8211;gstabs</code>]<br />
&nbsp;<wbr>[<code>&#8211;gstabs+</code>]&nbsp;<wbr>[<code>&#8211;gdwarf-2</code>]&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>dir</i>]&nbsp;<wbr>[<code>-J</code>]<br />
&nbsp;<wbr>[<code>-K</code>]&nbsp;<wbr>[<code>-L</code>]&nbsp;<wbr>[<code>&#8211;listing-lhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;listing-lhs-width2</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;<wbr>[<code>&#8211;listing-rhs-width</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;listing-cont-lines</code>=<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]&nbsp;<wbr>[<code>&#8211;keep-locals</code>]&nbsp;<wbr>[<code>-o</code><br />
&nbsp;<wbr><i>objfile</i>]&nbsp;<wbr>[<code>-R</code>]&nbsp;<wbr>[<code>&#8211;reduce-memory-overheads</code>]&nbsp;<wbr>[<code>&#8211;statistics</code>]<br />
&nbsp;<wbr>[<code>-v</code>]&nbsp;<wbr>[<code>-version</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>-W</code>]&nbsp;<wbr>[<code>&#8211;warn</code>]<br />
&nbsp;<wbr>[<code>&#8211;fatal-warnings</code>]&nbsp;<wbr>[<code>-w</code>]&nbsp;<wbr>[<code>-x</code>]&nbsp;<wbr>[<code>-Z</code>]&nbsp;<wbr>[<code>@</code><i></i><font SIZE="-1"><i>FILE</i></font><i></i>]<br />
&nbsp;<wbr>[<code>&#8211;target-help</code>]&nbsp;<wbr>[<i>target-options</i>]<br />
&nbsp;<wbr>[<code>&#8212;</code>|<i>files</i>&nbsp;<wbr>&#8230;] </p>
<p> <i>Target Alpha options:</i><br />
[<code>-m</code><i>cpu</i>]<br />
[<code>-mdebug</code>&nbsp;<wbr>|&nbsp;<wbr><code>-no-mdebug</code>]<br />
[<code>-relax</code>]&nbsp;<wbr>[<code>-g</code>]&nbsp;<wbr>[<code>-G</code><i>size</i>]<br />
[<code>-F</code>]&nbsp;<wbr>[<code>-32addr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARC</i></font><i> options:</i><br />
[<code>-marc[5|6|7|8]</code>]<br />
[<code>-EB</code>|<code>-EL</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>ARM</i></font><i> options:</i><br />
[<code>-mcpu</code>=<i>processor</i>[+<i>extension</i>&#8230;]]<br />
[<code>-march</code>=<i>architecture</i>[+<i>extension</i>&#8230;]]<br />
[<code>-mfpu</code>=<i>floating-point-format</i>]<br />
[<code>-mfloat-abi</code>=<i>abi</i>]<br />
[<code>-meabi</code>=<i>ver</i>]<br />
[<code>-mthumb</code>]<br />
[<code>-EB</code>|<code>-EL</code>]<br />
[<code>-mapcs-32</code>|<code>-mapcs-26</code>|<code>-mapcs-float</code>|<br />
&nbsp;<wbr><code>-mapcs-reentrant</code>]<br />
[<code>-mthumb-interwork</code>]&nbsp;<wbr>[<code>-k</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>CRIS</i></font><i> options:</i><br />
[<code>&#8211;underscore</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;no-underscore</code>]<br />
[<code>&#8211;pic</code>]&nbsp;<wbr>[<code>-N</code>]<br />
[<code>&#8211;emulation=criself</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;emulation=crisaout</code>]<br />
[<code>&#8211;march=v0_v10</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=v10</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=v32</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;march=common_v10_v32</code>] </p>
<p> <i>Target D10V options:</i><br />
[<code>-O</code>] </p>
<p> <i>Target D30V options:</i><br />
[<code>-O</code>|<code>-n</code>|<code>-N</code>] </p>
<p> <i>Target H8/300 options:</i><br />
[-h-tick-hex] </p>
<p> <i>Target i386 options:</i><br />
[<code>&#8211;32</code>|<code>&#8211;64</code>]&nbsp;<wbr>[<code>-n</code>]<br />
[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>[+<i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>&#8230;]]&nbsp;<wbr>[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;<wbr> </p>
<p> <i>Target i960 options:</i><br />
[<code>-ACA</code>|<code>-ACA_A</code>|<code>-ACB</code>|<code>-ACC</code>|<code>-AKA</code>|<code>-AKB</code>|<br />
&nbsp;<wbr><code>-AKC</code>|<code>-AMC</code>]<br />
[<code>-b</code>]&nbsp;<wbr>[<code>-no-relax</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IA-64</i></font><i> options:</i><br />
[<code>-mconstant-gp</code>|<code>-mauto-pic</code>]<br />
[<code>-milp32</code>|<code>-milp64</code>|<code>-mlp64</code>|<code>-mp64</code>]<br />
[<code>-mle</code>|<code>mbe</code>]<br />
[<code>-mtune=itanium1</code>|<code>-mtune=itanium2</code>]<br />
[<code>-munwind-check=warning</code>|<code>-munwind-check=error</code>]<br />
[<code>-mhint.b=ok</code>|<code>-mhint.b=warning</code>|<code>-mhint.b=error</code>]<br />
[<code>-x</code>|<code>-xexplicit</code>]&nbsp;<wbr>[<code>-xauto</code>]&nbsp;<wbr>[<code>-xdebug</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>IP2K</i></font><i> options:</i><br />
[<code>-mip2022</code>|<code>-mip2022ext</code>] </p>
<p> <i>Target M32C options:</i><br />
[<code>-m32c</code>|<code>-m16c</code>]&nbsp;<wbr>[-relax]&nbsp;<wbr>[-h-tick-hex] </p>
<p> <i>Target M32R options:</i><br />
[<code>&#8211;m32rx</code>|<code>&#8211;[no-]warn-explicit-parallel-conflicts</code>|<br />
<code>&#8211;W[n]p</code>] </p>
<p> <i>Target M680X0 options:</i><br />
[<code>-l</code>]&nbsp;<wbr>[<code>-m68000</code>|<code>-m68010</code>|<code>-m68020</code>|&#8230;] </p>
<p> <i>Target M68HC11 options:</i><br />
[<code>-m68hc11</code>|<code>-m68hc12</code>|<code>-m68hcs12</code>]<br />
[<code>-mshort</code>|<code>-mlong</code>]<br />
[<code>-mshort-double</code>|<code>-mlong-double</code>]<br />
[<code>&#8211;force-long-branches</code>]&nbsp;<wbr>[<code>&#8211;short-branches</code>]<br />
[<code>&#8211;strict-direct-mode</code>]&nbsp;<wbr>[<code>&#8211;print-insn-syntax</code>]<br />
[<code>&#8211;print-opcodes</code>]&nbsp;<wbr>[<code>&#8211;generate-example</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MCORE</i></font><i> options:</i><br />
[<code>-jsri2bsr</code>]&nbsp;<wbr>[<code>-sifilter</code>]&nbsp;<wbr>[<code>-relax</code>]<br />
[<code>-mcpu=[210|340]</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MIPS</i></font><i> options:</i><br />
[<code>-nocpp</code>]&nbsp;<wbr>[<code>-EL</code>]&nbsp;<wbr>[<code>-EB</code>]&nbsp;<wbr>[<code>-O</code>[<i>optimization level</i>]]<br />
[<code>-g</code>[<i>debug level</i>]]&nbsp;<wbr>[<code>-G</code>&nbsp;<wbr><i>num</i>]&nbsp;<wbr>[<code>-KPIC</code>]&nbsp;<wbr>[<code>-call_shared</code>]<br />
[<code>-non_shared</code>]&nbsp;<wbr>[<code>-xgot</code>&nbsp;<wbr>[<code>-mvxworks-pic</code>]<br />
[<code>-mabi</code>=<i></i><font SIZE="-1"><i>ABI</i></font><i></i>]&nbsp;<wbr>[<code>-32</code>]&nbsp;<wbr>[<code>-n32</code>]&nbsp;<wbr>[<code>-64</code>]&nbsp;<wbr>[<code>-mfp32</code>]&nbsp;<wbr>[<code>-mgp32</code>]<br />
[<code>-march</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;<wbr>[<code>-mtune</code>=<i></i><font SIZE="-1"><i>CPU</i></font><i></i>]&nbsp;<wbr>[<code>-mips1</code>]&nbsp;<wbr>[<code>-mips2</code>]<br />
[<code>-mips3</code>]&nbsp;<wbr>[<code>-mips4</code>]&nbsp;<wbr>[<code>-mips5</code>]&nbsp;<wbr>[<code>-mips32</code>]&nbsp;<wbr>[<code>-mips32r2</code>]<br />
[<code>-mips64</code>]&nbsp;<wbr>[<code>-mips64r2</code>]<br />
[<code>-construct-floats</code>]&nbsp;<wbr>[<code>-no-construct-floats</code>]<br />
[<code>-trap</code>]&nbsp;<wbr>[<code>-no-break</code>]&nbsp;<wbr>[<code>-break</code>]&nbsp;<wbr>[<code>-no-trap</code>]<br />
[<code>-mfix7000</code>]&nbsp;<wbr>[<code>-mno-fix7000</code>]<br />
[<code>-mips16</code>]&nbsp;<wbr>[<code>-no-mips16</code>]<br />
[<code>-msmartmips</code>]&nbsp;<wbr>[<code>-mno-smartmips</code>]<br />
[<code>-mips3d</code>]&nbsp;<wbr>[<code>-no-mips3d</code>]<br />
[<code>-mdmx</code>]&nbsp;<wbr>[<code>-no-mdmx</code>]<br />
[<code>-mdsp</code>]&nbsp;<wbr>[<code>-mno-dsp</code>]<br />
[<code>-mdspr2</code>]&nbsp;<wbr>[<code>-mno-dspr2</code>]<br />
[<code>-mmt</code>]&nbsp;<wbr>[<code>-mno-mt</code>]<br />
[<code>-mdebug</code>]&nbsp;<wbr>[<code>-no-mdebug</code>]<br />
[<code>-mpdr</code>]&nbsp;<wbr>[<code>-mno-pdr</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>MMIX</i></font><i> options:</i><br />
[<code>&#8211;fixed-special-register-names</code>]&nbsp;<wbr>[<code>&#8211;globalize-symbols</code>]<br />
[<code>&#8211;gnu-syntax</code>]&nbsp;<wbr>[<code>&#8211;relax</code>]&nbsp;<wbr>[<code>&#8211;no-predefined-symbols</code>]<br />
[<code>&#8211;no-expand</code>]&nbsp;<wbr>[<code>&#8211;no-merge-gregs</code>]&nbsp;<wbr>[<code>-x</code>]<br />
[<code>&#8211;linker-allocated-gregs</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>PDP11</i></font><i> options:</i><br />
[<code>-mpic</code>|<code>-mno-pic</code>]&nbsp;<wbr>[<code>-mall</code>]&nbsp;<wbr>[<code>-mno-extensions</code>]<br />
[<code>-m</code><i>extension</i>|<code>-mno-</code><i>extension</i>]<br />
[<code>-m</code><i>cpu</i>]&nbsp;<wbr>[<code>-m</code><i>machine</i>]&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <i>Target picoJava options:</i><br />
[<code>-mb</code>|<code>-me</code>] </p>
<p> <i>Target PowerPC options:</i><br />
[<code>-mpwrx</code>|<code>-mpwr2</code>|<code>-mpwr</code>|<code>-m601</code>|<code>-mppc</code>|<code>-mppc32</code>|<code>-m603</code>|<code>-m604</code>|<br />
&nbsp;<wbr><code>-m403</code>|<code>-m405</code>|<code>-mppc64</code>|<code>-m620</code>|<code>-mppc64bridge</code>|<code>-mbooke</code>|<br />
&nbsp;<wbr><code>-mbooke32</code>|<code>-mbooke64</code>]<br />
[<code>-mcom</code>|<code>-many</code>|<code>-maltivec</code>|<code>-mvsx</code>]&nbsp;<wbr>[<code>-memb</code>]<br />
[<code>-mregnames</code>|<code>-mno-regnames</code>]<br />
[<code>-mrelocatable</code>|<code>-mrelocatable-lib</code>]<br />
[<code>-mlittle</code>|<code>-mlittle-endian</code>|<code>-mbig</code>|<code>-mbig-endian</code>]<br />
[<code>-msolaris</code>|<code>-mno-solaris</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>SPARC</i></font><i> options:</i><br />
[<code>-Av6</code>|<code>-Av7</code>|<code>-Av8</code>|<code>-Asparclet</code>|<code>-Asparclite</code><br />
&nbsp;<wbr><code>-Av8plus</code>|<code>-Av8plusa</code>|<code>-Av9</code>|<code>-Av9a</code>]<br />
[<code>-xarch=v8plus</code>|<code>-xarch=v8plusa</code>]&nbsp;<wbr>[<code>-bump</code>]<br />
[<code>-32</code>|<code>-64</code>] </p>
<p> <i>Target </i><font SIZE="-1"><i>TIC54X</i></font><i> options:</i><br />
&nbsp;<wbr>[<code>-mcpu=54[123589]</code>|<code>-mcpu=54[56]lp</code>]&nbsp;<wbr>[<code>-mfar-mode</code>|<code>-mf</code>]&nbsp;<wbr><br />
&nbsp;<wbr>[<code>-merrors-to-file</code>&nbsp;<wbr><i>&lt;filename&gt;</i>|<code>-me</code>&nbsp;<wbr><i>&lt;filename&gt;</i>] </p>
<p> <i>Target Z80 options:</i><br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-z80</code>]&nbsp;<wbr>[<code>-r800</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-ignore-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Wnud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-ignore-unportable-instructions</code>]&nbsp;<wbr>[<code>-Wnup</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-warn-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Wud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-warn-unportable-instructions</code>]&nbsp;<wbr>[<code>-Wup</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-forbid-undocumented-instructions</code>]&nbsp;<wbr>[<code>-Fud</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>-forbid-unportable-instructions</code>]&nbsp;<wbr>[<code>-Fup</code>] </p>
<p> <i>Target Xtensa options:</i><br />
&nbsp;<wbr>[<code>&#8211;[no-]text-section-literals</code>]&nbsp;<wbr>[<code>&#8211;[no-]absolute-literals</code>]<br />
&nbsp;<wbr>[<code>&#8211;[no-]target-align</code>]&nbsp;<wbr>[<code>&#8211;[no-]longcalls</code>]<br />
&nbsp;<wbr>[<code>&#8211;[no-]transform</code>]<br />
&nbsp;<wbr>[<code>&#8211;rename-section</code>&nbsp;<wbr><i>oldname</i>=<i>newname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">GNU</font> <code>as</code> is really a family of assemblers. If you use (or have used) the <font SIZE="-1">GNU</font> assembler on one architecture, you should find a fairly similar environment when you use it on another architecture. Each version has much in common with the others, including object file formats, most assembler directives (often called <i>pseudo-ops</i>) and assembler syntax. </p>
<p> <code>as</code> is primarily intended to assemble the output of the <font SIZE="-1">GNU</font> C compiler <tt>&quot;gcc&quot;</tt> for use by the linker <tt>&quot;ld&quot;</tt>. Nevertheless, we&#8217;ve tried to make <code>as</code> assemble correctly everything that other assemblers for the same machine would assemble. Any exceptions are documented explicitly. This doesn&#8217;t mean <code>as</code> always uses the same syntax as another assembler for the same architecture; for example, we know of several incompatible versions of 680&#215;0 assembly language syntax. </p>
<p> Each time you run <code>as</code> it assembles exactly one source program. The source program is made up of one or more files. (The standard input is also a file.) </p>
<p> You give <code>as</code> a command line that has zero or more input file names. The input files are read (from left file name to right). A command line argument (in any position) that has no special meaning is taken to be an input file name. </p>
<p> If you give <code>as</code> no file names it attempts to read one input file from the <code>as</code> standard input, which is normally your terminal. You may have to type <code>ctl-D</code> to tell <code>as</code> there is no more program to assemble. </p>
<p> Use <code>&#8212;</code> if you need to explicitly name the standard input file in your command line. </p>
<p> If the source is empty, <code>as</code> produces a small, empty object file. </p>
<p> <code>as</code> may write warnings and error messages to the standard error file (usually your terminal). This should not happen when a compiler runs <code>as</code> automatically. Warnings report an assumption made so that <code>as</code> could keep assembling a flawed program; errors report a grave problem that stops the assembly. </p>
<p> If you are invoking <code>as</code> via the <font SIZE="-1">GNU</font> C compiler, you can use the <code>-Wa</code> option to pass arguments through to the assembler. The assembler arguments must be separated from each other (and the <code>-Wa</code>) by commas. For example: </p>
<pre>
        gcc -c -g -O -Wa,-alh,-L file.c
</pre>
<p> This passes two options to the assembler: <code>-alh</code> (emit a listing to standard output with high-level and assembly source) and <code>-L</code> (retain local symbols in the symbol table). </p>
<p> Usually you do not need to use this <code>-Wa</code> mechanism, since many compiler command-line options are automatically passed to the assembler by the compiler. (You can call the <font SIZE="-1">GNU</font> compiler driver with the <code>-v</code> option to see precisely what options it passes to each compilation pass, including the assembler.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</p>
<dt><code>-a[cdghlmns]</code></p>
<dd> Turn on listings, in any of a variety of ways:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-ac</code></p>
<dd> omit false conditionals</p>
<dt><code>-ad</code></p>
<dd> omit debugging directives</p>
<dt><code>-ag</code></p>
<dd> include general information, like as version and options passed</p>
<dt><code>-ah</code></p>
<dd> include high-level source</p>
<dt><code>-al</code></p>
<dd> include assembly</p>
<dt><code>-am</code></p>
<dd> include macro expansions</p>
<dt><code>-an</code></p>
<dd> omit forms processing</p>
<dt><code>-as</code></p>
<dd> include symbols</p>
<dt><code>=file</code></p>
<dd> set the name of the listing file</dl>
</dl>
<dl>
<dt>
<dd>
<p> You may combine these options; for example, use <code>-aln</code> for assembly listing without forms processing. The <code>=file</code> option, if used, must be the last one. By itself, <code>-a</code> defaults to <code>-ahls</code>.</dl>
<dt><code>&#8211;alternate</code></p>
<dd> Begin in alternate macro mode.</p>
<dt><code>-D</code></p>
<dd> Ignored. This option is accepted for script compatibility with calls to other assemblers.</p>
<dt><code>&#8211;debug-prefix-map</code> <i>old</i><code>=</code><i>new</i></p>
<dd> When assembling files in directory <i>old</i>, record debugging information describing them as in <i>new</i> instead.</p>
<dt><code>&#8211;defsym</code> <i>sym</i><code>=</code><i>value</i></p>
<dd> Define the symbol <i>sym</i> to be <i>value</i> before assembling the input file. <i>value</i> must be an integer constant. As in C, a leading <code>0x</code> indicates a hexadecimal value, and a leading <code>0</code> indicates an octal value. The value of the symbol can be overridden inside a source file via the use of a <tt>&quot;.set&quot;</tt> pseudo-op.</p>
<dt><code>-f</code></p>
<dd> &#8220;fast&#8221;&#8212;skip whitespace and comment preprocessing (assume source is compiler output).</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;gen-debug</code></p>
<dd> Generate debugging information for each assembler source line using whichever debug format is preferred by the target. This currently means either <font SIZE="-1">STABS</font>, <font SIZE="-1">ECOFF</font> or <font SIZE="-1">DWARF2</font>.</p>
<dt><code>&#8211;gstabs</code></p>
<dd> Generate stabs debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.</p>
<dt><code>&#8211;gstabs+</code></p>
<dd> Generate stabs debugging information for each assembler line, with <font SIZE="-1">GNU</font> extensions that probably only gdb can handle, and that could make other debuggers crash or refuse to read your program. This may help debugging assembler code. Currently the only <font SIZE="-1">GNU</font> extension is the location of the current working directory at assembling time.</p>
<dt><code>&#8211;gdwarf-2</code></p>
<dd> Generate <font SIZE="-1">DWARF2</font> debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it. Note&#8212;this option is only supported by some targets, not all of them.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a summary of the command line options and exit.</p>
<dt><code>&#8211;target-help</code></p>
<dd> Print a summary of all target specific options and exit.</p>
<dt><code>-I</code> <i>dir</i></p>
<dd> Add directory <i>dir</i> to the search list for <tt>&quot;.include&quot;</tt> directives.</p>
<dt><code>-J</code></p>
<dd> Don&#8217;t warn about signed overflow.</p>
<dt><code>-K</code></p>
<dd> Issue warnings when difference tables altered for long displacements.</p>
<dt><code>-L</code></p>
<dd>
<dt><code>&#8211;keep-locals</code></p>
<dd> Keep (in the symbol table) local symbols. These symbols start with system-specific local label prefixes, typically <code>.L</code> for <font SIZE="-1">ELF</font> systems or <code>L</code> for traditional a.out systems.</p>
<dt><code>&#8211;listing-lhs-width=</code><i>number</i></p>
<dd> Set the maximum width, in words, of the output data column for an assembler listing to <i>number</i>.</p>
<dt><code>&#8211;listing-lhs-width2=</code><i>number</i></p>
<dd> Set the maximum width, in words, of the output data column for continuation lines in an assembler listing to <i>number</i>.</p>
<dt><code>&#8211;listing-rhs-width=</code><i>number</i></p>
<dd> Set the maximum width of an input source line, as displayed in a listing, to <i>number</i> bytes.</p>
<dt><code>&#8211;listing-cont-lines=</code><i>number</i></p>
<dd> Set the maximum number of lines printed in a listing for a single line of input to <i>number</i> + 1.</p>
<dt><code>-o</code> <i>objfile</i></p>
<dd> Name the object-file output from <code>as</code> <i>objfile</i>.</p>
<dt><code>-R</code></p>
<dd> Fold the data section into the text section. </p>
<p> Set the default size of <font SIZE="-1">GAS</font>&#8216;s hash tables to a prime number close to <i>number</i>. Increasing this value can reduce the length of time it takes the assembler to perform its tasks, at the expense of increasing the assembler&#8217;s memory requirements. Similarly reducing this value can reduce the memory requirements at the expense of speed.</p>
<dt><code>&#8211;reduce-memory-overheads</code></p>
<dd> This option reduces <font SIZE="-1">GAS</font>&#8216;s memory requirements, at the expense of making the assembly processes slower. Currently this switch is a synonym for <code>&#8211;hash-size=4051</code>, but in the future it may have other effects as well.</p>
<dt><code>&#8211;statistics</code></p>
<dd> Print the maximum space (in bytes) and total time (in seconds) used by assembly.</p>
<dt><code>&#8211;strip-local-absolute</code></p>
<dd> Remove local absolute symbols from the outgoing symbol table.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>-version</code></p>
<dd> Print the <code>as</code> version.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the <code>as</code> version and exit.</p>
<dt><code>-W</code></p>
<dd>
<dt><code>&#8211;no-warn</code></p>
<dd> Suppress warning messages.</p>
<dt><code>&#8211;fatal-warnings</code></p>
<dd> Treat warnings as errors.</p>
<dt><code>&#8211;warn</code></p>
<dd> Don&#8217;t suppress warning messages or treat them as errors.</p>
<dt><code>-w</code></p>
<dd> Ignored.</p>
<dt><code>-x</code></p>
<dd> Ignored.</p>
<dt><code>-Z</code></p>
<dd> Generate an object file even after errors.</p>
<dt><code>&#8212; |</code> <i>files</i> <code>&#8230;</code></p>
<dd> Standard input, or source files to assemble.</dl>
<p> The following options are available when as is configured for an <font SIZE="-1">ARC</font> processor.</p>
<dl>
<dt><code>-marc[5|6|7|8]</code></p>
<dd> This option selects the core processor variant.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select either big-endian (-EB) or little-endian (-EL) output.</dl>
<p> The following options are available when as is configured for the <font SIZE="-1">ARM</font> processor family.</p>
<dl>
<dt><code>-mcpu=</code><i>processor</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> Specify which <font SIZE="-1">ARM</font> processor variant is the target.</p>
<dt><code>-march=</code><i>architecture</i><code>[+</code><i>extension</i><code>&#8230;]</code></p>
<dd> Specify which <font SIZE="-1">ARM</font> architecture variant is used by the target.</p>
<dt><code>-mfpu=</code><i>floating-point-format</i></p>
<dd> Select which Floating Point architecture is the target.</p>
<dt><code>-mfloat-abi=</code><i>abi</i></p>
<dd> Select which floating point <font SIZE="-1">ABI</font> is in use.</p>
<dt><code>-mthumb</code></p>
<dd> Enable Thumb only instruction decoding.</p>
<dt><code>-mapcs-32 | -mapcs-26 | -mapcs-float | -mapcs-reentrant</code></p>
<dd> Select which procedure calling convention is in use.</p>
<dt><code>-EB | -EL</code></p>
<dd> Select either big-endian (-EB) or little-endian (-EL) output.</p>
<dt><code>-mthumb-interwork</code></p>
<dd> Specify that the code has been generated with interworking between Thumb and <font SIZE="-1">ARM</font> code in mind.</p>
<dt><code>-k</code></p>
<dd> Specify that <font SIZE="-1">PIC</font> code has been generated.</dl>
<p> See the info pages for documentation of the CRIS-specific options. </p>
<p> The following options are available when as is configured for a D10V processor.</p>
<dl>
<dt><code>-O</code></p>
<dd> Optimize output by parallelizing instructions.</dl>
<p> The following options are available when as is configured for a D30V processor.</p>
<dl>
<dt><code>-O</code></p>
<dd> Optimize output by parallelizing instructions.</p>
<dt><code>-n</code></p>
<dd> Warn when nops are generated.</p>
<dt><code>-N</code></p>
<dd> Warn when a nop after a 32-bit multiply instruction is generated.</dl>
<p> The following options are available when as is configured for the Intel 80960 processor.</p>
<dl>
<dt><code>-ACA | -ACA_A | -ACB | -ACC | -AKA | -AKB | -AKC | -AMC</code></p>
<dd> Specify which variant of the 960 architecture is the target.</p>
<dt><code>-b</code></p>
<dd> Add code to collect statistics about branches taken.</p>
<dt><code>-no-relax</code></p>
<dd> Do not alter compare-and-branch instructions for long displacements; error if necessary.</dl>
<p> The following options are available when as is configured for the Ubicom <font SIZE="-1">IP2K</font> series.</p>
<dl>
<dt><code>-mip2022ext</code></p>
<dd> Specifies that the extended <font SIZE="-1">IP2022</font> instructions are allowed.</p>
<dt><code>-mip2022</code></p>
<dd> Restores the default behaviour, which restricts the permitted instructions to just the basic <font SIZE="-1">IP2022</font> ones.</dl>
<p> The following options are available when as is configured for the Renesas M32C and M16C processors.</p>
<dl>
<dt><code>-m32c</code></p>
<dd> Assemble M32C instructions.</p>
<dt><code>-m16c</code></p>
<dd> Assemble M16C instructions (the default).</p>
<dt><code>-relax</code></p>
<dd> Enable support for link-time relaxations.</p>
<dt><code>-h-tick-hex</code></p>
<dd> Support H&#8217;00 style hex constants in addition to 0x00 style.</dl>
<p> The following options are available when as is configured for the Renesas M32R (formerly Mitsubishi M32R) series.</p>
<dl>
<dt><code>&#8211;m32rx</code></p>
<dd> Specify which processor in the M32R family is the target. The default is normally the M32R, but this option changes it to the M32RX.</p>
<dt><code>&#8211;warn-explicit-parallel-conflicts or &#8211;Wp</code></p>
<dd> Produce warning messages when questionable parallel constructs are encountered.</p>
<dt><code>&#8211;no-warn-explicit-parallel-conflicts or &#8211;Wnp</code></p>
<dd> Do not produce warning messages when questionable parallel constructs are encountered.</dl>
<p> The following options are available when as is configured for the Motorola 68000 series.</p>
<dl>
<dt><code>-l</code></p>
<dd> Shorten references to undefined symbols, to one word instead of two.</p>
<dt><code>-m68000 | -m68008 | -m68010 | -m68020 | -m68030</code></p>
<dd>
<dt><code>| -m68040 | -m68060 | -m68302 | -m68331 | -m68332</code></p>
<dd>
<dt><code>| -m68333 | -m68340 | -mcpu32 | -m5200</code></p>
<dd> Specify what processor in the 68000 family is the target. The default is normally the 68020, but this can be changed at configuration time.</p>
<dt><code>-m68881 | -m68882 | -mno-68881 | -mno-68882</code></p>
<dd> The target machine does (or does not) have a floating-point coprocessor. The default is to assume a coprocessor for 68020, 68030, and cpu32. Although the basic 68000 is not compatible with the 68881, a combination of the two can be specified, since it&#8217;s possible to do emulation of the coprocessor instructions with the main processor.</p>
<dt><code>-m68851 | -mno-68851</code></p>
<dd> The target machine does (or does not) have a memory-management unit coprocessor. The default is to assume an <font SIZE="-1">MMU</font> for 68020 and up.</dl>
<p> For details about the <font SIZE="-1">PDP-11</font> machine dependent features options, see <code>PDP-11-Options</code>.</p>
<dl>
<dt><code>-mpic | -mno-pic</code></p>
<dd> Generate position-independent (or position-dependent) code. The default is <code>-mpic</code>.</p>
<dt><code>-mall</code></p>
<dd>
<dt><code>-mall-extensions</code></p>
<dd> Enable all instruction set extensions. This is the default.</p>
<dt><code>-mno-extensions</code></p>
<dd> Disable all instruction set extensions.</p>
<dt><code>-m</code><i>extension</i> <code>| -mno-</code><i>extension</i></p>
<dd> Enable (or disable) a particular instruction set extension.</p>
<dt><code>-m</code><i>cpu</i></p>
<dd> Enable the instruction set extensions supported by a particular <font SIZE="-1">CPU</font>, and disable all other extensions.</p>
<dt><code>-m</code><i>machine</i></p>
<dd> Enable the instruction set extensions supported by a particular machine model, and disable all other extensions.</dl>
<p> The following options are available when as is configured for a picoJava processor.</p>
<dl>
<dt><code>-mb</code></p>
<dd> Generate &#8220;big endian&#8221; format output.</p>
<dt><code>-ml</code></p>
<dd> Generate &#8220;little endian&#8221; format output.</dl>
<p> The following options are available when as is configured for the Motorola 68HC11 or 68HC12 series.</p>
<dl>
<dt><code>-m68hc11 | -m68hc12 | -m68hcs12</code></p>
<dd> Specify what processor is the target. The default is defined by the configuration option when building the assembler.</p>
<dt><code>-mshort</code></p>
<dd> Specify to use the 16-bit integer <font SIZE="-1">ABI</font>.</p>
<dt><code>-mlong</code></p>
<dd> Specify to use the 32-bit integer <font SIZE="-1">ABI</font>.</p>
<dt><code>-mshort-double</code></p>
<dd> Specify to use the 32-bit double <font SIZE="-1">ABI</font>.</p>
<dt><code>-mlong-double</code></p>
<dd> Specify to use the 64-bit double <font SIZE="-1">ABI</font>.</p>
<dt><code>&#8211;force-long-branches</code></p>
<dd> Relative branches are turned into absolute ones. This concerns conditional branches, unconditional branches and branches to a sub routine.</p>
<dt><code>-S | &#8211;short-branches</code></p>
<dd> Do not turn relative branches into absolute ones when the offset is out of range.</p>
<dt><code>&#8211;strict-direct-mode</code></p>
<dd> Do not turn the direct addressing mode into extended addressing mode when the instruction does not support direct addressing mode.</p>
<dt><code>&#8211;print-insn-syntax</code></p>
<dd> Print the syntax of instruction in case of error.</p>
<dt><code>&#8211;print-opcodes</code></p>
<dd> print the list of instructions with syntax and then exit.</p>
<dt><code>&#8211;generate-example</code></p>
<dd> print an example of instruction for each possible instruction and then exit. This option is only useful for testing <code>as</code>.</dl>
<p> The following options are available when <code>as</code> is configured for the <font SIZE="-1">SPARC</font> architecture:</p>
<dl>
<dt><code>-Av6 | -Av7 | -Av8 | -Asparclet | -Asparclite</code></p>
<dd>
<dt><code>-Av8plus | -Av8plusa | -Av9 | -Av9a</code></p>
<dd> Explicitly select a variant of the <font SIZE="-1">SPARC</font> architecture. </p>
<p> <code>-Av8plus</code> and <code>-Av8plusa</code> select a 32 bit environment. <code>-Av9</code> and <code>-Av9a</code> select a 64 bit environment. </p>
<p> <code>-Av8plusa</code> and <code>-Av9a</code> enable the <font SIZE="-1">SPARC</font> V9 instruction set with UltraSPARC extensions.</p>
<dt><code>-xarch=v8plus | -xarch=v8plusa</code></p>
<dd> For compatibility with the Solaris v9 assembler. These options are equivalent to -Av8plus and -Av8plusa, respectively.</p>
<dt><code>-bump</code></p>
<dd> Warn when the assembler switches to another architecture.</dl>
<p> The following options are available when as is configured for the &#8216;c54x architecture.</p>
<dl>
<dt><code>-mfar-mode</code></p>
<dd> Enable extended addressing mode. All addresses and relocations will assume extended addressing (usually 23 bits).</p>
<dt><code>-mcpu=</code><i></i><font SIZE="-1"><i>CPU_VERSION</i></font><i></i></p>
<dd> Sets the <font SIZE="-1">CPU</font> version being compiled for.</p>
<dt><code>-merrors-to-file</code> <i></i><font SIZE="-1"><i>FILENAME</i></font><i></i></p>
<dd> Redirect error output to a file, for broken systems which don&#8217;t support such behaviour in the shell.</dl>
<p> The following options are available when as is configured for a <font SIZE="-1">MIPS</font> processor.</p>
<dl>
<dt><code>-G</code> <i>num</i></p>
<dd> This option sets the largest size of an object that can be referenced implicitly with the <tt>&quot;gp&quot;</tt> register. It is only accepted for targets that use <font SIZE="-1">ECOFF</font> format, such as a DECstation running Ultrix. The default value is 8.</p>
<dt><code>-EB</code></p>
<dd> Generate &#8220;big endian&#8221; format output.</p>
<dt><code>-EL</code></p>
<dd> Generate &#8220;little endian&#8221; format output.</p>
<dt><code>-mips1</code></p>
<dd>
<dt><code>-mips2</code></p>
<dd>
<dt><code>-mips3</code></p>
<dd>
<dt><code>-mips4</code></p>
<dd>
<dt><code>-mips5</code></p>
<dd>
<dt><code>-mips32</code></p>
<dd>
<dt><code>-mips32r2</code></p>
<dd>
<dt><code>-mips64</code></p>
<dd>
<dt><code>-mips64r2</code></p>
<dd> Generate code for a particular <font SIZE="-1">MIPS</font> Instruction Set Architecture level. <code>-mips1</code> is an alias for <code>-march=r3000</code>, <code>-mips2</code> is an alias for <code>-march=r6000</code>, <code>-mips3</code> is an alias for <code>-march=r4000</code> and <code>-mips4</code> is an alias for <code>-march=r8000</code>. <code>-mips5</code>, <code>-mips32</code>, <code>-mips32r2</code>, <code>-mips64</code>, and <code>-mips64r2</code> correspond to generic <font SIZE="-1"><code>MIPS</code></font><code> V</code>, <font SIZE="-1"><code>MIPS32</code></font>, <font SIZE="-1"><code>MIPS32</code></font><code> Release 2</code>, <font SIZE="-1"><code>MIPS64</code></font>, and <font SIZE="-1"><code>MIPS64</code></font><code> Release 2</code> <font SIZE="-1">ISA</font> processors, respectively.</p>
<dt><code>-march=</code><i></i><font SIZE="-1"><i>CPU</i></font><i></i></p>
<dd> Generate code for a particular <font SIZE="-1">MIPS</font> cpu.</p>
<dt><code>-mtune=</code><i>cpu</i></p>
<dd> Schedule and tune for a particular <font SIZE="-1">MIPS</font> cpu.</p>
<dt><code>-mfix7000</code></p>
<dd>
<dt><code>-mno-fix7000</code></p>
<dd> Cause nops to be inserted if the read of the destination register of an mfhi or mflo instruction occurs in the following two instructions.</p>
<dt><code>-mdebug</code></p>
<dd>
<dt><code>-no-mdebug</code></p>
<dd> Cause stabs-style debugging output to go into an ECOFF-style .mdebug section instead of the standard <font SIZE="-1">ELF</font> .stabs sections.</p>
<dt><code>-mpdr</code></p>
<dd>
<dt><code>-mno-pdr</code></p>
<dd> Control generation of <tt>&quot;.pdr&quot;</tt> sections.</p>
<dt><code>-mgp32</code></p>
<dd>
<dt><code>-mfp32</code></p>
<dd> The register sizes are normally inferred from the <font SIZE="-1">ISA</font> and <font SIZE="-1">ABI</font>, but these flags force a certain group of registers to be treated as 32 bits wide at all times. <code>-mgp32</code> controls the size of general-purpose registers and <code>-mfp32</code> controls the size of floating-point registers.</p>
<dt><code>-mips16</code></p>
<dd>
<dt><code>-no-mips16</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS</font> 16 processor. This is equivalent to putting <tt>&quot;.set mips16&quot;</tt> at the start of the assembly file. <code>-no-mips16</code> turns off this option.</p>
<dt><code>-msmartmips</code></p>
<dd>
<dt><code>-mno-smartmips</code></p>
<dd> Enables the SmartMIPS extension to the <font SIZE="-1">MIPS32</font> instruction set. This is equivalent to putting <tt>&quot;.set smartmips&quot;</tt> at the start of the assembly file. <code>-mno-smartmips</code> turns off this option.</p>
<dt><code>-mips3d</code></p>
<dd>
<dt><code>-no-mips3d</code></p>
<dd> Generate code for the <font SIZE="-1">MIPS-3D</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MIPS-3D</font> instructions. <code>-no-mips3d</code> turns off this option.</p>
<dt><code>-mdmx</code></p>
<dd>
<dt><code>-no-mdmx</code></p>
<dd> Generate code for the <font SIZE="-1">MDMX</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MDMX</font> instructions. <code>-no-mdmx</code> turns off this option.</p>
<dt><code>-mdsp</code></p>
<dd>
<dt><code>-mno-dsp</code></p>
<dd> Generate code for the <font SIZE="-1">DSP</font> Release 1 Application Specific Extension. This tells the assembler to accept <font SIZE="-1">DSP</font> Release 1 instructions. <code>-mno-dsp</code> turns off this option.</p>
<dt><code>-mdspr2</code></p>
<dd>
<dt><code>-mno-dspr2</code></p>
<dd> Generate code for the <font SIZE="-1">DSP</font> Release 2 Application Specific Extension. This option implies -mdsp. This tells the assembler to accept <font SIZE="-1">DSP</font> Release 2 instructions. <code>-mno-dspr2</code> turns off this option.</p>
<dt><code>-mmt</code></p>
<dd>
<dt><code>-mno-mt</code></p>
<dd> Generate code for the <font SIZE="-1">MT</font> Application Specific Extension. This tells the assembler to accept <font SIZE="-1">MT</font> instructions. <code>-mno-mt</code> turns off this option.</p>
<dt><code>&#8211;construct-floats</code></p>
<dd>
<dt><code>&#8211;no-construct-floats</code></p>
<dd> The <code>&#8211;no-construct-floats</code> option disables the construction of double width floating point constants by loading the two halves of the value into the two single width floating point registers that make up the double width register. By default <code>&#8211;construct-floats</code> is selected, allowing construction of these floating point constants.</p>
<dt><code>&#8211;emulation=</code><i>name</i></p>
<dd> This option causes <code>as</code> to emulate <code>as</code> configured for some other target, in all respects, including output format (choosing between <font SIZE="-1">ELF</font> and <font SIZE="-1">ECOFF</font> only), handling of pseudo-opcodes which may generate debugging information or store symbol table information, and default endianness. The available configuration names are: <code>mipsecoff</code>, <code>mipself</code>, <code>mipslecoff</code>, <code>mipsbecoff</code>, <code>mipslelf</code>, <code>mipsbelf</code>. The first two do not alter the default endianness from that of the primary target for which the assembler was configured; the others change the default to little- or big-endian as indicated by the <code>b</code> or <code>l</code> in the name. Using <code>-EB</code> or <code>-EL</code> will override the endianness selection in any case. </p>
<p> This option is currently supported only when the primary target <code>as</code> is configured for is a <font SIZE="-1">MIPS</font> <font SIZE="-1">ELF</font> or <font SIZE="-1">ECOFF</font> target. Furthermore, the primary target or others specified with <code>&#8211;enable-targets=&#8230;</code> at configuration time must include support for the other format, if both are to be available. For example, the Irix 5 configuration includes support for both. </p>
<p> Eventually, this option will support more configurations, with more fine-grained control over the assembler&#8217;s behavior, and will be supported for more processors.</p>
<dt><code>-nocpp</code></p>
<dd> <code>as</code> ignores this option. It is accepted for compatibility with the native tools.</p>
<dt><code>&#8211;trap</code></p>
<dd>
<dt><code>&#8211;no-trap</code></p>
<dd>
<dt><code>&#8211;break</code></p>
<dd>
<dt><code>&#8211;no-break</code></p>
<dd> Control how to deal with multiplication overflow and division by zero. <code>&#8211;trap</code> or <code>&#8211;no-break</code> (which are synonyms) take a trap exception (and only work for Instruction Set Architecture level 2 and higher); <code>&#8211;break</code> or <code>&#8211;no-trap</code> (also synonyms, and the default) take a break exception.</p>
<dt><code>-n</code></p>
<dd> When this option is used, <code>as</code> will issue a warning every time it generates a nop instruction from a macro.</dl>
<p> The following options are available when as is configured for an MCore processor.</p>
<dl>
<dt><code>-jsri2bsr</code></p>
<dd>
<dt><code>-nojsri2bsr</code></p>
<dd> Enable or disable the <font SIZE="-1">JSRI</font> to <font SIZE="-1">BSR</font> transformation. By default this is enabled. The command line option <code>-nojsri2bsr</code> can be used to disable it.</p>
<dt><code>-sifilter</code></p>
<dd>
<dt><code>-nosifilter</code></p>
<dd> Enable or disable the silicon filter behaviour. By default this is disabled. The default can be overridden by the <code>-sifilter</code> command line option.</p>
<dt><code>-relax</code></p>
<dd> Alter jump instructions for long displacements.</p>
<dt><code>-mcpu=[210|340]</code></p>
<dd> Select the cpu type on the target hardware. This controls which instructions can be assembled.</p>
<dt><code>-EB</code></p>
<dd> Assemble for a big endian target.</p>
<dt><code>-EL</code></p>
<dd> Assemble for a little endian target.</dl>
<p> See the info pages for documentation of the MMIX-specific options. </p>
<p> The following options are available when as is configured for an Xtensa processor.</p>
<dl>
<dt><code>&#8211;text-section-literals | &#8211;no-text-section-literals</code></p>
<dd> With <code>&#8211;text-section-literals</code>, literal pools are interspersed in the text section. The default is <code>&#8211;no-text-section-literals</code>, which places literals in a separate section in the output file. These options only affect literals referenced via PC-relative <tt>&quot;L32R&quot;</tt> instructions; literals for absolute mode <tt>&quot;L32R&quot;</tt> instructions are handled separately.</p>
<dt><code>&#8211;absolute-literals | &#8211;no-absolute-literals</code></p>
<dd> Indicate to the assembler whether <tt>&quot;L32R&quot;</tt> instructions use absolute or PC-relative addressing. The default is to assume absolute addressing if the Xtensa processor includes the absolute <tt>&quot;L32R&quot;</tt> addressing option. Otherwise, only the PC-relative <tt>&quot;L32R&quot;</tt> mode can be used.</p>
<dt><code>&#8211;target-align | &#8211;no-target-align</code></p>
<dd> Enable or disable automatic alignment to reduce branch penalties at the expense of some code density. The default is <code>&#8211;target-align</code>.</p>
<dt><code>&#8211;longcalls | &#8211;no-longcalls</code></p>
<dd> Enable or disable transformation of call instructions to allow calls across a greater range of addresses. The default is <code>&#8211;no-longcalls</code>.</p>
<dt><code>&#8211;transform | &#8211;no-transform</code></p>
<dd> Enable or disable all assembler transformations of Xtensa instructions. The default is <code>&#8211;transform</code>; <code>&#8211;no-transform</code> should be used only in the rare cases when the instructions must be exactly as specified in the assembly source.</p>
<dt><code>&#8211;rename-section</code> <i>oldname</i><code>=</code><i>newname</i></p>
<dd> When generating output sections, rename the <i>oldname</i> section to <i>newname</i>.</dl>
<p> The following options are available when as is configured for a Z80 family processor.</p>
<dl>
<dt><code>-z80</code></p>
<dd> Assemble for Z80 processor.</p>
<dt><code>-r800</code></p>
<dd> Assemble for R800 processor.</p>
<dt><code>-ignore-undocumented-instructions</code></p>
<dd>
<dt><code>-Wnud</code></p>
<dd> Assemble undocumented Z80 instructions that also work on R800 without warning.</p>
<dt><code>-ignore-unportable-instructions</code></p>
<dd>
<dt><code>-Wnup</code></p>
<dd> Assemble all undocumented Z80 instructions without warning.</p>
<dt><code>-warn-undocumented-instructions</code></p>
<dd>
<dt><code>-Wud</code></p>
<dd> Issue a warning for undocumented Z80 instructions that also work on R800.</p>
<dt><code>-warn-unportable-instructions</code></p>
<dd>
<dt><code>-Wup</code></p>
<dd> Issue a warning for undocumented Z80 instructions that do not work on R800.</p>
<dt><code>-forbid-undocumented-instructions</code></p>
<dd>
<dt><code>-Fud</code></p>
<dd> Treat all undocumented instructions as errors.</p>
<dt><code>-forbid-unportable-instructions</code></p>
<dd>
<dt><code>-Fup</code></p>
<dd> Treat undocumented Z80 instructions that do not work on R800 as errors.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), and the Info entries for <i>binutils</i> and <i>ld</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 92, 93, 94, 95, 96, 97, 98, 99, 2000, 2001, 2002, 2006, 2007 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
