---
title: "skb_has_shared_frag(9)"
name: "skb_has_shared_frag"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_has_shared_frag/"
description: "skb_has_shared_frag – can any frag be overwritten"
---

<p>skb_has_shared_frag &#8211; can any frag be overwritten</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_has_shared_frag(const struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>buffer to test</dl>
<h2>Description</h2>
<p>Return true if the skb has at least one frag that might be modified by an external entity (as in <code>vmsplice</code>/<code>sendfile</code>)</p>
<h2>Copyright</h2>
