---
title: "gadget_avoids_skb_reserve(9)"
name: "gadget_avoids_skb_reserve"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gadget_avoids_skb_reserve/"
description: "gadget_avoids_skb_reserve – return true iff the hardware would like to avoid skb_reserve to improve performance."
---

<p>gadget_avoids_skb_reserve &#8211; return true iff the hardware would like to avoid skb_reserve to improve performance.</p>
<h2>Synopsis</h2>
<pre><code>int gadget_avoids_skb_reserve(struct usb_gadget *g);</code></pre>
<h2>Arguments</h2>
<p><i>g</i></p>
<dl>
<dd>
<dd>controller to check for quirk</dl>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
