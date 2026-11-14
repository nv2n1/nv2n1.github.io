---
title: "ibv_ack_async_event(3)"
name: "ibv_ack_async_event"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_ack_async_event/"
description: "ibv_get_async_event, ibv_ack_async_event – get or acknowledge asynchronous events"
---

<h2 class="name">NAME</h2>
<p> ibv_get_async_event, ibv_ack_async_event &#8211; get or acknowledge asynchronous events </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_get_async_event(struct ibv_context *context,
                        struct ibv_async_event *event);
void ibv_ack_async_event(struct ibv_async_event *event);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_get_async_event()</code> waits for the next async event of the RDMA device context <i>context</i> and returns it through the pointer <i>event</i>, which is an ibv_async_event struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_async_event {<br />
    union {<br />
        struct ibv_cq *cq;   /* CQ that got the event */<br />
        struct ibv_qp *qp;   /* QP that got the event */<br />
        struct ibv_srq *srq; /* SRQ that got the event */<br />
        int port_num;        /* port number that got the event */<br />
    } element;<br />
    enum ibv_event_type event_type; /* type of the event */<br />
};</p>
<p> One member of the element union will be valid, depending on the event_type member of the structure. event_type will be one of the following events: </p>
<p> <i>QP events:</i></p>
<dl>
<dt><code>IBV_EVENT_QP_FATAL </code> Error occurred on a QP and it transitioned to error state</p>
<dd>
<dt><code>IBV_EVENT_QP_REQ_ERR </code> Invalid Request Local Work Queue Error</p>
<dd>
<dt><code>IBV_EVENT_QP_ACCESS_ERR </code> Local access violation error</p>
<dd>
<dt><code>IBV_EVENT_COMM_EST </code> Communication was established on a QP</p>
<dd>
<dt><code>IBV_EVENT_SQ_DRAINED </code> Send Queue was drained of outstanding messages in progress</p>
<dd>
<dt><code>IBV_EVENT_PATH_MIG </code> A connection has migrated to the alternate path</p>
<dd>
<dt><code>IBV_EVENT_PATH_MIG_ERR </code> A connection failed to migrate to the alternate path</p>
<dd>
<dt><code>IBV_EVENT_QP_LAST_WQE_REACHED </code> Last WQE Reached on a QP associated with an SRQ</p>
<dd></dl>
<p> <i>CQ events:</i></p>
<dl>
<dt><code>IBV_EVENT_CQ_ERR </code> CQ is in error (CQ overrun)</p>
<dd></dl>
<p> <i>SRQ events:</i></p>
<dl>
<dt><code>IBV_EVENT_SRQ_ERR </code> Error occurred on an SRQ</p>
<dd>
<dt><code>IBV_EVENT_SRQ_LIMIT_REACHED </code> SRQ limit was reached</p>
<dd></dl>
<p> <i>Port events:</i></p>
<dl>
<dt><code>IBV_EVENT_PORT_ACTIVE </code> Link became active on a port</p>
<dd>
<dt><code>IBV_EVENT_PORT_ERR </code> Link became unavailable on a port</p>
<dd>
<dt><code>IBV_EVENT_LID_CHANGE </code> LID was changed on a port</p>
<dd>
<dt><code>IBV_EVENT_PKEY_CHANGE </code> P_Key table was changed on a port</p>
<dd>
<dt><code>IBV_EVENT_SM_CHANGE </code> SM was changed on a port</p>
<dd>
<dt><code>IBV_EVENT_CLIENT_REREGISTER </code> SM sent a CLIENT_REREGISTER request to a port</p>
<dd>
<dt><code>IBV_EVENT_GID_CHANGE </code> GID table was changed on a port</p>
<dd></dl>
<p> <i>CA events:</i></p>
<dl>
<dt><code>IBV_EVENT_DEVICE_FATAL </code> CA is in FATAL state</p>
<dd></dl>
<p> <code>ibv_ack_async_event()</code> acknowledge the async event <i>event</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_get_async_event()</code> returns 0 on success, and -1 on error. </p>
<p> <code>ibv_ack_async_event()</code> returns no value.</p>
<h2>NOTES</h2>
<p> All async events that <code>ibv_get_async_event()</code> returns must be acknowledged using <code>ibv_ack_async_event()</code>. To avoid races, destroying an object (CQ, SRQ or QP) will wait for all affiliated events for the object to be acknowledged; this avoids an application retrieving an affiliated event after the corresponding object has already been destroyed. </p>
<p> <code>ibv_get_async_event()</code> is a blocking function. If multiple threads call this function simultaneously, then when an async event occurs, only one thread will receive it, and it is not possible to predict which thread will receive it.</p>
<h2>EXAMPLES</h2>
<p> The following code example demonstrates one possible way to work with async events in non-blocking mode. It performs the following steps: </p>
<p> 1. Set the async events queue work mode to be non-blocked<br />
 2. Poll the queue until it has an async event<br />
 3. Get the async event and ack it </p>
<pre><code>
/* change the blocking mode of the async event queue */
flags = fcntl(ctx-&gt;async_fd, F_GETFL);
rc = fcntl(ctx-&gt;async_fd, F_SETFL, flags | O_NONBLOCK);
if (rc &lt; 0) {
    fprintf(stderr, "Failed to change file descriptor of async event queue
");
    return 1;
}
/*
 * poll the queue until it has an event and sleep ms_timeout
 * milliseconds between any iteration
 */
my_pollfd.fd = ctx-&gt;async_fd;
my_pollfd.events = POLLIN;
my_pollfd.revents = 0;
do {
    rc = poll(&amp;my_pollfd, 1, ms_timeout);
} while (rc == 0);
if (rc &lt; 0) {
    fprintf(stderr, "poll failed
");
    return 1;
}
/* Get the async event */
if (ibv_get_async_event(ctx, &amp;async_event)) {
    fprintf(stderr, "Failed to get async_event
");
    return 1;
}
/* Ack the event */
ibv_ack_async_event(&amp;async_event);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
