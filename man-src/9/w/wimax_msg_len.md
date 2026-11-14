---
title: "wimax_msg_len(9)"
name: "wimax_msg_len"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg_len/"
description: "wimax_msg_len – Return a message’s payload length"
---

<p>wimax_msg_len &#8211; Return a message&#8217;s payload length</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t wimax_msg_len(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>msg</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>msg</i></p>
<dl>
<dd>
<dd>Pointer to a message created with <code>wimax_msg_alloc</code></dl>
<h2>Copyright</h2>
