---
title: "ipx_interface(8)"
name: "ipx_interface"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipx_interface/"
description: "ipx_interface – add, delete, or display an IPX interface"
---

<p>ipx_interface &#8211; add, delete, or display an IPX interface</p>
<h2>Synopsis</h2>
<p><code>ipx_interface</code> add [-p] device frame_type [network number[:node number]] </p>
<p> <code>ipx_interface</code> del device frame_type </p>
<p> <code>ipx_interface</code> delall </p>
<p> <code>ipx_interface</code> check device frame_type </p>
<p> <code>ipx_interface</code> help</p>
<h2>Description</h2>
<p><code>ipx_interface</code> adds, deletes, or displays IPX interfaces depending on the option selected. An IPX interface is the item to which IPX sockets are bound. An IPX interface corresponds to an IPX Network Number which corresponds to a physical device and frame type. A sample IPX Interface would be: </p>
<p> Network Number: 0x00ABCDEF </p>
<p> Device: Eth0 </p>
<p> Frame Type: 802.2. There is a special IPX interface per host known as the <code>PRIMARY</code> or default interface. You should specify <code>node number</code> only if you really know, what you are doing &#8211; on <i>point-to-point</i> devices, on <i>loopback</i> and on <i>tap</i> device if you are running <code>Compatibility mode driver</code>.</p>
<h3>Options</h3>
<dl>
<dt><i>add</i></p>
<dd>This option is used to create an IPX interface. If the <code>-p</code> flag is used, the interface is made <code>PRIMARY.</code> The network number can be optionally assigned. If it is not assigned, it is set to 0 which indicates it should be detected from the traffic on the network.</p>
<dt><i>del</i></p>
<dd>This option is used to delete an IPX interface.</p>
<dt><i>delall</i></p>
<dd>This option is used to delete all IPX interfaces.</p>
<dt><i>check</i></p>
<dd>This option is used to display the device, frame type, and network number of an IPX interface.</p>
<dt><i>help</i></p>
<dd>This option displays information about the utility.</dl>
<h2>Files</h2>
<p><i>/proc/net/ipx_interface /proc/net/ipx_route</i></p>
<h2>Bugs</h2>
<p>This functionality really belongs in <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8).</code></p>
<h2>Author</h2>
<p>Greg Page &lt;greg.page [at] caldera.com&gt;</p>
