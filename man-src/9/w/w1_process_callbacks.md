---
title: "w1_process_callbacks(9)"
name: "w1_process_callbacks"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_process_callbacks/"
description: "w1_process_callbacks – execute each dev->async_list callback entry"
---

<p>w1_process_callbacks &#8211; execute each dev-&gt;async_list callback entry</p>
<h2>Synopsis</h2>
<pre><code>int w1_process_callbacks(struct w1_master *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>w1_master device</dl>
<h2>Description</h2>
<p>The w1 master list_mutex must be held.</p>
<h2>Return</h2>
<p>1 if there were commands to executed 0 otherwise</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
