---
title: "xcb_randr_screen_change_notify_event_t(3)"
name: "xcb_randr_screen_change_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_screen_change_notify_event_t/"
description: "xcb_randr_screen_change_notify_event_t –"
---

<p>xcb_randr_screen_change_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_randr_screen_change_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>rotation</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>timestamp</i>;
 xcb_timestamp_t <i>config_timestamp</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>request_window</i>;
 uint16_t <i>sizeID</i>;
 uint16_t <i>subpixel_order</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>mwidth</i>;
 uint16_t <i>mheight</i>;
} <code>xcb_randr_screen_change_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_RANDR_SCREEN_CHANGE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>rotation</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>config_timestamp</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>request_window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>sizeID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>subpixel_order</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>mwidth</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>mheight</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
