---
title: "tevent_request(3)"
name: "tevent_request"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_request/"
description: "The tevent request functions. –"
---

<p>The tevent request functions. &#8211; </p>
<p> A tevent_req represents an asynchronous computation.</p>
<h3>Typedefs</h3>
<p>typedef void(* <code>tevent_req_fn</code> )(struct tevent_req *req)<br />
 <i>A tevent request callback function. </i><br />
 typedef char *(* <code>tevent_req_print_fn</code> )(struct tevent_req *req, TALLOC_CTX *ctx)<br />
 <i>The print function which can be set for a tevent async request. </i><br />
 typedef bool(* <code>tevent_req_cancel_fn</code> )(struct tevent_req *req)<br />
 <i>A typedef for a cancel function for a tevent request. </i><br />
 typedef void(* <code>tevent_req_cleanup_fn</code> )(struct tevent_req *req, enum <code>tevent_req_state</code> req_state)<br />
 <i>A typedef for a cleanup function for a tevent request. </i></p>
<h3>Enumerations</h3>
<p>enum <code>tevent_req_state</code> { <code>TEVENT_REQ_INIT</code>, <code>TEVENT_REQ_IN_PROGRESS</code>, <code>TEVENT_REQ_DONE</code>, <code>TEVENT_REQ_USER_ERROR</code>, <code>TEVENT_REQ_TIMED_OUT</code>, <code>TEVENT_REQ_NO_MEMORY</code>, <code>TEVENT_REQ_RECEIVED</code> }<br />
 <i>An async request moves from TEVENT_REQ_INIT to TEVENT_REQ_IN_PROGRESS. </i></p>
<h3>Functions</h3>
<p>void <code>tevent_req_set_callback</code> (struct tevent_req *req, <code>tevent_req_fn</code> fn, void *pvt)<br />
 <i>Set an async request callback. </i><br />
 void * <code>tevent_req_callback_data</code> (struct tevent_req *req,#type)<br />
 <i>Get the private data cast to the given type for a callback from a tevent request structure. </i><br />
 void * <code>tevent_req_callback_data_void</code> (struct tevent_req *req)<br />
 <i>Get the private data for a callback from a tevent request structure. </i><br />
 void * <code>tevent_req_data</code> (struct tevent_req *req,#type)<br />
 <i>Get the private data from a tevent request structure. </i><br />
 void <code>tevent_req_set_print_fn</code> (struct tevent_req *req, <code>tevent_req_print_fn</code> fn)<br />
 <i>This function sets a print function for the given request. </i><br />
 char * <code>tevent_req_default_print</code> (struct tevent_req *req, TALLOC_CTX *mem_ctx)<br />
 <i>The default print function for creating debug messages. </i><br />
 char * <code>tevent_req_print</code> (TALLOC_CTX *mem_ctx, struct tevent_req *req)<br />
 <i>Print an tevent_req structure in debug messages. </i><br />
 void <code>tevent_req_set_cancel_fn</code> (struct tevent_req *req, <code>tevent_req_cancel_fn</code> fn)<br />
 <i>This function sets a cancel function for the given tevent request. </i><br />
 bool <code>tevent_req_cancel</code> (struct tevent_req *req)<br />
 <i>Try to cancel the given tevent request. </i><br />
 void <code>tevent_req_set_cleanup_fn</code> (struct tevent_req *req, <code>tevent_req_cleanup_fn</code> fn)<br />
 <i>This function sets a cleanup function for the given tevent request. </i><br />
 struct tevent_req * <code>tevent_req_create</code> (TALLOC_CTX *mem_ctx, void **pstate,#type)<br />
 <i>Create an async tevent request. </i><br />
 bool <code>tevent_req_set_endtime</code> (struct tevent_req *req, struct tevent_context *ev, struct timeval endtime)<br />
 <i>Set a timeout for an async request. </i><br />
 void <code>tevent_req_notify_callback</code> (struct tevent_req *req)<br />
 <i>Call the notify callback of the given tevent request manually. </i><br />
 void <code>tevent_req_done</code> (struct tevent_req *req)<br />
 <i>An async request has successfully finished. </i><br />
 bool <code>tevent_req_error</code> (struct tevent_req *req, uint64_t error)<br />
 <i>An async request has seen an error. </i><br />
 bool <code>tevent_req_nomem</code> (const void *p, struct tevent_req *req)<br />
 <i>Helper function for nomem check. </i><br />
 void <code>tevent_req_oom</code> (struct tevent_req *req)<br />
 <i>Indicate out of memory to a request. </i><br />
 struct tevent_req * <code>tevent_req_post</code> (struct tevent_req *req, struct tevent_context *ev)<br />
 <i>Finish a request before the caller had the change to set the callback. </i><br />
 void <code>tevent_req_defer_callback</code> (struct tevent_req *req, struct tevent_context *ev)<br />
 <i>Finish multiple requests within one function. </i><br />
 bool <code>tevent_req_is_in_progress</code> (struct tevent_req *req)<br />
 <i>Check if the given request is still in progress. </i><br />
 bool <code>tevent_req_poll</code> (struct tevent_req *req, struct tevent_context *ev)<br />
 <i>Actively poll for the given request to finish. </i><br />
 bool <code>tevent_req_is_error</code> (struct tevent_req *req, enum <code>tevent_req_state</code> *state, uint64_t *error)<br />
 <i>Get the tevent request state and the actual error set by tevent_req_error. </i><br />
 void <code>tevent_req_received</code> (struct tevent_req *req)<br />
 <i>Use as the last action of a _recv() function. </i><br />
 struct tevent_req * <code>tevent_wakeup_send</code> (TALLOC_CTX *mem_ctx, struct tevent_context *ev, struct timeval wakeup_time)<br />
 <i>Create a tevent subrequest at a given time. </i><br />
 bool <code>tevent_wakeup_recv</code> (struct tevent_req *req)<br />
 <i>Check if the wakeup has been correctly executed. </i></p>
<h2>Detailed Description</h2>
<p>A tevent_req represents an asynchronous computation. </p>
<p> The tevent_req group of API calls is the recommended way of programming async computations within tevent. In particular the file descriptor (tevent_add_fd) and timer (tevent_add_timed) events are considered too low-level to be used in larger computations. To read and write from and to sockets, Samba provides two calls on top of tevent_add_fd: tstream_read_packet_send/recv and tstream_writev_send/recv. These requests are much easier to compose than the low-level event handlers called from tevent_add_fd. </p>
<p> A lot of the simplicity tevent_req has brought to the notoriously hairy async programming came via a set of conventions that every async computation programmed should follow. One central piece of these conventions is the naming of routines and variables. </p>
<p> Every async computation needs a name (sensibly called &#8216;computation&#8217; down from here). From this name quite a few naming conventions are derived. </p>
<p> Every computation that requires local state needs a </p>
<pre>* struct computation_state {
* int local_var;
* };
* </pre>
<p>&nbsp;<wbr>Even if no local variables are required, such a state struct should be created containing a dummy variable. Quite a few helper functions and macros&nbsp;<wbr>(for example&nbsp;<wbr><code>tevent_req_create()</code>)&nbsp;<wbr>assume such a state struct. </p>
<p> An async computation is started by a computation_send function. When it is finished, its result can be received by a computation_recv function. For an example how to set up an async computation, see the code example in the documentation for <code>tevent_req_create()</code> and <code>tevent_req_post()</code>. The prototypes for _send and _recv functions should follow some conventions: </p>
<pre>* struct tevent_req *computation_send(TALLOC_CTX *mem_ctx,
* struct tevent_req *ev,
* ... further args);
* int computation_recv(struct tevent_req *req, ... further output args);
* </pre>
<p>The &#8216;int&#8217; result of computation_recv() depends on the result the sync version of the function would have, &#8216;int&#8217; is just an example here. </p>
<p> Another important piece of the conventions is that the program flow is interrupted as little as possible. Because a blocking sub-computation requires that the flow needs to continue in a separate function that is the logical sequel of some computation, it should lexically follow sending off the blocking sub-computation. Setting the callback function via <code>tevent_req_set_callback()</code> requires referencing a function lexically below the call to <code>tevent_req_set_callback()</code>, forward declarations are required. A lot of the async computations thus begin with a sequence of declarations such as </p>
<pre>* static void computation_step1_done(struct tevent_req *subreq);
* static void computation_step2_done(struct tevent_req *subreq);
* static void computation_step3_done(struct tevent_req *subreq);
* </pre>
<p>It really helps readability a lot to do these forward declarations, because the lexically sequential program flow makes the async computations almost as clear to read as a normal, sync program flow. </p>
<p> It is up to the user of the async computation to talloc_free it after it has finished. If an async computation should be aborted, the tevent_req structure can be talloc_free&#8217;ed. After it has finished, it should talloc_free&#8217;ed by the API user.</p>
<h2>Typedef Documentation</h2>
<h3>typedef bool(* tevent_req_cancel_fn)(struct tevent_req *req)</h3>
<p>A typedef for a cancel function for a tevent request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request calling this function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if the request could be canceled, false if not.</dl>
<h3>typedef void(* tevent_req_cleanup_fn)(struct tevent_req *req, enum <code>tevent_req_state</code> req_state)</h3>
<p>A typedef for a cleanup function for a tevent request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request calling this function.<br />
 <i>req_state</i> The current tevent_req_state.</dl>
<h3>typedef void(* tevent_req_fn)(struct tevent_req *req)</h3>
<p>A tevent request callback function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent async request which executed this callback.</dl>
<h3>typedef char*(* tevent_req_print_fn)(struct tevent_req *req, TALLOC_CTX *ctx)</h3>
<p>The print function which can be set for a tevent async request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent async request.<br />
 <i>ctx</i> A talloc memory context which can be uses to allocate memory.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated string buffer to print.</dl>
<p> Example: </p>
<pre>* static char *my_print(struct tevent_req *req, TALLOC_CTX *mem_ctx)
* {
* struct my_data *data = tevent_req_data(req, struct my_data);
* char *result;
*
* result = tevent_req_default_print(mem_ctx, req);
* if (result == NULL) {
* return NULL;
* }
*
* return talloc_asprintf_append_buffer(result, &quot;foo=%d, bar=%d&quot;,
* data-&gt;foo, data-&gt;bar);
* }
* </pre>
<p>&nbsp;<wbr></p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>tevent_req_state</code></h3>
<p>An async request moves from TEVENT_REQ_INIT to TEVENT_REQ_IN_PROGRESS. All other states are valid after a request has finished. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>TEVENT_REQ_INIT </i></p>
<dd>We are creating the request.</p>
<dt><i>TEVENT_REQ_IN_PROGRESS </i></p>
<dd>We are waiting the request to complete.</p>
<dt><i>TEVENT_REQ_DONE </i></p>
<dd>The request is finished successfully.</p>
<dt><i>TEVENT_REQ_USER_ERROR </i></p>
<dd>A user error has occurred. The user error has been indicated by <code>tevent_req_error()</code>, it can be retrieved via <code>tevent_req_is_error()</code>.</p>
<dt><i>TEVENT_REQ_TIMED_OUT </i></p>
<dd>Request timed out after the timeout set by tevent_req_set_endtime.</p>
<dt><i>TEVENT_REQ_NO_MEMORY </i></p>
<dd>An internal allocation has failed, or tevent_req_nomem has been given a NULL pointer as the first argument.</p>
<dt><i>TEVENT_REQ_RECEIVED </i></p>
<dd>The request has been received by the caller. No further action is valid.</dl>
<h2>Function Documentation</h2>
<h3>void* tevent_req_callback_data (struct tevent_req *req, #type)</h3>
<p>Get the private data cast to the given type for a callback from a tevent request structure. </p>
<pre>* static void computation_done(struct tevent_req *subreq) {
* struct tevent_req *req = tevent_req_callback_data(subreq, struct tevent_req);
* struct computation_state *state = tevent_req_data(req, struct computation_state);
* .... more things, eventually maybe call tevent_req_done(req);
* }
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>req</i> The structure to get the callback data from.<br />
 <i>type</i> The type of the private callback data to get.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The type casted private data set NULL if not set.</dl>
<h3>void* tevent_req_callback_data_void (struct tevent_req *req)</h3>
<p>Get the private data for a callback from a tevent request structure. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The structure to get the callback data from.<br />
 <i>req</i> The structure to get the data from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The private data or NULL if not set.</dl>
<h3>bool tevent_req_cancel (struct tevent_req *req)</h3>
<p>Try to cancel the given tevent request. This function can be used to cancel the given request. </p>
<p> It is only possible to cancel a request when the implementation has registered a cancel function via the <code>tevent_req_set_cancel_fn()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>This function returns true is the request is cancelable, othererwise false is returned.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>Even if the function returns true, the caller need to wait for the function to complete normally. Only the _recv() function of the given request indicates if the request was really canceled.</dl>
<h3>struct tevent_req* tevent_req_create (TALLOC_CTX *mem_ctx, void **pstate, #type)</h3>
<p>Create an async tevent request. The new async request will be initialized in state TEVENT_REQ_IN_PROGRESS. </p>
<pre>* struct tevent_req *req;
* struct computation_state *state;
* req = tevent_req_create(mem_ctx, &amp;state, struct computation_state);
* </pre>
<p>Tevent_req_create() allocates and zeros the state variable as a talloc child of its result. The state variable should be used as the talloc parent for all temporary variables that are allocated during the async computation. This way, when the user of the async computation frees the request, the state as a talloc child will be free&#8217;d along with all the temporary variables hanging off the state. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context for the result.<br />
 <i>pstate</i> Pointer to the private request state.<br />
 <i>type</i> The name of the request.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new async request. NULL on error.</dl>
<h3>void* tevent_req_data (struct tevent_req *req, #type)</h3>
<p>Get the private data from a tevent request structure. When the tevent_req has been created by tevent_req_create, the result of <code>tevent_req_data()</code> is the state variable created by <code>tevent_req_create()</code> as a child of the req. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The structure to get the private data from.<br />
 <i>type</i> The type of the private data</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The private data or NULL if not set.</dl>
<h3>char* tevent_req_default_print (struct tevent_req *req, TALLOC_CTX *mem_ctx)</h3>
<p>The default print function for creating debug messages. The function should not be used by users of the async API, but custom print function can use it and append custom text to the string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to be printed.<br />
 <i>mem_ctx</i> The memory context for the result.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Text representation of request.</dl>
<h3>void tevent_req_defer_callback (struct tevent_req *req, struct tevent_context *ev)</h3>
<p>Finish multiple requests within one function. Normally <code>tevent_req_notify_callback()</code> and all wrappers (e.g. <code>tevent_req_done()</code> and <code>tevent_req_error()</code>) need to be the last thing an event handler should call. This is because the callback is likely to destroy the context of the current function. </p>
<p> If a function wants to notify more than one caller, it is dangerous if it just triggers multiple callbacks in a row. With <code>tevent_req_defer_callback()</code> it is possible to set an event context that will be used to defer the callback via an immediate event (similar to <code>tevent_req_post()</code>). </p>
<pre>* struct complete_state {
* struct tevent_context *ev;
*
* struct tevent_req **reqs;
* };
*
* void complete(struct complete_state *state)
* {
* size_t i, c = talloc_array_length(state-&gt;reqs);
*
* for (i=0; i &lt; c; i++) {
* tevent_req_defer_callback(state-&gt;reqs[i], state-&gt;ev);
* tevent_req_done(state-&gt;reqs[i]);
* }
* }
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>req</i> The finished request.<br />
 <i>ev</i> The tevent_context for the immediate event.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The given request will be returned.</dl>
<h3>void tevent_req_done (struct tevent_req *req)</h3>
<p>An async request has successfully finished. This function is to be used by implementors of async requests. When a request is successfully finished, this function calls the user&#8217;s completion function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The finished request.</dl>
<h3>bool tevent_req_error (struct tevent_req *req, uint64_terror)</h3>
<p>An async request has seen an error. This function is to be used by implementors of async requests. When a request can not successfully completed, the implementation should call this function with the appropriate status code. </p>
<p> If error is 0 the function returns false and does nothing more. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request with an error.<br />
 <i>error</i> The error code.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>On success true is returned, false if error is 0.</dl>
<pre>* int error = first_function();
* if (tevent_req_error(req, error)) {
* return;
* }
*
* error = second_function();
* if (tevent_req_error(req, error)) {
* return;
* }
*
* tevent_req_done(req);
* return;
* </pre>
<p>&nbsp;<wbr></p>
<h3>bool tevent_req_is_error (struct tevent_req *req, enum <code>tevent_req_state</code> *state, uint64_t *error)</h3>
<p>Get the tevent request state and the actual error set by tevent_req_error. </p>
<pre>* int computation_recv(struct tevent_req *req, uint64_t *perr)
* {
* enum tevent_req_state state;
* uint64_t err;
* if (tevent_req_is_error(req, &amp;state, &amp;err)) {
* *perr = err;
* return -1;
* }
* return 0;
* }
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request to get the error from.<br />
 <i>state</i> A pointer to store the tevent request error state.<br />
 <i>error</i> A pointer to store the error set by <code>tevent_req_error()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if the function could set error and state, false otherwise.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_req_error()</code></dl>
<h3>bool tevent_req_is_in_progress (struct tevent_req *req)</h3>
<p>Check if the given request is still in progress. It is typically used by sync wrapper functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to poll.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The boolean form of &#8216;is in progress&#8217;.</dl>
<h3>bool tevent_req_nomem (const void *p, struct tevent_req *req)</h3>
<p>Helper function for nomem check. Convenience helper to easily check alloc failure within a callback implementing the next step of an async request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>p</i> The pointer to be checked.<br />
 <i>req</i> The request being processed.</dl>
<pre>* p = talloc(mem_ctx, bla);
* if (tevent_req_nomem(p, req)) {
* return;
* }
* </pre>
<p>&nbsp;<wbr></p>
<h3>void tevent_req_notify_callback (struct tevent_req *req)</h3>
<p>Call the notify callback of the given tevent request manually. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request to call the notify function from.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_req_set_callback()</code></dl>
<h3>void tevent_req_oom (struct tevent_req *req)</h3>
<p>Indicate out of memory to a request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request being processed.</dl>
<h3>bool tevent_req_poll (struct tevent_req *req, struct tevent_context *ev)</h3>
<p>Actively poll for the given request to finish. This function is typically used by sync wrapper functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to poll.<br />
 <i>ev</i> The tevent_context to be used.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>On success true is returned. If a critical error has happened in the tevent loop layer false is returned. This is not the return value of the given request!</dl>
<p> <code>Note:</code></p>
<dl>
<dd>This should only be used if the given tevent context was created by the caller, to avoid event loop nesting.</dl>
<pre>* req = tstream_writev_queue_send(mem_ctx,
* ev_ctx,
* tstream,
* send_queue,
* iov, 2);
* ok = tevent_req_poll(req, tctx-&gt;ev);
* rc = tstream_writev_queue_recv(req, &amp;sys_errno);
* TALLOC_FREE(req);
* </pre>
<p>&nbsp;<wbr></p>
<h3>struct tevent_req* tevent_req_post (struct tevent_req *req, struct tevent_context *ev)</h3>
<p>Finish a request before the caller had the change to set the callback. An implementation of an async request might find that it can either finish the request without waiting for an external event, or it can not even start the engine. To present the illusion of a callback to the user of the API, the implementation can call this helper function which triggers an immediate event. This way the caller can use the same calling conventions, independent of whether the request was actually deferred. </p>
<pre>* struct tevent_req *computation_send(TALLOC_CTX *mem_ctx,
* struct tevent_context *ev)
* {
* struct tevent_req *req, *subreq;
* struct computation_state *state;
* req = tevent_req_create(mem_ctx, &amp;state, struct computation_state);
* if (req == NULL) {
* return NULL;
* }
* subreq = subcomputation_send(state, ev);
* if (tevent_req_nomem(subreq, req)) {
* return tevent_req_post(req, ev);
* }
* tevent_req_set_callback(subreq, computation_done, req);
* return req;
* }
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>req</i> The finished request.<br />
 <i>ev</i> The tevent_context for the immediate event.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The given request will be returned.</dl>
<h3>char* tevent_req_print (TALLOC_CTX *mem_ctx, struct tevent_req *req)</h3>
<p>Print an tevent_req structure in debug messages. This function should be used by callers of the async API. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context for the result.<br />
 <i>req</i> The request to be printed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Text representation of request.</dl>
<h3>void tevent_req_received (struct tevent_req *req)</h3>
<p>Use as the last action of a _recv() function. This function destroys the attached private data. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The finished request.</dl>
<h3>void tevent_req_set_callback (struct tevent_req *req, <code>tevent_req_fn</code>fn, void *pvt)</h3>
<p>Set an async request callback. See the documentation of <code>tevent_req_post()</code> for an example how this is supposed to be used. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The async request to set the callback.<br />
 <i>fn</i> The callback function to set.<br />
 <i>pvt</i> A pointer to private data to pass to the async request callback.</dl>
<h3>void tevent_req_set_cancel_fn (struct tevent_req *req, <code>tevent_req_cancel_fn</code>fn)</h3>
<p>This function sets a cancel function for the given tevent request. This function can be used to setup a cancel function for the given request. This will be triggered if the <code>tevent_req_cancel()</code> function was called on the given request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to use.<br />
 <i>fn</i> A pointer to the cancel function.</dl>
<h3>void tevent_req_set_cleanup_fn (struct tevent_req *req, <code>tevent_req_cleanup_fn</code>fn)</h3>
<p>This function sets a cleanup function for the given tevent request. This function can be used to setup a cleanup function for the given request. This will be triggered when the <code>tevent_req_done()</code> or <code>tevent_req_error()</code> function was called, before notifying the callers callback function, and also before scheduling the deferred trigger. </p>
<p> This might be useful if more than one tevent_req belong together and need to finish both requests at the same time. </p>
<p> The cleanup function is able to call <code>tevent_req_done()</code> or <code>tevent_req_error()</code> recursively, the cleanup function is only triggered the first time. </p>
<p> The cleanup function is also called by <code>tevent_req_received()</code> (possibly triggered from tevent_req_destructor()) before destroying the private data of the tevent_req. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to use.<br />
 <i>fn</i> A pointer to the cancel function.</dl>
<h3>bool tevent_req_set_endtime (struct tevent_req *req, struct tevent_context *ev, struct timevalendtime)</h3>
<p>Set a timeout for an async request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to set the timeout for.<br />
 <i>ev</i> The event context to use for the timer.<br />
 <i>endtime</i> The endtime of the request.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if succeeded, false if not.</dl>
<h3>void tevent_req_set_print_fn (struct tevent_req *req, <code>tevent_req_print_fn</code>fn)</h3>
<p>This function sets a print function for the given request. This function can be used to setup a print function for the given request. This will be triggered if the <code>tevent_req_print()</code> function was called on the given request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The request to use.<br />
 <i>fn</i> A pointer to the print function</dl>
<p> <code>Note:</code></p>
<dl>
<dd>This function should only be used for debugging.</dl>
<h3>bool tevent_wakeup_recv (struct tevent_req *req)</h3>
<p>Check if the wakeup has been correctly executed. This function needs to be called in the callback function set after calling <code>tevent_wakeup_send()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>req</i> The tevent request to check.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True on success, false otherwise.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_wakeup_recv()</code></dl>
<h3>struct tevent_req* tevent_wakeup_send (TALLOC_CTX *mem_ctx, struct tevent_context *ev, struct timevalwakeup_time)</h3>
<p>Create a tevent subrequest at a given time. The idea is that always the same syntax for tevent requests. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The talloc memory context to use.<br />
 <i>ev</i> The event handle to setup the request.<br />
 <i>wakeup_time</i> The time to wakeup and execute the request.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new subrequest, NULL on error.</dl>
<p> Example: </p>
<pre>* static void my_callback_wakeup_done(tevent_req *subreq)
* {
* struct tevent_req *req = tevent_req_callback_data(subreq,
* struct tevent_req);
* bool ok;
*
* ok = tevent_wakeup_recv(subreq);
* TALLOC_FREE(subreq);
* if (!ok) {
* tevent_req_error(req, -1);
* return;
* }
* ...
* }
* </pre>
<pre>* subreq = tevent_wakeup_send(mem_ctx, ev, wakeup_time);
* if (tevent_req_nomem(subreq, req)) {
* return false;
* }
* tevent_set_callback(subreq, my_callback_wakeup_done, req);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>tevent_wakeup_recv()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for tevent from the source code.</p>
