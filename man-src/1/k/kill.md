---
title: "kill(1)"
name: "kill"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kill/"
description: "kill – send a signal to a process"
---

<h2 class="name">NAME</h2>
<p> kill &#8211; send a signal to a process </p>
<h2>SYNOPSIS</h2>
<p> <code>kill</code> [options] &lt;pid&gt; [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The default signal for kill is TERM. Use <code>-l</code> or <code>-L</code> to list available signals. Particularly useful signals include HUP, INT, KILL, STOP, CONT, and 0. Alternate signals may be specified in three ways: <code>-9</code>, <code>-SIGKILL</code> or <code>-KILL</code>. Negative PID values may be used to choose whole process groups; see the PGID column in ps command output. A PID of <code>-1</code> is special; it indicates all processes except the kill process itself and init.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&lt;pid&gt; [&#8230;]</code></p>
<dd> Send signal to every &lt;pid&gt; listed.</p>
<dt><code>-&lt;signal&gt;</code></p>
<dd> <code>-s &lt;signal&gt;</code> <code>&#8211;signal &lt;signal&gt;</code> Specify the <code>signal</code> to be sent. The signal can be specified by using name or number. The behavior of signals is explained in <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) manual page.</p>
<dt><code>-q</code>, <code>&#8211;queue </code><i>value</i></p>
<dd> Use <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a>(3)</code> rather than <code><a href="/docs/linux/man/2-kill/">kill</a>(2)</code> and the value argument is used to specify an integer to be sent with the signal. If the receiving process has installed a handler for this signal using the SA_SIGINFO flag to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a>(2)</code> , then it can obtain this data via the si_value field of the siginfo_t structure.</p>
<dt><code>-l</code>, <code>&#8211;list</code> [<i>signal</i>]</p>
<dd> List signal names. This option has optional argument, which will convert signal number to signal name, or other way round.</p>
<dt><code>-L</code>,<code>&nbsp;&#8211;table</code></p>
<dd> List signal names in a nice table.</p>
<dt>
<dd></dl>
<h2>NOTES</h2>
<p> Your shell (command line interpreter) may have a built-in kill command. You may need to run the command described here as /bin/kill to solve the conflict.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>kill -9 -1</code></p>
<dd> Kill all processes you can kill.</p>
<dt><code>kill -l 11</code></p>
<dd> Translate number 11 into a signal name.</p>
<dt><code>kill -L</code></p>
<dd> List the available signal choices in a nice table.</p>
<dt><code>kill 123 543 2341 3453</code></p>
<dd> Send the default signal, SIGTERM, to all those processes.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1), <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/1-skill/">skill</a></code>(1)</p>
<h2>STANDARDS</h2>
<p> This command meets appropriate standards. The <code>-L</code> flag is Linux-specific.</p>
<h2>AUTHOR</h2>
<p> Albert Cahalan wrote kill in 1999 to replace a bsdutils one that was not standards compliant. The util-linux one might also work correctly.</p>
<h2>REPORTING BUGS</h2>
<p> Please send bug reports to </p>
<h2>Index</h2>
