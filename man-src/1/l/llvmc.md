---
title: "llvmc(1)"
name: "llvmc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvmc/"
description: "llvmc – The LLVM Compiler Driver (WIP)"
---

<h2>SYNOPSIS</h2>
<p> <code>llvmc</code> [<i>options</i>] <i>filenames&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>llvmc</code> is a configurable driver for invoking other <font SIZE="-1">LLVM</font> (and non-LLVM) tools in order to compile, optimize and link software for multiple languages. For those familiar with <font SIZE="-1">FSF</font>&#8216;s <code>gcc</code> tool, it is very similar. Please note that <code>llvmc</code> is considered an experimental tool.</p>
<h2>OPTIONS</h2>
<h2>Built-in Options</h2>
<p> <font SIZE="-1">LLVMC</font> has some built-in options that can&#8217;t be overridden in the configuration libraries.</p>
<dl>
<dt><code>-o</code> <i>filename</i></dt>
<dd> Output file name.</dd>
<dt><code>-x</code> <i>language</i></dt>
<dd> Specify the language of the following input files until the next <code>-x</code> option.</dd>
<dt><code>-load</code> <i>plugin_name</i></dt>
<dd> Load the specified plugin <font SIZE="-1">DLL</font>. Example: -load&nbsp;<wbr><tt>$LLVM_DIR</tt>/Release/lib/LLVMCSimple.so.</dd>
<dt><code>-v</code> or <code>&#8211;verbose</code></dt>
<dd> Enable verbose mode, i.e. print out all executed commands.</dd>
<dt><code>&#8211;check-graph</code></dt>
<dd> Check the compilation for common errors like mismatched output/input language names, multiple default edges and cycles. Because of plugins, these checks can&#8217;t be performed at compile-time. Exit with code zero if no errors were found, and return the number of found errors otherwise. Hidden option, useful for debugging <font SIZE="-1">LLVMC</font> plugins.</dd>
<dt><code>&#8211;view-graph</code></dt>
<dd> Show a graphical representation of the compilation graph and exit. Requires that you have <i>dot</i> and <i>gv</i> programs installed. Hidden option, useful for debugging <font SIZE="-1">LLVMC</font> plugins.</dd>
<dt><code>&#8211;write-graph</code></dt>
<dd> Write a <i>compilation-graph.dot</i> file in the current directory with the compilation graph description in Graphviz format (identical to the file used by the <code>&#8211;view-graph</code> option). The <code>-o</code> option can be used to set the output file name. Hidden option, useful for debugging <font SIZE="-1">LLVMC</font> plugins.</dd>
<dt><code>&#8211;save-temps</code></dt>
<dd> Write temporary files to the current directory and do not delete them on exit. This option can also take an argument: the <i>&#8211;save-temps=obj</i> switch will write files into the directory specified with the <i>-o</i> option. The <i>&#8211;save-temps=cwd</i> and <i>&#8211;save-temps</i> switches are both synonyms for the default behaviour.</dd>
<dt><code>&#8211;temp-dir</code> <i>directory</i></dt>
<dd> Store temporary files in the given directory. This directory is deleted on exit unless <i>&#8211;save-temps</i> is specified. If <i>&#8211;save-temps=obj</i> is also specified, <i>&#8211;temp-dir</i> is given the precedence.</dd>
<dt><code>-help</code></dt>
<dd> Print a summary of command-line options and exit.</dd>
<dt><code>-help-hidden</code></dt>
<dd> Print a summary of command-line options and exit. Print help even for options intended for developers.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>@</code><i>file</i></dt>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </dd>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The file may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>Control Options</h2>
<p> By default, <font SIZE="-1">LLVMC</font> is built with some standard configuration libraries that define the following options:</p>
<dl>
<dt><code>-clang</code></dt>
<dd> Use Clang instead of llvm-gcc.</dd>
<dt><code>-opt</code></dt>
<dd> Enable optimization passes with <code>opt</code>. To pass options to the <code>opt</code> program use the <code>-Wo,</code> option.</dd>
<dt><code>-I</code> <i>directory</i></dt>
<dd> Add a directory to the header file search path.</dd>
<dt><code>-L</code> <i>directory</i></dt>
<dd> Add <i>directory</i> to the library search path.</dd>
<dt><code>-F</code> <i>directory</i></dt>
<dd> Add <i>directory</i> to the framework search path.</dd>
<dt><code>-l</code><i>name</i></dt>
<dd> Link in the library lib<i>name</i>.[bc | a | so]. This library should be a bitcode library.</dd>
<dt><code>-framework</code> <i>name</i></dt>
<dd> Link in the library lib<i>name</i>.[bc | a | so]. This library should be a bitcode library.</dd>
<dt><code>-emit-llvm</code></dt>
<dd> Output <font SIZE="-1">LLVM</font> bitcode (with <code>-c</code>) or assembly (with <code>-S</code>) instead of native object (or assembly). If <code>-emit-llvm</code> is given without either <code>-c</code> or <code>-S</code> it has no effect.</dd>
<dt><code>-Wa</code></dt>
<dd> Pass options to assembler.</dd>
<dt><code>-Wl</code></dt>
<dd> Pass options to linker.</dd>
<dt><code>-Wo</code></dt>
<dd> Pass options to opt.</dd>
<dt><code>-Wllc</code></dt>
<dd> Pass options to llc (code generator).</dd></dl>
<h2>EXIT STATUS</h2>
<p> If <code>llvmc</code> succeeds, it will exit with code 0. Otherwise, if an error occurs, it will exit with a non-zero value. If one of the compilation tools returns a non-zero status, pending actions will be discarded and <code>llvmc</code> will return the same result code as the failing compilation tool.</p>
<h2>SEE ALSO</h2>
<p> llvm-gcc, llvm-g++, llvm-as, llvm-dis, llc, llvm-link</p>
<h2>AUTHORS</h2>
<p> Maintained by the <font SIZE="-1">LLVM</font> Team (&lt;<a rel="nofollow" href="http://llvm.org">http://llvm.org</a>&gt;). </p>
