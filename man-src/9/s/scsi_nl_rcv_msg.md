---
title: "scsi_nl_rcv_msg(9)"
name: "scsi_nl_rcv_msg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_nl_rcv_msg/"
description: "scsi_nl_rcv_msg – Receive message handler."
---

<p>scsi_nl_rcv_msg &#8211; Receive message handler.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_nl_rcv_msg(struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>socket receive buffer</dl>
<h2>Description</h2>
<p>Extracts message from a receive buffer. Validates message header and calls appropriate transport message handler</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
