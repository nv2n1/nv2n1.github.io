---
title: "ipx_route(8)"
name: "ipx_route"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipx_route/"
description: "ipx_route – add or delete IPX route"
---

<p>ipx_route &#8211; add or delete IPX route</p>
<h2>Synopsis</h2>
<p><code>ipx_route</code> add target_network router_network router_node </p>
<p> <code>ipx_route</code> del target_network</p>
<h2>Description</h2>
<p><code>ipx_route</code> adds or deletes an IPX route. The kernel IPX stores only one route per target network at a time.</p>
<h3>Options</h3>
<dl>
<dt><i>add</i></p>
<dd>This option is used to set up the route to a target network.</p>
<dt><i>del</i></p>
<dd>This option is used to delete the route to a target network.</dl>
<h2>Files</h2>
<p><i>/proc/net/ipx_interface /proc/net/ipx_route</i></p>
<h2>Author</h2>
<p>Greg Page &lt;greg.page [at] caldera.com&gt;</p>
