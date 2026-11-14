---
title: "wl_display_get_protocol_error(3)"
name: "wl_display_get_protocol_error"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_display_get_protocol_error/"
description: "wl_display – Represents a connection to the compositor and acts as a proxy to the wl_display singleton object."
---

<p>wl_display &#8211; Represents a connection to the compositor and acts as a proxy to the <code>wl_display</code> singleton object.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-client.h&gt;

Public Member Functions
struct wl_client * wl_client_create (struct wl_display *display, int fd)



struct wl_display * wl_display_create (void)



void wl_display_destroy (struct wl_display *display)



uint32_t wl_display_get_serial (struct wl_display *display)



uint32_t wl_display_next_serial (struct wl_display *display)



int wl_display_add_socket (struct wl_display *display, const char *name)



uint32_t * wl_display_add_shm_format (struct wl_display *display, uint32_t format)



struct wl_array * wl_display_get_additional_shm_formats (struct wl_display *display)



struct wl_display * wl_display_connect_to_fd (int fd)



struct wl_display * wl_display_connect (const char *name)



void wl_display_disconnect (struct wl_display *display)



int wl_display_get_fd (struct wl_display *display)



int wl_display_roundtrip (struct wl_display *display)



int wl_display_read_events (struct wl_display *display)



int wl_display_prepare_read (struct wl_display *display)



void wl_display_cancel_read (struct wl_display *display)



int wl_display_dispatch (struct wl_display *display)



int wl_display_dispatch_pending (struct wl_display *display)



int wl_display_get_error (struct wl_display *display)



uint32_t wl_display_get_protocol_error (struct wl_display *display, const struct wl_interface **interface, uint32_t *id)



int wl_display_flush (struct wl_display *display)



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
<p> A <code>wl_display</code> has at least one event queue, called the <i>default queue</i>. Clients can create additional event queues with <code>wl_display_create_queue()</code> and assign <code>wl_proxy</code>&#8216;s to it. Events occurring in a particular proxy are always queued in its assigned queue. A client can ensure that a certain assumption, such as holding a lock or running from a given thread, is true when a proxy event handler is called by assigning that proxy to an event queue and making sure that this queue is only dispatched when the assumption holds. </p>
<p> The default queue is dispatched by calling <code>wl_display_dispatch()</code>. This will dispatch any events queued on the default queue and attempt to read from the display fd if it&#8217;s empty. Events read are then queued on the appropriate queues according to the proxy assignment. </p>
<p> A user created queue is dispatched with <code>wl_display_dispatch_queue()</code>. This function behaves exactly the same as <code>wl_display_dispatch()</code> but it dispatches given queue instead of the default queue. </p>
<p> A real world example of event queue usage is Mesa&#8217;s implementation of eglSwapBuffers() for the Wayland platform. This function might need to block until a frame callback is received, but dispatching the default queue could cause an event handler on the client to start drawing again. This problem is solved using another event queue, so that only the events handled by the EGL code are dispatched during the block. </p>
<p> This creates a problem where a thread dispatches a non-default queue, reading all the data from the display fd. If the application would call <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i> after that it would block, even though there might be events queued on the default queue. Those events should be dispatched with <code>pending()</code> before flushing and blocking.</p>
<h2>Member Function Documentation</h2>
<h3>struct <code>wl_client</code> * wl_client_create (struct <code>wl_display</code> * display, int fd)</h3>
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
<h3>uint32_t * wl_display_add_shm_format (struct <code>wl_display</code> * display, uint32_t format)</h3>
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
<h3>int wl_display_add_socket (struct <code>wl_display</code> * display, const char * name)</h3>
<p>Add a socket to Wayland display for the clients to connect. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> Wayland display to which the socket should be added.<br />
 <i>name</i> Name of the Unix socket.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if success. -1 if failed.</dl>
<p> This adds a Unix socket to Wayland display which can be used by clients to connect to Wayland display. </p>
<p> If NULL is passed as name, then it would look for WAYLAND_DISPLAY env variable for the socket name. If WAYLAND_DISPLAY is not set, then default wayland-0 is used. </p>
<p> The Unix socket will be created in the directory pointed to by environment variable XDG_RUNTIME_DIR. If XDG_RUNTIME_DIR is not set, then this function fails and returns -1. </p>
<p> The length of socket path, i.e., the path set in XDG_RUNTIME_DIR and the socket name, must not exceed the maxium length of a Unix socket path. The function also fails if the user do not have write permission in the XDG_RUNTIME_DIR path or if the socket name is already in use.</p>
<h3>void wl_display_cancel_read (struct <code>wl_display</code> * display)</h3>
<p>Cancel read intention on display&#8217;s fd </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> After a thread successfully called <code>wl_display_prepare_read()</code> it must either call <code>wl_display_read_events()</code> or <code>wl_display_cancel_read()</code>. If the threads do not follow this rule it will lead to deadlock. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_prepare_read()</code>, <code>wl_display_read_events()</code></dl>
<h3>struct <code>wl_display</code> * wl_display_connect (const char * name)</h3>
<p>Connect to a Wayland display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> Name of the Wayland display to connect to</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A <code>wl_display</code> object or NULL on failure</dl>
<p> Connect to the Wayland display named name. If name is NULL, its value will be replaced with the WAYLAND_DISPLAY environment variable if it is set, otherwise display &#8216;wayland-0&#8217; will be used.</p>
<h3>struct <code>wl_display</code> * wl_display_connect_to_fd (int fd)</h3>
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
<p> <code>Returns:</code></p>
<dl>
<dd>The Wayland display object. Null if failed to create</dl>
<p> This creates the <code>wl_display</code> object.</p>
<h3>void wl_display_destroy (struct <code>wl_display</code> * display)</h3>
<p>Destroy Wayland display object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The Wayland display object which should be destroyed.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>None.</dl>
<p> This function emits the <code>wl_display</code> destroy signal, releases all the sockets added to this display, free&#8217;s all the globals associated with this display, free&#8217;s memory of additional shared memory formats and destroy the display object. </p>
<p> <code>See also:</code></p>
<dl>
<dd>wl_display_add_destroy_listener</dl>
<h3>void wl_display_disconnect (struct <code>wl_display</code> * display)</h3>
<p>Close a connection to a Wayland display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> Close the connection to display and free all resources associated with it.</p>
<h3>int wl_display_dispatch (struct <code>wl_display</code> * display)</h3>
<p>Process incoming events </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Dispatch the display&#8217;s default event queue. </p>
<p> If the default event queue is empty, this function blocks until there are events to be read from the display fd. Events are read and queued on the appropriate event queues. Finally, events on the default event queue are dispatched. </p>
<p> In multi-threaded environment, programmer may want to use <code>wl_display_read_events()</code>. However, use of <code>wl_display_read_events()</code> must not be mixed with <code>wl_display_dispatch()</code>. See <code>wl_display_read_events()</code> and <code>wl_display_prepare_read()</code> for more details. </p>
<p> <code>Note:</code></p>
<dl>
<dd>It is not possible to check if there are events on the queue or not. For dispatching default queue events without blocking, see <code>wl_display_dispatch_pending()</code>.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_dispatch_pending()</code>, <code>wl_display_dispatch_queue()</code>, <code>wl_display_read_events()</code></dl>
<h3>int wl_display_dispatch_pending (struct <code>wl_display</code> * display)</h3>
<p>Dispatch default queue events without reading from the display fd </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events or -1 on failure</dl>
<p> This function dispatches events on the main event queue. It does not attempt to read the display fd and simply returns zero if the main queue is empty, i.e., it doesn&#8217;t block. </p>
<p> This is necessary when a client&#8217;s main loop wakes up on some fd other than the display fd (network socket, timer fd, etc) and calls <code>wl_display_dispatch_queue()</code> from that callback. This may queue up events in other queues while reading all data from the display fd. When the main loop returns from the handler, the display fd no longer has data, causing a call to <i><a href="/docs/linux/man/2-poll/">poll</a>(2)</i> (or similar functions) to block indefinitely, even though there are events ready to dispatch. </p>
<p> To proper integrate the wayland display fd into a main loop, the client should always call <code>wl_display_dispatch_pending()</code> and then <code>wl_display_flush()</code> prior to going back to sleep. At that point, the fd typically doesn&#8217;t have data so attempting I/O could block, but events queued up on the default queue should be dispatched. </p>
<p> A real-world example is a main loop that wakes up on a timerfd (or a sound card fd becoming writable, for example in a video player), which then triggers GL rendering and eventually eglSwapBuffers(). eglSwapBuffers() may call <code>wl_display_dispatch_queue()</code> if it didn&#8217;t receive the frame event for the previous frame, and as such queue events in the default queue. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_dispatch()</code>, <code>wl_display_dispatch_queue()</code>, <code>wl_display_flush()</code></dl>
<h3>int wl_display_flush (struct <code>wl_display</code> * display)</h3>
<p>Send all buffered requests on the display to the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of bytes sent on success or -1 on failure</dl>
<p> Send all buffered data on the client side to the server. Clients should call this function before blocking. On success, the number of bytes sent to the server is returned. On failure, this function returns -1 and errno is set appropriately. </p>
<p> <code>wl_display_flush()</code> never blocks. It will write as much data as possible, but if all data could not be written, errno will be set to EAGAIN and -1 returned. In that case, use poll on the display file descriptor to wait for it to become writable again.</p>
<h3>struct <code>wl_array</code> * wl_display_get_additional_shm_formats (struct <code>wl_display</code> * display)</h3>
<p>Get list of additional wl_shm pixel formats </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function returns the list of addition wl_shm pixel formats that the compositor supports. WL_SHM_FORMAT_ARGB8888 and WL_SHM_FORMAT_XRGB8888 are always supported and not included in the array, but all formats added through <code>wl_display_add_shm_format()</code> will be in the array. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_add_shm_format()</code></dl>
<h3>int wl_display_get_error (struct <code>wl_display</code> * display)</h3>
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
<h3>int wl_display_get_fd (struct <code>wl_display</code> * display)</h3>
<p>Get a display context&#8217;s file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Display object file descriptor</dl>
<p> Return the file descriptor associated with a display so it can be integrated into the client&#8217;s main loop.</p>
<h3>uint32_t wl_display_get_protocol_error (struct <code>wl_display</code> * display, const struct <code>wl_interface</code> ** interface, uint32_t * id)</h3>
<p>Retrieves the information about a protocol error: </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The Wayland display<br />
 <i>interface</i> if not NULL, stores the interface where the error occurred<br />
 <i>id</i> if not NULL, stores the object id that generated the error. There&#8217;s no guarantee the object is still valid; the client must know if it deleted the object.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The error code as defined in the interface specification.</dl>
<pre>int err = wl_display_get_error(display);
if (err == EPROTO) {
 code = wl_display_get_protocol_error(display, &amp;interface, &amp;id);
 handle_error(code, interface, id);
}
...</pre>
<p>&nbsp;<wbr></p>
<h3>uint32_t wl_display_get_serial (struct <code>wl_display</code> * display)</h3>
<p>Get the current serial number </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function returns the most recent serial number, but does not increment it.</p>
<h3>uint32_t wl_display_next_serial (struct <code>wl_display</code> * display)</h3>
<p>Get the next serial number </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display object</dl>
<p> This function increments the display serial number and returns the new value.</p>
<h3>int wl_display_prepare_read (struct <code>wl_display</code> * display)</h3>
<p>Prepare to read events from the display&#8217;s file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success or -1 if event queue was not empty</dl>
<p> This function must be called before reading from the file descriptor using <code>wl_display_read_events()</code>. Calling <code>wl_display_prepare_read()</code> announces the calling thread&#8217;s intention to read and ensures that until the thread is ready to read and calls <code>wl_display_read_events()</code>, no other thread will read from the file descriptor. This only succeeds if the event queue is empty though, and if there are undispatched events in the queue, -1 is returned and errno set to EAGAIN. </p>
<p> If a thread successfully calls <code>wl_display_prepare_read()</code>, it must either call <code>wl_display_read_events()</code> when it&#8217;s ready or cancel the read intention by calling <code>wl_display_cancel_read()</code>. </p>
<p> Use this function before polling on the display fd or to integrate the fd into a toolkit event loop in a race-free way. A correct usage would be (we left out most of error checking): </p>
<pre>while (wl_display_prepare_read(display) != 0)
 wl_display_dispatch_pending(display);
wl_display_flush(display);
ret = poll(fds, nfds, -1);
if (has_error(ret))
 wl_display_cancel_read(display);
else
 wl_display_read_events(display);
wl_display_dispatch_pending(display);</pre>
<p>Here we call <code>wl_display_prepare_read()</code>, which ensures that between returning from that call and eventually calling <code>wl_display_read_events()</code>, no other thread will read from the fd and queue events in our queue. If the call to <code>wl_display_prepare_read()</code> fails, we dispatch the pending events and try again until we&#8217;re successful. </p>
<p> When using <code>wl_display_dispatch()</code> we&#8217;d have something like: </p>
<pre>wl_display_dispatch_pending(display);
wl_display_flush(display);
poll(fds, nfds, -1);
wl_display_dispatch(display);</pre>
<p>This sequence in not thread-safe. The race is immediately after poll(), where one thread could preempt and read events before the other thread calls <code>wl_display_dispatch()</code>. This call now blocks and starves the other fds in the event loop. </p>
<p> Another race would be when using more event queues. When one thread calls wl_display_dispatch(_queue)(), then it reads all events from display&#8217;s fd and queues them in appropriate queues. Then it dispatches only its own queue and the other events are sitting in their queues, waiting for dispatching. If that happens before the other thread managed to call poll(), it will block with events queued. </p>
<p> <code>wl_display_prepare_read()</code> function doesn&#8217;t acquire exclusive access to the display&#8217;s fd. It only registers that the thread calling this function has intention to read from fd. When all registered readers call <code>wl_display_read_events()</code>, only one (at random) eventually reads and queues the events and the others are sleeping meanwhile. This way we avoid races and still can read from more threads. </p>
<p> If the relevant queue is not the default queue, then <code>wl_display_prepare_read_queue()</code> and <code>wl_display_dispatch_queue_pending()</code> need to be used instead. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_cancel_read()</code>, <code>wl_display_read_events()</code></dl>
<h3>int wl_display_read_events (struct <code>wl_display</code> * display)</h3>
<p>Read events from display file descriptor </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success or -1 on error. In case of error errno will be set accordingly</dl>
<p> This will read events from the file descriptor for the display. This function does not dispatch events, it only reads and queues events into their corresponding event queues. If no data is available on the file descriptor, <code>wl_display_read_events()</code> returns immediately. To dispatch events that may have been queued, call <code>wl_display_dispatch_pending()</code> or <code>wl_display_dispatch_queue_pending()</code>. </p>
<p> Before calling this function, <code>wl_display_prepare_read()</code> must be called first. When running in more threads (which is the usual case, since we&#8217;d use <code>wl_display_dispatch()</code> otherwise), every thread must call <code>wl_display_prepare_read()</code> before calling this function. </p>
<p> After calling <code>wl_display_prepare_read()</code> there can be some extra code before calling <code>wl_display_read_events()</code>, for example poll() or alike. Example of code in a thread: </p>
<pre>while (wl_display_prepare_read(display) &lt; 0)
 wl_display_dispatch_pending(display);
wl_display_flush(display);
... some code ...
fds[0].fd = wl_display_get_fd(display);
fds[0].events = POLLIN;
poll(fds, 1, -1);
if (!everything_ok()) {
 wl_display_cancel_read(display);
 handle_error();
}
if (wl_display_read_events(display) &lt; 0)
 handle_error();
...</pre>
<p>After <code>wl_display_prepare_read()</code> succeeds, other threads that enter <code>wl_display_read_events()</code> will sleep until the very last thread enters it too or cancels. Therefore when the display fd becomes (or already is) readable, <code>wl_display_read_events()</code> should be called as soon as possible to unblock all threads. If <code>wl_display_read_events()</code> will not be called, then <code>wl_display_cancel_read()</code> must be called instead to let the other threads continue. </p>
<p> This function must not be called simultaneously with <code>wl_display_dispatch()</code>. It may lead to deadlock. If programmer wants, for some reason, use <code>wl_display_dispatch()</code> in one thread and <code>wl_display_prepare_read()</code> with <code>wl_display_read_events()</code> in another, extra care must be taken to serialize these calls, i. e. use mutexes or similar (on whole prepare + read sequence) </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_prepare_read()</code>, <code>wl_display_cancel_read()</code>, <code>wl_display_dispatch_pending()</code>, <code>wl_display_dispatch()</code></dl>
<h3>int wl_display_roundtrip (struct <code>wl_display</code> * display)</h3>
<p>Block until all pending request are processed by the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Blocks until the server process all currently issued requests and sends out pending events on the default event queue. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This function uses <code>wl_display_dispatch_queue()</code> internally. If you are using <code>wl_display_read_events()</code> from more threads, don&#8217;t use this function (or make sure that calling <code>wl_display_roundtrip()</code> doesn&#8217;t interfere with calling <code>wl_display_prepare_read()</code> and <code>wl_display_read_events()</code>)</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
