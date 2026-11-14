---
title: "xcb_randr_set_crtc_config_unchecked(3)"
name: "xcb_randr_set_crtc_config_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_set_crtc_config_unchecked/"
description: "xcb_randr_set_crtc_config –"
---

<p>xcb_randr_set_crtc_config &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;

Request function

    xcb_randr_set_crtc_config_cookie_t
    xcb_randr_set_crtc_config(xcb_connection_t *conn, xcb_randr_crtc_t crtc, xcb_timestamp_t timestamp, xcb_timestamp_t config_timestamp, int16_t x, int16_t y, xcb_randr_mode_t mode, uint16_t rotation, uint32_t outputs_len, const xcb_randr_output_t *outputs);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_set_crtc_config_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>status</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_timestamp_t <i>timestamp</i>;
 uint8_t <i>pad0</i>[20];
} <code>xcb_randr_set_crtc_config_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_set_crtc_config_reply_t *<code>xcb_randr_set_crtc_config_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_set_crtc_config_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>crtc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>config_timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rotation</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>outputs_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>outputs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_SET_CRTC_CONFIG</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>status</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_set_crtc_config_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_set_crtc_config_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_set_crtc_config_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
