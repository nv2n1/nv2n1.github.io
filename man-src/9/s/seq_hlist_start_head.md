---
title: "seq_hlist_start_head(9)"
name: "seq_hlist_start_head"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_hlist_start_head/"
description: "seq_hlist_start_head – start an iteration of a hlist"
---

<p>seq_hlist_start_head &#8211; start an iteration of a hlist</p>
<h2>Synopsis</h2>
<pre><code>struct hlist_node *seq_hlist_start_head(struct hlist_head *head, loff_t pos);</code></pre>
<h2>Arguments</h2>
<p><i>head</i></p>
<dl>
<dd>
<dd>the head of the hlist</dl>
<p> <i>pos</i></p>
<dl>
<dd>the start position of the sequence</dl>
<h2>Description</h2>
<p>Called at seq_file-&gt;op-&gt;<code>start</code>. Call this function if you want to print a header at the top of the output.</p>
<h2>Copyright</h2>
