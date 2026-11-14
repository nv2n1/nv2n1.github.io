---
title: "xcb_graphics_exposure_event_t(3)"
name: "xcb_graphics_exposure_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_graphics_exposure_event_t/"
description: "xcb_graphics_exposure_event_t –"
---

<p>xcb_graphics_exposure_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_graphics_exposure_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_drawable_t <i>drawable</i>;
 uint16_t <i>x</i>;
 uint16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>minor_opcode</i>;
 uint16_t <i>count</i>;
 uint8_t <i>major_opcode</i>;
 uint8_t <i>pad1</i>[3];
} <code>xcb_graphics_exposure_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_GRAPHICS_EXPOSURE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>drawable</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>x</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>y</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>minor_opcode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>count</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>major_opcode</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
