---
title: "xcb_randr_get_panning_unchecked(3)"
name: "xcb_randr_get_panning_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_panning_unchecked/"
description: "xcb_randr_get_panning –"
---

<p>xcb_randr_get_panning &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_panning_cookie_t xcb_randr_get_panning(xcb_connection_t *conn, xcb_randr_crtc_t crtc);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_panning_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>status</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_timestamp_t <i>timestamp</i>;
 uint16_t <i>left</i>;
 uint16_t <i>top</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>track_left</i>;
 uint16_t <i>track_top</i>;
 uint16_t <i>track_width</i>;
 uint16_t <i>track_height</i>;
 int16_t <i>border_left</i>;
 int16_t <i>border_top</i>;
 int16_t <i>border_right</i>;
 int16_t <i>border_bottom</i>;
} <code>xcb_randr_get_panning_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_panning_reply_t *<code>xcb_randr_get_panning_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_panning_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>crtc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_PANNING</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>status</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>left</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>top</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>track_left</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>track_top</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>track_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>track_height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>border_left</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>border_top</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>border_right</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>border_bottom</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_panning_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_panning_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_panning_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
