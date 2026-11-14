---
title: "lastcomm(1)"
name: "lastcomm"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lastcomm/"
description: "lastcomm – print out information about previously executed commands."
---

<h2>NAME</h2>
<p> lastcomm &#8211; print out information about previously executed commands.</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>lastcomm</code></p>
<dd> [ <i>command-name &#8230;</i> ]<br />
 [ <i>user-name &#8230;</i> ]<br />
 [ <i>terminal-name &#8230;</i> ]<br />
 [ OPTION &#8230; ]</dl>
<h2>DESCRIPTION</h2>
<p> <code>lastcomm</code> prints out information about previously executed commands. If no arguments are specified, <code>lastcomm </code> will print info about all of the commands in <i>acct</i> (the record file). If called with one or more of <i>command-name,</i> <i>user-name, </i> or <i>terminal-name,</i> only records containing those items will be displayed. For example, to find out which users used command `a.out&#8217; and which users were logged into `tty0&#8242;, type: <center> lastcomm a.out tty0<br />
 </center> </p>
<p> This will print any entry for which `a.out&#8217; or `tty0&#8242; matches in any of the record&#8217;s fields (command, name, or terminal). If you want to find only items that match *all* of the arguments on the command line, you must use the &#8216;-strict-match&#8217; option. For example, to list all of the executions of command <i>a.out</i> by user <i>root</i> on terminal <i>tty0,</i> type: <center> lastcomm &#8211;strict-match &#8211;command a.out &#8211;user root &#8211;tty tty0<br />
 </center> </p>
<p> The order of the arguments is not important. </p>
<p> For each entry the following information is printed:<br />
+&nbsp;<wbr>command name of the process<br />
+&nbsp;<wbr>flags, as recorded by the system accounting routines:<br />
&nbsp;<wbr>&nbsp;<wbr>S &#8212; command executed by super-user<br />
&nbsp;<wbr>&nbsp;<wbr>F &#8212; command executed after a fork but without a following exec<br />
&nbsp;<wbr>&nbsp;<wbr>C &#8212; command run in PDP-11 compatibility mode&nbsp;<wbr>(VAX only)<br />
&nbsp;<wbr>&nbsp;<wbr>D &#8212; command terminated with the generation of a core file<br />
&nbsp;<wbr>&nbsp;<wbr>X &#8212; command was terminated with the signal SIGTERM<br />
+&nbsp;<wbr>the name of the user who ran the process<br />
+&nbsp;<wbr>time the process started</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;strict-match</code></p>
<dd> Print only entries that match *all* of the arguments on the command line.</p>
<dt><code>&#8211;print-controls </code></p>
<dd> Print control characters.</p>
<dt><code>&#8211;user</code><i> name</i></p>
<dd> List records for user with <i>name.</i> This is useful if you&#8217;re trying to match a username that happens to be the same as a command (e.g., <i>ed</i> ).</p>
<dt><code>&#8211;command</code><i> name</i></p>
<dd> List records for command <i>name.</i></p>
<dt><code>&#8211;tty</code><i> name</i></p>
<dd> List records for tty <i>name.</i></p>
<dt><code>&#8211;forwards</code></p>
<dd> Read file forwards instead of backwards. This avoids trying to seek on the file and can be used to read from a pipe. This must be specified prior to any <code>-f</code> arguments.</p>
<dt><code>-f</code><i> filename, </i><code>&#8211;file</code><i> filename</i></p>
<dd> Read from the file <i>filename </i> instead of <i>acct.</i> A filename of &quot;-&quot; will result in reading from stdin. This must either be the first <code>-f</code> option, or <code>&#8211;forwards</code> must precede all <code>-f</code> options.</p>
<dt><code>&#8211;ahz</code><i> hz</i></p>
<dd> Use this flag to tell the program what <code>AHZ</code> should be (in hertz). This option is useful if you are trying to view an <i>acct</i> file created on another machine which has the same byte order and file format as your current machine, but has a different value for <code>AHZ.</code></p>
<dt><code>-p, &#8211;show-paging</code></p>
<dd> Print paging statistics.</p>
<dt><code>&#8211;pid</code></p>
<dd> Show PID and PPID of the process if acct version 3 format is supported by kernel.</p>
<dt><code>&#8211;debug</code></p>
<dd> Print verbose internal information.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the version number of <code>lastcomm.</code></p>
<dt><code>-h, &#8211;help</code></p>
<dd> Prints the usage string and default locations of system files to standard output and exits. </p>
</dl>
<h2>FILES</h2>
<p> <i>acct</i></p>
<dl>
<dt>
<dd> The system wide process accounting file. See <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5) (or <code><a href="/docs/linux/man/5-pacct/">pacct</a></code>(5)) for further details. <i>/var/log/account</i></p>
<dl>
<dt>
<dd> This directory contains pacct files which contain the binary process accounting data as written by the kernel.</dl>
</dl>
<h2>AUTHOR</h2>
<p> The GNU accounting utilities were written by Noel Cragg &lt;noel [at] gnu.ai.mit.edu&gt;. The man page was adapted from the accounting texinfo page by Susan Kleinmann &lt;sgk [at] sgk.tiac.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-last/">last</a></code>(1), <code><a href="/docs/linux/man/5-acct/">acct</a></code>(5) </p>
<h2>Index</h2>
