---
title: "sk_stream_wait_connect(9)"
name: "sk_stream_wait_connect"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_stream_wait_connect/"
---

sk_stream_wait_connect - Wait for a socket to get into the connected state

<h2>Synopsis</h2>

<pre><code>int sk_stream_wait_connect(struct sock *sk, long *timeo_p);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>sock to wait on</dl>
 

 <i>timeo_p</i>
<dl><dd>for how long to wait</dl>

<h2>Description</h2>

Must be called with the socket locked.

<h2>Copyright</h2>


