---
title: "skb_try_coalesce(9)"
name: "skb_try_coalesce"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_try_coalesce/"
description: "skb_try_coalesce – try to merge skb to prior one"
---

<p>skb_try_coalesce &#8211; try to merge skb to prior one</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_try_coalesce(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>to</i><code>, struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>from</i><code>, bool&nbsp;<wbr>*&nbsp;<wbr></code><i>fragstolen</i><code>, int&nbsp;<wbr>*&nbsp;<wbr></code><i>delta_truesize</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>to</i></p>
<dl>
<dd>
<dd>prior buffer</dl>
<p> <i>from</i></p>
<dl>
<dd>buffer to add</dl>
<p> <i>fragstolen</i></p>
<dl>
<dd>pointer to boolean</dl>
<p> <i>delta_truesize</i></p>
<dl>
<dd>how much more was allocated than was requested</dl>
<h2>Copyright</h2>
