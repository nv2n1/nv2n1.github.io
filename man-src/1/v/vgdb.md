---
title: "vgdb(1)"
name: "vgdb"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vgdb/"
description: "vgdb – intermediary between Valgrind and GDB or a shell"
---

<h2 class="name">NAME</h2>
<p> vgdb &#8211; intermediary between Valgrind and GDB or a shell </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>vgdb</code> [<i>options</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>vgdb</code> (&quot;Valgrind to GDB&quot;) is used as an intermediary between Valgrind and GDB or a shell. It has two usage modes: </p>
<dl>
<dt>
<dd> 1.</p>
<dd>As a standalone utility, it is used from a shell command line to send monitor commands to a process running under Valgrind. For this usage, the vgdb OPTION(s) must be followed by the monitor command to send. To send more than one command, separate them with the <code>-c</code> option.</dl>
<dl>
<dt>
<dd> 2. In combination with GDB &quot;target remote |&quot; command, it is used as the relay application between GDB and the Valgrind gdbserver. For this usage, only OPTION(s) can be given, but no COMMAND can be given.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;pid=&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Specifies the PID of the process to which vgdb must connect to. This option is useful in case more than one Valgrind gdbserver can be connected to. If the <code>&#8211;pid</code> argument is not given and multiple Valgrind gdbserver processes are running, vgdb will report the list of such processes and then exit.</dl>
<p> <code>&#8211;vgdb-prefix</code></p>
<dl>
<dt>
<dd> Must be given to both Valgrind and vgdb if you want to change the default prefix for the FIFOs (named pipes) used for communication between the Valgrind gdbserver and vgdb.</dl>
<p> <code>&#8211;wait=&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Instructs vgdb to search for available Valgrind gdbservers for the specified number of seconds. This makes it possible start a vgdb process before starting the Valgrind gdbserver with which you intend the vgdb to communicate. This option is useful when used in conjunction with a <code>&#8211;vgdb-prefix</code> that is unique to the process you want to wait for. Also, if you use the <code>&#8211;wait</code> argument in the GDB &quot;target remote&quot; command, you must set the GDB remotetimeout to a value bigger than the &#8211;wait argument value. See option <code>&#8211;max-invoke-ms</code> (just below) for an example of setting the remotetimeout value.</dl>
<p> <code>&#8211;max-invoke-ms=&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Gives the number of milliseconds after which vgdb will force the invocation of gdbserver embedded in Valgrind. The default value is 100 milliseconds. A value of 0 disables forced invocation. The forced invocation is used when vgdb is connected to a Valgrind gdbserver, and the Valgrind process has all its threads blocked in a system call. </p>
<p> If you specify a large value, you might need to increase the GDB &quot;remotetimeout&quot; value from its default value of 2 seconds. You should ensure that the timeout (in seconds) is bigger than the <code>&#8211;max-invoke-ms</code> value. For example, for <code>&#8211;max-invoke-ms=5000</code>, the following GDB command is suitable: </p>
<dl>
<dt>
<dd>
<pre>
    (gdb) set remotetimeout 6
    
</pre>
</dl>
</dl>
<p> <code>&#8211;cmd-time-out=&lt;number&gt;</code></p>
<dl>
<dt>
<dd> Instructs a standalone vgdb to exit if the Valgrind gdbserver it is connected to does not process a command in the specified number of seconds. The default value is to never time out.</dl>
<p> <code>&#8211;port=&lt;portnr&gt;</code></p>
<dl>
<dt>
<dd> Instructs vgdb to use tcp/ip and listen for GDB on the specified port nr rather than to use a pipe to communicate with GDB. Using tcp/ip allows to have GDB running on one computer and debugging a Valgrind process running on another target computer. Example: </p>
<dl>
<dt>
<dd>
<pre>
# On the target computer, start your program under valgrind using
valgrind --vgdb-error=0 prog
# and then in another shell, run:
vgdb --port=1234
</pre>
</dl>
<p> On the computer which hosts GDB, execute the command: </p>
<dl>
<dt>
<dd>
<pre>
gdb prog
(gdb) target remote targetip:1234
</pre>
</dl>
<p> where targetip is the ip address or hostname of the target computer.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> To give more than one command to a standalone vgdb, separate the commands by an option <code>-c</code>. Example: </p>
<dl>
<dt>
<dd>
<pre>
vgdb v.set log_output -c leak_check any
</pre>
</dl>
</dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Instructs a standalone vgdb to report the list of the Valgrind gdbserver processes running and then exit.</dl>
<p> <code>-D</code></p>
<dl>
<dt>
<dd> Instructs a standalone vgdb to show the state of the shared memory used by the Valgrind gdbserver. vgdb will exit after having shown the Valgrind gdbserver shared memory state.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Instructs vgdb to produce debugging output. Give multiple <code>-d</code> args to increase the verbosity. When giving <code>-d</code> to a relay vgdb, you better redirect the standard error (stderr) of vgdb to a file to avoid interaction between GDB and vgdb debugging output.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html,">http://www.valgrind.org/docs/manual/index.html,</a> m[blue]<code>Debugging your program using Valgrind&#8217;s gdbserver and GDB</code>m[]<font SIZE="-2">[1]</font> m[blue]<code>vgdb</code>m[]<font SIZE="-2">[2]</font>, m[blue]<code>Valgrind monitor commands</code>m[]<font SIZE="-2">[3]</font>.</p>
<h2>AUTHOR</h2>
<p> Philippe Waroquiers.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Debugging your program using Valgrind&#8217;s gdbserver and GDB</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver</a></dl>
<dt> 2.</p>
<dd> vgdb</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.vgdb">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.vgdb</a></dl>
<dt> 3.</p>
<dd> Valgrind monitor commands</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.valgrind-monitor-commands">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.valgrind-monitor-commands</a></dl>
</dl>
<h2>Index</h2>
