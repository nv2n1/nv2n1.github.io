---
title: "xcb_damage_notify_event_t(3)"
name: "xcb_damage_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_damage_notify_event_t/"
description: "xcb_damage_notify_event_t –"
---

<p>xcb_damage_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/damage.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_damage_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>level</i>;
 uint16_t <i>sequence</i>;
 xcb_drawable_t <i>drawable</i>;
 xcb_damage_damage_t <i>damage</i>;
 xcb_timestamp_t <i>timestamp</i>;
 xcb_rectangle_t <i>area</i>;
 xcb_rectangle_t <i>geometry</i>;
} <code>xcb_damage_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_DAMAGE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>level</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>drawable</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>damage</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>timestamp</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>area</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>geometry</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from damage.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
