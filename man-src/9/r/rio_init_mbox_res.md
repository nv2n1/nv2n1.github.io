---
title: "rio_init_mbox_res(9)"
name: "rio_init_mbox_res"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_init_mbox_res/"
description: "rio_init_mbox_res – Initialize a RIO mailbox resource"
---

<p>rio_init_mbox_res &#8211; Initialize a RIO mailbox resource</p>
<h2>Synopsis</h2>
<pre><code>void rio_init_mbox_res(struct resource *res, int start, int end);</code></pre>
<h2>Arguments</h2>
<p><i>res</i></p>
<dl>
<dd>
<dd>resource struct</dl>
<p> <i>start</i></p>
<dl>
<dd>start of mailbox range</dl>
<p> <i>end</i></p>
<dl>
<dd>end of mailbox range</dl>
<h2>Description</h2>
<p>This function is used to initialize the fields of a resource for use as a mailbox resource. It initializes a range of mailboxes using the start and end arguments.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
