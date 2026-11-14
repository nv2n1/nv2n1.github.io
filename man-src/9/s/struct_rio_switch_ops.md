---
title: "struct_rio_switch_ops(9)"
name: "struct_rio_switch_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_switch_ops/"
description: "struct_rio_switch_ops – Per-switch operations"
---

<p>struct_rio_switch_ops &#8211; Per-switch operations</p>
<h2>Synopsis</h2>
<pre><code>struct rio_switch_ops {
    struct module *owner;
    int (*add_entry)(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 route_port);
    int (*get_entry)(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 *route_port);
    int (*clr_table)(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table);
    int (*set_domain)(struct rio_mport *mport, u16 destid, u8 hopcount, u8 sw_domain);
    int (*get_domain)(struct rio_mport *mport, u16 destid, u8 hopcount, u8 *sw_domain);
    int (*em_init)(struct rio_dev *dev);
    int (*em_handle)(struct rio_dev *dev, u8 swport);
};</code></pre>
<h2>Members</h2>
<p>owner</p>
<dl>
<dd>The module owner of this structure</dl>
<p> add_entry</p>
<dl>
<dd>Callback for switch-specific route add function</dl>
<p> get_entry</p>
<dl>
<dd>Callback for switch-specific route get function</dl>
<p> clr_table</p>
<dl>
<dd>Callback for switch-specific clear route table function</dl>
<p> set_domain</p>
<dl>
<dd>Callback for switch-specific domain setting function</dl>
<p> get_domain</p>
<dl>
<dd>Callback for switch-specific domain get function</dl>
<p> em_init</p>
<dl>
<dd>Callback for switch-specific error management init function</dl>
<p> em_handle</p>
<dl>
<dd>Callback for switch-specific error management handler function</dl>
<h2>Description</h2>
<p>Defines the operations that are necessary to initialize/control a particular RIO switch device.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
