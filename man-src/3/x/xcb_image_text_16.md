---
title: "xcb_image_text_16(3)"
name: "xcb_image_text_16"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_image_text_16/"
description: "xcb_image_text_16 – Draws text"
---

<p>xcb_image_text_16 &#8211; Draws text</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_image_text_16(xcb_connection_t *conn, uint8_t string_len, xcb_drawable_t drawable, xcb_gcontext_t gc, int16_t x, int16_t y, const xcb_char2b_t *string);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>string_len</i></p>
<dd>The length of the <i>string</i> in characters. Note that this parameter limited by 255 due to using 8 bits!</p>
<dt><i>drawable</i></p>
<dd>The drawable (Window or Pixmap) to draw text on.</p>
<dt><i>gc</i></p>
<dd>The graphics context to use. </p>
<p> The following graphics context components are used: plane-mask, foreground, background, font, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask.</p>
<dt><i>x</i></p>
<dd>The x coordinate of the first character, relative to the origin of <i>drawable</i>.</p>
<dt><i>y</i></p>
<dd>The y coordinate of the first character, relative to the origin of <i>drawable</i>.</p>
<dt><i>string</i></p>
<dd>The string to draw. Only the first 255 characters are relevant due to the data type of <i>string_len</i>. Every character uses 2 bytes (hence the 16 in this request&#8217;s name).</dl>
<h2>Description</h2>
<p>Fills the destination rectangle with the background pixel from <i>gc</i>, then paints the text with the foreground pixel from <i>gc</i>. The upper-left corner of the filled rectangle is at [x, y &#8211; font-ascent]. The width is overall-width, the height is font-ascent + font-descent. The overall-width, font-ascent and font-descent are as returned by <i>xcb_query_text_extents</i> (TODO). </p>
<p> Note that using X core fonts is deprecated (but still supported) in favor of client-side rendering using Xft.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_image_text_16_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>The specified <i>drawable</i> (Window or Pixmap) does not exist.</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>The specified graphics context does not exist.</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_image_text_8/">xcb_image_text_8</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
