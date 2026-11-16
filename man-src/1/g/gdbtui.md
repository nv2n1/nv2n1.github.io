---
title: "gdbtui(1)"
name: "gdbtui"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbtui/"
description: "gdb – The GNU Debugger"
---

<h2>NAME</h2>
<p> gdb &#8211; The GNU Debugger</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>gdb</code></dt>
<dd> [<code>-help</code>] [<code>-nx</code>] [<code>-q</code>] [<code>-batch</code>] [<code>-cd=</code><i>dir</i>] [<code>-f</code>] [<code>-b&nbsp;<wbr></code><i>bps</i>] [<code>-tty=</code><i>dev</i>] [<code>-s </code><i>symfile</i>] [<code>-e </code><i>prog</i>] [<code>-se </code><i>prog</i>] [<code>-c </code><i>core</i>] [<code>-x </code><i>cmds</i>] [<code>-d </code><i>dir</i>] [<i>prog</i>[<i>core</i>|<i>procID</i>]]</dd></dl>
<h2>DESCRIPTION</h2>
<p> The purpose of a debugger such as GDB is to allow you to see what is going on &#8220;inside&#8221; another program while it executes&#8212;or what another program was doing at the moment it crashed. </p>
<p> GDB can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act: </p>
<dl>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</dt>
<dd> Start your program, specifying anything that might affect its behavior. </dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</dt>
<dd> Make your program stop on specified conditions. </dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</dt>
<dd> Examine what has happened, when your program has stopped. </dd>
<dt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*</dt>
<dd> Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.</dd></dl>
<p> You can use GDB to debug programs written in C, C++, and Modula-2. Fortran support will be added when a GNU Fortran compiler is ready. </p>
<p> GDB is invoked with the shell command <code>gdb</code>. Once started, it reads commands from the terminal until you tell it to exit with the GDB command <code>quit</code>. You can get online help from <code>gdb</code> itself by using the command <code>help</code>. </p>
<p> You can run <code>gdb</code> with no arguments or options; but the most usual way to start GDB is with one argument or two, specifying an executable program as the argument: </p>
<p> gdb program </p>
<p> You can also start with both an executable program and a core file specified: </p>
<p> gdb program core </p>
<p> You can, instead, specify a process ID as a second argument, if you want to debug a running process: </p>
<p> gdb program 1234 </p>
<p> would attach GDB to process <code>1234</code> (unless you also have a file named `<code>1234</code>&#8216;; GDB does check for a core file first). </p>
<p> Here are some of the most frequently needed GDB commands:</p>
<dl>
<dt><code>break </code>[<i>file</i><code>:</code>]<i>function</i></dt>
<dd> Set a breakpoint at <i>function</i> (in <i>file</i>).</dd>
<dt><code>run </code>[<i>arglist</i>]</dt>
<dd> Start your program (with <i>arglist</i>, if specified).</dd>
<dt><code>bt</code></dt>
<dd> Backtrace: display the program stack.</dd>
<dt><code>print</code><i> expr</i></dt>
<dd> Display the value of an expression.</dd>
<dt><code>c</code></dt>
<dd> Continue running your program (after stopping, e.g. at a breakpoint).</dd>
<dt><code>next</code></dt>
<dd> Execute next program line (after stopping); step <i>over</i> any function calls in the line.</dd>
<dt><code>edit </code>[<i>file</i><code>:</code>]<i>function</i></dt>
<dd> look at the program line where it is presently stopped.</dd>
<dt><code>list </code>[<i>file</i><code>:</code>]<i>function</i></dt>
<dd> type the text of the program in the vicinity of where it is presently stopped.</dd>
<dt><code>step</code></dt>
<dd> Execute next program line (after stopping); step <i>into</i> any function calls in the line.</dd>
<dt><code>help </code>[<i>name</i>]</dt>
<dd> Show information about GDB command <i>name</i>, or general information about using GDB.</dd>
<dt><code>quit</code></dt>
<dd> Exit from GDB.</dd></dl>
<p> For full details on GDB, see <i>Using GDB: A Guide to the GNU Source-Level Debugger</i>, by Richard M. Stallman and Roland H. Pesch. The same text is available online as the <code>gdb</code> entry in the <code>info</code> program.</p>
<h2>OPTIONS</h2>
<p> Any arguments other than options specify an executable file and core file (or process ID); that is, the first argument encountered with no associated option flag is equivalent to a `<code>-se</code>&#8216; option, and the second, if any, is equivalent to a `<code>-c</code>&#8216; option if it&#8217;s the name of a file. Many options have both long and short forms; both are shown here. The long forms are also recognized if you truncate them, so long as enough of the option is present to be unambiguous. (If you prefer, you can flag option arguments with `<code>+</code>&#8216; rather than `<code>&#8211;</code>&#8216;, though we illustrate the more usual convention.) </p>
<p> All the options and command line arguments you give are processed in sequential order. The order makes a difference when the `<code>-x</code>&#8216; option is used. </p>
<dl>
<dt><code>-help</code></dt>
<dd>
</dd><dt><code>-h</code></dt>
<dd> List all options, with brief explanations. </dd>
<dt><code>-symbols=</code><i>file</i></dt>
<dd>
</dd><dt><code>-s </code><i>file</i></dt>
<dd> Read symbol table from file <i>file</i>. </dd>
<dt><code>-write</code></dt>
<dd> Enable writing into executable and core files. </dd>
<dt><code>-exec=</code><i>file</i></dt>
<dd>
</dd><dt><code>-e </code><i>file</i></dt>
<dd> Use file <i>file</i> as the executable file to execute when appropriate, and for examining pure data in conjunction with a core dump. </dd>
<dt><code>-se=</code><i>file</i></dt>
<dd> Read symbol table from file <i>file</i> and use it as the executable file. </dd>
<dt><code>-core=</code><i>file</i></dt>
<dd>
</dd><dt><code>-c </code><i>file</i></dt>
<dd> Use file <i>file</i> as a core dump to examine. </dd>
<dt><code>-command=</code><i>file</i></dt>
<dd>
</dd><dt><code>-x </code><i>file</i></dt>
<dd> Execute GDB commands from file <i>file</i>. </dd>
<dt><code>-directory=</code><i>directory</i></dt>
<dd>
</dd><dt><code>-d </code><i>directory</i></dt>
<dd> Add <i>directory</i> to the path to search for source files.</dd></dl>
<dl>
<dt><code>-nx</code></dt>
<dd>
</dd><dt><code>-n</code></dt>
<dd> Do not execute commands from any `<code>.gdbinit</code>&#8216; initialization files. Normally, the commands in these files are executed after all the command options and arguments have been processed. </dd>
<dt><code>-quiet</code></dt>
<dd>
</dd><dt><code>-q</code></dt>
<dd> &#8220;Quiet&#8221;. Do not print the introductory and copyright messages. These messages are also suppressed in batch mode. </dd>
<dt><code>-batch</code></dt>
<dd> Run in batch mode. Exit with status <code>0</code> after processing all the command files specified with `<code>-x</code>&#8216; (and `<code>.gdbinit</code>&#8216;, if not inhibited). Exit with nonzero status if an error occurs in executing the GDB commands in the command files. </dd>
<p> Batch mode may be useful for running GDB as a filter, for example to download and run a program on another computer; in order to make this more useful, the message </p>
<p> Program exited normally. </p>
<p> (which is ordinarily issued whenever a program running under GDB control terminates) is not issued when running in batch mode. </p>
<dt><code>-cd=</code><i>directory</i></dt>
<dd> Run GDB using <i>directory</i> as its working directory, instead of the current directory. </dd>
<dt><code>-fullname</code></dt>
<dd>
</dd><dt><code>-f</code></dt>
<dd> Emacs sets this option when it runs GDB as a subprocess. It tells GDB to output the full file name and line number in a standard, recognizable fashion each time a stack frame is displayed (which includes each time the program stops). This recognizable format looks like two `<code>&nbsp;<wbr>32</code>&#8216; characters, followed by the file name, line number and character position separated by colons, and a newline. The Emacs-to-GDB interface program uses the two `<code>&nbsp;<wbr>32</code>&#8216; characters as a signal to display the source code for the frame. </dd>
<dt><code>-b </code><i>bps</i></dt>
<dd> Set the line speed (baud rate or bits per second) of any serial interface used by GDB for remote debugging. </dd>
<dt><code>-tty=</code><i>device</i></dt>
<dd> Run using <i>device</i> for your program&#8217;s standard input and output.</dd></dl>
<h2>SEE ALSO</h2>
<p> `<code>gdb</code>&#8216; entry in <code>info</code>; <i>Using GDB: A Guide to the GNU Source-Level Debugger</i>, Richard M. Stallman and Roland H. Pesch, July 1991.</p>
<h2>COPYING</h2>
<p> Copyright (c) 1991 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English. </p>
<h2>Index</h2>
