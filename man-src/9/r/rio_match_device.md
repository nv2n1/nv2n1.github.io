---
title: "rio_match_device(9)"
name: "rio_match_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_match_device/"
description: "rio_match_device – Tell if a RIO device has a matching RIO device id structure"
---

<p>rio_match_device &#8211; Tell if a RIO device has a matching RIO device id structure</p>
<h2>Synopsis</h2>
<pre><code>const struct rio_device_id *rio_match_device(const struct rio_device_id *id, const struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>the RIO device id structure to match against</dl>
<p> <i>rdev</i></p>
<dl>
<dd>the RIO device structure to match against</dl>
<h2>Description</h2>
<p>Used from driver probe and bus matching to check whether a RIO device matches a device id structure provided by a RIO driver. Returns the matching struct rio_device_id or <code>NULL</code> if there is no match.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
