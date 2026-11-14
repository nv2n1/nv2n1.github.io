---
title: "fsystest(8)"
name: "fsystest"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsystest/"
description: "fsystest – run Frysk’s system testsuite"
---

<p>fsystest &#8211; run Frysk&#8217;s system testsuite</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>fsystest</code></dl>
<h2>Description</h2>
<p><code>fsystest</code></p>
<dd>runs frysk&#8217;s system testsuite. </p>
<p> Frysk&#8217;s system testsuite checks for regressions in the underlying system, and not regressions in frysk. For instance, this testsuite checks that the kernel correctly traces an exec system call (a problem in early 2.6.18 kernels).</p>
<h2>Example</h2>
<dl>
<dd>
<pre>/usr/lib/frysk/fsystest</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit/">funit</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
