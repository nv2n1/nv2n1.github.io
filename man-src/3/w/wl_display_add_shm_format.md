---
title: "wl_display_add_shm_format(3)"
name: "wl_display_add_shm_format"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_display_add_shm_format/"
description: "wl_display –"
---

<p>wl_display &#8211; </p>
<p> Represents a connection to the compositor and acts as a proxy to the <code>wl_display</code> singleton object.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-client.h&gt;

Public Member Functions
struct wl_event_queue * wl_display_create_queue (struct wl_display *display)



struct wl_display * wl_display_connect_to_fd (int fd)



struct wl_display * wl_display_connect (const char *name)



void wl_display_disconnect (struct wl_display *display)



int wl_display_get_fd (struct wl_display *display)



int wl_display_roundtrip (struct wl_display *display)



int wl_display_read_events (struct wl_display *display)



int wl_display_prepare_read (struct wl_display *display)



void wl_display_cancel_read (struct wl_display *display)



int wl_display_dispatch_queue (struct wl_display *display, struct wl_event_queue *queue)



int wl_display_dispatch_queue_pending (struct wl_display *display, struct wl_event_queue *queue)



int wl_display_dispatch (struct wl_display *display)



int wl_display_dispatch_pending (struct wl_display *display)



int wl_display_get_error (struct wl_display *display)



int wl_display_flush (struct wl_display *display)



struct wl_client * wl_client_create (struct wl_display *display, int fd)



struct wl_display * wl_display_create (void)



uint32_t wl_display_get_serial (struct wl_display *display)



uint32_t wl_display_next_serial (struct wl_display *display)



uint32_t * wl_display_add_shm_format (struct wl_display *display, uint32_t format)



struct wl_array * wl_display_get_additional_shm_formats (struct wl_display *display)



Public Attributes
struct wl_event_loop * loop



int run



uint32_t id



uint32_t serial



struct wl_list registry_resource_list



struct wl_list global_list



struct wl_list socket_list



struct wl_list client_list



struct wl_signal destroy_signal



struct wl_array additional_shm_formats</code></pre>
<h2>Detailed Description</h2>
<p>Represents a connection to the compositor and acts as a proxy to the <code>wl_display</code> singleton object. </p>
<p> A <code>wl_display</code> object represents a client connection to a Wayland compositor. It is created with either <code>wl_display_connect()</code> or <code>wl_display_connect_to_fd()</code>. A connection is terminated using <code>wl_display_disconnect()</code>. </p>
<p> A <code>wl_display</code> is also used as the <code>wl_proxy</code> for the <code>wl_display</code> singleton object on the compositor side. </p>
<p> A <code>wl_display</code> object handles all the data sent from and to the compositor. When a <code>wl_proxy</code> marshals a request, it will write its wire representation to the display&#8217;s write buffer. The data is sent to the compositor when the client calls <code>wl_display_flush()</code>. </p>
<p> Incoming data is handled in two steps: queueing and dispatching. In the queue step, the data coming from the display fd is interpreted and added to a queue. On the dispatch step, the handler for the incoming event set by the client on the corresponding <code>wl_proxy</code> is called. </p>
<p> A <code>wl_display</code> has at least one event queue, called the <i>main queue</i>. Clients can create additional event queues with <code>wl_display_create_queue()</code> and assign <code>wl_proxy</code>&#8216;s to it. Events occurring in a particular proxy are always queued in its assigned queue. A client can ensure that a certain assumption, such as holding a lock or running from a given thread, is true when a proxy event handler is called by assigning that proxy to an event queue and making sure that this queue is only dispatched when the assumption holds. </p>
<p> The main queue is dispatched by calling <code>wl_display_dispatch()</code>. This will dispatch any events queued on the main queue and attempt to read from the display fd if its empty. Events read are then queued on the appropriate queues according to the proxy assignment. Calling that function makes the calling thread the <i>main thread</i>. </p>
<p> A user created queue is dispatched with <code>wl_display_dispatch_queue()</code>. If there are no events to dispatch this function will block. If this is called by the main thread, this will attempt to read data from the display fd and queue any events on the appropriate queues. If calling from any other thread, the function will block until the main thread queues an event on the queue being dispatched. </p>
<p> A real world example of event queue usage is Mesa&#8217;s implementation of eglSwapBuffers() for the Wayland platform. This function might need to block until a frame callback is received, but dispatching the main queue could cause an event handler on the client to start drawing again. This problem is solved using another event queue, so that only the events handled by the EGL code are dispatched during the block. </p>
<p> This creates a problem where the main thread dispatches a non-main queue, reading all the data from the display fd. If the application would call <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i> after that it would block, even though there might be events queued on the main queue. Those events should be dispatched with <code>wl_display_dispatch_pending()</code> before flushing and blocking.</p>
<h2>Member Function Documentation</h2>
<h3>struct <code>wl_client</code> * wl_client_create (struct <code>wl_display</code> *display, intfd)</h3>
<p>Create a client for the given file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object<br />
 <i>fd</i> The file descriptor for the socket to the client</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The new client object or NULL on failure.</dl>
<p> Given a file descriptor corresponding to one end of a socket, this function will create a <code>wl_client</code> struct and add the new client to the compositors client list. At that point, the client is initialized and ready to run, as if the client had connected to the servers listening socket. When the client eventually sends requests to the compositor, the <code>wl_client</code> argument to the request handler will be the <code>wl_client</code> returned from this function. </p>
<p> The other end of the socket can be passed to <code>wl_display_connect_to_fd()</code> on the client side or used with the WAYLAND_SOCKET environment variable on the client side. </p>
<p> On failure this function sets errno accordingly and returns NULL.</p>
<h3>uint32_t * wl_display_add_shm_format (struct <code>wl_display</code> *display, uint32_tformat)</h3>
<p>Add support for a wl_shm pixel format </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object<br />
 <i>format</i> The wl_shm pixel format to advertise</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A pointer to the wl_shm format that was added to the list or NULL if adding it to the list failed.</dl>
<p> Add the specified wl_shm format to the list of formats the wl_shm object advertises when a client binds to it. Adding a format to the list means that clients will know that the compositor supports this format and may use it for creating wl_shm buffers. The compositor must be able to handle the pixel format when a client requests it. </p>
<p> The compositor by default supports WL_SHM_FORMAT_ARGB8888 and WL_SHM_FORMAT_XRGB8888.</p>
<h3>void wl_display_cancel_read (struct <code>wl_display</code> *display)</h3>
<p>Release exclusive access to display file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> This releases the exclusive access. Useful for canceling the lock when a timed out poll returns fd not readable and we&#8217;re not going to read from the fd anytime soon.</p>
<h3>struct <code>wl_display</code> * wl_display_connect (const char *name)</h3>
<p>Connect to a Wayland display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> Name of the Wayland display to connect to</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A <code>wl_display</code> object or NULL on failure</dl>
<p> Connect to the Wayland display named name. If name is NULL, its value will be replaced with the WAYLAND_DISPLAY environment variable if it is set, otherwise display &#8216;wayland-0&#8217; will be used.</p>
<h3>struct <code>wl_display</code> * wl_display_connect_to_fd (intfd)</h3>
<p>Connect to Wayland display on an already open fd </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>fd</i> The fd to use for the connection</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A <code>wl_display</code> object or NULL on failure</dl>
<p> The <code>wl_display</code> takes ownership of the fd and will close it when the display is destroyed. The fd will also be closed in case of failure.</p>
<h3>struct <code>wl_display</code> * wl_display_create (void)</h3>
<p>Create Wayland display object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>None</i></dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The Wayland display object. Null if failed to create</dl>
<p> This creates the <code>wl_display</code> object.</p>
<h3>struct <code>wl_event_queue</code> * wl_display_create_queue (struct <code>wl_display</code> *display)</h3>
<p>Create a new event queue for this display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new event queue associated with this display or NULL on failure.</dl>
<h3>void wl_display_disconnect (struct <code>wl_display</code> *display)</h3>
<p>Close a connection to a Wayland display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> Close the connection to display and free all resources associated with it.</p>
<h3>int wl_display_dispatch (struct <code>wl_display</code> *display)</h3>
<p>Process incoming events </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Dispatch the display&#8217;s main event queue. </p>
<p> If the main event queue is empty, this function blocks until there are events to be read from the display fd. Events are read and queued on the appropriate event queues. Finally, events on the main event queue are dispatched. </p>
<p> <code>Note:</code></p>
<dl>
<dd>It is not possible to check if there are events on the main queue or not. For dispatching main queue events without blocking, see <code>wl_display_dispatch_pending()</code>. </p>
<p> Calling this will release the display file descriptor if this thread acquired it using wl_display_acquire_fd().</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>wl_display_dispatch_pending()</code>, <code>wl_display_dispatch_queue()</code></dl>
<h3>int wl_display_dispatch_pending (struct <code>wl_display</code> *display)</h3>
<p>Dispatch main queue events without reading from the display fd </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events or -1 on failure</dl>
<p> This function dispatches events on the main event queue. It does not attempt to read the display fd and simply returns zero if the main queue is empty, i.e., it doesn&#8217;t block. </p>
<p> This is necessary when a client&#8217;s main loop wakes up on some fd other than the display fd (network socket, timer fd, etc) and calls <code>wl_display_dispatch_queue()</code> from that callback. This may queue up events in the main queue while reading all data from the display fd. When the main thread returns to the main loop to block, the display fd no longer has data, causing a call to <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i> (or similar functions) to block indefinitely, even though there are events ready to dispatch. </p>
<p> To proper integrate the wayland display fd into a main loop, the client should always call <code>wl_display_dispatch_pending()</code> and then <code>wl_display_flush()</code> prior to going back to sleep. At that point, the fd typically doesn&#8217;t have data so attempting I/O could block, but events queued up on the main queue should be dispatched. </p>
<p> A real-world example is a main loop that wakes up on a timerfd (or a sound card fd becoming writable, for example in a video player), which then triggers GL rendering and eventually eglSwapBuffers(). eglSwapBuffers() may call <code>wl_display_dispatch_queue()</code> if it didn&#8217;t receive the frame event for the previous frame, and as such queue events in the main queue. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Calling this makes the current thread the main one.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>wl_display_dispatch()</code>, <code>wl_display_dispatch_queue()</code>, <code>wl_display_flush()</code></dl>
<h3>int wl_display_dispatch_queue (struct <code>wl_display</code> *display, struct <code>wl_event_queue</code> *queue)</h3>
<p>Dispatch events in an event queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object<br />
 <i>queue</i> The event queue to dispatch</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Dispatch all incoming events for objects assigned to the given event queue. On failure -1 is returned and errno set appropriately. </p>
<p> This function blocks if there are no events to dispatch. If calling from the main thread, it will block reading data from the display fd. For other threads this will block until the main thread queues events on the queue passed as argument.</p>
<h3>int wl_display_dispatch_queue_pending (struct <code>wl_display</code> *display, struct <code>wl_event_queue</code> *queue)</h3>
<p>Dispatch pending events in an event queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object<br />
 <i>queue</i> The event queue to dispatch</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Dispatch all incoming events for objects assigned to the given event queue. On failure -1 is returned and errno set appropriately. If there are no events queued, this function returns immediately. </p>
<p> <code>Since:</code></p>
<dl>
<dd>1.0.2</dl>
<h3>int wl_display_flush (struct <code>wl_display</code> *display)</h3>
<p>Send all buffered requests on the display to the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of bytes sent on success or -1 on failure</dl>
<p> Send all buffered data on the client side to the server. Clients should call this function before blocking. On success, the number of bytes sent to the server is returned. On failure, this function returns -1 and errno is set appropriately. </p>
<p> <code>wl_display_flush()</code> never blocks. It will write as much data as possible, but if all data could not be written, errno will be set to EAGAIN and -1 returned. In that case, use poll on the display file descriptor to wait for it to become writable again.</p>
<h3>struct <code>wl_array</code> * wl_display_get_additional_shm_formats (struct <code>wl_display</code> *display)</h3>
<p>Get list of additional wl_shm pixel formats </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function returns the list of addition wl_shm pixel formats that the compositor supports. WL_SHM_FORMAT_ARGB8888 and WL_SHM_FORMAT_XRGB8888 are always supported and not included in the array, but all formats added through <code>wl_display_add_shm_format()</code> will be in the array. </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>wl_display_add_shm_format()</code></dl>
<h3>int wl_display_get_error (struct <code>wl_display</code> *display)</h3>
<p>Retrieve the last error that occurred on a display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The last error that occurred on display or 0 if no error occurred</dl>
<p> Return the last error that occurred on the display. This may be an error sent by the server or caused by the local client. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Errors are <code>fatal</code>. If this function returns non-zero the display can no longer be used.</dl>
<h3>int wl_display_get_fd (struct <code>wl_display</code> *display)</h3>
<p>Get a display context&#8217;s file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Display object file descriptor</dl>
<p> Return the file descriptor associated with a display so it can be integrated into the client&#8217;s main loop.</p>
<h3>uint32_t wl_display_get_serial (struct <code>wl_display</code> *display)</h3>
<p>Get the current serial number </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function returns the most recent serial number, but does not increment it.</p>
<h3>uint32_t wl_display_next_serial (struct <code>wl_display</code> *display)</h3>
<p>Get the next serial number </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function increments the display serial number and returns the new value.</p>
<h3>int wl_display_prepare_read (struct <code>wl_display</code> *display)</h3>
<p>Prepare to read events after polling file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success or -1 if event queue was not empty</dl>
<p> This function must be called before reading from the file descriptor using <code>wl_display_read_events()</code>. Calling <code>wl_display_prepare_read()</code> announces the calling threads intention to read and ensures that until the thread is ready to read and calls <code>wl_display_read_events()</code>, no other thread will read from the file descriptor. This only succeeds if the event queue is empty though, and if there are undispatched events in the queue, -1 is returned and errno set to EAGAIN. </p>
<p> If a thread successfully calls <code>wl_display_prepare_read()</code>, it must either call <code>wl_display_read_events()</code> when it&#8217;s ready or cancel the read intention by calling <code>wl_display_cancel_read()</code>. </p>
<p> Use this function before polling on the display fd or to integrate the fd into a toolkit event loop in a race-free way. Typically, a toolkit will call <code>wl_display_dispatch_pending()</code> before sleeping, to make sure it doesn&#8217;t block with unhandled events. Upon waking up, it will assume the file descriptor is readable and read events from the fd by calling <code>wl_display_dispatch()</code>. Simplified, we have: </p>
<p> wl_display_dispatch_pending(display); wl_display_flush(display); poll(fds, nfds, -1); wl_display_dispatch(display); </p>
<p> There are two races here: first, before blocking in poll(), the fd could become readable and another thread reads the events. Some of these events may be for the main queue and the other thread will queue them there and then the main thread will go to sleep in poll(). This will stall the application, which could be waiting for a event to kick of the next animation frame, for example. </p>
<p> The other race is immediately after poll(), where another thread could preempt and read events before the main thread calls <code>wl_display_dispatch()</code>. This call now blocks and starves the other fds in the event loop. </p>
<p> A correct sequence would be: </p>
<p> while (wl_display_prepare_read(display) != 0) wl_display_dispatch_pending(display); wl_display_flush(display); poll(fds, nfds, -1); wl_display_read_events(display); wl_display_dispatch_pending(display); </p>
<p> Here we call <code>wl_display_prepare_read()</code>, which ensures that between returning from that call and eventually calling <code>wl_display_read_events()</code>, no other thread will read from the fd and queue events in our queue. If the call to <code>wl_display_prepare_read()</code> fails, we dispatch the pending events and try again until we&#8217;re successful.</p>
<h3>int wl_display_read_events (struct <code>wl_display</code> *display)</h3>
<p>Read events from display file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success or -1 on error. In case of error errno will be set accordingly</dl>
<p> This will read events from the file descriptor for the display. This function does not dispatch events, it only reads and queues events into their corresponding event queues. If no data is avilable on the file descriptor, <code>wl_display_read_events()</code> returns immediately. To dispatch events that may have been queued, call <code>wl_display_dispatch_pending()</code> or <code>wl_display_dispatch_queue_pending()</code>. </p>
<p> Before calling this function, <code>wl_display_prepare_read()</code> must be called first.</p>
<h3>int wl_display_roundtrip (struct <code>wl_display</code> *display)</h3>
<p>Block until all pending request are processed by the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Blocks until the server process all currently issued requests and sends out pending events on all event queues.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
