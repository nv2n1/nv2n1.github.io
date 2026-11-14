---
title: "funit-exit(8)"
name: "funit-exit"
section: "8"
letter: "f"
url: "/docs/linux/man/8-funit-exit/"
description: "funit-exit – exit with specified status, or terminate with the specified signal"
---

<p>funit-exit &#8211; exit with specified status, or terminate with the specified signal</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>funit-exit</code> [<code>&#8211;</code><i>signal</i>] [<i>status</i>]</dl>
<h2>Description</h2>
<p><code>funit-exit</code></p>
<dd>exits with the specified <i>status</i> or terminates with the specified <i>signal</i>. </p>
<p> &#8211;<i>signal</i></p>
<dl>
<dd>Terminate with the specified. <i>signal</i>.</dl>
<p> <i>status</i></p>
<dl>
<dd>Exit with the specified <i>status</i>.</dl>
<h2>Examples</h2>
<p>Run the 32-bit version of the <code>funit-exit</code> program. </p>
<dl>
<dd>
<pre>/usr/lib/frysk/funit-exit 0</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit/">funit</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
