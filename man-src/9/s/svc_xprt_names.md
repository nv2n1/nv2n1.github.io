---
title: "svc_xprt_names(9)"
name: "svc_xprt_names"
section: "9"
letter: "s"
url: "/docs/linux/man/9-svc_xprt_names/"
---

svc_xprt_names - format a buffer with a list of transport names

<h2>Synopsis</h2>

<pre><code>int svc_xprt_names(struct svc_serv *serv, char *buf, const int buflen);</code></pre>

<h2>Arguments</h2>

<i>serv</i>
<dl><dd><dd>pointer to an RPC service</dl>
 

 <i>buf</i>
<dl><dd>pointer to a buffer to be filled in</dl>
 

 <i>buflen</i>
<dl><dd>length of buffer to be filled in</dl>

<h2>Description</h2>

Fills in <i>buf</i> with a string containing a list of transport names, each name terminated with '\n'. 

 Returns positive length of the filled-in string on success; otherwise a negative errno value is returned if an error occurs.

<h2>Copyright</h2>


