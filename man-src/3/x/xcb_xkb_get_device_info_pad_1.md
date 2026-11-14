---
title: "xcb_xkb_get_device_info_pad_1(3)"
name: "xcb_xkb_get_device_info_pad_1"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_device_info_pad_1/"
description: "xcb_xkb_get_device_info –"
---

<p>xcb_xkb_get_device_info &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_get_device_info_cookie_t xcb_xkb_get_device_info(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint16_t wanted, uint8_t allButtons, uint8_t firstButton, uint8_t nButtons, xcb_xkb_led_class_spec_t ledClass, xcb_xkb_id_spec_t ledID);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_device_info_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>present</i>;
 uint16_t <i>supported</i>;
 uint16_t <i>unsupported</i>;
 uint16_t <i>nDeviceLedFBs</i>;
 uint8_t <i>firstBtnWanted</i>;
 uint8_t <i>nBtnsWanted</i>;
 uint8_t <i>firstBtnRtrn</i>;
 uint8_t <i>nBtnsRtrn</i>;
 uint8_t <i>totalBtns</i>;
 uint8_t <i>hasOwnState</i>;
 uint16_t <i>dfltKbdFB</i>;
 uint16_t <i>dfltLedFB</i>;
 uint8_t <i>pad0</i>[2];
 xcb_atom_t <i>devType</i>;
 uint16_t <i>nameLen</i>;
} <code>xcb_xkb_get_device_info_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_device_info_reply_t *<code>xcb_xkb_get_device_info_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_device_info_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_xkb_string8_t *<code>xcb_xkb_get_device_info_name</code>(const xcb_xkb_get_device_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_device_info_name_length</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_xkb_get_device_info_name_end</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>); uint8_t *xcb_xkb_get_device_info_pad_1 (const xcb_xkb_get_device_info_request_t *reply)</p>
<dd>xcb_xkb_action_t *<code>xcb_xkb_get_device_info_btn_actions</code>(const xcb_xkb_get_device_info_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_device_info_btn_actions_length</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_action_iterator_t <code>xcb_xkb_get_device_info_btn_actions_iterator</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_device_info_leds_length</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_device_led_info_iterator_t <code>xcb_xkb_get_device_info_leds_iterator</code>(const xcb_xkb_get_device_info_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>wanted</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>allButtons</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstButton</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nButtons</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ledClass</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ledID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_DEVICE_INFO</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>present</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>supported</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>unsupported</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nDeviceLedFBs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstBtnWanted</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nBtnsWanted</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstBtnRtrn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nBtnsRtrn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalBtns</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>hasOwnState</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dfltKbdFB</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dfltLedFB</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>devType</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nameLen</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_device_info_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_device_info_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_device_info_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
