---
title: "request_percpu_irq(9)"
name: "request_percpu_irq"
section: "9"
letter: "r"
url: "/docs/linux/man/9-request_percpu_irq/"
description: "request_percpu_irq – allocate a percpu interrupt line"
---

<p>request_percpu_irq &#8211; allocate a percpu interrupt line</p>
<h2>Synopsis</h2>
<pre><code>int request_percpu_irq(unsigned int irq, irq_handler_t handler, const char *devname, void __percpu *dev_id);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt line to allocate</dl>
<p> <i>handler</i></p>
<dl>
<dd>Function to be called when the IRQ occurs.</dl>
<p> <i>devname</i></p>
<dl>
<dd>An ascii name for the claiming device</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>A percpu cookie passed back to the handler function</dl>
<h2>Description</h2>
<p>This call allocates interrupt resources and enables the interrupt on the local CPU. If the interrupt is supposed to be enabled on other CPUs, it has to be done on each CPU using <code>enable_percpu_irq</code>. </p>
<p> Dev_id must be globally unique. It is a per-cpu variable, and the handler gets called with the interrupted CPU&#8217;s instance of that variable.</p>
<h2>Copyright</h2>
