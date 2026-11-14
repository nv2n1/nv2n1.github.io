---
title: "skb_kill_datagram(9)"
name: "skb_kill_datagram"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_kill_datagram/"
---

skb_kill_datagram - Free a datagram skbuff forcibly

<h2>Synopsis</h2>

<pre><code>int skb_kill_datagram(struct sock *sk, struct sk_buff *skb, unsigned int flags);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>socket</dl>
 

 <i>skb</i>
<dl><dd>datagram skbuff</dl>
 

 <i>flags</i>
<dl><dd>MSG_ flags</dl>

<h2>Description</h2>

This function frees a datagram skbuff that was received by skb_recv_datagram. The flags argument must match the one used for skb_recv_datagram. 

 If the MSG_PEEK flag is set, and the packet is still on the receive queue of the socket, it will be taken off the queue before it is freed. 

 This function currently only disables BH when acquiring the sk_receive_queue lock. Therefore it must not be used in a context where that lock is acquired in an IRQ context. 

 It returns 0 if the packet was removed by us.

<h2>Copyright</h2>


