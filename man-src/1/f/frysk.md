---
title: "frysk(1)"
name: "frysk"
section: "1"
letter: "f"
url: "/docs/linux/man/1-frysk/"
description: "frysk – launches the Frysk Execution Analysis Tool"
---

<h2 class="name">NAME</h2>
<p> frysk &#8211; launches the Frysk Execution Analysis Tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>frysk</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>frysk</code></p>
<dd>launches the Frysk Execution Analsys Tool. </p>
<p> The goal of the frysk project is to create an intelligent, distributed, always-on system monitoring and debugging tool that allows developers and system administrators to monitor running processes and threads (including creation and destruction events), monitor the use of locking primitives, expose deadlocks, gather data and debug any given process by either choosing it from a list or by accepting frysk&#8217;s offer to open a source code or other window on a process that is in the process of crashing or that has been misbehaving in certain user-definable ways.</p>
<h3>Standard Frysk Options</h3>
<p> <code>-exe</code></p>
<dl>
<dt>
<dd> The full path of the executable to read.</dl>
<p> <code>-noexe</code></p>
<dl>
<dt>
<dd> Do not attempt to read the corresponding executable when loading a core file.</dl>
<p> <code>-sysroot </code><i>directory</i></p>
<dl>
<dt>
<dd> The system root directory under which all executables, libraries, and source are located.</dl>
<p> <code>-debug </code><i>class</i><code>=</code><i>level</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set internal debug-tracing of the specified Java <i>class</i> to <i>level</i> (level can be NONE, INFO, WARNING, FINE, and FINEST). If the <i>level</i> is absent, FINE is assumed; if the <i>class</i> is absent, the global level is set.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
frysk
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code>http:/sourceware.org/frysk</code>m[] </p>
<h2>Index</h2>
