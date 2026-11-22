---

title: "gdb(1)"
name: "gdb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdb/"
description: "gdb – The GNU Debugger"
---

<p> gdb &#8211; The GNU Debugger </p>
<h2>SYNOPSIS</h2>
<p> gdb [OPTIONS] [<i>prog</i>|<i>prog</i> <i>procID</i>|<i>prog</i> <i>core</i>]</p>
<h2>DESCRIPTION</h2>
<p> The purpose of a debugger such as GDB is to allow you to see what is going on &#8220;inside&#8221; another program while it executes &#8212; or what another program was doing at the moment it crashed. </p>
<p> GDB can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act:</p>
<dl>
<dt>&bull;</dt>
<dd> Start your program, specifying anything that might affect its behavior.</dd>
<dt>&bull;</dt>
<dd> Make your program stop on specified conditions.</dd>
<dt>&bull;</dt>
<dd> Examine what has happened, when your program has stopped.</dd>
<dt>&bull;</dt>
<dd> Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.</dd></dl>
<p> You can use GDB to debug programs written in C, C++, Fortran and Modula-2. </p>
<p> GDB is invoked with the shell command <tt>&quot;gdb&quot;</tt>. Once started, it reads commands from the terminal until you tell it to exit with the GDB command <tt>&quot;quit&quot;</tt> or <tt>&quot;exit&quot;</tt>. You can get online help from GDB itself by using the command <tt>&quot;help&quot;</tt>. </p>
<p> You can run <tt>&quot;gdb&quot;</tt> with no arguments or options; but the most usual way to start GDB is with one argument or two, specifying an executable program as the argument: </p>
<pre>
        gdb program
</pre>
<p> You can also start with both an executable program and a core file specified: </p>
<pre>
        gdb program core
</pre>
<p> You can, instead, specify a process ID as a second argument or use option <tt>&quot;-p&quot;</tt>, if you want to debug a running process: </p>
<pre>
        gdb program 1234
        gdb -p 1234
</pre>
<p> would attach GDB to process <tt>1234</tt>. With option <code>-p</code> you can omit the <i>program</i> filename. </p>
<p> Here are some of the most frequently needed GDB commands:</p>
<dl>
<dt><code>break [</code><i>file</i><code>:][</code><i>function</i><code>|</code><i>line</i><code>]</code></dt>
<dd> Set a breakpoint at <i>function</i> or <i>line</i> (in <i>file</i>).</dd>
<dt><code>run [</code><i>arglist</i><code>]</code></dt>
<dd> Start your program (with <i>arglist</i>, if specified).</dd>
<dt><code>bt</code></dt>
<dd> Backtrace: display the program stack.</dd>
<dt><code>print</code> <i>expr</i></dt>
<dd> Display the value of an expression.</dd>
<dt><code>c</code></dt>
<dd> Continue running your program (after stopping, e.g. at a breakpoint).</dd>
<dt><code>next</code></dt>
<dd> Execute next program line (after stopping); step <i>over</i> any function calls in the line.</dd>
<dt><code>edit [</code><i>file</i><code>:]</code><i>function</i></dt>
<dd> look at the program line where it is presently stopped.</dd>
<dt><code>list [</code><i>file</i><code>:]</code><i>function</i></dt>
<dd> type the text of the program in the vicinity of where it is presently stopped.</dd>
<dt><code>step</code></dt>
<dd> Execute next program line (after stopping); step <i>into</i> any function calls in the line.</dd>
<dt><code>help [</code><i>name</i><code>]</code></dt>
<dd> Show information about GDB command <i>name</i>, or general information about using GDB.</dd>
<dt><code>quit</code></dt>
<dd>
</dd><dt><code>exit</code></dt>
<dd> Exit from GDB.</dd></dl>
<p> For full details on GDB, see <i>Using </i><i>GDB: A</i><i> Guide to the </i><i>GNU</i><i> Source-Level Debugger</i>, by Richard M. Stallman and Roland H. Pesch. The same text is available online as the <tt>&quot;gdb&quot;</tt> entry in the <tt>&quot;info&quot;</tt> program.</p>
<h2>OPTIONS</h2>
<p> Any arguments other than options specify an executable file and core file (or process ID); that is, the first argument encountered with no associated option flag is equivalent to a <code>&#8211;se</code> option, and the second, if any, is equivalent to a <code>-c</code> option if it&#8217;s the name of a file. Many options have both long and abbreviated forms; both are shown here. The long forms are also recognized if you truncate them, so long as enough of the option is present to be unambiguous. </p>
<p> The abbreviated forms are shown here with <code>&#8211;</code> and long forms are shown with <code>&#8212;</code> to reflect how they are shown in <code>&#8211;help</code>. However, GDB recognizes all of the following conventions for most options:</p>
<dl>
<dt>&quot;&#8211;option=<i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;&#8211;option <i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;-option=<i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;-option <i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;&#8211;o=<i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;&#8211;o <i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;-o=<i>value</i>&quot;</dt>
<dd>
</dd><dt>&quot;-o <i>value</i>&quot;</dt>
<dd></dd></dl>
<p> All the options and command line arguments you give are processed in sequential order. The order makes a difference when the <code>-x</code> option is used.</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd>
</dd><dt><code>-h</code></dt>
<dd> List all options, with brief explanations.</dd>
<dt><code>&#8211;symbols=</code><i>file</i></dt>
<dd>
</dd><dt><code>-s</code> <i>file</i></dt>
<dd> Read symbol table from <i>file</i>.</dd>
<dt><code>&#8211;write</code></dt>
<dd> Enable writing into executable and core files.</dd>
<dt><code>&#8211;exec=</code><i>file</i></dt>
<dd>
</dd><dt><code>-e</code> <i>file</i></dt>
<dd> Use <i>file</i> as the executable file to execute when appropriate, and for examining pure data in conjunction with a core dump.</dd>
<dt><code>&#8211;se=</code><i>file</i></dt>
<dd> Read symbol table from <i>file</i> and use it as the executable file.</dd>
<dt><code>&#8211;core=</code><i>file</i></dt>
<dd>
</dd><dt><code>-c</code> <i>file</i></dt>
<dd> Use <i>file</i> as a core dump to examine.</dd>
<dt><code>&#8211;command=</code><i>file</i></dt>
<dd>
</dd><dt><code>-x</code> <i>file</i></dt>
<dd> Execute GDB commands from <i>file</i>.</dd>
<dt><code>&#8211;eval-command=</code><i>command</i></dt>
<dd>
</dd><dt><code>-ex</code> <i>command</i></dt>
<dd> Execute given GDB <i>command</i>.</dd>
<dt><code>&#8211;init-eval-command=</code><i>command</i></dt>
<dd>
</dd><dt><code>-iex</code></dt>
<dd> Execute GDB <i>command</i> before loading the inferior.</dd>
<dt><code>&#8211;directory=</code><i>directory</i></dt>
<dd>
</dd><dt><code>-d</code> <i>directory</i></dt>
<dd> Add <i>directory</i> to the path to search for source files.</dd>
<dt><code>&#8211;nh</code></dt>
<dd> Do not execute commands from <i>~/.config/gdb/gdbinit</i>, <i>~/.gdbinit</i>, <i>~/.config/gdb/gdbearlyinit</i>, or <i>~/.gdbearlyinit</i></dd>
<dt><code>&#8211;nx</code></dt>
<dd>
</dd><dt><code>-n</code></dt>
<dd> Do not execute commands from any <i>.gdbinit</i> or <i>.gdbearlyinit</i> initialization files.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd>
</dd><dt><code>&#8211;silent</code></dt>
<dd>
</dd><dt><code>-q</code></dt>
<dd> &#8220;Quiet&#8221;. Do not print the introductory and copyright messages. These messages are also suppressed in batch mode.</dd>
<dt><code>&#8211;batch</code></dt>
<dd> Run in batch mode. Exit with status <tt>0</tt> after processing all the command files specified with <code>-x</code> (and <i>.gdbinit</i>, if not inhibited). Exit with nonzero status if an error occurs in executing the GDB commands in the command files. </dd>
<p> Batch mode may be useful for running GDB as a filter, for example to download and run a program on another computer; in order to make this more useful, the message </p>
<pre>
        Program exited normally.
</pre>
<p> (which is ordinarily issued whenever a program running under GDB control terminates) is not issued when running in batch mode.</p>
<dt><code>&#8211;batch-silent</code></dt>
<dd> Run in batch mode, just like <code>&#8211;batch</code>, but totally silent. All GDB output is supressed (stderr is unaffected). This is much quieter than <code>&#8211;silent</code> and would be useless for an interactive session. </dd>
<p> This is particularly useful when using targets that give <code>Loading section</code> messages, for example. </p>
<p> Note that targets that give their output via GDB, as opposed to writing directly to <tt>&quot;stdout&quot;</tt>, will also be made silent.</p>
<dt><code>&#8211;args</code> <i>prog</i> <code>[</code><i>arglist</i><code>]</code></dt>
<dd> Change interpretation of command line so that arguments following this option are passed as arguments to the inferior. As an example, take the following command: </dd>
<pre>
        gdb ./a.out -q
</pre>
<p> It would start GDB with <code>-q</code>, not printing the introductory message. On the other hand, using: </p>
<pre>
        gdb --args ./a.out -q
</pre>
<p> starts GDB with the introductory message, and passes the option to the inferior.</p>
<dt><code>&#8211;pid=</code><i>pid</i></dt>
<dd> Attach GDB to an already running program, with the PID <i>pid</i>.</dd>
<dt><code>&#8211;tui</code></dt>
<dd> Open the terminal user interface.</dd>
<dt><code>&#8211;readnow</code></dt>
<dd> Read all symbols from the given symfile on the first access.</dd>
<dt><code>&#8211;readnever</code></dt>
<dd> Do not read symbol files.</dd>
<dt><code>&#8211;dbx</code></dt>
<dd> Run in DBX compatibility mode.</dd>
<dt><code>&#8211;return-child-result</code></dt>
<dd> GDB&#8216;s exit code will be the same as the child&#8217;s exit code.</dd>
<dt><code>&#8211;configuration</code></dt>
<dd> Print details about GDB configuration and then exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and then exit.</dd>
<dt><code>&#8211;cd=</code><i>directory</i></dt>
<dd> Run GDB using <i>directory</i> as its working directory, instead of the current directory.</dd>
<dt><code>&#8211;data-directory=</code><i>directory</i></dt>
<dd>
</dd><dt><code>-D</code></dt>
<dd> Run GDB using <i>directory</i> as its data directory. The data directory is where GDB searches for its auxiliary files.</dd>
<dt><code>&#8211;fullname</code></dt>
<dd>
</dd><dt><code>-f</code></dt>
<dd> Emacs sets this option when it runs GDB as a subprocess. It tells GDB to output the full file name and line number in a standard, recognizable fashion each time a stack frame is displayed (which includes each time the program stops). This recognizable format looks like two <code></code> characters, followed by the file name, line number and character position separated by colons, and a newline. The Emacs-to-GDB interface program uses the two <code></code> characters as a signal to display the source code for the frame.</dd>
<dt><code>-b</code> <i>baudrate</i></dt>
<dd> Set the line speed (baud rate or bits per second) of any serial interface used by GDB for remote debugging.</dd>
<dt><code>-l</code> <i>timeout</i></dt>
<dd> Set timeout, in seconds, for remote debugging.</dd>
<dt><code>&#8211;tty=</code><i>device</i></dt>
<dd> Run using <i>device</i> for your program&#8217;s standard input and output.</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for GDB is maintained as a Texinfo manual. If the <tt>&quot;info&quot;</tt> and <tt>&quot;gdb&quot;</tt> programs and GDB&#8216;s Texinfo documentation are properly installed at your site, the command </p>
<pre>
        info gdb
</pre>
<p> should give you access to the complete manual. </p>
<p> <i>Using </i><i>GDB: A</i><i> Guide to the </i><i>GNU</i><i> Source-Level Debugger</i>, Richard M. Stallman and Roland H. Pesch, July 1991.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1988-2022 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;Free Software&#8221; and &#8220;Free Software Needs Free Documentation&#8221;, with the Front-Cover Texts being &#8220;A GNU Manual,&#8221; and with the Back-Cover Texts as in (a) below. </p>
<p> (a) The FSF&#8216;s Back-Cover Text is: &#8220;You are free to copy and modify this GNU Manual. Buying copies from GNU Press supports the FSF in developing GNU and promoting software freedom.&#8221; </p>
