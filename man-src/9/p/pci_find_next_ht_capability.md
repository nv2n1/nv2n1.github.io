---
title: "pci_find_next_ht_capability(9)"
name: "pci_find_next_ht_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_next_ht_capability/"
description: "pci_find_next_ht_capability – query a device’s Hypertransport capabilities"
---

<p>pci_find_next_ht_capability &#8211; query a device&#8217;s Hypertransport capabilities</p>
<h2>Synopsis</h2>
<pre><code>int pci_find_next_ht_capability(struct pci_dev *dev, int pos, int ht_cap);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to query</dl>
<p> <i>pos</i></p>
<dl>
<dd>Position from which to continue searching</dl>
<p> <i>ht_cap</i></p>
<dl>
<dd>Hypertransport capability code</dl>
<h2>Description</h2>
<p>To be used in conjunction with <code>pci_find_ht_capability</code> to search for all capabilities matching <i>ht_cap</i>. <i>pos</i> should always be a value returned from <code>pci_find_ht_capability</code>. </p>
<p> NB. To be 100% safe against broken PCI devices, the caller should take steps to avoid an infinite loop.</p>
<h2>Copyright</h2>
