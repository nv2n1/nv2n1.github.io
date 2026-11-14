---
title: "xcb_randr_get_screen_resources_names_length(3)"
name: "xcb_randr_get_screen_resources_names_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_screen_resources_names_length/"
description: "xcb_randr_get_screen_resources –"
---

<p>xcb_randr_get_screen_resources &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_screen_resources_cookie_t xcb_randr_get_screen_resources(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_screen_resources_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_timestamp_t <i>timestamp</i>;
 xcb_timestamp_t <i>config_timestamp</i>;
 uint16_t <i>num_crtcs</i>;
 uint16_t <i>num_outputs</i>;
 uint16_t <i>num_modes</i>;
 uint16_t <i>names_len</i>;
 uint8_t <i>pad1</i>[8];
} <code>xcb_randr_get_screen_resources_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_screen_resources_reply_t *<code>xcb_randr_get_screen_resources_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_screen_resources_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_randr_crtc_t *<code>xcb_randr_get_screen_resources_crtcs</code>(const xcb_randr_get_screen_resources_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_screen_resources_crtcs_length</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_screen_resources_crtcs_end</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_randr_output_t *<code>xcb_randr_get_screen_resources_outputs</code>(const xcb_randr_get_screen_resources_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_screen_resources_outputs_length</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_screen_resources_outputs_end</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_randr_mode_info_t *<code>xcb_randr_get_screen_resources_modes</code>(const xcb_randr_get_screen_resources_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_screen_resources_modes_length</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_randr_mode_info_iterator_t <code>xcb_randr_get_screen_resources_modes_iterator</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>uint8_t *<code>xcb_randr_get_screen_resources_names</code>(const xcb_randr_get_screen_resources_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_screen_resources_names_length</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_screen_resources_names_end</code>(const xcb_randr_get_screen_resources_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_SCREEN_RESOURCES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>config_timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_crtcs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_outputs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_modes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>names_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_screen_resources_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_screen_resources_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_screen_resources_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
