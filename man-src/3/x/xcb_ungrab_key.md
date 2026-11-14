---
title: "xcb_ungrab_key(3)"
name: "xcb_ungrab_key"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_ungrab_key/"
description: "xcb_ungrab_key – release a key combination"
---

<p>xcb_ungrab_key &#8211; release a key combination</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_ungrab_key(xcb_connection_t *conn, xcb_keycode_t key, xcb_window_t grab_window, uint16_t modifiers);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>key</i></p>
<dd>The keycode of the specified key combination. </p>
<p> Using the special value <i>XCB_GRAB_ANY</i> means releasing all possible key codes.</p>
<dt><i>grab_window</i></p>
<dd>The window on which the grabbed key combination will be released.</p>
<dt><i>modifiers</i></p>
<dd>The modifiers of the specified key combination. </p>
<p> Using the special value <i>XCB_MOD_MASK_ANY</i> means releasing the key combination with every possible modifier combination.</dl>
<h2>Description</h2>
<p>Releases the key combination on <i>grab_window</i> if you grabbed it using <i>xcb_grab_key</i> before.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_ungrab_key_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>grab_window</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_key/">xcb_grab_key</a></code>(3), <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
