---
title: "bdev_read_page(9)"
name: "bdev_read_page"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdev_read_page/"
---

bdev_read_page - Start reading a page from a block device

<h2>Synopsis</h2>

<pre><code>int bdev_read_page(struct block_device *bdev, sector_t sector, struct page *page);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>The device to read the page from</dl>
 

 <i>sector</i>
<dl><dd>The offset on the device to read the page to (need not be aligned)</dl>
 

 <i>page</i>
<dl><dd>The page to read</dl>

<h2>Description</h2>

On entry, the page should be locked. It will be unlocked when the page has been read. If the block driver implements rw_page synchronously, that will be true on exit from this function, but it need not be. 

 Errors returned by this function are usually "soft", eg out of memory, or queue full; callers should try a different route to read this page rather than propagate an error back up the stack.

<h2>Return</h2>

negative errno if an error occurs, 0 if submission was successful.

<h2>Copyright</h2>


