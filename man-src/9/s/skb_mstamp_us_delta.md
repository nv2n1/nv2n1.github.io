---
title: "skb_mstamp_us_delta(9)"
name: "skb_mstamp_us_delta"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_mstamp_us_delta/"
description: "skb_mstamp_us_delta – compute the difference in usec between two skb_mstamp"
---

<p>skb_mstamp_us_delta &#8211; compute the difference in usec between two skb_mstamp</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 skb_mstamp_us_delta(const struct skb_mstamp&nbsp;<wbr>*&nbsp;<wbr></code><i>t1</i><code>, const struct skb_mstamp&nbsp;<wbr>*&nbsp;<wbr></code><i>t0</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>t1</i></p>
<dl>
<dd>
<dd>pointer to newest sample</dl>
<p> <i>t0</i></p>
<dl>
<dd>pointer to oldest sample</dl>
<h2>Copyright</h2>
