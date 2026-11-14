---
title: "falcon(1)"
name: "falcon"
section: "1"
letter: "f"
url: "/docs/linux/man/1-falcon/"
description: "falcon – The Falcon Programming Language command line interpreter"
---

<h2>NAME</h2>
<p> falcon &#8211; The Falcon Programming Language command line interpreter </p>
<h2>SYNOPSIS</h2>
<p> <code>falcon [options] [main_script] [script_options]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>falcon</code> command line interpreter is used to launch, compile, assemble or debug scripts written in the Falcon Programming Language. The command line interpreter pushes the <code>core</code> module and the <code>rtl</code> module in the script load table, so they are available by default to all the scripts. </p>
<p> The default operation is that of launching the given script, or read it from the standard input if the script name is not given. By default, <code>falcon</code> saves also the compiled module of the script in the same directory where it is found, changing the extension to &quot;.fam&quot;. </p>
<p> The <code>main_script</code> can be a &quot;logical&quot; module name, a relative path or an absolute path. In case it&#8217;s a logical module name, that is, a script name without extension nor leading path, it is searched through the load path. The default load path is determined by the compilation options of the interpreter, and usually it includes the current directory. The environment variable <code>FALCON_LOAD_PATH</code> and the command line option <code>-L can change the default module search path.</code> </p>
<p> When the main module is found, its path is added to the module search path; in other words, there isn&#8217;t any need to specify the path containing the main module to have other modules in its same directory to get loaded. The main module and other source Falcon module it loads can be stored in a directory that is not listed in the module search path; indicating an absolute or relative path as the <code>main_script</code> parameter will add that path on top of the active search path. </p>
<p> If not differently specified, falcon will search for .fam modules newer than the relative .fal source scripts and will load those ones instead of compiling the sources. </p>
<p> Options past the script name will be directly passed in the <code>args[]</code> global variable of the script. </p>
<p> The interpreter is compatible with the UNIX script execution directive &quot;#!&quot;. A main script can have on the very first line of the code the directive </p>
<p> <i>#!/path/to/falcon</i> </p>
<p> to declare to the shell that the falcon command line is to be loaded. If falcon command line interpreter is also in the system PATH environment variable, which is usually the case of a normal installation, then the interpreter directive may also be simply </p>
<p> <i>#!/bin/env falcon</i> </p>
<p> It is then simply necessary to make the main script executable with </p>
<p> <i>chmod 744 script_name</i> </p>
<p> to be able to call the script directly. </p>
<p> Scripts executed in this way will add their path to the falcon module load path as soon as they are loade, so other modules referenced by them will be searched in the directory where they resides before being searched elsewhere. </p>
<p> Options to the falcon compiler may be passed normally by writing them after the execution directive in the main script. </p>
<p> Since version 0.8.12, the falcon command line interpreter has also an interactive mode which accepts statements and provide results as the expressions are evaluated. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> Assembles the given script. The resulting module is not executed; this options causes Falcon to just assemble the module and exit. By default, the output module is written in a file with the same name of the input file with the &quot;.fam&quot; extension.</p>
<dt>-c</p>
<dd> Compile but do not execute. This makes falcon to compile the given module into a .fam file and then terminate. By default, the .fam file is written to a file with the same name as the input one, with the .fam extension.</p>
<dt>-C</p>
<dd> Check for memory leaks in VM execution. Like the -M option of faltest, this function sets the falcon engine memory allocators to slower functions that checks for memory to be allocated and deallocated correctly during the execution of a module. If the script is executed, before Falcon exits it writes a small report to the standard output.</p>
<dt>-d &lt;directive&gt;=&lt;value&gt;</p>
<dd> Sets the given directive to the desired value. Compilation directives and their values are the ones that scripts can set through the directive statement.</p>
<dt>-d &lt;constant&gt;=&lt;value&gt;</p>
<dd> Sets the given constant to the desired value. Constants are made available at compile time, and can be employed in macro and meta compilation.</p>
<dt>-e&nbsp;<wbr>&lt;enc&gt;</p>
<dd> Set given encoding as default for VM I/O. Unless the scripts select a different I/O encoding, the streams that are provided to the falcon VM (like the output stream for printf) are encoded using the given ISO encoding. This overrides the default encoding that is detected by reading the environment settings. In example, if your system uses iso-8859-1 encoding by default, but you want your script to read and write utf-8 files, use the option <i>-e utf-8</i> </p>
<p> The <code>-e</code> option also determines the default encoding of the source files. To override this, use <code>-E</code></p>
<dt>-E&nbsp;<wbr>&lt;enc&gt;</p>
<dd> Set source script encoding. As <code>-e</code> , but this determines only the encoding used by falcon when loading the source scripts. This options overrides <code>-e</code> values, so it can be used to set the script encoding when they have to read and write from different encodings.</p>
<dt>-f</p>
<dd> Force recompilation of modules even when .fam are found.</p>
<dt>-h or -?</p>
<dd> Prints a brief help on stdout and exits.</p>
<dt>-h or -?</p>
<dd> Interactive mode. Falcon interpreter reads language statements from a prompt and present evaluation results to the user.</p>
<dt>-l &lt;lang_code&gt;</p>
<dd> Select a different language code for internationalized programs. This option loads an alternate string table for all the modules loaded. If the table doesn&#8217;t exist or if the modules doesn&#8217;t have a <code>.ftr</code> file containing the translation, the operation silently files and the original strings are used instead. Language codes should be in the international ISO format of five characters with a language name, an underscore and the regional code, like in <code>en_US</code></p>
<dt>-L &lt;path&gt;</p>
<dd> Changes the default load path. This overrides both the internal built in settings and the contents of environment variable FALCON_LOAD_PATH. Each directory in the path should be separated by &quot;;&quot; and use forward slashes, like this: </p>
<p> <i>falcon -L </i></p>
<dt>-m</p>
<dd> Use temporary files for intermediate steps. By default compilation is completely performed in memory; this option makes falcon to use temporary files instead.</p>
<dt>-M</p>
<dd> Do NOT save the compiled modules in &#8216;.fam&#8217; files. </p>
<dt>-o&nbsp;<wbr>&lt;fn&gt;</p>
<dd> Redirects output to &lt;fn&gt;. This is useful to control the output of falcon when using options as -c, -a, -S etc. If <code>&lt;fn&gt;</code> is a dash (-) the output is sent to stdout.</p>
<dt>-p&nbsp;<wbr>&lt;module&gt;</p>
<dd> Preloads the given module as if it were loaded by the main script.</p>
<dt>-P</p>
<dd> Ignore default load paths and uses only the paths set via the -L switch.</p>
<dt>-r</p>
<dd> Ignore source files and only use available .fam. This does not affects the main script; use the -x option if also the main script is a pre-compiled .fam module and source script must be ignored.</p>
<dt>-S</p>
<dd> Produce an assembly output. Writes an assembly representation of the given script to the standard output aznd the exit. Use -o to change file destination.</p>
<dt>-t</p>
<dd> Generates a syntactic tree of the source and writes it to the standard output, then exits. The syntactic tree is a representation of the script that is known by the compiler and used by the generators to create the final code. This option is useful when debugging the compiler and to test for the correct working of optimization algorithm.</p>
<dt>-T</p>
<dd> Force input parsing as .ftd (Falcon Template Document). Normally, only files ending with &quot;.ftd&quot; (case sensitive) are parsed as template document; when this switch is selected, the input is treated as a template document regardless of its name.</p>
<dt>-v</p>
<dd> Prints copyright notice and version and exits.</p>
<dt>-w</p>
<dd> After execution, requires the user to confirm program termination by pressing &lt;enter&gt;. This helps in point &amp; click environments, where Falcon window is closed as soon as the program terminates.</p>
<dt>-x</p>
<dd> Executes a pre-compiled .fam module.</p>
<dt>-y</p>
<dd> Creates a template file for internationalization. This option creates a single .ftt file from a single source, .fam module or binary module. By default, the name of the template is the same as the module plus &quot;.temp.ftt&quot; added at the end; it is possible to change the destination template file using the <code>-o</code> option. </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/lib/libfalcon_engine.so</i></p>
<dl>
<dt>
<dd> Default location of the Falcon Engine loadable module.</dl>
<p> <i>/usr/lib/falcon</i></p>
<dl>
<dt>
<dd> Default directory containing Falcon binary modules.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>FALCON_LOAD_PATH</p>
<dd> Default search path for modules loaded by the scripts. </p>
<dt>FALCON_SRC_ENCODING</p>
<dd> Default encoding for the source scripts loaded by falcon (when different from the system default). </p>
<dt>FALCON_VM_ENCODING</p>
<dd> Default encoding for the VM I/O streams (when different from system default). </p>
</dl>
<h2>AUTHOR</h2>
<p> Giancarlo Niccolai &lt;gc [at] falconpl.org&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-falrun/">falrun</a></code>(1) <code><a href="/docs/linux/man/1-faldisass/">faldisass</a></code>(1) <code><a href="/docs/linux/man/1-fallc-fal/">fallc.fal</a></code>(1) </p>
<h2>LICENSE</h2>
<p> This document is released under the &quot;GNU Free Documentation License, version 1.2&quot;. On Debian systems, the complete text of the Free Documentation License, version 1.2, can be found in /usr/share/common-licenses/. </p>
<h2>Index</h2>
