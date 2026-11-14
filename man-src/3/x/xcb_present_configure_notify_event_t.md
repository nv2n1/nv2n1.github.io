---
title: "xcb_present_configure_notify_event_t(3)"
name: "xcb_present_configure_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_present_configure_notify_event_t/"
description: "xcb_present_configure_notify_event_t –"
---

<p>xcb_present_configure_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/present.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_present_configure_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>extension</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>event_type</i>;
 uint8_t <i>pad0</i>[2];
 xcb_present_event_t <i>event</i>;
 xcb_window_t <i>window</i>;
 int16_t <i>x</i>;
 int16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 int16_t <i>off_x</i>;
 int16_t <i>off_y</i>;
 uint32_t <i>full_sequence</i>;
 uint16_t <i>pixmap_width</i>;
 uint16_t <i>pixmap_height</i>;
 uint32_t <i>pixmap_flags</i>;
} <code>xcb_present_configure_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_PRESENT_CONFIGURE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>extension</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>length</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_type</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>off_x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>off_y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>full_sequence</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>pixmap_width</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>pixmap_height</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>pixmap_flags</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from present.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
