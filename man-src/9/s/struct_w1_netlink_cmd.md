---
title: "struct_w1_netlink_cmd(9)"
name: "struct_w1_netlink_cmd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_netlink_cmd/"
description: "struct_w1_netlink_cmd – holds the command and data"
---

<p>struct_w1_netlink_cmd &#8211; holds the command and data</p>
<h2>Synopsis</h2>
<pre><code>struct w1_netlink_cmd {
    __u8 cmd;
    __u8 res;
    __u16 len;
    __u8 data[0];
};</code></pre>
<h2>Members</h2>
<p>cmd</p>
<dl>
<dd>one of enum w1_commands</dl>
<p> res</p>
<dl>
<dd>reserved</dl>
<p> len</p>
<dl>
<dd>length of data following w1_netlink_cmd</dl>
<p> data[0]</p>
<dl>
<dd>start address of any following data</dl>
<h2>Description</h2>
<p>One or more struct w1_netlink_cmd is placed starting at w1_netlink_msg.data each with optional data.</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
