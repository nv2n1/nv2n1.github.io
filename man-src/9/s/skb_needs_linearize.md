---
title: "skb_needs_linearize(9)"
name: "skb_needs_linearize"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_needs_linearize/"
description: "skb_needs_linearize – check if we need to linearize a given skb depending on the given device features."
---

<p>skb_needs_linearize &#8211; check if we need to linearize a given skb depending on the given device features.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_needs_linearize(struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>, netdev_features_t&nbsp;<wbr></code><i>features</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>socket buffer to check</dl>
<p> <i>features</i></p>
<dl>
<dd>net device features</dl>
<h2>Description</h2>
<p>Returns true if either: 1. skb has frag_list and the device doesn&#8217;t support FRAGLIST, or 2. skb is fragmented and the device does not support SG.</p>
<h2>Copyright</h2>
