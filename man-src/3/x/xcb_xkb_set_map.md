---
title: "xcb_xkb_set_map(3)"
name: "xcb_xkb_set_map"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_map/"
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
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>present</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>flags</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>minKeyCode</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>maxKeyCode</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstType</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nTypes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKeySym</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeySyms</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalSyms</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyAction</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyActions</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalActions</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyBehavior</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyBehaviors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalKeyBehaviors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyExplicit</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyExplicit</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalKeyExplicit</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstModMapKey</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nModMapKeys</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalModMapKeys</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstVModMapKey</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nVModMapKeys</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalVModMapKeys</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>virtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>values</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_map_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
