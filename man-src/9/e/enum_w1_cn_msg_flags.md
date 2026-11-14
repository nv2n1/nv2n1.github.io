---
title: "enum_w1_cn_msg_flags(9)"
name: "enum_w1_cn_msg_flags"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_w1_cn_msg_flags/"
description: "enum_w1_cn_msg_flags – bitfield flags for struct cn_msg.flags"
---

<p>enum_w1_cn_msg_flags &#8211; bitfield flags for struct cn_msg.flags</p>
<h2>Synopsis</h2>
<pre>enum w1_cn_msg_flags {
 W1_CN_BUNDLE
}; </pre>
<h2>Constants</h2>
<p>W1_CN_BUNDLE</p>
<dl>
<dd>Request bundling replies into fewer messagse. Be prepared to handle multiple struct cn_msg, struct w1_netlink_msg, and struct w1_netlink_cmd in one packet.</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
