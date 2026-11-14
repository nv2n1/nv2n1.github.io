---
title: "seq_hlist_start_percpu(9)"
name: "seq_hlist_start_percpu"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_hlist_start_percpu/"
description: "seq_hlist_start_percpu – start an iteration of a percpu hlist array"
---

<p>seq_hlist_start_percpu &#8211; start an iteration of a percpu hlist array</p>
<h2>Synopsis</h2>
<pre><code>struct hlist_node *seq_hlist_start_percpu(struct hlist_head __percpu *head, int *cpu, loff_t pos);</code></pre>
<h2>Arguments</h2>
<p><i>head</i></p>
<dl>
<dd>
<dd>pointer to percpu array of struct hlist_heads</dl>
<p> <i>cpu</i></p>
<dl>
<dd>pointer to cpu &#8220;cursor&#8221;</dl>
<p> <i>pos</i></p>
<dl>
<dd>start position of sequence</dl>
<h2>Description</h2>
<p>Called at seq_file-&gt;op-&gt;<code>start</code>.</p>
<h2>Copyright</h2>
