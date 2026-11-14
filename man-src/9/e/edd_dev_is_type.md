---
title: "edd_dev_is_type(9)"
name: "edd_dev_is_type"
section: "9"
letter: "e"
url: "/docs/linux/man/9-edd_dev_is_type/"
---

edd_dev_is_type - is this EDD device a 'type' device?

<h2>Synopsis</h2>

<pre><code>int edd_dev_is_type(struct edd_device *edev, const char *type);</code></pre>

<h2>Arguments</h2>

<i>edev</i>
<dl><dd><dd>target edd_device</dl>
 

 <i>type</i>
<dl><dd>a host bus or interface identifier string per the EDD spec</dl>

<h2>Description</h2>

Returns 1 (TRUE) if it is a 'type' device, 0 otherwise.

<h2>Copyright</h2>


