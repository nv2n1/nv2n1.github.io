---
title: "ht_create_irq(9)"
name: "ht_create_irq"
section: "9"
letter: "h"
url: "/docs/linux/man/9-ht_create_irq/"
---

ht_create_irq - create an irq and attach it to a device.

<h2>Synopsis</h2>

<pre><code>int ht_create_irq(struct pci_dev *dev, int idx);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>The hypertransport device to find the irq capability on.</dl>
 

 <i>idx</i>
<dl><dd>Which of the possible irqs to attach to.</dl>

<h2>Description</h2>

ht_create_irq needs to be called for all hypertransport devices that generate irqs. 

 The irq number of the new irq or a negative error value is returned.

<h2>Copyright</h2>


