---
title: "umad_debug(3)"
name: "umad_debug"
section: "3"
letter: "u"
url: "/docs/linux/man/3-umad_debug/"
description: "umad_debug – set debug level"
---

<p>umad_debug &#8211; set debug level</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/umad.h&gt;

int umad_debug(int level);</code></pre>
<h2>Description</h2>
<p><code>umad_debug()</code> sets the umad library internal debug level to <i>level</i>. The following debug levels are supported: 0 &#8211; no debug (the default), 1 &#8211; basic debug information, 2 &#8211; verbose debug information. Negative values are ignored in terms of set. Note that the current debug level can be queried by passing a negative value as <i>level</i>.</p>
<h2>Return Value</h2>
<p><code>umad_debug()</code> returns the actual debug level.</p>
<h2>Authors</h2>
<dl>
<dt>Hal Rosenstock &lt;halr [at] voltaire.com&gt;</p>
<dd>
<dt>Dotan Barak &lt;dotanb [at] mellanox.co.il&gt;</p>
<dd></dl>
