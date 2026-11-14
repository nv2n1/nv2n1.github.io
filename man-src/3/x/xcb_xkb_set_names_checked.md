---
title: "xcb_xkb_set_names_checked(3)"
name: "xcb_xkb_set_names_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_names_checked/"
description: "xcb_xkb_set_names –"
---

<p>xcb_xkb_set_names &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;

Request function

    xcb_void_cookie_t
    xcb_xkb_set_names(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint16_t virtualMods, uint32_t which, uint8_t firstType, uint8_t nTypes, uint8_t firstKTLevelt, uint8_t nKTLevels, uint32_t indicators, uint8_t groupNames, uint8_t nRadioGroups, xcb_keycode_t firstKey, uint8_t nKeys, uint8_t nKeyAliases, uint16_t totalKTLevelNames, const void *values);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>virtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>which</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKTLevelt</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKTLevels</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>indicators</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupNames</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nRadioGroups</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyAliases</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>totalKTLevelNames</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>values</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_names_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
