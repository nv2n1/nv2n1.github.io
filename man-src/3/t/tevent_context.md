---
title: "tevent_context(3)"
name: "tevent_context"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_context/"
description: "tevent_context – Chapter 1: Tevent context"
---

<p>tevent_context &#8211; Chapter 1: Tevent context</p>
<h2>Tevent with threads</h2>
<p>Tevent context is an essential logical unit of tevent library. For working with events at least one such context has to be created &#8211; allocated, initialized. Then, events which are meant to be caught and handled have to be registered within this specific context. Reason for subordinating events to a tevent context structure rises from the fact that several context can be created and each of them is processed at different time. So, there can be 1 context containing just file descriptor events, another one taking care of signal and time events and the third one which keeps information about the rest. </p>
<p> Tevent loops are the part of the library which represents the mechanism where noticing events and triggering handlers actually happens. They accept just one argument &#8211; tevent context structure. Therefore if theoretically an infinity loop (tevent_loop_wait) was called, only those arguments which belong to the passed tevent context structure can be caught and invoked within this call. Although some more signal events were registered (but within some other context) they will not be noticed.</p>
<h3>Example</h3>
<p>First lines which handle mem_ctx belong to talloc library knowledge but because of the fact that tevent uses the talloc library for its mechanisms it is necessary to understand a bit talloc as well. For more information about working with talloc, please visit talloc website where tutorial and documentation are located. </p>
<p> Tevent context structure *event_ctx represents the unit which will further contain information about registered events. It is created via calling <code>tevent_context_init()</code>. </p>
<pre>TALLOC_CTX *mem_ctx = talloc_new(NULL);
if (mem_ctx == NULL) {
 // error handling
}
struct tevent_context *ev_ctx = tevent_context_init(mem_ctx);
if(ev_ctx == NULL) {
 // error handling
}</pre>
<p>Tevent context has a structure containing lots of information. It include lists of all events which are divided according their type and are in order showing the sequence as they came. </p>
<p> In addition to the lists shown in the diagram, the tevent context also contains many other data (e.g. information about the available system mechanism for triggering callbacks).</p>
<h2>Tevent loops</h2>
<p>Tevent loops are the dispatcher for events. They catch them and trigger the handlers. In the case of longer processes, the program spends most of its time at this point waiting for events, invoking handlers and waiting for another event again. There are 2 types of loop available for use in tevent library: </p>
<dl>
<dt>&bull;</p>
<dd>int <code>tevent_loop_wait()</code></p>
<dt>&bull;</p>
<dd>int <code>tevent_loop_once()</code></dl>
<p> Both of functions accept just one parametr (tevent context) and the only difference lies in the fact that the first loop can theoretically last for ever but the second one will wait just for a single one event to catch and then the loop breaks and the program continue.</p>
<h2>Tevent with threads</h2>
<p>In order to use tevent with threads, you must first understand how to use the talloc library in threaded programs. For more information about working with talloc, please visit talloc website where tutorial and documentation are located. </p>
<p> If a tevent context structure is talloced from a NULL, thread-safe talloc context, then it can be safe to use in a threaded program. The function talloc_disable_null_tracking() <code>must</code> be called from the initial program thread before any talloc calls are made to ensure talloc is thread-safe. </p>
<p> Each thread must create it&#8217;s own tevent context structure as follows tevent_context_init(NULL) and no talloc memory contexts can be shared between threads. </p>
<p> Separate threads using tevent in this way can communicate by writing data into file descriptors that are being monitored by a tevent context on another thread. For example (simplified with no error handling): </p>
<pre>Main thread:
main()
{
 talloc_disable_null_tracking();
 struct tevent_context *master_ev = tevent_context_init(NULL);
 void *mem_ctx = talloc_new(master_ev);
 // Create file descriptor to monitor.
 int pipefds[2];
 pipe(pipefds);
 struct tevent_fd *fde = tevent_add_fd(master_ev,
 mem_ctx,
 pipefds[0], // read side of pipe
 TEVENT_FD_READ,
 pipe_read_handler, // callback function
 private_data_pointer);
 // Create sub thread, pass pipefds[1] write side of pipe to it.
 // The above code not shown here..
 // Process events.
 tevent_loop_wait(master_ev);
 // Cleanup if loop exits.
 talloc_free(master_ev);
}</pre>
<p>When the subthread writes to pipefds[1], the function pipe_read_handler() will be called in the main thread.</p>
<h3>sophisticated use</h3>
<p>A popular way to use an event library within threaded programs is to allow a sub-thread to asynchronously schedule a tevent_immediate function call from the event loop of another thread. This can be built out of the basic functions and isolation mechanisms of tevent, but tevent also comes with some utility functions that make this easier, so long as you understand the limitations that using threads with talloc and tevent impose. </p>
<p> To allow a tevent context to receive an asynchronous tevent_immediate function callback from another thread, create a struct tevent_thread_proxy * by calling </p>
<pre>struct tevent_thread_proxy *tevent_thread_proxy_create(
 struct tevent_context *dest_ev_ctx);</pre>
<p>This function allocates the internal data structures to allow asynchronous callbacks as a talloc child of the struct tevent_context *, and returns a struct tevent_thread_proxy * that can be passed to another thread. </p>
<p> When you have finished receiving asynchronous callbacks, simply talloc_free the struct tevent_thread_proxy *, or talloc_free the struct tevent_context *, which will deallocate the resources used. </p>
<p> To schedule an asynchronous tevent_immediate function call from one thread on the tevent loop of another thread, use </p>
<pre>void tevent_thread_proxy_schedule(struct tevent_thread_proxy *tp,
 struct tevent_immediate **pp_im,
 tevent_immediate_handler_t handler,
 void **pp_private_data);</pre>
<p>This function causes the function handler() to be invoked as a tevent_immediate callback from the event loop of the thread that created the struct tevent_thread_proxy * (so the owning struct tevent_context * should be long-lived and not in the process of being torn down). </p>
<p> The struct tevent_thread_proxy object being used here is a child of the event context of the target thread. So external synchronization mechanisms must be used to ensure that the target object is still in use at the time of the <code>tevent_thread_proxy_schedule()</code> call. In the example below, the request/response nature of the communication ensures this. </p>
<p> The struct tevent_immediate **pp_im passed into this function should be a struct tevent_immediate * allocated on a talloc context local to this thread, and will be reparented via talloc_move to be owned by struct tevent_thread_proxy *tp. *pp_im will be set to NULL on successful scheduling of the tevent_immediate call. </p>
<p> handler() will be called as a normal tevent_immediate callback from the struct tevent_context * of the destination event loop that created the struct tevent_thread_proxy * </p>
<p> Returning from this functions does not mean that the handler has been invoked, merely that it has been scheduled to be called in the destination event loop. </p>
<p> Because the calling thread does not wait for the callback to be scheduled and run on the destination thread, this is a fire-and-forget call. If you wish confirmation of the handler() being successfully invoked, you must ensure it replies to the caller in some way. </p>
<p> Because of asynchronous nature of this call, the nature of the parameter passed to the destination thread has some restructions. If you don&#8217;t need parameters, merely pass NULL as the value of void **pp_private_data. </p>
<p> If you wish to pass a pointer to data between the threads, it <code>MUST</code> be a pointer to a talloced pointer, which is not part of a talloc-pool, and it must not have a destructor attached. The ownership of the memory pointed to will be passed from the calling thread to the tevent library, and if the receiving thread does not talloc-reparent it to its own contexts, it will be freed once the handler is called. </p>
<p> On success, *pp_private will be NULL to signify the talloc memory ownership has been moved. </p>
<p> In practice for message passing between threads in event loops these restrictions are not very onerous. </p>
<p> The easiest way to to a request-reply pair between tevent loops on different threads is to pass the parameter block of memory back and forth using a reply <code>tevent_thread_proxy_schedule()</code> call. </p>
<p> Here is an example (without error checking for simplicity): </p>
<pre>------------------------------------------------
// Master thread.
main()
{
 // Make talloc thread-safe.
 talloc_disable_null_tracking();
 // Create the master event context.
 struct tevent_context *master_ev = tevent_context_init(NULL);
 // Create the master thread proxy to allow it to receive
 // async callbacks from other threads.
 struct tevent_thread_proxy *master_tp =
 tevent_thread_proxy_create(master_ev);
 // Create sub-threads, passing master_tp in
 // some way to them.
 // This code not shown..
 // Process events.
 // Function master_callback() below
 // will be invoked on this thread on
 // master_ev event context.
 tevent_loop_wait(master_ev);
 // Cleanup if loop exits.
 talloc_free(master_ev);
}
// Data passed between threads.
struct reply_state {
 struct tevent_thread_proxy *reply_tp;
 pthread_t thread_id;
 bool *p_finished;
};
// Callback Called in child thread context.
static void thread_callback(struct tevent_context *ev,
 struct tevent_immediate *im,
 void *private_ptr)
{
 // Move the ownership of what private_ptr
 // points to from the tevent library back to this thread.
 struct reply_state *rsp =
 talloc_get_type_abort(private_ptr, struct reply_state);
 talloc_steal(ev, rsp);
 *rsp-&gt;p_finished = true;
 // im will be talloc_freed on return from this call.
 // but rsp will not.
}
// Callback Called in master thread context.
static void master_callback(struct tevent_context *ev,
 struct tevent_immediate *im,
 void *private_ptr)
{
 // Move the ownership of what private_ptr
 // points to from the tevent library to this thread.
 struct reply_state *rsp =
 talloc_get_type_abort(private_ptr, struct reply_state);
 talloc_steal(ev, rsp);
 printf(&quot;Callback from thread %s, thread_id_to_string(rsp-&gt;thread_id));
 /* Now reply to the thread ! */
 tevent_thread_proxy_schedule(rsp-&gt;reply_tp,
 &amp;im,
 thread_callback,
 &amp;rsp);
 // Note - rsp and im are now NULL as the tevent library
 // owns the memory.
}
// Child thread.
static void *thread_fn(void *private_ptr)
{
 struct tevent_thread_proxy *master_tp =
 talloc_get_type_abort(private_ptr, struct tevent_thread_proxy);
 bool finished = false;
 int ret;
 // Create our own event context.
 struct tevent_context *ev = tevent_context_init(NULL);
 // Create the local thread proxy to allow us to receive
 // async callbacks from other threads.
 struct tevent_thread_proxy *local_tp =
 tevent_thread_proxy_create(master_ev);
 // Setup the data to send.
 struct reply_state *rsp = talloc(ev, struct reply_state);
 rsp-&gt;reply_tp = local_tp;
 rsp-&gt;thread_id = pthread_self();
 rsp-&gt;p_finished = &amp;finished;
 // Create the immediate event to use.
 struct tevent_immediate *im = tevent_create_immediate(ev);
 // Call the master thread.
 tevent_thread_proxy_schedule(master_tp,
 &amp;im,
 master_callback,
 &amp;rsp);
 // Note - rsp and im are now NULL as the tevent library
 // owns the memory.
 // Wait for the reply.
 while (!finished) {
 tevent_loop_once(ev);
 }
 // Cleanup.
 talloc_free(ev);
 return NULL;
}</pre>
<p>Note this doesn&#8217;t have to be a master-subthread communication. Any thread that has access to the struct tevent_thread_proxy * pointer of another thread that has called <code>tevent_thread_proxy_create()</code> can send an async tevent_immediate request. </p>
<p> But remember the caveat that external synchronization must be used to ensure the target struct tevent_thread_proxy * object exists at the time of the <code>tevent_thread_proxy_schedule()</code> call or unreproducible crashes will result.</p>
