---

title: "pprof(1)"
name: "pprof"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pprof/"
description: "pprof – manual page for pprof (part of gperftools)"
---

<h2>NAME</h2>
<p> pprof &#8211; manual page for pprof (part of gperftools)</p>
<p> <code>pprof</code> [<i>options</i>] <i>&lt;program&gt; &lt;profile&gt;</i></p>
<dl>
<dt>
</dt><dd> Prints specified cpu- or heap-profile</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cum</code></dt>
<dd> Sort by cumulative data</dd>
<dt><code>&#8211;base=</code>&lt;base&gt;</dt>
<dd> Subtract &lt;base&gt; from &lt;profile&gt; before display</dd></dl>
<h3>Reporting Granularity:</h3>
<dl>
<dt><code>&#8211;addresses</code></dt>
<dd> Report at address level</dd>
<dt><code>&#8211;lines</code></dt>
<dd> Report at source line level</dd>
<dt><code>&#8211;functions</code></dt>
<dd> Report at function level [default]</dd>
<dt><code>&#8211;files</code></dt>
<dd> Report at source file level</dd></dl>
<h3>Output type:</h3>
<dl>
<dt><code>&#8211;text</code></dt>
<dd> Generate text report [default]</dd>
<dt><code>&#8211;gv</code></dt>
<dd> Generate Postscript and display</dd>
<dt><code>&#8211;list=</code>&lt;regexp&gt;</dt>
<dd> Generate source listing of matching routines</dd>
<dt><code>&#8211;disasm=</code>&lt;regexp&gt;</dt>
<dd> Generate disassembly of matching routines</dd>
<dt><code>&#8211;dot</code></dt>
<dd> Generate DOT file to stdout</dd>
<dt><code>&#8211;ps</code></dt>
<dd> Generate Postcript to stdout</dd>
<dt><code>&#8211;pdf</code></dt>
<dd> Generate PDF to stdout</dd>
<dt><code>&#8211;gif</code></dt>
<dd> Generate GIF to stdout</dd></dl>
<h3>Heap-Profile Options:</h3>
<dl>
<dt><code>&#8211;inuse_space</code></dt>
<dd> Display in-use (mega)bytes [default]</dd>
<dt><code>&#8211;inuse_objects</code></dt>
<dd> Display in-use objects</dd>
<dt><code>&#8211;alloc_space</code></dt>
<dd> Display allocated (mega)bytes</dd>
<dt><code>&#8211;alloc_objects</code></dt>
<dd> Display allocated objects</dd>
<dt><code>&#8211;show_bytes</code></dt>
<dd> Display space in bytes</dd>
<dt><code>&#8211;drop_negative</code></dt>
<dd> Ignore negaive differences</dd></dl>
<h3>Call-graph Options:</h3>
<dl>
<dt><code>&#8211;nodecount=</code>&lt;n&gt;</dt>
<dd> Show at most so many nodes [default=80]</dd>
<dt><code>&#8211;nodefraction=</code>&lt;f&gt;</dt>
<dd> Hide nodes below &lt;f&gt;*total [default=.005]</dd>
<dt><code>&#8211;edgefraction=</code>&lt;f&gt;</dt>
<dd> Hide edges below &lt;f&gt;*total [default=.001]</dd>
<dt><code>&#8211;focus=</code>&lt;regexp&gt;</dt>
<dd> Focus on nodes matching &lt;regexp&gt;</dd>
<dt><code>&#8211;ignore=</code>&lt;regexp&gt;</dt>
<dd> Ignore nodes matching &lt;regexp&gt;</dd>
<dt><code>&#8211;scale=</code>&lt;n&gt;</dt>
<dd> Set GV scaling [default=0]</dd></dl>
<h2>EXAMPLES</h2>
<p> pprof /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Outputs one line per procedure</dd></dl>
<p> pprof <code>&#8211;gv</code> /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Displays annotated call-graph via &#8216;gv&#8217;</dd></dl>
<p> pprof <code>&#8211;gv</code> <code>&#8211;focus</code>=<i>Mutex</i> /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Restricts to code paths including a .*Mutex.* entry</dd></dl>
<p> pprof <code>&#8211;gv</code> <code>&#8211;focus</code>=<i>Mutex</i> <code>&#8211;ignore</code>=<i>string</i> /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Code paths including Mutex but not string</dd></dl>
<p> pprof <code>&#8211;list</code>=<i>getdir</i> /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Dissassembly (with per-line annotations) for getdir()</dd></dl>
<p> pprof <code>&#8211;disasm</code>=<i>getdir</i> /bin/ls ls.prof</p>
<dl>
<dt>
</dt><dd> Dissassembly (with per-PC annotations) for getdir()</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Google Inc.</p>
<h2>SEE ALSO</h2>
<p> Further documentation for <code>pprof</code> is maintained as a web page called <code>cpu_profiler.html</code> and is likely installed at one of the following locations:</p>
<dl>
<dt>
</dt><dd> <code>/usr/share/gperftools/cpu_profiler.html</code><br />
 <code>/usr/local/share/gperftools/cpu_profiler.html</code></dd></dl>
