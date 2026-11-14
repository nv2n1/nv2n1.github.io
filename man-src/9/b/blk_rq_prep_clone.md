---
title: "blk_rq_prep_clone(9)"
name: "blk_rq_prep_clone"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_rq_prep_clone/"
description: "blk_rq_prep_clone – Helper function to setup clone request"
---

<p>blk_rq_prep_clone &#8211; Helper function to setup clone request</p>
<h2>Synopsis</h2>
<pre><code>int blk_rq_prep_clone(struct request *rq, struct request *rq_src, struct bio_set *bs, gfp_t gfp_mask, int (*bio_ctr)(struct bio *, struct bio *, void *), void *data);</code></pre>
<h2>Arguments</h2>
<p><i>rq</i></p>
<dl>
<dd>
<dd>the request to be setup</dl>
<p> <i>rq_src</i></p>
<dl>
<dd>original request to be cloned</dl>
<p> <i>bs</i></p>
<dl>
<dd>bio_set that bios for clone are allocated from</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>memory allocation mask for bio</dl>
<p> <i>bio_ctr</i></p>
<dl>
<dd>setup function to be called for each clone bio. Returns <code>0</code> for success, non <code>0</code> for failure.</dl>
<p> <i>data</i></p>
<dl>
<dd>private data to be passed to <i>bio_ctr</i></dl>
<h2>Description</h2>
<p>Clones bios in <i>rq_src</i> to <i>rq</i>, and copies attributes of <i>rq_src</i> to <i>rq</i>. The actual data parts of <i>rq_src</i> (e.g. -&gt;cmd, -&gt;sense) are not copied, and copying such parts is the caller&#8217;s responsibility. Also, pages which the original bios are pointing to are not copied and the cloned bios just point same pages. So cloned bios must be completed before original bios, which means the caller must complete <i>rq</i> before <i>rq_src</i>.</p>
<h2>Copyright</h2>
