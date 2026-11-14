---
title: "register_blkdev(9)"
name: "register_blkdev"
section: "9"
letter: "r"
url: "/docs/linux/man/9-register_blkdev/"
---

register_blkdev - register a new block device

<h2>Synopsis</h2>

<pre><code>int register_blkdev(unsigned int major, const char *name);</code></pre>

<h2>Arguments</h2>

<i>major</i>
<dl><dd><dd>the requested major device number [1..255]. If <i>major</i>=0, try to allocate any unused major number.</dl>
 

 <i>name</i>
<dl><dd>the name of the new block device as a zero terminated string</dl>

<h2>Description</h2>

The <i>name</i> must be unique within the system. 

 The return value depends on the <i>major</i> input parameter. - if a major device number was requested in range [1..255] then the function returns zero on success, or a negative error code - if any unused major number was requested with <i>major</i>=0 parameter then the return value is the allocated major number in range [1..255] or a negative error code otherwise

<h2>Copyright</h2>


