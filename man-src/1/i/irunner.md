---
title: "irunner(1)"
name: "irunner"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irunner/"
description: "irunner – interactive runner interface"
---

<h2>NAME</h2>
<p> <code>irunner &#8211; interactive runner interface </code></p>
<h2>SYNOPSIS</h2>
<pre>
<code>irunner</code> [<i>options</i>] <i>file_to_run</i>
</pre>
<h2>DESCRIPTION</h2>
<p> irunner is an interface to the various interactive runners available in IPython&#8217;s <code>irunner</code> module. </p>
<p> The already implemented runners are listed below; adding one for a new program is a trivial task, see the source for examples.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>&#8211;ipython</code></p>
<dd> IPython interactive runner (default).</p>
<dt><code>&#8211;python</code></p>
<dd> Python interactive runner.</p>
<dt><code>&#8211;sage</code></p>
<dd> SAGE interactive runner.</dl>
<h2>EXAMPLE</h2>
<p> irunner.py &#8211;python &#8212; &#8211;help will pass &#8211;help to the python runner. Similarly, irunner.py &#8211;ipython &#8212; &#8211;interact script.ipy</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipython/">ipython</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> <code>irunner</code> is an extension of Ken Schutte &lt;kschutte-AT-csail.mit.edu&gt;&#8217;s script contributed on the ipython-user list: <a rel="nofollow" href="http://scipy.net/pipermail/ipython-user/2006-May/001705.html">http://scipy.net/pipermail/ipython-user/2006-May/001705.html</a> </p>
<p> This manual page was written by Bernd Zeimetz &lt;bernd [at] bzed.de&gt;, for the Debian project (but may be used by others). Modified by Fernando Perez &lt;Fernando.Perez [at] berkeley.edu&gt; for inclusion in IPython. </p>
<h2>Index</h2>
