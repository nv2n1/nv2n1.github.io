---
title: "seq_hlist_next(9)"
name: "seq_hlist_next"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_hlist_next/"
description: "seq_hlist_next – move to the next position of the hlist"
---

<p>seq_hlist_next &#8211; move to the next position of the hlist</p>
<h2>Synopsis</h2>
<pre><code>struct hlist_node *seq_hlist_next(void *v, struct hlist_head *head, loff_t *ppos);</code></pre>
<h2>Arguments</h2>
<p><i>v</i></p>
<dl>
<dd>
<dd>the current iterator</dl>
<p> <i>head</i></p>
<dl>
<dd>the head of the hlist</dl>
<p> <i>ppos</i></p>
<dl>
<dd>the current position</dl>
<h2>Description</h2>
<p>Called at seq_file-&gt;op-&gt;<code>next</code>.</p>
<h2>Copyright</h2>
