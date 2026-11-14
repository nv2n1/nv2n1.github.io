---
title: "blk_release_queue(9)"
name: "blk_release_queue"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_release_queue/"
description: "blk_release_queue – release a struct request_queue when it is no longer needed"
---

<p>blk_release_queue &#8211; release a struct request_queue when it is no longer needed</p>
<h2>Synopsis</h2>
<pre><code>void blk_release_queue(struct kobject *kobj);</code></pre>
<h2>Arguments</h2>
<p><i>kobj</i></p>
<dl>
<dd>
<dd>the kobj belonging to the request queue to be released</dl>
<h2>Description</h2>
<p>blk_release_queue is the pair to <code>blk_init_queue</code> or <code>blk_queue_make_request</code>. It should be called when a request queue is being released; typically when a block device is being de-registered. Currently, its primary task it to free all the struct request structures that were allocated to the queue and the queue itself.</p>
<h2>Note</h2>
<p>The low level driver must have finished any outstanding requests first via <code>blk_cleanup_queue</code>.</p>
<h2>Copyright</h2>
