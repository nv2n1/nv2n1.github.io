---
title: "cli(1)"
name: "cli"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cli/"
description: "mono – Mono’s ECMA-CLI native code generator (Just-in-Time and Ahead-of-Time)"
---

<h2 class="name">NAME</h2>
<p> mono &#8211; Mono&#8217;s ECMA-CLI native code generator (Just-in-Time and Ahead-of-Time) </p>
<h2>SYNOPSIS</h2>
<p> <code>mono [options] file [arguments&#8230;]</code> </p>
<p> <code>mono-sgen [options] file [arguments&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>mono</i> is a runtime implementation of the ECMA Common Language Infrastructure. This can be used to run ECMA and .NET applications. </p>
<p> The runtime loads the specified <i>file</i> and optionally passes the <i>arguments</i> to it. The <i>file</i> is an ECMA assembly. They typically have a .exe or .dll extension. </p>
<p> These executables can reference additional functionality in the form of assembly references. By default those assembly references are resolved as follows: the <code>mscorlib.dll</code> is resolved from the system profile that is configured by Mono, and other assemblies are loaded from the Global Assembly Cache (GAC). </p>
<p> The runtime contains a native code generator that transforms the Common Intermediate Language into native code. </p>
<p> The code generator can operate in two modes: Just-in-time compilation (JIT) or Ahead-of-time compilation (AOT). Since code can be dynamically loaded, the runtime environment and the JIT are always present, even if code is compiled ahead of time. </p>
<p> The runtime provides a number of configuration options for running applications, for developing and debugging, and for testing and debugging the runtime itself. </p>
<p> The <i>mono</i> command uses the moving and generational SGen garbage collector while the <i>mono-boehm</i> command uses the conservative Boehm garbage collector.</p>
<h2>PORTABILITY</h2>
<p> On Unix-based systems, Mono provides a mechanism to emulate the Windows-style file access, this includes providing a case insensitive view of the file system, directory separator mapping (from \ to /) and stripping the drive letters. </p>
<p> This functionality is enabled by setting the <code>MONO_IOMAP </code> environment variable to one of <code>all, drive</code> and <code>case.</code> </p>
<p> See the description for <code>MONO_IOMAP</code> in the environment variables section for more details.</p>
<h2>METHOD DESCRIPTIONS</h2>
<p> A number of diagnostic command line options take as argument a method description. A method description is a textual representation that can be used to uniquely identify a method. The syntax is as follows: </p>
<pre><code>
[namespace] classname : methodname[(arguments)]
</code></pre>
<p> The values in brackets are optional, like the namespace and the arguments. The arguments themselves are either empty, or a comma-separated list of arguments. Both the <code>classname</code> and <code>methodname</code> can be set to the special value &#8216;*&#8217; to match any values (Unix shell users should escape the argument to avoid the shell interpreting this). </p>
<p> The arguments, if present should be a comma separated list of types either a full typename, or for built-in types it should use the low-level ILAsm type names for the built-in types, like &#8216;void&#8217;, &#8216;char&#8217;, &#8216;bool&#8217;, &#8216;byte&#8217;, &#8216;sbyte&#8217;, &#8216;uint16&#8217;, &#8216;int16&#8217;, &#8216;uint&#8217;, </p>
<p> Pointer types should be the name of the type, followed by a &#8216;*&#8217;, arrays should be the typename followed by &#8216;[&#8216; one or more commas (to indicate the rank of the array), and &#8216;]&#8217;. </p>
<p> Generic values should use &#8216;&lt;&#8216;, one or more type names, separated by both a comma and a space and &#8216;&gt;&#8217;. </p>
<p> By-reference arguments should include a &quot;&amp;&quot; after the typename. </p>
<p> Examples:<br />
* : ctor(int)                  // All constructors that take an int as an argument<br />
    * : Main                   // Methods named Main in any class<br />
            * : Main(string[]) // Methods named Main that take a string array in any class</p>
<h2>RUNTIME OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt><code>&#8211;aot</code>, <code>&#8211;aot[=options]</code></p>
<dd> This option is used to precompile the CIL code in the specified assembly to native code. The generated code is stored in a file with the extension .so. This file will be automatically picked up by the runtime when the assembly is executed. Ahead-of-Time compilation is most useful if you use it in combination with the -O=all,-shared flag which enables all of the optimizations in the code generator to be performed. Some of those optimizations are not practical for Just-in-Time compilation since they might be very time consuming. Unlike the .NET Framework, Ahead-of-Time compilation will not generate domain independent code: it generates the same code that the Just-in-Time compiler would produce. Since most applications use a single domain, this is fine. If you want to optimize the generated code for use in multi-domain applications, consider using the -O=shared flag. This pre-compiles the methods, but the original assembly is still required to execute as this one contains the metadata and exception information which is not available on the generated file. When precompiling code, you might want to compile with all optimizations (-O=all). Pre-compiled code is position independent code. Precompilation is just a mechanism to reduce startup time, increase code sharing across multiple mono processes and avoid just-in-time compilation program startup costs. The original assembly must still be present, as the metadata is contained there. AOT code typically can not be moved from one computer to another (CPU-specific optimizations that are detected at runtime) so you should not try to move the pre-generated assemblies or package the pre-generated assemblies for deployment. A few options are available as a parameter to the <code>&#8211;aot </code> command line option. The options are separated by commas, and more than one can be specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>asmonly</i></p>
<dd> Instructs the AOT compiler to output assembly code instead of an object file.</p>
<dt><i>bind-to-runtime-version</i></p>
<dd> If specified, forces the generated AOT files to be bound to the runtime version of the compiling Mono. This will prevent the AOT files from being consumed by a different Mono runtime.</p>
<dt><i>data-outfile=FILE.dll.aotdata</i></p>
<dd> This instructs the AOT code generator to output certain data constructs into a separate file. This can reduce the executable images some five to twenty percent. Developers need to then ship the resulting aotdata as a resource and register a hook to load the data on demand by using the <i>mono_install_load_aot_data_hook</i> method.</p>
<dt><i>direct-icalls</i></p>
<dd> When this option is specified, icalls (internal calls made from the standard library into the mono runtime code) are invoked directly instead of going through the operating system symbol lookup operation. This requires use of the <i>static</i> option.</p>
<dt><i>direct-pinvoke</i></p>
<dd> When this option is specified, P/Invoke methods are invoked directly instead of going through the operating system symbol lookup operation. This requires use of the <i>static</i> option.</p>
<dt><i>dwarfdebug</i></p>
<dd> Instructs the AOT compiler to emit DWARF debugging information. When used together with the nodebug option, only DWARF debugging information is emitted, but not the information that can be used at runtime.</p>
<dt><i>full</i></p>
<dd> This creates binaries which can be used with the &#8211;full-aot option.</p>
<dt><i>hybrid</i></p>
<dd> This creates binaries which can be used with the &#8211;hybrid-aot option.</p>
<dt><i>llvm</i></p>
<dd> AOT will be performed with the LLVM backend instead of the Mono backend where possible. This will be slower to compile but most likely result in a performance improvement.</p>
<dt><i>llvmonly</i></p>
<dd> AOT will be performed with the LLVM backend exclusively and the Mono backend will not be used. The only output in this mode will be the bitcode file normally specified with the <i>llvm-outfile</i> option. Use of <i>llvmonly</i> automatically enables the <i>full</i> and <i>llvm</i> options. This feature is experimental.</p>
<dt><i>llvmopts=[options]</i></p>
<dd> Use this option to add more flags to the built-in set of flags passed to the LLVM optimizer. When you invoke the <i>mono</i> command with the <i>&#8211;aot=llvm </i> it displays the current list of flags that are being passed to the <i>opt</i> command. <i>The list of possible flags that can be passed can be</i> obtained by calling the bundled <i>opt </i> program that comes with Mono, and calling it like this: </p>
<pre>
        opt --help
</pre>
<dt><i>llvmllc=[options]</i></p>
<dd> Use this option to add more flags to the built-in set of flags passed to the LLVM static compiler (llc). The list of possible flags that can be passed can be obtained by calling the bundled <i>llc</i> program that comes with Mono, and calling it like this: </p>
<pre>
        llc --help
</pre>
<dt><i>mcpu=[native o generic]</i></p>
<dd> cpu=native allows AOT mode to use all instructions current CPU supports, e.g. AVX2, SSE42, etc. Default value is &#8216;generic&#8217;. <i>mattr=[cpu feature]</i> Allows AOT code generator to use specified CPU features where possible including `System.Runtime.Intrinsics.*&#8217;. E.g. `mattr=+avx2,mattr=-lzcnt&#8217; unlocks sse1-4.2, avx1-2 and disables lzcnt. It&#8217;s useful for cross-compilation or when it&#8217;s not possible to use `-mcpu=native&#8217; (which enables all cpu feature current cpu has). <i>llvm-outfile=[filename]</i> Gives the path for the temporary LLVM bitcode file created during AOT. <i>dedup</i> Each AOT module will typically contain the code for inflated methods and wrappers that are called by code in that module. In dedup mode, we identify and skip compiling all of those methods. When using this mode with fullaot, dedup-include is required or these methods will remain missing.</p>
<dt><i>dedup-include=[filename]</i></p>
<dd> In dedup-include mode, we are in the pass of compilation where we compile the methods that we had previously skipped. All of them are emitted into the assembly that is passed as this option. We consolidate the many duplicate skipped copies of the same method into one.</p>
<dt>
<dt><i>info</i></p>
<dd>
<dd> Print the architecture the AOT in this copy of Mono targets and quit.</p>
<dt><i>interp</i></p>
<dd> Generates all required wrappers, so that it is possible to run &#8211;interpreter without any code generation at runtime. This option only makes sense with <code>mscorlib.dll</code>. Embedders can set</p>
<dt><i>depfile=[filename]</i></p>
<dd> Outputs a gcc -M style dependency file. </p>
<pre>
mono_jit_set_aot_mode (MONO_AOT_MODE_INTERP);
</pre>
<dt><i>ld-flags</i></p>
<dd> Additional flags to pass to the C linker (if the current AOT mode calls for invoking it).</p>
<dt><i>llvm-path=&lt;PREFIX&gt;</i></p>
<dd> Same for the llvm tools &#8216;opt&#8217; and &#8216;llc&#8217;.</p>
<dt><i>msym-dir=&lt;PATH&gt;</i></p>
<dd> Instructs the AOT compiler to generate offline sequence points .msym files. The generated .msym files will be stored into a subfolder of &lt;PATH&gt; named as the compilation AOTID.</p>
<dt><i>mtriple=&lt;TRIPLE&gt;</i></p>
<dd> Use the GNU style target triple &lt;TRIPLE&gt; to determine some code generation options, i.e. &#8211;mtriple=armv7-linux-gnueabi will generate code that targets ARMv7. This is currently only supported by the ARM backend. In LLVM mode, this triple is passed on to the LLVM llc compiler.</p>
<dt><i>nimt-trampolines=[number]</i></p>
<dd> When compiling in full aot mode, the IMT trampolines must be precreated in the AOT image. You can add additional method trampolines with this argument. Defaults to 512.</p>
<dt><i>ngsharedvt-trampolines=[number]</i></p>
<dd> When compiling in full aot mode, the value type generic sharing trampolines must be precreated in the AOT image. You can add additional method trampolines with this argument. Defaults to 512.</p>
<dt><i>nodebug</i></p>
<dd> Instructs the AOT compiler to not output any debugging information.</p>
<dt><i>no-direct-calls</i></p>
<dd> This prevents the AOT compiler from generating a direct calls to a method. The AOT compiler usually generates direct calls for certain methods that do not require going through the PLT (for example, methods that are known to not require a hook like a static constructor) or call into simple internal calls.</p>
<dt><i>nrgctx-trampolines=[number]</i></p>
<dd> When compiling in full aot mode, the generic sharing trampolines must be precreated in the AOT image. You can add additional method trampolines with this argument. Defaults to 4096.</p>
<dt><i>nrgctx-fetch-trampolines=[number]</i></p>
<dd> When compiling in full aot mode, the generic sharing fetch trampolines must be precreated in the AOT image. You can add additional method trampolines with this argument. Defaults to 128.</p>
<dt><i>ntrampolines=[number]</i></p>
<dd> When compiling in full aot mode, the method trampolines must be precreated in the AOT image. You can add additional method trampolines with this argument. Defaults to 4096.</p>
<dt><i>outfile=[filename]</i></p>
<dd> Instructs the AOT compiler to save the output to the specified file.</p>
<dt><i>print-skipped-methods</i></p>
<dd> If the AOT compiler cannot compile a method for any reason, enabling this flag will output the skipped methods to the console.</p>
<dt><i>profile=[file]</i></p>
<dd> Specify a file to use for profile-guided optimization. See the <code>AOT profiler</code> sub-section. To specify multiple files, include the <i>profile</i> option multiple times.</p>
<dt><i>profile-only</i></p>
<dd> AOT *only* the methods described in the files specified with the <i>profile</i> option. See the <code>AOT profiler</code> sub-section.</p>
<dt><i>readonly-value=namespace.typename.fieldname=type/value</i></p>
<dd> Override the value of a static readonly field. Usually, during JIT compilation, the static constructor is ran eagerly, so the value of a static readonly field is known at compilation time and the compiler can do a number of optimizations based on it. During AOT, instead, the static constructor can&#8217;t be ran, so this option can be used to set the value of such a field and enable the same set of optimizations. Type can be any of i1, i2, i4 for integers of the respective sizes (in bytes). Note that signed/unsigned numbers do not matter here, just the storage size. This option can be specified multiple times and it doesn&#8217;t prevent the static constructor for the type defining the field to execute with the usual rules at runtime (hence possibly computing a different value for the field).</p>
<dt><i>save-temps,keep-temps</i></p>
<dd> Instructs the AOT compiler to keep temporary files.</p>
<dt><i>soft-debug</i></p>
<dd> This instructs the compiler to generate sequence point checks that allow Mono&#8217;s soft debugger to debug applications even on systems where it is not possible to set breakpoints or to single step (certain hardware configurations like the cell phones and video gaming consoles).</p>
<dt><i>static</i></p>
<dd> Create an ELF object file (.o) or .s file which can be statically linked into an executable when embedding the mono runtime. When this option is used, the object file needs to be registered with the embedded runtime using the mono_aot_register_module function which takes as its argument the mono_aot_module_&lt;ASSEMBLY NAME&gt;_info global symbol from the object file: </p>
<p>extern void *mono_aot_module_hello_info;<br />
mono_aot_register_module(mono_aot_module_hello_info);</p>
<dt><i>stats</i></p>
<dd> Print various stats collected during AOT compilation.</p>
<dt><i>temp-path=[path]</i></p>
<dd> Explicitly specify path to store temporary files created during AOT compilation.</p>
<dt><i>threads=[number]</i></p>
<dd> This is an experimental option for the AOT compiler to use multiple threads when compiling the methods.</p>
<dt><i>tool-prefix=&lt;PREFIX&gt;</i></p>
<dd> Prepends &lt;PREFIX&gt; to the name of tools ran by the AOT compiler, i.e. &#8216;as&#8217;/&#8217;ld&#8217;. For example, &#8211;tool=prefix=arm-linux-gnueabi- will make the AOT compiler run</p>
<dt><i>verbose</i></p>
<dd> Prints additional information about type loading failures.</p>
<dt><i>write-symbols,no-write-symbols</i></p>
<dd> Instructs the AOT compiler to emit (or not emit) debug symbol information.</p>
<dt><i>no-opt</i></p>
<dd> Instructs the AOT compiler tot no call opt when compiling with LLVM.</dl>
<p> For more information about AOT, see: <a rel="nofollow" href="http://www.mono-project.com/docs/advanced/aot/">http://www.mono-project.com/docs/advanced/aot/</a></dl>
<dt><code>&#8211;aot-path=PATH</code></p>
<dd> List of additional directories to search for AOT images.</p>
<dt><code>&#8211;apply-bindings=FILE</code></p>
<dd> Apply the assembly bindings from the specified configuration file when running the AOT compiler. This is useful when compiling an auxiliary assembly that is referenced by a main assembly that provides a configuration file. For example, if app.exe uses lib.dll then in order to make the assembly bindings from app.exe.config available when compiling lib.dll ahead of time, use: </p>
<pre>
        mono --apply-bindings=app.exe.config --aot lib.dll
</pre>
<dt><code>&#8211;assembly-loader=MODE</code></p>
<dd> If mode is <code>strict</code>, Mono will check that the public key token, culture and version of a candidate assembly matches the requested strong name. If mode is <code>legacy</code>, as long as the name matches, the candidate will be allowed. <code>strict</code> is the behavior consistent with .NET Framework but may break some existing mono-based applications. The default is <code>legacy</code>.</p>
<dt><code>&#8211;attach=[options]</code></p>
<dd> Currently the only option supported by this command line argument is <code>disable</code> which disables the attach functionality.</p>
<dt><code>&#8211;config filename</code></p>
<dd> Load the specified configuration file instead of the default one(s). The default files are /etc/mono/config and ~/.mono/config or the file specified in the MONO_CONFIG environment variable, if set. See the <a href="/docs/linux/man/5-mono-config/">mono-config</a>(5) man page for details on the format of this file.</p>
<dt><code>&#8211;debugger-agent=[options]</code></p>
<dd> This instructs the Mono runtime to start a debugging agent inside the Mono runtime and connect it to a client user interface will control the Mono process. This option is typically used by IDEs, like the MonoDevelop or Visual Studio IDEs.</p>
<dl>
<dt>
<dd> The configuration is specified using one of more of the following options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>address=host:port</i></p>
<dd> Use this option to specify the IP address where your debugger client is listening to.</p>
<dt><i>loglevel=LEVEL</i></p>
<dd> Specifies the diagnostics log level for</p>
<dt><i>logfile=filename</i></p>
<dd> Used to specify the file where the log will be stored, it defaults to standard output.</p>
<dt><i>server=[y/n]</i></p>
<dd> Defaults to no, with the default option Mono will actively connect to the host/port configured with the <code>address</code> option. If you set it to &#8216;y&#8217;, it instructs the Mono runtime to start debugging in server mode, where Mono actively waits for the debugger front end to connect to the Mono process. Mono will print out to stdout the IP address and port where it is listening.</p>
<dt><i>setpgid=[y/n]</i></p>
<dd> If set to yes, Mono will call <code>setpgid(0, 0)</code> on startup, if that function is available on the system. This is useful for ensuring that signals delivered to a process that is executing the debuggee are not propagated to the debuggee, e.g. when Ctrl-C sends <code>SIGINT</code> to the <code>sdb</code> tool.</p>
<dt><i>suspend=[y/n]</i></p>
<dd> Defaults to yes, with the default option Mono will suspend the vm on startup until it connects successfully to a debugger front end. If you set it to &#8216;n&#8217;, in conjunction with <code>server=y</code>, it instructs the Mono runtime to run as normal, while caching metadata to send to the debugger front end on connection..</p>
<dt><i>transport=transport_name</i></p>
<dd> This is used to specify the transport that the debugger will use to communicate. It must be specified and currently requires this to be &#8216;dt_socket&#8217;.</dl>
</dl>
<dl>
<dt><code>&#8211;desktop</code></p>
<dd> Configures the virtual machine to be better suited for desktop applications. Currently this sets the GC system to avoid expanding the heap as much as possible at the expense of slowing down garbage collection a bit.</p>
<dt><code>&#8211;full-aot</code></p>
<dd> This flag instructs the Mono runtime to not generate any code at runtime and depend exclusively on the code generated from using mono &#8211;aot=full previously. This is useful for platforms that do not permit dynamic code generation, or if you need to run assemblies that have been stripped of IL (for example using mono-cil-strip). Notice that this feature will abort execution at runtime if a codepath in your program, or Mono&#8217;s class libraries attempts to generate code dynamically. You should test your software upfront and make sure that you do not use any dynamic features.</p>
<dt><code>&#8211;full-aot-interp</code></p>
<dd> Same as &#8211;full-aot with fallback to the interpreter.</p>
<dt><code>&#8211;gc=boehm</code>, <code>&#8211;gc=sgen</code></p>
<dd> Selects the Garbage Collector engine for Mono to use, Boehm or SGen. Currently this merely ensures that you are running either the <i>mono</i> or <i>mono-sgen</i> commands. This flag can be set in the <code>MONO_ENV_OPTIONS</code> environment variable to force all of your child processes to use one particular kind of GC with the Mono runtime.</p>
<dt><code>&#8211;gc-debug=[options]</code></p>
<dd> Command line equivalent of the <code>MONO_GC_DEBUG</code> environment variable.</p>
<dt><code>&#8211;gc-params=[options]</code></p>
<dd> Command line equivalent of the <code>MONO_GC_PARAMS</code> environment variable.</p>
<dt><code>&#8211;arch=32</code>, <code>&#8211;arch=64</code></p>
<dd> (Mac OS X only): Selects the bitness of the Mono binary used, if available. If the binary used is already for the selected bitness, nothing changes. If not, the execution switches to a binary with the selected bitness suffix installed side by side (for example, &#8216;/bin/mono &#8211;arch=64&#8217; will switch to &#8216;/bin/mono64&#8217; iff &#8216;/bin/mono&#8217; is a 32-bit build).</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Displays usage instructions.</p>
<dt><code>&#8211;interpreter</code></p>
<dd> The Mono runtime will use its interpreter to execute a given assembly. The interpreter is usually slower than the JIT, but it can be useful on platforms where code generation at runtime is not allowed.</p>
<dt><code>&#8211;hybrid-aot</code></p>
<dd> This flag allows the Mono runtime to run assemblies that have been stripped of IL, for example using mono-cil-strip. For this to work, the assembly must have been AOT compiled with &#8211;aot=hybrid. </p>
<p> This flag is similar to &#8211;full-aot, but it does not disable the JIT. This means you can use dynamic features such as System.Reflection.Emit.</p>
<dt><code>&#8211;llvm</code></p>
<dd> If the Mono runtime has been compiled with LLVM support (not available in all configurations), Mono will use the LLVM optimization and code generation engine to JIT or AOT compile. For more information, consult: <a rel="nofollow" href="http://www.mono-project.com/docs/advanced/mono-llvm/">http://www.mono-project.com/docs/advanced/mono-llvm/</a></p>
<dt><code>&#8211;ffast-math</code></p>
<dd> This flag allows Mono and LLVM to apply aggressive floating point optimizations. Can break IEEE754 compliance.</p>
<dt><code>&#8211;nollvm</code></p>
<dd> When using a Mono that has been compiled with LLVM support, it forces Mono to fallback to its JIT engine and not use the LLVM backend.</p>
<dt><code>&#8211;optimize=MODE</code>, <code>-O=MODE</code></p>
<dd> MODE is a comma separated list of optimizations. They also allow optimizations to be turned off by prefixing the optimization name with a minus sign. In general, Mono has been tuned to use the default set of flags, before using these flags for a deployment setting, you might want to actually measure the benefits of using them. The following optimization flags are implemented in the core engine:<br />
abcrem Array bound checks removal<br />
        all Turn on all optimizations<br />
            aot Usage of Ahead Of Time compiled code<br />
                branch Branch optimizations<br />
                    cfold Constant folding<br />
                        cmov Conditional moves[arch &#8211; dependency] deadce Dead code elimination<br />
                            consprop Constant propagation<br />
                                copyprop Copy propagation<br />
                                    fcmov Fast x86 FP compares[arch &#8211; dependency] float32 Perform 32 &#8211;<br />
    bit float arithmetic using 32 &#8211; bit operations gshared Enable generic code sharing.inline Inline method calls intrins Intrinsic method implementations linears Linear scan global reg allocation leaf Leaf procedures optimizations loop Loop related optimizations peephole Peephole postpass precomp Precompile all methods before executing Main sched Instruction scheduling shared Emit per &#8211; domain code sse2 SSE2 instructions on x86[arch &#8211; dependency] tailc Tail recursion and tail calls<br />
 For example, to enable all the optimization but dead code elimination and inlining, you can use: </p>
<pre>
        -O=all,-deadce,-inline
</pre>
<p> The flags that are flagged with [arch-dependency] indicate that the given option if used in combination with Ahead of Time compilation (&#8211;aot flag) would produce pre-compiled code that will depend on the current CPU and might not be safely moved to another computer.</p>
<dl>
<dt>
<dd>
<p> The following optimizations are supported</p>
<dl>
<dt><i>float32</i></p>
<dd> Requests that the runtime performn 32-bit floating point operations using only 32-bits. By default the Mono runtime tries to use the highest precision available for floating point operations, but while this might render better results, the code might run slower. This options also affects the code generated by the LLVM backend.</p>
<dt><i>inline</i></p>
<dd> Controls whether the runtime should attempt to inline (the default), or not inline methods invocations</dl>
</dl>
<p> <code>&#8211;response=FILE</code> Provides a response file, this instructs the Mono command to read other command line options from the specified file, as if the options had been specified on the command line. Useful when you have very long command lines.</p>
<dt><code>&#8211;runtime=VERSION</code></p>
<dd> Mono supports different runtime versions. The version used depends on the program that is being run or on its configuration file (named program.exe.config). This option can be used to override such autodetection, by forcing a different runtime version to be used. Note that this should only be used to select a later compatible runtime version than the one the program was compiled against. A typical usage is for running a 1.1 program on a 2.0 version: </p>
<pre>
         mono --runtime=v2.0.50727 program.exe
</pre>
<dt><code>&#8211;server</code></p>
<dd> Configures the virtual machine to be better suited for server operations (currently, allows a heavier threadpool initialization).</p>
<dt><code>&#8211;use-map-jit</code></p>
<dd> Instructs Mono to generate code using MAP_JIT on MacOS. Necessary for bundled applications.</p>
<dt><code>&#8211;verify-all</code></p>
<dd> Verifies mscorlib and assemblies in the global assembly cache for valid IL, and all user code for IL verifiability. </p>
<p> This is different from <code>&#8211;security</code>&#8216;s verifiable or validil in that these options only check user code and skip mscorlib and assemblies located on the global assembly cache.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Prints JIT version information (system configuration, release number and branch names if available).</p>
<dt><code>&#8211;version=number</code></p>
<dd> Print version number only. </p>
</dl>
</dl>
</dl>
<h2>DEVELOPMENT OPTIONS</h2>
<p> The following options are used to help when developing a JITed application.</p>
<dl>
<dt><code>&#8211;debug</code>, <code>&#8211;debug=OPTIONS</code></p>
<dd> Turns on the debugging mode in the runtime. If an assembly was compiled with debugging information, it will produce line number information for stack traces.</p>
<dl>
<dt>
<dd>
<p> The optional OPTIONS argument is a comma separated list of debugging options. These options are turned off by default since they generate much larger and slower code at runtime.</p>
<dl>
<dt>The following options are supported:</p>
<dd>
<dt><i>casts</i></p>
<dd> Produces a detailed error when throwing a InvalidCastException. This option needs to be enabled as this generates more verbose code at execution time.</p>
<dt><i>mdb-optimizations</i></p>
<dd> Disable some JIT optimizations which are usually only disabled when running inside the debugger. This can be helpful if you want to attach to the running process with mdb.</p>
<dt><i>gdb</i></p>
<dd> Generate and register debugging information with gdb. This is only supported on some platforms, and only when using gdb 7.0 or later.</dl>
</dl>
<dt><code>&#8211;profile</code>[=<i>profiler</i>[:<i>profiler_args</i>]]</p>
<dd> Loads a profiler module with the given arguments. For more information, see the <code>PROFILING</code> section. This option can be used multiple times; each time will load an additional profiler module.</p>
<dt><code>&#8211;trace[=expression]</code></p>
<dd> Shows method names as they are invoked. By default all methods are traced. The trace can be customized to include or exclude methods, classes or assemblies. A trace expression is a comma separated list of targets, each target can be prefixed with a minus sign to turn off a particular target. The words `program&#8217;, `all&#8217; and `disabled&#8217; have special meaning. `program&#8217; refers to the main program being executed, and `all&#8217; means all the method calls. The `disabled&#8217; option is used to start up with tracing disabled. It can be enabled at a later point in time in the program by sending the SIGUSR2 signal to the runtime. Assemblies are specified by their name, for example, to trace all calls in the System assembly, use: </p>
<pre>
        mono --trace=System app.exe
</pre>
<p> Classes are specified with the T: prefix. For example, to trace all calls to the System.String class, use: </p>
<pre>
        mono --trace=T:System.String app.exe
</pre>
<p> And individual methods are referenced with the M: prefix, and the standard method notation: </p>
<pre>
        mono --trace=M:System.Console:WriteLine app.exe
</pre>
<p> Exceptions can also be traced, it will cause a stack trace to be printed every time an exception of the specified type is thrown. The exception type can be specified with or without the namespace, and to trace all exceptions, specify &#8216;all&#8217; as the type name. </p>
<pre>
        mono --trace=E:System.Exception app.exe
</pre>
<p> As previously noted, various rules can be specified at once: </p>
<pre>
        mono --trace=T:System.String,T:System.Random app.exe
</pre>
<p> You can exclude pieces, the next example traces calls to System.String except for the System.String:Concat method. </p>
<pre>
        mono --trace=T:System.String,-M:System.String:Concat
</pre>
<p> You can trace managed to unmanaged transitions using the wrapper qualifier: </p>
<pre>
        mono --trace=wrapper app.exe
</pre>
<p> Finally, namespaces can be specified using the N: prefix: </p>
<pre>
        mono --trace=N:System.Xml
</pre>
<dt><code>&#8211;no-x86-stack-align</code></p>
<dd> Don&#8217;t align stack frames on the x86 architecture. By default, Mono aligns stack frames to 16 bytes on x86, so that local floating point and SIMD variables can be properly aligned. This option turns off the alignment, which usually saves one instruction per call, but might result in significantly lower floating point and SIMD performance.</p>
<dt><code>&#8211;jitmap</code></p>
<dd> Generate a JIT method map in a /tmp/perf-PID.map file. This file is then used, for example, by the perf tool included in recent Linux kernels. Each line in the file has: </p>
<pre>
        HEXADDR HEXSIZE methodname
</pre>
<p> Currently this option is only supported on Linux.</dl>
<h2>JIT MAINTAINER OPTIONS</h2>
<p> The maintainer options are only used by those developing the runtime itself, and not typically of interest to runtime users or developers.</p>
<dl>
<dt><code>&#8211;bisect=optimization:filename</code></p>
<dd> This flag is used by the automatic optimization bug bisector. It takes an optimization flag and a filename of a file containing a list of full method names, one per line. When it compiles one of the methods in the file it will use the optimization given, in addition to the optimizations that are otherwise enabled. Note that if the optimization is enabled by default, you should disable it with `-O`, otherwise it will just apply to every method, whether it&#8217;s in the file or not.</p>
<dt><code>&#8211;break method</code></p>
<dd> Inserts a breakpoint before the method whose name is `method&#8217; (namespace.class:methodname). Use `Main&#8217; as method name to insert a breakpoint on the application&#8217;s main method. You can use it also with generics, for example &quot;System.Collections.Generic.Queue`1:Peek&quot;</p>
<dt><code>&#8211;breakonex</code></p>
<dd> Inserts a breakpoint on exceptions. This allows you to debug your application with a native debugger when an exception is thrown.</p>
<dt><code>&#8211;compile name</code></p>
<dd> This compiles a method (namespace.name:methodname), this is used for testing the compiler performance or to examine the output of the code generator.</p>
<dt><code>&#8211;compile-all</code></p>
<dd> Compiles all the methods in an assembly. This is used to test the compiler performance or to examine the output of the code generator</p>
<dt><code>&#8211;graph=TYPE METHOD</code></p>
<dd> This generates a postscript file with a graph with the details about the specified method (namespace.name:methodname). This requires `dot&#8217; and ghostview to be installed (it expects Ghostview to be called &quot;gv&quot;). The following graphs are available: </p>
<pre>
          cfg        Control Flow Graph (CFG)
          dtree      Dominator Tree
          code       CFG showing code
          ssa        CFG showing code after SSA translation
          optcode    CFG showing code after IR optimizations
</pre>
<p> Some graphs will only be available if certain optimizations are turned on.</p>
<dt><code>&#8211;ncompile</code></p>
<dd> Instruct the runtime on the number of times that the method specified by &#8211;compile (or all the methods if &#8211;compile-all is used) to be compiled. This is used for testing the code generator performance.</p>
<dt><code>&#8211;stats</code></p>
<dd> Displays information about the work done by the runtime during the execution of an application.</p>
<dt><code>&#8211;wapi=hps|semdel</code></p>
<dd> Perform maintenance of the process shared data. semdel will delete the global semaphore. hps will list the currently used handles.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Increases the verbosity level, each time it is listed, increases the verbosity level to include more information (including, for example, a disassembly of the native code produced, code selector info etc.).</dl>
<h2>ATTACH SUPPORT</h2>
<p> The Mono runtime allows external processes to attach to a running process and load assemblies into the running program. To attach to the process, a special protocol is implemented in the Mono.Management assembly. </p>
<p> With this support it is possible to load assemblies that have an entry point (they are created with -target:exe or -target:winexe) to be loaded and executed in the Mono process. </p>
<p> The code is loaded into the root domain, and it starts execution on the special runtime attach thread. The attached program should create its own threads and return after invocation. </p>
<p> This support allows for example debugging applications by having the csharp shell attach to running processes.</p>
<h2>PROFILING</h2>
<p> The Mono runtime includes a profiler API that dynamically loaded profiler modules and embedders can use to collect performance-related data about an application. Profiler modules are loaded by passing the <code>&#8211;profile</code> command line argument to the Mono runtime. </p>
<p> Mono ships with a few profiler modules, of which the <code>log</code> profiler is the most feature-rich. It is also the default profiler if the <i>profiler</i> argument is not given, or if <code>default</code> is given. It is possible to write your own profiler modules; see the <code>Custom profilers</code> sub-section.</p>
<h3>Log profiler</h3>
<p> The log profiler can be used to collect a lot of information about a program running in the Mono runtime. This data can be used (both while the process is running and later) to do analyses of the program behavior, determine resource usage, performance issues or even look for particular execution patterns. </p>
<p> This is accomplished by logging the events provided by the Mono runtime through the profiler API and periodically writing them to a file which can later be inspected with the <code><a href="/docs/linux/man/1-mprof-report/">mprof-report</a></code>(1) tool. </p>
<p> More information about how to use the log profiler is available on the <code><a href="/docs/linux/man/1-mono-profilers/">mono-profilers</a></code>(1) page, under the <code>LOG PROFILER</code> section, as well as the <code><a href="/docs/linux/man/1-mprof-report/">mprof-report</a></code>(1) page.</p>
<h3>Coverage profiler</h3>
<p> The code coverage profiler can instrument a program to help determine which classes, methods, code paths, etc are actually executed. This is most useful when running a test suite to determine whether the tests actually cover the code they&#8217;re expected to. </p>
<p> More information about how to use the coverage profiler is available on the <code><a href="/docs/linux/man/1-mono-profilers/">mono-profilers</a></code>(1) page, under the <code>COVERAGE PROFILER</code> section.</p>
<h3>AOT profiler</h3>
<p> The AOT profiler can help improve startup performance by logging which generic instantiations are used by a program, which the AOT compiler can then use to compile those instantiations ahead of time so that they won&#8217;t have to be JIT compiled at startup. </p>
<p> More information about how to use the AOT profiler is available on the <code><a href="/docs/linux/man/1-mono-profilers/">mono-profilers</a></code>(1) page, under the <code>AOT PROFILER</code> section.</p>
<h3>Custom profilers</h3>
<p> Custom profiler modules can be loaded in exactly the same way as the standard modules that ship with Mono. They can also access the same profiler API to gather all kinds of information about the code being executed. </p>
<p> For example, to use a third-party profiler called <code>custom</code>, you would load it like this: </p>
<pre>
<dl><dt><dd>mono --profile=custom program.exe
</dl>
</pre>
<p> You could also pass arguments to it: </p>
<pre>
<dl><dt><dd>mono --profile=custom:arg1,arg2=arg3 program.exe
</dl>
</pre>
<p> In the above example, Mono will load the profiler from the shared library called <i>libmono-profiler-custom.so</i> (name varies based on platform, e.g., <i>libmono-profiler-custom.dylib</i> on OS X). This profiler module must be on your dynamic linker library path (<code>LD_LIBRARY_PATH</code> on most systems, <code>DYLD_LIBRARY_PATH</code> on OS X). </p>
<p> For a sample of how to write your own custom profiler, look at the <i>samples/profiler/sample.c</i> file in the Mono source tree.</p>
<h2>DEBUGGING AIDS</h2>
<p> To debug managed applications, you can use the <code>mdb</code> command, a command line debugger. </p>
<p> It is possible to obtain a stack trace of all the active threads in Mono by sending the QUIT signal to Mono, you can do this from the command line, like this: </p>
<pre>
        kill -QUIT pid
</pre>
<p> Where pid is the Process ID of the Mono process you want to examine. The process will continue running afterwards, but its state is not guaranteed. </p>
<p> <code>Important:</code> this is a last-resort mechanism for debugging applications and should not be used to monitor or probe a production application. The integrity of the runtime after sending this signal is not guaranteed and the application might crash or terminate at any given point afterwards. </p>
<p> The <code>&#8211;debug=casts</code> option can be used to get more detailed information for Invalid Cast operations, it will provide information about the types involved. </p>
<p> You can use the MONO_LOG_LEVEL and MONO_LOG_MASK environment variables to get verbose debugging output about the execution of your application within Mono. </p>
<p> The <i>MONO_LOG_LEVEL</i> environment variable if set, the logging level is changed to the set value. Possible values are &quot;error&quot;, &quot;critical&quot;, &quot;warning&quot;, &quot;message&quot;, &quot;info&quot;, &quot;debug&quot;. The default value is &quot;error&quot;. Messages with a logging level greater then or equal to the log level will be printed to stdout/stderr. </p>
<p> Use &quot;info&quot; to track the dynamic loading of assemblies. </p>
<p> Use the <i>MONO_LOG_MASK</i> environment variable to limit the extent of the messages you get: If set, the log mask is changed to the set value. Possible values are &quot;asm&quot; (assembly loader), &quot;type&quot;, &quot;dll&quot; (native library loader), &quot;gc&quot; (garbage collector), &quot;cfg&quot; (config file loader), &quot;aot&quot; (precompiler), &quot;security&quot; (e.g. Moonlight CoreCLR support), &quot;threadpool&quot; (thread pool generic), &quot;io-selector&quot; (async socket operations), &quot;io-layer&quot; (I/O layer &#8211; processes, files, sockets, events, semaphores, mutexes and handles), &quot;io-layer-process&quot;, &quot;io-layer-file&quot;, &quot;io-layer-socket&quot;, &quot;io-layer-event&quot;, &quot;io-layer-semaphore&quot;, &quot;io-layer-mutex&quot;, &quot;io-layer-handle&quot; and &quot;all&quot;. The default value is &quot;all&quot;. Changing the mask value allows you to display only messages for a certain component. You can use multiple masks by comma separating them. For example to see config file messages and assembly loader messages set you mask to &quot;asm,cfg&quot;. </p>
<p> The following is a common use to track down problems with P/Invoke: </p>
<pre>
        $ MONO_LOG_LEVEL=&quot;debug&quot; MONO_LOG_MASK=&quot;dll&quot; mono glue.exe
</pre>
<h2>DEBUGGING WITH LLDB</h2>
<p> If you are using LLDB, you can use the <code>mono.py</code> script to print some internal data structures with it. To use this, add this to your <code>$HOME/.lldbinit</code> file: </p>
<pre>
command script import $PREFIX/lib/mono/lldb/mono.py
</pre>
<p> Where $PREFIX is the prefix value that you used when you configured Mono (typically /usr). </p>
<p> Once this is done, then you can inspect some Mono Runtime data structures, for example: </p>
<pre>
(lldb) p method
(MonoMethod *) $0 = 0x05026ac0 [mscorlib]System.OutOfMemoryException:.ctor()
</pre>
<h2>SERIALIZATION</h2>
<p> Mono&#8217;s XML serialization engine by default will use a reflection-based approach to serialize which might be slow for continuous processing (web service applications). The serialization engine will determine when a class must use a hand-tuned serializer based on a few parameters and if needed it will produce a customized C# serializer for your types at runtime. This customized serializer then gets dynamically loaded into your application. </p>
<p> You can control this with the MONO_XMLSERIALIZER_THS environment variable. </p>
<p> The possible values are <code>`no&#8217; </code> to disable the use of a C# customized serializer, or an integer that is the minimum number of uses before the runtime will produce a custom serializer (0 will produce a custom serializer on the first access, 50 will produce a serializer on the 50th use). Mono will fallback to an interpreted serializer if the serializer generation somehow fails. This behavior can be disabled by setting the option <code>`nofallback&#8217;</code> (for example: MONO_XMLSERIALIZER_THS=0,nofallback).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>GC_DONT_GC</code></p>
<dd> Turns off the garbage collection in Mono. This should be only used for debugging purposes</p>
<dt><code>HTTP_PROXY</code></p>
<dd> (Also <code>http_proxy</code>) If set, web requests using the Mono Class Library will be automatically proxied through the given URL. Not supported on Windows, Mac OS, iOS or Android. See also <code>NO_PROXY</code>.</p>
<dt><code>LLVM_COUNT</code></p>
<dd> When Mono is compiled with LLVM support, this instructs the runtime to stop using LLVM after the specified number of methods are JITed. This is a tool used in diagnostics to help isolate problems in the code generation backend. For example <code>LLVM_COUNT=10</code> would only compile 10 methods with LLVM and then switch to the Mono JIT engine. <code>LLVM_COUNT=0</code> would disable the LLVM engine altogether.</p>
<dt><code>MONO_ASPNET_INHIBIT_SETTINGSMAP</code></p>
<dd> Mono contains a feature which allows modifying settings in the .config files shipped with Mono by using config section mappers. The mappers and the mapping rules are defined in the $prefix/etc/mono/2.0/settings.map file and, optionally, in the settings.map file found in the top-level directory of your ASP.NET application. Both files are read by System.Web on application startup, if they are found at the above locations. If you don&#8217;t want the mapping to be performed you can set this variable in your environment before starting the application and no action will be taken.</p>
<dt><code>MONO_ASPNET_WEBCONFIG_CACHESIZE</code></p>
<dd> Mono has a cache of ConfigSection objects for speeding up WebConfigurationManager queries. Its default size is 100 items, and when more items are needed, cache evictions start happening. If evictions are too frequent this could impose unnecessary overhead, which could be avoided by using this environment variable to set up a higher cache size (or to lower memory requirements by decreasing it).</p>
<dt><code>MONO_CAIRO_DEBUG_DISPOSE</code></p>
<dd> If set, causes Mono.Cairo to collect stack traces when objects are allocated, so that the finalization/Dispose warnings include information about the instance&#8217;s origin.</p>
<dt><code>MONO_CFG_DIR</code></p>
<dd> If set, this variable overrides the default system configuration directory ($PREFIX/etc). It&#8217;s used to locate machine.config file.</p>
<dt><code>MONO_COM</code></p>
<dd> Sets the style of COM interop. If the value of this variable is &quot;MS&quot; Mono will use string marhsalling routines from the liboleaut32 for the BSTR type library, any other values will use the mono-builtin BSTR string marshalling.</p>
<dt><code>MONO_CONFIG</code></p>
<dd> If set, this variable overrides the default runtime configuration file ($PREFIX/etc/mono/config). The &#8211;config command line options overrides the environment variable.</p>
<dt><code>MONO_CPU_ARCH</code></p>
<dd> Override the automatic cpu detection mechanism. Currently used only on arm. The format of the value is as follows:<br />
&#8220;armvV [thumb[2]]&#8221;<br />
 where V is the architecture number 4, 5, 6, 7 and the options can be currently be &quot;thumb&quot; or &quot;thumb2&quot;. Example: </p>
<pre>
        MONO_CPU_ARCH=&quot;armv4 thumb&quot; mono ...
</pre>
<dt><code>MONO_ARM_FORCE_SOFT_FLOAT</code></p>
<dd> When Mono is built with a soft float fallback on ARM and this variable is set to &quot;1&quot;, Mono will always emit soft float code, even if a VFP unit is detected.</p>
<dt><code>MONO_DARWIN_USE_KQUEUE_FSW</code></p>
<dd> Fall back on the kqueue FileSystemWatcher implementation in Darwin. The default is the FSEvent implementation.</p>
<dt><code>MONO_DARWIN_WATCHER_MAXFDS</code></p>
<dd> This is a debugging aid used to force limits on the kqueue FileSystemWatcher implementation in Darwin. There is no limit by default.</p>
<dt><code>MONO_DISABLE_MANAGED_COLLATION</code></p>
<dd> If this environment variable is `yes&#8217;, the runtime uses unmanaged collation (which actually means no culture-sensitive collation). It internally disables managed collation functionality invoked via the members of System.Globalization.CompareInfo class. Collation is enabled by default.</p>
<dt><code>MONO_DISABLE_SHARED_AREA</code></p>
<dd> Unix only: If set, disable usage of shared memory for exposing performance counters. This means it will not be possible to both externally read performance counters from this processes or read those of external processes.</p>
<dt><code>MONO_DNS</code></p>
<dd> When set, enables the use of a fully managed DNS resolver instead of the regular libc functions. This resolver performs much better when multiple queries are run in parallel. </p>
<p> Note that /etc/nsswitch.conf will be ignored.</p>
<dt><code>MONO_EGD_SOCKET</code></p>
<dd> For platforms that do not otherwise have a way of obtaining random bytes this can be set to the name of a file system socket on which an egd or prngd daemon is listening.</p>
<dt><code>MONO_ENABLE_AIO</code></p>
<dd> If set, tells mono to attempt using native asynchronous I/O services. If not set, a default select/poll implementation is used. Currently epoll and kqueue are supported.</p>
<dt><code>MONO_THREADS_SUSPEND</code> Selects a mechanism that Mono will use to suspend</p>
<dd> threads. May be set to &quot;preemptive&quot;, &quot;coop&quot;, or &quot;hybrid&quot;. Threads may need to be suspended by the debugger, or using some .NET threading APIs, and most commonly when the SGen garbage collector needs to stop all threads during a critical phase of garbage collection. Preemptive mode is the mode that Mono has used historically, going back to the Boehm days, where the garbage collector would run at any point and suspend execution of all threads as required to perform a garbage collection. The cooperative mode on the other hand requires the cooperation of all threads to stop at a safe point. This makes for an easier to debug garbage collector and it improves the stability of the runtime because threads are not suspended when accessing critical resources. In scenarios where Mono is embedded in another application, cooperative suspend requires the embedder code to follow coding guidelines in order to cooperate with the garbage collector. Cooperative suspend in embedded Mono is currently experimental. Hybrid mode is a combination of the two that retains better compatability with scenarios where Mono is embedded in another application: threads that are running managed code or code that comprises the Mono runtime will be cooperatively suspended, while threads running embedder code will be preemptively suspended. Hybrid suspend is the default on some desktop platforms. </p>
<p> Alternatively, coop and hybrid mode can be enabled at compile time by using the &#8211;enable-cooperative-suspend or &#8211;enable-hybrid-suspend flags, respectively, when calling configure. The <code>MONO_THREADS_SUSPEND</code> environment variable takes priority over the compiled default.</p>
<dt><code>MONO_ENABLE_COOP_SUSPEND</code></p>
<dd> This environment variable is obsolete, but retained for backward compatibility. Use <code>MONO_THREADS_SUSPEND</code> set to &quot;coop&quot; instead. Note that if configure flags were provided to enable cooperative or hybrid suspend, this variable is ignored.</p>
<dt><code>MONO_ENV_OPTIONS</code></p>
<dd> This environment variable allows you to pass command line arguments to a Mono process through the environment. This is useful for example to force all of your Mono processes to use LLVM or SGEN without having to modify any launch scripts.</p>
<dt><code>MONO_SDB_ENV_OPTIONS</code></p>
<dd> Used to pass extra options to the debugger agent in the runtime, as they were passed using &#8211;debugger-agent=.</p>
<dt><code>MONO_EVENTLOG_TYPE</code></p>
<dd> Sets the type of event log provider to use (for System.Diagnostics.EventLog). Possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>local[:path]</i></p>
<dd> Persists event logs and entries to the local file system. The directory in which to persist the event logs, event sources and entries can be specified as part of the value. If the path is not explicitly set, it defaults to &quot;/var/lib/mono/eventlog&quot; on unix and &quot;%APPDATA%monoentlog&quot; on Windows.</p>
<dt><i>win32</i></p>
<dd> <code>Uses the native win32 API to write events and registers event logs and</code> event sources in the registry. This is only available on Windows. On Unix, the directory permission for individual event log and event source directories is set to 777 (with +t bit) allowing everyone to read and write event log entries while only allowing entries to be deleted by the user(s) that created them.</p>
<dt><i>null</i></p>
<dd> Silently discards any events.</dl>
<p> The default is &quot;null&quot; on Unix (and versions of Windows before NT), and &quot;win32&quot; on Windows NT (and higher).</dl>
<dt><code>MONO_EXTERNAL_ENCODINGS</code></p>
<dd> If set, contains a colon-separated list of text encodings to try when turning externally-generated text (e.g. command-line arguments or filenames) into Unicode. The encoding names come from the list provided by iconv, and the special case &quot;default_locale&quot; which refers to the current locale&#8217;s default encoding.</p>
<dt>
<dd> When reading externally-generated text strings UTF-8 is tried first, and then this list is tried in order with the first successful conversion ending the search. When writing external text (e.g. new filenames or arguments to new processes) the first item in this list is used, or UTF-8 if the environment variable is not set.</p>
<dt>
<dd> The problem with using MONO_EXTERNAL_ENCODINGS to process your files is that it results in a problem: although its possible to get the right file name it is not necessarily possible to open the file. In general if you have problems with encodings in your filenames you should use the &quot;convmv&quot; program.</p>
<dt><code>MONO_GC_PARAMS</code></p>
<dd> When using Mono with the SGen garbage collector this variable controls several parameters of the collector. The variable&#8217;s value is a comma separated list of words.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>max-heap-size=</code><i>size</i></p>
<dd> Sets the maximum size of the heap. The size is specified in bytes and must be a power of two. The suffixes `k&#8217;, `m&#8217; and `g&#8217; can be used to specify kilo-, mega- and gigabytes, respectively. The limit is the sum of the nursery, major heap and large object heap. Once the limit is reached the application will receive OutOfMemoryExceptions when trying to allocate. Not the full extent of memory set in max-heap-size could be available to satisfy a single allocation due to internal fragmentation. By default heap limits is disabled and the GC will try to use all available memory.</p>
<dt><code>nursery-size=</code><i>size</i></p>
<dd> Sets the size of the nursery. The size is specified in bytes and must be a power of two. The suffixes `k&#8217;, `m&#8217; and `g&#8217; can be used to specify kilo-, mega- and gigabytes, respectively. The nursery is the first generation (of two). A larger nursery will usually speed up the program but will obviously use more memory. The default nursery size 4 MB.</p>
<dt><code>major=</code><i>collector</i></p>
<dd> Specifies which major collector to use. Options are `marksweep&#8217; for the Mark&amp;Sweep collector, `marksweep-conc&#8217; for concurrent Mark&amp;Sweep and `marksweep-conc-par&#8217; for parallel and concurrent Mark&amp;Sweep. The concurrent Mark&amp;Sweep collector is the default.</p>
<dt><code>mode=balanced|throughput|pause</code>[:<i>max-pause</i>]</p>
<dd> Specifies what should be the garbage collector&#8217;s target. The `throughput&#8217; mode aims to reduce time spent in the garbage collector and improve application speed, the `pause&#8217; mode aims to keep pause times to a minimum and it receives the argument <i>max-pause</i> which specifies the maximum pause time in milliseconds that is acceptable and the `balanced&#8217; mode which is a general purpose optimal mode.</p>
<dt><code>soft-heap-limit=</code><i>size</i></p>
<dd> Once the heap size gets larger than this size, ignore what the default major collection trigger metric says and only allow four nursery size&#8217;s of major heap growth between major collections.</p>
<dt><code>evacuation-threshold=</code><i>threshold</i></p>
<dd> Sets the evacuation threshold in percent. This option is only available on the Mark&amp;Sweep major collectors. The value must be an integer in the range 0 to 100. The default is 66. If the sweep phase of the collection finds that the occupancy of a specific heap block type is less than this percentage, it will do a copying collection for that block type in the next major collection, thereby restoring occupancy to close to 100 percent. A value of 0 turns evacuation off.</p>
<dt><code>(no-)lazy-sweep</code></p>
<dd> Enables or disables lazy sweep for the Mark&amp;Sweep collector. If enabled, the sweeping of individual major heap blocks is done piecemeal whenever the need arises, typically during nursery collections. Lazy sweeping is enabled by default.</p>
<dt><code>(no-)concurrent-sweep</code></p>
<dd> Enables or disables concurrent sweep for the Mark&amp;Sweep collector. If enabled, the iteration of all major blocks to determine which ones can be freed and which ones have to be kept and swept, is done concurrently with the running program. Concurrent sweeping is enabled by default.</p>
<dt><code>stack-mark=</code><i>mark-mode</i></p>
<dd> Specifies how application threads should be scanned. Options are `precise` and `conservative`. Precise marking allow the collector to know what values on stack are references and what are not. Conservative marking threats all values as potentially references and leave them untouched. Precise marking reduces floating garbage and can speed up nursery collection and allocation rate, it has the downside of requiring a significant extra memory per compiled method. The right option, unfortunately, requires experimentation.</p>
<dt><code>save-target-ratio=</code><i>ratio</i></p>
<dd> Specifies the target save ratio for the major collector. The collector lets a given amount of memory to be promoted from the nursery due to minor collections before it triggers a major collection. This amount is based on how much memory it expects to free. It is represented as a ratio of the size of the heap after a major collection. Valid values are between 0.1 and 2.0. The default is 0.5. Smaller values will keep the major heap size smaller but will trigger more major collections. Likewise, bigger values will use more memory and result in less frequent major collections. This option is EXPERIMENTAL, so it might disappear in later versions of mono.</p>
<dt><code>default-allowance-ratio=</code><i>ratio</i></p>
<dd> Specifies the default allocation allowance when the calculated size is too small. The allocation allowance is how much memory the collector let be promoted before triggered a major collection. It is a ratio of the nursery size. Valid values are between 1.0 and 10.0. The default is 4.0. Smaller values lead to smaller heaps and more frequent major collections. Likewise, bigger values will allow the heap to grow faster but use more memory when it reaches a stable size. This option is EXPERIMENTAL, so it might disappear in later versions of mono.</p>
<dt><code>minor=</code><i>minor-collector</i></p>
<dd> Specifies which minor collector to use. Options are `simple&#8217; which promotes all objects from the nursery directly to the old generation, `simple-par&#8217; which has same promotion behavior as `simple&#8217; but using multiple workers and `split&#8217; which lets objects stay longer on the nursery before promoting.</p>
<dt><code>alloc-ratio=</code><i>ratio</i></p>
<dd> Specifies the ratio of memory from the nursery to be use by the alloc space. This only can only be used with the split minor collector. Valid values are integers between 1 and 100. Default is 60.</p>
<dt><code>promotion-age=</code><i>age</i></p>
<dd> Specifies the required age of an object must reach inside the nursery before been promoted to the old generation. This only can only be used with the split minor collector. Valid values are integers between 1 and 14. Default is 2.</p>
<dt><code>(no-)cementing</code></p>
<dd> Enables or disables cementing. This can dramatically shorten nursery collection times on some benchmarks where pinned objects are referred to from the major heap.</p>
<dt><code>allow-synchronous-major</code></p>
<dd> This forbids the major collector from performing synchronous major collections. The major collector might want to do a synchronous collection due to excessive fragmentation. Disabling this might trigger OutOfMemory error in situations that would otherwise not happen.</dl>
</dl>
<dt><code>MONO_GC_DEBUG</code></p>
<dd> When using Mono with the SGen garbage collector this environment variable can be used to turn on various debugging features of the collector. The value of this variable is a comma separated list of words. Do not use these options in production.</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>number</i></p>
<dd> Sets the debug level to the specified number.</p>
<dt><code>print-allowance</code></p>
<dd> After each major collection prints memory consumption for before and after the collection and the allowance for the minor collector, i.e. how much the heap is allowed to grow from minor collections before the next major collection is triggered.</p>
<dt><code>print-pinning</code></p>
<dd> Gathers statistics on the classes whose objects are pinned in the nursery and for which global remset entries are added. Prints those statistics when shutting down.</p>
<dt><code>collect-before-allocs</code></p>
<dd>
<dt><code>check-remset-consistency</code></p>
<dd> This performs a remset consistency check at various opportunities, and also clears the nursery at collection time, instead of the default, when buffers are allocated (clear-at-gc). The consistency check ensures that there are no major to minor references that are not on the remembered sets.</p>
<dt><code>mod-union-consistency-check</code></p>
<dd> Checks that the mod-union cardtable is consistent before each finishing major collection pause. This check is only applicable to concurrent major collectors.</p>
<dt><code>check-mark-bits</code></p>
<dd> Checks that mark bits in the major heap are consistent at the end of each major collection. Consistent mark bits mean that if an object is marked, all objects that it had references to must also be marked.</p>
<dt><code>check-nursery-untag</code></p>
<dd> After garbage collections, check whether all vtable pointers are no longer tagged.</p>
<dt><code>xdomain-checks</code></p>
<dd> Performs a check to make sure that no references are left to an unloaded AppDomain.</p>
<dt><code>clear-at-tlab-creation</code></p>
<dd> Clears the nursery incrementally when the thread local allocation buffers (TLAB) are created. The default setting clears the whole nursery at GC time.</p>
<dt><code>debug-clear-at-tlab-creation</code></p>
<dd> Clears the nursery incrementally when the thread local allocation buffers (TLAB) are created, but at GC time fills it with the byte `0xff`, which should result in a crash more quickly if `clear-at-tlab-creation` doesn&#8217;t work properly.</p>
<dt><code>clear-at-gc</code></p>
<dd> This clears the nursery at GC time instead of doing it when the thread local allocation buffer (TLAB) is created. The default is to clear the nursery at TLAB creation time.</p>
<dt><code>disable-minor</code></p>
<dd> Don&#8217;t do minor collections. If the nursery is full, a major collection is triggered instead, unless it, too, is disabled.</p>
<dt><code>disable-major</code></p>
<dd> Don&#8217;t do major collections.</p>
<dt><code>conservative-stack-mark</code></p>
<dd> Forces the GC to scan the stack conservatively, even if precise scanning is available.</p>
<dt><code>no-managed-allocator</code></p>
<dd> Disables the managed allocator.</p>
<dt><code>check-scan-starts</code></p>
<dd> If set, does a plausibility check on the scan_starts before and after each collection</p>
<dt><code>verify-nursery-at-minor-gc</code></p>
<dd> If set, does a complete object walk of the nursery at the start of each minor collection.</p>
<dt><code>dump-nursery-at-minor-gc</code></p>
<dd> If set, dumps the contents of the nursery at the start of each minor collection. Requires verify-nursery-at-minor-gc to be set.</p>
<dt><code>heap-dump=</code><i>file</i></p>
<dd> Dumps the heap contents to the specified file. To visualize the information, use the mono-heapviz tool.</p>
<dt><code>binary-protocol=</code><i>file</i></p>
<dd> Outputs the debugging output to the specified file. For this to work, Mono needs to be compiled with the BINARY_PROTOCOL define on sgen-gc.c. You can then use this command to explore the output </p>
<pre>
                sgen-grep-binprot 0x1234 0x5678 &lt; file
</pre>
<dt><code>nursery-canaries</code></p>
<dd> If set, objects allocated in the nursery are suffixed with a canary (guard) word, which is checked on each minor collection. Can be used to detect/debug heap corruption issues. </p>
<dt><code>do-not-finalize(=</code><i>classes</i><code>)</code></p>
<dd> If enabled, finalizers will not be run. Everything else will be unaffected: finalizable objects will still be put into the finalization queue where they survive until they&#8217;re scheduled to finalize. Once they&#8217;re not in the queue anymore they will be collected regularly. If a list of comma-separated class names is given, only objects from those classes will not be finalized. </p>
<dt><code>log-finalizers</code></p>
<dd> Log verbosely around the finalization process to aid debugging.</dl>
</dl>
<dt><code>MONO_GAC_PREFIX</code></p>
<dd> Provides a prefix the runtime uses to look for Global Assembly Caches. Directories are separated by the platform path separator (colons on unix). MONO_GAC_PREFIX should point to the top directory of a prefixed install. Or to the directory provided in the gacutil /gacdir command. Example: <code>/home/username/.mono:/usr/local/mono/</code></p>
<dt><code>MONO_IOMAP</code></p>
<dd> Enables some filename rewriting support to assist badly-written applications that hard-code Windows paths. Set to a colon-separated list of &quot;drive&quot; to strip drive letters, or &quot;case&quot; to do case-insensitive file matching in every directory in a path. &quot;all&quot; enables all rewriting methods. (Backslashes are always mapped to slashes if this variable is set to a valid option). For example, this would work from the shell: </p>
<pre>
        MONO_IOMAP=drive:case
        export MONO_IOMAP
</pre>
<p> If you are using mod_mono to host your web applications, you can use the <code>MonoIOMAP</code> directive instead, like this: </p>
<pre>
        MonoIOMAP &lt;appalias&gt; all
</pre>
<p> See <a href="/docs/linux/man/8-mod_mono/">mod_mono</a>(8) for more details.</p>
<dt><code>MONO_LLVM</code></p>
<dd> When Mono is using the LLVM code generation backend you can use this environment variable to pass code generation options to the LLVM compiler.</p>
<dt><code>MONO_MANAGED_WATCHER</code></p>
<dd> If set to &quot;disabled&quot;, System.IO.FileSystemWatcher will use a file watcher implementation which silently ignores all the watching requests. If set to any other value, System.IO.FileSystemWatcher will use the default managed implementation (slow). If unset, mono will try to use inotify, FAM, Gamin, kevent under Unix systems and native API calls on Windows, falling back to the managed implementation on error.</p>
<dt><code>MONO_MESSAGING_PROVIDER</code></p>
<dd> Mono supports a plugin model for its implementation of System.Messaging making it possible to support a variety of messaging implementations (e.g. AMQP, ActiveMQ). To specify which messaging implementation is to be used the evironement variable needs to be set to the full class name for the provider. E.g. to use the RabbitMQ based AMQP implementation the variable should be set to: </p>
<p>Mono.Messaging.RabbitMQ.RabbitMQMessagingProvider,Mono.Messaging.RabbitMQ<br />
MONO_NO_SMPIf set causes the mono process to be bound to a single processor. This may be<br />
useful when debugging or working around race conditions.<br />
MONO_NO_TLSDisable inlining of thread local accesses. Try setting this if you get a segfault<br />
early on in the execution of mono.<br />
MONO_PATHProvides a search path to the runtime where to look for library<br />
files.   This is a tool convenient for debugging applications, but<br />
should not be used by deployed applications as it breaks the assembly<br />
loader in subtle ways.<br />
Directories are separated by the platform path separator (colons on unix). Example:<br />
/home/username/lib:/usr/local/mono/lib<br />
Relative paths are resolved based on the launch-time current directory.<br />
Alternative solutions to MONO_PATH include: installing libraries into<br />
the Global Assembly Cache (see gacutil(1)) or having the dependent<br />
libraries side-by-side with the main executable.<br />
For a complete description of recommended practices for application<br />
deployment, see<br />
http://www.mono-project.com/docs/getting-started/application-deployment/<br />
MONO_SHARED_DIRIf set its the directory where the &#8220;.wapi&#8221; handle state is stored.<br />
This is the directory where the Windows I/O Emulation layer stores its<br />
shared state data (files, events, mutexes, pipes).  By default Mono<br />
will store the &#8220;.wapi&#8221; directory in the users&#8217;s home directory.<br />
MONO_SHARED_HOSTNAMEUses the string value of this variable as a replacement for the host name when<br />
creating file names in the &#8220;.wapi&#8221; directory. This helps if the host name of<br />
your machine is likely to be changed when a mono application is running or if<br />
you have a .wapi directory shared among several different computers.<br />
Mono typically uses the hostname to create the files that are used to<br />
share state across multiple Mono processes.  This is done to support<br />
home directories that might be shared over the network.<br />
MONO_STRICT_IO_EMULATIONIf set, extra checks are made during IO operations.  Currently, this<br />
includes only advisory locks around file writes.<br />
MONO_TLS_PROVIDERThis environment variable controls which TLS/SSL provider Mono will<br />
use.  The options are usually determined by the operating system where<br />
Mono was compiled and the configuration options that were used for<br />
it.   </p>
<p>default<br />
Uses the default TLS stack that the Mono runtime was configured with.<br />
Usually this is configured to use Apple&#8217;s SSL stack on Apple<br />
platforms, and Boring SSL on other platforms.<br />
apple<br />
Forces the use of the Apple SSL stack, only works on Apple platforms.<br />
btls<br />
Forces the use of the BoringSSL stack.    See<br />
https://opensource.google.com/projects/boringssl for more information<br />
about this stack.<br />
legacy<br />
This is the old Mono stack, which only supports SSL and TLS up to<br />
version 1.0.   It is deprecated and will be removed in the future.</p>
<p>MONO_TLS_SESSION_CACHE_TIMEOUTThe time, in seconds, that the SSL/TLS session cache will keep it&#8217;s entry to<br />
avoid a new negotiation between the client and a server. Negotiation are very<br />
CPU intensive so an application-specific custom value may prove useful for<br />
small embedded systems.<br />
The default is 180 seconds.<br />
MONO_THREADS_PER_CPUThe minimum number of threads in the general threadpool will be<br />
MONO_THREADS_PER_CPU * number of CPUs. The default value for this<br />
variable is 1.<br />
MONO_XMLSERIALIZER_THSControls the threshold for the XmlSerializer to produce a custom<br />
serializer for a given class instead of using the Reflection-based<br />
interpreter.  The possible values are `no&#8217; to disable the use of a<br />
custom serializer or a number to indicate when the XmlSerializer<br />
should start serializing.   The default value is 50, which means that<br />
the a custom serializer will be produced on the 50th use.<br />
MONO_X509_REVOCATION_MODESets the revocation mode used when validating a X509 certificate chain (https,<br />
ftps, smtps&#8230;).  The default is &#8216;nocheck&#8217;, which performs no revocation check<br />
at all. The other possible values are &#8216;offline&#8217;, which performs CRL check (not<br />
implemented yet) and &#8216;online&#8217; which uses OCSP and CRL to verify the revocation<br />
status (not implemented yet).<br />
NO_PROXY(Also no_proxy) If both HTTP_PROXY and NO_PROXY are<br />
set, NO_PROXY will be treated as a comma-separated list of &#8220;bypass&#8221; domains<br />
which will not be sent through the proxy. Domains in NO_PROXY may contain<br />
wildcards, as in &#8220;*.mono-project.com&#8221; or &#8220;build????.local&#8221;. Not supported on<br />
Windows, Mac OS, iOS or Android.</p>
<h2>ENVIRONMENT VARIABLES FOR DEBUGGING</h2>
<dl>
<dt><code>MONO_ASPNET_NODELETE</code></p>
<dd> If set to any value, temporary source files generated by ASP.NET support classes will not be removed. They will be kept in the user&#8217;s temporary directory.</p>
<dt><code>MONO_DEBUG</code></p>
<dd> If set, enables some features of the runtime useful for debugging. This variable should contain a comma separated list of debugging options. Currently, the following options are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>align-small-structs</code></p>
<dd> Enables small structs alignment to 4/8 bytes.</p>
<dt><code>arm-use-fallback-tls</code></p>
<dd> When this option is set on ARM, a fallback thread local store will be used instead of the default fast thread local storage primitives.</p>
<dt><code>break-on-unverified</code></p>
<dd> If this variable is set, when the Mono VM runs into a verification problem, instead of throwing an exception it will break into the debugger. This is useful when debugging verifier problems</p>
<dt><code>casts</code></p>
<dd> This option can be used to get more detailed information from InvalidCast exceptions, it will provide information about the types involved.</p>
<dt><code>check-pinvoke-callconv</code></p>
<dd> This option causes the runtime to check for calling convention mismatches when using pinvoke, i.e. mixing cdecl/stdcall. It only works on windows. If a mismatch is detected, an ExecutionEngineException is thrown.</p>
<dt><code>collect-pagefault-stats</code></p>
<dd> Collects information about pagefaults. This is used internally to track the number of page faults produced to load metadata. To display this information you must use this option with &quot;&#8211;stats&quot; command line option.</p>
<dt><code>debug-domain-unload</code></p>
<dd> When this option is set, the runtime will invalidate the domain memory pool instead of destroying it.</p>
<dt><code>disable_omit_fp</code></p>
<dd> Disables a compiler optimization where the frame pointer is omitted from the stack. This optimization can interact badly with debuggers.</p>
<dt><code>dont-free-domains</code></p>
<dd> This is an Optimization for multi-AppDomain applications (most commonly ASP.NET applications). Due to internal limitations Mono, Mono by default does not use typed allocations on multi-appDomain applications as they could leak memory when a domain is unloaded. Although this is a fine default, for applications that use more than on AppDomain heavily (for example, ASP.NET applications) it is worth trading off the small leaks for the increased performance (additionally, since ASP.NET applications are not likely going to unload the application domains on production systems, it is worth using this feature).</p>
<dt><code>dyn-runtime-invoke</code></p>
<dd> Instructs the runtime to try to use a generic runtime-invoke wrapper instead of creating one invoke wrapper.</p>
<dt><code>explicit-null-checks</code></p>
<dd> Makes the JIT generate an explicit NULL check on variable dereferences instead of depending on the operating system to raise a SIGSEGV or another form of trap event when an invalid memory location is accessed.</p>
<dt><code>gdb</code></p>
<dd> Equivalent to setting the <code>MONO_XDEBUG</code> variable, this emits symbols into a shared library as the code is JITed that can be loaded into GDB to inspect symbols.</p>
<dt><code>gen-seq-points</code></p>
<dd> Automatically generates sequence points where the IL stack is empty. These are places where the debugger can set a breakpoint.</p>
<dt><code>no-compact-seq-points</code></p>
<dd> Unless the option is used, the runtime generates sequence points data that maps native offsets to IL offsets. Sequence point data is used to display IL offset in stacktraces. Stacktraces with IL offsets can be symbolicated using mono-symbolicate tool.</p>
<dt><code>handle-sigint</code></p>
<dd> Captures the interrupt signal (Control-C) and displays a stack trace when pressed. Useful to find out where the program is executing at a given point. This only displays the stack trace of a single thread.</p>
<dt><code>init-stacks</code></p>
<dd> Instructs the runtime to initialize the stack with some known values (0x2a on x86-64) at the start of a method to assist in debuggin the JIT engine.</p>
<dt><code>keep-delegates</code></p>
<dd> This option will leak delegate trampolines that are no longer referenced as to present the user with more information about a delegate misuse. Basically a delegate instance might be created, passed to unmanaged code, and no references kept in managed code, which will garbage collect the code. With this option it is possible to track down the source of the problems.</p>
<dt><code>no-gdb-backtrace</code></p>
<dd> This option will disable the GDB backtrace emitted by the runtime after a SIGSEGV or SIGABRT in unmanaged code.</p>
<dt><code>partial-sharing</code></p>
<dd> When this option is set, the runtime can share generated code between generic types effectively reducing the amount of code generated.</p>
<dt><code>reverse-pinvoke-exceptions</p>
<dd> This option will cause mono to abort with a descriptive message when during stack unwinding after an exception it reaches a native stack frame. This happens when a managed delegate is passed to native code, and the managed delegate throws an exception. Mono will normally try to unwind the stack to the first (managed) exception handler, and it will skip any native stack frames in the process. This leads to undefined behaviour (since mono doesn&#8217;t know how to process native frames), leaks, and possibly crashes too.</p>
<dt>single-imm-size</code></p>
<dd> This guarantees that each time managed code is compiled the same instructions and registers are used, regardless of the size of used values.</p>
<dt><code>soft-breakpoints</code></p>
<dd> This option allows using single-steps and breakpoints in hardware where we cannot do it with signals.</p>
<dt><code>suspend-on-native-crash</code></p>
<dd> This option will suspend the program when a native crash occurs (SIGSEGV, SIGILL, &#8230;). This is useful for debugging crashes which do not happen under gdb, since a live process contains more information than a core file.</p>
<dt><code>suspend-on-sigsegv</code></p>
<dd> Same as <code>suspend-on-native-crash</code>.</p>
<dt><code>suspend-on-exception</code></p>
<dd> This option will suspend the program when an exception occurs.</p>
<dt><code>suspend-on-unhandled</code></p>
<dd> This option will suspend the program when an unhandled exception occurs.</p>
<dt><code>thread-dump-dir=DIR</code></p>
<dd> Use DIR for storage thread dumps created by SIGQUIT.</p>
<dt><code>weak-memory-model</code></p>
<dd> Don&#8217;t enforce the CLR memory model on platforms with weak memory models. This can introduce random crashes in some rare cases, for multithreaded environments. This can be used for a performance boost on applications that are single threaded.</p>
<dt><code>verbose-gdb</code></p>
<dd> Make gdb output on native crashes more verbose.</dl>
</dl>
<dt><code>MONO_LOG_LEVEL</code></p>
<dd> The logging level, possible values are `error&#8217;, `critical&#8217;, `warning&#8217;, `message&#8217;, `info&#8217; and `debug&#8217;. See the DEBUGGING section for more details.</p>
<dt><code>MONO_LOG_MASK</code></p>
<dd> Controls the domain of the Mono runtime that logging will apply to. If set, the log mask is changed to the set value. Possible values are &quot;asm&quot; (assembly loader), &quot;type&quot;, &quot;dll&quot; (native library loader), &quot;gc&quot; (garbage collector), &quot;cfg&quot; (config file loader), &quot;aot&quot; (precompiler), &quot;security&quot; (e.g. Moonlight CoreCLR support) and &quot;all&quot;. The default value is &quot;all&quot;. Changing the mask value allows you to display only messages for a certain component. You can use multiple masks by comma separating them. For example to see config file messages and assembly loader messages set you mask to &quot;asm,cfg&quot;.</p>
<dt><code>MONO_LOG_DEST</code></p>
<dd> Controls where trace log messages are written. If not set then the messages go to stdout. If set, the string either specifies a path to a file that will have messages appended to it, or the string &quot;syslog&quot; in which case the messages will be written to the system log. Under Windows, this is simulated by writing to a file called &quot;mono.log&quot;. <code>MONO_LOG_HEADER</code> Controls whether trace log messages not directed to syslog have the id, timestamp, and pid as the prefix to the log message. To enable a header this environment variable need just be non-null.</p>
<dt><code>MONO_TRACE</code></p>
<dd> Used for runtime tracing of method calls. The format of the comma separated trace options is: </p>
<pre><code>
[-] M : method name
            [-] N : namespace
                        [-] T : class name
                                    [-] all
                                        [-] program
                                            disabled Trace output off upon start.
</code></pre>
<p> You can toggle trace output on/off sending a SIGUSR2 signal to the program.</p>
<dt><code>MONO_TRACE_LISTENER</code></p>
<dd> If set, enables the System.Diagnostics.DefaultTraceListener, which will print the output of the System.Diagnostics Trace and Debug classes. It can be set to a filename, and to Console.Out or Console.Error to display output to standard output or standard error, respectively. If it&#8217;s set to Console.Out or Console.Error you can append an optional prefix that will be used when writing messages like this: Console.Error:MyProgramName. See the System.Diagnostics.DefaultTraceListener documentation for more information.</p>
<dt><code>MONO_WCF_TRACE</code></p>
<dd> This eases WCF diagnostics functionality by simply outputs all log messages from WCF engine to &quot;stdout&quot;, &quot;stderr&quot; or any file passed to this environment variable. The log format is the same as usual diagnostic output.</p>
<dt><code>MONO_XEXCEPTIONS</code></p>
<dd> This throws an exception when a X11 error is encountered; by default a message is displayed but execution continues</p>
<dt><code>MONO_XMLSERIALIZER_DEBUG</code></p>
<dd> Set this value to 1 to prevent the serializer from removing the temporary files that are created for fast serialization; This might be useful when debugging.</p>
<dt><code>MONO_XSYNC</code></p>
<dd> This is used in the System.Windows.Forms implementation when running with the X11 backend. This is used to debug problems in Windows.Forms as it forces all of the commands send to X11 server to be done synchronously. The default mode of operation is asynchronous which makes it hard to isolate the root of certain problems.</p>
<dt><code>MONO_XDEBUG</code></p>
<dd> When the the MONO_XDEBUG env var is set, debugging info for JITted code is emitted into a shared library, loadable into gdb. This enables, for example, to see managed frame names on gdb backtraces.</p>
<dt><code>MONO_VERBOSE_METHOD</code></p>
<dd> Enables the maximum JIT verbosity for the specified method. This is very helpfull to diagnose a miscompilation problems of a specific method. This can be a semicolon-separated list of method names to match. If the name is simple, this applies to any method with that name, otherwise you can use a mono method description (see the section METHOD DESCRIPTIONS).</p>
<dt><code>MONO_JIT_DUMP_METHOD</code></p>
<dd> Enables sending of the JITs intermediate representation for a specified method to the IdealGraphVisualizer tool.</p>
<dt><code>MONO_VERBOSE_HWCAP</code></p>
<dd> If set, makes the JIT output information about detected CPU features (such as SSE, CMOV, FCMOV, etc) to stdout.</p>
<dt><code>MONO_CONSERVATIVE_HWCAP</code></p>
<dd> If set, the JIT will not perform any hardware capability detection. This may be useful to pinpoint the cause of JIT issues. This is the default when Mono is built as an AOT cross compiler, so that the generated code will run on most hardware.</dl>
<h2>VALGRIND</h2>
<p> If you want to use Valgrind, you will find the file `mono.supp&#8217; useful, it contains the suppressions for the GC which trigger incorrect warnings. Use it like this: </p>
<pre>
    valgrind --suppressions=mono.supp mono ...
</pre>
<h2>DTRACE</h2>
<p> On some platforms, Mono can expose a set of DTrace probes (also known as user-land statically defined, USDT Probes).</p>
<dl>
<dt>They are defined in the file `mono.d&#8217;.</p>
<dd>
<dt><code>ves-init-begin, ves-init-end</code></p>
<dd> Begin and end of runtime initialization.</p>
<dt><code>method-compile-begin, method-compile-end</code></p>
<dd> Begin and end of method compilation. The probe arguments are class name, method name and signature, and in case of method-compile-end success or failure of compilation.</p>
<dt><code>gc-begin, gc-end</code></p>
<dd> Begin and end of Garbage Collection.</p>
<dt>To verify the availability of the probes, run:</p>
<dd>
<pre>
    dtrace -P mono'$target' -l -c mono
</pre>
</dl>
<h2>PERMISSIONS</h2>
<p> Mono&#8217;s Ping implementation for detecting network reachability can create the ICMP packets itself without requiring the system ping command to do the work. If you want to enable this on Linux for non-root users, you need to give the Mono binary special permissions. </p>
<p> As root, run this command: </p>
<pre>
   # setcap cap_net_raw=+ep /usr/bin/mono
</pre>
<h2>FILES</h2>
<p> On Unix assemblies are loaded from the installation lib directory. If you set `prefix&#8217; to /usr, the assemblies will be located in /usr/lib. On Windows, the assemblies are loaded from the directory where mono and mint live.</p>
<dl>
<dt><code>~/.mono/aot-cache</code></p>
<dd> The directory for the ahead-of-time compiler demand creation assemblies are located.</p>
<dt><code>/etc/mono/config, ~/.mono/config</code></p>
<dd> Mono runtime configuration file. See the <a href="/docs/linux/man/5-mono-config/">mono-config</a>(5) manual page for more information.</p>
<dt><code>~/.config/.mono/certs, /usr/share/.mono/certs</code></p>
<dd> Contains Mono certificate stores for users / machine. See the <a href="/docs/linux/man/1-certmgr/">certmgr</a>(1) manual page for more information on managing certificate stores and the <a href="/docs/linux/man/1-mozroots/">mozroots</a>(1) page for information on how to import the Mozilla root certificates into the Mono certificate store.</p>
<dt><code>~/.mono/assemblies/ASSEMBLY/ASSEMBLY.config</code></p>
<dd> Files in this directory allow a user to customize the configuration for a given system assembly, the format is the one described in the <a href="/docs/linux/man/5-mono-config/">mono-config</a>(5) page.</p>
<dt><code>~/.config/.mono/keypairs, /usr/share/.mono/keypairs</code></p>
<dd> Contains Mono cryptographic keypairs for users / machine. They can be accessed by using a CspParameters object with DSACryptoServiceProvider and RSACryptoServiceProvider classes.</p>
<dt><code>~/.config/.isolatedstorage, ~/.local/share/.isolatedstorage, /usr/share/.isolatedstorage</code></p>
<dd> Contains Mono isolated storage for non-roaming users, roaming users and local machine. Isolated storage can be accessed using the classes from the System.IO.IsolatedStorage namespace.</p>
<dt><code>&lt;assembly&gt;.config</code></p>
<dd> Configuration information for individual assemblies is loaded by the runtime from side-by-side files with the .config files, see the <a rel="nofollow" href="http://www.mono-project.com/Config">http://www.mono-project.com/Config</a> for more information.</p>
<dt><code>Web.config, web.config</code></p>
<dd> ASP.NET applications are configured through these files, the configuration is done on a per-directory basis. For more information on this subject see the <a rel="nofollow" href="http://www.mono-project.com/Config_system.web">http://www.mono-project.com/Config_system.web</a> page.</dl>
<h2>MAILING LISTS</h2>
<p> Mailing lists are listed at the <a rel="nofollow" href="http://www.mono-project.com/community/help/mailing-lists/">http://www.mono-project.com/community/help/mailing-lists/</a></p>
<h2>WEB SITE</h2>
<p> <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-certmgr/">certmgr</a></code>(1), <code><a href="/docs/linux/man/1-cert-sync/">cert-sync</a></code>(1), <code><a href="/docs/linux/man/1-csharp/">csharp</a></code>(1), <code><a href="/docs/linux/man/1-gacutil/">gacutil</a></code>(1), <code><a href="/docs/linux/man/1-mcs/">mcs</a></code>(1), <code><a href="/docs/linux/man/1-monodis/">monodis</a></code>(1), <code><a href="/docs/linux/man/5-mono-config/">mono-config</a></code>(5), <code><a href="/docs/linux/man/1-mono-profilers/">mono-profilers</a></code>(1), <code><a href="/docs/linux/man/1-mprof-report/">mprof-report</a></code>(1), <code><a href="/docs/linux/man/1-pdb2mdb/">pdb2mdb</a></code>(1), <code><a href="/docs/linux/man/1-xsp/">xsp</a></code>(1), <code><a href="/docs/linux/man/8-mod_mono/">mod_mono</a></code>(8) </p>
<p> For more information on AOT: <a rel="nofollow" href="http://www.mono-project.com/docs/advanced/aot/">http://www.mono-project.com/docs/advanced/aot/</a> </p>
<p> For ASP.NET-related documentation, see the <a href="/docs/linux/man/1-xsp/">xsp</a>(1) manual page </p>
<h2>Index</h2>
