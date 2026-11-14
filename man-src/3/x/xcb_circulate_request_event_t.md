---
title: "xcb_circulate_request_event_t(3)"
name: "xcb_circulate_request_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_circulate_request_event_t/"
description: "xcb_circulate_request_event_t – NOT YET DOCUMENTED"
---

<p>xcb_circulate_request_event_t &#8211; NOT YET DOCUMENTED</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_circulate_request_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>window</i>;
 uint8_t <i>pad1</i>[4];
 uint8_t <i>place</i>;
 uint8_t <i>pad2</i>[3];
} <code>xcb_circulate_request_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_CIRCULATE_REQUEST</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>event</i></p>
<dd>Either the restacked window or its parent, depending on whether <i>StructureNotify</i> or <i>SubstructureNotify</i> was selected.</p>
<dt><i>window</i></p>
<dd>The restacked window.</p>
<dt><i>place</i></p>
<dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_circulate_window/">xcb_circulate_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
