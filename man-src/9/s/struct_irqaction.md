---
title: "struct_irqaction(9)"
name: "struct_irqaction"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irqaction/"
description: "struct_irqaction – per interrupt action descriptor"
---

<p>struct_irqaction &#8211; per interrupt action descriptor</p>
<h2>Synopsis</h2>
<pre><code>struct irqaction {
    irq_handler_t handler;
    void *dev_id;
    void __percpu *percpu_dev_id;
    struct irqaction *next;
    irq_handler_t thread_fn;
    struct task_struct *thread;
    struct irqaction *secondary;
    unsigned int irq;
    unsigned int flags;
    unsigned long thread_flags;
    unsigned long thread_mask;
    const char *name;
    struct proc_dir_entry *dir;
};</code></pre>
<h2>Members</h2>
<p>handler</p>
<dl>
<dd>interrupt handler function</dd></dl>
<p> dev_id</p>
<dl>
<dd>cookie to identify the device</dd></dl>
<p> percpu_dev_id</p>
<dl>
<dd>cookie to identify the device</dd></dl>
<p> next</p>
<dl>
<dd>pointer to the next irqaction for shared interrupts</dd></dl>
<p> thread_fn</p>
<dl>
<dd>interrupt handler function for threaded interrupts</dd></dl>
<p> thread</p>
<dl>
<dd>thread pointer for threaded interrupts</dd></dl>
<p> secondary</p>
<dl>
<dd>pointer to secondary irqaction (force threading)</dd></dl>
<p> irq</p>
<dl>
<dd>interrupt number</dd></dl>
<p> flags</p>
<dl>
<dd>flags (see IRQF_* above)</dd></dl>
<p> thread_flags</p>
<dl>
<dd>flags related to <i>thread</i></dd></dl>
<p> thread_mask</p>
<dl>
<dd>bitmask for keeping track of <i>thread</i> activity</dd></dl>
<p> name</p>
<dl>
<dd>name of the device</dd></dl>
<p> dir</p>
<dl>
<dd>pointer to the proc/irq/NN/name entry</dd></dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
