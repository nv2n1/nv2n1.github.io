---
title: "iverilog(1)"
name: "iverilog"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iverilog/"
description: "iverilog – Icarus Verilog compiler"
---

<h2>NAME</h2>
<p> iverilog &#8211; Icarus Verilog compiler </p>
<h2>SYNOPSIS</h2>
<p> <code>iverilog</code> [-ESVv] [-Bpath] [-ccmdfile|-fcmdfile] [-Dmacro[=defn]] [-pflag=value] [-dname] [-g1995|-g2001|-g2005|-g&lt;feature&gt;] [-Iincludedir] [-mmodule] [-Mfile] [-Nfile] [-ooutputfilename] [-stopmodule] [-ttype] [-Tmin/typ/max] [-Wclass] [-ypath] sourcefile </p>
<h2>DESCRIPTION</h2>
<p> <i>iverilog</i> is a compiler that translates Verilog source code into executable programs for simulation, or other netlist formats for further processing. The currently supported targets are <i>vvp</i> for simulation, and <i>fpga</i> for synthesis. Other target types are added as code generators are implemented. </p>
<h2>OPTIONS</h2>
<p> <i>iverilog</i> accepts the following options:</p>
<dl>
<dt><code>-B</code><i>base</i></p>
<dd> The <i>iverilog</i> program uses external programs and configuration files to preprocess and compile the Verilog source. Normally, the path used to locate these tools is built into the <i>iverilog</i> program. However, the <code>-B</code> switch allows the user to select a different set of programs. The path given is used to locate <i>ivlpp</i>, <i>ivl</i>, code generators and the VPI modules.</p>
<dt><code>-c</code><i>file</i> -f<i>file</i></p>
<dd> These flags specifies an input file that contains a list of Verilog source files. This is similar to the <i>command file</i> of other Verilog simulators, in that it is a file that contains the file names instead of taking them on the command line. See <code>Command Files</code> below.</p>
<dt><code>-D</code><i>macro</i></p>
<dd> Defines macro <i>macro</i> with the string `1&#8242; as its definition. This form is normally only used to trigger ifdef conditionals in the Verilog source.</p>
<dt><code>-D</code><i>macro=defn</i></p>
<dd> Defines macro <i>macro</i> as <i>defn</i>.</p>
<dt><code>-d</code><i>name</i></p>
<dd> Activate a class of compiler debugging messages. The <code>-d</code> switch may be used as often as necessary to activate all the desired messages. Supported names are scopes, eval_tree, elaborate, and synth2; any other names are ignored.</p>
<dt><code>-E</code></p>
<dd> Preprocess the Verilog source, but do not compile it. The output file is the Verilog input, but with file inclusions and macro references expanded and removed. This is useful, for example, to preprocess Verilog source for use by other compilers.</p>
<dt><code>-g1995</code><i>|</i>-g2001<i>|</i>-g2001-noconfig<i>|</i>-g2005</p>
<dd> Select the Verilog language <i>generation</i> to support in the compiler. This selects between <i>IEEE1364-1995</i>, <i>IEEE1364-2001</i>, or <i>IEEE1364-2005</i>. Normally, Icarus Verilog defaults to the latest known generation of the language. This flag is most useful to restrict the language to a set supported by tools of specific generations, for compatibility with other tools.</p>
<dt><code>-gverilog-ams</code><i>|</i>-gno-verilog-ams</p>
<dd> Enable or disable (default) support for Verilog-AMS. Very little Verilog-AMS specific functionality is currently supported.</p>
<dt><code>-gspecify</code><i>|</i>-gno-specify</p>
<dd> Enable or disable (default) specify block support. When enabled, specify block code is elaborated. When disabled, specify blocks are parsed but ignored. Specify blocks are commonly not needed for RTL simulation, and in fact can hurt performance of the simulation. However, disabling specify blocks reduces accuracy of full-timing simulations.</p>
<dt><code>-gstd-include</code><i>|</i>-gno-std-include</p>
<dd> Enable (default) or disable the search of a standard installation include directory after all other explicit include directories. This standard include directory is a convenient place to install standard header files that a Verilog program may include.</p>
<dt><code>-grelative-include</code><i>|</i>-gno-relative-include</p>
<dd> Enable or disable (default) adding the local files directory to the beginning of the include file search path. This allows files to be included relative to the current file not the more common files are only found in the working directory or in the specified include file search path.</p>
<dt><code>-gxtypes</code><i>|</i>-gno-xtypes</p>
<dd> Enable (default) or disable support for extended types. Enabling extended types allows for new types that are supported by Icarus Verilog as extensions beyond the baseline Verilog. It may be necessary to disable extended types if compiling code that clashes with the few new keywords used to implement the type system.</p>
<dt><code>-gio-range-error</code><i>|</i>-gno-io-range-error</p>
<dd> The standards requires that a vectored port have matching ranges for its port declaration as well as any net/register declaration. It was common practice in the past to only specify the range for the net/register declaration and some tools still allow this. By default any mismatch is reported as a error. Using <code>-gno-io-range-error</code> will produce a warning instead of a fatal error for the case of a vectored net/register and a scalar port declaration.</p>
<dt><code>-gstrict-ca-eval</code><i>|</i>-gno-strict-ca-eval</p>
<dd> The standard requires that if any input to a continuous assignment expression changes value, the entire expression is re-evaluated. By default, parts of the expression that do not depend on the changed input value(s) are not re-evaluated. If an expression contains a call to a function that doesn&#8217;t depend solely on its input values or that has side effects, the resulting behavior will differ from that required by the standard. Using <i>-gstrict-ca-eval</i> will force standard compliant behavior (with some loss in performance).</p>
<dt><code>-I</code><i>includedir</i></p>
<dd> Append directory <i>includedir</i> to list of directories searched for Verilog include files. The <code>-I</code> switch may be used many times to specify several directories to search, the directories are searched in the order they appear on the command line.</p>
<dt><code>-M</code><i>path</i></p>
<dd> Write into the file specified by path a list of files that contribute to the compilation of the design. This includes files that are included by include directives and files that are automatically loaded by library support. The output is one file name per line, with no leading or trailing space.</p>
<dt><code>-m</code><i>module</i></p>
<dd> Add this module to the list of VPI modules to be loaded by the simulation. Many modules can be specified, and all will be loaded, in the order specified. The system module is implicit and always included. If a System Function Table file (&lt;module&gt;.sft) exists for the module it will be loaded automatically.</p>
<dt><code>-N</code><i>path</i></p>
<dd> This is used for debugging the compiler proper. Dump the final netlist form of the design to the specified file. It otherwise does not affect operation of the compiler. The dump happens after the design is elaborated and optimized.</p>
<dt><code>-o </code><i>filename</i></p>
<dd> Place output in the file <i>filename</i>. If no output file name is specified, <i>iverilog</i> uses the default name <code>a.out</code>.</p>
<dt><code>-p</code><i>flag=value</i></p>
<dd> Assign a value to a target specific flag. The <code>-p</code> switch may be used as often as necessary to specify all the desired flags. The flags that are used depend on the target that is selected, and are described in target specific documentation. Flags that are not used are ignored.</p>
<dt><code>-S</code></p>
<dd> Synthesize. Normally, if the target can accept behavioral descriptions the compiler will leave processes in behavioral form. The <code>-S</code> switch causes the compiler to perform synthesis even if it is not necessary for the target. If the target type is a netlist format, the <code>-S</code> switch is unnecessary and has no effect.</p>
<dt><code>-s </code><i>topmodule</i></p>
<dd> Specify the top level module to elaborate. Icarus Verilog will by default choose modules that are not instantiated in any other modules, but sometimes that is not sufficient, or instantiates too many modules. If the user specifies one or more root modules with <code>-s</code> flags, then they will be used as root modules instead.</p>
<dt><code>-T</code><i>min|typ|max</i></p>
<dd> Use this switch to select min, typ or max times from min:typ:max expressions. Normally, the compiler will simply use the typ value from these expressions (printing a warning for the first ten it finds) but this switch will tell the compiler explicitly which value to use. This will suppress the warning that the compiler is making a choice.</p>
<dt><code>-t</code><i>target</i></p>
<dd> Use this switch to specify the target output format. See the <code>TARGETS</code> section below for a list of valid output formats.</p>
<dt><code>-v</code></p>
<dd> Turn on verbose messages. This will print the command lines that are executed to perform the actual compilation, along with version information from the various components, as well as the version of the product as a whole. You will notice that the command lines include a reference to a key temporary file that passes information to the compiler proper. To keep that file from being deleted at the end of the process, provide a file name of your own in the environment variable <code>IVERILOG_ICONFIG</code>.</p>
<dt><code>-V</code></p>
<dd> Print the version of the compiler, and exit.</p>
<dt><code>-W</code><i>class</i></p>
<dd> Turn on different classes of warnings. See the <code>WARNING TYPES</code> section below for descriptions of the different warning groups. If multiple <code>-W</code> switches are used, the warning set is the union of all the requested classes.</p>
<dt><code>-y</code><i>libdir</i></p>
<dd> Append the directory to the library module search path. When the compiler finds an undefined module, it looks in these directories for files with the right name.</p>
<dt><code>-Y</code><i>suffix</i></p>
<dd> Add suffix to the list of accepted file name suffixes used when searching a library for cells. The list defaults to the single entry <i>.v</i>. </p>
</dl>
<h2>MODULE LIBRARIES</h2>
<p> The Icarus Verilog compiler supports module libraries as directories that contain Verilog source files. During elaboration, the compiler notices the instantiation of undefined module types. If the user specifies library search directories, the compiler will search the directory for files with the name of the missing module type. If it finds such a file, it loads it as a Verilog source file, they tries again to elaborate the module. </p>
<p> Library module files should contain only a single module, but this is not a requirement. Library modules may reference other modules in the library or in the main design. </p>
<h2>TARGETS</h2>
<p> The Icarus Verilog compiler supports a variety of targets, for different purposes, and the <code>-t</code> switch is used to select the desired target. </p>
<dl>
<dt><code>null</code></p>
<dd> The null target causes no code to be generated. It is useful for checking the syntax of the Verilog source.</p>
<dt><code>vvp</code></p>
<dd> This is the default. The vvp target generates code for the vvp runtime. The output is a complete program that simulates the design but must be run by the <code>vvp</code> command.</p>
<dt><code>fpga</code></p>
<dd> This is a synthesis target that supports a variety of fpga devices, mostly by EDIF format output. The Icarus Verilog fpga code generator can generate complete designs or EDIF macros that can in turn be imported into larger designs by other tools. The <code>fpga</code> target implies the synthesis <code>-S</code> flag.</p>
<dt><code>vhdl</code></p>
<dd> This target produces a VHDL translation of the Verilog netlist. The output is a single file containing VHDL entities corresponding to the modules in the Verilog source code. Note that only a subset of the Verilog language is supported. See the wiki for more information. </p>
</dl>
<h2>WARNING TYPES</h2>
<p> These are the types of warnings that can be selected by the <code>-W</code> switch. All the warning types (other than <code>all</code>) can also be prefixed with <code>no-</code> to turn off that warning. This is most useful after a <code>-Wall</code> argument to suppress isolated warning types. </p>
<dl>
<dt><code>all</code></p>
<dd> This enables the implicit, portbind, select-range, timescale, and sensitivity-entire-array warning categories. </p>
<dt><code>implicit</code></p>
<dd> This enables warnings for creation of implicit declarations. For example, if a scalar wire X is used but not declared in the Verilog source, this will print a warning at its first use. </p>
<dt><code>portbind</code></p>
<dd> This enables warnings for ports of module instantiations that are not connected but probably should be. Dangling input ports, for example, will generate a warning. </p>
<dt><code>select-range</code></p>
<dd> This enables warnings for constant out of bound selects. This includes partial or fully out of bound selects as well as a select containing a &#8216;bx or &#8216;bz in the index. </p>
<dt><code>timescale</code></p>
<dd> This enables warnings for inconsistent use of the timescale directive. It detects if some modules have no timescale, or if modules inherit timescale from another file. Both probably mean that timescales are inconsistent, and simulation timing can be confusing and dependent on compilation order. </p>
<dt><code>infloop</code></p>
<dd> This enables warnings for always statements that may have runtime infinite loops (has paths with no or zero delay). This class of warnings is not included in <code>-Wall</code> and hence does not have a <code>no-</code> variant. A fatal error message will always be printed when the compiler can determine that there will definitely be an infinite loop (all paths have no or zero delay). </p>
<p> When you suspect an always statement is producing a runtime infinite loop use this flag to find the always statements that need to have their logic verified. It is expected that many of the warnings will be false positives, since the code treats the value of all variables and signals as indeterminate. </p>
<dt><code>sensitivity-entire-vector</code></p>
<dd> This enables warnings for when a part select within an &quot;always @*&quot; statement results in the entire vector being added to the implicit sensitivity list. Although this behaviour is prescribed by the IEEE standard, it is not what might be expected and can have performance implications if the vector is large. </p>
<dt><code>sensitivity-entire-array</code></p>
<dd> This enables warnings for when a word select within an &quot;always @*&quot; statement results in the entire array being added to the implicit sensitivity list. Although this behaviour is prescribed by the IEEE standard, it is not what might be expected and can have performance implications if the array is large. </p>
</dl>
<h2>SYSTEM FUNCTION TABLE FILES</h2>
<p> If the source file name as a <code>.sft</code> suffix, then it is taken to be a system function table file. A System function table file is used to describe to the compiler the return types for system functions. This is necessary because the compiler needs this information to elaborate expressions that contain these system functions, but cannot run the sizetf functions since it has no run-time. </p>
<p> The format of the table is ASCII, one function per line. Empty lines are ignored, and lines that start with the &#8216;<i>#</i>&#8216; character are comment lines. Each non-comment line starts with the function name, then the vpi type (i.e. vpiSysFuncReal). The following types are supported: </p>
<dl>
<dt><code>vpiSysFuncReal</code></p>
<dd> The function returns a real/realtime value. </p>
<dt><code>vpiSysFuncInt</code></p>
<dd> The function returns an integer. </p>
<dt><code>vpiSysFuncSized &lt;wid&gt; &lt;signed|unsigned&gt;</code></p>
<dd> The function returns a vector with the given width, and is signed or unsigned according to the flag. </p>
</dl>
<h2>COMMAND FILES</h2>
<p> The command file allows the user to place source file names and certain command line switches into a text file instead of on a long command line. Command files can include C or C++ style comments, as well as # comments, if the # starts the line. </p>
<dl>
<dt><i>file name</i></p>
<dd> A simple file name or file path is taken to be the name of a Verilog source file. The path starts with the first non-white-space character. Variables are substituted in file names. </p>
<dt><code>-c&nbsp;<wbr></code><i>cmdfile</i> -f&nbsp;<wbr><i>cmdfile</i></p>
<dd> A <code>-c</code> or <code>-f</code> token prefixes a command file, exactly like it does on the command line. The cmdfile may be on the same line or the next non-comment line. </p>
<dt><code>-y&nbsp;<wbr></code><i>libdir</i></p>
<dd> A <code>-y</code> token prefixes a library directory in the command file, exactly like it does on the command line. The parameter to the <code>-y</code> flag may be on the same line or the next non-comment line. </p>
<p> Variables in the <i>libdir</i> are substituted. </p>
<dt><code>+incdir+</code><i>includedir</i></p>
<dd> The <code>+incdir+</code> token in command files gives directories to search for include files in much the same way that <code>-I</code> flags work on the command line. The difference is that multiple <i>+includedir</i> directories are valid parameters to a single <code>+incdir+</code> token, although you may also have multiple <code>+incdir+</code> lines. </p>
<p> Variables in the <i>includedir</i> are substituted. </p>
<dt><code>+libext+</code><i>ext</i></p>
<dd> The <code>+libext</code> token in command files fives file extensions to try when looking for a library file. This is useful in conjunction with <code>-y</code> flags to list suffixes to try in each directory before moving on to the next library directory. </p>
<dt><code>+libdir+</code><i>dir</i></p>
<dd> This is another way to specify library directories. See the -y flag. </p>
<dt><code>+libdir-nocase+</code><i>dir</i></p>
<dd> This is like the <code>+libdir</code> statement, but file names inside the directories declared here are case insensitive. The missing module name in a lookup need not match the file name case, as long as the letters are correct. For example, &quot;foo&quot; matches &quot;Foo.v&quot; but not &quot;bar.v&quot;. </p>
<dt><code>+define+</code><i>NAME</i>=<i>value</i></p>
<dd> The <code>+define+</code> token is the same as the <code>-D</code> option on the command line. The value part of the token is optional. </p>
<dt><code>+timescale+</code><i>value</i></p>
<dd> The <code>+timescale+</code> token is used to set the default timescale for the simulation. This is the time units and precision before any `timescale directive or after a `resetall directive. The default is 1s/1s. </p>
<dt><code>+toupper-filename</code></p>
<dd> This token causes file names after this in the command file to be translated to uppercase. This helps with situations where a directory has passed through a DOS machine, and in the process the file names become munged. </p>
<dt><code>+tolower-filename</code></p>
<dd> This is similar to the <code>+toupper-filename</code> hack described above. </p>
<dt><code>+integer-width+</code><i>value</i></p>
<dd> This allows the programmer to select the width for integer variables in the Verilog source. The default is 32, the value can be any desired integer value. </p>
</dl>
<h2>VARIABLES IN COMMAND FILES</h2>
<p> In certain cases, iverilog supports variables in command files. These are strings of the form &quot;$(<i>varname</i>)&quot; or &quot;${<i>varname</i>}&quot;, where <i>varname</i> is the name of the environment variable to read. The entire string is replaced with the contents of that variable. Variables are only substituted in contexts that explicitly support them, including file and directory strings. </p>
<p> Variable values come from the operating system environment, and not from preprocessor defines elsewhere in the file or the command line. </p>
<h2>PREDEFINED MACROS</h2>
<p> The following macros are predefined by the compiler:</p>
<dl>
<dt><code>__ICARUS__ = 1</code></p>
<dd> This is always defined when compiling with Icarus Verilog. </p>
<dt><code>__VAMS_ENABLE__ = 1</code></p>
<dd> This is defined if Verilog-AMS is enabled. </p>
</dl>
<h2>EXAMPLES</h2>
<p> These examples assume that you have a Verilog source file called hello.v in the current directory </p>
<p> To compile hello.v to an executable file called a.out: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iverilog hello.v</p>
<p> To compile hello.v to an executable file called hello: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iverilog -o hello hello.v</p>
<p> To compile and run explicitly using the vvp runtime: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iverilog -ohello.vvp -tvvp hello.v</p>
<h2>AUTHOR</h2>
<pre>
Steve Williams (steve [at] icarus.com)
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vvp/">vvp</a>(1), <code>&lt;<a rel="nofollow" href="http://www.icarus.com/eda/verilog/">http://www.icarus.com/eda/verilog/</a>&gt;</code> </p>
<p> Tips on using, debugging, and developing the compiler can be found at <code>&lt;<a rel="nofollow" href="http://iverilog.wikia.com/">http://iverilog.wikia.com/</a>&gt;</code> </p>
<h2>COPYRIGHT</h2>
<pre>
Copyright &#169;  2002-2010 Stephen Williams
This document can be freely redistributed according to the terms of the
GNU General Public License version 2.0
</pre>
<h2>Index</h2>
