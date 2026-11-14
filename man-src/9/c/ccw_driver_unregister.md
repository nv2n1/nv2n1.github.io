---
title: "ccw_driver_unregister(9)"
name: "ccw_driver_unregister"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_driver_unregister/"
description: "ccw_driver_unregister – deregister a ccw driver"
---

<p>ccw_driver_unregister &#8211; deregister a ccw driver</p>
<h2>Synopsis</h2>
<pre><code>void ccw_driver_unregister(struct ccw_driver *cdriver);</code></pre>
<h2>Arguments</h2>
<p><i>cdriver</i></p>
<dl>
<dd>
<dd>driver to be deregistered</dl>
<h2>Description</h2>
<p>This function is mainly a wrapper around <code>driver_unregister</code>.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
