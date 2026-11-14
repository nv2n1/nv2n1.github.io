---
title: "ccw_driver_register(9)"
name: "ccw_driver_register"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_driver_register/"
description: "ccw_driver_register – register a ccw driver"
---

<p>ccw_driver_register &#8211; register a ccw driver</p>
<h2>Synopsis</h2>
<pre><code>int ccw_driver_register(struct ccw_driver *cdriver);</code></pre>
<h2>Arguments</h2>
<p><i>cdriver</i></p>
<dl>
<dd>
<dd>driver to be registered</dl>
<h2>Description</h2>
<p>This function is mainly a wrapper around <code>driver_register</code>.</p>
<h2>Return</h2>
<p><code>0</code> on success and a negative error value on failure.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
