---
title: "xcb_alloc_color(3)"
name: "xcb_alloc_color"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_alloc_color/"
description: "xcb_alloc_color – Allocate a color"
---

<p>xcb_alloc_color &#8211; Allocate a color</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_alloc_color_cookie_t xcb_alloc_color(xcb_connection_t *conn, xcb_colormap_t cmap, uint16_t red, uint16_t green, uint16_t blue);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_alloc_color_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>red</i>;
 uint16_t <i>green</i>;
 uint16_t <i>blue</i>;
 uint8_t <i>pad1</i>[2];
 uint32_t <i>pixel</i>;
} <code>xcb_alloc_color_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_alloc_color_reply_t *<code>xcb_alloc_color_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_alloc_color_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>cmap</i></dt>
<dd>TODO</dd>
<dt><i>red</i></dt>
<dd>The red value of your color.</dd>
<dt><i>green</i></dt>
<dd>The green value of your color.</dd>
<dt><i>blue</i></dt>
<dd>The blue value of your color.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_ALLOC_COLOR</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>red</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>green</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>blue</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>pixel</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<p>Allocates a read-only colormap entry corresponding to the closest RGB value supported by the hardware. If you are using TrueColor, you can take a shortcut and directly calculate the color pixel value to avoid the round trip. But, for example, on 16-bit color setups (VNC), you can easily get the closest supported RGB value to the RGB value you are specifying.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_alloc_color_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_alloc_color_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_alloc_color_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_colormap_error_t</i></dt>
<dd>The specified colormap <i>cmap</i> does not exist.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
