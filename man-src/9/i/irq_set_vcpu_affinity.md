---
title: "irq_set_vcpu_affinity(9)"
name: "irq_set_vcpu_affinity"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_set_vcpu_affinity/"
description: "irq_set_vcpu_affinity – Set vcpu affinity for the interrupt"
---

<p>irq_set_vcpu_affinity &#8211; Set vcpu affinity for the interrupt</p>
<h2>Synopsis</h2>
<pre><code>int irq_set_vcpu_affinity(unsigned int irq, void *vcpu_info);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>interrupt number to set affinity</dl>
<p> <i>vcpu_info</i></p>
<dl>
<dd>vCPU specific data</dl>
<h2>Description</h2>
<p>This function uses the vCPU specific data to set the vCPU affinity for an irq. The vCPU specific data is passed from outside, such as KVM. One example code path is as below: KVM -&gt; IOMMU -&gt; <code>irq_set_vcpu_affinity</code>.</p>
<h2>Copyright</h2>
