---
title: "xcb_get_keyboard_control(3)"
name: "xcb_get_keyboard_control"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_keyboard_control/"
description: "xcb_get_keyboard_control –"
---

<p>xcb_get_keyboard_control &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_get_keyboard_control_cookie_t xcb_get_keyboard_control(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_keyboard_control_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>global_auto_repeat</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>led_mask</i>;
 uint8_t <i>key_click_percent</i>;
 uint8_t <i>bell_percent</i>;
 uint16_t <i>bell_pitch</i>;
 uint16_t <i>bell_duration</i>;
 uint8_t <i>pad0</i>[2];
 uint8_t <i>auto_repeats</i>[32];
} <code>xcb_get_keyboard_control_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_keyboard_control_reply_t *<code>xcb_get_keyboard_control_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_keyboard_control_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GET_KEYBOARD_CONTROL</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>global_auto_repeat</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_AUTO_REPEAT_MODE_OFF</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_AUTO_REPEAT_MODE_ON</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_AUTO_REPEAT_MODE_DEFAULT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<dt><i>led_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>key_click_percent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bell_percent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bell_pitch</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bell_duration</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>auto_repeats</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_keyboard_control_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_keyboard_control_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_keyboard_control_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
