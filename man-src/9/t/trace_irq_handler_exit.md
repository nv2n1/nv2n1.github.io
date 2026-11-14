---
title: "trace_irq_handler_exit(9)"
name: "trace_irq_handler_exit"
section: "9"
letter: "t"
url: "/docs/linux/man/9-trace_irq_handler_exit/"
description: "trace_irq_handler_exit – called immediately after the irq action handler returns"
---

<p>trace_irq_handler_exit &#8211; called immediately after the irq action handler returns</p>
<h2>Synopsis</h2>
<pre><code>void trace_irq_handler_exit(int irq, struct irqaction *action, int ret);</code></pre>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>irq number</dl>
<p> <i>action</i></p>
<dl>
<dd>pointer to struct irqaction</dl>
<p> <i>ret</i></p>
<dl>
<dd>return value</dl>
<h2>Description</h2>
<p>If the <i>ret</i> value is set to IRQ_HANDLED, then we know that the corresponding <i>action</i>-&gt;handler successfully handled this irq. Otherwise, the irq might be a shared irq line, or the irq was not handled successfully. Can be used in conjunction with the irq_handler_entry to understand irq handler latencies.</p>
<h2>Authors</h2>
<p><code>Jason Baron</code> &lt;jbaron [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>William Cohen</code> &lt;wcohen [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
