---
title: "rdma_migrate_id(3)"
name: "rdma_migrate_id"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_migrate_id/"
---

rdma_migrate_id - Move a communication identifer to a different event channel.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_migrate_id

    (struct rdma_cm_id *id,

     struct rdma_event_channel *channel);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>An existing communication identifier to migrate.
<dt>channel
<dd>The communication channel that events associated with the allocated rdma_cm_id will be reported on. May be NULL.</dl>

<h2>Description</h2>

Migrates a communication identifier to a different event channel.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

This routine migrates a communication identifier to the specified event channel and moves any pending events associated with the rdma_cm_id to the new channel. Users should not poll for events on the rdma_cm_id's current event channel or invoke other routines on the rdma_cm_id while migrating between channels. This call will block while there are any unacknowledged events on the current event channel. 

 If the channel parameter is NULL, the specified rdma_cm_id will be placed into synchronous operation mode. All calls on the id will block until the operation completes.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_event_channel/">rdma_create_event_channel</a>(3), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
