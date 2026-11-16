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
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_XKB_EXTENSION_DEVICE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>xkbType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>deviceID</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>reason</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ledClass</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ledID</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ledsDefined</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ledState</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstButton</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nButtons</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>supported</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>unsupported</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
