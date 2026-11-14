---
title: "tevent(3)"
name: "tevent"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent/"
description: "The tevent API – The tevent low-level API."
---

<p>The tevent API &#8211; The tevent low-level API.</p>
<h3>Modules</h3>
<p><code>The tevent request functions.</code><br />
 <i>A tevent_req represents an asynchronous computation. </i><br />
 <code>The tevent helper functiions</code> </p>
<p> <code>The tevent queue functions</code><br />
 <i>A tevent_queue is used to queue up async requests that must be serialized. </i><br />
 <code>The tevent operation functions</code><br />
 <i>The following structure and registration functions are exclusively needed for people writing and pluggin a different event engine. </i><br />
 <code>The tevent compatibility functions</code><br />
 <i>The following definitions are usueful only for compatibility with the implementation originally developed within the samba4 code and will be soon removed. </i></p>
<h3>Macros</h3>
<pre><code>#define TEVENT_FD_READ   1


Monitor a file descriptor for write availability.


#define TEVENT_FD_WRITE   2


Monitor a file descriptor for data to be read.


#define TEVENT_FD_WRITEABLE(fde)   tevent_fd_set_flags(fde, tevent_fd_get_flags(fde) | TEVENT_FD_WRITE)


Convenience function for declaring a tevent_fd writable.


#define TEVENT_FD_READABLE(fde)   tevent_fd_set_flags(fde, tevent_fd_get_flags(fde) | TEVENT_FD_READ)


Convenience function for declaring a tevent_fd readable.


#define TEVENT_FD_NOT_WRITEABLE(fde)   tevent_fd_set_flags(fde, tevent_fd_get_flags(fde) &amp; ~TEVENT_FD_WRITE)


Convenience function for declaring a tevent_fd non-writable.


#define TEVENT_FD_NOT_READABLE(fde)   tevent_fd_set_flags(fde, tevent_fd_get_flags(fde) &amp; ~TEVENT_FD_READ)


Convenience function for declaring a tevent_fd non-readable.



Typedefs</code></pre>
<p> typedef void(* <code>tevent_fd_handler_t</code> )(struct tevent_context *ev, struct tevent_fd *fde, uint16_t flags, void *private_data)<br />
 <i>Called when a file descriptor monitored by tevent has data to be read or written on it. </i><br />
 typedef void(* <code>tevent_fd_close_fn_t</code> )(struct tevent_context *ev, struct tevent_fd *fde, int fd, void *private_data)<br />
 <i>Called when tevent is ceasing the monitoring of a file descriptor. </i><br />
 typedef void(* <code>tevent_timer_handler_t</code> )(struct tevent_context *ev, struct tevent_timer *te, struct timeval current_time, void *private_data)<br />
 <i>Called when a tevent timer has fired. </i><br />
 typedef void(* <code>tevent_immediate_handler_t</code> )(struct tevent_context *ctx, struct tevent_immediate *im, void *private_data)<br />
 <i>Called when a tevent immediate event is invoked. </i><br />
 typedef void(* <code>tevent_signal_handler_t</code> )(struct tevent_context *ev, struct tevent_signal *se, int signum, int count, void *siginfo, void *private_data)<br />
 <i>Called after tevent detects the specified signal. </i><br />
 typedef void(* <code>tevent_debug_fn</code> )(void *context, enum <code>tevent_debug_level</code> level, const char *fmt, va_list ap)<br />
 <i>The tevent debug callbac. </i></p>
<h3>Enumerations</h3>
<p>enum <code>tevent_debug_level</code><br />
 <i>Debug level of tevent. </i><br />
 enum <code>tevent_trace_point</code> { <code>TEVENT_TRACE_BEFORE_WAIT</code>, <code>TEVENT_TRACE_AFTER_WAIT</code>, <code>TEVENT_TRACE_BEFORE_LOOP_ONCE</code>, <code>TEVENT_TRACE_AFTER_LOOP_ONCE</code> }</p>
<h3>Functions</h3>
<p>struct tevent_context * <code>tevent_context_init</code> (TALLOC_CTX *mem_ctx)<br />
 <i>Create a event_context structure. </i><br />
 struct tevent_context * <code>tevent_context_init_byname</code> (TALLOC_CTX *mem_ctx, const char *name)<br />
 <i>Create a event_context structure and select a specific backend. </i><br />
 struct tevent_context * <code>tevent_context_init_ops</code> (TALLOC_CTX *mem_ctx, const struct tevent_ops *ops, void *additional_data)<br />
 <i>Create a custom event context. </i><br />
 const char ** <code>tevent_backend_list</code> (TALLOC_CTX *mem_ctx)<br />
 <i>List available backends. </i><br />
 void <code>tevent_set_default_backend</code> (const char *backend)<br />
 <i>Set the default tevent backend. </i><br />
 struct tevent_fd * <code>tevent_add_fd</code> (struct tevent_context *ev, TALLOC_CTX *mem_ctx, int fd, uint16_t flags, <code>tevent_fd_handler_t</code> handler, void *private_data)<br />
 <i>Add a file descriptor based event. </i><br />
 struct tevent_timer * <code>tevent_add_timer</code> (struct tevent_context *ev, TALLOC_CTX *mem_ctx, struct timeval next_event, <code>tevent_timer_handler_t</code> handler, void *private_data)<br />
 <i>Add a timed event. </i><br />
 struct tevent_immediate * <code>tevent_create_immediate</code> (TALLOC_CTX *mem_ctx)<br />
 <i>Initialize an immediate event object. </i><br />
 void <code>tevent_schedule_immediate</code> (struct tevent_immediate *im, struct tevent_context *ctx, <code>tevent_immediate_handler_t</code> handler, void *private_data)<br />
 <i>Schedule an event for immediate execution. </i><br />
 struct tevent_signal * <code>tevent_add_signal</code> (struct tevent_context *ev, TALLOC_CTX *mem_ctx, int signum, int sa_flags, <code>tevent_signal_handler_t</code> handler, void *private_data)<br />
 <i>Add a tevent signal handler. </i><br />
 size_t <code>tevent_num_signals</code> (void)<br />
 <i>the number of supported signals </i><br />
 size_t <code>tevent_sa_info_queue_count</code> (void)<br />
 <i>the number of pending realtime signals </i><br />
 int <code>tevent_loop_once</code> (struct tevent_context *ev)<br />
 <i>Pass a single time through the mainloop. </i><br />
 int <code>tevent_loop_wait</code> (struct tevent_context *ev)<br />
 <i>Run the mainloop. </i><br />
 void <code>tevent_fd_set_close_fn</code> (struct tevent_fd *fde, <code>tevent_fd_close_fn_t</code> close_fn)<br />
 <i>Assign a function to run when a tevent_fd is freed. </i><br />
 void <code>tevent_fd_set_auto_close</code> (struct tevent_fd *fde)<br />
 <i>Automatically close the file descriptor when the tevent_fd is freed. </i><br />
 uint16_t <code>tevent_fd_get_flags</code> (struct tevent_fd *fde)<br />
 <i>Return the flags set on this file descriptor event. </i><br />
 void <code>tevent_fd_set_flags</code> (struct tevent_fd *fde, uint16_t flags)<br />
 <i>Set flags on a file descriptor event. </i><br />
 bool <code>tevent_signal_support</code> (struct tevent_context *ev)<br />
 <i>Query whether tevent supports signal handling. </i><br />
 int <code>tevent_set_debug</code> (struct tevent_context *ev, <code>tevent_debug_fn</code> debug, void *context)<br />
 <i>Set destination for tevent debug messages. </i><br />
 int <code>tevent_set_debug_stderr</code> (struct tevent_context *ev)<br />
 <i>Designate stderr for debug message output. </i><br />
 void <code>tevent_set_trace_callback</code> (struct tevent_context *ev, tevent_trace_callback_t cb, void *private_data)<br />
 <i>Register a callback to be called at certain trace points. </i><br />
 void <code>tevent_get_trace_callback</code> (struct tevent_context *ev, tevent_trace_callback_t *cb, void *private_data)<br />
 <i>Retrieve the current trace callback. </i></p>
<h2>Detailed Description</h2>
<p>The tevent low-level API. </p>
<p> This API provides the public interface to manage events in the tevent mainloop. Functions are provided for managing low-level events such as timer events, fd events and signal handling.</p>
<h2>Typedef Documentation</h2>
<h3>typedef void(* tevent_debug_fn)(void *context, enum <code>tevent_debug_level</code> level, const char *fmt, va_list ap)</h3>
<p>The tevent debug callbac. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> The memory context to use.<br />
 <i>level</i> The debug level.<br />
 <i>fmt</i> The format string.<br />
 <i>ap</i> The arguments for the format string.</dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>tevent_trace_point</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>TEVENT_TRACE_BEFORE_WAIT </i></p>
<dd>Corresponds to a trace point just before waiting.</p>
<dt><i>TEVENT_TRACE_AFTER_WAIT </i></p>
<dd>Corresponds to a trace point just after waiting.</p>
<dt><i>TEVENT_TRACE_BEFORE_LOOP_ONCE </i></p>
<dd>Corresponds to a trace point just before calling the loop_once() backend function.</p>
<dt><i>TEVENT_TRACE_AFTER_LOOP_ONCE </i></p>
<dd>Corresponds to a trace point right after the loop_once() backend function has returned.</dl>
<h2>Function Documentation</h2>
<h3>struct tevent_fd* tevent_add_fd (struct tevent_context *ev, TALLOC_CTX *mem_ctx, intfd, uint16_tflags, <code>tevent_fd_handler_t</code>handler, void *private_data)</h3>
<p>Add a file descriptor based event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> The event context to work on.<br />
 <i>mem_ctx</i> The talloc memory context to use.<br />
 <i>fd</i> The file descriptor to base the event on.<br />
 <i>flags</i> <code>TEVENT_FD_READ</code> or <code>TEVENT_FD_WRITE</code><br />
 <i>handler</i> The callback handler for the event.<br />
 <i>private_data</i> The private data passed to the callback handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The file descriptor based event, NULL on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>To cancel the monitoring of a file descriptor, call talloc_free() on the object returned by this function. </p>
<p> The caller should avoid closing the file descriptor before calling talloc_free()! Otherwise the behaviour is undefined which might result in crashes. See <a rel="nofollow" href="https://bugzilla.samba.org/show_bug.cgi?id=11141">https://bugzilla.samba.org/show_bug.cgi?id=11141</a> for an example.</dl>
<h3>struct tevent_signal* tevent_add_signal (struct tevent_context *ev, TALLOC_CTX *mem_ctx, intsignum, intsa_flags, <code>tevent_signal_handler_t</code>handler, void *private_data)</h3>
<p>Add a tevent signal handler. <code>tevent_add_signal()</code> creates a new event for handling a signal the next time through the mainloop. It implements a very simple traditional signal handler whose only purpose is to add the handler event into the mainloop. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> The event context to work on.<br />
 <i>mem_ctx</i> The talloc memory context to use.<br />
 <i>signum</i> The signal to trap<br />
 <i>handler</i> The callback handler for the signal.<br />
 <i>sa_flags</i> sigaction flags for this signal handler.<br />
 <i>private_data</i> The private data passed to the callback handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The newly-created signal handler event, or NULL on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>To cancel a signal handler, call talloc_free() on the event returned from this function.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_num_signals</code>, <code>tevent_sa_info_queue_count</code></dl>
<h3>struct tevent_timer* tevent_add_timer (struct tevent_context *ev, TALLOC_CTX *mem_ctx, struct timevalnext_event, <code>tevent_timer_handler_t</code>handler, void *private_data)</h3>
<p>Add a timed event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> The event context to work on.<br />
 <i>mem_ctx</i> The talloc memory context to use.<br />
 <i>next_event</i> Timeval specifying the absolute time to fire this event. This is not an offset.<br />
 <i>handler</i> The callback handler for the event.<br />
 <i>private_data</i> The private data passed to the callback handler.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The newly-created timer event, or NULL on error.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>To cancel a timer event before it fires, call talloc_free() on the event returned from this function. This event is automatically talloc_free()-ed after its event handler files, if it hasn&#8217;t been freed yet. </p>
<p> Unlike some mainloops, tevent timers are one-time events. To set up a recurring event, it is necessary to call <code>tevent_add_timer()</code> again during the handler processing. </p>
<p> Due to the internal mainloop processing, a timer set to run immediately will do so after any other pending timers fire, but before any further file descriptor or signal handling events fire. Callers should not rely on this behavior!</dl>
<h3>const char** tevent_backend_list (TALLOC_CTX *mem_ctx)</h3>
<p>List available backends. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A string vector with a terminating NULL element, NULL on error.</dl>
<h3>struct tevent_context* tevent_context_init (TALLOC_CTX *mem_ctx)</h3>
<p>Create a event_context structure. This must be the first events call, and all subsequent calls pass this event_context as the first element. Event handlers also receive this as their first argument. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated tevent context, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_context_init()</code></dl>
<h3>struct tevent_context* tevent_context_init_byname (TALLOC_CTX *mem_ctx, const char *name)</h3>
<p>Create a event_context structure and select a specific backend. This must be the first events call, and all subsequent calls pass this event_context as the first element. Event handlers also receive this as their first argument. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context to use.<br />
 <i>name</i> The name of the backend to use.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated tevent context, NULL on error.</dl>
<h3>struct tevent_context* tevent_context_init_ops (TALLOC_CTX *mem_ctx, const struct tevent_ops *ops, void *additional_data)</h3>
<p>Create a custom event context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The memory context to use.<br />
 <i>ops</i> The function pointer table of the backend.<br />
 <i>additional_data</i> The additional/private data to this instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An allocated tevent context, NULL on error.</dl>
<h3>struct tevent_immediate* tevent_create_immediate (TALLOC_CTX *mem_ctx)</h3>
<p>Initialize an immediate event object. This object can be used to trigger an event to occur immediately after returning from the current event (before any other event occurs) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>mem_ctx</i> The talloc memory context to use as the parent</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>An empty tevent_immediate object. Use tevent_schedule_immediate to populate and use it.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>Available as of tevent 0.9.8</dl>
<h3>uint16_t tevent_fd_get_flags (struct tevent_fd *fde)</h3>
<p>Return the flags set on this file descriptor event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fde</i> File descriptor event to query</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The flags set on the event. See <code>TEVENT_FD_READ</code> and <code>TEVENT_FD_WRITE</code></dl>
<h3>void tevent_fd_set_auto_close (struct tevent_fd *fde)</h3>
<p>Automatically close the file descriptor when the tevent_fd is freed. This function calls close(fd) internally. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fde</i> File descriptor event to auto-close</dl>
<h3>void tevent_fd_set_close_fn (struct tevent_fd *fde, <code>tevent_fd_close_fn_t</code>close_fn)</h3>
<p>Assign a function to run when a tevent_fd is freed. This function is a destructor for the tevent_fd. It does not automatically close the file descriptor. If this is the desired behavior, then it must be performed by the close_fn. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fde</i> File descriptor event on which to set the destructor<br />
 <i>close_fn</i> Destructor to execute when fde is freed</dl>
<h3>void tevent_fd_set_flags (struct tevent_fd *fde, uint16_tflags)</h3>
<p>Set flags on a file descriptor event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fde</i> File descriptor event to set<br />
 <i>flags</i> Flags to set on the event. See <code>TEVENT_FD_READ</code> and <code>TEVENT_FD_WRITE</code></dl>
<h3>void tevent_get_trace_callback (struct tevent_context *ev, tevent_trace_callback_t *cb, void *private_data)</h3>
<p>Retrieve the current trace callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> Event context<br />
 <i>cb</i> Registered trace callback<br />
 <i>private_data</i> Registered data to be passed to callback</dl>
<p> <code>Note:</code></p>
<dl>
<dd>This can be used to allow one component that wants to register a callback to respect the callback that another component has already registered.</dl>
<h3>int tevent_loop_once (struct tevent_context *ev)</h3>
<p>Pass a single time through the mainloop. This will process any appropriate signal, immediate, fd and timer events </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> The event context to process</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Zero on success, nonzero if an internal error occurred</dl>
<h3>int tevent_loop_wait (struct tevent_context *ev)</h3>
<p>Run the mainloop. The mainloop will run until there are no events remaining to be processed </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> The event context to process</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Zero if all events have been processed. Nonzero if an internal error occurred.</dl>
<h3>size_t tevent_num_signals (void)</h3>
<p>the number of supported signals This returns value of the configure time TEVENT_NUM_SIGNALS constant. </p>
<p> The &#8216;signum&#8217; argument of <code>tevent_add_signal()</code> must be less than TEVENT_NUM_SIGNALS. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_add_signal</code></dl>
<h3>size_t tevent_sa_info_queue_count (void)</h3>
<p>the number of pending realtime signals This returns value of TEVENT_SA_INFO_QUEUE_COUNT. </p>
<p> The tevent internals remember the last TEVENT_SA_INFO_QUEUE_COUNT siginfo_t structures for SA_SIGINFO signals. If the system generates more some signals get lost. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>tevent_add_signal</code></dl>
<h3>void tevent_schedule_immediate (struct tevent_immediate *im, struct tevent_context *ctx, <code>tevent_immediate_handler_t</code>handler, void *private_data)</h3>
<p>Schedule an event for immediate execution. This event will occur immediately after returning from the current event (before any other event occurs) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>im</i> The tevent_immediate object to populate and use<br />
 <i>ctx</i> The tevent_context to run this event<br />
 <i>handler</i> The event handler to run when this event fires<br />
 <i>private_data</i> Data to pass to the event handler</dl>
<h3>int tevent_set_debug (struct tevent_context *ev, <code>tevent_debug_fn</code>debug, void *context)</h3>
<p>Set destination for tevent debug messages. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> Event context to debug<br />
 <i>debug</i> Function to handle output printing<br />
 <i>context</i> The context to pass to the debug function.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Always returns 0 as of version 0.9.8</dl>
<p> <code>Note:</code></p>
<dl>
<dd>Default is to emit no debug messages</dl>
<h3>int tevent_set_debug_stderr (struct tevent_context *ev)</h3>
<p>Designate stderr for debug message output. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> Event context to debug</dl>
<p> <code>Note:</code></p>
<dl>
<dd>This function will only output TEVENT_DEBUG_FATAL, TEVENT_DEBUG_ERROR and TEVENT_DEBUG_WARNING messages. For TEVENT_DEBUG_TRACE, please define a function for <code>tevent_set_debug()</code></dl>
<h3>void tevent_set_default_backend (const char *backend)</h3>
<p>Set the default tevent backend. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>backend</i> The name of the backend to set.</dl>
<h3>void tevent_set_trace_callback (struct tevent_context *ev, tevent_trace_callback_tcb, void *private_data)</h3>
<p>Register a callback to be called at certain trace points. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> Event context<br />
 <i>cb</i> Trace callback<br />
 <i>private_data</i> Data to be passed to callback</dl>
<p> <code>Note:</code></p>
<dl>
<dd>The callback will be called at trace points defined by tevent_trace_point. Call with NULL to reset.</dl>
<h3>bool tevent_signal_support (struct tevent_context *ev)</h3>
<p>Query whether tevent supports signal handling. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ev</i> An initialized tevent context</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>True if this platform and tevent context support signal handling</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for tevent from the source code.</p>
