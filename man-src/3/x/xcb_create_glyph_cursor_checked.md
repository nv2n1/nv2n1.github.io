---
title: "xcb_create_glyph_cursor_checked(3)"
name: "xcb_create_glyph_cursor_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_create_glyph_cursor_checked/"
description: "xcb_create_glyph_cursor – create cursor"
---

<p>xcb_create_glyph_cursor &#8211; create cursor</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_create_glyph_cursor(xcb_connection_t *conn, xcb_cursor_t cid, xcb_font_t source_font, xcb_font_t mask_font, uint16_t source_char, uint16_t mask_char, uint16_t fore_red, uint16_t fore_green, uint16_t fore_blue, uint16_t back_red, uint16_t back_green, uint16_t back_blue);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>cid</i></dt>
<dd>The ID with which you will refer to the cursor, created by <i>xcb_generate_id</i>.</dd>
<dt><i>source_font</i></dt>
<dd>In which font to look for the cursor glyph.</dd>
<dt><i>mask_font</i></dt>
<dd>In which font to look for the mask glyph.</dd>
<dt><i>source_char</i></dt>
<dd>The glyph of <i>source_font</i> to use.</dd>
<dt><i>mask_char</i></dt>
<dd>The glyph of <i>mask_font</i> to use as a mask: Pixels which are set to 1 define which source pixels are displayed. All pixels which are set to 0 are not displayed.</dd>
<dt><i>fore_red</i></dt>
<dd>The red value of the foreground color.</dd>
<dt><i>fore_green</i></dt>
<dd>The green value of the foreground color.</dd>
<dt><i>fore_blue</i></dt>
<dd>The blue value of the foreground color.</dd>
<dt><i>back_red</i></dt>
<dd>The red value of the background color.</dd>
<dt><i>back_green</i></dt>
<dd>The green value of the background color.</dd>
<dt><i>back_blue</i></dt>
<dd>The blue value of the background color.</dd></dl>
<h2>Description</h2>
<p>Creates a cursor from a font glyph. X provides a set of standard cursor shapes in a special font named cursor. Applications are encouraged to use this interface for their cursors because the font can be customized for the individual display type. </p>
<p> All pixels which are set to 1 in the source will use the foreground color (as specified by <i>fore_red</i>, <i>fore_green</i> and <i>fore_blue</i>). All pixels set to 0 will use the background color (as specified by <i>back_red</i>, <i>back_green</i> and <i>back_blue</i>).</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_create_glyph_cursor_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></dt>
<dd>The X server could not allocate the requested resources (no memory?).</dd>
<dt><i>xcb_font_error_t</i></dt>
<dd>The specified <i>source_font</i> or <i>mask_font</i> does not exist.</dd>
<dt><i>xcb_value_error_t</i></dt>
<dd>Either <i>source_char</i> or <i>mask_char</i> are not defined in <i>source_font</i> or <i>mask_font</i>, respectively.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
