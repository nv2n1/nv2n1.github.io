---
title: "sk_wait_data(9)"
name: "sk_wait_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_wait_data/"
description: "sk_wait_data – wait for data to arrive at sk_receive_queue"
---

<p>sk_wait_data &#8211; wait for data to arrive at sk_receive_queue</p>
<h2>Synopsis</h2>
<pre><code>int sk_wait_data(struct sock *sk, long *timeo, const struct sk_buff *skb);</code></pre>
<h2>Arguments</h2>
<p><i>sk</i></p>
<dl>
<dd>
<dd>sock to wait on</dl>
<p> <i>timeo</i></p>
<dl>
<dd>for how long</dl>
<p> <i>skb</i></p>
<dl>
<dd>last skb seen on sk_receive_queue</dl>
<h2>Description</h2>
<p>Now socket state including sk-&gt;sk_err is changed only under lock, hence we may omit checks after joining wait queue. We check receive queue before <code>schedule</code> only as optimization; it is very likely that <code>release_sock</code> added new data.</p>
<h2>Copyright</h2>
