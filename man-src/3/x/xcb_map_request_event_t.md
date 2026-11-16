---
title: "xcb_map_request_event_t(3)"
name: "xcb_map_request_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_map_request_event_t/"
description: "xcb_map_request_event_t – window wants to be mapped"
---

<p>xcb_map_request_event_t &#8211; window wants to be mapped</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_map_request_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>parent</i>;
 xcb_window_t <i>window</i>;
} <code>xcb_map_request_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_MAP_REQUEST</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>parent</i></dt>
<dd>The parent of <i>window</i>.</dd>
<dt><i>window</i></dt>
<dd>The window to be mapped.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3), <code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
