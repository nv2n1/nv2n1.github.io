---
title: "xcb_input_grab_device_reply(3)"
name: "xcb_input_grab_device_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_grab_device_reply/"
description: "xcb_input_grab_device –"
---

<p>xcb_input_grab_device &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;

Request function

    xcb_input_grab_device_cookie_t
    xcb_input_grab_device(xcb_connection_t *conn, xcb_window_t grab_window, xcb_timestamp_t time, uint16_t num_classes, uint8_t this_device_mode, uint8_t other_device_mode, uint8_t owner_events, uint8_t device_id, const xcb_input_event_class_t *classes);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_input_grab_device_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xi_reply_type</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>status</i>;
 uint8_t <i>pad0</i>[23];
} <code>xcb_input_grab_device_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_input_grab_device_reply_t *<code>xcb_input_grab_device_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_input_grab_device_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>grab_window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_classes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>this_device_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>other_device_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>owner_events</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>device_id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>classes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_INPUT_GRAB_DEVICE</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>xi_reply_type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>status</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_input_grab_device_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_input_grab_device_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_input_grab_device_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
