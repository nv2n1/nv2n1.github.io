---
title: "pbs_rescreserve(3)"
name: "pbs_rescreserve"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pbs_rescreserve/"
description: "pbs_rescreserve, pbs_rescrelease – reserve/free batch resources"
---

<p>pbs_rescreserve, pbs_rescrelease &#8211; reserve/free batch resources</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pbs_error.h&gt;

#include &lt;pbs_ifl.h&gt;</code></pre>
<pre>int pbs_rescreserve(int connect, char&nbsp;<wbr>**resourcelist, int arraysize,
resource_t *resource_id)
int pbs_rescrelease(int connect, resource_t resource_id)</pre>
<h2>Description</h2>
<dl>
<dt> <code>pbs_rescreserver</code></p>
<dd>
<dd>Issue a request to the batch server to reserve specified resources. <i> is the connection returned by </i><code>pbs_connect</code>(). <i> is an array of one or more strings specifying the resources to be queried. is the is the number of strings in resourcelist. is a pointer to a resource handle. The pointer cannot be null. If the present value of the resource handle is </i><code>RESOURCE_T_NULL ,</code> this request is for a new reservation and if successful, a resource handle will be returned in resource_id.</p>
<dd>If the value of resource_id as supplied by the caller is not <code>RESOURCE_T_NULL ,</code> this is a existing (partial) reservation. Resources currently reserved for this handle will be released and the full reservation will be attempted again. If the caller wishes to release the resources allocated to a partial reservation, the caller should pass the resource handle to <code>pbs_rescrelease</code>().</p>
<dd>At the present time the only resources which may be specified are &quot;nodes&quot;. It should be specified as <code> where specification is what a user specifies in the -l option arguement list for nodes, see </code><i>qsub (1B).</i></p>
<dt> <code>pbs_rescrelease</code></p>
<dd>
<dd>The <code>pbs_rescrelease</code>() call releases or frees resources reserved with the resource handle of <i> returned from a prior </i><code>pbs_rescreserve</code>() call. <i> is the connection returned by </i><code>pbs_connect</code>().</dl>
<p> Both functions require that the issuing user have operator or administrator privilege.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_disconnect/">pbs_disconnect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_rescquery/">pbs_rescquery</a>(3B) and <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources/">pbs_resources</a>(7B)</p>
<h2>Diagnostics</h2>
<p>pbs_rescreserve() and pbs_rescrelease() return zero on success. Otherwise, a non zero error is returned. The error number is also set in pbs_errno.</p>
<dl>
<dt>PBSE_RMPART</p>
<dd>is a special case indicating that some but not all of the requested resources could be reserved; a partial reservation was made. The reservation request should either be rerequested with the returned handle or the partial resources released.</p>
<dt>PBSE_RMBADPARAM</p>
<dd>a parameter is incorrect, such as a null for the pointer to the resource_id.</p>
<dt>PBSE_RMNOPARAM</p>
<dd>a parameter is missing, such as a null resoruce list.</dl>
