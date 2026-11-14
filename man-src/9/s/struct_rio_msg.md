---
title: "struct_rio_msg(9)"
name: "struct_rio_msg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_msg/"
description: "struct_rio_msg – RIO message event"
---

<p>struct_rio_msg &#8211; RIO message event</p>
<h2>Synopsis</h2>
<pre><code>struct rio_msg {
    struct resource *res;
    void (*mcback)(struct rio_mport *mport, void *dev_id, int mbox, int slot);
};</code></pre>
<h2>Members</h2>
<p>res</p>
<dl>
<dd>Mailbox resource</dl>
<p> mcback</p>
<dl>
<dd>Message event callback</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
