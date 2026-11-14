---
title: "ferror(1)"
name: "ferror"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ferror/"
description: "ferror – print a stack trace when the given message is printed by the traced program"
---

<h2 class="name">NAME</h2>
<p> ferror &#8211; print a stack trace when the given message is printed by the traced program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ferror</code> [<i>options</i>] {<i>program</i>&nbsp;<wbr><i>arg</i>&nbsp;<wbr>&#8230; | <i>pid</i>&#8230;}</dl>
<h2>DESCRIPTION</h2>
<p> <code>ferror</code></p>
<dd>monitors the processes write system call for the specified MESSAGE, printing a stack trace of the process at the point of the write.</p>
<h3>Stack Print Options</h3>
<p> <code>-number-of-frames </code><i>count</i></p>
<dl>
<dt>
<dd> Limit the back-trace to <i>count</i> frames. The default is to limit the back-trace to 10 frames. Specify 0 or &quot;all&quot; to print all frames.</dl>
<p> <code>-lite</code></p>
<dl>
<dt>
<dd> Perform a light-weight stack backtrace containing only minimal information. Equivalent to <code>-print &#8211;</code>.</dl>
<p> <code>-rich</code></p>
<dl>
<dt>
<dd> Perform a detailed stack back-trace that includes, where possible, inlined function calls, parameter names and values, and debug-names. Equivalent to <code>-print inline,params,debug-names</code>.</dl>
<p> <code>-print </code><i>print-option</i><code>,&#8230;</code></p>
<dl>
<dt>
<dd> Specify the level of detail to include in a stack back-trace. <i>print-option</i> can be any of: </p>
<p> debug-names: use debug information, such as DWARF, to determine the name of functions </p>
<p> paths: include the full path to source files and libraries </p>
<p> inline: include in-line function in back-trace </p>
<p> locals: to include local variables from each frame </p>
<p> params: include the function parameters </p>
<p> To negate a <i>print-option</i> prefix it with &quot;-&quot;.</dl>
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
ferror -e &quot;No such file or directory&quot; -- ls fake
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
