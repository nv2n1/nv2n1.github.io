---
title: "rio_match_bus(9)"
name: "rio_match_bus"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_match_bus/"
description: "rio_match_bus – Tell if a RIO device structure has a matching RIO driver device id structure"
---

<p>rio_match_bus &#8211; Tell if a RIO device structure has a matching RIO driver device id structure</p>
<h2>Synopsis</h2>
<pre><code>int rio_match_bus(struct device *dev, struct device_driver *drv);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the standard device structure to match against</dl>
<p> <i>drv</i></p>
<dl>
<dd>the standard driver structure containing the ids to match against</dl>
<h2>Description</h2>
<p>Used by a driver to check whether a RIO device present in the system is in its list of supported devices. Returns 1 if there is a matching struct rio_device_id or 0 if there is no match.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
