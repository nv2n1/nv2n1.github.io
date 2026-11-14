---
title: "wakeup_readers(9)"
name: "wakeup_readers"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wakeup_readers/"
---

wakeup_readers - wake up readers waiting on a channel

<h2>Synopsis</h2>

<pre><code>void wakeup_readers(struct irq_work *work);</code></pre>

<h2>Arguments</h2>

<i>work</i>
<dl><dd><dd>contains the channel buffer</dl>

<h2>Description</h2>

This is the function used to defer reader waking

<h2>Copyright</h2>


