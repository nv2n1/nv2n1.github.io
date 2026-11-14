---
title: "bdev_write_page(9)"
name: "bdev_write_page"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bdev_write_page/"
---

bdev_write_page - Start writing a page to a block device

<h2>Synopsis</h2>

<pre><code>int bdev_write_page(struct block_device *bdev, sector_t sector, struct page *page, struct writeback_control *wbc);</code></pre>

<h2>Arguments</h2>

<i>bdev</i>
<dl><dd><dd>The device to write the page to</dl>
 

 <i>sector</i>
<dl><dd>The offset on the device to write the page to (need not be aligned)</dl>
 

 <i>page</i>
<dl><dd>The page to write</dl>
 

 <i>wbc</i>
<dl><dd>The writeback_control for the write</dl>

<h2>Description</h2>

On entry, the page should be locked and not currently under writeback. On exit, if the write started successfully, the page will be unlocked and under writeback. If the write failed already (eg the driver failed to queue the page to the device), the page will still be locked. If the caller is a -&gt;writepage implementation, it will need to unlock the page. 

 Errors returned by this function are usually "soft", eg out of memory, or queue full; callers should try a different route to write this page rather than propagate an error back up the stack.

<h2>Return</h2>

negative errno if an error occurs, 0 if submission was successful.

<h2>Copyright</h2>


