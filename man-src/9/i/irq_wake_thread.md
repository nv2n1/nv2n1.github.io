---
title: "irq_wake_thread(9)"
name: "irq_wake_thread"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_wake_thread/"
---

irq_wake_thread - wake the irq thread for the action identified by dev_id

<h2>Synopsis</h2>

<pre><code>void irq_wake_thread(unsigned int irq, void *dev_id);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>Interrupt line</dl>
 

 <i>dev_id</i>
<dl><dd>Device identity for which the thread should be woken</dl>

<h2>Copyright</h2>


