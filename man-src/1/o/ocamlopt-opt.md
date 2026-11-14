---
title: "ocamlopt-opt(1)"
name: "ocamlopt-opt"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlopt-opt/"
description: "ocamlopt – The OCaml native-code compiler"
---

<p>ocamlopt &#8211; The OCaml native-code compiler</p>
<h2>Synopsis</h2>
<p><code>ocamlopt</code> [ <i>options</i> ] <i>filename</i>&nbsp;<wbr>&#8230; </p>
<p> <code>ocamlopt.opt</code> (same options) </p>
<h2>Description</h2>
<p>The OCaml high-performance native-code compiler <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) compiles OCaml source files to native code object files and link these object files to produce standalone executables. </p>
<p> The <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) command has a command-line interface very close to that of <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1). It accepts the same types of arguments and processes them sequentially: </p>
<p> Arguments ending in .mli are taken to be source files for compilation unit interfaces. Interfaces specify the names exported by compilation units: they declare value names with their types, define public data types, declare abstract data types, and so on. From the file <i>x</i>.mli, the <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) compiler produces a compiled interface in the file <i>x</i>.cmi. The interface produced is identical to that produced by the bytecode compiler <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1). </p>
<p> Arguments ending in .ml are taken to be source files for compilation unit implementations. Implementations provide definitions for the names exported by the unit, and also contain expressions to be evaluated for their side-effects. From the file <i>x</i>.ml, the <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) compiler produces two files: <i>x</i>.o, containing native object code, and <i>x</i>.cmx, containing extra information for linking and optimization of the clients of the unit. The compiled implementation should always be referred to under the name <i>x</i>.cmx (when given a .o file, <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) assumes that it contains code compiled from C, not from OCaml). </p>
<p> The implementation is checked against the interface file <i>x</i>.mli (if it exists) as described in the manual for <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1). </p>
<p> Arguments ending in .cmx are taken to be compiled object code. These files are linked together, along with the object files obtained by compiling .ml arguments (if any), and the OCaml standard library, to produce a native-code executable program. The order in which .cmx and .ml arguments are presented on the command line is relevant: compilation units are initialized in that order at run-time, and it is a link-time error to use a component of a unit before having initialized it. Hence, a given <i>x</i>.cmx file must come before all .cmx files that refer to the unit <i>x</i>. </p>
<p> Arguments ending in .cmxa are taken to be libraries of object code. Such a library packs in two files <i>lib</i>.cmxa and <i>lib</i>.a a set of object files (.cmx/.o files). Libraries are build with <code>ocamlopt -a</code> (see the description of the <code>-a</code> option below). The object files contained in the library are linked as regular .cmx files (see above), in the order specified when the library was built. The only difference is that if an object file contained in a library is not referenced anywhere in the program, then it is not linked in. </p>
<p> Arguments ending in .c are passed to the C compiler, which generates a .o object file. This object file is linked with the program. </p>
<p> Arguments ending in .o or .a are assumed to be C object files and libraries. They are linked with the program. </p>
<p> The output of the linking phase is a regular Unix executable file. It does not need <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1) to run. </p>
<p> <code>ocamlopt.opt</code> is the same compiler as <code>ocamlopt</code>, but compiled with itself instead of with the bytecode compiler <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1). Thus, it behaves exactly like <code>ocamlopt</code>, but compiles faster. <code>ocamlopt.opt</code> is not available in all installations of OCaml. </p>
<h2>Options</h2>
<p>The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).</p>
<dl COMPACT>
<dt><code>-a</code></p>
<dd>Build a library (.cmxa/.a file) with the object files (.cmx/.o files) given on the command line, instead of linking them into an executable file. The name of the library must be set with the <code>-o</code> option. </p>
<p> If <code>-cclib</code>&nbsp;<wbr>or<code>&nbsp;<wbr>-ccopt</code> options are passed on the command line, these options are stored in the resulting .cmxa library. Then, linking with this library automatically adds back the <code>-cclib</code>&nbsp;<wbr>and<code>&nbsp;<wbr>-ccopt</code> options as if they had been provided on the command line, unless the <code>-noautolink</code> option is given.</p>
<dt><code>-absname</code></p>
<dd>Show absolute filenames in error messages.</p>
<dt><code>-annot</code></p>
<dd>Dump detailed information about the compilation (types, bindings, tail-calls, etc). The information for file <i>src</i>.ml is put into file <i>src</i>.annot. In case of a type error, dump all the information inferred by the type-checker before the error. The <i>src</i>.annot file can be used with the emacs commands given in <code>emacs/caml-types.el</code> to display types and other annotations interactively.</p>
<dt><code>-bin-annot</code></p>
<dd>Dump detailed information about the compilation (types, bindings, tail-calls, etc) in binary format. The information for file <i>src</i>.ml is put into file <i>src</i>.cmt. In case of a type error, dump all the information inferred by the type-checker before the error. The annotation files produced by <code>-bin-annot</code> contain more information and are much more compact than the files produced by <code>-annot</code>.</p>
<dt><code>-c</code></p>
<dd>Compile only. Suppress the linking phase of the compilation. Source code files are turned into compiled files, but no executable file is produced. This option is useful to compile modules separately.</p>
<dt><code>-cc</code><i>&nbsp;<wbr>ccomp</i></p>
<dd>Use <i>ccomp</i> as the C linker called to build the final executable and as the C compiler for compiling .c source files.</p>
<dt><code>-cclib -l</code><i>libname</i></p>
<dd>Pass the <code>-l</code><i>libname</i> option to the linker. This causes the given C library to be linked with the program.</p>
<dt><code>-ccopt</code><i>&nbsp;<wbr>option</i></p>
<dd>Pass the given option to the C compiler and linker. For instance, <code>-ccopt -L</code><i>dir</i> causes the C linker to search for C libraries in directory <i>dir</i>.</p>
<dt><code>-compact</code></p>
<dd>Optimize the produced code for space rather than for time. This results in smaller but slightly slower programs. The default is to optimize for speed.</p>
<dt><code>-config</code></p>
<dd>Print the version number of <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) and a detailed summary of its configuration, then exit.</p>
<dt><code>-for-pack</code><i>&nbsp;<wbr>module-path</i></p>
<dd>Generate an object file (.cmx and .o files) that can later be included as a sub-module (with the given access path) of a compilation unit constructed with <code>-pack</code>. For instance, <code>ocamlopt -for-pack P -c A.ml</code> will generate a.cmx and a.o files that can later be used with <code>ocamlopt -pack -o P.cmx a.cmx</code>.</p>
<dt><code>-g</code></p>
<dd>Add debugging information while compiling and linking. This option is required in order to produce stack backtraces when the program terminates on an uncaught exception (see <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1)).</p>
<dt><code>-i</code></p>
<dd>Cause the compiler to print all defined names (with their inferred types or their definitions) when compiling an implementation (.ml file). No compiled files (.cmo and .cmi files) are produced. This can be useful to check the types inferred by the compiler. Also, since the output follows the syntax of interfaces, it can help in writing an explicit interface (.mli file) for a file: just redirect the standard output of the compiler to a .mli file, and edit that file to remove all declarations of unexported names.</p>
<dt><code>-I</code><i>&nbsp;<wbr>directory</i></p>
<dd>Add the given directory to the list of directories searched for compiled interface files (.cmi), compiled object code files (.cmx), and libraries (.cmxa). By default, the current directory is searched first, then the standard library directory. Directories added with -I are searched after the current directory, in the order in which they were given on the command line, but before the standard library directory. See also option <code>-nostdlib</code>. </p>
<p> If the given directory starts with <code>+</code>, it is taken relative to the standard library directory. For instance, <code>-I&nbsp;<wbr>+labltk</code> adds the subdirectory <code>labltk</code> of the standard library to the search path.</p>
<dt><code>-impl</code><i>&nbsp;<wbr>filename</i></p>
<dd>Compile the file <i>filename</i> as an implementation file, even if its extension is not .ml.</p>
<dt><code>-inline</code><i>&nbsp;<wbr>n</i></p>
<dd>Set aggressiveness of inlining to <i>n</i>, where <i>n</i> is a positive integer. Specifying <code>-inline 0</code> prevents all functions from being inlined, except those whose body is smaller than the call site. Thus, inlining causes no expansion in code size. The default aggressiveness, <code>-inline 1</code>, allows slightly larger functions to be inlined, resulting in a slight expansion in code size. Higher values for the <code>-inline</code> option cause larger and larger functions to become candidate for inlining, but can result in a serious increase in code size.</p>
<dt><code>-intf</code><i>&nbsp;<wbr>filename</i></p>
<dd>Compile the file <i>filename</i> as an interface file, even if its extension is not .mli.</p>
<dt><code>-intf-suffix</code><i>&nbsp;<wbr>string</i></p>
<dd>Recognize file names ending with <i>string</i> as interface files (instead of the default .mli).</p>
<dt><code>-labels</code></p>
<dd>Labels are not ignored in types, labels may be used in applications, and labelled parameters can be given in any order. This is the default.</p>
<dt><code>-linkall</code></p>
<dd>Force all modules contained in libraries to be linked in. If this flag is not given, unreferenced modules are not linked in. When building a library (<code>-a</code> flag), setting the <code>-linkall</code> flag forces all subsequent links of programs involving that library to link all the modules contained in the library.</p>
<dt><code>-no-app-funct</code></p>
<dd>Deactivates the applicative behaviour of functors. With this option, each functor application generates new types in its result and applying the same functor twice to the same argument yields two incompatible structures.</p>
<dt><code>-noassert</code></p>
<dd>Do not compile assertion checks. Note that the special form <code>assert false</code> is always compiled because it is typed specially. This flag has no effect when linking already-compiled files.</p>
<dt><code>-noautolink</code></p>
<dd>When linking .cmxa libraries, ignore <code>-cclib</code>&nbsp;<wbr>and<code>&nbsp;<wbr>-ccopt</code> options potentially contained in the libraries (if these options were given when building the libraries). This can be useful if a library contains incorrect specifications of C libraries or C options; in this case, during linking, set <code>-noautolink</code> and pass the correct C libraries and options on the command line.</p>
<dt><code>-nodynlink</code></p>
<dd>Allow the compiler to use some optimizations that are valid only for code that is never dynlinked.</p>
<dt><code>-nostdlib</code></p>
<dd>Do not automatically add the standard library directory the list of directories searched for compiled interface files (.cmi), compiled object code files (.cmx), and libraries (.cmxa). See also option <code>-I</code>.</p>
<dt><code>-nolabels</code></p>
<dd>Ignore non-optional labels in types. Labels cannot be used in applications, and parameter order becomes strict.</p>
<dt><code>-o</code><i>&nbsp;<wbr>exec-file</i></p>
<dd>Specify the name of the output file produced by the linker. The default output name is a.out, in keeping with the Unix tradition. If the <code>-a</code> option is given, specify the name of the library produced. If the <code>-pack</code> option is given, specify the name of the packed object file produced. If the <code>-output-obj</code> option is given, specify the name of the output file produced. If the <code>-shared</code> option is given, specify the name of plugin file produced.</p>
<dt><code>-output-obj</code></p>
<dd>Cause the linker to produce a C object file instead of an executable file. This is useful to wrap OCaml code as a C library, callable from any C program. The name of the output object file must be set with the <code>-o</code> option. This option can also be used to produce a compiled shared/dynamic library (.so extension).</p>
<dt><code>-p</code></p>
<dd>Generate extra code to write profile information when the program is executed. The profile information can then be examined with the analysis program <code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1). The <code>-p</code> option must be given both at compile-time and at link-time. Linking object files not compiled with <code>-p</code> is possible, but results in less precise profiling. </p>
<p> See the <code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1) man page for more information about the profiles. </p>
<p> Full support for <code><a href="/docs/linux/man/1-gprof/">gprof</a></code>(1) is only available for certain platforms (currently: Intel x86/Linux and Alpha/Digital Unix). On other platforms, the <code>-p</code> option will result in a less precise profile (no call graph information, only a time profile).</p>
<dt><code>-pack</code></p>
<dd>Build an object file (.cmx and .o files) and its associated compiled interface (.cmi) that combines the .cmx object files given on the command line, making them appear as sub-modules of the output .cmx file. The name of the output .cmx file must be given with the <code>-o</code> option. For instance, <code>ocamlopt -pack -o P.cmx A.cmx B.cmx C.cmx</code> generates compiled files P.cmx, P.o and P.cmi describing a compilation unit having three sub-modules A, B and C, corresponding to the contents of the object files A.cmx, B.cmx and C.cmx. These contents can be referenced as P.A, P.B and P.C in the remainder of the program. </p>
<p> The .cmx object files being combined must have been compiled with the appropriate <code>-for-pack</code> option. In the example above, A.cmx, B.cmx and C.cmx must have been compiled with <code>ocamlopt -for-pack P</code>. </p>
<p> Multiple levels of packing can be achieved by combining <code>-pack</code> with <code>-for-pack</code>. See <i>The OCaml user&#8217;s manual</i>, chapter &quot;Native-code compilation&quot; for more details.</p>
<dt><code>-pp</code><i>&nbsp;<wbr>command</i></p>
<dd>Cause the compiler to call the given <i>command</i> as a preprocessor for each source file. The output of <i>command</i> is redirected to an intermediate file, which is compiled. If there are no compilation errors, the intermediate file is deleted afterwards.</p>
<dt><code>-ppx</code><i>&nbsp;<wbr>command</i></p>
<dd>After parsing, pipe the abstract syntax tree through the preprocessor <i>command</i>. The format of the input and ouput of the preprocessor are not yet documented.</p>
<dt><code>-principal</code></p>
<dd>Check information path during type-checking, to make sure that all types are derived in a principal way. All programs accepted in <code>-principal</code> mode are also accepted in default mode with equivalent types, but different binary signatures.</p>
<dt><code>-rectypes</code></p>
<dd>Allow arbitrary recursive types during type-checking. By default, only recursive types where the recursion goes through an object type are supported. Note that once you have created an interface using this flag, you must use it again for all dependencies.</p>
<dt><code>-runtime-variant</code><i>&nbsp;<wbr>suffix</i></p>
<dd>Add <i>suffix</i> to the name of the runtime library that will be used by the program. If OCaml was configured with option <code>-with-debug-runtime</code>, then the <code>d</code> suffix is supported and gives a debug version of the runtime.</p>
<dt><code>-S</code></p>
<dd>Keep the assembly code produced during the compilation. The assembly code for the source file <i>x</i>.ml is saved in the file <i>x</i>.s.</p>
<dt><code>-shared</code></p>
<dd>Build a plugin (usually .cmxs) that can be dynamically loaded with the <code>Dynlink</code> module. The name of the plugin must be set with the <code>-o</code> option. A plugin can include a number of OCaml modules and libraries, and extra native objects (.o, .a files). Building native plugins is only supported for some operating system. Under some systems (currently, only Linux AMD 64), all the OCaml code linked in a plugin must have been compiled without the <code>-nodynlink</code> flag. Some constraints might also apply to the way the extra native objects have been compiled (under Linux AMD 64, they must contain only position-independent code).</p>
<dt><code>-short-paths</code></p>
<dd>When a type is visible under several module-paths, use the shortest one when printing the type&#8217;s name in inferred interfaces and error and warning messages.</p>
<dt><code>-strict-sequence</code></p>
<dd>The left-hand part of a sequence must have type unit.</p>
<dt><code>-thread</code></p>
<dd>Compile or link multithreaded programs, in combination with the system threads library described in <i>The OCaml user&#8217;s manual</i>.</p>
<dt><code>-unsafe</code></p>
<dd>Turn bound checking off for array and string accesses (the <code>v.(i)</code>and<code>s.[i]</code> constructs). Programs compiled with <code>-unsafe</code> are therefore faster, but unsafe: anything can happen if the program accesses an array or string outside of its bounds. Additionally, turn off the check for zero divisor in integer division and modulus operations. With <code>-unsafe</code>, an integer division (or modulus) by zero can halt the program or continue with an unspecified result instead of raising a <code>Division_by_zero</code> exception.</p>
<dt><code>-v</code></p>
<dd>Print the version number of the compiler and the location of the standard library directory, then exit.</p>
<dt><code>-verbose</code></p>
<dd>Print all external commands before they are executed, in particular invocations of the assembler, C compiler, and linker.</p>
<dt><code>-version</code>&nbsp;<wbr>or&nbsp;<wbr><code>-vnum</code></p>
<dd>Print the version number of the compiler in short form (e.g. &quot;3.11.0&quot;), then exit.</p>
<dt><code>-w</code><i>&nbsp;<wbr>warning-list</i></p>
<dd>Enable, disable, or mark as fatal the warnings specified by the argument <i>warning-list</i>. See <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) for the syntax of <i>warning-list</i>.</p>
<dt><code>-warn-error</code><i>&nbsp;<wbr>warning-list</i></p>
<dd>Mark as fatal the warnings specified in the argument <i>warning-list</i>. The compiler will stop with an error when one of these warnings is emitted. The <i>warning-list</i> has the same meaning as for the <code>-w</code> option: a <code>+</code> sign (or an uppercase letter) marks the corresponding warnings as fatal, a <code>&#8211;</code> sign (or a lowercase letter) turns them back into non-fatal warnings, and a <code>@</code> sign both enables and marks as fatal the corresponding warnings. </p>
<p> Note: it is not recommended to use the <code>-warn-error</code> option in production code, because it will almost certainly prevent compiling your program with later versions of OCaml when they add new warnings. </p>
<p> The default setting is <code>-warn-error -a (all warnings are non-fatal).</code></p>
<dt><code>-warn-help</code></p>
<dd>Show the description of all available warning numbers.</p>
<dt><code>-where</code></p>
<dd>Print the location of the standard library, then exit.</p>
<dt><code>&#8211;</code><i>&nbsp;<wbr>file</i></p>
<dd>Process <i>file</i> as a file name, even if it starts with a dash (-) character.</p>
<dt><code>-help</code>&nbsp;<wbr>or<code>&nbsp;<wbr>&#8211;help</code></p>
<dd>Display a short usage summary and exit. </p>
</dl>
<h2>Options For The Ia32 Architecture</h2>
<p>The IA32 code generator (Intel Pentium, AMD Athlon) supports the following additional option:</p>
<dl COMPACT>
<dt><code>-ffast-math</code></p>
<dd>Use the IA32 instructions to compute trigonometric and exponential functions, instead of calling the corresponding library routines. The functions affected are: <code>atan</code>, <code>atan2</code>, <code>cos</code>, <code>log</code>, <code>log10</code>, <code>sin</code>, <code>sqrt</code> and <code>tan</code>. The resulting code runs faster, but the range of supported arguments and the precision of the result can be reduced. In particular, trigonometric operations <code>cos</code>, <code>sin</code>, <code>tan</code> have their range reduced to [-2^64, 2^64]. </p>
</dl>
<h2>Options For The Amd64 Architecture</h2>
<p>The AMD64 code generator (64-bit versions of Intel Pentium and AMD Athlon) supports the following additional options:</p>
<dl COMPACT>
<dt><code>-fPIC</code></p>
<dd>Generate position-independent machine code. This is the default.</p>
<dt><code>-fno-PIC</code></p>
<dd>Generate position-dependent machine code. </p>
</dl>
<h2>Options For The Sparc Architecture</h2>
<p>The Sparc code generator supports the following additional options:</p>
<dl COMPACT>
<dt><code>-march=v8</code></p>
<dd>Generate SPARC version 8 code.</p>
<dt><code>-march=v9</code></p>
<dd>Generate SPARC version 9 code.</dl>
<p> The default is to generate code for SPARC version 7, which runs on all SPARC processors. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Native-code compilation&quot;.</p>
