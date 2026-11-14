---
title: "gdbserver(1)"
name: "gdbserver"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdbserver/"
description: "gdbserver – Remote Server for the GNU Debugger"
---

<h2 class="name">NAME</h2>
<p> gdbserver &#8211; Remote Server for the GNU Debugger </p>
<h2>SYNOPSIS</h2>
<p> gdbserver <i>comm</i> <i>prog</i> [<i>args</i>&#8230;] </p>
<p> gdbserver &#8211;attach <i>comm</i> <i>pid</i> </p>
<p> gdbserver &#8211;multi <i>comm</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gdbserver</code> is a program that allows you to run <font SIZE="-1">GDB</font> on a different machine than the one which is running the program being debugged. </p>
<p> Usage (server (target) side): </p>
<p> First, you need to have a copy of the program you want to debug put onto the target system. The program can be stripped to save space if needed, as <code>gdbserver</code> doesn&#8217;t care about symbols. All symbol handling is taken care of by the <font SIZE="-1">GDB</font> running on the host system. </p>
<p> To use the server, you log on to the target system, and run the <code>gdbserver</code> program. You must tell it (a) how to communicate with <font SIZE="-1">GDB,</font> (b) the name of your program, and (c) its arguments. The general syntax is: </p>
<pre>
        target&gt; gdbserver &lt;comm&gt; &lt;program&gt; [&lt;args&gt; ...]
</pre>
<p> For example, using a serial port, you might say: </p>
<pre>
        target&gt; gdbserver /dev/com1 emacs foo.txt
</pre>
<p> This tells <code>gdbserver</code> to debug emacs with an argument of foo.txt, and to communicate with <font SIZE="-1">GDB</font> via <i>/dev/com1</i>. <code>gdbserver</code> now waits patiently for the host <font SIZE="-1">GDB</font> to communicate with it. </p>
<p> To use a <font SIZE="-1">TCP</font> connection, you could say: </p>
<pre>
        target&gt; gdbserver host:2345 emacs foo.txt
</pre>
<p> This says pretty much the same thing as the last example, except that we are going to communicate with the <tt>&quot;host&quot;</tt> <font SIZE="-1">GDB</font> via <font SIZE="-1">TCP.</font> The <tt>&quot;host:2345&quot;</tt> argument means that we are expecting to see a <font SIZE="-1">TCP</font> connection from <tt>&quot;host&quot;</tt> to local <font SIZE="-1">TCP</font> port 2345. (Currently, the <tt>&quot;host&quot;</tt> part is ignored.) You can choose any number you want for the port number as long as it does not conflict with any existing <font SIZE="-1">TCP</font> ports on the target system. This same port number must be used in the host GDBs <tt>&quot;target remote&quot;</tt> command, which will be described shortly. Note that if you chose a port number that conflicts with another service, <code>gdbserver</code> will print an error message and exit. </p>
<p> <code>gdbserver</code> can also attach to running programs. This is accomplished via the <code>&#8211;attach</code> argument. The syntax is: </p>
<pre>
        target&gt; gdbserver --attach &lt;comm&gt; &lt;pid&gt;
</pre>
<p> <i>pid</i> is the process <font SIZE="-1">ID</font> of a currently running process. It isn&#8217;t necessary to point <code>gdbserver</code> at a binary for the running process. </p>
<p> To start <tt>&quot;gdbserver&quot;</tt> without supplying an initial command to run or process <font SIZE="-1">ID</font> to attach, use the <code>&#8211;multi</code> command line option. In such case you should connect using <tt>&quot;target extended-remote&quot;</tt> to start the program you want to debug. </p>
<pre>
        target&gt; gdbserver --multi &lt;comm&gt;
</pre>
<p> Usage (host side): </p>
<p> You need an unstripped copy of the target program on your host system, since <font SIZE="-1">GDB</font> needs to examine its symbol tables and such. Start up <font SIZE="-1">GDB</font> as you normally would, with the target program as the first argument. (You may need to use the <code>&#8211;baud</code> option if the serial line is running at anything except 9600 baud.) That is <tt>&quot;gdb TARGET-PROG&quot;</tt>, or <tt>&quot;gdb --baud BAUD TARGET-PROG&quot;</tt>. After that, the only new command you need to know about is <tt>&quot;target remote&quot;</tt> (or <tt>&quot;target extended-remote&quot;</tt>). Its argument is either a device name (usually a serial device, like <i>/dev/ttyb</i>), or a <tt>&quot;HOST:PORT&quot;</tt> descriptor. For example: </p>
<pre>
        (gdb) target remote /dev/ttyb
</pre>
<p> communicates with the server via serial line <i>/dev/ttyb</i>, and: </p>
<pre>
        (gdb) target remote the-target:2345
</pre>
<p> communicates via a <font SIZE="-1">TCP</font> connection to port 2345 on host `the-target&#8217;, where you previously started up <code>gdbserver</code> with the same port number. Note that for <font SIZE="-1">TCP</font> connections, you must start up <code>gdbserver</code> prior to using the `target remote&#8217; command, otherwise you may get an error that looks something like `Connection refused&#8217;. </p>
<p> <code>gdbserver</code> can also debug multiple inferiors at once, described in the <font SIZE="-1">GDB</font> manual in node <tt>&quot;Inferiors and Programs&quot;</tt> &#8212; shell command <tt>&quot;info -f gdb -n 'Inferiors and Programs'&quot;</tt>. In such case use the <tt>&quot;extended-remote&quot;</tt> <font SIZE="-1">GDB</font> command variant: </p>
<pre>
        (gdb) target extended-remote the-target:2345
</pre>
<p> The <code>gdbserver</code> option <code>&#8211;multi</code> may or may not be used in such case.</p>
<h2>OPTIONS</h2>
<p> There are three different modes for invoking <code>gdbserver</code>:</p>
<dl>
<dt>&bull;</p>
<dd> Debug a specific program specified by its program name: </p>
<pre>
        gdbserver &lt;comm&gt; &lt;prog&gt; [&lt;args&gt;...]
</pre>
<p> The <i>comm</i> parameter specifies how should the server communicate with <font SIZE="-1">GDB</font>; it is either a device name (to use a serial line), a <font SIZE="-1">TCP</font> port number (<tt>&quot;:1234&quot;</tt>), or <tt>&quot;-&quot;</tt> or <tt>&quot;stdio&quot;</tt> to use stdin/stdout of <tt>&quot;gdbserver&quot;</tt>. Specify the name of the program to debug in <i>prog</i>. Any remaining arguments will be passed to the program verbatim. When the program exits, <font SIZE="-1">GDB</font> will close the connection, and <tt>&quot;gdbserver&quot;</tt> will exit.</p>
<dt>&bull;</p>
<dd> Debug a specific program by specifying the process <font SIZE="-1">ID</font> of a running program: </p>
<pre>
        gdbserver --attach &lt;comm&gt; &lt;pid&gt;
</pre>
<p> The <i>comm</i> parameter is as described above. Supply the process <font SIZE="-1">ID</font> of a running program in <i>pid</i>; <font SIZE="-1">GDB</font> will do everything else. Like with the previous mode, when the process <i>pid</i> exits, <font SIZE="-1">GDB</font> will close the connection, and <tt>&quot;gdbserver&quot;</tt> will exit.</p>
<dt>&bull;</p>
<dd> Multi-process mode &#8212; debug more than one program/process: </p>
<pre>
        gdbserver --multi &lt;comm&gt;
</pre>
<p> In this mode, <font SIZE="-1">GDB</font> can instruct <code>gdbserver</code> which command(s) to run. Unlike the other 2 modes, <font SIZE="-1">GDB</font> will not close the connection when a process being debugged exits, so you can debug several processes in the same session.</dl>
<p> In each of the modes you may specify these options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> List all options, with brief explanations.</p>
<dt><code>&#8211;version</code></p>
<dd> This option causes <code>gdbserver</code> to print its version number and exit.</p>
<dt><code>&#8211;attach</code></p>
<dd> <code>gdbserver</code> will attach to a running program. The syntax is: </p>
<pre>
        target&gt; gdbserver --attach &lt;comm&gt; &lt;pid&gt;
</pre>
<p> <i>pid</i> is the process <font SIZE="-1">ID</font> of a currently running process. It isn&#8217;t necessary to point <code>gdbserver</code> at a binary for the running process.</p>
<dt><code>&#8211;multi</code></p>
<dd> To start <tt>&quot;gdbserver&quot;</tt> without supplying an initial command to run or process <font SIZE="-1">ID</font> to attach, use this command line option. Then you can connect using <tt>&quot;target extended-remote&quot;</tt> and start the program you want to debug. The syntax is: </p>
<pre>
        target&gt; gdbserver --multi &lt;comm&gt;
</pre>
<dt><code>&#8211;debug</code></p>
<dd> Instruct <tt>&quot;gdbserver&quot;</tt> to display extra status information about the debugging process. This option is intended for <tt>&quot;gdbserver&quot;</tt> development and for bug reports to the developers.</p>
<dt><code>&#8211;remote-debug</code></p>
<dd> Instruct <tt>&quot;gdbserver&quot;</tt> to display remote protocol debug output. This option is intended for <tt>&quot;gdbserver&quot;</tt> development and for bug reports to the developers.</p>
<dt><code>&#8211;debug-file=</code><i>filename</i></p>
<dd> Instruct <tt>&quot;gdbserver&quot;</tt> to send any debug output to the given <i>filename</i>. This option is intended for <tt>&quot;gdbserver&quot;</tt> development and for bug reports to the developers.</p>
<dt><code>&#8211;debug-format=option1</code>[<code>,option2,&#8230;</code>]</p>
<dd> Instruct <tt>&quot;gdbserver&quot;</tt> to include extra information in each line of debugging output.</p>
<dt><code>&#8211;wrapper</code></p>
<dd> Specify a wrapper to launch programs for debugging. The option should be followed by the name of the wrapper, then any command-line arguments to pass to the wrapper, then <tt>&quot;--&quot;</tt> indicating the end of the wrapper arguments.</p>
<dt><code>&#8211;once</code></p>
<dd> By default, <code>gdbserver</code> keeps the listening <font SIZE="-1">TCP</font> port open, so that additional connections are possible. However, if you start <tt>&quot;gdbserver&quot;</tt> with the <code>&#8211;once</code> option, it will stop listening for any further connection attempts after connecting to the first <font SIZE="-1">GDB</font> session.</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <font SIZE="-1">GDB</font> is maintained as a Texinfo manual. If the <tt>&quot;info&quot;</tt> and <tt>&quot;gdb&quot;</tt> programs and <font SIZE="-1">GDB</font>&#8216;s Texinfo documentation are properly installed at your site, the command </p>
<pre>
        info gdb
</pre>
<p> should give you access to the complete manual. </p>
<p> <i>Using </i><font SIZE="-1"><i>GDB: A</i></font><i> Guide to the </i><font SIZE="-1"><i>GNU</i></font><i> Source-Level Debugger</i>, Richard M. Stallman and Roland H. Pesch, July 1991.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1988-2020 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;Free Software&#8221; and &#8220;Free Software Needs Free Documentation&#8221;, with the Front-Cover Texts being &#8220;A <font SIZE="-1">GNU</font> Manual,&#8221; and with the Back-Cover Texts as in (a) below. </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: &#8220;You are free to copy and modify this <font SIZE="-1">GNU</font> Manual. Buying copies from <font SIZE="-1">GNU</font> Press supports the <font SIZE="-1">FSF</font> in developing <font SIZE="-1">GNU</font> and promoting software freedom.&#8221; </p>
<h2>Index</h2>
