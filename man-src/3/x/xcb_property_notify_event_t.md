---
title: "xcb_property_notify_event_t(3)"
name: "xcb_property_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_property_notify_event_t/"
description: "xcb_property_notify_event_t – a window property changed"
---

<p>xcb_property_notify_event_t &#8211; a window property changed</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_property_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>window</i>;
 xcb_atom_t <i>atom</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>state</i>;
 uint8_t <i>pad1</i>[3];
} <code>xcb_property_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_PROPERTY_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>window</i></p>
<dd>The window whose associated property was changed.</p>
<dt><i>atom</i></p>
<dd>The property&#8217;s atom, to indicate which property was changed.</p>
<dt><i>time</i></p>
<dd>A timestamp of the server time when the property was changed.</p>
<dt><i>state</i></p>
<dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_change_property/">xcb_change_property</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
