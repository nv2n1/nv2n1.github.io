---
title: "fhpd(1)"
name: "fhpd"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fhpd/"
description: "fhpd – a command line debugger"
---

<h2 class="name">NAME</h2>
<p> fhpd &#8211; a command line debugger </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fhpd</code> [<i>options</i>] {<i>program</i>&nbsp;<wbr><i>arg</i>&nbsp;<wbr>&#8230; | <i>pid</i>&#8230; | <i>core-file</i>&nbsp;<wbr>[&nbsp;<wbr><i>core-executable</i>&nbsp;<wbr>]&#8230; }</dl>
<h2>DESCRIPTION</h2>
<p> <code>fhpd</code></p>
<dd>is a command line oriented debugger implemented using the <a href="/docs/linux/man/7-frysk/">frysk</a>(7) framework with a command set loosely based on the High Performance Debugger Forum&#8217;s Version 1 standard.</p>
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
fhpd 1234
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>STANDARDS</h2>
<p> High Performance Debugging Forum Version 1 Standard</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
