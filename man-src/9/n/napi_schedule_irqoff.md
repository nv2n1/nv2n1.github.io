---
title: "napi_schedule_irqoff(9)"
name: "napi_schedule_irqoff"
section: "9"
letter: "n"
url: "/docs/linux/man/9-napi_schedule_irqoff/"
description: "napi_schedule_irqoff – schedule NAPI poll"
---

<p>napi_schedule_irqoff &#8211; schedule NAPI poll</p>
<h2>Synopsis</h2>
<pre><code>void napi_schedule_irqoff(struct napi_struct *n);</code></pre>
<h2>Arguments</h2>
<p><i>n</i></p>
<dl>
<dd>
<dd>NAPI context</dl>
<h2>Description</h2>
<p>Variant of <code>napi_schedule</code>, assuming hard irqs are masked.</p>
<h2>Copyright</h2>
