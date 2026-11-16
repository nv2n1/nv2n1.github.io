---
title: "xcb_configure_notify_event_t(3)"
name: "xcb_configure_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_configure_notify_event_t/"
description: "xcb_configure_notify_event_t – NOT YET DOCUMENTED"
---

<p>xcb_configure_notify_event_t &#8211; NOT YET DOCUMENTED</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_configure_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>window</i>;
 xcb_window_t <i>above_sibling</i>;
 int16_t <i>x</i>;
 int16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>border_width</i>;
 uint8_t <i>override_redirect</i>;
 uint8_t <i>pad1</i>;
} <code>xcb_configure_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_CONFIGURE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>event</i></dt>
<dd>The reconfigured window or its parent, depending on whether <i>StructureNotify</i> or <i>SubstructureNotify</i> was selected.</dd>
<dt><i>window</i></dt>
<dd>The window whose size, position, border, and/or stacking order was changed.</dd>
<dt><i>above_sibling</i></dt>
<dd>If <i>XCB_NONE</i>, the <i>window</i> is on the bottom of the stack with respect to sibling windows. However, if set to a sibling window, the <i>window</i> is placed on top of this sibling window.</dd>
<dt><i>x</i></dt>
<dd>The X coordinate of the upper-left outside corner of <i>window</i>, relative to the parent window&#8217;s origin.</dd>
<dt><i>y</i></dt>
<dd>The Y coordinate of the upper-left outside corner of <i>window</i>, relative to the parent window&#8217;s origin.</dd>
<dt><i>width</i></dt>
<dd>The inside width of <i>window</i>, not including the border.</dd>
<dt><i>height</i></dt>
<dd>The inside height of <i>window</i>, not including the border.</dd>
<dt><i>border_width</i></dt>
<dd>The border width of <i>window</i>.</dd>
<dt><i>override_redirect</i></dt>
<dd>Window managers should ignore this window if <i>override_redirect</i> is 1.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3), <code><a href="/docs/linux/man/3-xcb_free_colormap/">xcb_free_colormap</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
