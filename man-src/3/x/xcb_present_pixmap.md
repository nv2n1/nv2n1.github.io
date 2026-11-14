---
title: "xcb_present_pixmap(3)"
name: "xcb_present_pixmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_present_pixmap/"
description: "xcb_present_pixmap –"
---

<p>xcb_present_pixmap &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/present.h&gt;

Request function

    xcb_void_cookie_t
    xcb_present_pixmap(xcb_connection_t *conn, xcb_window_t window, xcb_pixmap_t pixmap, uint32_t serial, xcb_xfixes_region_t valid, xcb_xfixes_region_t update, int16_t x_off, int16_t y_off, xcb_randr_crtc_t target_crtc, xcb_sync_fence_t wait_fence, xcb_sync_fence_t idle_fence, uint32_t options, uint64_t target_msc, uint64_t divisor, uint64_t remainder, uint32_t notifies_len, const xcb_present_notify_t *notifies);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pixmap</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>serial</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>valid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>update</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x_off</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y_off</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>target_crtc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>wait_fence</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>idle_fence</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>options</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>target_msc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>divisor</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>remainder</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>notifies_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>notifies</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_present_pixmap_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from present.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
