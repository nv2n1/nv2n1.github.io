---
title: "xcb_xkb_get_map_reply(3)"
name: "xcb_xkb_get_map_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_map_reply/"
description: "xcb_xkb_get_map –"
---

<p>xcb_xkb_get_map &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_get_map_cookie_t xcb_xkb_get_map(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint16_t full, uint16_t partial, uint8_t firstType, uint8_t nTypes, xcb_keycode_t firstKeySym, uint8_t nKeySyms, xcb_keycode_t firstKeyAction, uint8_t nKeyActions, xcb_keycode_t firstKeyBehavior, uint8_t nKeyBehaviors, uint16_t virtualMods, xcb_keycode_t firstKeyExplicit, uint8_t nKeyExplicit, xcb_keycode_t firstModMapKey, uint8_t nModMapKeys, xcb_keycode_t firstVModMapKey, uint8_t nVModMapKeys);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_map_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>pad0</i>[2];
 xcb_keycode_t <i>minKeyCode</i>;
 xcb_keycode_t <i>maxKeyCode</i>;
 uint16_t <i>present</i>;
 uint8_t <i>firstType</i>;
 uint8_t <i>nTypes</i>;
 uint8_t <i>totalTypes</i>;
 xcb_keycode_t <i>firstKeySym</i>;
 uint16_t <i>totalSyms</i>;
 uint8_t <i>nKeySyms</i>;
 xcb_keycode_t <i>firstKeyAction</i>;
 uint16_t <i>totalActions</i>;
 uint8_t <i>nKeyActions</i>;
 xcb_keycode_t <i>firstKeyBehavior</i>;
 uint8_t <i>nKeyBehaviors</i>;
 uint8_t <i>totalKeyBehaviors</i>;
 xcb_keycode_t <i>firstKeyExplicit</i>;
 uint8_t <i>nKeyExplicit</i>;
 uint8_t <i>totalKeyExplicit</i>;
 xcb_keycode_t <i>firstModMapKey</i>;
 uint8_t <i>nModMapKeys</i>;
 uint8_t <i>totalModMapKeys</i>;
 xcb_keycode_t <i>firstVModMapKey</i>;
 uint8_t <i>nVModMapKeys</i>;
 uint8_t <i>totalVModMapKeys</i>;
 uint8_t <i>pad1</i>;
 uint16_t <i>virtualMods</i>;
} <code>xcb_xkb_get_map_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_map_reply_t *<code>xcb_xkb_get_map_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_map_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<p>xcb_xkb_get_map_map_t *xcb_xkb_get_map_map (const xcb_xkb_get_map_request_t *reply)</p>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>full</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>partial</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeySym</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeySyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyAction</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyActions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyBehavior</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyBehaviors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>virtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyExplicit</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyExplicit</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstModMapKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstVModMapKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nVModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_MAP</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>minKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>maxKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>present</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeySym</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalSyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeySyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyAction</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalActions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyActions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyBehavior</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyBehaviors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalKeyBehaviors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyExplicit</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyExplicit</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalKeyExplicit</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstModMapKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstVModMapKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nVModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalVModMapKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>virtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_map_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_map_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_map_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
