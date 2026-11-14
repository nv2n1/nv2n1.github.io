---
title: "pci_find_ext_capability(9)"
name: "pci_find_ext_capability"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_find_ext_capability/"
description: "pci_find_ext_capability – Find an extended capability"
---

<p>pci_find_ext_capability &#8211; Find an extended capability</p>
<h2>Synopsis</h2>
<pre><code>int pci_find_ext_capability(struct pci_dev *dev, int cap);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>PCI device to query</dl>
<p> <i>cap</i></p>
<dl>
<dd>capability code</dl>
<h2>Description</h2>
<p>Returns the address of the requested extended capability structure within the device&#8217;s PCI configuration space or 0 if the device does not support it. Possible values for <i>cap</i>: </p>
<p> <code>PCI_EXT_CAP_ID_ERR</code> Advanced Error Reporting <code>PCI_EXT_CAP_ID_VC</code> Virtual Channel <code>PCI_EXT_CAP_ID_DSN</code> Device Serial Number <code>PCI_EXT_CAP_ID_PWR</code> Power Budgeting</p>
<h2>Copyright</h2>
