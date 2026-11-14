---
title: "svc_reserve(9)"
name: "svc_reserve"
section: "9"
letter: "s"
url: "/docs/linux/man/9-svc_reserve/"
---

svc_reserve - change the space reserved for the reply to a request.

<h2>Synopsis</h2>

<pre><code>void svc_reserve(struct svc_rqst *rqstp, int space);</code></pre>

<h2>Arguments</h2>

<i>rqstp</i>
<dl><dd><dd>The request in question</dl>
 

 <i>space</i>
<dl><dd>new max space to reserve</dl>

<h2>Description</h2>

Each request reserves some space on the output queue of the transport to make sure the reply fits. This function reduces that reserved space to be the amount of space used already, plus <i>space</i>.

<h2>Copyright</h2>


