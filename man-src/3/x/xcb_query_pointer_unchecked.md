---
title: "xcb_query_pointer_unchecked(3)"
name: "xcb_query_pointer_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_query_pointer_unchecked/"
description: "xcb_query_pointer – get pointer coordinates"
---

<p>xcb_query_pointer &#8211; get pointer coordinates</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_query_pointer_cookie_t xcb_query_pointer(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_query_pointer_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>same_screen</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>child</i>;
 int16_t <i>root_x</i>;
 int16_t <i>root_y</i>;
 int16_t <i>win_x</i>;
 int16_t <i>win_y</i>;
 uint16_t <i>mask</i>;
 uint8_t <i>pad0</i>[2];
} <code>xcb_query_pointer_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_query_pointer_reply_t *<code>xcb_query_pointer_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_query_pointer_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>A window to check if the pointer is on the same screen as <i>window</i> (see the <i>same_screen</i> field in the reply).</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_QUERY_POINTER</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>same_screen</i></p>
<dd>If <i>same_screen</i> is False, then the pointer is not on the same screen as the argument window, <i>child</i> is None, and <i>win_x</i> and <i>win_y</i> are zero. If <i>same_screen</i> is True, then <i>win_x</i> and <i>win_y</i> are the pointer coordinates relative to the argument window&#8217;s origin, and child is the child containing the pointer, if any.</p>
<dt><i>root</i></p>
<dd>The root window the pointer is logically on.</p>
<dt><i>child</i></p>
<dd>The child window containing the pointer, if any, if <i>same_screen</i> is true. If <i>same_screen</i> is false, <i>XCB_NONE</i> is returned.</p>
<dt><i>root_x</i></p>
<dd>The pointer X position, relative to <i>root</i>.</p>
<dt><i>root_y</i></p>
<dd>The pointer Y position, relative to <i>root</i>.</p>
<dt><i>win_x</i></p>
<dd>The pointer X coordinate, relative to <i>child</i>, if <i>same_screen</i> is true. Zero otherwise.</p>
<dt><i>win_y</i></p>
<dd>The pointer Y coordinate, relative to <i>child</i>, if <i>same_screen</i> is true. Zero otherwise.</p>
<dt><i>mask</i></p>
<dd>The current logical state of the modifier keys and the buttons. Note that the logical state of a device (as seen by means of the protocol) may lag the physical state if device event processing is frozen.</dl>
<h2>Description</h2>
<p>Gets the root window the pointer is logically on and the pointer coordinates relative to the root window&#8217;s origin.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_query_pointer_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_query_pointer_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_query_pointer_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>window</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
