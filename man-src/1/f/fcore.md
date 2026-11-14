---
title: "fcore(1)"
name: "fcore"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcore/"
description: "fcore – extract a core file from a process"
---

<h2 class="name">NAME</h2>
<p> fcore &#8211; extract a core file from a process </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fcore</code> [<i>options</i>] {<i>pid</i>&#8230;}</dl>
<h2>DESCRIPTION</h2>
<p> <code>fcore</code></p>
<dd>constructs a core-file from a running process, and writes it to disk. </p>
<p> <code>-a</code>, <code>-allmaps</code></p>
<dl>
<dt>
<dd> Write all readable segment maps. The default level is to attempt to emulate gcore segment writing strategy. By specifying this option, fcore will write all readable maps.</dl>
<p> <code>-s</code>, <code>-segments </code><i>regex</i></p>
<dl>
<dt>
<dd> Writes only the segments that match the regex specified. Elide all other segments.</dl>
<p> <code>-o </code><i>output-file</i></p>
<dl>
<dt>
<dd> Specifies the name of the core file. Default is core. The core-file extension will still use the pid of the process being dumped.</dl>
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
fcore 1234
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
