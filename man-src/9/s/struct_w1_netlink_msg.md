---
title: "struct_w1_netlink_msg(9)"
name: "struct_w1_netlink_msg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_netlink_msg/"
description: "struct_w1_netlink_msg – holds w1 message type, id, and result"
---

<p>struct_w1_netlink_msg &#8211; holds w1 message type, id, and result</p>
<h2>Synopsis</h2>
<pre><code>struct w1_netlink_msg {
    __u8 type;
    __u8 status;
    __u16 len;
    union id;
    __u8 data[0];
};</code></pre>
<h2>Members</h2>
<p>type</p>
<dl>
<dd>one of enum w1_netlink_message_types</dl>
<p> status</p>
<dl>
<dd>kernel feedback for success 0 or errno failure value</dl>
<p> len</p>
<dl>
<dd>length of data following w1_netlink_msg</dl>
<p> id</p>
<dl>
<dd>union holding master bus id (msg.id) and slave device id (id[8]).</dl>
<p> data[0]</p>
<dl>
<dd>start address of any following data</dl>
<h2>Description</h2>
<p>The base message structure for w1 messages over netlink. The netlink connector data sequence is, struct nlmsghdr, struct cn_msg, then one or more struct w1_netlink_msg (each with optional data).</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
