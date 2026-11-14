---
title: "bio_alloc_bioset(9)"
name: "bio_alloc_bioset"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bio_alloc_bioset/"
description: "bio_alloc_bioset – allocate a bio for I/O"
---

<p>bio_alloc_bioset &#8211; allocate a bio for I/O</p>
<h2>Synopsis</h2>
<pre><code>struct bio *bio_alloc_bioset(gfp_t gfp_mask, int nr_iovecs, struct bio_set *bs);</code></pre>
<h2>Arguments</h2>
<p><i>gfp_mask</i></p>
<dl>
<dd>
<dd>the GFP_ mask given to the slab allocator</dl>
<p> <i>nr_iovecs</i></p>
<dl>
<dd>number of iovecs to pre-allocate</dl>
<p> <i>bs</i></p>
<dl>
<dd>the bio_set to allocate from.</dl>
<h2>Description</h2>
<p>If <i>bs</i> is NULL, uses <code>kmalloc</code> to allocate the bio; else the allocation is backed by the <i>bs</i>&#8216;s mempool. </p>
<p> When <i>bs</i> is not NULL, if <code>__GFP_DIRECT_RECLAIM</code> is set then bio_alloc will always be able to allocate a bio. This is due to the mempool guarantees. To make this work, callers must never allocate more than 1 bio at a time from this pool. Callers that need to allocate more than 1 bio must always submit the previously allocated bio for IO before attempting to allocate a new one. Failure to do so can cause deadlocks under memory pressure. </p>
<p> Note that when running under <code>generic_make_request</code> (i.e. any block driver), bios are not submitted until after you return &#8211; see the code in <code>generic_make_request</code> that converts recursion into iteration, to prevent stack overflows. </p>
<p> This would normally mean allocating multiple bios under <code>generic_make_request</code> would be susceptible to deadlocks, but we have deadlock avoidance code that resubmits any blocked bios from a rescuer thread. </p>
<p> However, we do not guarantee forward progress for allocations from other mempools. Doing multiple allocations from the same mempool under <code>generic_make_request</code> should be avoided &#8211; instead, use bio_set&#8217;s front_pad for per bio allocations.</p>
<h2>Return</h2>
<p>Pointer to new bio on success, NULL on failure.</p>
<h2>Copyright</h2>
