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
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectInternalRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>internalRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectIgnoreLockRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ignoreLockRealMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectInternalVirtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>internalVirtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectIgnoreLockVirtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ignoreLockVirtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mouseKeysDfltBtn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupsWrap</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXOptions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectEnabledControls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>enabledControls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>changeControls</i></p>
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
<dt><i>accessXTimeout</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutValues</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutOptionsMask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>accessXTimeoutOptionsValues</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>perKeyRepeat</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_controls_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
