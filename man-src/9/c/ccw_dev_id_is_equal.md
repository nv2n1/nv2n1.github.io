---
title: "ccw_dev_id_is_equal(9)"
name: "ccw_dev_id_is_equal"
section: "9"
letter: "c"
url: "/docs/linux/man/9-ccw_dev_id_is_equal/"
description: "ccw_dev_id_is_equal – compare two ccw_dev_ids"
---

<p>ccw_dev_id_is_equal &#8211; compare two ccw_dev_ids</p>
<h2>Synopsis</h2>
<pre><code>int ccw_dev_id_is_equal(struct ccw_dev_id *dev_id1, struct ccw_dev_id *dev_id2);</code></pre>
<h2>Arguments</h2>
<p><i>dev_id1</i></p>
<dl>
<dd>
<dd>a ccw_dev_id</dl>
<p> <i>dev_id2</i></p>
<dl>
<dd>another ccw_dev_id</dl>
<h2>Return</h2>
<p><code>1</code> if the two structures are equal field-by-field, <code>0</code> if not.</p>
<h2>Context</h2>
<p>any</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
