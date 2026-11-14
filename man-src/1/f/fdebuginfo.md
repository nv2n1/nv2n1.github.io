---
title: "fdebuginfo(1)"
name: "fdebuginfo"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdebuginfo/"
description: "fdebuginfo – display the debug-info paths for a process and its shared modules"
---

<h2 class="name">NAME</h2>
<p> fdebuginfo &#8211; display the debug-info paths for a process and its shared modules </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fdebuginfo</code> [<i>options</i>] {<i>program</i>&nbsp;<wbr><i>arg</i>&nbsp;<wbr>&#8230; | <i>pid</i>&#8230; | <i>core-file</i>&nbsp;<wbr>[&nbsp;<wbr><i>core-executable</i>&nbsp;<wbr>]&#8230; }</dl>
<h2>DESCRIPTION</h2>
<p> <code>fdebuginfo</code></p>
<dd>lists the modules of a process and the location of their Debugging Information, if present. </p>
<p> The output is in the form: &quot;Module Name&quot; &quot;Debuginfo Path&quot;</p>
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
fdebuginfo 1234
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/1-fdebugrpm/">fdebugrpm</a>(1)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
