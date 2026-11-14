---
title: "sync_mapping_buffers(9)"
name: "sync_mapping_buffers"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sync_mapping_buffers/"
description: "sync_mapping_buffers – write out & wait upon a mapping’s “associated” buffers"
---

<p>sync_mapping_buffers &#8211; write out &amp; wait upon a mapping&#8217;s &#8220;associated&#8221; buffers</p>
<h2>Synopsis</h2>
<pre><code>int sync_mapping_buffers(struct address_space *mapping);</code></pre>
<h2>Arguments</h2>
<p><i>mapping</i></p>
<dl>
<dd>
<dd>the mapping which wants those buffers written</dl>
<h2>Description</h2>
<p>Starts I/O against the buffers at mapping-&gt;private_list, and waits upon that I/O. </p>
<p> Basically, this is a convenience function for <code>fsync</code>. <i>mapping</i> is a file or directory which needs those buffers to be written for a successful <code>fsync</code>.</p>
<h2>Copyright</h2>
