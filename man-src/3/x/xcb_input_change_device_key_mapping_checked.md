---
title: "xcb_input_change_device_key_mapping_checked(3)"
name: "xcb_input_change_device_key_mapping_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_change_device_key_mapping_checked/"
description: "xcb_input_change_device_key_mapping –"
---

<p>xcb_input_change_device_key_mapping &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;

Request function

    xcb_void_cookie_t
    xcb_input_change_device_key_mapping(xcb_connection_t *conn, uint8_t device_id, xcb_input_key_code_t first_keycode, uint8_t keysyms_per_keycode, uint8_t keycode_count, const xcb_keysym_t *keysyms);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>device_id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>first_keycode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>keysyms_per_keycode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>keycode_count</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>keysyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_change_device_key_mapping_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
