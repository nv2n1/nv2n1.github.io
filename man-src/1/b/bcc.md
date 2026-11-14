---
title: "bcc(1)"
name: "bcc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcc/"
description: "bcc – Bruce’s C compiler"
---

<h2 class="name">NAME</h2>
<p> bcc &#8211; Bruce&#8217;s C compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>bcc</code> [<code>-03EGNOPSVcegvwxW</code>] [<code>-Aas_option</code>] [<code>-Bexecutable_prefix</code>] [<code>-Ddefine</code>] [<code>-Uundef</code>] [<code>-Mc_mode</code>] [<code>-o outfile</code>] [<code>-ansi</code>] [<code>-Ccc1_option</code>] [<code>-Pcpp_option</code>] [<code>-Iinclude_dir</code>] [<code>-Lld_option</code>] [<code>-Ttmpdir</code>] [<code>-Qc386_option</code>] [<code>-ttext_segno</code>] [<code>ld_options</code>] [<code>infiles</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Bcc</code> is a simple C compiler that produces 8086 assembler, in addition compiler compile time options allow 80386 or 6809 versions. The compiler understands traditional K&amp;R C with just the restriction that bit fields are mapped to one of the other integer types. </p>
<p> The default operation is to produce an 8086 executable called <code>a.out</code> from the source file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ansi</code></p>
<dd> Pass the C source through <code>unprotoize</code> after preprocessing and before code generation. This will allow <i>some</i> ansi C to be compiled but it is definitly <code>NOT</code> a true ansi-C compiler.</p>
<dt><code>-0</code></p>
<dd> 8086 target (works on 80386 host, but not 6809)</p>
<dt><code>-3</code></p>
<dd> 80386 target (may work on 8086 host, but not 6809)</p>
<dt><code>-A</code></p>
<dd> pass remainder of option to assembler (e.g. -A-l -Alistfile for a listing)</p>
<dt><code>-B</code></p>
<dd> prefix for executable search path (as usual; the search order is all paths specified using <code>-B</code>, in order, then the path given in the environment variable <code>BCC_EXEC_PREFIX</code> if that is set, then the compiled-in defaults (something like /usr/lib/bcc/ followed by /usr/bin/)</p>
<dt><code>-C</code></p>
<dd> pass remainder of option to bcc-cc1, see code generation options.</p>
<dt><code>-D</code></p>
<dd> preprocessor define</p>
<dt><code>-E</code></p>
<dd> produce preprocessor output to standard out.</p>
<dt><code>-G</code></p>
<dd> produce GCC objects (Same as -Mg)</p>
<dt><code>-Ixyz</code></p>
<dd> include search &#8216;xyz&#8217; path</p>
<dt><code>-I</code></p>
<dd> don&#8217;t add default include to search list</p>
<dt><code>-Lxyz</code></p>
<dd> add directory name &#8216;xyz&#8217; to the head of the list of library directories searched</p>
<dt><code>-L</code></p>
<dd> don&#8217;t add default library to search list</p>
<dt><code>-Md</code></p>
<dd> alters the arguments for all passes to produce MSDOS executable COM files. These are small model executables, use <code>-i</code> to get tiny model.</p>
<dt><code>-Mf</code></p>
<dd> sets bcc to pass the <code>-c</code> and <code>-f</code> arguments to the code generator for smaller faster code. Note this code is not compatible with the standard calling conventions so a different version of the C library is linked too.</p>
<dt><code>-Mc</code></p>
<dd> sets bcc to pass the <code>-c</code> argument to the code generator for smaller faster code. Note the standard libc is normally transparent to this, but there are exceptions.</p>
<dt><code>-Ms</code></p>
<dd> alters the arguments for all passes and selects C-library to produce standalone Linux-86 executables</p>
<dt><code>-Ml</code></p>
<dd> switches to i386-Linux code generator and library. This configuration accepts the <code>-z</code> flag to generate QMAGIC a.out files instead of the normal OMAGIC.</p>
<dt><code>-Mg</code></p>
<dd> switches to i386-Linux code generator and generates OMAGIC object files that can be linked with some versions of gcc; unfortunatly the most recent versions use &#8216;collect2&#8217; to link and this crashes.</p>
<dt><code>-N</code></p>
<dd> makes the linker produce a native a.out file (Linux OMAGIC) if combined with -3 the executable will run under Linux-i386.</p>
<dt><code>-O</code></p>
<dd> optimize, call <code>copt</code>(<code>1</code>) to optimize 8086 code. Specifiers to choose which rules <code>copt</code> should use can be appended to the <code>-O</code> and the option can be repeated.</p>
<dt><code>-P</code></p>
<dd> produce preprocessor output with no line numbers to standard output.</p>
<dt><code>-Q</code></p>
<dd> pass full option to c386 (Only for c386 version)</p>
<dt><code>-S</code></p>
<dd> produce assembler file</p>
<dt><code>-T</code></p>
<dd> temporary directory (overrides previous value and default; default is from the environment variable TMPDIR if that is set, otherwise /tmp)</p>
<dt><code>-U</code></p>
<dd> preprocessor undefine</p>
<dt><code>-V</code></p>
<dd> print names of files being compiled</p>
<dt><code>-X</code></p>
<dd> pass remainder of option to linker (e.g. -X-Ofile is passed to the linker as -Ofile)</p>
<dt><code>-c</code></p>
<dd> produce object file</p>
<dt><code>-f</code></p>
<dd> turn on floating point support, no effect with i386, changes libc library with 8086 code.</p>
<dt><code>-g</code></p>
<dd> produce debugging info (ignored.)</p>
<dt><code>-o</code></p>
<dd> output file name follows (assembler, object or executable) (as usual)</p>
<dt><code>-p</code></p>
<dd> produce profiling info (ignored.)</p>
<dt><code>-t1</code></p>
<dd> pass to the assembler to renumber the text segment for multi-segment programs.</p>
<dt><code>-v</code></p>
<dd> print names and args of subprocesses being run. Two or more -v&#8217;s print names of files being unlinked. Three or more -v&#8217;s print names of paths being searched.</p>
<dt><code>-w</code></p>
<dd> Supress any warning diagnostics.</p>
<dt><code>-W</code></p>
<dd> Turn <code>on</code> assembler warning messages.</p>
<dt><code>-x</code></p>
<dd> don&#8217;t include crt0.o in the link.</p>
<dt><code>-i</code></p>
<dd> don&#8217;t pass <code>-i</code> to the linker so that it will create an impure executable.</p>
<dt><code>-7</code></p>
<dd> Turn on ancient C mode (see CODE GENERATOR OPTIONS below). Among other things, this disables valuable error checks and even parses certain constructs incompatibly (e.g. <i>=-</i> is postdecrement instead of an assignment of a negative number) to later C standards, so this option should only be used with ancient code. To generate executables for a V7 variant you should tell linker to generate old a.out header with <code>-X-7</code> option.</dl>
<p> Other options are passed to the linker, in particular -lx, -M, -m, -s, -H. </p>
<h2>CODE GENERATOR OPTIONS</h2>
<p> These are all options that the code generator pass <code>bcc-cc1</code> understands, only some will be useful for the <code>-C</code> option of bcc.</p>
<dl>
<dt><code>-0</code></p>
<dd> 8086 target (works even on 80386 host, not on 6809)</p>
<dt><code>-3</code></p>
<dd> 80386 target (may work even on 8086 host, not on 6809)</p>
<dt><code>-D</code></p>
<dd> define (as usual)</p>
<dt><code>-E</code></p>
<dd> produce preprocessor output (as usual)</p>
<dt><code>-I</code></p>
<dd> include search path (as usual)</p>
<dt><code>-P</code></p>
<dd> produce preprocessor output with no line numbers (as usual)</p>
<dt><code>-c</code></p>
<dd> produce code with caller saving regs before function calls</p>
<dt><code>-d</code></p>
<dd> print debugging information in assembly output</p>
<dt><code>-f</code></p>
<dd> produce code with 1st argument passed in a register (AX, EAX or X)</p>
<dt><code>-l</code></p>
<dd> produce code for 2 3 1 0 long byte order (only works in 16-bit code), a special library of compiler helper functions is needed for this mode.</p>
<dt><code>-o</code></p>
<dd> assembler output file name follows</p>
<dt><code>-p</code></p>
<dd> produce (almost) position-independent code (only for the 6809)</p>
<dt><code>-t</code></p>
<dd> print source code in assembly output</p>
<dt><code>-w</code></p>
<dd> print what cc1 thinks is the location counter in assembly output</p>
<dt><code>-7</code></p>
<dd> Accept various obsolete construct for ancient C compilers, including Ritchie&#8217;s Sixth Edition UNIX C compiler and Seventh Edition UNIX Portable C compiler. Enough of these compilers is emulated to compile all of Seventh Edition userspace and kernel.</dl>
<p> All the options except -D, -I and -o may be turned off by following the option letter by a &#8216;-&#8216;. Options are processed left to right so the last setting has precedence. </p>
<h2>PREPROCESSOR DEFINES</h2>
<p> The preprocessor has a number of manifest constants.</p>
<dl>
<dt><code>__BCC__ 1</code></p>
<dd> The compiler identifier, normally used to avoid compiler limitations.</p>
<dt><code>__FILE__</code></p>
<dd> stringized name of current input file</p>
<dt><code>__LINE__</code></p>
<dd> current line number</p>
<dt><code>__MSDOS__ 1</code></p>
<dd> compiler is configured for generating MSDOS executable COM files.</p>
<dt><code>__STANDALONE__ 1</code></p>
<dd> compiler is configured for generating standalone executables.</p>
<dt><code>__AS386_16__ 1</code></p>
<dd> compiler is generating 16 bit 8086 assembler and the <code>#asm</code> keyword is available for including 8086 code.</p>
<dt><code>__AS386_32__ 1</code></p>
<dd> compiler is generating 32 bit 80386 assembler and the <code>#asm</code> keyword is available for including 80386 code.</p>
<dt><code>__CALLER_SAVES__ 1</code></p>
<dd> compiler calling conventions are altered so the calling function must save the <i>SI</i> and <i>DI</i> registers if they are in use (ESI and EDI on the 80386)</p>
<dt><code>__FIRST_ARG_IN_AX__ 1</code></p>
<dd> compiler calling conventions are altered so the calling function is passing the first argument to the function in the <i>AX</i> (or <i>EAX</i> ) register.</p>
<dt><code>__LONG_BIG_ENDIAN__ 1</code></p>
<dd> alters the word order of code generated by the 8086 compiler.</dl>
<p> These defines only occur in the 6809 version of the compiler.</p>
<dl>
<dt><code>__AS09__ 1</code></p>
<dd> compiler is generating 6809 code</p>
<dt><code>__FIRST_ARG_IN_X__ 1</code></p>
<dd> the first argument to functions is passed in the <i>X</i> register.</p>
<dt><code>__POS_INDEPENDENT__ 1</code></p>
<dd> the code generated is (almost) position independent.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>BCC_EXEC_PREFIX</code></p>
<dd> default directory to seach for compiler passes</p>
<dt><code>TMPDIR</code></p>
<dd> directory to place temporary files (default /tmp)</dl>
<h2>DIRECTORIES</h2>
<p> All the include, library and compiler components are stored under the <i>/usr/bcc</i> directory under Linux-i386, this is laid out the same as a <i>/usr</i> filesystem and if bcc is to be the primary compiler on a system it should be moved there. The configuration for this is in the <code>bcc.c</code> source file only, all other executables are independent of location. </p>
<p> The library installation also creates the file <code>/usr/lib/liberror.txt</code>, this path is hardcoded into the C library. </p>
<p> The <code>bcc</code> executable itself, <code>as86</code> and <code>ld86</code> are in /usr/bin. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-as86/">as86</a>(1), <a href="/docs/linux/man/1-ld86/">ld86</a>(1), <a href="/docs/linux/man/1-elksemu/">elksemu</a>(1)</p>
<h2>BUGS</h2>
<p> The bcc.c compiler driver source is very untidy. </p>
<p> The linker, ld86, produces a broken a.out object file if given one input and the <code>-r</code> option this is so it is compatible with pre-dev86 versions. </p>
<h2>Index</h2>
