---
title: "struct_rio_dbell(9)"
name: "struct_rio_dbell"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_dbell/"
description: "struct_rio_dbell – RIO doorbell event"
---

<p>struct_rio_dbell &#8211; RIO doorbell event</p>
<h2>Synopsis</h2>
<pre><code>struct rio_dbell {
    struct list_head node;
    struct resource *res;
    void (*dinb)(struct rio_mport *mport, void *dev_id, u16 src, u16 dst, u16 info);
    void *dev_id;
};</code></pre>
<h2>Members</h2>
<p>node</p>
<dl>
<dd>Node in list of doorbell events</dl>
<p> res</p>
<dl>
<dd>Doorbell resource</dl>
<p> dinb</p>
<dl>
<dd>Doorbell event callback</dl>
<p> dev_id</p>
<dl>
<dd>Device specific pointer to pass on event</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
