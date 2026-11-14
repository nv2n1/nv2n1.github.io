---
title: "xcb_randr_set_crtc_transform_checked(3)"
name: "xcb_randr_set_crtc_transform_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_set_crtc_transform_checked/"
description: "xcb_randr_set_crtc_transform –"
---

<p>xcb_randr_set_crtc_transform &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;

Request function

    xcb_void_cookie_t
    xcb_randr_set_crtc_transform(xcb_connection_t *conn, xcb_randr_crtc_t crtc, xcb_render_transform_t transform, uint16_t filter_len, const char *filter_name, uint32_t filter_params_len, const xcb_render_fixed_t *filter_params);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>crtc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>transform</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>filter_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>filter_name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>filter_params_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>filter_params</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_randr_set_crtc_transform_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
