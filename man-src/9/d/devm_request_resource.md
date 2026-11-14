---
title: "devm_request_resource(9)"
name: "devm_request_resource"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_request_resource/"
description: "devm_request_resource – request and reserve an I/O or memory resource"
---

<p>devm_request_resource &#8211; request and reserve an I/O or memory resource</p>
<h2>Synopsis</h2>
<pre><code>int devm_request_resource(struct device *dev, struct resource *root, struct resource *new);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>device for which to request the resource</dl>
<p> <i>root</i></p>
<dl>
<dd>root of the resource tree from which to request the resource</dl>
<p> <i>new</i></p>
<dl>
<dd>descriptor of the resource to request</dl>
<h2>Description</h2>
<p>This is a device-managed version of <code>request_resource</code>. There is usually no need to release resources requested by this function explicitly since that will be taken care of when the device is unbound from its driver. If for some reason the resource needs to be released explicitly, because of ordering issues for example, drivers must call <code>devm_release_resource</code> rather than the regular <code>release_resource</code>. </p>
<p> When a conflict is detected between any existing resources and the newly requested resource, an error message will be printed. </p>
<p> Returns 0 on success or a negative error code on failure.</p>
<h2>Copyright</h2>
