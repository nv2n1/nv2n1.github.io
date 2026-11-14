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
<h2>SYNOPSIS</h2>
<p> <code>pprof</code> [<i>options</i>] <i>&lt;program&gt; &lt;profile&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Prints specified cpu- or heap-profile</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cum</code></p>
<dd> Sort by cumulative data</p>
<dt><code>&#8211;base=</code>&lt;base&gt;</p>
<dd> Subtract &lt;base&gt; from &lt;profile&gt; before display</dl>
<h3>Reporting Granularity:</h3>
<dl>
<dt><code>&#8211;addresses</code></p>
<dd> Report at address level</p>
<dt><code>&#8211;lines</code></p>
<dd> Report at source line level</p>
<dt><code>&#8211;functions</code></p>
<dd> Report at function level [default]</p>
<dt><code>&#8211;files</code></p>
<dd> Report at source file level</dl>
<h3>Output type:</h3>
<dl>
<dt><code>&#8211;text</code></p>
<dd> Generate text report [default]</p>
<dt><code>&#8211;gv</code></p>
<dd> Generate Postscript and display</p>
<dt><code>&#8211;list=</code>&lt;regexp&gt;</p>
<dd> Generate source listing of matching routines</p>
<dt><code>&#8211;disasm=</code>&lt;regexp&gt;</p>
<dd> Generate disassembly of matching routines</p>
<dt><code>&#8211;dot</code></p>
<dd> Generate DOT file to stdout</p>
<dt><code>&#8211;ps</code></p>
<dd> Generate Postcript to stdout</p>
<dt><code>&#8211;pdf</code></p>
<dd> Generate PDF to stdout</p>
<dt><code>&#8211;gif</code></p>
<dd> Generate GIF to stdout</dl>
<h3>Heap-Profile Options:</h3>
<dl>
<dt><code>&#8211;inuse_space</code></p>
<dd> Display in-use (mega)bytes [default]</p>
<dt><code>&#8211;inuse_objects</code></p>
<dd> Display in-use objects</p>
<dt><code>&#8211;alloc_space</code></p>
<dd> Display allocated (mega)bytes</p>
<dt><code>&#8211;alloc_objects</code></p>
<dd> Display allocated objects</p>
<dt><code>&#8211;show_bytes</code></p>
<dd> Display space in bytes</p>
<dt><code>&#8211;drop_negative</code></p>
<dd> Ignore negaive differences</dl>
<h3>Call-graph Options:</h3>
<dl>
<dt><code>&#8211;nodecount=</code>&lt;n&gt;</p>
<dd> Show at most so many nodes [default=80]</p>
<dt><code>&#8211;nodefraction=</code>&lt;f&gt;</p>
<dd> Hide nodes below &lt;f&gt;*total [default=.005]</p>
<dt><code>&#8211;edgefraction=</code>&lt;f&gt;</p>
<dd> Hide edges below &lt;f&gt;*total [default=.001]</p>
<dt><code>&#8211;focus=</code>&lt;regexp&gt;</p>
<dd> Focus on nodes matching &lt;regexp&gt;</p>
<dt><code>&#8211;ignore=</code>&lt;regexp&gt;</p>
<dd> Ignore nodes matching &lt;regexp&gt;</p>
<dt><code>&#8211;scale=</code>&lt;n&gt;</p>
<dd> Set GV scaling [default=0]</dl>
<h2>EXAMPLES</h2>
<p> pprof /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Outputs one line per procedure</dl>
<p> pprof <code>&#8211;gv</code> /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Displays annotated call-graph via &#8216;gv&#8217;</dl>
<p> pprof <code>&#8211;gv</code> <code>&#8211;focus</code>=<i>Mutex</i> /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Restricts to code paths including a .*Mutex.* entry</dl>
<p> pprof <code>&#8211;gv</code> <code>&#8211;focus</code>=<i>Mutex</i> <code>&#8211;ignore</code>=<i>string</i> /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Code paths including Mutex but not string</dl>
<p> pprof <code>&#8211;list</code>=<i>getdir</i> /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Dissassembly (with per-line annotations) for getdir()</dl>
<p> pprof <code>&#8211;disasm</code>=<i>getdir</i> /bin/ls ls.prof</p>
<dl>
<dt>
<dd> Dissassembly (with per-PC annotations) for getdir()</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Google Inc.</p>
<h2>SEE ALSO</h2>
<p> Further documentation for <code>pprof</code> is maintained as a web page called <code>cpu_profiler.html</code> and is likely installed at one of the following locations:</p>
<dl>
<dt>
<dd> <code>/usr/share/gperftools/cpu_profiler.html</code><br />
 <code>/usr/local/share/gperftools/cpu_profiler.html</code></dl>
<h2>Index</h2>
