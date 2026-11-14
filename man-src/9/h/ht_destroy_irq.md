---
title: "ht_destroy_irq(9)"
name: "ht_destroy_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-ht_destroy_irq/"
---

ht_destroy_irq - destroy an irq created with ht_create_irq

<h2>Synopsis</h2>

<pre><code>void ht_destroy_irq(unsigned int irq);</code></pre>

<h2>Arguments</h2>

<i>irq</i>
<dl><dd><dd>irq to be destroyed</dl>

<h2>Description</h2>

This reverses ht_create_irq removing the specified irq from existence. The irq should be free before this happens.

<h2>Copyright</h2>


