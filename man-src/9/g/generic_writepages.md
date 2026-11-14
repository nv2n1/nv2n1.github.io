---
title: "generic_writepages(9)"
name: "generic_writepages"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_writepages/"
description: "generic_writepages – walk the list of dirty pages of the given address space and writepage all of them."
---

<p>generic_writepages &#8211; walk the list of dirty pages of the given address space and <code>writepage</code> all of them.</p>
<h2>Synopsis</h2>
<pre><code>int generic_writepages(struct address_space *mapping, struct writeback_control *wbc);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>address space structure to write</dl>
<p> <i>wbc</i></p>
<dl>
<dd>subtract the number of written pages from *<i>wbc</i>-&gt;nr_to_write</dl>
<h2>Description</h2>
<p>This is a library function, which implements the <code>writepages</code> address_space_operation.</p>
<h2>Copyright</h2>
