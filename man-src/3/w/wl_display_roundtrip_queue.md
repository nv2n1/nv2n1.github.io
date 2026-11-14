---
title: "wl_display_roundtrip_queue(3)"
name: "wl_display_roundtrip_queue"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_display_roundtrip_queue/"
description: "wl_event_queue – A queue for wl_proxy object events."
---

<p>wl_event_queue &#8211; A queue for <code>wl_proxy</code> object events.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-client.h&gt;

Public Member Functions
void wl_event_queue_destroy (struct wl_event_queue *queue)



struct wl_event_queue * wl_display_create_queue (struct wl_display *display)



int wl_display_roundtrip_queue (struct wl_display *display, struct wl_event_queue *queue)



int wl_display_prepare_read_queue (struct wl_display *display, struct wl_event_queue *queue)



int wl_display_dispatch_queue (struct wl_display *display, struct wl_event_queue *queue)



int wl_display_dispatch_queue_pending (struct wl_display *display, struct wl_event_queue *queue)</code></pre>
<h2>Detailed Description</h2>
<p>A queue for <code>wl_proxy</code> object events. </p>
<p> Event queues allows the events on a display to be handled in a thread-safe manner. See <code>wl_display</code> for details.</p>
<h2>Member Function Documentation</h2>
<h3>struct <code>wl_event_queue</code> * wl_display_create_queue (struct <code>wl_display</code> * display)</h3>
<p>Create a new event queue for this display </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new event queue associated with this display or NULL on failure.</dl>
<h3>int wl_display_dispatch_queue (struct <code>wl_display</code> * display, struct <code>wl_event_queue</code> * queue)</h3>
<p>Dispatch events in an event queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object<br />
 <i>queue</i> The event queue to dispatch</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Dispatch all incoming events for objects assigned to the given event queue. On failure -1 is returned and errno set appropriately. </p>
<p> The behaviour of this function is exactly the same as the behaviour of <code>wl_display_dispatch()</code>, but it dispatches events on given queue, not on the default queue. </p>
<p> This function blocks if there are no events to dispatch (if there are, it only dispatches these events and returns immediately). When this function returns after blocking, it means that it read events from display&#8217;s fd and queued them to appropriate queues. If among the incoming events were some events assigned to the given queue, they are dispatched by this moment. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Since Wayland 1.5 the display has an extra queue for its own events (i. e. delete_id). This queue is dispatched always, no matter what queue we passed as an argument to this function. That means that this function can return non-0 value even when it haven&#8217;t dispatched any event for the given queue.</dl>
<p> This function has the same constrains for using in multi-threaded apps as <code>wl_display_dispatch()</code>. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_dispatch()</code>, <code>wl_display_dispatch_pending()</code>, <code>wl_display_dispatch_queue_pending()</code></dl>
<h3>int wl_display_dispatch_queue_pending (struct <code>wl_display</code> * display, struct <code>wl_event_queue</code> * queue)</h3>
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
<h3>int wl_display_prepare_read_queue (struct <code>wl_display</code> * display, struct <code>wl_event_queue</code> * queue)</h3>
<p>Prepare to read events from the display to this queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object<br />
 <i>queue</i> The event queue to use</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on success or -1 if event queue was not empty</dl>
<p> Atomically makes sure the queue is empty and stops any other thread from placing events into this (or any) queue. Caller must eventually call either <code>wl_display_cancel_read()</code> or <code>wl_display_read_events()</code>, usually after waiting for the display fd to become ready for reading, to release the lock. </p>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_prepare_read</code></dl>
<h3>int wl_display_roundtrip_queue (struct <code>wl_display</code> * display, struct <code>wl_event_queue</code> * queue)</h3>
<p>Block until all pending request are processed by the server </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>display</i> The display context object<br />
 <i>queue</i> The queue on which to run the roundtrip</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The number of dispatched events on success or -1 on failure</dl>
<p> Blocks until the server process all currently issued requests and sends out pending events on the event queue. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This function uses <code>wl_display_dispatch_queue()</code> internally. If you are using <code>wl_display_read_events()</code> from more threads, don&#8217;t use this function (or make sure that calling <code>wl_display_roundtrip_queue()</code> doesn&#8217;t interfere with calling <code>wl_display_prepare_read()</code> and <code>wl_display_read_events()</code>)</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>wl_display_roundtrip()</code></dl>
<h3>void wl_event_queue_destroy (struct <code>wl_event_queue</code> * queue)</h3>
<p>Destroy an event queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The event queue to be destroyed</dl>
<p> Destroy the given event queue. Any pending event on that queue is discarded. </p>
<p> The <code>wl_display</code> object used to create the queue should not be destroyed until all event queues created with it are destroyed with this function.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
