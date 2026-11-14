---
title: "hugs(1)"
name: "hugs"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hugs/"
description: "hugs, runhugs, ffihugs – Hugs 98, functional programming system"
---

<h2 class="name">NAME</h2>
<p> hugs, runhugs, ffihugs &#8211; Hugs 98, functional programming system </p>
<h2>SYNOPSIS</h2>
<p> <code>hugs</code> [ <i>options</i> ] [ <i>modules</i> ]<br />
 <code>runhugs</code> [ <i>options</i> ] <i>module</i> [ <i>args</i> ]<br />
 <code>ffihugs</code> [ <i>options</i> ] <i>module</i> [ <i>compiler_argument</i> ] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Hugs is an interpreter for Haskell, a standard non-strict functional programming language. Hugs implements almost all of the Haskell 98 standard, except for mutually recursive modules. The name <code>Hugs</code> is a mnemonic for the <code>Haskell User&#8217;s Gofer System</code>. </p>
<p> The interpreter is started using the <i>hugs</i> command. After processing options, it loads the standard module <code>Prelude</code> and any other modules listed on the command line. </p>
<p> Each Haskell module is stored in a separate file. When loading a module <i>name</i>, <i>Hugs</i> replaces each `<code>.</code>&#8216; in <i>name</i> with a `<code>/</code>&#8216; and looks in each of the directories on its search path (see <code>-P</code> under <code>OPTIONS</code>) for the files <i>name</i><code>.hs</code> and <i>name</i><code>.lhs</code>. (The recognized suffixes may be changed using the <code>-S</code> option, described under <code>OPTIONS</code>.) It also tries <i>name</i> as a literal filename. Files ending in &quot;<code>.lhs</code>&quot; are treated as literate scripts.</p>
<h2>OPTIONS</h2>
<p> Some options are toggled with <code>+</code> or <code>&#8211;</code> to turn them on or off, respectively.</p>
<h3>Language conformance</h3>
<dl>
<dt><code>+98</code></p>
<dd> Accept only Haskell 98 (cannot be changed within <i>Hugs</i>; default: on). Turning this off enables several special Hugs extensions, which are described in the <i>Hugs 98 User Manual</i>.</p>
<dt><code>+o</code></p>
<dd> Allow overlapping instances (a Hugs extension; default: off)</p>
<dt><code>+O</code></p>
<dd> Allow unsafe overlapping instances (a Hugs extension; default: off)</p>
<dt><code>+H</code></p>
<dd> Allow `here documents&#8217; (a Hugs extension; default: off)</dl>
<h3>Module loading</h3>
<dl>
<dt><code>+l</code></p>
<dd> Treat files whose names end in neither `<code>.hs</code>&#8216; nor `<code>.lhs</code>&#8216; as literate scripts (default: off)</p>
<dt><code>+.</code></p>
<dd> Print dots to show progress while loading modules (default: off)</p>
<dt><code>+q</code></p>
<dd> Print nothing to show progress while loading modules (default: on)</p>
<dt><code>+w</code></p>
<dd> Always show which files are loaded (default: off)</dl>
<h3>Expression evaluation</h3>
<dl>
<dt><code>+s</code></p>
<dd> Print number of reductions/cells after each evaluation (default: off)</p>
<dt><code>+t</code></p>
<dd> Print type after each evaluation (default: off)</p>
<dt><code>+T</code></p>
<dd> Apply the Haskell defaulting rules before printing types (default: off)</p>
<dt><code>+g</code></p>
<dd> Print number of cells recovered after each garbage collection (default: off)</p>
<dt><code>+Q</code></p>
<dd> Qualify names when printing (default: off)</p>
<dt><code>+k</code></p>
<dd> Show kind errors in full (default: off)</p>
<dt><code>+u</code></p>
<dd> Use &quot;<code>show</code>&quot; to display results (default: on)</p>
<dt><code>+I</code></p>
<dd> Display results of IO programs (default: off)</dl>
<h3>Parameters</h3>
<p> Other options (in which <code>&#8211;</code> could be replaced by <code>+</code>, the choice making no difference) are:</p>
<dl>
<dt><code>-h</code><i>num</i></p>
<dd> Set heap size (cannot be changed within <i>Hugs</i>; default: 250K)</p>
<dt><code>-p</code><i>str</i></p>
<dd> Set prompt string to <i>str</i> (default: `<code>%s&gt; </code>&#8216;). Any <code>%s</code> in the prompt will be replaced by the current module name.</p>
<dt><code>-r</code><i>str</i></p>
<dd> Set repeat last expression string to <i>str</i> (default: <code>$$</code>).</p>
<dt><code>-P</code><i>str</i></p>
<dd> Set search path for source files to <i>str</i>, which should be a colon-separated list of directories. A null entry in this list will be replaced by the previous search path; a null <i>str</i> means the default path. Any occurrence of <code>{Hugs}</code> in this string is expanded to the Hugs library directory, namely <code>/usr/lib64/hugs</code>. Similarly, <code>{Home}</code> is expanded to your home directory (the value of the <code>HOME</code> environment variable). An entry of the form `<i>directory</i><code>/*</code>&#8216; means all the immediate subdirectories of <i>directory</i>. The default value is</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>.:{Home}/lib/hugs/packages/*:/usr/local/lib/hugs/packages/*:{Hugs}/packages/*</code></dl>
</dl>
<dt><code>-S</code><i>str</i></p>
<dd> Set the colon-separated list of source file suffixes to <i>str</i> (default: <code>.hs:.lhs</code>). A null entry in this list will be replaced by the previous suffix list; a null <i>str</i> means the default list.</p>
<dt><code>-E</code><i>str</i></p>
<dd> Use editor setting given by <i>str</i> (default: the value of the <code>EDITOR</code> environment variable). Any occurrences of <code>%d</code> and <code>%s</code> in the editor option are replaced by the start line number and the name of the file to be edited, respectively. A common setting is &quot;<i>vi +%d %s</i>&quot;.</p>
<dt><code>-c</code><i>num</i></p>
<dd> Set constraint cutoff limit in the type checker to <i>num</i> (default: 40).</p>
<dt><code>-F</code><i>cmd</i></p>
<dd> Set preprocessor filter for source files to <i>cmd</i> (unset by default). Instead of reading a source file directly, <i>Hugs</i> will read the standard output of <i>cmd</i> run with the source file name as argument.</p>
<dt><code>-X</code><i>str</i></p>
<dd> The string <i>str</i> is interpreted as an option string. This is useful, for example, for passing multiple arguments to <code>runhugs</code> in a <code>#!</code> script.</dl>
<h2>COMMANDS</h2>
<p> Once the interpreter has been loaded, the following commands are available:</p>
<dl>
<dt><code>:load</code> [<i>modules</i>]</p>
<dd> clear all modules except the prelude, and load the specified modules.</p>
<dt><code>:also</code> <i>modules</i></p>
<dd> read additional modules.</p>
<dt><code>:reload</code></p>
<dd> repeat last <code>load</code> command.</p>
<dt><code>:edit</code> <i>file</i></p>
<dd> edit <i>file</i>.</p>
<dt><code>:edit</code></p>
<dd> edit last file.</p>
<dt><code>:module</code> <i>module</i></p>
<dd> set module for evaluating expressions.</p>
<dt><i>expr</i></p>
<dd> evaluate expression.</p>
<dt><code>:type</code> <i>expr</i></p>
<dd> print type of expression.</p>
<dt><code>:?</code></p>
<dd> display this list of commands.</p>
<dt><code>:set</code> <i>options</i></p>
<dd> set command line options.</p>
<dt><code>:set</code></p>
<dd> help on command line options.</p>
<dt><code>:names</code> [<i>patterns</i>]</p>
<dd> list names currently in scope matching any of the shell-style patterns.</p>
<dt><code>:info</code> <i>names</i></p>
<dd> describe named objects.</p>
<dt><code>:browse</code> <i>modules</i></p>
<dd> browse names exported by <i>modules</i>.</p>
<dt><code>:find</code> <i>name</i></p>
<dd> edit file containing definition of <i>name</i>.</p>
<dt><code>:!</code><i>command</i></p>
<dd> shell escape.</p>
<dt><code>:cd</code> <i>dir</i></p>
<dd> change directory.</p>
<dt><code>:gc</code></p>
<dd> force garbage collection.</p>
<dt><code>:version</code></p>
<dd> print Hugs version.</p>
<dt><code>:quit</code></p>
<dd> exit Hugs interpreter.</dl>
<p> Any command may be abbreviated to <code>:</code><i>c</i> where <i>c</i> is the first character in the full name. On most systems, you can also exit from <i>Hugs</i> by typing the end-of-file character (^D). </p>
<p> Note that the interrupt key (^C on most systems) can be used at any time whilst using <i>Hugs</i> to abandon the process of reading in a file of function definitions or the evaluation of an expression. When the interrupt is detected, <i>Hugs</i> prints the string &quot;<code>{Interrupted!}</code>&quot; and prints the prompt so that further commands can be entered.</p>
<h2>STANDALONE PROGRAMS</h2>
<p> The <i>runhugs</i> command is an interpreter for an executable Hugs script, which must contain a Haskell <code>Main</code> module. For example, the executable file <code>hello</code> might contain the lines </p>
<pre>
<dl><dt><dd><code>#!/usr/bin/runhugs +l
&gt; module Main where
&gt; main = putStr &quot;Hello, World
&quot;</code>
</dl>
</pre>
<p> When this file is executed, <i>runhugs</i> will invoke the <code>main</code> function. Any arguments given on the command line will be available through <code>getArgs</code>. </p>
<p> Note that <code>#!</code> passes only one orgument to the script. The <code>-X</code> option may be used to get around this.</p>
<h2>C INTERFACE</h2>
<p> On architectures that support dynamic linking, <i>Hugs</i> implements the part of the <i>Haskell 98 Foreign Function Interface</i> (FFI) that allows Haskell functions to call C routines. (On the x86, PowerPC and Sparc architectures, all <code>foreign import</code>s are supported; on others, only <code>static</code> imports are provided.) Modules containing such <code>foreign</code> declarations must be compiled using the <i>ffihugs</i> command before use with <code>hugs</code>. Additional arguments for the C compiler may be supplied via <i>compiler_argument</i>s. For example, suppose you have some C functions in <code>test.c</code> and some FFI declarations for those functions in <code>Test.hs</code> and the code in <code>test.c</code> needs to be compiled with <code>-lm</code>. Then you would compile the module with the command</p>
<dl>
<dt>
<dd> <code>ffihugs Test.hs test.c -lm </code></dl>
<p> which generates an object file <code>Test.so</code>. Then when <i>hugs</i> loads <code>Test.hs</code>, it will also load <code>Test.so</code>. </p>
<p> In the standard FFI, each <code>foreign import</code> declaration should name a C header file containing the prototype of the function. Because this is often cumbersome, <code>ffihugs</code> provides the following additional option:</p>
<dl>
<dt><code>-i</code><i>str</i></p>
<dd> Specify an include for the generated C file. The include string should be something that can follow &quot;<code>#include</code>&quot; in a C program, as in</p>
<dt>
<dd> <code>ffihugs &#8216;-i&lt;math.h&gt;&#8217; &#8216;-i&quot;mydefs.h&quot;&#8217; Test.hs test.c -lm</code></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HUGSFLAGS</code></p>
<dd> Additional options for <i>hugs</i>, processed before any given on the command line.</p>
<dt><code>HUGSDIR</code></p>
<dd> The Hugs library directory (default: <code>/usr/lib64/hugs</code>).</p>
<dt><code>EDITOR</code></p>
<dd> The default editor, if <code>-E</code> is not given.</p>
<dt><code>SHELL</code></p>
<dd> Used to specify the shell that is invoked by the <code>:!</code> command.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/bin/hugs</i></p>
<dd> executable binary.</p>
<dt><i>/usr/lib64/hugs</i></p>
<dd> directory containing support files.</dl>
<h2>WEB REFERENCES</h2>
<dl>
<dt><i><a rel="nofollow" href="http://www.haskell.org/hugs/">http://www.haskell.org/hugs/</a></i></p>
<dd> The Hugs home page.</p>
<dt><i><a rel="nofollow" href="http://www.haskell.org/">http://www.haskell.org/</a></i></p>
<dd> The Haskell home page, including the language definition, various mailing lists and much more.</dl>
<h2>SEE ALSO</h2>
<p> Mark P. Jones et al. <i>Hugs 98 User Manual</i>, June 1999. </p>
<p> <i>Hugs 98 User&#8217;s Guide</i> (distributed with Hugs). </p>
<p> Paul Hudak &amp; Joseph H. Fasel. A gentle introduction to Haskell. <i>ACM SIGPLAN Notices</i>, <a href="/docs/linux/man/5-27/">27</a>(5), May 1992. </p>
<p> S. Peyton Jones (editor). <i>Haskell 98 Language and Libraries: The Revised Report</i>. December 2002. </p>
<p> Manuel Chakravarty et al. <i>Haskell 98 Foreign Function Interface 1.0,</i> <i>Addendum to the Haskell Report</i>, September 2003.</p>
<h2>AUTHOR</h2>
<p> Hugs 98: Mark Jones and others, June 1999. </p>
<p> Manual page: Jonathan Bowen, modified by Gary Leavens, and then (with apologies to the original authors) by Mark Jones. Updated for Hugs 98 by Antti-Juhani Kaijanaho and Ross Paterson. Updated for the March 2005 ffihugs changes by Joseph P. Skudlarek. </p>
<h2>Index</h2>
