---
title: "svc_print_addr(9)"
name: "svc_print_addr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-svc_print_addr/"
---

svc_print_addr - Format rq_addr field for printing

<h2>Synopsis</h2>

<pre><code>char *svc_print_addr(struct svc_rqst *rqstp, char *buf, size_t len);</code></pre>

<h2>Arguments</h2>

<i>rqstp</i>
<dl><dd><dd>svc_rqst struct containing address to print</dl>
 

 <i>buf</i>
<dl><dd>target buffer for formatted address</dl>
 

 <i>len</i>
<dl><dd>length of target buffer</dl>

<h2>Copyright</h2>


