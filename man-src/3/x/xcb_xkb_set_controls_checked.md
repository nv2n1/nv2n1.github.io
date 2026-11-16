---
title: "xcb_xkb_set_controls_checked(3)"
name: "xcb_xkb_set_controls_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_controls_checked/"
description: "xcb_xkb_set_controls –"
---

<p>xcb_xkb_set_controls &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;
Request function
    xcb_void_cookie_t
    xcb_xkb_set_controls(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint8_t affectInternalRealMods, uint8_t internalRealMods, uint8_t affectIgnoreLockRealMods, uint8_t ignoreLockRealMods, uint16_t affectInternalVirtualMods, uint16_t internalVirtualMods, uint16_t affectIgnoreLockVirtualMods, uint16_t ignoreLockVirtualMods, uint8_t mouseKeysDfltBtn, uint8_t groupsWrap, uint16_t accessXOptions, uint32_t affectEnabledControls, uint32_t enabledControls, uint32_t changeControls, uint16_t repeatDelay, uint16_t repeatInterval, uint16_t slowKeysDelay, uint16_t debounceDelay, uint16_t mouseKeysDelay, uint16_t mouseKeysInterval, uint16_t mouseKeysTimeToMax, uint16_t mouseKeysMaxSpeed, int16_t mouseKeysCurve, uint16_t accessXTimeout, uint32_t accessXTimeoutMask, uint32_t accessXTimeoutValues, uint16_t accessXTimeoutOptionsMask, uint16_t accessXTimeoutOptionsValues, const uint8_t *perKeyRepeat);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>affectInternalRealMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>internalRealMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>affectIgnoreLockRealMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ignoreLockRealMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>affectInternalVirtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>internalVirtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>affectIgnoreLockVirtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ignoreLockVirtualMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysDfltBtn</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>groupsWrap</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXOptions</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>affectEnabledControls</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>enabledControls</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>changeControls</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>repeatDelay</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>repeatInterval</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>slowKeysDelay</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>debounceDelay</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysDelay</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysInterval</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysTimeToMax</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysMaxSpeed</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mouseKeysCurve</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXTimeout</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXTimeoutMask</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXTimeoutValues</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXTimeoutOptionsMask</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>accessXTimeoutOptionsValues</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>perKeyRepeat</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_controls_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
