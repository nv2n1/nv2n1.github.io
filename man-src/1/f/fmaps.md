---

title: "fmaps(1)"
name: "fmaps"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fmaps/"
description: "fmaps – print the process or a corefile’s address maps"
---

<dl>
<dt> <code>fmaps</code> {<i>program</i>&nbsp;<wbr><i>arg</i>&nbsp;<wbr>&#8230; | <i>pid</i>&#8230; | <i>core-file</i>&nbsp;<wbr>[&nbsp;<wbr><i>core-executable</i>&nbsp;<wbr>]&#8230; }</dt></dl>
<p> <code>fmaps</code></p>
<dd>prints out a process or a corefile&#8217;s address maps</dd>
<h3>Standard Frysk Options</h3>
<p> <code>-exe</code></p>
<dl>
<dt>
</dt><dd> The full path of the executable to read.</dd></dl>
<p> <code>-noexe</code></p>
<dl>
<dt>
</dt><dd> Do not attempt to read the corresponding executable when loading a core file.</dd></dl>
<p> <code>-sysroot </code><i>directory</i></p>
<dl>
<dt>
</dt><dd> The system root directory under which all executables, libraries, and source are located.</dd></dl>
<p> <code>-debug </code><i>class</i><code>=</code><i>level</i><code>&#8230;</code></p>
<dl>
<dt>
</dt><dd> Set internal debug-tracing of the specified Java <i>class</i> to <i>level</i> (level can be NONE, INFO, WARNING, FINE, and FINEST). If the <i>level</i> is absent, FINE is assumed; if the <i>class</i> is absent, the global level is set.</dd></dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
</dt><dd>
<pre>
fmaps pid [...]
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-frysk/">frysk</a>(7)</p>
<h2>BUGS</h2>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
