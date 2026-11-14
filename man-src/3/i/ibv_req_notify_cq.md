---
title: "ibv_req_notify_cq(3)"
name: "ibv_req_notify_cq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_req_notify_cq/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_req_notify_cq - request completion notification on a completion queue (CQ) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_req_notify_cq(struct ibv_cq *cq, int solicited_only);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_req_notify_cq() requests a completion notification on the completion queue (CQ) cq. 

 Upon the addition of a new CQ entry (CQE) to cq, a completion event will be added to the completion channel associated with the CQ. If the argument solicited_only is zero, a completion event is generated for any new CQE. If solicited_only is non-zero, an event is only generated for a new CQE with that is considered "solicited." A CQE is solicited if it is a receive completion for a message with the Solicited Event header bit set, or if the status is not successful. All other successful receive completions, or any successful send completion is unsolicited.

<h2>RETURN VALUE</h2>

 

 ibv_req_notify_cq() returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>NOTES</h2>

 

 The request for notification is "one shot." Only one completion event will be generated for each call to ibv_req_notify_cq().

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_create_comp_channel/">ibv_create_comp_channel</a>(3), <a HREF="/docs/linux/man/3-ibv_create_cq/">ibv_create_cq</a>(3), <a HREF="/docs/linux/man/3-ibv_get_cq_event/">ibv_get_cq_event</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


