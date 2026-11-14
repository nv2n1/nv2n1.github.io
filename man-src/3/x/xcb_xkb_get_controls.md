---
title: "xcb_xkb_get_controls(3)"
name: "xcb_xkb_get_controls"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_controls/"
description: "xcb_xkb_get_controls –"
---

<p>xcb_xkb_get_controls &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_get_controls_cookie_t xcb_xkb_get_controls(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_controls_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>mouseKeysDfltBtn</i>;
 uint8_t <i>numGroups</i>;
 uint8_t <i>groupsWrap</i>;
 uint8_t <i>internalModsMask</i>;
 uint8_t <i>ignoreLockModsMask</i>;
 uint8_t <i>internalModsRealMods</i>;
 uint8_t <i>ignoreLockModsRealMods</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>internalModsVmods</i>;
 uint16_t <i>ignoreLockModsVmods</i>;
 uint16_t <i>repeatDelay</i>;
 uint16_t <i>repeatInterval</i>;
 uint16_t <i>slowKeysDelay</i>;
 uint16_t <i>debounceDelay</i>;
 uint16_t <i>mouseKeysDelay</i>;
 uint16_t <i>mouseKeysInterval</i>;
 uint16_t <i>mouseKeysTimeToMax</i>;
 uint16_t <i>mouseKeysMaxSpeed</i>;
 int16_t <i>mouseKeysCurve</i>;
 uint16_t <i>accessXOption</i>;
 uint16_t <i>accessXTimeout</i>;
 uint16_t <i>accessXTimeoutOptionsMask</i>;
 uint16_t <i>accessXTimeoutOptionsValues</i>;
 uint8_t <i>pad1</i>[2];
 uint32_t <i>accessXTimeoutMask</i>;
 uint32_t <i>accessXTimeoutValues</i>;
 uint32_t <i>enabledControls</i>;
 uint8_t <i>perKeyRepeat</i>[32];
} <code>xcb_xkb_get_controls_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_controls_reply_t *<code>xcb_xkb_get_controls_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_controls_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_CONTROLS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysDfltBtn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>numGroups</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupsWrap</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>internalModsMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ignoreLockModsMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>internalModsRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ignoreLockModsRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>internalModsVmods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ignoreLockModsVmods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>repeatDelay</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>repeatInterval</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>slowKeysDelay</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>debounceDelay</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysDelay</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysInterval</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysTimeToMax</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysMaxSpeed</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysCurve</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXOption</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeout</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutOptionsMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutOptionsValues</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutValues</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>enabledControls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>perKeyRepeat</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_controls_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_controls_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_controls_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
