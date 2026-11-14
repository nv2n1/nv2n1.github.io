---
title: "blk_queue_make_request(9)"
name: "blk_queue_make_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_queue_make_request/"
description: "blk_queue_make_request – define an alternate make_request function for a device"
---

<p>blk_queue_make_request &#8211; define an alternate make_request function for a device</p>
<h2>Synopsis</h2>
<pre><code>void blk_queue_make_request(struct request_queue *q, make_request_fn *mfn);</code></pre>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>the request queue for the device to be affected</dl>
<p> <i>mfn</i></p>
<dl>
<dd>the alternate make_request function</dl>
<h2>Description</h2>
<p>The normal way for struct bios to be passed to a device driver is for them to be collected into requests on a request queue, and then to allow the device driver to select requests off that queue when it is ready. This works well for many block devices. However some block devices (typically virtual devices such as md or lvm) do not benefit from the processing on the request queue, and are served best by having the requests passed directly to them. This can be achieved by providing a function to <code>blk_queue_make_request</code>. </p>
<p> Caveat: The driver that does this *must* be able to deal appropriately with buffers in &#8220;highmemory&#8221;. This can be accomplished by either calling <code>__bio_kmap_atomic</code> to get a temporary kernel mapping, or by calling <code>blk_queue_bounce</code> to create a buffer in normal memory.</p>
<h2>Copyright</h2>
