---
title: "register_adapter_interrupt(9)"
name: "register_adapter_interrupt"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_adapter_interrupt/"
description: "register_adapter_interrupt – register adapter interrupt handler"
---

<p>register_adapter_interrupt &#8211; register adapter interrupt handler</p>
<h2>Synopsis</h2>
<pre><code>int register_adapter_interrupt(struct airq_struct *airq);</code></pre>
<h2>Arguments</h2>
<p><i>airq</i></p>
<dl>
<dd>
<dd>pointer to adapter interrupt descriptor</dl>
<h2>Description</h2>
<p>Returns 0 on success, or -EINVAL.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
