---

title: "pydb(1)"
name: "pydb"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pydb/"
description: "pydb — enhanced Python debugger"
---

<p> pydb &#8212; enhanced Python debugger </p>
<h2>SYNOPSIS</h2>
<p> <code>pydb </code> [debugger-options] python-script [script-options&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pydb</code> command. </p>
<p> <code>pydb</code> is an extended Python debugger. It extends the Python standard debugger pdb and is suited for use with the graphical debugger DDD. The purpose of a debugger such as this one is to allow you to see what is going on &#8220;inside&#8221; another program while it executes&#8212;or what another program was doing at the moment it crashed. </p>
<p> We follow gdb&#8217;s command set unless there&#8217;s good reason not to. </p>
<p> pydb can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act: </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Start or restart your Python script, specifying arguments that might affect its behavior.</dt>
<dd>
</dd><dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Make your program stop at various points possibly determined by</dt>
<dd> specified conditions. </dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Examine what has happened when your program has stopped.</dt>
<dd>
</dd><dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>* Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.</dt>
<dd></dd></dl>
<p> Here are some of the most frequently-needed commands: </p>
<dl>
<dt><code>break </code>[<i>file</i><code>:</code><i>line</i>|<i>function</i>]</dt>
<dd> Set a breakpoint at <i>function</i> or at the specified file and line.</dd></dl>
<dl>
<dt><code>clear </code>[<i>file</i><code>:</code><i>line</i>|<i>function</i>]</dt>
<dd> Clear a breakpoint at <i>function</i> or at the specified file and line. If line number is specified, all breakpoints in that line are cleared. If a function is specified, breakpoints at beginning of function are cleared. With no argument, clears all breakpoints in the line that the selected frame is executing in. See also the <code>delete</code> command which clears breakpoints by number.</dd></dl>
<dl>
<dt><code>continue </code>[<i>line</i>]</dt>
<dd> Continue running your program until the next breakpoint or until the end of the program. If a line number is given set a one-time breakpoint at that line.</dd></dl>
<dl>
<dt><code>delete </code>[<i>breakpoint-numbers</i>]</dt>
<dd> Delete breakpoints by number. To delete all breakpoints, give no breakpoint number. See also the <code>clear</code> command which clears breakpoints by line/file number.</dd></dl>
<dl>
<dt><code>disassemble </code>[<i>location</i>]</dt>
<dd> Disassemble Python instructions at the point you are currently stopped at. If location is a line number, do not show instructions before line. Location can also be a class, method, function, code or string argument.</dd></dl>
<dl>
<dt><code>examine</code><i> expr</i></dt>
<dd> Give type/object and value information about expression.</dd>
<dt></dt></dl>
<dd> <code>finish</code> Run until the completion of the current function or method. </dd>
<dl>
<dt><code>frame</code><i> frame-number</i></dt>
<dd> Set the stack frame to <i>frame-number</i> for purposes of examinine local variables. For positioning relative to the current frame, use <code>up</code> or <code>down.</code></dd></dl>
<dl>
<dt><code>help </code>[<i>name</i>]</dt>
<dd> Show information about pydb command <i>name</i>, or general information about using pydb.</dd></dl>
<dl>
<dt><code>info </code>[<i>name</i>]</dt>
<dd> Get the various information usually about the debugged program.</dd></dl>
<dl>
<dt><code>list </code>[<i>file</i><code>:</code><i>line</i>|<i>function]</i></dt>
<dd> type the text of the program in the vicinity of where it is presently stopped or at the specified function or file and line.</dd></dl>
<dl>
<dt><code>next </code>[<i>count</i>]</dt>
<dd> Execute next program line(s) (after stopping); step <i>over</i> any function calls in the line.</dd></dl>
<dl>
<dt><code>pp</code><i> expr</i></dt>
<dd> Pretty print the value of an expression.</dd></dl>
<dl>
<dt><code>print</code><i> expr</i></dt>
<dd> Display the value of an expression.</dd></dl>
<dl>
<dt><code>source</code><i> filename</i></dt>
<dd> Read and execute the lines in file <i>filename</i> as a series of debugger commands. An error in any command terminates execution of the command file and control is returned to the console.</dd></dl>
<dl>
<dt><code>quit</code></dt>
<dd> Exit from the debugger.</dd></dl>
<dl>
<dt><code>run </code>[<i>arglist</i>]</dt>
<dd> (Re)start your program (with <i>arglist</i>, if specified). If you want the debugger to get reloaded, use <code>restart</code> instead.</dd></dl>
<dl>
<dt><code>set</code></dt>
<dd> Modify parts of the debugger environment.</dd></dl>
<dl>
<dt><code>shell </code><i>command</i></dt>
<dd> Run a shell command.</dd></dl>
<dl>
<dt><code>show</code></dt>
<dd> See the debugger environment settings</dd></dl>
<dl>
<dt><code>step </code>[<i>count</i>]</dt>
<dd> Execute next program line(s) (after stopping); step <i>into</i> any function calls in the line.</dd></dl>
<dl>
<dt><code>where </code>[<i>count</i>]</dt>
<dd> Display all or <i>count</i> items of the program stack.</dd></dl>
<p> For full details on pydb, see <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/pydb/index.html">http://bashdb.sourceforge.net/pydb/pydb/index.html</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show the version number and exit</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> show invocation help and exit</dd>
<dt><code>-X | &#8211;trace</code></dt>
<dd> Show lines before executing them. This option also sets <code>&#8211;batch.</code></dd>
<dt><code>-X | &#8211;fntrace</code></dt>
<dd> Show functions before executing them. This option also sets <code>&#8211;batch</code></dd>
<dt><code>&#8211;batch</code></dt>
<dd> Don&#8217;t run interactive commands on debugger entry</dd>
<dt><code>&#8211;basename</code></dt>
<dd> Report file locations as only the base filename, and omit the directory name. This is useful in running regression tests.</dd>
<dt><code>-x | &#8211;command=FILE</code></dt>
<dd> Execute commands from FILE.</dd>
<dt><code>&#8211;cd=DIR</code></dt>
<dd> Change current directory to DIR.</dd>
<dt><code>&#8211;error=FILE</code></dt>
<dd> Write debugger&#8217;s error output (stderr) to FILE</dd>
<dt>
</dt><dt><code>-e | &#8211;exec</code></dt>
<dd>
</dd><dd> Run debugger commands command-list. Commands should be separated by &quot;;;&quot;-the same as you would do inside the debugger. You may need to quote this option to prevent command shell interpretation, e.g. <code>&#8211;exec</code> &quot;break 20;; continue&quot;</dd>
<dt><code>-n | &#8211;nx</code></dt>
<dd> Don&#8217;t execute commands found in any initialization files</dd>
<dt><code>-o FILE | &#8211;output=FILE</code></dt>
<dd> Write debugger&#8217;s output (stdout) to FILE</dd>
<dt><code>&#8211;sigcheck</code></dt>
<dd> Set to watch for signal handler changes.</dd>
<dt><code>-T, &#8211;threading</code></dt>
<dd> Start off with threading debug support.</dd>
<dt><code>-A LEVEL | &#8211;annotate=LEVEL</code></dt>
<dd> Set gdb-like annotation_level. The annotation level is used by front-ends to get posted about program information when things change without having to poll for the information.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/">http://bashdb.sourceforge.net/pydb/</a> </p>
<p> <a rel="nofollow" href="http://bashdb.sourceforge.net/pydb/lib/index.html">http://bashdb.sourceforge.net/pydb/lib/index.html</a></p>
<h2>AUTHOR</h2>
<p> pydb was written by Richard Wolff &lt;rwolff [at] noao.edu&gt; (now retired) based on the standard Python debugger pdb.py. Over the many years, pdb.py and pydb.py have diverged. It was subsequently revised and expanded to be more like gdb by Rocky Bernstein &lt;rocky [at] gnu.org&gt; </p>
<p> The first version of this manual page was written by Gregor Hoffleit &lt;flight [at] debian.org&gt; for the Debian project (but may be used by others). </p>
