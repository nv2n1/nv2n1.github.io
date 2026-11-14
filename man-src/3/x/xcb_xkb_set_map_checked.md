---
title: "xcb_xkb_set_map_checked(3)"
name: "xcb_xkb_set_map_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_map_checked/"
description: "xcb_xkb_set_map –"
---

<p>xcb_xkb_set_map &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;

Request function

    xcb_void_cookie_t
    xcb_xkb_set_map(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint16_t present, uint16_t flags, xcb_keycode_t minKeyCode, xcb_keycode_t maxKeyCode, uint8_t firstType, uint8_t nTypes, xcb_keycode_t firstKeySym, uint8_t nKeySyms, uint16_t totalSyms, xcb_keycode_t firstKeyAction, uint8_t nKeyActions, uint16_t totalActions, xcb_keycode_t firstKeyBehavior, uint8_t nKeyBehaviors, uint8_t totalKeyBehaviors, xcb_keycode_t firstKeyExplicit, uint8_t nKeyExplicit, uint8_t totalKeyExplicit, xcb_keycode_t firstModMapKey, uint8_t nModMapKeys, uint8_t totalModMapKeys, xcb_keycode_t firstVModMapKey, uint8_t nVModMapKeys, uint8_t totalVModMapKeys, uint16_t virtualMods, const void *values);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>present</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>flags</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>minKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>maxKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeySym</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeySyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalSyms</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKeyAction</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyActions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalActions</i></p>
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
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>values</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_map_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
