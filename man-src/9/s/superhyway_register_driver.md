---
title: "superhyway_register_driver(9)"
name: "superhyway_register_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-superhyway_register_driver/"
description: "superhyway_register_driver – Register a new SuperHyway driver"
---

<p>superhyway_register_driver &#8211; Register a new SuperHyway driver</p>
<h2>Synopsis</h2>
<pre><code>int superhyway_register_driver(struct superhyway_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>drv</i></p>
<dl>
<dd>
<dd>SuperHyway driver to register.</dl>
<h2>Description</h2>
<p>This registers the passed in <i>drv</i>. Any devices matching the id table will automatically be populated and handed off to the driver&#8217;s specified probe routine.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
