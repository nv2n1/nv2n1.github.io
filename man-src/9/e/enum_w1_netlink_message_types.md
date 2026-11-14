---
title: "enum_w1_netlink_message_types(9)"
name: "enum_w1_netlink_message_types"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_w1_netlink_message_types/"
description: "enum_w1_netlink_message_types – message type"
---

<p>enum_w1_netlink_message_types &#8211; message type</p>
<h2>Synopsis</h2>
<pre>enum w1_netlink_message_types {
 W1_SLAVE_ADD,
 W1_SLAVE_REMOVE,
 W1_MASTER_ADD,
 W1_MASTER_REMOVE,
 W1_MASTER_CMD,
 W1_SLAVE_CMD,
 W1_LIST_MASTERS
}; </pre>
<h2>Constants</h2>
<p>W1_SLAVE_ADD</p>
<dl>
<dd>notification that a slave device was added</dl>
<p> W1_SLAVE_REMOVE</p>
<dl>
<dd>notification that a slave device was removed</dl>
<p> W1_MASTER_ADD</p>
<dl>
<dd>notification that a new bus master was added</dl>
<p> W1_MASTER_REMOVE</p>
<dl>
<dd>notification that a bus masterwas removed</dl>
<p> W1_MASTER_CMD</p>
<dl>
<dd>initiate operations on a specific master</dl>
<p> W1_SLAVE_CMD</p>
<dl>
<dd>sends reset, selects the slave, then does a read/write/touch operation</dl>
<p> W1_LIST_MASTERS</p>
<dl>
<dd>used to determine the bus master identifiers</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
