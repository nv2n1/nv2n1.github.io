---
title: "xcb_destroy_notify_event_t(3)"
name: "xcb_destroy_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_destroy_notify_event_t/"
description: "xcb_destroy_notify_event_t – a window is destroyed"
---

<p>xcb_destroy_notify_event_t &#8211; a window is destroyed</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_destroy_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>window</i>;
} <code>xcb_destroy_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_DESTROY_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>event</i></p>
<dd>The reconfigured window or its parent, depending on whether <i>StructureNotify</i> or <i>SubstructureNotify</i> was selected.</p>
<dt><i>window</i></p>
<dd>The window that is destroyed.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_destroy_window/">xcb_destroy_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
