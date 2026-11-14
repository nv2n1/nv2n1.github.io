---
title: "struct_iio_trigger(9)"
name: "struct_iio_trigger"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_trigger/"
description: "struct_iio_trigger – industrial I/O trigger device"
---

<p>struct_iio_trigger &#8211; industrial I/O trigger device</p>
<h2>Synopsis</h2>
<pre><code>struct iio_trigger {
    const struct iio_trigger_ops *ops;
    int id;
    const char *name;
    struct device dev;
    struct list_head list;
    struct list_head alloc_list;
    atomic_t use_count;
    struct irq_chip subirq_chip;
    int subirq_base;
    struct iio_subirq subirqs[CONFIG_IIO_CONSUMERS_PER_TRIGGER];
    unsigned long pool[BITS_TO_LONGS(CONFIG_IIO_CONSUMERS_PER_TRIGGER)];
    struct mutex pool_lock;
    bool attached_own_device;
};</code></pre>
<h2>Members</h2>
<p>ops</p>
<dl>
<dd>[DRIVER] operations structure</dl>
<p> id</p>
<dl>
<dd>[INTERN] unique id number</dl>
<p> name</p>
<dl>
<dd>[DRIVER] unique name</dl>
<p> dev</p>
<dl>
<dd>[DRIVER] associated device (if relevant)</dl>
<p> list</p>
<dl>
<dd>[INTERN] used in maintenance of global trigger list</dl>
<p> alloc_list</p>
<dl>
<dd>[DRIVER] used for driver specific trigger list</dl>
<p> use_count</p>
<dl>
<dd>use count for the trigger</dl>
<p> subirq_chip</p>
<dl>
<dd>[INTERN] associate &#8216;virtual&#8217; irq chip.</dl>
<p> subirq_base</p>
<dl>
<dd>[INTERN] base number for irqs provided by trigger.</dl>
<p> subirqs[CONFIG_IIO_CONSUMERS_PER_TRIGGER]</p>
<dl>
<dd>[INTERN] information about the &#8216;child&#8217; irqs.</dl>
<p> pool[BITS_TO_LONGS(CONFIG_IIO_CONSUMERS_PER_TRIGGER)]</p>
<dl>
<dd>[INTERN] bitmap of irqs currently in use.</dl>
<p> pool_lock</p>
<dl>
<dd>[INTERN] protection of the irq pool.</dl>
<p> attached_own_device</p>
<dl>
<dd>[INTERN] if we are using our own device as trigger, i.e. if we registered a poll function to the same device as the one providing the trigger.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
