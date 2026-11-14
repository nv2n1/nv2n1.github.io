---
title: "wl_signal_emit(3)"
name: "wl_signal_emit"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_signal_emit/"
description: "wl_signal –"
---

<p>wl_signal &#8211; </p>
<p> A source of a type of observable event.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;wayland-server.h&gt;

Public Member Functions
static void wl_signal_init (struct wl_signal *signal)



static void wl_signal_add (struct wl_signal *signal, struct wl_listener *listener)



static struct wl_listener * wl_signal_get (struct wl_signal *signal, wl_notify_func_t notify)



static void wl_signal_emit (struct wl_signal *signal, void *data)



Public Attributes
struct wl_list listener_list</code></pre>
<h2>Detailed Description</h2>
<p>A source of a type of observable event. </p>
<p> Signals are recognized points where significant events can be observed. Compositors as well as the server can provide signals. Observers are <code>wl_listener</code>&#8216;s that are added through <code>wl_signal_add</code>. Signals are emitted using <code>wl_signal_emit</code>, which will invoke all listeners until that listener is removed by #wl_list_remove (or whenever the signal is destroyed). </p>
<p> <code>See Also:</code></p>
<dl>
<dd><code>wl_listener</code> for more information on using <code>wl_signal</code></dl>
<h2>Member Function Documentation</h2>
<h3>static void wl_signal_add (struct <code>wl_signal</code> *signal, struct <code>wl_listener</code> *listener) [inline]</h3>
<p>Add the specified listener to this signal. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>signal</i> The signal that will emit events to the listener<br />
 <i>listener</i> The listener to add</dl>
<h3>static void wl_signal_emit (struct <code>wl_signal</code> *signal, void *data) [inline]</h3>
<p>Emits this signal, notifying all registered listeners. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>signal</i> The signal object that will emit the signal<br />
 <i>data</i> The data that will be emitted with the signal</dl>
<h3>static struct <code>wl_listener</code> * wl_signal_get (struct <code>wl_signal</code> *signal, wl_notify_func_tnotify)</h3>
<p>Gets the listener struct for the specified callback. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>signal</i> The signal that contains the specified listener<br />
 <i>notify</i> The listener that is the target of this search</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the list item that corresponds to the specified listener, or NULL if none was found</dl>
<h3>static void wl_signal_init (struct <code>wl_signal</code> *signal) [inline]</h3>
<p>Initialize a new <code>wl_signal</code> for use. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>signal</i> The signal that will be initialized</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
