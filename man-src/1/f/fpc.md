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
<p> The compilation proces is started by typing <i>fpc</i> followed by a sourcefile name (normally with .pas or .pp extension). Before processing the actual processing of the source file, <code><a href="/docs/linux/man/5-fpc-cfg/">fpc.cfg</a></code>(5) the configuration file of the compiler is read which contains the location of the RTL, other packages (FCL, FreeVision), and optionally default values for some switches. See the separate manpage of <code><a href="/docs/linux/man/5-fpc-cfg/">fpc.cfg</a></code>(5) for more information. </p>
<h2>Options</h2>
<p> General options </p>
<dl>
<dt><code>-h</code></p>
<dd> if you specify this option, the compiler outputs a list of all options, and exits after that.</p>
<dt><code>-?</code></p>
<dd> idem as -h, but waiting after every screenfull for the enter key.</p>
<dt><code>-i</code></p>
<dd> This option tells the compiler to print the copyright information. </p>
<p> You can give it an option, as -ixxx where &quot;xxx&quot; can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>D</i></p>
<dd> Returns the compiler date.</p>
<dt><i>V</i></p>
<dd> Returns the compiler version.</p>
<dt><i>SO</i></p>
<dd> Returns the compiler OS.</p>
<dt><i>SP</i></p>
<dd> Returns the compiler processor.</p>
<dt><i>TO</i></p>
<dd> Returns the target OS.</p>
<dt><i>TP</i></p>
<dd> Returns the target Processor.</dl>
</dl>
<dt><i>-l</i></p>
<dd> This option tells the compiler to print the <i>FPC</i> logo on standard output. It also gives you the <i>FPC</i> version number.</p>
<dt><i>-n</i></p>
<dd> Tells the compiler not to read the configuration file <code><a href="/docs/linux/man/5-fpc-cfg/">fpc.cfg</a></code>(5) </p>
</dl>
<p> Options for getting feedback</p>
<dl>
<dt><code>-v</code><i>xxx</i></p>
<dd> Be verbose. &quot;xxx&quot; is a combination of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>e</i></p>
<dd> Tells the compiler to show only errors. This option is on by default.</p>
<dt><i>i</i></p>
<dd> Tells the compiler to show some general information.</p>
<dt><i>w</i></p>
<dd> Tells the compiler to issue warnings.</p>
<dt><i>n</i></p>
<dd> Tells the compiler to issue notes.</p>
<dt><i>h</i></p>
<dd> Tells the compiler to issue hints.</p>
<dt><i>l</i></p>
<dd> Tells the compiler to show the line numbers as it processes a file. Numbers are shown per 100.</p>
<dt><i>u</i></p>
<dd> Tells the compiler to print the names of the files it opens.</p>
<dt><i>t</i></p>
<dd> Tells the compiler to print the names of the files it tries to open.</p>
<dt><i>p</i></p>
<dd> Tells the compiler to print the names of procedures and functions as it is processing them.</p>
<dt><i>c</i></p>
<dd> Tells the compiler to warn you when it processes a conditional.</p>
<dt><i>m</i></p>
<dd> Tells the compiler to write which macros are defined.</p>
<dt><i>d</i></p>
<dd> Tells the compiler to write other debugging info.</p>
<dt><i>a</i></p>
<dd> Tells the compiler to write all possible info. (this is the same as specifying all options)</p>
<dt><i>0</i></p>
<dd> Tells the compiler to write no messages. This is useful when you want to override the default setting in the configuration file.</p>
<dt><i>b</i></p>
<dd> Tells the compiler to show all procedure declarations if an overloaded function error occurs.</p>
<dt><i>x</i></p>
<dd> Tells the compiler to output some executable info (for Win32 platform only).</p>
<dt><i>r</i></p>
<dd> Rhide/GCC compatibility mode: formats the error differently, so they are understood by RHIDE.</dl>
</dl>
</dl>
<p> Options concerning files and directories</p>
<dl>
<dt><code>-e</code><i>xxx</i></p>
<dd> tells the compiler that <i>xxx</i> is the directory where it can find the executables as (the assembler) and ld (the linker).</p>
<dt><code>-FD</code></p>
<dd> same as <i>-e.</i></p>
<dt><code>-Fe</code><i>xxx</i></p>
<dd> This option tells the compiler to write errors, etc. to the file <i>xxx</i></p>
<dt><code>-FE</code><i>xxx</i></p>
<dd> set the executable/unit output path to <i>xxx</i></p>
<dt><code>-Fi</code><i>xxx</i></p>
<dd> adds <i>xxx</i> to the path where the compiler searches for its include files.</p>
<dt><code>-Fl</code><i>xxx</i></p>
<dd> Adds <i>xxx</i> to the library searching path, and is passe to the linker.</p>
<dt><code>-FL</code><i>xxx</i></p>
<dd> ( Linux only) Tells the compiler to use <i>xxx</i> as the dynamic linker. Default this is /lib/ld-linux.so.2, or lib/ld-linux.so.1, depending on which one is found.</p>
<dt><code>-Fo</code><i>xxx</i></p>
<dd> Adds <i>xxx</i> to the object file path. This path is used when looking for files that need to be linked in.</p>
<dt><code>-Fr</code><i>xxx</i></p>
<dd> tells the compiler that <i>xxx</i> contains the compiler messages. Default the compiler has built-in messages. Specifying this option will override the default messages. (useful if you want to use a language other than the default language).</p>
<dt><code>-Fu</code><i>xxx</i></p>
<dd> Adds <i>xxx</i> to the unit path. By default, the compiler only searches for units in the current directory and the directory where the compiler itself resides. This option tells the compiler also to look in the directory <i>xxx</i></p>
<dt><code>-FU</code><i>xxx</i></p>
<dd> Tells the compiler to write units in directory <i>xxx</i> instead of the current directory.</p>
<dt><code>-I</code><i>xxx</i></p>
<dd> Add <i>xxx</i> to the include file search path. This path is used when looking for include files. </p>
</dl>
<p> for more information on these options, see also the programmers manual.</p>
<dl>
<dt><code>-a</code></p>
<dd> Tells the compiler not to delete the assembler file. This also counts for the (possibly) generated batch script.</p>
<dt><code>-al</code></p>
<dd> Tells the compiler to include the sourcecode lines in the assembler file as comments.</p>
<dt><code>-an</code></p>
<dd> Tells the compiler to include node information in the generated assembler file. This is mainly for use by the compiler developers.</p>
<dt><code>-ap</code></p>
<dd> Tells the compiler to use pipes to communicate with the assembler.</p>
<dt><code>-ar</code></p>
<dd> Tells the compiler to include register allocation/deallocation information.</p>
<dt><code>-at</code></p>
<dd> Tells the compiler to include temparary register allocation/deallocation information.</p>
<dt><code>-A</code><i>xxx</i></p>
<dd> specifies what kind of assembler should be generated . Here <i>xxx</i> is one of the following :</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>AS</i></p>
<dd> A unix .o (object) file, using <i>GNU AS</i></p>
<dt><i>coff</i></p>
<dd> coff object file (go32) using internal writer.</p>
<dt><i>default</i></p>
<dd> Use the default writer for the current platform.</p>
<dt><i>elf</i></p>
<dd> elf object file (linux, 32-bit only) using internal writer.</p>
<dt><i>nasmcoff</i></p>
<dd> a coff file using the <i>nasm</i> assembler.</p>
<dt><i>nasmelf</i></p>
<dd> a ELF32 file (LINUX only) using the <i>nasm</i> assembler.</p>
<dt><i>nasmobj</i></p>
<dd> a obj file using the <i>nasm</i> assembler.</p>
<dt><i>masm</i></p>
<dd> An obj file using the Microsoft <i>masm</i> assembler.</p>
<dt><i>pecoff</i></p>
<dd> pecoff object file (win32) using internal writer.</p>
<dt><i>tasm</i></p>
<dd> An obj file using the Borland <i>tasm</i> assembler.</p>
<dt><i>wasm</i></p>
<dd> An obj file using the Watcom assembler.</dl>
</dl>
<dt><code>-Ccxxx</code></p>
<dd> set the default calling convention to XXX.</p>
<dt><code>-CD</code></p>
<dd> Create dynamic library.</p>
<dt>
<dt><code>-Ce</code></p>
<dd>
<dd> Compile using emulated floating point instructions.</p>
<dt><code>-Cfxxx</code></p>
<dd> Set the used floating point instruction set to xxx.</p>
<dt><code>-Cg</code></p>
<dd> Generate PIC code.</p>
<dt><code>-Ch</code><i>xxx</i></p>
<dd> Reserves <i>xxx</i> bytes heap. <i>xxx</i> should be between 1024 and 67107840.</p>
<dt><code>-Ci</code></p>
<dd> Generate Input/Output checking code.</p>
<dt><code>-Cn</code></p>
<dd> Omit the linking stage.</p>
<dt><code>-Co</code></p>
<dd> Generate Integer overflow checking code.</p>
<dt><code>-CR</code></p>
<dd> Verify object call validity (method calls mustbe valid).</p>
<dt><code>-Cr</code></p>
<dd> Generate Range checking code.</p>
<dt><code>-Cs</code><i>xxx</i></p>
<dd> Set stack size to <i>xxx</i> bytes.</p>
<dt><code>-Ct</code></p>
<dd> generate stack checking code.</p>
<dt><code>-CX</code></p>
<dd> Create a smartlinked library.</p>
<dt><code>-d</code><i>xxx</i></p>
<dd> Define the symbol name <i>xxx</i> This can be used to conditionally compile parts of your code. </p>
<dt><code>-E</code></p>
<dd> Same as -Cn.</p>
<dt><code>-g</code></p>
<dd> Generate debugging information for debugging with <i>GDB</i></p>
<dt><code>-gg</code></p>
<dd> idem as <code>-g.</code></p>
<dt><code>-gd</code></p>
<dd> generate debugging info for dbx.</p>
<dt><code>-gh</code></p>
<dd> use the heaptrc unit (see the units part of the FPC manual).</p>
<dt><code>-gl</code></p>
<dd> use the lineinfo unit for line information (see the units part of the FPC manual).</p>
<dt><code>-gv</code></p>
<dd> Generate information for debugging with valgrind.</p>
<dt><code>-gw</code></p>
<dd> Generate DWARF debugging information.</p>
<dt><code>-O</code><i>xxx</i></p>
<dd> optimize the compiler&#8217;s output; <i>xxx</i> can have one of the following values :</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>g</i></p>
<dd> optimize for size, try to generate smaller code.</p>
<dt><i>G</i></p>
<dd> optimize for time, try to generate faster code (default).</p>
<dt><i>r</i></p>
<dd> keep certain variables in registers (experimental, use with caution).</p>
<dt><i>u</i></p>
<dd> uncertain optimizations</p>
<dt><i>1</i></p>
<dd> Level 1 optimizations (quick optimizations).</p>
<dt><i>2</i></p>
<dd> Level 2 optimizations (-O1 plus some slower optimizations).</p>
<dt><i>3</i></p>
<dd> Level 3 optimizations (-O2 plus -Ou).</p>
<dt><i>pn</i></p>
<dd> Specify processor : n can be one of</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>1</i></p>
<dd> optimize for 386/486</p>
<dt><i>2</i></p>
<dd> optimize for Pentium/PentiumMMX &#8482;</p>
<dt><i>3</i></p>
<dd> optimizations for PentiumPro / P-II / Cyrix 6&#215;86 / K6 &#8482;</dl>
</dl>
<p> The exact effect of these effects can be found in the programmers part of the manual.</dl>
</dl>
<dt><code>-o</code><i>xxx</i></p>
<dd> Tells the compiler to use <i>xxx</i> as the name of the output file (executable). Only with programs.</p>
<dt><code>-pg</code></p>
<dd> Generate profiler code for gprof.</p>
<dt><code>-s</code></p>
<dd> Tells the compiler not to call the assembler and linker. Instead, the compiler writes a script, PPAS.BAT under DOS, or ppas.sh under Linux, which can then be executed to produce an executable.</p>
<dt><code>-sh</code></p>
<dd> Tells the compiler to generate a script that can be used to assemble and link on the host system, not on the target system. Use this when cross-compiling.</p>
<dt><code>-sr</code></p>
<dd> Skip register allocation stage in compiler (use with -ar)</p>
<dt><code>-st</code></p>
<dd> Tells the compiler to generate a script that can be used to assemble and link on the target system, not on the host system. Use this when cross-compiling.</p>
<dt><code>-T</code><i>xxx</i></p>
<dd> Specifies the target operating system. <i>xxx</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>EMX</i></p>
<dd> OS/2 and DOS via the EMX extender.</p>
<dt><i>FREEBSD</i></p>
<dd> FreeBSD</p>
<dt><i>GO32V2</i></p>
<dd> DOS and version 2 of the DJ DELORIE extender.</p>
<dt><i>LINUX</i></p>
<dd> Linux.</p>
<dt><i>NETBSD</i></p>
<dd> Netbsd.</p>
<dt><i>NETWARE</i></p>
<dd> Novell Netware module (clib)</p>
<dt><i>NETLIBC</i></p>
<dd> Novell Netware module (libc)</p>
<dt><i>OPENBSD</i></p>
<dd> OpenBSD</p>
<dt><i>OS2</i></p>
<dd> OS/2 (native mode)</p>
<dt><i>SunOS</i></p>
<dd> Solaris SunOS</p>
<dt><i>WATCOM</i></p>
<dd> WatCOM dos extender</p>
<dt><i>WDOSX</i></p>
<dd> WDosX Dos extender</p>
<dt><i>WIN32</i></p>
<dd> Windows 32 bit.</dl>
</dl>
<dt><code>-u</code><i>xxx</i></p>
<dd> undefine the symbol <i>xxx</i> if it is defined. This is the opposite of the <code>-d </code> option.</p>
<dt><code>-X</code><i>x</i></p>
<dd> Executable options. These tell the compiler what kind of executable should be generated. the parameter <i>x</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>c</i></p>
<dd> (Linux only, obsolete) Link with the C library. You should only use this when you start to port Free Pascal to another operating system.</p>
<dt><i>D</i></p>
<dd> Link with dynamic libraries (defines the FPC_LINK_DYNAMIC symbol)</p>
<dt><i>d</i></p>
<dd> Don&#8217;t use the standard library path. Use this when cross-compiling, to avoid linking with the host OS libraries.</p>
<dt><i>Pxxx</i></p>
<dd> Prepend the names of binutils (as, ld) with xxx. For use when cross-compiling.</p>
<dt><i>rxxx</i></p>
<dd> Set the library search path to xxx.</p>
<dt><i>s</i></p>
<dd> Strip the symbols from the executable.</p>
<dt><i>S</i></p>
<dd> Link with static libraries (defines the FPC_LINK_STATIC symbol)</p>
<dt><i>t</i></p>
<dd> Link statically (passes -static to the linker)</p>
<dt><i>X</i></p>
<dd> Link smart. Using this option sets the FPC_LINK_SMART symbol.</dl>
</dl>
</dl>
<p> Options concerning the sources (language options) for more information on these options, see also in the Programmers Manual</p>
<dl>
<dt><code>-M</code><i>mode</i></p>
<dd> Specify the language mode. <i>mode</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>delphi</i></p>
<dd> Delphi-compatibility mode. This loads the objpas unit, and switches on ansistring mode ( <code>-Sh</code> ).</p>
<dt><i>fpc</i></p>
<dd> Default mode.</p>
<dt><i>gpc</i></p>
<dd> GNU pascal mode (does nothing at the moment)</p>
<dt><i>macpas</i></p>
<dd> Mac pascal mode. This loads the macpas unit and switches on some Mac extensions (mainly macros)</p>
<dt><i>objfpc</i></p>
<dd> Object Pascal mode. This loads the objpas unit.</p>
<dt><i>tp</i></p>
<dd> Turbo Pascal mode.</dl>
</dl>
<dt><code>-R</code><i>xxx</i></p>
<dd> Specifies what assembler you use in your &quot;asm&quot; assembler code blocks. Here <i>xxx</i> is one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>att</i></p>
<dd> Asm blocks contain AT&amp;T assembler.</p>
<dt><i>intel</i></p>
<dd> Asm blocks contain Intel assembler.</p>
<dt><i>direct</i></p>
<dd> Asm blocks should be copied as-is in the assembler file.</dl>
</dl>
<dt><code>-S2</code></p>
<dd> Switch on Delphi 2 extensions.</p>
<dt><code>-Sa</code></p>
<dd> Generate code for assertions.</p>
<dt><code>-Sc</code></p>
<dd> Support C-style operators, i.e. *=, +=, /= and -=.</p>
<dt><code>-Sd</code></p>
<dd> Tries to be Delphi compatible</p>
<dt><code>-Se</code></p>
<dd> The compiler stops after the first error. Normally, the compiler tries to continue compiling after an error, until 50 errors are reached, or a fatal error is reached, and then it stops. With this switch, the compiler will stop after the first error.</p>
<dt><code>-Sg</code></p>
<dd> Support the label and goto commands.</p>
<dt><code>-Sh</code></p>
<dd> use ansistrings by default.</p>
<dt><code>-SIxxx</code></p>
<dd> Specify the kind of interfaces. <i>xxx</i> can be one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>COM </i></p>
<dd> use COM interfaces. (all interfaces descend from IUnknown)</p>
<dt><i>CORBA </i></p>
<dd> use CORBA interfaces. (no inheritance is supposed)</dl>
</dl>
<dt><code>-Si</code></p>
<dd> Support C++ style INLINE.</p>
<dt><code>-Sm</code></p>
<dd> Support C-style macros.</p>
<dt><code>-So</code></p>
<dd> Try to be Borland TP 7.0 compatible (no function overloading etc.).</p>
<dt><code>-Sp</code></p>
<dd> Try to be <i>GPC (GNU Pascal Compiler)</i> compatible.</p>
<dt><code>-Ss</code></p>
<dd> The name of constructors must be &quot;init&quot;, and the name of destructors should be &quot;done&quot;.</p>
<dt><code>-St</code></p>
<dd> Allow the &quot;static&quot; keyword in objects.</p>
<dt><code>-Un</code></p>
<dd> Do not check the unit name. Normally, the unit name is the same as the filename. This option allows both to be different.</p>
<dt><code>-Ur</code></p>
<dd> Create a release unit. This sets a special flag in the unit, causing the compiler not to look for sources.</p>
<dt><code>-Us</code></p>
<dd> Compile a system unit. This option causes the compiler to define only some very basic types. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-fpc-cfg/">fpc.cfg</a></code>(5) <code><a href="/docs/linux/man/1-ppdep/">ppdep</a></code>(1) <code><a href="/docs/linux/man/1-ppudump/">ppudump</a></code>(1) <code><a href="/docs/linux/man/1-ppumove/">ppumove</a></code>(1) <code><a href="/docs/linux/man/1-ptop/">ptop</a></code>(1) <code><a href="/docs/linux/man/1-h2pas/">h2pas</a></code>(1) <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) <code><a href="/docs/linux/man/1-as/">as</a></code>(1) </p>
<h2>Index</h2>
