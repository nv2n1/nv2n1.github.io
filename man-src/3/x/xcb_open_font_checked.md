---
title: "xcb_open_font_checked(3)"
name: "xcb_open_font_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_open_font_checked/"
description: "xcb_open_font – opens a font"
---

<p>xcb_open_font &#8211; opens a font</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_open_font(xcb_connection_t *conn, xcb_font_t fid, uint16_t name_len, const char *name);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>fid</i></p>
<dd>The ID with which you will refer to the font, created by <i>xcb_generate_id</i>.</p>
<dt><i>name_len</i></p>
<dd>Length (in bytes) of <i>name</i>.</p>
<dt><i>name</i></p>
<dd>A pattern describing an X core font.</dl>
<h2>Description</h2>
<p>Opens any X core font matching the given <i>name</i> (for example &quot;-misc-fixed-*&quot;). </p>
<p> Note that X core fonts are deprecated (but still supported) in favor of client-side rendering using Xft.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_open_font_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_name_error_t</i></p>
<dd>No font matches the given <i>name</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_generate_id/">xcb_generate_id</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
