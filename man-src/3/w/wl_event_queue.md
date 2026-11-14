---
title: "wl_event_queue(3)"
name: "wl_event_queue"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_event_queue/"
description: "wl_event_queue –"
---

<p>wl_event_queue &#8211; </p>
<p> A queue for <code>wl_proxy</code> object events.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-client.h&gt;

Public Member Functions
void wl_event_queue_destroy (struct wl_event_queue *queue)</code></pre>
<h2>Detailed Description</h2>
<p>A queue for <code>wl_proxy</code> object events. </p>
<p> Event queues allows the events on a display to be handled in a thread-safe manner. See <code>wl_display</code> for details.</p>
<h2>Member Function Documentation</h2>
<h3>void wl_event_queue_destroy (struct <code>wl_event_queue</code> *queue)</h3>
<p>Destroy an event queue </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>queue</i> The event queue to be destroyed</dl>
<p> Destroy the given event queue. Any pending event on that queue is discarded. </p>
<p> The <code>wl_display</code> object used to create the queue should not be destroyed until all event queues created with it are destroyed with this function.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
