---
title: "lookup_bdev(9)"
name: "lookup_bdev"
section: "9"
letter: "l"
url: "/docs/linux/man/9-lookup_bdev/"
---

lookup_bdev - lookup a struct block_device by name

<h2>Synopsis</h2>

<pre><code>struct block_device *lookup_bdev(const char *pathname);</code></pre>

<h2>Arguments</h2>

<i>pathname</i>
<dl><dd><dd>special file representing the block device</dl>

<h2>Description</h2>

Get a reference to the blockdevice at <i>pathname</i> in the current namespace if possible and return it. Return ERR_PTR(error) otherwise.

<h2>Copyright</h2>


