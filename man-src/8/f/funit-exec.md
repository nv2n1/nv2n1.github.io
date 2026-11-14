---
title: "funit-exec(8)"
name: "funit-exec"
section: "8"
letter: "f"
url: "/docs/linux/man/8-funit-exec/"
description: "funit-exec – on CNTRL-C exec the specified program"
---

<p>funit-exec &#8211; on CNTRL-C exec the specified program</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>funit-exec</code> [<i>OPTION</i>] {<i>program</i>} [<i>arg</i>&#8230;]</dl>
<h2>Description</h2>
<dd>Wait for a SIGINT (cntrl-c) signal and then exec <i>program</i> passing it <i>args</i>. </p>
<p> Sending a SIGUSR1 signal will cause a random non-main thread to make the exec call. </p>
<p> <code>-m </code><i>pid</i></p>
<dl>
<dd>The <i>pid</i> of the master process that should be sent a signal once this program is running (default 0).</dl>
<p> <code>-s </code><i>signal</i></p>
<dl>
<dd>The <i>signal</i> to send to the master process once this program is running (default 0).</dl>
<p> <code>-t </code><i>timeout</i></p>
<dl>
<dd>Exit after <i>timeout</i> seconds.</dl>
<p> <code>-c </code><i>count</i></p>
<dl>
<dd>Create <i>count</i> threads.</dl>
<p> <code>-e </code><i>executable</i></p>
<dl>
<dd>The <i>executable</i> to exec (default is the <i>program</i>).</dl>
<p> <code>-b</code></p>
<dl>
<dd>Brand the exec with the thread that initiated it by setting argv[0] to the string TID:PID.</dl>
<p> <i>program</i> <i>arg</i>&#8230;</p>
<dl>
<dd>The program and arguments to pass to the exec call.</dl>
<p> This program is used by <code>funit</code>, as part of frysk&#8217;s JUnit testsuite.</p>
<h2>Example</h2>
<p>Create a 32-bit process that, on cntrl-c (SIGINT), will exec the 64-bit <code>funit-exit</code> program. </p>
<dl>
<dd>
<pre>/usr/lib/frysk/funit-exec \
 /usr/lib64/frysk/funit-exec /bin/echo done</pre>
</dl>
<p> Create a process, with one additional thread, signals the shell with SIGUSR1 once it is running, and then execs <code>/bin/echo</code> but with argument zero set to &quot;arg0&quot;. </p>
<dl>
<dd>
<pre>/usr/lib/frysk/funit-exec -c 1 -s 1 -p $$ \
 -e /bin/echo arg0 arg1</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit/">funit</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
