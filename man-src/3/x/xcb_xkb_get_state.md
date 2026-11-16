---
title: "xcb_xkb_get_state(3)"
name: "xcb_xkb_get_state"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_state/"
description: "xcb_xkb_get_state –"
---

<p>xcb_xkb_get_state &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;
Request function
xcb_xkb_get_state_cookie_t xcb_xkb_get_state(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_state_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>mods</i>;
 uint8_t <i>baseMods</i>;
 uint8_t <i>latchedMods</i>;
 uint8_t <i>lockedMods</i>;
 uint8_t <i>group</i>;
 uint8_t <i>lockedGroup</i>;
 int16_t <i>baseGroup</i>;
 int16_t <i>latchedGroup</i>;
 uint8_t <i>compatState</i>;
 uint8_t <i>grabMods</i>;
 uint8_t <i>compatGrabMods</i>;
 uint8_t <i>lookupMods</i>;
 uint8_t <i>compatLookupMods</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>ptrBtnState</i>;
 uint8_t <i>pad1</i>[6];
} <code>xcb_xkb_get_state_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_state_reply_t *<code>xcb_xkb_get_state_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_state_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_STATE</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>deviceID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>baseMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>latchedMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>lockedMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>group</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>lockedGroup</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>baseGroup</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>latchedGroup</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>compatState</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>grabMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>compatGrabMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>lookupMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>compatLookupMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ptrBtnState</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_state_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_state_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_state_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
