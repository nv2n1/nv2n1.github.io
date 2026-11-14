---
title: "ccwgroup_driver_register(9)"
name: "ccwgroup_driver_register"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccwgroup_driver_register/"
description: "ccwgroup_driver_register – register a ccw group driver"
---

<p>ccwgroup_driver_register &#8211; register a ccw group driver</p>
<h2>Synopsis</h2>
<pre><code>int ccwgroup_driver_register(struct ccwgroup_driver *cdriver);</code></pre>
<h2>Arguments</h2>
<p><i>cdriver</i></p>
<dl>
<dd>
<dd>driver to be registered</dl>
<h2>Description</h2>
<p>This function is mainly a wrapper around <code>driver_register</code>.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
