---
title: "devm_release_resource(9)"
name: "devm_release_resource"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_release_resource/"
description: "devm_release_resource – release a previously requested resource"
---

<p>devm_release_resource &#8211; release a previously requested resource</p>
<h2>Synopsis</h2>
<pre><code>void devm_release_resource(struct device *dev, struct resource *new);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device for which to release the resource</dl>
<p> <i>new</i></p>
<dl>
<dd>descriptor of the resource to release</dl>
<h2>Description</h2>
<p>Releases a resource previously requested using <code>devm_request_resource</code>.</p>
<h2>Copyright</h2>
