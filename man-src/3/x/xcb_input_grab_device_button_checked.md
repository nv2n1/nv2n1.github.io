---
title: "xcb_input_grab_device_button_checked(3)"
name: "xcb_input_grab_device_button_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_grab_device_button_checked/"
description: "xcb_input_grab_device_button –"
---

<p>xcb_input_grab_device_button &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;

Request function

    xcb_void_cookie_t
    xcb_input_grab_device_button(xcb_connection_t *conn, xcb_window_t grab_window, uint8_t grabbed_device, uint8_t modifier_device, uint16_t num_classes, uint16_t modifiers, uint8_t this_device_mode, uint8_t other_device_mode, uint8_t button, uint8_t owner_events, const xcb_input_event_class_t *classes);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>grab_window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>grabbed_device</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>modifier_device</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_classes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>modifiers</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>this_device_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>other_device_mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>button</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>owner_events</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>classes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_grab_device_button_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
