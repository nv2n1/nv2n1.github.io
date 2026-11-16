---
title: "xcb_change_property_checked(3)"
name: "xcb_change_property_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_property_checked/"
description: "xcb_change_property – Changes a window property"
---

<p>xcb_change_property &#8211; Changes a window property</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
    xcb_void_cookie_t
    xcb_change_property(xcb_connection_t *conn, uint8_t mode, xcb_window_t window, xcb_atom_t property, xcb_atom_t type, uint8_t format, uint32_t data_len, const void *data);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>mode</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_PROP_MODE_REPLACE</i></dt>
<dd>Discard the previous property value and store the new data.</dd>
<dt><i>XCB_PROP_MODE_PREPEND</i></dt>
<dd>Insert the new data before the beginning of existing data. The <i>format</i> must match existing property value. If the property is undefined, it is treated as defined with the correct type and format with zero-length data.</dd>
<dt><i>XCB_PROP_MODE_APPEND</i></dt>
<dd>Insert the new data after the beginning of existing data. The <i>format</i> must match existing property value. If the property is undefined, it is treated as defined with the correct type and format with zero-length data.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt><i>window</i></dt>
<dd>The window whose property you want to change.</dd>
<dt><i>property</i></dt>
<dd>The property you want to change (an atom).</dd>
<dt><i>type</i></dt>
<dd>The type of the property you want to change (an atom).</dd>
<dt><i>format</i></dt>
<dd>Specifies whether the data should be viewed as a list of 8-bit, 16-bit or 32-bit quantities. Possible values are 8, 16 and 32. This information allows the X server to correctly perform byte-swap operations as necessary.</dd>
<dt><i>data_len</i></dt>
<dd>Specifies the number of elements (see <i>format</i>).</dd>
<dt><i>data</i></dt>
<dd>The property data.</dd></dl>
<h2>Description</h2>
<p>Sets or updates a property on the specified <i>window</i>. Properties are for example the window title (<i>WM_NAME</i>) or its minimum size (<i>WM_NORMAL_HINTS</i>). Protocols such as EWMH also use properties &#8211; for example EWMH defines the window title, encoded as UTF-8 string, in the <i>_NET_WM_NAME</i> property.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_property_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></dt>
<dd>The X server could not store the property (no memory?).</dd>
<dt><i>xcb_atom_error_t</i></dt>
<dd><i>property</i> or <i>type</i> do not refer to a valid atom.</dd>
<dt><i>xcb_match_error_t</i></dt>
<dd>TODO: reasons?</dd>
<dt><i>xcb_value_error_t</i></dt>
<dd>TODO: reasons?</dd>
<dt><i>xcb_window_error_t</i></dt>
<dd>The specified <i>window</i> does not exist.</dd></dl>
<h2>Example</h2>
<pre>/*
 * Sets the WM_NAME property of the window to &quot;XCB Example&quot;.
 *
 */
void my_example(xcb_connection_t *conn, xcb_window_t window) {
 xcb_change_property(conn,
 XCB_PROP_MODE_REPLACE,
 window,
 XCB_ATOM_WM_NAME,
 XCB_ATOM_STRING,
 8,
 strlen(&quot;XCB Example&quot;),
 &quot;XCB Example&quot;);
 xcb_flush(conn);
}</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/3-xcb_intern_atom/">xcb_intern_atom</a></code>(3), <code><a href="/docs/linux/man/1-xprop/">xprop</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
