---
title: "skb_append_datato_frags(9)"
name: "skb_append_datato_frags"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_append_datato_frags/"
---

skb_append_datato_frags - append the user data to a skb

<h2>Synopsis</h2>

<pre><code>int skb_append_datato_frags(struct sock *sk, struct sk_buff *skb, int (*getfrag)(void *from, char *to, int offset, int len, int odd, struct sk_buff *skb), void *from, int length);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>sock structure</dl>
 

 <i>skb</i>
<dl><dd>skb structure to be appended with user data.</dl>
 

 <i>getfrag</i>
<dl><dd>call back function to be used for getting the user data</dl>
 

 <i>from</i>
<dl><dd>pointer to user message iov</dl>
 

 <i>length</i>
<dl><dd>length of the iov message</dl>

<h2>Description</h2>

This procedure append the user data in the fragment part of the skb if any page alloc fails user this procedure returns -ENOMEM

<h2>Copyright</h2>


