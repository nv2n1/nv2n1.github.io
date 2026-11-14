---
title: "xcb_randr_get_crtc_info(3)"
name: "xcb_randr_get_crtc_info"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_crtc_info/"
description: "xcb_randr_get_crtc_info –"
---

<p>xcb_randr_get_crtc_info &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_crtc_info_cookie_t xcb_randr_get_crtc_info(xcb_connection_t *conn, xcb_randr_crtc_t crtc, xcb_timestamp_t config_timestamp);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_crtc_info_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>status</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_timestamp_t <i>timestamp</i>;
 int16_t <i>x</i>;
 int16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 xcb_randr_mode_t <i>mode</i>;
 uint16_t <i>rotation</i>;
 uint16_t <i>rotations</i>;
 uint16_t <i>num_outputs</i>;
 uint16_t <i>num_possible_outputs</i>;
} <code>xcb_randr_get_crtc_info_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_crtc_info_reply_t *<code>xcb_randr_get_crtc_info_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_crtc_info_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_randr_output_t *<code>xcb_randr_get_crtc_info_outputs</code>(const xcb_randr_get_crtc_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_info_outputs_length</code>(const xcb_randr_get_crtc_info_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_info_outputs_end</code>(const xcb_randr_get_crtc_info_reply_t *<i>reply</i>);</p>
<dd>xcb_randr_output_t *<code>xcb_randr_get_crtc_info_possible</code>(const xcb_randr_get_crtc_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_info_possible_length</code>(const xcb_randr_get_crtc_info_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_info_possible_end</code>(const xcb_randr_get_crtc_info_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>crtc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>config_timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_CRTC_INFO</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>status</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rotation</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rotations</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_outputs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_possible_outputs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_crtc_info_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_crtc_info_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_crtc_info_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
