---
title: "seq_hlist_next_percpu(9)"
name: "seq_hlist_next_percpu"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_hlist_next_percpu/"
description: "seq_hlist_next_percpu – move to the next position of the percpu hlist array"
---

<p>seq_hlist_next_percpu &#8211; move to the next position of the percpu hlist array</p>
<h2>Synopsis</h2>
<pre><code>struct hlist_node *seq_hlist_next_percpu(void *v, struct hlist_head __percpu *head, int *cpu, loff_t *pos);</code></pre>
<h2>Arguments</h2>
<p><i>v</i></p>
<dl>
<dd>
<dd>pointer to current hlist_node</dl>
<p> <i>head</i></p>
<dl>
<dd>pointer to percpu array of struct hlist_heads</dl>
<p> <i>cpu</i></p>
<dl>
<dd>pointer to cpu &#8220;cursor&#8221;</dl>
<p> <i>pos</i></p>
<dl>
<dd>start position of sequence</dl>
<h2>Description</h2>
<p>Called at seq_file-&gt;op-&gt;<code>next</code>.</p>
<h2>Copyright</h2>
