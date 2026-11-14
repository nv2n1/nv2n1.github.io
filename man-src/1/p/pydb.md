---
title: "pydb(1)"
name: "pydb"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pydb/"
description: "pydb — enhanced Python debugger"
---

<h2 class="name">NAME</h2>
<p> pydb &#8212; enhanced Python debugger </p>
<h2>SYNOPSIS</h2>
<p> <code>pydb </code> [debugger-options] python-script [script-options&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pydb</code> command. </p>
<p> <code>pydb</code> is an extended Python debugger. It extends the Python standard debugger pdb and is suited for use with the graphical debugger DDD. The purpose of a debugger such as this one is to allow you to see what is going on &#8220;inside&#8221; another program while it executes&#8212;or what another program was doing at the moment it crashed. </p>
<p> We follow gdb&#8217;s command set unless there&#8217;s good reason not to. </p>
<p> pydb can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act: </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Start or restart your Python script, specifying arguments that might affect its behavior.</p>
<dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Make your program stop at various points possibly determined by</p>
<dd> specified conditions. </p>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Examine what has happened when your program has stopped.</p>
<dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.</p>
<dd></dl>
<p> Here are some of the most frequently-needed commands: </p>
<dl>
<dt><code>break </code>[<i>file</i><code>:</code><i>line</i>|<i>function</i>]</p>
<dd> Set a breakpoint at <i>function</i> or at the specified file and line.</dl>
<dl>
<dt><code>clear </code>[<i>file</i><code>:</code><i>line</i>|<i>function</i>]</p>
<dd> Clear a breakpoint at <i>function</i> or at the specified file and line. If line number is specified, all breakpoints in that line are cleared. If a function is specified, breakpoints at beginning of function are cleared. With no argument, clears all breakpoints in the line that the selected frame is executing in. See also the <code>delete</code> command which clears breakpoints by number.</dl>
<dl>
<dt><code>continue </code>[<i>line</i>]</p>
<dd> Continue running your program until the next breakpoint or until the end of the program. If a line number is given set a one-time breakpoint at that line.</dl>
<dl>
<dt><code>delete </code>[<i>breakpoint-numbers</i>]</p>
<dd> Delete breakpoints by number. To delete all breakpoints, give no breakpoint number. See also the <code>clear</code> command which clears breakpoints by line/file number.</dl>
<dl>
<dt><code>disassemble </code>[<i>location</i>]</p>
<dd> Disassemble Python instructions at the point you are currently stopped at. If location is a line number, do not show instructions before line. Location can also be a class, method, function, code or string argument.</dl>
<dl>
<dt><code>examine</code><i> expr</i></p>
<dd> Give type/object and value information about expression.</p>
<dt></dl>
<dd> <code>finish</code> Run until the completion of the current function or method. </p>
<dl>
<dt><code>frame</code><i> frame-number</i></p>
<dd> Set the stack frame to <i>frame-number</i> for purposes of examinine local variables. For positioning relative to the current frame, use <code>up</code> or <code>down.</code></dl>
<dl>
<dt><code>help </code>[<i>name</i>]</p>
<dd> Show information about pydb command <i>name</i>, or general information about using pydb.</dl>
<dl>
<dt><code>info </code>[<i>name</i>]</p>
<dd> Get the various information usually about the debugged program.</dl>
<dl>
<dt><code>list </code>[<i>file</i><code>:</code><i>line</i>|<i>function]</i></p>
<dd> type the text of the program in the vicinity of where it is presently stopped or at the specified function or file and line.</dl>
<dl>
<dt><code>next </code>[<i>count</i>]</p>
<dd> Execute next program line(s) (after stopping); step <i>over</i> any function calls in the line.</dl>
<dl>
<dt><code>pp</code><i> expr</i></p>
<dd> Pretty print the value of an expression.</dl>
<dl>
<dt><code>print</code><i> expr</i></p>
<dd> Display the value of an expression.</dl>
<dl>
<dt><code>source</code><i> filename</i></p>
<dd> Read and execute the lines in file <i>filename</i> as a series of debugger commands. An error in any command terminates execution of the command file and control is returned to the console.</dl>
<dl>
<dt><code>quit</code></p>
<dd> Exit from the debugger.</dl>
<dl>
<dt><code>run </code>[<i>arglist</i>]</p>
<dd> (Re)start your program (with <i>arglist</i>, if specified). If you want the debugger to get reloaded, use <code>restart</code> instead.</dl>
<dl>
<dt><code>set</code></p>
<dd> Modify parts of the debugger environment.</dl>
<dl>
<dt><code>shell </code><i>command</i></p>
<dd> Run a shell command.</dl>
<dl>
<dt><code>show</code></p>
<dd> See the debugger environment settings</dl>
<dl>
<dt><code>step </code>[<i>count</i>]</p>
<dd> Execute next program line(s) (after stopping); step <i>into</i> any function calls in the line.</dl>
<dl>
<dt><code>where </code>[<i>count</i>]</p>
<dd> Display all or <i>count</i> items of the program stack.</dl>
<p> For full details on pydb, see <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/pydb/index.html">http://bashdb.sourceforge.net/pydb/pydb/index.html</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show the version number and exit</p>
<dt><code>-h | &#8211;help</code></p>
<dd> show invocation help and exit</p>
<dt><code>-X | &#8211;trace</code></p>
<dd> Show lines before executing them. This option also sets <code>&#8211;batch.</code></p>
<dt><code>-X | &#8211;fntrace</code></p>
<dd> Show functions before executing them. This option also sets <code>&#8211;batch</code></p>
<dt><code>&#8211;batch</code></p>
<dd> Don&#8217;t run interactive commands on debugger entry</p>
<dt><code>&#8211;basename</code></p>
<dd> Report file locations as only the base filename, and omit the directory name. This is useful in running regression tests.</p>
<dt><code>-x | &#8211;command=FILE</code></p>
<dd> Execute commands from FILE.</p>
<dt><code>&#8211;cd=DIR</code></p>
<dd> Change current directory to DIR.</p>
<dt><code>&#8211;error=FILE</code></p>
<dd> Write debugger&#8217;s error output (stderr) to FILE</p>
<dt>
<dt><code>-e | &#8211;exec</code></p>
<dd>
<dd> Run debugger commands command-list. Commands should be separated by &quot;;;&quot;-the same as you would do inside the debugger. You may need to quote this option to prevent command shell interpretation, e.g. <code>&#8211;exec</code> &quot;break 20;; continue&quot;</p>
<dt><code>-n | &#8211;nx</code></p>
<dd> Don&#8217;t execute commands found in any initialization files</p>
<dt><code>-o FILE | &#8211;output=FILE</code></p>
<dd> Write debugger&#8217;s output (stdout) to FILE</p>
<dt><code>&#8211;sigcheck</code></p>
<dd> Set to watch for signal handler changes.</p>
<dt><code>-T, &#8211;threading</code></p>
<dd> Start off with threading debug support.</p>
<dt><code>-A LEVEL | &#8211;annotate=LEVEL</code></p>
<dd> Set gdb-like annotation_level. The annotation level is used by front-ends to get posted about program information when things change without having to poll for the information.</dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/">http://bashdb.sourceforge.net/pydb/</a> </p>
<p> <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/lib/index.html">http://bashdb.sourceforge.net/pydb/lib/index.html</a></p>
<h2>AUTHOR</h2>
<p> pydb was written by Richard Wolff &lt;rwolff [at] noao.edu&gt; (now retired) based on the standard Python debugger pdb.py. Over the many years, pdb.py and pydb.py have diverged. It was subsequently revised and expanded to be more like gdb by Rocky Bernstein &lt;rocky [at] gnu.org&gt; </p>
<p> The first version of this manual page was written by Gregor Hoffleit &lt;flight [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
