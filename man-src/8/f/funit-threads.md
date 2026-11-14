---
title: "funit-threads(8)"
name: "funit-threads"
section: "8"
letter: "f"
url: "/docs/linux/man/8-funit-threads/"
description: "funit-threads – creates lots and lots of threads"
---

<p>funit-threads &#8211; creates lots and lots of threads</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>funit-threads</code> [<code>&#8211;clone</code>] [<code>&#8211;block</code>] [<code>&#8211;loop</code>] {<i>pid</i>} {<i>signal</i>} {<i>seconds</i>} {<i>number-threads</i>}</dl>
<h2>Description</h2>
<dd>A small slave program, used by <code>funit</code>, as part of frysk&#8217;s JUnit testsuite. </p>
<p> <code>&#8211;clone</code></p>
<dl>
<dd>Each thread will repeatedly clone itself (default).</dl>
<p> <code>&#8211;block</code></p>
<dl>
<dd>Each thread will block.</dl>
<p> <code>&#8211;loop</code></p>
<dl>
<dd>Each thread will execute an infinite loop.</dl>
<p> <i>pid</i></p>
<dl>
<dd>Thread ID to send <i>signal</i> to once all threads have been created.</dl>
<p> <i>signal</i></p>
<dl>
<dd>The signal to send to <i>tid</i> once all threads have been started.</dl>
<p> <i>seconds</i></p>
<dl>
<dd>Number of seconds to wait before the program exits.</dl>
<p> <i>number-threads</i></p>
<dl>
<dd>Number of threads to create.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre>/usr/lib/frysk/funit-threads</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit/">funit</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
