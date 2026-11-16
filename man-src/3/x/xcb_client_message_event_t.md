---
title: "xcb_client_message_event_t(3)"
name: "xcb_client_message_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_client_message_event_t/"
description: "xcb_client_message_event_t – NOT YET DOCUMENTED"
---

<p>xcb_client_message_event_t &#8211; NOT YET DOCUMENTED</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_client_message_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>format</i>;
 uint16_t <i>sequence</i>;
 xcb_window_t <i>window</i>;
 xcb_atom_t <i>type</i>;
 xcb_client_message_data_t <i>data</i>;
} <code>xcb_client_message_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_CLIENT_MESSAGE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>format</i></dt>
<dd>Specifies how to interpret <i>data</i>. Can be either 8, 16 or 32.</dd>
<dt><i>window</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>type</i></dt>
<dd>An atom which indicates how the data should be interpreted by the receiving client.</dd>
<dt><i>data</i></dt>
<dd>The data itself (20 bytes max).</dd></dl>
<h2>Description</h2>
<p>This event represents a ClientMessage, sent by another X11 client. An example is a client sending the <i>_NET_WM_STATE</i> ClientMessage to the root window to indicate the fullscreen window state, effectively requesting that the window manager puts it into fullscreen mode.</p>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3), <code><a href="/docs/linux/man/3-xcb_send_event/">xcb_send_event</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
