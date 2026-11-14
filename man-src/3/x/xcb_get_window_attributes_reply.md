---
title: "xcb_get_window_attributes_reply(3)"
name: "xcb_get_window_attributes_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_get_window_attributes_reply/"
description: "xcb_get_window_attributes – Gets window attributes"
---

<p>xcb_get_window_attributes &#8211; Gets window attributes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_get_window_attributes_cookie_t xcb_get_window_attributes(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_get_window_attributes_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>backing_store</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_visualid_t <i>visual</i>;
 uint16_t <i>_class</i>;
 uint8_t <i>bit_gravity</i>;
 uint8_t <i>win_gravity</i>;
 uint32_t <i>backing_planes</i>;
 uint32_t <i>backing_pixel</i>;
 uint8_t <i>save_under</i>;
 uint8_t <i>map_is_installed</i>;
 uint8_t <i>map_state</i>;
 uint8_t <i>override_redirect</i>;
 xcb_colormap_t <i>colormap</i>;
 uint32_t <i>all_event_masks</i>;
 uint32_t <i>your_event_mask</i>;
 uint16_t <i>do_not_propagate_mask</i>;
 uint8_t <i>pad0</i>[2];
} <code>xcb_get_window_attributes_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_get_window_attributes_reply_t *<code>xcb_get_window_attributes_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_get_window_attributes_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to get the attributes from.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GET_WINDOW_ATTRIBUTES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>backing_store</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_BACKING_STORE_NOT_USEFUL</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_BACKING_STORE_WHEN_MAPPED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_BACKING_STORE_ALWAYS</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>visual</i></p>
<dd>The associated visual structure of <i>window</i>.</p>
<dt><i>_class</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_WINDOW_CLASS_COPY_FROM_PARENT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_WINDOW_CLASS_INPUT_OUTPUT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_WINDOW_CLASS_INPUT_ONLY</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>bit_gravity</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_GRAVITY_BIT_FORGET</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_WIN_UNMAP</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_CENTER</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_STATIC</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>win_gravity</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_GRAVITY_BIT_FORGET</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_WIN_UNMAP</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_NORTH_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_CENTER</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH_WEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_SOUTH_EAST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_GRAVITY_STATIC</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>backing_planes</i></p>
<dd>Planes to be preserved if possible.</p>
<dt><i>backing_pixel</i></p>
<dd>Value to be used when restoring planes.</p>
<dt><i>save_under</i></p>
<dd>Boolean, should bits under be saved?</p>
<dt><i>map_is_installed</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>map_state</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_MAP_STATE_UNMAPPED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_MAP_STATE_UNVIEWABLE</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_MAP_STATE_VIEWABLE</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>override_redirect</i></p>
<dd>Window managers should ignore this window if <i>override_redirect</i> is 1.</p>
<dt><i>colormap</i></p>
<dd>Color map to be associated with window.</p>
<dt><i>all_event_masks</i></p>
<dd>Set of events all people have interest in.</p>
<dt><i>your_event_mask</i></p>
<dd>My event mask.</p>
<dt><i>do_not_propagate_mask</i></p>
<dd>Set of events that should not propagate.</dl>
<h2>Description</h2>
<p>Gets the current attributes for the specified <i>window</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_get_window_attributes_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_get_window_attributes_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_get_window_attributes_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>window</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
