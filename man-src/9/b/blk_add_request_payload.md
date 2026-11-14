---
title: "blk_add_request_payload(9)"
name: "blk_add_request_payload"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_add_request_payload/"
---

blk_add_request_payload - add a payload to a request

<h2>Synopsis</h2>

<pre><code>void blk_add_request_payload(struct request *rq, struct page *page, int offset, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>rq</i>
<dl><dd><dd>request to update</dl>
 

 <i>page</i>
<dl><dd>page backing the payload</dl>
 

 <i>offset</i>
<dl><dd>offset in page</dl>
 

 <i>len</i>
<dl><dd>length of the payload.</dl>

<h2>Description</h2>

This allows to later add a payload to an already submitted request by a block driver. The driver needs to take care of freeing the payload itself. 

 Note that this is a quite horrible hack and nothing but handling of discard requests should ever use it.

<h2>Copyright</h2>


