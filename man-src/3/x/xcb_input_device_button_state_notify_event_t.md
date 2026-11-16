---
title: "xcb_input_device_button_state_notify_event_t(3)"
name: "xcb_input_device_button_state_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_device_button_state_notify_event_t/"
description: "xcb_input_device_button_state_notify_event_t –"
---

<p>xcb_input_device_button_state_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_input_device_button_state_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>device_id</i>;
 uint16_t <i>sequence</i>;
 uint8_t <i>buttons</i>[28];
} <code>xcb_input_device_button_state_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_INPUT_DEVICE_BUTTON_STATE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>device_id</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>buttons</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
