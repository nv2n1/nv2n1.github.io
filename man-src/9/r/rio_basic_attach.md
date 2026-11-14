---
title: "rio_basic_attach(9)"
name: "rio_basic_attach"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_basic_attach/"
description: "rio_basic_attach –"
---

<p>rio_basic_attach &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int rio_basic_attach(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>When this enumeration/discovery method is loaded as a module this function registers its specific enumeration and discover routines for all available RapidIO mport devices. The &#8220;scan&#8221; command line parameter controls ability of the module to start RapidIO enumeration/discovery automatically. </p>
<p> Returns 0 for success or -EIO if unable to register itself. </p>
<p> This enumeration/discovery method cannot be unloaded and therefore does not provide a matching cleanup_module routine.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
