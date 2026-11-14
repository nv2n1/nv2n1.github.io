---
title: "ipx_internal_net(8)"
name: "ipx_internal_net"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipx_internal_net/"
description: "ipx_internal_net – add or delete the IPX internal network"
---

<p>ipx_internal_net &#8211; add or delete the IPX internal network</p>
<h2>Synopsis</h2>
<p><code>ipx_internal_net</code> add network_number node_number </p>
<p> <code>ipx_internal_net</code> del</p>
<h2>Description</h2>
<p><code>ipx_internal_net</code> adds or deletes the IPX internal network. An IPX internal network is a special kind of IPX interface that does not have a physical device or frame type. It is used to provide a route-independent address for service providers. Internal networks are optional; however, when one is present it is also the Primary Interface. There can only be one internal network per host.</p>
<h3>Options</h3>
<dl>
<dt><i>add</i></p>
<dd>This option is used to create the IPX internal network.</p>
<dt><i>del</i></p>
<dd>This option is used to delete the IPX internal network.</dl>
<h2>Files</h2>
<p><i>/proc/net/ipx_interface /proc/net/ipx_route</i></p>
<h2>Bugs</h2>
<p>This functionality really belongs in <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8).</code></p>
<h2>Author</h2>
<p>Greg Page &lt;greg.page [at] caldera.com&gt;</p>
