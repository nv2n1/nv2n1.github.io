---
title: "xcb_mapping_notify_event_t(3)"
name: "xcb_mapping_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_mapping_notify_event_t/"
description: "xcb_mapping_notify_event_t – keyboard mapping changed"
---

<p>xcb_mapping_notify_event_t &#8211; keyboard mapping changed</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_mapping_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint8_t <i>request</i>;
 xcb_keycode_t <i>first_keycode</i>;
 uint8_t <i>count</i>;
 uint8_t <i>pad1</i>;
} <code>xcb_mapping_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_MAPPING_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>request</i></p>
<dd>
<dt><i>first_keycode</i></p>
<dd>The first number in the range of the altered mapping.</p>
<dt><i>count</i></p>
<dd>The number of keycodes altered.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
