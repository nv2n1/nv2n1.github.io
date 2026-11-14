---
title: "sock_tx_timestamp(9)"
name: "sock_tx_timestamp"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_tx_timestamp/"
---

sock_tx_timestamp - checks whether the outgoing packet is to be time stamped

<h2>Synopsis</h2>

<pre><code>void sock_tx_timestamp(const struct sock *sk, __u16 tsflags, __u8 *tx_flags);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>socket sending this packet</dl>
 

 <i>tsflags</i>
<dl><dd>timestamping flags to use</dl>
 

 <i>tx_flags</i>
<dl><dd>completed with instructions for time stamping</dl>

<h2>Note</h2>

callers should take care of initial *tx_flags value (usually 0)

<h2>Copyright</h2>


