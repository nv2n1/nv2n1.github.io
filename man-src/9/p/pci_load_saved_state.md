---
title: "pci_load_saved_state(9)"
name: "pci_load_saved_state"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_load_saved_state/"
description: "pci_load_saved_state – Reload the provided save state into struct pci_dev."
---

<p>pci_load_saved_state &#8211; Reload the provided save state into struct pci_dev.</p>
<h2>Synopsis</h2>
<pre><code>int pci_load_saved_state(struct pci_dev *dev, struct pci_saved_state *state);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device that we&#8217;re dealing with</dl>
<p> <i>state</i></p>
<dl>
<dd>Saved state returned from <code>pci_store_saved_state</code></dl>
<h2>Copyright</h2>
