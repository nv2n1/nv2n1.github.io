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
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_DRI2_BUFFER_SWAP_COMPLETE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>event_type</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>drawable</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ust_hi</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ust_lo</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>msc_hi</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>msc_lo</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>sbc</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from dri2.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
