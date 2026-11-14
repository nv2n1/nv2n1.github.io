---
title: "rio_is_switch(9)"
name: "rio_is_switch"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_is_switch/"
description: "rio_is_switch – Tests if a RIO device has switch capabilities"
---

<p>rio_is_switch &#8211; Tests if a RIO device has switch capabilities</p>
<h2>Synopsis</h2>
<pre><code>int rio_is_switch(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<h2>Description</h2>
<p>Gets the RIO device Processing Element Features register contents and tests for switch capabilities. Returns 1 if the device is a switch or 0 if it is not a switch. The RIO device struct is freed.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
