---
title: "struct_gnet_estimator(9)"
name: "struct_gnet_estimator"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_gnet_estimator/"
---

struct_gnet_estimator - rate estimator configuration

<h2>Synopsis</h2>

<pre><code>struct gnet_estimator {
    signed char interval;
    unsigned char ewma_log;
};</code></pre>

<h2>Members</h2>

interval
<dl><dd>sampling period</dl>
 

 ewma_log
<dl><dd>the log of measurement window weight</dl>

<h2>Copyright</h2>


