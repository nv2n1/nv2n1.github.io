---
title: "funit-procmask(8)"
name: "funit-procmask"
section: "8"
letter: "f"
url: "/docs/linux/man/8-funit-procmask/"
description: "funit-procmask – test the processes signal mask for the presence (or absence) of a list if signals"
---

<p>funit-procmask &#8211; test the processes signal mask for the presence (or absence) of a list if signals</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>funit-procmask</code> [<code>-y</code>] [<code>-n</code>] <i>signal-number</i>&#8230;</dl>
<h2>Description</h2>
<dd>Test for the presence (or absence) of the list of signals in the processes signal mask. If the test fails, exit with a non-zero status. </p>
<p> <code>-y</code></p>
<dl>
<dd>Test in the affermative, only exit successfully when all the signals are present.</dl>
<p> <code>-n</code></p>
<dl>
<dd>Test in the negative, only exit successfully when all the signals are absent.</dl>
<p> This program is used by <code><a href="/docs/linux/man/8-funit/">funit</a></code>(8), as part of Frysk&#8217;s testsuite.</p>
<h2>Example</h2>
<p>Test if SIGUSR1 (1) is absent from the default signal mask. </p>
<dl>
<dd>
<pre>/usr/lib/frysk/funit-procmask -n 1</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit/">funit</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
