---
title: "xcb_input_device_key_release_event_t(3)"
name: "xcb_input_device_key_release_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_device_key_release_event_t/"
description: "xcb_input_device_key_release_event_t –"
---

<p>xcb_input_device_key_release_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_input_device_key_release_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>detail</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>child</i>;
 int16_t <i>root_x</i>;
 int16_t <i>root_y</i>;
 int16_t <i>event_x</i>;
 int16_t <i>event_y</i>;
 uint16_t <i>state</i>;
 uint8_t <i>same_screen</i>;
 uint8_t <i>device_id</i>;
} <code>xcb_input_device_key_release_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_INPUT_DEVICE_KEY_RELEASE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>detail</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>root</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>event</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>child</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>root_x</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>root_y</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>event_x</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>event_y</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>state</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>same_screen</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>device_id</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
