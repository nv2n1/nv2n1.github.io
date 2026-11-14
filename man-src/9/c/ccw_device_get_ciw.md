---
title: "ccw_device_get_ciw(9)"
name: "ccw_device_get_ciw"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_device_get_ciw/"
description: "ccw_device_get_ciw – Search for CIW command in extended sense data."
---

<p>ccw_device_get_ciw &#8211; Search for CIW command in extended sense data.</p>
<h2>Synopsis</h2>
<pre><code>struct ciw *ccw_device_get_ciw(struct ccw_device *cdev, __u32 ct);</code></pre>
<h2>Arguments</h2>
<p><i>cdev</i></p>
<dl>
<dd>
<dd>ccw device to inspect</dl>
<p> <i>ct</i></p>
<dl>
<dd>command type to look for</dl>
<h2>Description</h2>
<p>During SenseID, command information words (CIWs) describing special commands available to the device may have been stored in the extended sense data. This function searches for CIWs of a specified command type in the extended sense data.</p>
<h2>Return</h2>
<p><code>NULL</code> if no extended sense data has been stored or if no CIW of the specified command type could be found, else a pointer to the CIW of the specified command type.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
