---
title: "xcb_ge_generic_event_t(3)"
name: "xcb_ge_generic_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_ge_generic_event_t/"
description: "xcb_ge_generic_event_t – generic event (with length)"
---

<p>xcb_ge_generic_event_t &#8211; generic event (with length)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_ge_generic_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>extension</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>event_type</i>;
 uint8_t <i>pad0</i>[22];
 uint32_t <i>full_sequence</i>;
} <code>xcb_ge_generic_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_GE_GENERIC</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>extension</i></dt>
<dd>The major opcode of the extension creating this event</dd>
<dt><i>length</i></dt>
<dd>The amount (in 4-byte units) of data beyond 32 bytes</dd>
<dt><i>event_type</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>full_sequence</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
