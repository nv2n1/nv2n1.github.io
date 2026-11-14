---
title: "skb_clone_sk(9)"
name: "skb_clone_sk"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_clone_sk/"
---

skb_clone_sk - create clone of skb, and take reference to socket

<h2>Synopsis</h2>

<pre><code>struct sk_buff *skb_clone_sk(struct sk_buff *skb);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>the skb to clone</dl>

<h2>Description</h2>

This function creates a clone of a buffer that holds a reference on sk_refcnt. Buffers created via this function are meant to be returned using sock_queue_err_skb, or free via kfree_skb. 

 When passing buffers allocated with this function to sock_queue_err_skb it is necessary to wrap the call with sock_hold/sock_put in order to prevent the socket from being released prior to being enqueued on the sk_error_queue.

<h2>Copyright</h2>


