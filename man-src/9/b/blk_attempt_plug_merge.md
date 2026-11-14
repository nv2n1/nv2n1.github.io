---
title: "blk_attempt_plug_merge(9)"
name: "blk_attempt_plug_merge"
section: "9"
letter: "b"
url: "/docs/linux/man/9-blk_attempt_plug_merge/"
description: "blk_attempt_plug_merge – try to merge with current‘s plugged list"
---

<p>blk_attempt_plug_merge &#8211; try to merge with <code>current</code>&#8216;s plugged list</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool blk_attempt_plug_merge(struct request_queue&nbsp;<wbr>*&nbsp;<wbr></code><i>q</i><code>, struct bio&nbsp;<wbr>*&nbsp;<wbr></code><i>bio</i><code>, unsigned int&nbsp;<wbr>*&nbsp;<wbr></code><i>request_count</i><code>, struct request&nbsp;<wbr>**&nbsp;<wbr></code><i>same_queue_rq</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>q</i></p>
<dl>
<dd>
<dd>request_queue new bio is being queued at</dl>
<p> <i>bio</i></p>
<dl>
<dd>new bio being queued</dl>
<p> <i>request_count</i></p>
<dl>
<dd>out parameter for number of traversed plugged requests</dl>
<p> <i>same_queue_rq</i></p>
<dl>
<dd>pointer to struct request that gets filled in when another request associated with <i>q</i> is found on the plug list (optional, may be <code>NULL</code>)</dl>
<h2>Description</h2>
<p>Determine whether <i>bio</i> being queued on <i>q</i> can be merged with a request on <code>current</code>&#8216;s plugged list. Returns <code>true</code> if merge was successful, otherwise <code>false</code>. </p>
<p> Plugging coalesces IOs from the same issuer for the same purpose without going through <i>q</i>-&gt;queue_lock. As such it&#8217;s more of an issuing mechanism than scheduling, and the request, while may have elvpriv data, is not added on the elevator at this point. In addition, we don&#8217;t have reliable access to the elevator outside queue lock. Only check basic merging parameters without querying the elevator. </p>
<p> Caller must ensure !blk_queue_nomerges(q) beforehand.</p>
<h2>Copyright</h2>
