---
title: "pci_alloc_irq_vectors(9)"
name: "pci_alloc_irq_vectors"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_alloc_irq_vectors/"
description: "pci_alloc_irq_vectors – allocate multiple IRQs for a device"
---

<p>pci_alloc_irq_vectors &#8211; allocate multiple IRQs for a device</p>
<h2>Synopsis</h2>
<pre><code>int pci_alloc_irq_vectors(struct pci_dev *dev, unsigned int min_vecs, unsigned int max_vecs, unsigned int flags);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to operate on</dl>
<p> <i>min_vecs</i></p>
<dl>
<dd>minimum number of vectors required (must be &gt;= 1)</dl>
<p> <i>max_vecs</i></p>
<dl>
<dd>maximum (desired) number of vectors</dl>
<p> <i>flags</i></p>
<dl>
<dd>flags or quirks for the allocation</dl>
<h2>Description</h2>
<p>Allocate up to <i>max_vecs</i> interrupt vectors for <i>dev</i>, using MSI-X or MSI vectors if available, and fall back to a single legacy vector if neither is available. Return the number of vectors allocated, (which might be smaller than <i>max_vecs</i>) if successful, or a negative error code on error. If less than <i>min_vecs</i> interrupt vectors are available for <i>dev</i> the function will fail with -ENOSPC. </p>
<p> To get the Linux IRQ number used for a vector that can be passed to <code>request_irq</code> use the <code>pci_irq_vector</code> helper.</p>
<h2>Copyright</h2>
