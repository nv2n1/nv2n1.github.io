---
title: "struct_rio_driver(9)"
name: "struct_rio_driver"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_driver/"
description: "struct_rio_driver – RIO driver info"
---

<p>struct_rio_driver &#8211; RIO driver info</p>
<h2>Synopsis</h2>
<pre><code>struct rio_driver {
    struct list_head node;
    char *name;
    const struct rio_device_id *id_table;
    int (*probe)(struct rio_dev *dev, const struct rio_device_id *id);
    void (*remove)(struct rio_dev *dev);
    void (*shutdown)(struct rio_dev *dev);
    int (*suspend)(struct rio_dev *dev, u32 state);
    int (*resume)(struct rio_dev *dev);
    int (*enable_wake)(struct rio_dev *dev, u32 state, int enable);
    struct device_driver driver;
};</code></pre>
<h2>Members</h2>
<p>node</p>
<dl>
<dd>Node in list of drivers</dl>
<p> name</p>
<dl>
<dd>RIO driver name</dl>
<p> id_table</p>
<dl>
<dd>RIO device ids to be associated with this driver</dl>
<p> probe</p>
<dl>
<dd>RIO device inserted</dl>
<p> remove</p>
<dl>
<dd>RIO device removed</dl>
<p> shutdown</p>
<dl>
<dd>shutdown notification callback</dl>
<p> suspend</p>
<dl>
<dd>RIO device suspended</dl>
<p> resume</p>
<dl>
<dd>RIO device awakened</dl>
<p> enable_wake</p>
<dl>
<dd>RIO device enable wake event</dl>
<p> driver</p>
<dl>
<dd>LDM driver struct</dl>
<h2>Description</h2>
<p>Provides info on a RIO device driver for insertion/removal and power management purposes.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
