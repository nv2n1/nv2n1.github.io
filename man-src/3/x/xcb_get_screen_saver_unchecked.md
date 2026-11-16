---
title: "xcb_get_screen_saver_unchecked(3)"
name: "xcb_get_screen_saver_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_screen_saver_unchecked/"
description: "xcb_get_screen_saver –"
---

<p>xcb_get_screen_saver &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_get_screen_saver_cookie_t xcb_get_screen_saver(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_screen_saver_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>timeout</i>;
 uint16_t <i>interval</i>;
 uint8_t <i>prefer_blanking</i>;
 uint8_t <i>allow_exposures</i>;
 uint8_t <i>pad1</i>[18];
} <code>xcb_get_screen_saver_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_screen_saver_reply_t *<code>xcb_get_screen_saver_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_screen_saver_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_GET_SCREEN_SAVER</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>timeout</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>interval</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>prefer_blanking</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_BLANKING_NOT_PREFERRED</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_BLANKING_PREFERRED</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_BLANKING_DEFAULT</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<dt><i>allow_exposures</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_EXPOSURES_NOT_ALLOWED</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_EXPOSURES_ALLOWED</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_EXPOSURES_DEFAULT</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_screen_saver_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_screen_saver_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_screen_saver_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
