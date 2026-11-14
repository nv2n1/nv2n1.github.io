---
title: "seq_open(9)"
name: "seq_open"
section: "9"
letter: "s"
url: "/docs/linux/man/9-seq_open/"
description: "seq_open – initialize sequential file"
---

<p>seq_open &#8211; initialize sequential file</p>
<h2>Synopsis</h2>
<pre><code>int seq_open(struct file *file, const struct seq_operations *op);</code></pre>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>file we initialize</dl>
<p> <i>op</i></p>
<dl>
<dd>method table describing the sequence</dl>
<h2>Description</h2>
<p><code>seq_open</code> sets <i>file</i>, associating it with a sequence described by <i>op</i>. <i>op</i>-&gt;<code>start</code> sets the iterator up and returns the first element of sequence. <i>op</i>-&gt;<code>stop</code> shuts it down. <i>op</i>-&gt;<code>next</code> returns the next element of sequence. <i>op</i>-&gt;<code>show</code> prints element into the buffer. In case of error -&gt;<code>start</code> and -&gt;<code>next</code> return ERR_PTR(error). In the end of sequence they return <code>NULL</code>. -&gt;<code>show</code> returns 0 in case of success and negative number in case of error. Returning SEQ_SKIP means &#8220;discard this element and move on&#8221;.</p>
<h2>Note</h2>
<p><code>seq_open</code> will allocate a struct seq_file and store its pointer in <i>file</i>-&gt;private_data. This pointer should not be modified.</p>
<h2>Copyright</h2>
