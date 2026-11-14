---
title: "blk_unprep_request(9)"
name: "blk_unprep_request"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_unprep_request/"
---

blk_unprep_request - unprepare a request

<h2>Synopsis</h2>

<pre><code>void blk_unprep_request(struct request *req);</code></pre>

<h2>Arguments</h2>

<i>req</i>
<dl><dd><dd>the request</dl>

<h2>Description</h2>

This function makes a request ready for complete resubmission (or completion). It happens only after all error handling is complete, so represents the appropriate moment to deallocate any resources that were allocated to the request in the prep_rq_fn. The queue lock is held when calling this.

<h2>Copyright</h2>


