---
title: "pci_bus_alloc_resource(9)"
name: "pci_bus_alloc_resource"
section: "9"
letter: "p"
url: "/docs/linux/man/9-pci_bus_alloc_resource/"
---

pci_bus_alloc_resource - allocate a resource from a parent bus

<h2>Synopsis</h2>

<pre><code>int pci_bus_alloc_resource(struct pci_bus *bus, struct resource *res, resource_size_t size, resource_size_t align, resource_size_t min, unsigned long type_mask, resource_size_t (*alignf)(void *, const struct resource *, resource_size_t, resource_size_t), void *alignf_data);</code></pre>

<h2>Arguments</h2>

<i>bus</i>
<dl><dd><dd>PCI bus</dl>
 

 <i>res</i>
<dl><dd>resource to allocate</dl>
 

 <i>size</i>
<dl><dd>size of resource to allocate</dl>
 

 <i>align</i>
<dl><dd>alignment of resource to allocate</dl>
 

 <i>min</i>
<dl><dd>minimum /proc/iomem address to allocate</dl>
 

 <i>type_mask</i>
<dl><dd>IORESOURCE_* type flags</dl>
 

 <i>alignf</i>
<dl><dd>resource alignment function</dl>
 

 <i>alignf_data</i>
<dl><dd>data argument for resource alignment function</dl>

<h2>Description</h2>

Given the PCI bus a device resides on, the size, minimum address, alignment and type, try to find an acceptable resource allocation for a specific device resource.

<h2>Copyright</h2>


