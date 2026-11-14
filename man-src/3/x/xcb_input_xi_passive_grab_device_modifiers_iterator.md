---
title: "xcb_input_xi_passive_grab_device_modifiers_iterator(3)"
name: "xcb_input_xi_passive_grab_device_modifiers_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_xi_passive_grab_device_modifiers_iterator/"
description: "xcb_input_xi_passive_grab_device –"
---

<p>xcb_input_xi_passive_grab_device &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;

Request function

    xcb_input_xi_passive_grab_device_cookie_t
    xcb_input_xi_passive_grab_device(xcb_connection_t *conn, xcb_timestamp_t time, xcb_window_t grab_window, xcb_cursor_t cursor, uint32_t detail, xcb_input_device_id_t deviceid, uint16_t num_modifiers, uint16_t mask_len, uint8_t grab_type, uint8_t grab_mode, uint8_t paired_device_mode, uint8_t owner_events, const uint32_t *mask, const uint32_t *modifiers);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_input_xi_passive_grab_device_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>num_modifiers</i>;
 uint8_t <i>pad1</i>[22];
} <code>xcb_input_xi_passive_grab_device_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_input_xi_passive_grab_device_reply_t *<code>xcb_input_xi_passive_grab_device_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_input_xi_passive_grab_device_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_input_grab_modifier_info_t *<code>xcb_input_xi_passive_grab_device_modifiers</code>(const xcb_input_xi_passive_grab_device_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_input_xi_passive_grab_device_modifiers_length</code>(const xcb_input_xi_passive_grab_device_reply_t *<i>reply</i>);</p>
<dd>xcb_input_grab_modifier_info_iterator_t <code>xcb_input_xi_passive_grab_device_modifiers_iterator</code>(const xcb_input_xi_passive_grab_device_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>time</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>grab_window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>cursor</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>detail</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>deviceid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_modifiers</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mask_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>grab_type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>grab_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>paired_device_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>owner_events</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>modifiers</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_INPUT_XI_PASSIVE_GRAB_DEVICE</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>num_modifiers</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_input_xi_passive_grab_device_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_input_xi_passive_grab_device_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_input_xi_passive_grab_device_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
