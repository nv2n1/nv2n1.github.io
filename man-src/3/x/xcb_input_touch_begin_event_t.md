---
title: "xcb_input_touch_begin_event_t(3)"
name: "xcb_input_touch_begin_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_touch_begin_event_t/"
description: "xcb_input_touch_begin_event_t –"
---

<p>xcb_input_touch_begin_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_input_touch_begin_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>extension</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>event_type</i>;
 xcb_input_device_id_t <i>deviceid</i>;
 xcb_timestamp_t <i>time</i>;
 uint32_t <i>detail</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>child</i>;
 uint32_t <i>full_sequence</i>;
 xcb_input_fp1616_t <i>root_x</i>;
 xcb_input_fp1616_t <i>root_y</i>;
 xcb_input_fp1616_t <i>event_x</i>;
 xcb_input_fp1616_t <i>event_y</i>;
 uint16_t <i>buttons_len</i>;
 uint16_t <i>valuators_len</i>;
 xcb_input_device_id_t <i>sourceid</i>;
 uint8_t <i>pad0</i>[2];
 uint32_t <i>flags</i>;
 xcb_input_modifier_info_t <i>mods</i>;
 xcb_input_group_info_t <i>group</i>;
} <code>xcb_input_touch_begin_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_INPUT_TOUCH_END</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>extension</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>length</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_type</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>deviceid</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>detail</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>child</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>full_sequence</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root_x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root_y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>buttons_len</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>valuators_len</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>sourceid</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>flags</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>mods</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>group</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
