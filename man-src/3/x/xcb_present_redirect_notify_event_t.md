---
title: "xcb_present_redirect_notify_event_t(3)"
name: "xcb_present_redirect_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_present_redirect_notify_event_t/"
description: "xcb_present_redirect_notify_event_t –"
---

<p>xcb_present_redirect_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/present.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_present_redirect_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>extension</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>event_type</i>;
 uint8_t <i>update_window</i>;
 uint8_t <i>pad0</i>;
 xcb_present_event_t <i>event</i>;
 xcb_window_t <i>event_window</i>;
 xcb_window_t <i>window</i>;
 xcb_pixmap_t <i>pixmap</i>;
 uint32_t <i>serial</i>;
 uint32_t <i>full_sequence</i>;
 xcb_xfixes_region_t <i>valid_region</i>;
 xcb_xfixes_region_t <i>update_region</i>;
 xcb_rectangle_t <i>valid_rect</i>;
 xcb_rectangle_t <i>update_rect</i>;
 int16_t <i>x_off</i>;
 int16_t <i>y_off</i>;
 xcb_randr_crtc_t <i>target_crtc</i>;
 xcb_sync_fence_t <i>wait_fence</i>;
 xcb_sync_fence_t <i>idle_fence</i>;
 uint32_t <i>options</i>;
 uint8_t <i>pad1</i>[4];
 uint64_t <i>target_msc</i>;
 uint64_t <i>divisor</i>;
 uint64_t <i>remainder</i>;
} <code>xcb_present_redirect_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_PRESENT_REDIRECT_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>extension</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>length</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_type</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>update_window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>event_window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>pixmap</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>serial</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>full_sequence</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>valid_region</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>update_region</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>valid_rect</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>update_rect</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>x_off</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>y_off</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>target_crtc</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>wait_fence</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>idle_fence</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>options</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>target_msc</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>divisor</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>remainder</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from present.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
