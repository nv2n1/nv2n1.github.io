---
title: "superhyway_unregister_driver(9)"
name: "superhyway_unregister_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-superhyway_unregister_driver/"
description: "superhyway_unregister_driver – Unregister a SuperHyway driver"
---

<p>superhyway_unregister_driver &#8211; Unregister a SuperHyway driver</p>
<h2>Synopsis</h2>
<pre><code>void superhyway_unregister_driver(struct superhyway_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>drv</i></p>
<dl>
<dd>
<dd>SuperHyway driver to unregister.</dl>
<h2>Description</h2>
<p>This cleans up after <code>superhyway_register_driver</code>, and should be invoked in the exit path of any module drivers.</p>
<h2>Author</h2>
<p><code>Paul Mundt</code> &lt;lethal [at] linux-sh.org&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
