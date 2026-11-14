---
title: "xcb_colormap_notify_event_t(3)"
name: "xcb_colormap_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_colormap_notify_event_t/"
description: "xcb_colormap_notify_event_t – the colormap for some window changed"
---

<p>xcb_colormap_notify_event_t &#8211; the colormap for some window changed</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_colormap_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>window</i>;
 xcb_colormap_t <i>colormap</i>;
 uint8_t <i>_new</i>;
 uint8_t <i>state</i>;
 uint8_t <i>pad1</i>[2];
} <code>xcb_colormap_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_COLORMAP_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>window</i></p>
<dd>The window whose associated colormap is changed, installed or uninstalled.</p>
<dt><i>colormap</i></p>
<dd>The colormap which is changed, installed or uninstalled. This is <i>XCB_NONE</i> when the colormap is changed by a call to <i>FreeColormap</i>.</p>
<dt><i>_new</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>state</i></p>
<dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_free_colormap/">xcb_free_colormap</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
