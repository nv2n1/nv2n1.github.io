---
title: "fpc(1)"
name: "fpc"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fpc/"
description: "fpc – Free Pascal Compiler (FPC) binary"
---

<h2>NAME</h2>
<p> fpc &#8211; Free Pascal Compiler (FPC) binary </p>
<h2>SYNOPSIS</h2>
<p> <code>fpc [options] [sourcefile]</code></p>
<h2>DESCRIPTION</h2>
<p> This binary is the main binary of the <i>Free Pascal Compiler (FPC)</i> which is a <i>Turbo Pascal</i> and <i>Delphi (7.0) </i> compatible standalone (non GCC frontend) multitarget Pascal compiler. </p>
<p> The compiler uses <code><a href="/docs/linux/man/1-ld/">LD</a></code>(1) and can use <code><a href="/docs/linux/man/1-as/">AS</a></code>(1) (see parameter -Aas), but also has its own binary object writer. </p>
<p> The current main targets are <i>Go32V2</i> (Dos DJGPP extender), <i>Freebsd,</i> <i>Linux,</i> <i>MacOS,</i> <i>MacOSX,</i> <i>MorphOS,</i> <i>Netware,</i> <i>OS/2</i> and <i>Win32.</i> The other targets (M68K compilers for Atari and Amiga) are either based on older versions of the compiler or are still in development. </p>
<p> This manpage is meant for quick-reference only. FPC comes with a great (2000+ pages) manual, which is updated constantly, while this man page can be out of date. </p>
<h2>Version number</h2>
<p> Starting with release 1.0, a new versioning system has been implemented. If the last number is even (1.0, 1.0.2), it is stable, and if the last number is odd it is a daily changing development version.(1.0.5, 1.1) just like the linux kernel. </p>
<p> Version 0.99.5 however is a stable release. It was made before the even/odd version naming system was introduced. </p>
<h2>Usage</h2>
<p> The compilation proces is started by typing <i>fpc</i> followed by a sourcefile name (normally with .pas or .pp extension). Before processing the actual processing of the source file, <code>fpc.cfg</code>(5) the configuration file of the compiler is read which contains the location of the RTL, other packages (FCL, FreeVision), and optionally default values for some switches. See the separate manpage of <code>fpc.cfg</code>(5) for more information. </p>
<h2>Options</h2>
<p> General options </p>
<dl>
<dt><code>-h</code></dt>
<dd> if you specify this option, the compiler outputs a list of all options, and exits after that.</dd>
<dt><code>-?</code></dt>
<dd> idem as -h, but waiting after every screenfull for the enter key.</dd>
<dt><code>-i</code></dt>
<dd> This option tells the compiler to print the copyright information. </dd>
<p> You can give it an option, as -ixxx where &quot;xxx&quot; can be one of the following:</p>
<dl>
<dl>
<dt><i>D</i></dt>
<dd> Returns the compiler date.</dd>
<dt><i>V</i></dt>
<dd> Returns the compiler version.</dd>
<dt><i>SO</i></dt>
<dd> Returns the compiler OS.</dd>
<dt><i>SP</i></dt>
<dd> Returns the compiler processor.</dd>
<dt><i>TO</i></dt>
<dd> Returns the target OS.</dd>
<dt><i>TP</i></dt>
<dd> Returns the target Processor.</dd></dl>
</dl>
<dt><i>-l</i></dt>
<dd> This option tells the compiler to print the <i>FPC</i> logo on standard output. It also gives you the <i>FPC</i> version number.</dd>
<dt><i>-n</i></dt>
<dd> Tells the compiler not to read the configuration file <code>fpc.cfg</code>(5) </dd>
</dl>
<p> Options for getting feedback</p>
<dl>
<dt><code>-v</code><i>xxx</i></dt>
<dd> Be verbose. &quot;xxx&quot; is a combination of the following:</dd>
<dl>
<dl>
<dt><i>e</i></dt>
<dd> Tells the compiler to show only errors. This option is on by default.</dd>
<dt><i>i</i></dt>
<dd> Tells the compiler to show some general information.</dd>
<dt><i>w</i></dt>
<dd> Tells the compiler to issue warnings.</dd>
<dt><i>n</i></dt>
<dd> Tells the compiler to issue notes.</dd>
<dt><i>h</i></dt>
<dd> Tells the compiler to issue hints.</dd>
<dt><i>l</i></dt>
<dd> Tells the compiler to show the line numbers as it processes a file. Numbers are shown per 100.</dd>
<dt><i>u</i></dt>
<dd> Tells the compiler to print the names of the files it opens.</dd>
<dt><i>t</i></dt>
<dd> Tells the compiler to print the names of the files it tries to open.</dd>
<dt><i>p</i></dt>
<dd> Tells the compiler to print the names of procedures and functions as it is processing them.</dd>
<dt><i>c</i></dt>
<dd> Tells the compiler to warn you when it processes a conditional.</dd>
<dt><i>m</i></dt>
<dd> Tells the compiler to write which macros are defined.</dd>
<dt><i>d</i></dt>
<dd> Tells the compiler to write other debugging info.</dd>
<dt><i>a</i></dt>
<dd> Tells the compiler to write all possible info. (this is the same as specifying all options)</dd>
<dt><i>0</i></dt>
<dd> Tells the compiler to write no messages. This is useful when you want to override the default setting in the configuration file.</dd>
<dt><i>b</i></dt>
<dd> Tells the compiler to show all procedure declarations if an overloaded function error occurs.</dd>
<dt><i>x</i></dt>
<dd> Tells the compiler to output some executable info (for Win32 platform only).</dd>
<dt><i>r</i></dt>
<dd> Rhide/GCC compatibility mode: formats the error differently, so they are understood by RHIDE.</dd></dl>
</dl>
</dl>
<p> Options concerning files and directories</p>
<dl>
<dt><code>-e</code><i>xxx</i></dt>
<dd> tells the compiler that <i>xxx</i> is the directory where it can find the executables as (the assembler) and ld (the linker).</dd>
<dt><code>-FD</code></dt>
<dd> same as <i>-e.</i></dd>
<dt><code>-Fe</code><i>xxx</i></dt>
<dd> This option tells the compiler to write errors, etc. to the file <i>xxx</i></dd>
<dt><code>-FE</code><i>xxx</i></dt>
<dd> set the executable/unit output path to <i>xxx</i></dd>
<dt><code>-Fi</code><i>xxx</i></dt>
<dd> adds <i>xxx</i> to the path where the compiler searches for its include files.</dd>
<dt><code>-Fl</code><i>xxx</i></dt>
<dd> Adds <i>xxx</i> to the library searching path, and is passe to the linker.</dd>
<dt><code>-FL</code><i>xxx</i></dt>
<dd> ( Linux only) Tells the compiler to use <i>xxx</i> as the dynamic linker. Default this is /lib/ld-linux.so.2, or lib/ld-linux.so.1, depending on which one is found.</dd>
<dt><code>-Fo</code><i>xxx</i></dt>
<dd> Adds <i>xxx</i> to the object file path. This path is used when looking for files that need to be linked in.</dd>
<dt><code>-Fr</code><i>xxx</i></dt>
<dd> tells the compiler that <i>xxx</i> contains the compiler messages. Default the compiler has built-in messages. Specifying this option will override the default messages. (useful if you want to use a language other than the default language).</dd>
<dt><code>-Fu</code><i>xxx</i></dt>
<dd> Adds <i>xxx</i> to the unit path. By default, the compiler only searches for units in the current directory and the directory where the compiler itself resides. This option tells the compiler also to look in the directory <i>xxx</i></dd>
<dt><code>-FU</code><i>xxx</i></dt>
<dd> Tells the compiler to write units in directory <i>xxx</i> instead of the current directory.</dd>
<dt><code>-I</code><i>xxx</i></dt>
<dd> Add <i>xxx</i> to the include file search path. This path is used when looking for include files. </dd>
</dl>
<p> for more information on these options, see also the programmers manual.</p>
<dl>
<dt><code>-a</code></dt>
<dd> Tells the compiler not to delete the assembler file. This also counts for the (possibly) generated batch script.</dd>
<dt><code>-al</code></dt>
<dd> Tells the compiler to include the sourcecode lines in the assembler file as comments.</dd>
<dt><code>-an</code></dt>
<dd> Tells the compiler to include node information in the generated assembler file. This is mainly for use by the compiler developers.</dd>
<dt><code>-ap</code></dt>
<dd> Tells the compiler to use pipes to communicate with the assembler.</dd>
<dt><code>-ar</code></dt>
<dd> Tells the compiler to include register allocation/deallocation information.</dd>
<dt><code>-at</code></dt>
<dd> Tells the compiler to include temparary register allocation/deallocation information.</dd>
<dt><code>-A</code><i>xxx</i></dt>
<dd> specifies what kind of assembler should be generated . Here <i>xxx</i> is one of the following :</dd>
<dl>
<dl>
<dt><i>AS</i></dt>
<dd> A unix .o (object) file, using <i>GNU AS</i></dd>
<dt><i>coff</i></dt>
<dd> coff object file (go32) using internal writer.</dd>
<dt><i>default</i></dt>
<dd> Use the default writer for the current platform.</dd>
<dt><i>elf</i></dt>
<dd> elf object file (linux, 32-bit only) using internal writer.</dd>
<dt><i>nasmcoff</i></dt>
<dd> a coff file using the <i>nasm</i> assembler.</dd>
<dt><i>nasmelf</i></dt>
<dd> a ELF32 file (LINUX only) using the <i>nasm</i> assembler.</dd>
<dt><i>nasmobj</i></dt>
<dd> a obj file using the <i>nasm</i> assembler.</dd>
<dt><i>masm</i></dt>
<dd> An obj file using the Microsoft <i>masm</i> assembler.</dd>
<dt><i>pecoff</i></dt>
<dd> pecoff object file (win32) using internal writer.</dd>
<dt><i>tasm</i></dt>
<dd> An obj file using the Borland <i>tasm</i> assembler.</dd>
<dt><i>wasm</i></dt>
<dd> An obj file using the Watcom assembler.</dd></dl>
</dl>
<dt><code>-Ccxxx</code></dt>
<dd> set the default calling convention to XXX.</dd>
<dt><code>-CD</code></dt>
<dd> Create dynamic library.</dd>
<dt>
</dt><dt><code>-Ce</code></dt>
<dd>
</dd><dd> Compile using emulated floating point instructions.</dd>
<dt><code>-Cfxxx</code></dt>
<dd> Set the used floating point instruction set to xxx.</dd>
<dt><code>-Cg</code></dt>
<dd> Generate PIC code.</dd>
<dt><code>-Ch</code><i>xxx</i></dt>
<dd> Reserves <i>xxx</i> bytes heap. <i>xxx</i> should be between 1024 and 67107840.</dd>
<dt><code>-Ci</code></dt>
<dd> Generate Input/Output checking code.</dd>
<dt><code>-Cn</code></dt>
<dd> Omit the linking stage.</dd>
<dt><code>-Co</code></dt>
<dd> Generate Integer overflow checking code.</dd>
<dt><code>-CR</code></dt>
<dd> Verify object call validity (method calls mustbe valid).</dd>
<dt><code>-Cr</code></dt>
<dd> Generate Range checking code.</dd>
<dt><code>-Cs</code><i>xxx</i></dt>
<dd> Set stack size to <i>xxx</i> bytes.</dd>
<dt><code>-Ct</code></dt>
<dd> generate stack checking code.</dd>
<dt><code>-CX</code></dt>
<dd> Create a smartlinked library.</dd>
<dt><code>-d</code><i>xxx</i></dt>
<dd> Define the symbol name <i>xxx</i> This can be used to conditionally compile parts of your code. </dd>
<dt><code>-E</code></dt>
<dd> Same as -Cn.</dd>
<dt><code>-g</code></dt>
<dd> Generate debugging information for debugging with <i>GDB</i></dd>
<dt><code>-gg</code></dt>
<dd> idem as <code>-g.</code></dd>
<dt><code>-gd</code></dt>
<dd> generate debugging info for dbx.</dd>
<dt><code>-gh</code></dt>
<dd> use the heaptrc unit (see the units part of the FPC manual).</dd>
<dt><code>-gl</code></dt>
<dd> use the lineinfo unit for line information (see the units part of the FPC manual).</dd>
<dt><code>-gv</code></dt>
<dd> Generate information for debugging with valgrind.</dd>
<dt><code>-gw</code></dt>
<dd> Generate DWARF debugging information.</dd>
<dt><code>-O</code><i>xxx</i></dt>
<dd> optimize the compiler&#8217;s output; <i>xxx</i> can have one of the following values :</dd>
<dl>
<dl>
<dt><i>g</i></dt>
<dd> optimize for size, try to generate smaller code.</dd>
<dt><i>G</i></dt>
<dd> optimize for time, try to generate faster code (default).</dd>
<dt><i>r</i></dt>
<dd> keep certain variables in registers (experimental, use with caution).</dd>
<dt><i>u</i></dt>
<dd> uncertain optimizations</dd>
<dt><i>1</i></dt>
<dd> Level 1 optimizations (quick optimizations).</dd>
<dt><i>2</i></dt>
<dd> Level 2 optimizations (-O1 plus some slower optimizations).</dd>
<dt><i>3</i></dt>
<dd> Level 3 optimizations (-O2 plus -Ou).</dd>
<dt><i>pn</i></dt>
<dd> Specify processor : n can be one of</dd>
<dl>
<dl>
<dt><i>1</i></dt>
<dd> optimize for 386/486</dd>
<dt><i>2</i></dt>
<dd> optimize for Pentium/PentiumMMX &#8482;</dd>
<dt><i>3</i></dt>
<dd> optimizations for PentiumPro / P-II / Cyrix 6&#215;86 / K6 &#8482;</dd></dl>
</dl>
<p> The exact effect of these effects can be found in the programmers part of the manual.</dl>
</dl>
<dt><code>-o</code><i>xxx</i></dt>
<dd> Tells the compiler to use <i>xxx</i> as the name of the output file (executable). Only with programs.</dd>
<dt><code>-pg</code></dt>
<dd> Generate profiler code for gprof.</dd>
<dt><code>-s</code></dt>
<dd> Tells the compiler not to call the assembler and linker. Instead, the compiler writes a script, PPAS.BAT under DOS, or ppas.sh under Linux, which can then be executed to produce an executable.</dd>
<dt><code>-sh</code></dt>
<dd> Tells the compiler to generate a script that can be used to assemble and link on the host system, not on the target system. Use this when cross-compiling.</dd>
<dt><code>-sr</code></dt>
<dd> Skip register allocation stage in compiler (use with -ar)</dd>
<dt><code>-st</code></dt>
<dd> Tells the compiler to generate a script that can be used to assemble and link on the target system, not on the host system. Use this when cross-compiling.</dd>
<dt><code>-T</code><i>xxx</i></dt>
<dd> Specifies the target operating system. <i>xxx</i> can be one of the following:</dd>
<dl>
<dl>
<dt><i>EMX</i></dt>
<dd> OS/2 and DOS via the EMX extender.</dd>
<dt><i>FREEBSD</i></dt>
<dd> FreeBSD</dd>
<dt><i>GO32V2</i></dt>
<dd> DOS and version 2 of the DJ DELORIE extender.</dd>
<dt><i>LINUX</i></dt>
<dd> Linux.</dd>
<dt><i>NETBSD</i></dt>
<dd> Netbsd.</dd>
<dt><i>NETWARE</i></dt>
<dd> Novell Netware module (clib)</dd>
<dt><i>NETLIBC</i></dt>
<dd> Novell Netware module (libc)</dd>
<dt><i>OPENBSD</i></dt>
<dd> OpenBSD</dd>
<dt><i>OS2</i></dt>
<dd> OS/2 (native mode)</dd>
<dt><i>SunOS</i></dt>
<dd> Solaris SunOS</dd>
<dt><i>WATCOM</i></dt>
<dd> WatCOM dos extender</dd>
<dt><i>WDOSX</i></dt>
<dd> WDosX Dos extender</dd>
<dt><i>WIN32</i></dt>
<dd> Windows 32 bit.</dd></dl>
</dl>
<dt><code>-u</code><i>xxx</i></dt>
<dd> undefine the symbol <i>xxx</i> if it is defined. This is the opposite of the <code>-d </code> option.</dd>
<dt><code>-X</code><i>x</i></dt>
<dd> Executable options. These tell the compiler what kind of executable should be generated. the parameter <i>x</i> can be one of the following:</dd>
<dl>
<dl>
<dt><i>c</i></dt>
<dd> (Linux only, obsolete) Link with the C library. You should only use this when you start to port Free Pascal to another operating system.</dd>
<dt><i>D</i></dt>
<dd> Link with dynamic libraries (defines the FPC_LINK_DYNAMIC symbol)</dd>
<dt><i>d</i></dt>
<dd> Don&#8217;t use the standard library path. Use this when cross-compiling, to avoid linking with the host OS libraries.</dd>
<dt><i>Pxxx</i></dt>
<dd> Prepend the names of binutils (as, ld) with xxx. For use when cross-compiling.</dd>
<dt><i>rxxx</i></dt>
<dd> Set the library search path to xxx.</dd>
<dt><i>s</i></dt>
<dd> Strip the symbols from the executable.</dd>
<dt><i>S</i></dt>
<dd> Link with static libraries (defines the FPC_LINK_STATIC symbol)</dd>
<dt><i>t</i></dt>
<dd> Link statically (passes -static to the linker)</dd>
<dt><i>X</i></dt>
<dd> Link smart. Using this option sets the FPC_LINK_SMART symbol.</dd></dl>
</dl>
</dl>
<p> Options concerning the sources (language options) for more information on these options, see also in the Programmers Manual</p>
<dl>
<dt><code>-M</code><i>mode</i></dt>
<dd> Specify the language mode. <i>mode</i> can be one of the following:</dd>
<dl>
<dl>
<dt><i>delphi</i></dt>
<dd> Delphi-compatibility mode. This loads the objpas unit, and switches on ansistring mode ( <code>-Sh</code> ).</dd>
<dt><i>fpc</i></dt>
<dd> Default mode.</dd>
<dt><i>gpc</i></dt>
<dd> GNU pascal mode (does nothing at the moment)</dd>
<dt><i>macpas</i></dt>
<dd> Mac pascal mode. This loads the macpas unit and switches on some Mac extensions (mainly macros)</dd>
<dt><i>objfpc</i></dt>
<dd> Object Pascal mode. This loads the objpas unit.</dd>
<dt><i>tp</i></dt>
<dd> Turbo Pascal mode.</dd></dl>
</dl>
<dt><code>-R</code><i>xxx</i></dt>
<dd> Specifies what assembler you use in your &quot;asm&quot; assembler code blocks. Here <i>xxx</i> is one of the following:</dd>
<dl>
<dl>
<dt><i>att</i></dt>
<dd> Asm blocks contain AT&amp;T assembler.</dd>
<dt><i>intel</i></dt>
<dd> Asm blocks contain Intel assembler.</dd>
<dt><i>direct</i></dt>
<dd> Asm blocks should be copied as-is in the assembler file.</dd></dl>
</dl>
<dt><code>-S2</code></dt>
<dd> Switch on Delphi 2 extensions.</dd>
<dt><code>-Sa</code></dt>
<dd> Generate code for assertions.</dd>
<dt><code>-Sc</code></dt>
<dd> Support C-style operators, i.e. *=, +=, /= and -=.</dd>
<dt><code>-Sd</code></dt>
<dd> Tries to be Delphi compatible</dd>
<dt><code>-Se</code></dt>
<dd> The compiler stops after the first error. Normally, the compiler tries to continue compiling after an error, until 50 errors are reached, or a fatal error is reached, and then it stops. With this switch, the compiler will stop after the first error.</dd>
<dt><code>-Sg</code></dt>
<dd> Support the label and goto commands.</dd>
<dt><code>-Sh</code></dt>
<dd> use ansistrings by default.</dd>
<dt><code>-SIxxx</code></dt>
<dd> Specify the kind of interfaces. <i>xxx</i> can be one of the following:</dd>
<dl>
<dl>
<dt><i>COM </i></dt>
<dd> use COM interfaces. (all interfaces descend from IUnknown)</dd>
<dt><i>CORBA </i></dt>
<dd> use CORBA interfaces. (no inheritance is supposed)</dd></dl>
</dl>
<dt><code>-Si</code></dt>
<dd> Support C++ style INLINE.</dd>
<dt><code>-Sm</code></dt>
<dd> Support C-style macros.</dd>
<dt><code>-So</code></dt>
<dd> Try to be Borland TP 7.0 compatible (no function overloading etc.).</dd>
<dt><code>-Sp</code></dt>
<dd> Try to be <i>GPC (GNU Pascal Compiler)</i> compatible.</dd>
<dt><code>-Ss</code></dt>
<dd> The name of constructors must be &quot;init&quot;, and the name of destructors should be &quot;done&quot;.</dd>
<dt><code>-St</code></dt>
<dd> Allow the &quot;static&quot; keyword in objects.</dd>
<dt><code>-Un</code></dt>
<dd> Do not check the unit name. Normally, the unit name is the same as the filename. This option allows both to be different.</dd>
<dt><code>-Ur</code></dt>
<dd> Create a release unit. This sets a special flag in the unit, causing the compiler not to look for sources.</dd>
<dt><code>-Us</code></dt>
<dd> Compile a system unit. This option causes the compiler to define only some very basic types. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>fpc.cfg</code>(5) <code><a href="/docs/linux/man/1-ppdep/">ppdep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) <code><a href="/docs/linux/man/1-as/">as</a></code>(1) </p>
