---
title: "generic_make_request(9)"
name: "generic_make_request"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_make_request/"
description: "generic_make_request – hand a buffer to its device driver for I/O"
---

<p>generic_make_request &#8211; hand a buffer to its device driver for I/O</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>blk_qc_t generic_make_request(struct bio&nbsp;<wbr>*&nbsp;<wbr></code><i>bio</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>bio</i></p>
<dl>
<dd>
<dd>The bio describing the location in memory and on the device.</dl>
<h2>Description</h2>
<p><code>generic_make_request</code> is used to make I/O requests of block devices. It is passed a struct bio, which describes the I/O that needs to be done. </p>
<p> <code>generic_make_request</code> does not return any status. The success/failure status of the request, along with notification of completion, is delivered asynchronously through the bio-&gt;bi_end_io function described (one day) else where. </p>
<p> The caller of generic_make_request must make sure that bi_io_vec are set to describe the memory buffer, and that bi_dev and bi_sector are set to describe the device address, and the bi_end_io and optionally bi_private are set to describe how completion notification should be signaled. </p>
<p> generic_make_request and the drivers it calls may use bi_next if this bio happens to be merged with someone else, and may resubmit the bio to a lower device by calling into generic_make_request recursively, which means the bio should NOT be touched after the call to -&gt;make_request_fn.</p>
<h2>Copyright</h2>
