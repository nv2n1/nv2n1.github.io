---
title: "tevent_queue(3)"
name: "tevent_queue"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_queue/"
description: "The tevent queue functions –"
---

<p>The tevent queue functions &#8211; </p>
<p> A tevent_queue is used to queue up async requests that must be serialized.</p>
<h3>Typedefs</h3>
<p>typedef void(* <code>tevent_queue_trigger_fn_t</code> )(struct tevent_req *req, void *private_data)<br />
 <i>A callback trigger function run by the queue. </i></p>
<h3>Functions</h3>
<p>struct tevent_queue * <code>tevent_queue_create</code> (TALLOC_CTX *mem_ctx, const char *name)<br />
 <i>Create and start a tevent queue. </i><br />
 bool <code>tevent_queue_add</code> (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code> trigger, void *private_data)<br />
 <i>Add a tevent request to the queue. </i><br />
 struct tevent_queue_entry * <code>tevent_queue_add_entry</code> (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code> trigger, void *private_data)<br />
 <i>Add a tevent request to the queue. </i><br />
 struct tevent_queue_entry * <code>tevent_queue_add_optimize_empty</code> (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code> trigger, void *private_data)<br />
 <i>Add a tevent request to the queue using a possible optimization. </i><br />
 void <code>tevent_queue_start</code> (struct tevent_queue *queue)<br />
 <i>Start a tevent queue. </i><br />
 void <code>tevent_queue_stop</code> (struct tevent_queue *queue)<br />
 <i>Stop a tevent queue. </i><br />
 size_t <code>tevent_queue_length</code> (struct tevent_queue *queue)<br />
 <i>Get the length of the queue. </i><br />
 bool <code>tevent_queue_running</code> (struct tevent_queue *queue)<br />
 <i>Is the tevent queue running. </i><br />
 struct tevent_req * <code>tevent_queue_wait_send</code> (TALLOC_CTX *mem_ctx, struct tevent_context *ev, struct tevent_queue *queue)<br />
 <i>Create a tevent subrequest that waits in a tevent_queue. </i><br />
 bool <code>tevent_queue_wait_recv</code> (struct tevent_req *req)<br />
 <i>Check if we no longer need to wait in the queue. </i><br />
 struct tevent_thread_proxy * <code>tevent_thread_proxy_create</code> (struct tevent_context *dest_ev_ctx)<br />
 <i>Create a tevent_thread_proxy for message passing between threads. </i><br />
 void <code>tevent_thread_proxy_schedule</code> (struct tevent_thread_proxy *tp, struct tevent_immediate **pp_im, <code>tevent_immediate_handler_t</code> handler, void *pp_private_data)<br />
 <i>Schedule an immediate event on an event context from another thread. </i></p>
<h2>Detailed Description</h2>
<p>A tevent_queue is used to queue up async requests that must be serialized. </p>
<p> For example writing buffers into a socket must be serialized. Writing a large lump of data into a socket can require multiple <a href="/docs/linux/man/2-write/">write</a>(2) or <a href="/docs/linux/man/2-send/">send</a>(2) system calls. If more than one async request is outstanding to write large buffers into a socket, every request must individually be completed before the next one begins, even if multiple syscalls are required. </p>
<p> Take a look at <code>The tevent_queue tutorial</code> for more details.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* tevent_queue_trigger_fn_t)(struct tevent_req *req, void *private_data)</h3>
<p>A callback trigger function run by the queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request the trigger function is executed on.<br />
 <i>private_data</i> The private data pointer specified by <code>tevent_queue_add()</code>.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_add()</code> </p>
<p> <code>tevent_queue_add_entry()</code> </p>
<p> <code>tevent_queue_add_optimize_empty()</code></dl>
<h2>Function Documentation</h2>
<h3>bool tevent_queue_add (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code>trigger, void *private_data)</h3>
<p>Add a tevent request to the queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to add the request.<br />
 <i>ev</i> The event handle to use for the request.<br />
 <i>req</i> The tevent request to add to the queue.<br />
 <i>trigger</i> The function triggered by the queue when the request is called. Since tevent 0.9.14 it&#8217;s possible to pass NULL, in order to just add a &#8216;blocker&#8217; to the queue.<br />
 <i>private_data</i> The private data passed to the trigger function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if the request has been successfully added, false otherwise.</dl>
<h3>struct tevent_queue_entry* tevent_queue_add_entry (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code>trigger, void *private_data)</h3>
<p>Add a tevent request to the queue. The request can be removed from the queue by calling talloc_free() (or a similar function) on the returned queue entry. This is the only difference to <code>tevent_queue_add()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to add the request.<br />
 <i>ev</i> The event handle to use for the request.<br />
 <i>req</i> The tevent request to add to the queue.<br />
 <i>trigger</i> The function triggered by the queue when the request is called. Since tevent 0.9.14 it&#8217;s possible to pass NULL, in order to just add a &#8216;blocker&#8217; to the queue.<br />
 <i>private_data</i> The private data passed to the trigger function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a pointer to the tevent_queue_entry if the request has been successfully added, NULL otherwise.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_add()</code> </p>
<p> <code>tevent_queue_add_optimize_empty()</code></dl>
<h3>struct tevent_queue_entry* tevent_queue_add_optimize_empty (struct tevent_queue *queue, struct tevent_context *ev, struct tevent_req *req, <code>tevent_queue_trigger_fn_t</code>trigger, void *private_data)</h3>
<p>Add a tevent request to the queue using a possible optimization. This tries to optimize for the empty queue case and may calls the trigger function directly. This is the only difference compared to <code>tevent_queue_add_entry()</code>. </p>
<p> The caller needs to be prepared that the trigger function has already called <code>tevent_req_notify_callback()</code>, <code>tevent_req_error()</code>, <code>tevent_req_done()</code> or a similar function. </p>
<p> The request can be removed from the queue by calling talloc_free() (or a similar function) on the returned queue entry. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to add the request.<br />
 <i>ev</i> The event handle to use for the request.<br />
 <i>req</i> The tevent request to add to the queue.<br />
 <i>trigger</i> The function triggered by the queue when the request is called. Since tevent 0.9.14 it&#8217;s possible to pass NULL, in order to just add a &#8216;blocker&#8217; to the queue.<br />
 <i>private_data</i> The private data passed to the trigger function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>a pointer to the tevent_queue_entry if the request has been successfully added, NULL otherwise.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_add()</code> </p>
<p> <code>tevent_queue_add_entry()</code></dl>
<h3>struct tevent_queue* tevent_queue_create (TALLOC_CTX *mem_ctx, const char *name)</h3>
<p>Create and start a tevent queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The talloc memory context to allocate the queue.<br />
 <i>name</i> The name to use to identify the queue.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated tevent queue on success, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_start()</code> </p>
<p> <code>tevent_queue_stop()</code></dl>
<h3>size_t tevent_queue_length (struct tevent_queue *queue)</h3>
<p>Get the length of the queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to get the length from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of elements.</dl>
<h3>bool tevent_queue_running (struct tevent_queue *queue)</h3>
<p>Is the tevent queue running. The queue is started by default. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Wether the queue is running or not..</dl>
<h3>void tevent_queue_start (struct tevent_queue *queue)</h3>
<p>Start a tevent queue. The queue is started by default. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to start.</dl>
<h3>void tevent_queue_stop (struct tevent_queue *queue)</h3>
<p>Stop a tevent queue. The queue is started by default. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The queue to stop.</dl>
<h3>bool tevent_queue_wait_recv (struct tevent_req *req)</h3>
<p>Check if we no longer need to wait in the queue. This function needs to be called in the callback function set after calling <code>tevent_queue_wait_send()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request to check.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True on success, false otherwise.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_wait_send()</code></dl>
<h3>struct tevent_req* tevent_queue_wait_send (TALLOC_CTX *mem_ctx, struct tevent_context *ev, struct tevent_queue *queue)</h3>
<p>Create a tevent subrequest that waits in a tevent_queue. The idea is that always the same syntax for tevent requests. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The talloc memory context to use.<br />
 <i>ev</i> The event handle to setup the request.<br />
 <i>queue</i> The queue to wait in.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new subrequest, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_queue_wait_recv()</code></dl>
<h3>struct tevent_thread_proxy* tevent_thread_proxy_create (struct tevent_context *dest_ev_ctx)</h3>
<p>Create a tevent_thread_proxy for message passing between threads. The tevent_context must have been allocated on the NULL talloc context, and talloc_disable_null_tracking() must have been called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>dest_ev_ctx</i> The tevent_context to receive events.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated tevent_thread_proxy, NULL on error. If tevent was compiled without PTHREAD support NULL is always returned and errno set to ENOSYS.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_thread_proxy_schedule()</code></dl>
<h3>void tevent_thread_proxy_schedule (struct tevent_thread_proxy *tp, struct tevent_immediate **pp_im, <code>tevent_immediate_handler_t</code>handler, void *pp_private_data)</h3>
<p>Schedule an immediate event on an event context from another thread. Causes dest_ev_ctx, being run by another thread, to receive an immediate event calling the handler with the *pp_private parameter. </p>
<p> *pp_im must be a pointer to an immediate event talloced on a context owned by the calling thread, or the NULL context. Ownership will be transferred to the tevent_thread_proxy and *pp_im will be returned as NULL. </p>
<p> *pp_private_data must be a talloced area of memory with no destructors. Ownership of this memory will be transferred to the tevent library and *pp_private_data will be set to NULL on successful completion of the call. Set pp_private to NULL if no parameter transfer needed (a pure callback). This is an asynchronous request, caller does not wait for callback to be completed before returning. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>tp</i> The tevent_thread_proxy to use.<br />
 <i>pp_im</i> Pointer to immediate event pointer.<br />
 <i>handler</i> The function that will be called.<br />
 <i>pp_private_data</i> The talloced memory to transfer.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_thread_proxy_create()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for tevent from the source code.</p>
