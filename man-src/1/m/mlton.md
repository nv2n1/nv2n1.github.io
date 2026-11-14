---
title: "mlton(1)"
name: "mlton"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlton/"
description: "mlton – whole-program compiler for the Standard ML (SML) programming language"
---

<h2>NAME</h2>
<p> <code>mlton</code> &#8211; whole-program compiler for the Standard ML (SML) programming language</p>
<h2>SYNOPSIS</h2>
<p> <code>mlton</code> <i>[option &#8230;] file</i><code>.</code>{<code>c</code>|<code>cm</code>|<code>mlb</code>|<code>o</code>|<code>sml</code>} [file<code>.</code>{<code>c</code>|<code>o</code>|<code>s</code>|<code>S</code>} &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>MLton</code> is run from the command line with a collection of options followed by a file name and a list of files with which to compile, assemble, and link with. The simplest case is to run <code>mlton foo.sml</code>, where <code>foo.sml</code> contains a valid SML program, in which case MLton compiles the program to produce an executable <code>foo</code>. Since <code>MLton</code> does not support separate compilation, the program must be the entire program you wish to compile. However, the program may refer to signatures and structures defined in the Basis Library. </p>
<p> Larger programs, spanning many files, may be compiled with the ML Basis system. In this case, <code>mlton foo.mlb</code> will compile the complete SML program described by the basis <code>foo.mlb</code>, which may specify both SML files and additional bases. See the <code>MLton Guide</code> for details. </p>
<p> <code>MLton</code> also supports a limited subset of SML/NJ Compilation Manager (CM) files. For example, <code>mlton foo.cm</code> will compile the complete SML program consisting of the concatenation of all the SML files referred to (either directly or indirectly) by <code>foo.cm</code>. </p>
<p> <code>MLton</code>&#8216;s compile-time options control the name of the output file, the verbosity of compile-time messages, and whether or not certain optimizations are performed. They also can specify which intermediate files are saved and can stop the compilation process early, at some intermediate pass, in which case compilation can be resumed by passing the generated files to <code>MLton</code>. <code>MLton</code> uses the input file suffix to determine the type of input program. The possibilities are <code>.c</code>, <code>.cm</code>, <code>.mlb</code>, <code>.o</code>, <code>.S</code>, and <code>.sml</code>. </p>
<p> With no arguments, <code>MLton</code> prints the version number and exits. For a usage message, run <code>MLton</code> with an invalid switch, e.g. <code>mlton -z</code>. In the explanation below and in the usage message, for flags that take a number of choices (e.g. <i>{</i><code>true</code>|<code>false</code>}), the first value listed is the default. </p>
<h2>Compile-time options</h2>
<dl>
<dt><code>-align </code><i>{</i><code>4</code>|<code>8</code>}</p>
<dd> Aligns object sizes and doubles in memory by the specified alignment. The default varies depending on architecture. </p>
<dt><code>-as-opt </code><i>option</i></p>
<dd> Pass <i>option</i> to <code>gcc</code> when assembling. </p>
<dt><code>-cc-opt </code><i>option</i></p>
<dd> Pass <i>option</i> to <code>gcc</code> when compiling C code. </p>
<dt><code>-codegen </code><i>{</i><code>native</code>|<code>x86</code>|<code>amd64</code>|<code>c</code>|<code>bytecode</code>}</p>
<dd> Generate native code, C code, or byte code. With <code>-codegen native</code> (<code>-codegen x86</code> or <code>-codegen amd64</code>), <code>MLton</code> typically compiles more quickly and generates better code. </p>
<dt><code>-const &#8216;</code><i>name value</i>&#8216;</p>
<dd> Set the value of a compile-time constant. Here is a list of available constants, their default values, and what they control. </p>
<p> <code>Exn.keepHistory </code><i>{</i><code>false</code>|<code>true</code>} Enable <code>MLton.Exn.history</code>. There is a performance cost to setting this to <code>true</code>, both in memory usage of exceptions and in run time, because of additional work that must be performed at each exception construction, raise, and handle. </p>
<dt><code>-default-ann </code><i>ann</i></p>
<dd> Specify default ML Basis annotations. For example, <code>-default-ann &#8216;warnUnused true&#8217;</code> causes unused variable warnings to be enabled by default. Defaults may be overridden by an annotation in an ML Basis file. </p>
<dt><code>-default-type </code><i>type</i></p>
<dd> Specify the default binding for a primitive type. For example, <code>-default-type word64</code> causes the top-level type <code>word</code> and the top-level structure <code>Word</code> in the Basis Library to be equal to <code>Word64.word</code> and <code>Word64:WORD</code>, respectively. Similarly, <code>-default-type intinf</code> causes the top-level type <code>int</code> and the top-level structure <code>Int</code> in the Basis Library to be equal to <code>IntInf.int</code> and <code>IntInf:INTEGER</code>, respectively. </p>
<dt><code>-disable-ann </code><i>ann</i></p>
<dd> Ignore the specified ML Basis annotation in every ML Basis File. For example, to see <i>all</i> match and unused warnings, compile with <code>-default-ann &#8216;warnUnused true&#8217;</code>, <code>-disable-ann forceUsed</code>, <code>-disable-ann nonexhaustiveMatch</code>, <code>-disable-ann redundantMatch</code>, and <code>-disable-ann warnUnused</code>. </p>
<dt><code>-export-header </code><i>file</i></p>
<dd> Write C prototypes to <i>file</i> for all of the functions in the program exported from SML to C. </p>
<dt><code>-ieee-fp </code><i>{</i><code>false</code>|<code>true</code>}</p>
<dd> Cause the x86 native code generator to be pedantic about following the IEEE floating point standard. By default, it is not, because of the performance cost. This only has an effect with <code>-codegen x86</code>. </p>
<dt><code>-inline </code><i>n</i></p>
<dd> Set the inlining threshold used in the optimizer. The threshold is an approximate measure of code size of a procedure. The default is 320. </p>
<dt><code>-keep </code><i>{</i><code>g</code>|<code>o</code>|<code>sml</code>}</p>
<dd> Save intermediate files. If no <code>-keep</code> argument is given, then only the output file is saved. <code>g</code> generated <code>.S</code> and <code>.c</code> files passed to gcc and the assembler<br />
 <code>o</code> object (<code>.o</code>) files<br />
 <code>sml</code> SML file </p>
<dt><code>-link-opt </code><i>option</i></p>
<dd> Pass <i>option</i> to <code>gcc</code> when linking. You can use this to specify library search paths, e.g. <code>-link-opt -Lpath</code>, and libraries to link with, e.g. <code>-link-opt -lfoo</code>, or even both at the same time, e.g. <code>-link-opt &#8216;-Lpath -lfoo&#8217;</code>. If you wish to pass an option to the linker, you must use <code>gcc</code>&#8216;s <code>-Wl,</code> syntax, e.g., <code>-link-opt &#8216;-Wl,&#8211;export-dynamic&#8217;</code>. </p>
<dt><code>-mlb-path-map </code><i>file</i></p>
<dd> Use <i>file</i> as an ML Basis path map to define additional MLB path variables. Multiple uses of <code>-mlb-path-map</code> are allowed, with variable definitions in later path maps taking precendence over earlier ones. </p>
<dt><code>-output </code><i>file</i></p>
<dd> Specify the name of the final output file. The default name is the input file name with its suffix removed and an appropriate, possibly empty, suffix added. </p>
<dt><code>-profile </code><i>{</i><code>no</code>|<code>alloc</code>|<code>count</code>|<code>time</code>}</p>
<dd> Produce an executable that gathers profiling data. When such an executable is run, it will produce an <code>mlmon.out</code> file. The man page on <code>mlprof</code> describes how to extract information from this file. </p>
<dt><code>-profile-branch </code><i>{</i><code>false</code>|<code>true</code>}</p>
<dd> If true, the profiler will separately gather profiling data for each branch of a function definition, <code>case</code> expression, and <code>if</code> expression. </p>
<dt><code>-profile-stack </code><i>{</i><code>false</code>|<code>true</code>}</p>
<dd> If true, the profiler will gather profiling data for all functions on the stack, not just the currently executing function. </p>
<dt><code>-profile-val </code><i>{</i><code>false</code>|<code>true</code>}</p>
<dd> If true, the profiler will separately gather profiling data for each (expansive) <code>val</code> declaration. </p>
<dt><code>-runtime </code><i>arg</i></p>
<dd> Pass argument to the runtime system via <code>@MLton</code>. The argument will be processed before other <code>@MLton</code> command line switches. Multiple uses of <code>-runtime</code> are allowed, and will pass all the arguments in order. If the same runtime switch occurs more than once, then the last setting will take effect. There is no need to supply the leading <code>@MLton</code> or the trailing <code>&#8212;</code>; these will be supplied automatically. </p>
<p> An argument to <code>-runtime</code> may contain spaces, which will cause the argument to be treated as a sequence of words by the runtime. For example, the command line: <code>mlton -runtime &#8216;ram-slop 0.4&#8217; foo.sml</code> will cause foo to run as if it had been called like <code>foo @MLton ram-slop 0.4 &#8212;</code> </p>
<p> An executable created with <code>-runtime stop</code> doesn&#8217;t proces any <code>@MLton</code> arguments. This is useful to create an executable, e.g. <code>echo</code>, that must treat <code>@MLton</code> like any other command-line argument. <code>% mlton -runtime stop echo.sml</code> <code>% echo @MLton &#8212;</code> <code>@MLton &#8212;</code> </p>
<dt><code>-show-basis </code><i>file</i></p>
<dd> Pretty print to <i>file</i> the basis defined by the input program. </p>
<dt><code>-show-def-use </code><i>file</i></p>
<dd> Output def-use information to <i>file</i>. Each identifier that is defined appears on a line, follwed on subequent lines by the position of each use. </p>
<dt><code>-stop </code><i>{</i><code>f</code>|<code>g</code>|<code>o</code>|<code>sml</code>|<code>tc</code>}</p>
<dd> Specify when to stop. <code>f</code> list of files on stdout (only makes sense when input is <code>foo.cm</code> or <code>foo.mlb</code>)<br />
 <code>g</code> generated <code>.S</code> and <code>.c</code> files<br />
 <code>o</code> object (<code>.o</code>) files<br />
 <code>sml</code> SML file (only makes sense when input is <code>foo.cm</code> or <code>foo.mlb</code>)<br />
 <code>tc</code> after type checking If you compile <code>-stop g</code> or <code>-stop o</code>, you can resume compilation by running <code>MLton</code> on the generated <code>.c</code> and <code>.S</code> or <code>.o</code> files. </p>
<dt><code>-target </code><i>{</i><code>self</code>|&#8230;}</p>
<dd> Generate an executable that runs on the specified platform. The default is <code>self</code>, which means to compile for the machine that <code>MLton</code> is running on. To use any other target, you must first install a cross compiler. See the <code>MLton Guide</code> for details. </p>
<dt><code>-target-as-opt </code><i>target</i> <i>option</i></p>
<dd> Like <code>-as-opt</code>, this passes <i>option</i> to <code>gcc</code> when assembling, except it only passes <i>option</i> when the target architecture or operating system is <i>target</i>. Valid values for <i>target</i> are: <code>amd64</code>, <code>hppa</code>, <code>powerpc</code>, <code>sparc</code>, <code>x86</code>, <code>aix</code>, <code>cygwin</code>, <code>darwin</code>, <code>freebsd</code>, <code>hpuxP, linux</code>, <code>mingw</code>, <code>netbsd</code>, <code>openbsd</code>, <code>solaris</code>. </p>
<dt><code>-target-cc-opt </code><i>target</i> <i>option</i></p>
<dd> Like <code>-cc-opt</code>, this passes <i>option</i> to <code>gcc</code> when compiling C code, except it only passes <i>option</i> when the target architecture or operating system is <i>target</i>. Valid values for <i>target</i> are as for <code>-target-as-opt</code>. </p>
<dt><code>-target-link-opt </code><i>target</i> <i>option</i></p>
<dd> Like <code>-link-opt</code>, this passes <i>option</i> to <code>gcc</code> when linking, except it only passes <i>option</i> when the target architecture or operating system is <i>target</i>. Valid values for <i>target</i> are as for <code>-target-as-opt</code>. </p>
<dt><code>-verbose </code><i>{</i><code>0</code>|<code>1</code>|<code>2</code>|<code>3</code>}</p>
<dd> How verbose to be about what passes are running. The default is 0. <code>0</code> silent<br />
 <code>1</code> calls to compiler, assembler, and linker<br />
 <code>2</code> 1, plus intermediate compiler passes<br />
 <code>3</code> 2, plus some data structure sizes </p>
</dl>
<h2>Runtime system options</h2>
<p> Executables produced by <code>MLton</code> take command line arguments that control the runtime system. These arguments are optional, and occur before the executable&#8217;s usual arguments. To use these options, the first argument to the executable must be <code>@MLton</code>. The optional arguments then follow, must be terminated by <code>&#8212;</code>, and are followed by any arguments to the program. The optional arguments are <i>not</i> made available to the SML program via <code>CommandLine.arguments</code>. For example, a valid call to <code>hello-world</code> is: <code>hello-world @MLton gc-summary fixed-heap 10k &#8212; a b c</code> In the above example, <code>CommandLine.arguments () = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]</code>. </p>
<p> It is allowed to have a sequence of <code>@MLton</code> arguments, as in: <code>hello-world @MLton gc-summary &#8212; @MLton fixed-heap 10k &#8212; a b c</code> </p>
<p> Run-time options can also control <code>MLton</code>, as in <code>mlton @MLton fixed-heap 0.5g &#8212; foo.sml</code> </p>
<dl>
<dt><code>fixed-heap </code><i>x{</i><code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>}</p>
<dd> Use a fixed size heap of size <i>x</i>, where <i>x</i> is a real number and the trailing letter indicates its units. <code>k</code> or <code>K</code> 1024<br />
 m or <code>M</code> 1,048,576<br />
 <code>g</code> or <code>G</code> 1,073,741,824 A value of <code>0</code> means to use almost all the RAM present on the machine. </p>
<p> The heap size used by <code>fixed-heap</code> includes all memory allocated by SML code, including memory for the stack (or stacks, if there are multiple threads). It does not, however, include any memory used for code itself or memory used by C globals, the C stack, or malloc. </p>
<dt><code>gc-messages</code></p>
<dd> Print a message at the start and end of every garbage collection. </p>
<dt><code>gc-summary</code></p>
<dd> Print a summary of garbage collection statistics upon program termination. </p>
<dt><code>load-world </code><i>world</i></p>
<dd> Restart the computation with the file specified by <i>world</i>, which must have been created by a call to <code>MLton.World.save</code> by the same executable. See the <code>MLton Guide</code> for details. </p>
<dt><code>max-heap </code><i>x{</i><code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>}</p>
<dd> Run the computation with an automatically resized heap that is never larger than <i>x</i>, where <i>x</i> is a real number and the trailing letter indicates the units as with <code>fixed-heap</code>. The heap size for <code>max-heap</code> is accounted for as with <code>fixed-heap</code>. </p>
<dt><code>no-load-world</code></p>
<dd> Disable <code>load-world</code>. This can be used as an argument to the compiler via <code>-runtime no-load-world</code> to create executables that will not load a world. This may be useful to ensure that set-uid executables do not load some strange world. </p>
<dt><code>ram-slop </code><i>x</i></p>
<dd> Multiply <code>x</code> by the amount of RAM on the machine to obtain what the runtime views as the amount of RAM it can use. Typically <code>x</code> is less than 1, and is used to account for space used by other programs running on the same machine. </p>
<dt><code>stop</code></p>
<dd> Causes the runtime to stop processing <code>@MLton</code> arguments once the next <code>&#8212;</code> is reached. This can be used as an argument to the compiler via <code>-runtime stop</code> to create executables that don&#8217;t process any <code>@MLton</code> arguments. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> MLton&#8217;s type error messages are not in a form suitable for processing by Emacs. For details on how to fix this, see <a rel="nofollow" href="http://mlton.org/Emacs.">http://mlton.org/Emacs.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mlprof/">mlprof</a></code>(1) and the <code>MLton Guide</code>. </p>
<h2>Index</h2>
