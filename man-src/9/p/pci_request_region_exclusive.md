---
title: "pci_request_region_exclusive(9)"
name: "pci_request_region_exclusive"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_request_region_exclusive/"
description: "pci_request_region_exclusive – Reserved PCI I/O and memory resource"
---

<p>pci_request_region_exclusive &#8211; Reserved PCI I/O and memory resource</p>
<h2>Synopsis</h2>
<pre><code>int pci_request_region_exclusive(struct pci_dev *pdev, int bar, const char *res_name);</code></pre>
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
<dd>Name to be associated with resource.</dl>
<h2>Description</h2>
<p>Mark the PCI region associated with PCI device <i>pdev</i> BR <i>bar</i> as being reserved by owner <i>res_name</i>. Do not access any address inside the PCI regions unless this call returns successfully. </p>
<p> Returns 0 on success, or <code>EBUSY</code> on error. A warning message is also printed on failure. </p>
<p> The key difference that _exclusive makes it that userspace is explicitly not allowed to map the resource via /dev/mem or sysfs.</p>
<h2>Copyright</h2>
