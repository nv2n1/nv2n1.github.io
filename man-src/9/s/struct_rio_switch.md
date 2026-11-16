---
title: "struct_rio_switch(9)"
name: "struct_rio_switch"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_switch/"
description: "struct_rio_switch – RIO switch info"
---

<p>struct_rio_switch &#8211; RIO switch info</p>
<h2>Synopsis</h2>
<pre><code>struct rio_switch {
    struct list_head node;
    u8 *route_table;
    u32 port_ok;
    struct rio_switch_ops *ops;
    spinlock_t lock;
    struct rio_dev *nextdev[0];
};</code></pre>
<h2>Members</h2>
<p>node</p>
<dl>
<dd>Node in global list of switches</dd></dl>
<p> route_table</p>
<dl>
<dd>Copy of switch routing table</dd></dl>
<p> port_ok</p>
<dl>
<dd>Status of each port (one bit per port) &#8211; OK=1 or UNINIT=0</dd></dl>
<p> ops</p>
<dl>
<dd>pointer to switch-specific operations</dd></dl>
<p> lock</p>
<dl>
<dd>lock to serialize operations updates</dd></dl>
<p> nextdev[0]</p>
<dl>
<dd>Array of per-port pointers to the next attached device</dd></dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Copyright</h2>
