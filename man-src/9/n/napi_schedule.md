---
title: "napi_schedule(9)"
name: "napi_schedule"
section: "9"
letter: "n"
url: "/docs/linux/man/9-napi_schedule/"
---

napi_schedule - schedule NAPI poll

<h2>Synopsis</h2>

<pre><code>void napi_schedule(struct napi_struct *n);</code></pre>

<h2>Arguments</h2>

<i>n</i>
<dl><dd><dd>NAPI context</dl>

<h2>Description</h2>

Schedule NAPI poll routine to be called if it is not already running.

<h2>Copyright</h2>


