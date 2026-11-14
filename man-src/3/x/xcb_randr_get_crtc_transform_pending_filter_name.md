---
title: "xcb_randr_get_crtc_transform_pending_filter_name(3)"
name: "xcb_randr_get_crtc_transform_pending_filter_name"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_crtc_transform_pending_filter_name/"
description: "xcb_randr_get_crtc_transform –"
---

<p>xcb_randr_get_crtc_transform &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_crtc_transform_cookie_t xcb_randr_get_crtc_transform(xcb_connection_t *conn, xcb_randr_crtc_t crtc);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_crtc_transform_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_render_transform_t <i>pending_transform</i>;
 uint8_t <i>has_transforms</i>;
 uint8_t <i>pad1</i>[3];
 xcb_render_transform_t <i>current_transform</i>;
 uint8_t <i>pad2</i>[4];
 uint16_t <i>pending_len</i>;
 uint16_t <i>pending_nparams</i>;
 uint16_t <i>current_len</i>;
 uint16_t <i>current_nparams</i>;
} <code>xcb_randr_get_crtc_transform_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_crtc_transform_reply_t *<code>xcb_randr_get_crtc_transform_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_crtc_transform_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>char *<code>xcb_randr_get_crtc_transform_pending_filter_name</code>(const xcb_randr_get_crtc_transform_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_transform_pending_filter_name_length</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_transform_pending_filter_name_end</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>); uint8_t *xcb_randr_get_crtc_transform_pad_3 (const xcb_randr_get_crtc_transform_request_t *reply)</p>
<dd>xcb_render_fixed_t *<code>xcb_randr_get_crtc_transform_pending_params</code>(const xcb_randr_get_crtc_transform_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_transform_pending_params_length</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_transform_pending_params_end</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);</p>
<dd>char *<code>xcb_randr_get_crtc_transform_current_filter_name</code>(const xcb_randr_get_crtc_transform_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_transform_current_filter_name_length</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_transform_current_filter_name_end</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>); uint8_t *xcb_randr_get_crtc_transform_pad_4 (const xcb_randr_get_crtc_transform_request_t *reply)</p>
<dd>xcb_render_fixed_t *<code>xcb_randr_get_crtc_transform_current_params</code>(const xcb_randr_get_crtc_transform_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_crtc_transform_current_params_length</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_crtc_transform_current_params_end</code>(const xcb_randr_get_crtc_transform_reply_t *<i>reply</i>);
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
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_CRTC_TRANSFORM</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>pending_transform</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>has_transforms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>current_transform</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pending_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pending_nparams</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>current_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>current_nparams</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_crtc_transform_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_crtc_transform_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_crtc_transform_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
