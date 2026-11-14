---
title: "xcb_shape_notify_event_t(3)"
name: "xcb_shape_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_shape_notify_event_t/"
description: "xcb_shape_notify_event_t –"
---

<p>xcb_shape_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/shape.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_shape_notify_event_t {
 uint8_t <i>response_type</i>;
 xcb_shape_kind_t <i>shape_kind</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>affected_window</i>;
 int16_t <i>extents_x</i>;
 int16_t <i>extents_y</i>;
 uint16_t <i>extents_width</i>;
 uint16_t <i>extents_height</i>;
 xcb_timestamp_t <i>server_time</i>;
 uint8_t <i>shaped</i>;
 uint8_t <i>pad0</i>[11];
} <code>xcb_shape_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_SHAPE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>shape_kind</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>affected_window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>extents_x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>extents_y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>extents_width</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>extents_height</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>server_time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>shaped</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from shape.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
