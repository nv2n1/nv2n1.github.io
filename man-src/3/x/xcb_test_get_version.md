---
title: "xcb_test_get_version(3)"
name: "xcb_test_get_version"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_test_get_version/"
description: "xcb_test_get_version –"
---

<p>xcb_test_get_version &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xtest.h&gt;
Request function
xcb_test_get_version_cookie_t xcb_test_get_version(xcb_connection_t *conn, uint8_t major_version, uint16_t minor_version);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_test_get_version_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>major_version</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>minor_version</i>;
} <code>xcb_test_get_version_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_test_get_version_reply_t *<code>xcb_test_get_version_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_test_get_version_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>major_version</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>minor_version</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_TEST_GET_VERSION</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>major_version</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>minor_version</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_test_get_version_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_test_get_version_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_test_get_version_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xtest.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
