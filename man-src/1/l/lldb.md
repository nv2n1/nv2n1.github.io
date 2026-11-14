---
title: "lldb(1)"
name: "lldb"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lldb/"
description: "Darwin"
---

<p>Darwin</p>
<h2>NAME <code>lldb</code></h2>
<p> &#8211; The debugger</p>
<h2>SYNOPSIS <code>lldb</code></h2>
<p> [-<code>hvdexw</code> ] [-<code>a </code><i>arch</i> ] [-<code>l </code><i>script-language</i> ] [-<code>s </code><i>lldb-commands</i> ] [-<code>n </code><i>process-name</i> ] [-<code>p </code><i>pid</i> ] <i>[[&#8211;] &lt;PROGRAM-ARG1&gt; &lt;PROGRAM-ARG2&gt; &#8230;]</i></p>
<h2>DESCRIPTION <code>lldb</code></h2>
<p> is the command line interface for the LLDB debugger library. <code>lldb</code> can debug C, C++, Objective-C, and Objective-C++ programs. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-h, -help </code></p>
<dd> Prints out the usage information for the <code>lldb</code> debugger. The <code>&#8211;help</code> text may be more up-to-date and authoritative than the command line options described in this man page.</p>
<dt><code>-v, -version </code></p>
<dd> Prints out the version number of the <code>lldb</code> debugger.</p>
<dt><code>-a, -arch </code><i>arch</i></p>
<dd> Specifies which architecture <code>lldb</code> will use when launching the specified program (assuming the provided executable is built for multiple architectures.)</p>
<dt><code>-f, -file </code><i>filename</i></p>
<dd> Specifies the executable file that will be launching / attaching to.</p>
<dt><code>-n, -attach-name </code><i>process-name</i></p>
<dd> Specifies the name of a currently-running process to attach to. (or the name of a process to wait for if <code>-w</code> is used.)</p>
<dt><code>-w, -wait-for</code></p>
<dd> When used in concert with <code>-n process-name-E</code>, indicates that <code>lldb</code> should wait for a new process of that name to be started &#8212; and attach to it as early in the process-launch as possible.</p>
<dt><code>-p, -attach-pid </code><i>pid</i></p>
<dd> Specifies a currently running process that <code>lldb</code> should attach to.</p>
<dt><code>-l, -script-language </code><i>language</i></p>
<dd> Tells the debugger to use the specified scripting language for user-defined scripts, rather than the default. Valid scripting languages that can be specified include Python, Perl, Ruby and Tcl. Currently only the Python extensions have been implemented.</p>
<dt><code>-d, -debug</code></p>
<dd> Tells the debugger to print out extra information for debugging itself.</p>
<dt><code>-s, -source </code><i>filename</i></p>
<dd> Tells <code>lldb</code> to read in and execute the file &quot;<code>filename</code>&quot;, which should contain <code>lldb</code> commands.</p>
<dt><code>-e, -editor</code></p>
<dd> Instructs <code>lldb</code> to open source files using the host&#8217;s &quot;external editor&quot; mechanism.</p>
<dt><code>-x, -no-lldbinit</code></p>
<dd> Do not automatically parse any &#8216;.lldbinit&#8217; files. </p>
<p> (If you don&#8217;t provide -f then the first argument will be the file to be debugged so &#8216;lldb &#8212; &lt;filename&gt; [&lt;ARG1&gt; [&lt;ARG2&gt;]]&#8217; also works. Remember to end the options with &quot;&#8211;&quot; if any of your arguments have a &quot;-&quot; in them.)</dl>
<h2>USING LLDB</h2>
<p> In <code>lldb</code> there is a <code>help</code> command which can be used to find descriptions and examples of all <code>lldb</code> commands. To get help on &quot;<code>breakpoint set</code>&quot; you would type &quot;<code>help breakpoint set</code>&quot;. </p>
<p> There is also an <code>apropos</code> command which will search the help text of all commands for a given term &#8212; this is useful for locating a command by topic. For instance, &quot;<code>apropos breakpoint</code>&quot; will list any command that has the word <code>breakpoint</code> in its help text.</p>
<h2>FILES</h2>
<p> <code>lldb</code> will read settings/aliases/commands from three files at startup, if they exist. </p>
<p> First, it will read a <code>~/.lldbinit-</code><i>debugger</i> command file. If you are using the <code>lldb</code> command line interface, this is <code>~/.lldbinit-lldb</code>. If you are using <code>lldb</code> inside a GUI debugger like <code>Xcode</code> this will be <code>~/.lldbinit-Xcode</code>. This is a useful place to put settings that you want to apply only when a given <code>lldb</code> command interpreter is used. </p>
<p> Second, <code>~/.lldbinit</code> is read. </p>
<p> Third, an .lldbinit file in the current working directory (where <code>lldb</code> is started) will be read.</p>
<h2>SEE ALSO</h2>
<p> The LLDB project page <a rel="nofollow" href="http://lldb.llvm.org/">http://lldb.llvm.org/</a> has many different resources for <code>lldb</code> users &#8212; the gdb/lldb command equivalence page <a rel="nofollow" href="http://lldb.llvm.org/lldb-gdb.html">http://lldb.llvm.org/lldb-gdb.html</a> can be especially helpful for users coming from gdb.</p>
<h2>BUGS</h2>
<p> To report bugs, please visit <a rel="nofollow" href="http://llvm.org/bugs/">http://llvm.org/bugs/</a></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLDB Team, <a rel="nofollow" href="http://lldb.llvm.org/">http://lldb.llvm.org/</a> </p>
<h2>Index</h2>
