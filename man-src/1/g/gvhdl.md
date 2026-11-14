---
title: "gvhdl(1)"
name: "gvhdl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gvhdl/"
description: "gvhdl – Frontend to the VHDL compiler/simulator FreeHDL."
---

<h2>NAME</h2>
<p> gvhdl &#8211; Frontend to the VHDL compiler/simulator FreeHDL.</p>
<h2>SYNOPSIS</h2>
<p> <code>gvhdl</code> [<i>OPTION</i>] &#8230; [<i>VHDL_FILES</i>] &#8230; [<i>OBJECT_FILES</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>FreeHDL</code> is a compiler/simulator suite for the hardware description language VHDL. VHDL&#8217;93 as well as VHDL&#8217;87 standards are supported. </p>
<p> <code>FreeHDL</code> translates the original VHDL source FILEs into C++. Then, the C++ source can be compiled and linked to the kernel to build the simulation program. Starting the generated executable will simulate the corresponding VHDL model. The actual build process to generate the simulator from the VHDL source is a complex process which is handled by the <code>gvhdl</code> script. </p>
<p> <i>VHDL_FILES</i> is a list of VHDL source file names that must end with .vhdl or .vhd. The first VHDL file name also determines the name of the simulator executable. This is, the final executable will be named after the first VHDL file without the .vhdl or .vhd extension. Note that the object files as well as the simulator will be created in the current directory. </p>
<p> <i>OBJECT_FILES</i> specifies a list of object files that are linked to the simulator executable. <code>gvhdl</code> considers all files that end with .o to be object files. Typically, these object files are generated previously (using option -c) from VHDL source code during a separate compilation step.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-L</code> VHDLLIB</p>
<dd> Path to VHDL library root directory. Within this directory the compiler search for a file named <i>v2cc.libs</i>. The mapping file <i>v2cc.libs</i> translates library unit names to directories. Note that more than one VHDLLIB may be provided.</p>
<dt><code>-g</code></p>
<dd> Adds debug information to the executable. In detail, this options associates the generated machine code to the corresponding lines in the VHDL source files.</p>
<dt><code>-G</code></p>
<dd> Adds debug information to the executable but does not associate machine code to VHDL source lines. This option is actually used to debug the generated C++ code.</p>
<dt><code>-c</code></p>
<dd> Do not generate simulator executable. Using this option, the compiler translated VHDL source into executables and compiles them into object code but does not generate a final simulator executable. This option is especially useful to compile VHDL packages.</p>
<dt><code>-l</code> LIBNAME</p>
<dd> Associate the VHDL source code to VHDL library LIBNAME. As default the library name WORK is used. This option is especially important if VHDL components from several VHDL libraries shall be build into the simulator. Note that in order to successfully use a VHDL component from another than the current working library, the corresponding VHDL files must be found by the compiler using the mechanisms described in v2cc.libs. Further, components must be compiled with the appropriate -l LIBNAME option.</p>
<dt><code>&#8211;relaxed-component-visibility</code></p>
<dd> Allows invisible default bindings from <i>WORK</i>.</p>
<dt><code>&#8211;libieee</code></p>
<dd> Add the IEEE standard library files to the simulation executable.</p>
<dt></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dd>
<dl>
<dt>V2CC_LIBRARY_PATH</p>
<dd> The variable V2CC_LIBRARY_PATH consists of &quot;:&quot; separated filenames. In addition to the environment variable, you can use the &quot;-L libdir&quot; command line option with v2cc. The directories specified with &quot;-L&quot; are added in front of the ones specified by V2CC_LIBRARY_PATH. In the final library path, they appear in the same order as on the command line.</dl>
<h2>SUPPORTED VHDL SUBSET</h2>
<p> Currently, FreeHDL does not support the entire VHDL&#8217;93 standard. The following incomplete list gives an overview on what is currently not supported: </p>
<p> &#8211; Individual association of formals of composite type are not supported. </p>
<p> &#8211; Shared variables are not supported. </p>
<p> &#8211; Attributes transaction, quiet, stable and delayed are not supported. </p>
<p> &#8211; User defined attributes are not supported. </p>
<p> &#8211; Groups are not supported. </p>
<p> &#8211; Guarded signal assignments are not supported. </p>
<p> &#8211; Configurations are not supported. </p>
<p> &#8211; Currently, drivers cannot be switched off.</p>
<h2>EXAMPLES</h2>
<p> Use </p>
<p>&nbsp;<wbr>gvhdl -c adder.vhdl </p>
<p> to build an object file for adder.vhdl. Note that adder.vhdl may contain several VHDL models. </p>
<p>&nbsp;<wbr>gvhdl adder.vhdl </p>
<p> will generate a simulator for the <code>last</code> VHDL model found in adder.vhdl. However, in this case, all VHDL components that area required to build the simulator must be included in the VHDL source file. </p>
<p>&nbsp;<wbr>gvhdl top.vhdl adder.o &#8211;libieee </p>
<p> generates a simulator for the last VHDL model found in top.vhdl by compiling all models in top.vhdl and linking (the previously generated) adder.o object file and the IEEE standard libraries to the executable. </p>
<p>&nbsp;<wbr>gvhdl -c -l mylib adder.vhdl </p>
<p> will build an object file including all components provided in adder.vhdl. However, in this case the components will be associated with library mylib instead of the default library name work. Note that option -l does only effect the generated C++ source code but does not alter the place where the object files or executables are stored.</p>
<h2>SIMULATION COMMANDS</h2>
<p> After the simulator has been started a short summary of the available commands is printed to the screen: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>c&nbsp;<wbr>&lt;number&gt;&nbsp;<wbr>: execute cycles&nbsp;<wbr>=&nbsp;<wbr>execute&nbsp;<wbr>&lt;number&gt;&nbsp;<wbr>simulation cycles<br />
&nbsp;<wbr>&nbsp;<wbr>n&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: next&nbsp;<wbr>=&nbsp;<wbr>execute next simulation cycle<br />
&nbsp;<wbr>&nbsp;<wbr>q&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: quit&nbsp;<wbr>=&nbsp;<wbr>quit simulation<br />
&nbsp;<wbr>&nbsp;<wbr>r&nbsp;<wbr>&lt;time&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: run&nbsp;<wbr>=&nbsp;<wbr>execute simulation for&nbsp;<wbr>&lt;time&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>d&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: dump&nbsp;<wbr>=&nbsp;<wbr>dump signals<br />
&nbsp;<wbr>&nbsp;<wbr>doff&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: dump off&nbsp;<wbr>=&nbsp;<wbr>stop dumping signals<br />
&nbsp;<wbr>&nbsp;<wbr>don&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: dump on&nbsp;<wbr>=&nbsp;<wbr>continue dumping signals<br />
&nbsp;<wbr>&nbsp;<wbr>s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: show&nbsp;<wbr>=&nbsp;<wbr>show signal values<br />
&nbsp;<wbr>&nbsp;<wbr>dv&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: dump var&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>dump a signal from the signal lists<br />
&nbsp;<wbr>&nbsp;<wbr>ds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: dump show&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>shows the list of dumped signals<br />
&nbsp;<wbr>&nbsp;<wbr>nds&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: number&nbsp;<wbr>&nbsp;<wbr>show&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>shows the number&nbsp;<wbr>&nbsp;<wbr>of dumped signals<br />
&nbsp;<wbr>&nbsp;<wbr>dc&nbsp;<wbr>[-f&nbsp;<wbr>&lt;filename&gt;]&nbsp;<wbr>[-t&nbsp;<wbr>&lt;timescale&gt;&nbsp;<wbr>&lt;time unit&gt;]&nbsp;<wbr>[-cfg&nbsp;<wbr>&lt;translation file&gt;]&nbsp;<wbr>[-q]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: configures dump process&nbsp;<wbr> </p>
<p> Note that signals are dumped into a file (default file name is &quot;wave.dmp&quot;) in VCD format. This file format should be accepted by each VCD waveform viewer. The file name is set to &quot;wave.dmp&quot; but may be changed using &quot;dc -f &lt;new_file_name&gt;&quot;. However, make sure to execute &quot;dc -f &#8230;&quot; before executing &quot;d&quot;.</p>
<h2>SIMULATOR COMMAND LINE OPTIONS</h2>
<p> Simulation can be controlled via the command line parameter &#8216;-cmd &quot;cmd1; cmd2; &#8230;&quot;&#8217; where &#8216;cmd1&#8217;, &#8216;cmd2&#8217;, &#8230; are simulation commands as described in the previous section. Note that each command must be separated by &#8216;;&#8217;. E.g., executing </p>
<p>./top -cmd&nbsp;<wbr>&quot;d;run 1000 ns;q;&quot; </p>
<p> will start simulation program &#8216;top&#8217;, dump all signals and run simulation for 1000 ns. Finally, simulation is terminated. Actually, the last command &#8216;q;&#8217; is optional as the simulator automatically terminates as soon as the last command has been executed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-freehdl-v2cc/">freehdl-v2cc</a>(1), <a href="/docs/linux/man/1-freehdl-config/">freehdl-config</a>(1), <a href="/docs/linux/man/5-v2cc-libs/">v2cc.libs</a>(5)</p>
<h2>AVAILABILITY</h2>
<p> The latest version of FreeHDL can always be obtained from <code><a rel="nofollow" href="http://www.freehdl.seul.org">www.freehdl.seul.org</a></code></p>
<h2>REPORTING BUGS</h2>
<p> Known bugs are documented within the BUGS file. If your report addresses a parser related topic then contact Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt;. If it is related to the code generator or compiler then send an email to Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. If your are not sure send it to Edwin. He will take care of forwarding your report to the appropriate recipient.</p>
<h2>COPYRIGHT</h2>
<p> Edwin Naroska &#169; 1999, 2000, 2001, 2002, 2003, 2004, 2005 &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>AUTHORS</h2>
<p> Written by Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt; and Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. </p>
<h2>Index</h2>
