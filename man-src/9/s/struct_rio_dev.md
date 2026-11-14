---
title: "struct_rio_dev(9)"
name: "struct_rio_dev"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_dev/"
description: "struct_rio_dev – RIO device info"
---

<p>struct_rio_dev &#8211; RIO device info</p>
<h2>Synopsis</h2>
<pre><code>struct rio_dev {
    struct list_head global_list;
    struct list_head net_list;
    struct rio_net *net;
    bool do_enum;
    u16 did;
    u16 vid;
    u32 device_rev;
    u16 asm_did;
    u16 asm_vid;
    u16 asm_rev;
    u16 efptr;
    u32 pef;
    u32 swpinfo;
    u32 src_ops;
    u32 dst_ops;
    u32 comp_tag;
    u32 phys_efptr;
    u32 phys_rmap;
    u32 em_efptr;
    u64 dma_mask;
    struct rio_driver *driver;
    struct device dev;
    struct resource riores[RIO_MAX_DEV_RESOURCES];
    int (*pwcback)(struct rio_dev *rdev, union rio_pw_msg *msg, int step);
    u16 destid;
    u8 hopcount;
    struct rio_dev *prev;
    atomic_t state;
    struct rio_switch rswitch[0];
};</code></pre>
<h2>Members</h2>
<p>global_list</p>
<dl>
<dd>Node in list of all RIO devices</dl>
<p> net_list</p>
<dl>
<dd>Node in list of RIO devices in a network</dl>
<p> net</p>
<dl>
<dd>Network this device is a part of</dl>
<p> do_enum</p>
<dl>
<dd>Enumeration flag</dl>
<p> did</p>
<dl>
<dd>Device ID</dl>
<p> vid</p>
<dl>
<dd>Vendor ID</dl>
<p> device_rev</p>
<dl>
<dd>Device revision</dl>
<p> asm_did</p>
<dl>
<dd>Assembly device ID</dl>
<p> asm_vid</p>
<dl>
<dd>Assembly vendor ID</dl>
<p> asm_rev</p>
<dl>
<dd>Assembly revision</dl>
<p> efptr</p>
<dl>
<dd>Extended feature pointer</dl>
<p> pef</p>
<dl>
<dd>Processing element features</dl>
<p> swpinfo</p>
<dl>
<dd>Switch port info</dl>
<p> src_ops</p>
<dl>
<dd>Source operation capabilities</dl>
<p> dst_ops</p>
<dl>
<dd>Destination operation capabilities</dl>
<p> comp_tag</p>
<dl>
<dd>RIO component tag</dl>
<p> phys_efptr</p>
<dl>
<dd>RIO device extended features pointer</dl>
<p> phys_rmap</p>
<dl>
<dd>LP-Serial Register Map Type (1 or 2)</dl>
<p> em_efptr</p>
<dl>
<dd>RIO Error Management features pointer</dl>
<p> dma_mask</p>
<dl>
<dd>Mask of bits of RIO address this device implements</dl>
<p> driver</p>
<dl>
<dd>Driver claiming this device</dl>
<p> dev</p>
<dl>
<dd>Device model device</dl>
<p> riores[RIO_MAX_DEV_RESOURCES]</p>
<dl>
<dd>RIO resources this device owns</dl>
<p> pwcback</p>
<dl>
<dd>port-write callback function for this device</dl>
<p> destid</p>
<dl>
<dd>Network destination ID (or associated destid for switch)</dl>
<p> hopcount</p>
<dl>
<dd>Hopcount to this device</dl>
<p> prev</p>
<dl>
<dd>Previous RIO device connected to the current one</dl>
<p> state</p>
<dl>
<dd>device state</dl>
<p> rswitch[0]</p>
<dl>
<dd>struct rio_switch (if valid for this device)</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
