---
title: "trace_irq_handler_entry(9)"
name: "trace_irq_handler_entry"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_irq_handler_entry/"
description: "trace_irq_handler_entry – called immediately before the irq action handler"
---

<p>trace_irq_handler_entry &#8211; called immediately before the irq action handler</p>
<h2>Synopsis</h2>
<pre><code>void trace_irq_handler_entry(int irq, struct irqaction *action);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>irq number</dl>
<p> <i>action</i></p>
<dl>
<dd>pointer to struct irqaction</dl>
<h2>Description</h2>
<p>The struct irqaction pointed to by <i>action</i> contains various information about the handler, including the device name, <i>action</i>-&gt;name, and the device id, <i>action</i>-&gt;dev_id. When used in conjunction with the irq_handler_exit tracepoint, we can figure out irq handler latencies.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
