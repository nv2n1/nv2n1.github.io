---
title: "xcb_input_xi_passive_ungrab_device_checked(3)"
name: "xcb_input_xi_passive_ungrab_device_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_xi_passive_ungrab_device_checked/"
description: "xcb_input_xi_passive_ungrab_device –"
---

<p>xcb_input_xi_passive_ungrab_device &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;
Request function
    xcb_void_cookie_t
    xcb_input_xi_passive_ungrab_device(xcb_connection_t *conn, xcb_window_t grab_window, uint32_t detail, xcb_input_device_id_t deviceid, uint16_t num_modifiers, uint8_t grab_type, const uint32_t *modifiers);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>grab_window</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>detail</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>deviceid</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>num_modifiers</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>grab_type</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>modifiers</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_xi_passive_ungrab_device_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
