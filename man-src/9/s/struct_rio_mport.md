---
title: "struct_rio_mport(9)"
name: "struct_rio_mport"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_mport/"
description: "struct_rio_mport – RIO master port info"
---

<p>struct_rio_mport &#8211; RIO master port info</p>
<h2>Synopsis</h2>
<pre><code>struct rio_mport {
    struct list_head dbells;
    struct list_head pwrites;
    struct list_head node;
    struct list_head nnode;
    struct rio_net *net;
    struct mutex lock;
    struct resource iores;
    struct resource riores[RIO_MAX_MPORT_RESOURCES];
    struct rio_msg inb_msg[RIO_MAX_MBOX];
    struct rio_msg outb_msg[RIO_MAX_MBOX];
    int host_deviceid;
    struct rio_ops *ops;
    unsigned char id;
    unsigned char index;
    unsigned int sys_size;
    u32 phys_efptr;
    u32 phys_rmap;
    unsigned char name[RIO_MAX_MPORT_NAME];
    struct device dev;
    void *priv;
#ifdef CONFIG_RAPIDIO_DMA_ENGINE
    struct dma_device dma;
#endif
    struct rio_scan *nscan;
    atomic_t state;
    unsigned int pwe_refcnt;
};</code></pre>
<h2>Members</h2>
<p>dbells</p>
<dl>
<dd>List of doorbell events</dl>
<p> pwrites</p>
<dl>
<dd>List of portwrite events</dl>
<p> node</p>
<dl>
<dd>Node in global list of master ports</dl>
<p> nnode</p>
<dl>
<dd>Node in network list of master ports</dl>
<p> net</p>
<dl>
<dd>RIO net this mport is attached to</dl>
<p> lock</p>
<dl>
<dd>lock to synchronize lists manipulations</dl>
<p> iores</p>
<dl>
<dd>I/O mem resource that this master port interface owns</dl>
<p> riores[RIO_MAX_MPORT_RESOURCES]</p>
<dl>
<dd>RIO resources that this master port interfaces owns</dl>
<p> inb_msg[RIO_MAX_MBOX]</p>
<dl>
<dd>RIO inbound message event descriptors</dl>
<p> outb_msg[RIO_MAX_MBOX]</p>
<dl>
<dd>RIO outbound message event descriptors</dl>
<p> host_deviceid</p>
<dl>
<dd>Host device ID associated with this master port</dl>
<p> ops</p>
<dl>
<dd>configuration space functions</dl>
<p> id</p>
<dl>
<dd>Port ID, unique among all ports</dl>
<p> index</p>
<dl>
<dd>Port index, unique among all port interfaces of the same type</dl>
<p> sys_size</p>
<dl>
<dd>RapidIO common transport system size</dl>
<p> phys_efptr</p>
<dl>
<dd>RIO port extended features pointer</dl>
<p> phys_rmap</p>
<dl>
<dd>LP-Serial EFB Register Mapping type (1 or 2).</dl>
<p> name[RIO_MAX_MPORT_NAME]</p>
<dl>
<dd>Port name string</dl>
<p> dev</p>
<dl>
<dd>device structure associated with an mport</dl>
<p> priv</p>
<dl>
<dd>Master port private data</dl>
<p> dma</p>
<dl>
<dd>DMA device associated with mport</dl>
<p> nscan</p>
<dl>
<dd>RapidIO network enumeration/discovery operations</dl>
<p> state</p>
<dl>
<dd>mport device state</dl>
<p> pwe_refcnt</p>
<dl>
<dd>port-write enable ref counter to track enable/disable requests</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
