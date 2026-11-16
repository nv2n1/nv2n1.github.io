---
title: "xcb_randr_set_crtc_gamma(3)"
name: "xcb_randr_set_crtc_gamma"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_set_crtc_gamma/"
description: "xcb_randr_set_crtc_gamma –"
---

<p>xcb_randr_set_crtc_gamma &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;
Request function
    xcb_void_cookie_t
    xcb_randr_set_crtc_gamma(xcb_connection_t *conn, xcb_randr_crtc_t crtc, uint16_t size, const uint16_t *red, const uint16_t *green, const uint16_t *blue);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>crtc</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>size</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>red</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>green</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>blue</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_randr_set_crtc_gamma_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
