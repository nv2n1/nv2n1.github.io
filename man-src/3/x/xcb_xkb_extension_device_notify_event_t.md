---
title: "xcb_xkb_extension_device_notify_event_t(3)"
name: "xcb_xkb_extension_device_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_extension_device_notify_event_t/"
description: "xcb_xkb_extension_device_notify_event_t –"
---

<p>xcb_xkb_extension_device_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_extension_device_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>reason</i>;
 uint16_t <i>ledClass</i>;
 uint16_t <i>ledID</i>;
 uint32_t <i>ledsDefined</i>;
 uint32_t <i>ledState</i>;
 uint8_t <i>firstButton</i>;
 uint8_t <i>nButtons</i>;
 uint16_t <i>supported</i>;
 uint16_t <i>unsupported</i>;
 uint8_t <i>pad1</i>[2];
} <code>xcb_xkb_extension_device_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_XKB_EXTENSION_DEVICE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>xkbType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>deviceID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>reason</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ledClass</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ledID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ledsDefined</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ledState</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstButton</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nButtons</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>supported</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>unsupported</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
