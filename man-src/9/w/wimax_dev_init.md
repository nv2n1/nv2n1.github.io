---
title: "wimax_dev_init(9)"
name: "wimax_dev_init"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_dev_init/"
---

wimax_dev_init - initialize a newly allocated instance

<h2>Synopsis</h2>

<pre><code>void wimax_dev_init(struct wimax_dev *wimax_dev);</code></pre>

<h2>Arguments</h2>

<i>wimax_dev</i>
<dl><dd><dd>WiMAX device descriptor to initialize.</dl>

<h2>Description</h2>

Initializes fields of a freshly allocated <i>wimax_dev</i> instance. This function assumes that after allocation, the memory occupied by <i>wimax_dev</i> was zeroed.

<h2>Copyright</h2>


