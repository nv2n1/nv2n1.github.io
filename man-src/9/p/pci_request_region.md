---
title: "pci_request_region(9)"
name: "pci_request_region"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_request_region/"
description: "pci_request_region – Reserve PCI I/O and memory resource"
---

<p>pci_request_region &#8211; Reserve PCI I/O and memory resource</p>
<h2>Synopsis</h2>
<pre><code>int pci_request_region(struct pci_dev *pdev, int bar, const char *res_name);</code></pre>
<h2>Arguments</h2>
<p><i>pdev</i></p>
<dl>
<dd>
<dd>PCI device whose resources are to be reserved</dl>
<p> <i>bar</i></p>
<dl>
<dd>BAR to be reserved</dl>
<p> <i>res_name</i></p>
<dl>
<dd>Name to be associated with resource</dl>
<h2>Description</h2>
<p>Mark the PCI region associated with PCI device <i>pdev</i> BAR <i>bar</i> as being reserved by owner <i>res_name</i>. Do not access any address inside the PCI regions unless this call returns successfully. </p>
<p> Returns 0 on success, or <code>EBUSY</code> on error. A warning message is also printed on failure.</p>
<h2>Copyright</h2>
