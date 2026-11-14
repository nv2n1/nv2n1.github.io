---
title: "xcb_map_notify_event_t(3)"
name: "xcb_map_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_map_notify_event_t/"
description: "xcb_map_notify_event_t – a window was mapped"
---

<p>xcb_map_notify_event_t &#8211; a window was mapped</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_map_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>window</i>;
 uint8_t <i>override_redirect</i>;
 uint8_t <i>pad1</i>[3];
} <code>xcb_map_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_MAP_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>event</i></p>
<dd>The window which was mapped or its parent, depending on whether <i>StructureNotify</i> or <i>SubstructureNotify</i> was selected.</p>
<dt><i>window</i></p>
<dd>The window that was mapped.</p>
<dt><i>override_redirect</i></p>
<dd>Window managers should ignore this window if <i>override_redirect</i> is 1.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
