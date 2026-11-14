---
title: "ibv_ack_cq_events(3)"
name: "ibv_ack_cq_events"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_ack_cq_events/"
description: "ibv_get_cq_event, ibv_ack_cq_events – get and acknowledge completion queue (CQ) events"
---

<h2 class="name">NAME</h2>
<p> ibv_get_cq_event, ibv_ack_cq_events &#8211; get and acknowledge completion queue (CQ) events</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_get_cq_event(struct ibv_comp_channel *channel,
                     struct ibv_cq **cq, void **cq_context);
void ibv_ack_cq_events(struct ibv_cq *cq, unsigned int nevents);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_get_cq_event()</code> waits for the next completion event in the completion event channel <i>channel</i>. Fills the arguments <i>cq</i> with the CQ that got the event and <i>cq_context</i> with the CQ&#8217;s context. </p>
<p> <code>ibv_ack_cq_events()</code> acknowledges <i>nevents</i> events on the CQ <i>cq</i>. </p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_get_cq_event()</code> returns 0 on success, and -1 on error. </p>
<p> <code>ibv_ack_cq_events()</code> returns no value.</p>
<h2>NOTES</h2>
<p> All completion events that <code>ibv_get_cq_event()</code> returns must be acknowledged using <code>ibv_ack_cq_events()</code>. To avoid races, destroying a CQ will wait for all completion events to be acknowledged; this guarantees a one-to-one correspondence between acks and successful gets. </p>
<p> Calling <code>ibv_ack_cq_events()</code> may be relatively expensive in the datapath, since it must take a mutex. Therefore it may be better to amortize this cost by keeping a count of the number of events needing acknowledgement and acking several completion events in one call to <code>ibv_ack_cq_events()</code>.</p>
<h2>EXAMPLES</h2>
<p> The following code example demonstrates one possible way to work with completion events. It performs the following steps: </p>
<p> Stage I: Preparation<br />
 1. Creates a CQ<br />
 2. Requests for notification upon a new (first) completion event </p>
<p> Stage II: Completion Handling Routine<br />
 3. Wait for the completion event and ack it<br />
 4. Request for notification upon the next completion event<br />
 5. Empty the CQ </p>
<p> Note that an extra event may be triggered without having a corresponding completion entry in the CQ. This occurs if a completion entry is added to the CQ between Step 4 and Step 5, and the CQ is then emptied (polled) in Step 5. </p>
<p>cq = ibv_create_cq(ctx, 1, ev_ctx, channel, 0);<br />
if (!cq) {<br />
    fprintf(stderr, &#8220;Failed to create CQ
&#8221;);<br />
    return 1;<br />
}<br />
/* Request notification before any completion can be created */<br />
if (ibv_req_notify_cq(cq, 0)) {<br />
    fprintf(stderr, &#8220;Couldn&#8217;t request CQ notification
&#8221;);<br />
    return 1;<br />
}<br />
.<br />
    .<br />
    .<br />
    /* Wait for the completion event */<br />
    if (ibv_get_cq_event(channel, &amp;ev_cq, &amp;ev_ctx))<br />
{<br />
    fprintf(stderr, &#8220;Failed to get cq_event
&#8221;);<br />
    return 1;<br />
}<br />
/* Ack the event */<br />
ibv_ack_cq_events(ev_cq, 1);<br />
/* Request notification upon the next completion event */<br />
if (ibv_req_notify_cq(ev_cq, 0)) {<br />
    fprintf(stderr, &#8220;Couldn&#8217;t request CQ notification
&#8221;);<br />
    return 1;<br />
}<br />
/* Empty the CQ: poll all of the completions from the CQ (if any exist) */<br />
do {<br />
    ne = ibv_poll_cq(cq, 1, &amp;wc);<br />
    if (ne &lt; 0) {<br />
        fprintf(stderr, &#8220;Failed to poll completions from the CQ
&#8221;);<br />
        return 1;<br />
    }<br />
    /* there may be an extra event with no completion in the CQ */<br />
    if (ne == 0)<br />
        continue;<br />
    if (wc.status != IBV_WC_SUCCESS) {<br />
        fprintf(stderr, &#8220;Completion with status 0x%x was found
&#8221;, wc.status);<br />
        return 1;<br />
    }<br />
} while (ne);</p>
<p> The following code example demonstrates one possible way to work with completion events in non-blocking mode. It performs the following steps: </p>
<p> 1. Set the completion event channel to be non-blocked<br />
 2. Poll the channel until there it has a completion event<br />
 3. Get the completion event and ack it </p>
<pre><code>
/* change the blocking mode of the completion channel */
flags = fcntl(channel-&gt;fd, F_GETFL);
rc = fcntl(channel-&gt;fd, F_SETFL, flags | O_NONBLOCK);
if (rc &lt; 0) {
    fprintf(stderr, "Failed to change file descriptor of completion event channel
");
    return 1;
}
/*
 * poll the channel until it has an event and sleep ms_timeout
 * milliseconds between any iteration
 */
my_pollfd.fd = channel-&gt;fd;
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
ev_cq = cq;
/* Wait for the completion event */
if (ibv_get_cq_event(channel, &amp;ev_cq, &amp;ev_ctx)) {
    fprintf(stderr, "Failed to get cq_event
");
    return 1;
}
/* Ack the event */
ibv_ack_cq_events(ev_cq, 1);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_comp_channel/">ibv_create_comp_channel</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_cq/">ibv_create_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_req_notify_cq/">ibv_req_notify_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a></code>(3) </p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak</p>
<dd> &lt;<i>dotanba [at] gmail.com</i>&gt; </p>
</dl>
<h2>Index</h2>
