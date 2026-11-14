---
title: "pci_msi_create_irq_domain(9)"
name: "pci_msi_create_irq_domain"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_msi_create_irq_domain/"
---

pci_msi_create_irq_domain - Create a MSI interrupt domain

<h2>Synopsis</h2>

<pre><code>struct irq_domain *pci_msi_create_irq_domain(struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent);</code></pre>

<h2>Arguments</h2>

<i>fwnode</i>
<dl><dd><dd>Optional fwnode of the interrupt controller</dl>
 

 <i>info</i>
<dl><dd>MSI domain info</dl>
 

 <i>parent</i>
<dl><dd>Parent irq domain</dl>

<h2>Description</h2>

Updates the domain and chip ops and creates a MSI interrupt domain.

<h2>Return</h2>

A domain pointer or NULL in case of failure.

<h2>Copyright</h2>


