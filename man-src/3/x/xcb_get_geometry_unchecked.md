---
title: "xcb_get_geometry_unchecked(3)"
name: "xcb_get_geometry_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_geometry_unchecked/"
description: "xcb_get_geometry – Get current window geometry"
---

<p>xcb_get_geometry &#8211; Get current window geometry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_get_geometry_cookie_t xcb_get_geometry(xcb_connection_t *conn, xcb_drawable_t drawable);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_geometry_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>depth</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>root</i>;
 int16_t <i>x</i>;
 int16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>border_width</i>;
 uint8_t <i>pad0</i>[2];
} <code>xcb_get_geometry_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_geometry_reply_t *<code>xcb_get_geometry_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_geometry_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>drawable</i></p>
<dd>The drawable (<i>Window</i> or <i>Pixmap</i>) of which the geometry will be received.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GET_GEOMETRY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>depth</i></p>
<dd>The depth of the drawable (bits per pixel for the object).</p>
<dt><i>root</i></p>
<dd>Root window of the screen containing <i>drawable</i>.</p>
<dt><i>x</i></p>
<dd>The X coordinate of <i>drawable</i>. If <i>drawable</i> is a window, the coordinate specifies the upper-left outer corner relative to its parent&#8217;s origin. If <i>drawable</i> is a pixmap, the X coordinate is always 0.</p>
<dt><i>y</i></p>
<dd>The Y coordinate of <i>drawable</i>. If <i>drawable</i> is a window, the coordinate specifies the upper-left outer corner relative to its parent&#8217;s origin. If <i>drawable</i> is a pixmap, the Y coordinate is always 0.</p>
<dt><i>width</i></p>
<dd>The width of <i>drawable</i>.</p>
<dt><i>height</i></p>
<dd>The height of <i>drawable</i>.</p>
<dt><i>border_width</i></p>
<dd>The border width (in pixels).</dl>
<h2>Description</h2>
<p>Gets the current geometry of the specified drawable (either <i>Window</i> or <i>Pixmap</i>).</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_geometry_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_geometry_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_geometry_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>Example</h2>
<pre><code>/*
 * Displays the x and y position of the given window.
 *
 */
void my_example(xcb_connection_t *c, xcb_window_t window)
{
    xcb_get_geometry_cookie_t cookie;
    xcb_get_geometry_reply_t *reply;

    cookie = xcb_get_geometry(c, window);
    /* ... do other work here if possible ... */
    if ((reply = xcb_get_geometry_reply(c, cookie, NULL))) {
        printf(&quot;This window is at %d, %d
&quot;, reply-&gt;x, reply-&gt;y);
    }
    free(reply);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
