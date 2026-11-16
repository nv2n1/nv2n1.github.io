---
title: "xcb_xkb_set_names(3)"
name: "xcb_xkb_set_names"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_names/"
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
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>virtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>which</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstType</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nTypes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKTLevelt</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKTLevels</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>indicators</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>groupNames</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nRadioGroups</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>firstKey</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeys</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyAliases</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>totalKTLevelNames</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>values</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_names_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
