---
title: "rio_dev_put(9)"
name: "rio_dev_put"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_dev_put/"
description: "rio_dev_put – Release a use of the RIO device structure"
---

<p>rio_dev_put &#8211; Release a use of the RIO device structure</p>
<h2>Synopsis</h2>
<pre><code>void rio_dev_put(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device being disconnected</dl>
<h2>Description</h2>
<p>Must be called when a user of a device is finished with it. When the last user of the device calls this function, the memory of the device is freed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
