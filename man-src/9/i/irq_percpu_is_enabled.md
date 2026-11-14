---
title: "irq_percpu_is_enabled(9)"
name: "irq_percpu_is_enabled"
section: "9"
letter: "i"
url: "/docs/linux/man/9-irq_percpu_is_enabled/"
description: "irq_percpu_is_enabled – Check whether the per cpu irq is enabled"
---

<p>irq_percpu_is_enabled &#8211; Check whether the per cpu irq is enabled</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool irq_percpu_is_enabled(unsigned int&nbsp;<wbr></code><i>irq</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Linux irq number to check for</dl>
<h2>Description</h2>
<p>Must be called from a non migratable context. Returns the enable state of a per cpu interrupt on the current cpu.</p>
<h2>Copyright</h2>
