---
title: "xcb_xkb_set_named_indicator_checked(3)"
name: "xcb_xkb_set_named_indicator_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_named_indicator_checked/"
description: "xcb_xkb_set_named_indicator –"
---

<p>xcb_xkb_set_named_indicator &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;
Request function
xcb_void_cookie_t xcb_xkb_set_named_indicator(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, xcb_xkb_led_class_spec_t ledClass, xcb_xkb_id_spec_t ledID, xcb_atom_t indicator, uint8_t setState, uint8_t on, uint8_t setMap, uint8_t createMap, uint8_t map_flags, uint8_t map_whichGroups, uint8_t map_groups, uint8_t map_whichMods, uint8_t map_realMods, uint16_t map_vmods, uint32_t map_ctrls);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ledClass</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ledID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>indicator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>setState</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>on</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>setMap</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>createMap</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_flags</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_whichGroups</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_groups</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_whichMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_realMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_vmods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_ctrls</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_named_indicator_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
