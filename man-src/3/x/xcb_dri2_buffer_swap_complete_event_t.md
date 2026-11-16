---
title: "xcb_dri2_buffer_swap_complete_event_t(3)"
name: "xcb_dri2_buffer_swap_complete_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_dri2_buffer_swap_complete_event_t/"
description: "xcb_dri2_buffer_swap_complete_event_t –"
---

<p>xcb_dri2_buffer_swap_complete_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/dri2.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_dri2_buffer_swap_complete_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint16_t <i>event_type</i>;
 uint8_t <i>pad1</i>[2];
 xcb_drawable_t <i>drawable</i>;
 uint32_t <i>ust_hi</i>;
 uint32_t <i>ust_lo</i>;
 uint32_t <i>msc_hi</i>;
 uint32_t <i>msc_lo</i>;
 uint32_t <i>sbc</i>;
} <code>xcb_dri2_buffer_swap_complete_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_DRI2_BUFFER_SWAP_COMPLETE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>event_type</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>drawable</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ust_hi</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ust_lo</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>msc_hi</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>msc_lo</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>sbc</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from dri2.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
