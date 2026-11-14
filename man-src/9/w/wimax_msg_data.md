---
title: "wimax_msg_data(9)"
name: "wimax_msg_data"
section: "9"
letter: "w"
url: "/docs/linux/man/9-wimax_msg_data/"
description: "wimax_msg_data – Return a pointer to a message’s payload"
---

<p>wimax_msg_data &#8211; Return a pointer to a message&#8217;s payload</p>
<h2>Synopsis</h2>
<pre><code>const void *wimax_msg_data(struct sk_buff *msg);</code></pre>
<h2>Arguments</h2>
<p><i>msg</i></p>
<dl>
<dd>
<dd>Pointer to a message created with <code>wimax_msg_alloc</code></dl>
<h2>Copyright</h2>
