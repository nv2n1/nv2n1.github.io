---
title: "xcb_randr_get_monitors_reply(3)"
name: "xcb_randr_get_monitors_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_monitors_reply/"
description: "xcb_randr_get_monitors –"
---

<p>xcb_randr_get_monitors &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_monitors_cookie_t xcb_randr_get_monitors(xcb_connection_t *conn, xcb_window_t window, uint8_t get_active);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_monitors_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_timestamp_t <i>timestamp</i>;
 uint32_t <i>nMonitors</i>;
 uint32_t <i>nOutputs</i>;
 uint8_t <i>pad1</i>[12];
} <code>xcb_randr_get_monitors_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_monitors_reply_t *<code>xcb_randr_get_monitors_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_monitors_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_randr_get_monitors_monitors_length</code>(const xcb_randr_get_monitors_reply_t *<i>reply</i>);</p>
<dd>xcb_randr_monitor_info_iterator_t <code>xcb_randr_get_monitors_monitors_iterator</code>(const xcb_randr_get_monitors_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>get_active</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_MONITORS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>timestamp</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nMonitors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nOutputs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_monitors_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_monitors_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_monitors_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
