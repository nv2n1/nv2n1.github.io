---
title: "struct_irq_affinity_notify(9)"
name: "struct_irq_affinity_notify"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_affinity_notify/"
description: "struct_irq_affinity_notify – context for notification of IRQ affinity changes"
---

<p>struct_irq_affinity_notify &#8211; context for notification of IRQ affinity changes</p>
<h2>Synopsis</h2>
<pre><code>struct irq_affinity_notify {
    unsigned int irq;
    struct kref kref;
    struct work_struct work;
    void (*notify)(struct irq_affinity_notify *, const cpumask_t *mask);
    void (*release)(struct kref *ref);
};</code></pre>
<h2>Members</h2>
<p>irq</p>
<dl>
<dd>Interrupt to which notification applies</dl>
<p> kref</p>
<dl>
<dd>Reference count, for internal use</dl>
<p> work</p>
<dl>
<dd>Work item, for internal use</dl>
<p> notify</p>
<dl>
<dd>Function to be called on change. This will be called in process context.</dl>
<p> release</p>
<dl>
<dd>Function to be called on release. This will be called in process context. Once registered, the structure must only be freed when this function is called or later.</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
