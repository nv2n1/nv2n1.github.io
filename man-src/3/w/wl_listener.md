---
title: "wl_listener(3)"
name: "wl_listener"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_listener/"
description: "wl_listener –"
---

<p>wl_listener &#8211; </p>
<p> A single listener for Wayland signals.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-server.h&gt;

Public Attributes
struct wl_list link



wl_notify_func_t notify</code></pre>
<h2>Detailed Description</h2>
<p>A single listener for Wayland signals. </p>
<p> <code>wl_listener</code> provides the means to listen for <code>wl_signal</code> notifications. Many Wayland objects use <code>wl_listener</code> for notification of significant events like object destruction. </p>
<p> Clients should create <code>wl_listener</code> objects manually and can register them as listeners to signals using <code>wl_signal_add</code>, assuming the signal is directly accessible. For opaque structs like wl_event_loop, adding a listener should be done through provided accessor methods. A listener can only listen to one signal at a time. </p>
<pre>struct wl_listener your_listener;
your_listener.notify = your_callback_method;
/* Direct access */
wl_signal_add(&amp;some_object-&gt;destroy_signal, &amp;your_listener);
/* Accessor access */
wl_event_loop *loop = ...;
wl_event_loop_add_destroy_listener(loop, &amp;your_listener);</pre>
<p>If the listener is part of a larger struct, <code>wl_container_of</code> can be used to retrieve a pointer to it: </p>
<pre>* void your_listener(struct wl_listener *listener, void *data)
* {
* struct your_data *data;
*
* your_data = wl_container_of(listener, data, your_member_name);
* }
* </pre>
<p>If you need to remove a listener from a signal, use #wl_list_remove. </p>
<pre>* wl_list_remove(&amp;your_listener.link);
* </pre>
<p><code>See Also:</code></p>
<dl>
<dd><code>wl_signal</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
