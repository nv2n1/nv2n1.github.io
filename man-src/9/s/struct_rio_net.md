---
title: "struct_rio_net(9)"
name: "struct_rio_net"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_net/"
description: "struct_rio_net – RIO network info"
---

<p>struct_rio_net &#8211; RIO network info</p>
<h2>Synopsis</h2>
<pre><code>struct rio_net {
    struct list_head node;
    struct list_head devices;
    struct list_head switches;
    struct list_head mports;
    struct rio_mport *hport;
    unsigned char id;
    struct device dev;
    void *enum_data;
    void (*release)(struct rio_net *net);
};</code></pre>
<h2>Members</h2>
<p>node</p>
<dl>
<dd>Node in global list of RIO networks</dl>
<p> devices</p>
<dl>
<dd>List of devices in this network</dl>
<p> switches</p>
<dl>
<dd>List of switches in this network</dl>
<p> mports</p>
<dl>
<dd>List of master ports accessing this network</dl>
<p> hport</p>
<dl>
<dd>Default port for accessing this network</dl>
<p> id</p>
<dl>
<dd>RIO network ID</dl>
<p> dev</p>
<dl>
<dd>Device object</dl>
<p> enum_data</p>
<dl>
<dd>private data specific to a network enumerator</dl>
<p> release</p>
<dl>
<dd>enumerator-specific release callback</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
