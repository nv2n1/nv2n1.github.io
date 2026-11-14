---
title: "struct_rio_ops(9)"
name: "struct_rio_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_ops/"
description: "struct_rio_ops – Low-level RIO configuration space operations"
---

<p>struct_rio_ops &#8211; Low-level RIO configuration space operations</p>
<h2>Synopsis</h2>
<pre><code>struct rio_ops {
    int (*lcread)(struct rio_mport *mport, int index, u32 offset, int len, u32 *data);
    int (*lcwrite)(struct rio_mport *mport, int index, u32 offset, int len, u32 data);
    int (*cread)(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 *data);
    int (*cwrite)(struct rio_mport *mport, int index, u16 destid, u8 hopcount, u32 offset, int len, u32 data);
    int (*dsend)(struct rio_mport *mport, int index, u16 destid, u16 data);
    int (*pwenable)(struct rio_mport *mport, int enable);
    int (*open_outb_mbox)(struct rio_mport *mport, void *dev_id, int mbox, int entries);
    void (*close_outb_mbox)(struct rio_mport *mport, int mbox);
    int (*open_inb_mbox)(struct rio_mport *mport, void *dev_id, int mbox, int entries);
    void (*close_inb_mbox)(struct rio_mport *mport, int mbox);
    int (*add_outb_message)(struct rio_mport *mport, struct rio_dev *rdev, int mbox, void *buffer, size_t len);
    int (*add_inb_buffer)(struct rio_mport *mport, int mbox, void *buf);
    void *(*get_inb_message)(struct rio_mport *mport, int mbox);
    int (*map_inb)(struct rio_mport *mport, dma_addr_t lstart, u64 rstart, u64 size, u32 flags);
    void (*unmap_inb)(struct rio_mport *mport, dma_addr_t lstart);
    int (*query_mport)(struct rio_mport *mport, struct rio_mport_attr *attr);
    int (*map_outb)(struct rio_mport *mport, u16 destid, u64 rstart, u32 size, u32 flags, dma_addr_t *laddr);
    void (*unmap_outb)(struct rio_mport *mport, u16 destid, u64 rstart);
};</code></pre>
<h2>Members</h2>
<p>lcread</p>
<dl>
<dd>Callback to perform local (master port) read of config space.</dl>
<p> lcwrite</p>
<dl>
<dd>Callback to perform local (master port) write of config space.</dl>
<p> cread</p>
<dl>
<dd>Callback to perform network read of config space.</dl>
<p> cwrite</p>
<dl>
<dd>Callback to perform network write of config space.</dl>
<p> dsend</p>
<dl>
<dd>Callback to send a doorbell message.</dl>
<p> pwenable</p>
<dl>
<dd>Callback to enable/disable port-write message handling.</dl>
<p> open_outb_mbox</p>
<dl>
<dd>Callback to initialize outbound mailbox.</dl>
<p> close_outb_mbox</p>
<dl>
<dd>Callback to shut down outbound mailbox.</dl>
<p> open_inb_mbox</p>
<dl>
<dd>Callback to initialize inbound mailbox.</dl>
<p> close_inb_mbox</p>
<dl>
<dd>Callback to shut down inbound mailbox.</dl>
<p> add_outb_message</p>
<dl>
<dd>Callback to add a message to an outbound mailbox queue.</dl>
<p> add_inb_buffer</p>
<dl>
<dd>Callback to add a buffer to an inbound mailbox queue.</dl>
<p> get_inb_message</p>
<dl>
<dd>Callback to get a message from an inbound mailbox queue.</dl>
<p> map_inb</p>
<dl>
<dd>Callback to map RapidIO address region into local memory space.</dl>
<p> unmap_inb</p>
<dl>
<dd>Callback to unmap RapidIO address region mapped with <code>map_inb</code>.</dl>
<p> query_mport</p>
<dl>
<dd>Callback to query mport device attributes.</dl>
<p> map_outb</p>
<dl>
<dd>Callback to map outbound address region into local memory space.</dl>
<p> unmap_outb</p>
<dl>
<dd>Callback to unmap outbound RapidIO address region.</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
