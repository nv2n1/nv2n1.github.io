---
title: "xcb_input_device_mapping_notify_event_t(3)"
name: "xcb_input_device_mapping_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_device_mapping_notify_event_t/"
description: "xcb_input_device_mapping_notify_event_t –"
---

<p>xcb_input_device_mapping_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_input_device_mapping_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>device_id</i>;
 uint16_t <i>sequence</i>;
 uint8_t <i>request</i>;
 xcb_input_key_code_t <i>first_keycode</i>;
 uint8_t <i>count</i>;
 uint8_t <i>pad0</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>pad1</i>[20];
} <code>xcb_input_device_mapping_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_INPUT_DEVICE_MAPPING_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>device_id</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>request</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>first_keycode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>count</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
