---
title: "pci_cfg_access_trylock(9)"
name: "pci_cfg_access_trylock"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_cfg_access_trylock/"
description: "pci_cfg_access_trylock – try to lock PCI config reads/writes"
---

<p>pci_cfg_access_trylock &#8211; try to lock PCI config reads/writes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool pci_cfg_access_trylock(struct pci_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>pci device struct</dl>
<h2>Description</h2>
<p>Same as pci_cfg_access_lock, but will return 0 if access is already locked, 1 otherwise. This function can be used from atomic contexts.</p>
<h2>Copyright</h2>
