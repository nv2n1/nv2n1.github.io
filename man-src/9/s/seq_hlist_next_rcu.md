---
title: "seq_hlist_next_rcu(9)"
name: "seq_hlist_next_rcu"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_hlist_next_rcu/"
description: "seq_hlist_next_rcu – move to the next position of the hlist protected by RCU"
---

<p>seq_hlist_next_rcu &#8211; move to the next position of the hlist protected by RCU</p>
<h2>Synopsis</h2>
<pre><code>struct hlist_node *seq_hlist_next_rcu(void *v, struct hlist_head *head, loff_t *ppos);</code></pre>
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
<p>Called at seq_file-&gt;op-&gt;<code>next</code>. </p>
<p> This list-traversal primitive may safely run concurrently with the _rcu list-mutation primitives such as <code>hlist_add_head_rcu</code> as long as the traversal is guarded by <code>rcu_read_lock</code>.</p>
<h2>Copyright</h2>
