---
title: "xcb_get_property_value(3)"
name: "xcb_get_property_value"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_property_value/"
description: "xcb_get_property – Gets a window property"
---

<p>xcb_get_property &#8211; Gets a window property</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_get_property_cookie_t xcb_get_property(xcb_connection_t *conn, uint8_t _delete, xcb_window_t window, xcb_atom_t property, xcb_atom_t type, uint32_t long_offset, uint32_t long_length);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_property_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>format</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>type</i>;
 uint32_t <i>bytes_after</i>;
 uint32_t <i>value_len</i>;
 uint8_t <i>pad0</i>[12];
} <code>xcb_get_property_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_property_reply_t *<code>xcb_get_property_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_property_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>void *<code>xcb_get_property_value</code>(const xcb_get_property_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_get_property_value_length</code>(const xcb_get_property_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_get_property_value_end</code>(const xcb_get_property_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>_delete</i></p>
<dd>Whether the property should actually be deleted. For deleting a property, the specified <i>type</i> has to match the actual property type.</p>
<dt><i>window</i></p>
<dd>The window whose property you want to get.</p>
<dt><i>property</i></p>
<dd>The property you want to get (an atom).</p>
<dt><i>type</i></p>
<dd>The type of the property you want to get (an atom).</p>
<dt><i>long_offset</i></p>
<dd>Specifies the offset (in 32-bit multiples) in the specified property where the data is to be retrieved.</p>
<dt><i>long_length</i></p>
<dd>Specifies how many 32-bit multiples of data should be retrieved (e.g. if you set <i>long_length</i> to 4, you will receive 16 bytes of data).</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GET_PROPERTY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>format</i></p>
<dd>Specifies whether the data should be viewed as a list of 8-bit, 16-bit, or 32-bit quantities. Possible values are 8, 16, and 32. This information allows the X server to correctly perform byte-swap operations as necessary.</p>
<dt><i>type</i></p>
<dd>The actual type of the property (an atom).</p>
<dt><i>bytes_after</i></p>
<dd>The number of bytes remaining to be read in the property if a partial read was performed.</p>
<dt><i>value_len</i></p>
<dd>The length of value. You should use the corresponding accessor instead of this field.</dl>
<h2>Description</h2>
<p>Gets the specified <i>property</i> from the specified <i>window</i>. Properties are for example the window title (<i>WM_NAME</i>) or its minimum size (<i>WM_NORMAL_HINTS</i>). Protocols such as EWMH also use properties &#8211; for example EWMH defines the window title, encoded as UTF-8 string, in the <i>_NET_WM_NAME</i> property. </p>
<p> TODO: talk about <i>type</i> </p>
<p> TODO: talk about <i>delete</i> </p>
<p> TODO: talk about the offset/length thing. what&#8217;s a valid use case?</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_property_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_property_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_property_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_atom_error_t</i></p>
<dd><i>property</i> or <i>type</i> do not refer to a valid atom.</p>
<dt><i>xcb_value_error_t</i></p>
<dd>The specified <i>long_offset</i> is beyond the actual property length (e.g. the property has a length of 3 bytes and you are setting <i>long_offset</i> to 1, resulting in a byte offset of 4).</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>window</i> does not exist.</dl>
<h2>Example</h2>
<pre><code>/*
 * Prints the WM_NAME property of the window.
 *
 */
void my_example(xcb_connection_t *c, xcb_window_t window)
{
    xcb_get_property_cookie_t cookie;
    xcb_get_property_reply_t *reply;

    /* These atoms are predefined in the X11 protocol. */
    xcb_atom_t property = XCB_ATOM_WM_NAME;
    xcb_atom_t type = XCB_ATOM_STRING;

    // TODO: a reasonable long_length for WM_NAME?
    cookie = xcb_get_property(c, 0, window, property, type, 0, 0);
    if ((reply = xcb_get_property_reply(c, cookie, NULL))) {
        int len = xcb_get_property_value_length(reply);
        if (len == 0) {
            printf(&quot;TODO
&quot;);
            free(reply);
            return;
        }
        printf(&quot;WM_NAME is %.*s
&quot;, len,
               (char *)xcb_get_property_value(reply));
    }
    free(reply);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3), <code><a href="/docs/linux/man/3-xcb_intern_atom/">xcb_intern_atom</a></code>(3), <code><a href="/docs/linux/man/1-xprop/">xprop</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
