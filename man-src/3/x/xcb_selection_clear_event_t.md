---
title: "xcb_selection_clear_event_t(3)"
name: "xcb_selection_clear_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_selection_clear_event_t/"
description: "xcb_selection_clear_event_t –"
---

<p>xcb_selection_clear_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_selection_clear_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 xcb_window_t <i>owner</i>;
 xcb_atom_t <i>selection</i>;
} <code>xcb_selection_clear_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_SELECTION_CLEAR</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>owner</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>selection</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
