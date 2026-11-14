---
title: "sk_filter_trim_cap(9)"
name: "sk_filter_trim_cap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_filter_trim_cap/"
---

sk_filter_trim_cap - run a packet through a socket filter

<h2>Synopsis</h2>

<pre><code>int sk_filter_trim_cap(struct sock *sk, struct sk_buff *skb, unsigned int cap);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>sock associated with sk_buff</dl>
 

 <i>skb</i>
<dl><dd>buffer to filter</dl>
 

 <i>cap</i>
<dl><dd>limit on how short the eBPF program may trim the packet</dl>

<h2>Description</h2>

Run the eBPF program and then cut skb-&gt;data to correct size returned by the program. If pkt_len is 0 we toss packet. If skb-&gt;len is smaller than pkt_len we keep whole skb-&gt;data. This is the socket level wrapper to BPF_PROG_RUN. It returns 0 if the packet should be accepted or -EPERM if the packet should be tossed.

<h2>Copyright</h2>


