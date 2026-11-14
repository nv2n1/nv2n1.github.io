---
title: "pci_wait_for_pending_transaction(9)"
name: "pci_wait_for_pending_transaction"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_wait_for_pending_transaction/"
---

pci_wait_for_pending_transaction - waits for pending transaction

<h2>Synopsis</h2>

<pre><code>int pci_wait_for_pending_transaction(struct pci_dev *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>the PCI device to operate on</dl>

<h2>Description</h2>

Return 0 if transaction is pending 1 otherwise.

<h2>Copyright</h2>


