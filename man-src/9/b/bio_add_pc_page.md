---
title: "bio_add_pc_page(9)"
name: "bio_add_pc_page"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_add_pc_page/"
---

bio_add_pc_page - attempt to add page to bio

<h2>Synopsis</h2>

<pre><code>int bio_add_pc_page(struct request_queue *q, struct bio *bio, struct page *page, unsigned int len, unsigned int offset);</code></pre>

<h2>Arguments</h2>

<i>q</i>
<dl><dd><dd>the target queue</dl>
 

 <i>bio</i>
<dl><dd>destination bio</dl>
 

 <i>page</i>
<dl><dd>page to add</dl>
 

 <i>len</i>
<dl><dd>vec entry length</dl>
 

 <i>offset</i>
<dl><dd>vec entry offset</dl>

<h2>Description</h2>

Attempt to add a page to the bio_vec maplist. This can fail for a number of reasons, such as the bio being full or target block device limitations. The target block device must allow bio's up to PAGE_SIZE, so it is always possible to add a single page to an empty bio. 

 This should only be used by REQ_PC bios.

<h2>Copyright</h2>


