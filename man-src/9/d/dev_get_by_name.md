---
title: "dev_get_by_name(9)"
name: "dev_get_by_name"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_by_name/"
description: "dev_get_by_name – find a device by its name"
---

<p>dev_get_by_name &#8211; find a device by its name</p>
<h2>Synopsis</h2>
<pre><code>struct net_device *dev_get_by_name(struct net *net, const char *name);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>the applicable net namespace</dl>
<p> <i>name</i></p>
<dl>
<dd>name to find</dl>
<h2>Description</h2>
<p>Find an interface by name. This can be called from any context and does its own locking. The returned handle has the usage count incremented and the caller must use <code>dev_put</code> to release it when it is no longer needed. <code>NULL</code> is returned if no matching device is found.</p>
<h2>Copyright</h2>
