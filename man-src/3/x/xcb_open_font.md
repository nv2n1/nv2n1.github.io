---
title: "xcb_open_font(3)"
name: "xcb_open_font"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_open_font/"
---

xcb_open_font - opens a font

<h2>Synopsis</h2>

<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_open_font(xcb_connection_t *conn, xcb_font_t fid, uint16_t name_len, const char *name);</code></pre>

<h2>Request Arguments</h2>

<dl><dt><i>conn</i>
<dd>The XCB connection to X11.
<dt><i>fid</i>
<dd>The ID with which you will refer to the font, created by <i>xcb_generate_id</i>.
<dt><i>name_len</i>
<dd>Length (in bytes) of <i>name</i>.
<dt><i>name</i>
<dd>A pattern describing an X core font.</dl>

<h2>Description</h2>

Opens any X core font matching the given <i>name</i> (for example &quot;-misc-fixed-*&quot;). 

 Note that X core fonts are deprecated (but still supported) in favor of client-side rendering using Xft.

<h2>Return Value</h2>

Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. 

 If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_open_font_checked</i>. See <b><a HREF="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</b> for details.

<h2>Errors</h2>

<dl><dt><i>xcb_name_error_t</i>
<dd>No font matches the given <i>name</i>.</dl>

<h2>See Also</h2>

<b><a HREF="/docs/linux/man/3-xcb-requests/">xcb-requests</a></b>(3), <b><a HREF="/docs/linux/man/3-xcb_generate_id/">xcb_generate_id</a></b>(3)

<h2>Author</h2>

Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.
