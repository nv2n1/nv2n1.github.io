---
title: "xcb_randr_get_screen_info_rates_length(3)"
name: "xcb_randr_get_screen_info_rates_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_screen_info_rates_length/"
description: "xcb_randr_get_screen_info –"
---

<p>xcb_randr_get_screen_info &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;
Request function
xcb_randr_get_screen_info_cookie_t xcb_randr_get_screen_info(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_screen_info_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>rotations</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>root</i>;
 xcb_timestamp_t <i>timestamp</i>;
 xcb_timestamp_t <i>config_timestamp</i>;
 uint16_t <i>nSizes</i>;
 uint16_t <i>sizeID</i>;
 uint16_t <i>rotation</i>;
 uint16_t <i>rate</i>;
 uint16_t <i>nInfo</i>;
 uint8_t <i>pad0</i>[2];
} <code>xcb_randr_get_screen_info_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_screen_info_reply_t *<code>xcb_randr_get_screen_info_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_screen_info_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_randr_screen_size_t *<code>xcb_randr_get_screen_info_sizes</code>(const xcb_randr_get_screen_info_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_randr_get_screen_info_sizes_length</code>(const xcb_randr_get_screen_info_reply_t *<i>reply</i>);</dd>
<dd>xcb_randr_screen_size_iterator_t <code>xcb_randr_get_screen_info_sizes_iterator</code>(const xcb_randr_get_screen_info_reply_t *<i>reply</i>);</dd>
<dd>int <code>xcb_randr_get_screen_info_rates_length</code>(const xcb_randr_get_screen_info_reply_t *<i>reply</i>);</dd>
<dd>xcb_randr_refresh_rates_iterator_t <code>xcb_randr_get_screen_info_rates_iterator</code>(const xcb_randr_get_screen_info_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>window</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_SCREEN_INFO</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>rotations</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>root</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>timestamp</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>config_timestamp</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nSizes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>sizeID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>rotation</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>rate</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nInfo</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_screen_info_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_screen_info_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_screen_info_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
