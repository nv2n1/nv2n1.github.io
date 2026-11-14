---
title: "struct_irq_chip(9)"
name: "struct_irq_chip"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irq_chip/"
description: "struct_irq_chip – hardware interrupt chip descriptor"
---

<p>struct_irq_chip &#8211; hardware interrupt chip descriptor</p>
<h2>Synopsis</h2>
<pre><code>struct irq_chip {
    struct device *parent_device;
    const char *name;
    unsigned int (*irq_startup)(struct irq_data *data);
    void (*irq_shutdown)(struct irq_data *data);
    void (*irq_enable)(struct irq_data *data);
    void (*irq_disable)(struct irq_data *data);
    void (*irq_ack)(struct irq_data *data);
    void (*irq_mask)(struct irq_data *data);
    void (*irq_mask_ack)(struct irq_data *data);
    void (*irq_unmask)(struct irq_data *data);
    void (*irq_eoi)(struct irq_data *data);
    int (*irq_set_affinity)(struct irq_data *data, const struct cpumask *dest, bool force);
    int (*irq_retrigger)(struct irq_data *data);
    int (*irq_set_type)(struct irq_data *data, unsigned int flow_type);
    int (*irq_set_wake)(struct irq_data *data, unsigned int on);
    void (*irq_bus_lock)(struct irq_data *data);
    void (*irq_bus_sync_unlock)(struct irq_data *data);
    void (*irq_cpu_online)(struct irq_data *data);
    void (*irq_cpu_offline)(struct irq_data *data);
    void (*irq_suspend)(struct irq_data *data);
    void (*irq_resume)(struct irq_data *data);
    void (*irq_pm_shutdown)(struct irq_data *data);
    void (*irq_calc_mask)(struct irq_data *data);
    void (*irq_print_chip)(struct irq_data *data, struct seq_file *p);
    int (*irq_request_resources)(struct irq_data *data);
    void (*irq_release_resources)(struct irq_data *data);
    void (*irq_compose_msi_msg)(struct irq_data *data, struct msi_msg *msg);
    void (*irq_write_msi_msg)(struct irq_data *data, struct msi_msg *msg);
    int (*irq_get_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool *state);
    int (*irq_set_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool state);
    int (*irq_set_vcpu_affinity)(struct irq_data *data, void *vcpu_info);
    void (*ipi_send_single)(struct irq_data *data, unsigned int cpu);
    void (*ipi_send_mask)(struct irq_data *data, const struct cpumask *dest);
    unsigned long flags;
};</code></pre>
<h2>Members</h2>
<p>parent_device</p>
<dl>
<dd>pointer to parent device for irqchip</dl>
<p> name</p>
<dl>
<dd>name for /proc/interrupts</dl>
<p> irq_startup</p>
<dl>
<dd>start up the interrupt (defaults to -&gt;enable if NULL)</dl>
<p> irq_shutdown</p>
<dl>
<dd>shut down the interrupt (defaults to -&gt;disable if NULL)</dl>
<p> irq_enable</p>
<dl>
<dd>enable the interrupt (defaults to chip-&gt;unmask if NULL)</dl>
<p> irq_disable</p>
<dl>
<dd>disable the interrupt</dl>
<p> irq_ack</p>
<dl>
<dd>start of a new interrupt</dl>
<p> irq_mask</p>
<dl>
<dd>mask an interrupt source</dl>
<p> irq_mask_ack</p>
<dl>
<dd>ack and mask an interrupt source</dl>
<p> irq_unmask</p>
<dl>
<dd>unmask an interrupt source</dl>
<p> irq_eoi</p>
<dl>
<dd>end of interrupt</dl>
<p> irq_set_affinity</p>
<dl>
<dd>set the CPU affinity on SMP machines</dl>
<p> irq_retrigger</p>
<dl>
<dd>resend an IRQ to the CPU</dl>
<p> irq_set_type</p>
<dl>
<dd>set the flow type (IRQ_TYPE_LEVEL/etc.) of an IRQ</dl>
<p> irq_set_wake</p>
<dl>
<dd>enable/disable power-management wake-on of an IRQ</dl>
<p> irq_bus_lock</p>
<dl>
<dd>function to lock access to slow bus (i2c) chips</dl>
<p> irq_bus_sync_unlock</p>
<dl>
<dd>function to sync and unlock slow bus (i2c) chips</dl>
<p> irq_cpu_online</p>
<dl>
<dd>configure an interrupt source for a secondary CPU</dl>
<p> irq_cpu_offline</p>
<dl>
<dd>un-configure an interrupt source for a secondary CPU</dl>
<p> irq_suspend</p>
<dl>
<dd>function called from core code on suspend once per chip, when one or more interrupts are installed</dl>
<p> irq_resume</p>
<dl>
<dd>function called from core code on resume once per chip, when one ore more interrupts are installed</dl>
<p> irq_pm_shutdown</p>
<dl>
<dd>function called from core code on shutdown once per chip</dl>
<p> irq_calc_mask</p>
<dl>
<dd>Optional function to set irq_data.mask for special cases</dl>
<p> irq_print_chip</p>
<dl>
<dd>optional to print special chip info in show_interrupts</dl>
<p> irq_request_resources</p>
<dl>
<dd>optional to request resources before calling any other callback related to this irq</dl>
<p> irq_release_resources</p>
<dl>
<dd>optional to release resources acquired with irq_request_resources</dl>
<p> irq_compose_msi_msg</p>
<dl>
<dd>optional to compose message content for MSI</dl>
<p> irq_write_msi_msg</p>
<dl>
<dd>optional to write message content for MSI</dl>
<p> irq_get_irqchip_state</p>
<dl>
<dd>return the internal state of an interrupt</dl>
<p> irq_set_irqchip_state</p>
<dl>
<dd>set the internal state of a interrupt</dl>
<p> irq_set_vcpu_affinity</p>
<dl>
<dd>optional to target a vCPU in a virtual machine</dl>
<p> ipi_send_single</p>
<dl>
<dd>send a single IPI to destination cpus</dl>
<p> ipi_send_mask</p>
<dl>
<dd>send an IPI to destination cpus in cpumask</dl>
<p> flags</p>
<dl>
<dd>chip specific flags</dl>
<h2>Authors</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Ingo Molnar</code> &lt;mingo [at] elte.hu&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
