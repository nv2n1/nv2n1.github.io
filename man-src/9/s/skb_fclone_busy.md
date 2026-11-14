---
title: "skb_fclone_busy(9)"
name: "skb_fclone_busy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_fclone_busy/"
description: "skb_fclone_busy – check if fclone is busy"
---

<p>skb_fclone_busy &#8211; check if fclone is busy</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool skb_fclone_busy(const struct sock&nbsp;<wbr>*&nbsp;<wbr></code><i>sk</i><code>, const struct sk_buff&nbsp;<wbr>*&nbsp;<wbr></code><i>skb</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>socket</dl>
<p> <i>skb</i></p>
<dl>
<dd>buffer</dl>
<h2>Description</h2>
<p>Returns true if skb is a fast clone, and its clone is not freed. Some drivers call <code>skb_orphan</code> in their <code>ndo_start_xmit</code>, so we also check that this didnt happen.</p>
<h2>Copyright</h2>
