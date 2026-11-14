---
title: "clang(1)"
name: "clang"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clang/"
description: "clang – the Clang C, C++, and Objective-C compiler"
---

<h2 class="name">NAME</h2>
<p> clang &#8211; the Clang C, C++, and Objective-C compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>clang</code> [<i>options</i>] <i>filename …</i></p>
<h2>DESCRIPTION</h2>
<p> <code>clang</code> is a C, C++, and Objective-C compiler which encompasses preprocessing, parsing, optimization, code generation, assembly, and linking. Depending on which high-level mode setting is passed, Clang will stop before doing a full link. While Clang is highly integrated, it is important to understand the stages of compilation, to understand how to invoke it. These stages are:</p>
<dl>
<dt><code>Driver</code></p>
<dd> The clang executable is actually a small driver which controls the overall execution of other tools such as the compiler, assembler and linker. Typically you do not need to interact with the driver, but you transparently use it to run the other tools.</p>
<dt><code>Preprocessing</code></p>
<dd> This stage handles tokenization of the input source file, macro expansion, #include expansion and handling of other preprocessor directives. The output of this stage is typically called a “.i” (for C), “.ii” (for C++), “.mi” (for Objective-C), or “.mii” (for Objective-C++) file.</p>
<dt><code>Parsing and Semantic Analysis</code></p>
<dd> This stage parses the input file, translating preprocessor tokens into a parse tree. Once in the form of a parse tree, it applies semantic analysis to compute types for expressions as well and determine whether the code is well formed. This stage is responsible for generating most of the compiler warnings as well as parse errors. The output of this stage is an “Abstract Syntax Tree” (AST).</p>
<dt><code>Code Generation and Optimization</code></p>
<dd> This stage translates an AST into low-level intermediate code (known as “LLVM IR”) and ultimately to machine code. This phase is responsible for optimizing the generated code and handling target-specific code generation. The output of this stage is typically called a “.s” file or “assembly” file. </p>
<p> Clang also supports the use of an integrated assembler, in which the code generator produces object files directly. This avoids the overhead of generating the “.s” file and of calling the target assembler.</p>
<dt><code>Assembler</code></p>
<dd> This stage runs the target assembler to translate the output of the compiler into a target object file. The output of this stage is typically called a “.o” file or “object” file.</p>
<dt><code>Linker</code></p>
<dd> This stage runs the target linker to merge multiple object files into an executable or dynamic library. The output of this stage is typically called an “a.out”, “.dylib” or “.so” file. </p>
<p> <code>Clang Static Analyzer</code> </p>
<p> The Clang Static Analyzer is a tool that scans source code to try to find bugs through code analysis. This tool uses many parts of Clang and is built into the same driver. Please see &lt;<i><a rel="nofollow" href="https://clang-analyzer.llvm.org">https://clang-analyzer.llvm.org</a></i>&gt; for more details on how to use the static analyzer.</dl>
<h2>OPTIONS</h2>
<h3>Stage Selection Options</h3>
<dl>
<dt><code>-E</code></p>
<dd> Run the preprocessor stage.</p>
<dt><code>-fsyntax-only</code></p>
<dd> Run the preprocessor, parser and type checking stages.</p>
<dt><code>-S</code></p>
<dd> Run the previous stages as well as LLVM generation and optimization stages and target-specific code generation, producing an assembly file.</p>
<dt><code>-c</code></p>
<dd> Run all of the above, plus the assembler, generating a target “.o” object file.</p>
<dt><code>no stage selection option</code></p>
<dd> If no stage selection option is specified, all stages above are run, and the linker is run to combine the results into an executable or shared library.</dl>
<h3>Language Selection and Mode Options</h3>
<dl>
<dt><code>-x &lt;language&gt;</code></p>
<dd> Treat subsequent input files as having type language.</p>
<dt><code>-std=&lt;standard&gt;</code></p>
<dd> Specify the language standard to compile for. </p>
<p> Supported values for the C language are: </p>
<pre>
<code>c89</code>
<code>c90</code>
<code>iso9899:1990</code>
</pre>
<p> ISO C 1990 </p>
<pre>
<code>iso9899:199409</code>
</pre>
<p> ISO C 1990 with amendment 1 </p>
<pre>
<code>gnu89</code>
<code>gnu90</code>
</pre>
<p> ISO C 1990 with GNU extensions </p>
<pre>
<code>c99</code>
<code>iso9899:1999</code>
</pre>
<p> ISO C 1999 </p>
<pre>
<code>gnu99</code>
</pre>
<p> ISO C 1999 with GNU extensions </p>
<pre>
<code>c11</code>
<code>iso9899:2011</code>
</pre>
<p> ISO C 2011 </p>
<pre>
<code>gnu11</code>
</pre>
<p> ISO C 2011 with GNU extensions </p>
<pre>
<code>c17</code>
<code>iso9899:2017</code>
</pre>
<p> ISO C 2017 </p>
<pre>
<code>gnu17</code>
</pre>
<p> ISO C 2017 with GNU extensions </p>
<p> The default C language standard is <code>gnu17</code>, except on PS4, where it is <code>gnu99</code>. </p>
<p> Supported values for the C++ language are: </p>
<pre>
<code>c++98</code>
<code>c++03</code>
</pre>
<p> ISO C++ 1998 with amendments </p>
<pre>
<code>gnu++98</code>
<code>gnu++03</code>
</pre>
<p> ISO C++ 1998 with amendments and GNU extensions </p>
<pre>
<code>c++11</code>
</pre>
<p> ISO C++ 2011 with amendments </p>
<pre>
<code>gnu++11</code>
</pre>
<p> ISO C++ 2011 with amendments and GNU extensions </p>
<pre>
<code>c++14</code>
</pre>
<p> ISO C++ 2014 with amendments </p>
<pre>
<code>gnu++14</code>
</pre>
<p> ISO C++ 2014 with amendments and GNU extensions </p>
<pre>
<code>c++17</code>
</pre>
<p> ISO C++ 2017 with amendments </p>
<pre>
<code>gnu++17</code>
</pre>
<p> ISO C++ 2017 with amendments and GNU extensions </p>
<pre>
<code>c++2a</code>
</pre>
<p> Working draft for ISO C++ 2020 </p>
<pre>
<code>gnu++2a</code>
</pre>
<p> Working draft for ISO C++ 2020 with GNU extensions </p>
<p> The default C++ language standard is <code>gnu++14</code>. </p>
<p> Supported values for the OpenCL language are: </p>
<pre>
<code>cl1.0</code>
</pre>
<p> OpenCL 1.0 </p>
<pre>
<code>cl1.1</code>
</pre>
<p> OpenCL 1.1 </p>
<pre>
<code>cl1.2</code>
</pre>
<p> OpenCL 1.2 </p>
<pre>
<code>cl2.0</code>
</pre>
<p> OpenCL 2.0 </p>
<p> The default OpenCL language standard is <code>cl1.0</code>. </p>
<p> Supported values for the CUDA language are: </p>
<pre>
<code>cuda</code>
</pre>
<p> NVIDIA CUDA(tm)</p>
<dt><code>-stdlib=&lt;library&gt;</code></p>
<dd> Specify the C++ standard library to use; supported options are libstdc++ and libc++. If not specified, platform default will be used.</p>
<dt><code>-rtlib=&lt;library&gt;</code></p>
<dd> Specify the compiler runtime library to use; supported options are libgcc and compiler-rt. If not specified, platform default will be used.</p>
<dt><code>-ansi</code></p>
<dd> Same as -std=c89.</p>
<dt><code>-ObjC, -ObjC++</code></p>
<dd> Treat source input files as Objective-C and Object-C++ inputs respectively.</p>
<dt><code>-trigraphs</code></p>
<dd> Enable trigraphs.</p>
<dt><code>-ffreestanding</code></p>
<dd> Indicate that the file should be compiled for a freestanding, not a hosted, environment. Note that it is assumed that a freestanding environment will additionally provide <i>memcpy</i>, <i>memmove</i>, <i>memset</i> and <i>memcmp</i> implementations, as these are needed for efficient codegen for many programs.</p>
<dt><code>-fno-builtin</code></p>
<dd> Disable special handling and optimizations of builtin functions like <code>strlen()</code> and <code>malloc()</code>.</p>
<dt><code>-fmath-errno</code></p>
<dd> Indicate that math functions should be treated as updating <code>errno</code>.</p>
<dt><code>-fpascal-strings</code></p>
<dd> Enable support for Pascal-style strings with “\pfoo”.</p>
<dt><code>-fms-extensions</code></p>
<dd> Enable support for Microsoft extensions.</p>
<dt><code>-fmsc-version=</code></p>
<dd> Set _MSC_VER. Defaults to 1300 on Windows. Not set otherwise.</p>
<dt><code>-fborland-extensions</code></p>
<dd> Enable support for Borland extensions.</p>
<dt><code>-fwritable-strings</code></p>
<dd> Make all string literals default to writable. This disables uniquing of strings and other optimizations.</p>
<dt><code>-flax-vector-conversions, -flax-vector-conversions=&lt;kind&gt;, -fno-lax-vector-conversions</code></p>
<dd> Allow loose type checking rules for implicit vector conversions. Possible values of &lt;kind&gt;:</p>
<dt>&bull;</p>
<dd> <code>none</code>: allow no implicit conversions between vectors</p>
<dt>&bull;</p>
<dd> <code>integer</code>: allow implicit bitcasts between integer vectors of the same overall bit-width</p>
<dt>&bull;</p>
<dd> <code>all</code>: allow implicit bitcasts between any vectors of the same overall bit-width </p>
<p> &lt;kind&gt; defaults to <code>integer</code> if unspecified.</p>
<dt><code>-fblocks</code></p>
<dd> Enable the “Blocks” language feature.</p>
<dt><code>-fobjc-abi-version=version</code></p>
<dd> Select the Objective-C ABI version to use. Available versions are 1 (legacy “fragile” ABI), 2 (non-fragile ABI 1), and 3 (non-fragile ABI 2).</p>
<dt><code>-fobjc-nonfragile-abi-version=&lt;version&gt;</code></p>
<dd> Select the Objective-C non-fragile ABI version to use by default. This will only be used as the Objective-C ABI when the non-fragile ABI is enabled (either via <i>-fobjc-nonfragile-abi</i>, or because it is the platform default).</p>
<dt><code>-fobjc-nonfragile-abi, -fno-objc-nonfragile-abi</code></p>
<dd> Enable use of the Objective-C non-fragile ABI. On platforms for which this is the default ABI, it can be disabled with <i>-fno-objc-nonfragile-abi</i>.</dl>
<h3>Target Selection Options</h3>
<p> Clang fully supports cross compilation as an inherent part of its design. Depending on how your version of Clang is configured, it may have support for a number of cross compilers, or may only support a native target.</p>
<dl>
<dt><code>-target &lt;architecture&gt;</code></p>
<dd> Specify the architecture to build for.</p>
<dt><code>&#8211;print-supported-cpus</code></p>
<dd> Print out a list of supported processors for the given target (specified through <code>&#8211;target=&lt;architecture&gt;</code> or <code>-arch</code> <code>&lt;architecture&gt;</code>). If no target is specified, the system default target will be used.</p>
<dt><code>-mcpu=?, -mtune=?</code></p>
<dd> Acts as an alias for <i>&#8211;print-supported-cpus</i>.</p>
<dt><code>-march=&lt;cpu&gt;</code></p>
<dd> Specify that Clang should generate code for a specific processor family member and later. For example, if you specify -march=i486, the compiler is allowed to generate instructions that are valid on i486 and later processors, but which may not exist on earlier ones.</dl>
<h3>Code Generation Options</h3>
<dl>
<dt><code>-O0, -O1, -O2, -O3, -Ofast, -Os, -Oz, -Og, -O, -O4</code></p>
<dd> Specify which optimization level to use: <i>-O0</i> Means “no optimization”: this level compiles the fastest and generates the most debuggable code. </p>
<p> <i>-O1</i> Somewhere between <i>-O0</i> and <i>-O2</i>. </p>
<p> <i>-O2</i> Moderate level of optimization which enables most optimizations. </p>
<p> <i>-O3</i> Like <i>-O2</i>, except that it enables optimizations that take longer to perform or that may generate larger code (in an attempt to make the program run faster). </p>
<p> <i>-Ofast</i> Enables all the optimizations from <i>-O3</i> along with other aggressive optimizations that may violate strict compliance with language standards. </p>
<p> <i>-Os</i> Like <i>-O2</i> with extra optimizations to reduce code size. </p>
<p> <i>-Oz</i> Like <i>-Os</i> (and thus <i>-O2</i>), but reduces code size further. </p>
<p> <i>-Og</i> Like <i>-O1</i>. In future versions, this option might disable different optimizations in order to improve debuggability. </p>
<p> <i>-O</i> Equivalent to <i>-O1</i>. </p>
<p> <i>-O4</i> and higher Currently equivalent to <i>-O3</i></p>
<dt><code>-g, -gline-tables-only, -gmodules</code></p>
<dd> Control debug information output. Note that Clang debug information works best at <i>-O0</i>. When more than one option starting with <i>-g</i> is specified, the last one wins: <code>-g</code> Generate debug information. </p>
<p> <code>-gline-tables-only</code> Generate only line table debug information. This allows for symbolicated backtraces with inlining information, but does not include any information about variables, their locations or types. </p>
<p> <i>-gmodules</i> Generate debug information that contains external references to types defined in Clang modules or precompiled headers instead of emitting redundant debug type information into every object file. This option transparently switches the Clang module format to object file containers that hold the Clang module together with the debug information. When compiling a program that uses Clang modules or precompiled headers, this option produces complete debug information with faster compile times and much smaller object files. </p>
<p> This option should not be used when building static libraries for distribution to other machines because the debug info will contain references to the module cache on the machine the object files in the library were built on.</p>
<dt><code>-fstandalone-debug -fno-standalone-debug</code></p>
<dd> Clang supports a number of optimizations to reduce the size of debug information in the binary. They work based on the assumption that the debug type information can be spread out over multiple compilation units. For instance, Clang will not emit type definitions for types that are not needed by a module and could be replaced with a forward declaration. Further, Clang will only emit type info for a dynamic C++ class in the module that contains the vtable for the class. </p>
<p> The <code>-fstandalone-debug</code> option turns off these optimizations. This is useful when working with 3rd-party libraries that don’t come with debug information. This is the default on Darwin. Note that Clang will never emit type information for types that are not referenced at all by the program.</p>
<dt><code>-feliminate-unused-debug-types</code></p>
<dd> By default, Clang does not emit type information for types that are defined but not used in a program. To retain the debug info for these unused types, the negation <code>-fno-eliminate-unused-debug-types</code> can be used.</p>
<dt><code>-fexceptions</code></p>
<dd> Enable generation of unwind information. This allows exceptions to be thrown through Clang compiled stack frames. This is on by default in x86-64.</p>
<dt><code>-ftrapv</code></p>
<dd> Generate code to catch integer overflow errors. Signed integer overflow is undefined in C. With this flag, extra code is generated to detect this and abort when it happens.</p>
<dt><code>-fvisibility</code></p>
<dd> This flag sets the default visibility level.</p>
<dt><code>-fcommon, -fno-common</code></p>
<dd> This flag specifies that variables without initializers get common linkage. It can be disabled with <i>-fno-common</i>.</p>
<dt><code>-ftls-model=&lt;model&gt;</code></p>
<dd> Set the default thread-local storage (TLS) model to use for thread-local variables. Valid values are: “global-dynamic”, “local-dynamic”, “initial-exec” and “local-exec”. The default is “global-dynamic”. The default model can be overridden with the tls_model attribute. The compiler will try to choose a more efficient model if possible.</p>
<dt><code>-flto, -flto=full, -flto=thin, -emit-llvm</code></p>
<dd> Generate output files in LLVM formats, suitable for link time optimization. When used with <i>-S</i> this generates LLVM intermediate language assembly files, otherwise this generates LLVM bitcode format object files (which may be passed to the linker depending on the stage selection options). </p>
<p> The default for <i>-flto</i> is “full”, in which the LLVM bitcode is suitable for monolithic Link Time Optimization (LTO), where the linker merges all such modules into a single combined module for optimization. With “thin”, ThinLTO compilation is invoked instead. </p>
<p> <code>NOTE:</code> On Darwin, when using <i>-flto</i> along with <code>-g</code> and compiling and linking in separate steps, you also need to pass <code>-Wl,-object_path_lto,&lt;lto-filename&gt;.o</code> at the linking step to instruct the ld64 linker not to delete the temporary object file generated during Link Time Optimization (this flag is automatically passed to the linker by Clang if compilation and linking are done in a single step). This allows debugging the executable as well as generating the <code>.dSYM</code> bundle using <code><a href="/docs/linux/man/1-dsymutil/">dsymutil</a>(1)</code>.</dl>
<h3>Driver Options</h3>
<dl>
<dt><code>-###</code></p>
<dd> Print (but do not run) the commands to run for this compilation.</p>
<dt><code>&#8211;help</code></p>
<dd> Display available options.</p>
<dt><code>-Qunused-arguments</code></p>
<dd> Do not emit any warnings for unused driver arguments.</p>
<dt><code>-Wa,&lt;args&gt;</code></p>
<dd> Pass the comma separated arguments in args to the assembler.</p>
<dt><code>-Wl,&lt;args&gt;</code></p>
<dd> Pass the comma separated arguments in args to the linker.</p>
<dt><code>-Wp,&lt;args&gt;</code></p>
<dd> Pass the comma separated arguments in args to the preprocessor.</p>
<dt><code>-Xanalyzer &lt;arg&gt;</code></p>
<dd> Pass arg to the static analyzer.</p>
<dt><code>-Xassembler &lt;arg&gt;</code></p>
<dd> Pass arg to the assembler.</p>
<dt><code>-Xlinker &lt;arg&gt;</code></p>
<dd> Pass arg to the linker.</p>
<dt><code>-Xpreprocessor &lt;arg&gt;</code></p>
<dd> Pass arg to the preprocessor.</p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Write output to file.</p>
<dt><code>-print-file-name=&lt;file&gt;</code></p>
<dd> Print the full library path of file.</p>
<dt><code>-print-libgcc-file-name</code></p>
<dd> Print the library path for the currently used compiler runtime library (“libgcc.a” or “libclang_rt.builtins.*.a”).</p>
<dt><code>-print-prog-name=&lt;name&gt;</code></p>
<dd> Print the full program path of name.</p>
<dt><code>-print-search-dirs</code></p>
<dd> Print the paths used for finding libraries and programs.</p>
<dt><code>-save-temps</code></p>
<dd> Save intermediate compilation results.</p>
<dt><code>-save-stats, -save-stats=cwd, -save-stats=obj</code></p>
<dd> Save internal code generation (LLVM) statistics to a file in the current directory (<i>-save-stats</i>/”-save-stats=cwd”) or the directory of the output file (“-save-state=obj”).</p>
<dt><code>-integrated-as, -no-integrated-as</code></p>
<dd> Used to enable and disable, respectively, the use of the integrated assembler. Whether the integrated assembler is on by default is target dependent.</p>
<dt><code>-time</code></p>
<dd> Time individual commands.</p>
<dt><code>-ftime-report</code></p>
<dd> Print timing summary of each stage of compilation.</p>
<dt><code>-v</code></p>
<dd> Show commands to run and use verbose output.</dl>
<h3>Diagnostics Options</h3>
<dl>
<dt><code>-fshow-column, -fshow-source-location, -fcaret-diagnostics, -fdiagnostics-fixit-info, -fdiagnostics-parseable-fixits, -fdiagnostics-print-source-range-info, -fprint-source-range-info, -fdiagnostics-show-option, -fmessage-length</code></p>
<dd> These options control how Clang prints out information about diagnostics (errors and warnings). Please see the Clang User’s Manual for more information.</dl>
<h3>Preprocessor Options</h3>
<dl>
<dt><code>-D&lt;macroname&gt;=&lt;value&gt;</code></p>
<dd> Adds an implicit #define into the predefines buffer which is read before the source file is preprocessed.</p>
<dt><code>-U&lt;macroname&gt;</code></p>
<dd> Adds an implicit #undef into the predefines buffer which is read before the source file is preprocessed.</p>
<dt><code>-include &lt;filename&gt;</code></p>
<dd> Adds an implicit #include into the predefines buffer which is read before the source file is preprocessed.</p>
<dt><code>-I&lt;directory&gt;</code></p>
<dd> Add the specified directory to the search path for include files.</p>
<dt><code>-F&lt;directory&gt;</code></p>
<dd> Add the specified directory to the search path for framework include files.</p>
<dt><code>-nostdinc</code></p>
<dd> Do not search the standard system directories or compiler builtin directories for include files.</p>
<dt><code>-nostdlibinc</code></p>
<dd> Do not search the standard system directories for include files, but do search compiler builtin include directories.</p>
<dt><code>-nobuiltininc</code></p>
<dd> Do not search clang’s builtin directory for include files.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TMPDIR, TEMP, TMP</code></p>
<dd> These environment variables are checked, in order, for the location to write temporary files used during the compilation process.</p>
<dt><code>CPATH</code></p>
<dd> If this environment variable is present, it is treated as a delimited list of paths to be added to the default system include path list. The delimiter is the platform dependent delimiter, as used in the PATH environment variable. </p>
<p> Empty components in the environment variable are ignored.</p>
<dt><code>C_INCLUDE_PATH, OBJC_INCLUDE_PATH, CPLUS_INCLUDE_PATH, OBJCPLUS_INCLUDE_PATH</code></p>
<dd> These environment variables specify additional paths, as for <i>CPATH</i>, which are only used when processing the appropriate language.</dl>
<h2>BUGS</h2>
<p> To report bugs, please visit &lt;<i><a rel="nofollow" href="https://github.com/llvm/llvm-project/issues/">https://github.com/llvm/llvm-project/issues/</a></i>&gt;. Most bug reports should include preprocessed source files (use the <i>-E</i> option) and the full output of the compiler, along with information to reproduce.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-as/">as</a>(1)</code>, <code><a href="/docs/linux/man/1-ld/">ld</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the Clang / LLVM Team (&lt;<a rel="nofollow" href="http://clang.llvm.org">http://clang.llvm.org</a>&gt;)</p>
<h2>COPYRIGHT</h2>
<p> 2007-2022, The Clang Team </p>
<h2>Index</h2>
