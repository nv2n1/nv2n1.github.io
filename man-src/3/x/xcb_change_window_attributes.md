---
title: "xcb_change_window_attributes(3)"
name: "xcb_change_window_attributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_window_attributes/"
description: "xcb_change_window_attributes – change window attributes"
---

<p>xcb_change_window_attributes &#8211; change window attributes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_change_window_attributes(xcb_connection_t *conn, xcb_window_t window, uint32_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to change.</p>
<dt><i>value_mask</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_CW_BACK_PIXMAP</i></p>
<dd>Overrides the default background-pixmap. The background pixmap and window must have the same root and same depth. Any size pixmap can be used, although some sizes may be faster than others. </p>
<p> If <i>XCB_BACK_PIXMAP_NONE</i> is specified, the window has no defined background. The server may fill the contents with the previous screen contents or with contents of its own choosing. </p>
<p> If <i>XCB_BACK_PIXMAP_PARENT_RELATIVE</i> is specified, the parent&#8217;s background is used, but the window must have the same depth as the parent (or a Match error results). The parent&#8217;s background is tracked, and the current version is used each time the window background is required.</p>
<dt><i>XCB_CW_BACK_PIXEL</i></p>
<dd>Overrides <i>BackPixmap</i>. A pixmap of undefined size filled with the specified background pixel is used for the background. Range-checking is not performed, the background pixel is truncated to the appropriate number of bits.</p>
<dt><i>XCB_CW_BORDER_PIXMAP</i></p>
<dd>Overrides the default border-pixmap. The border pixmap and window must have the same root and the same depth. Any size pixmap can be used, although some sizes may be faster than others. </p>
<p> The special value <i>XCB_COPY_FROM_PARENT</i> means the parent&#8217;s border pixmap is copied (subsequent changes to the parent&#8217;s border attribute do not affect the child), but the window must have the same depth as the parent.</p>
<dt><i>XCB_CW_BORDER_PIXEL</i></p>
<dd>Overrides <i>BorderPixmap</i>. A pixmap of undefined size filled with the specified border pixel is used for the border. Range checking is not performed on the border-pixel value, it is truncated to the appropriate number of bits.</p>
<dt><i>XCB_CW_BIT_GRAVITY</i></p>
<dd>Defines which region of the window should be retained if the window is resized.</p>
<dt><i>XCB_CW_WIN_GRAVITY</i></p>
<dd>Defines how the window should be repositioned if the parent is resized (see <i>ConfigureWindow</i>).</p>
<dt><i>XCB_CW_BACKING_STORE</i></p>
<dd>A backing-store of <i>WhenMapped</i> advises the server that maintaining contents of obscured regions when the window is mapped would be beneficial. A backing-store of <i>Always</i> advises the server that maintaining contents even when the window is unmapped would be beneficial. In this case, the server may generate an exposure event when the window is created. A value of <i>NotUseful</i> advises the server that maintaining contents is unnecessary, although a server may still choose to maintain contents while the window is mapped. Note that if the server maintains contents, then the server should maintain complete contents not just the region within the parent boundaries, even if the window is larger than its parent. While the server maintains contents, exposure events will not normally be generated, but the server may stop maintaining contents at any time.</p>
<dt><i>XCB_CW_BACKING_PLANES</i></p>
<dd>The backing-planes indicates (with bits set to 1) which bit planes of the window hold dynamic data that must be preserved in backing-stores and during save-unders.</p>
<dt><i>XCB_CW_BACKING_PIXEL</i></p>
<dd>The backing-pixel specifies what value to use in planes not covered by backing-planes. The server is free to save only the specified bit planes in the backing-store or save-under and regenerate the remaining planes with the specified pixel value. Any bits beyond the specified depth of the window in these values are simply ignored.</p>
<dt><i>XCB_CW_OVERRIDE_REDIRECT</i></p>
<dd>The override-redirect specifies whether map and configure requests on this window should override a SubstructureRedirect on the parent, typically to inform a window manager not to tamper with the window.</p>
<dt><i>XCB_CW_SAVE_UNDER</i></p>
<dd>If 1, the server is advised that when this window is mapped, saving the contents of windows it obscures would be beneficial.</p>
<dt><i>XCB_CW_EVENT_MASK</i></p>
<dd>The event-mask defines which events the client is interested in for this window (or for some event types, inferiors of the window).</p>
<dt><i>XCB_CW_DONT_PROPAGATE</i></p>
<dd>The do-not-propagate-mask defines which events should not be propagated to ancestor windows when no client has the event type selected in this window.</p>
<dt><i>XCB_CW_COLORMAP</i></p>
<dd>The colormap specifies the colormap that best reflects the true colors of the window. Servers capable of supporting multiple hardware colormaps may use this information, and window man- agers may use it for InstallColormap requests. The colormap must have the same visual type and root as the window (or a Match error results). If CopyFromParent is specified, the parent&#8217;s colormap is copied (subsequent changes to the parent&#8217;s colormap attribute do not affect the child). However, the window must have the same visual type as the parent (or a Match error results), and the parent must not have a colormap of None (or a Match error results). For an explanation of None, see FreeColormap request. The colormap is copied by sharing the colormap object between the child and the parent, not by making a complete copy of the colormap contents.</p>
<dt><i>XCB_CW_CURSOR</i></p>
<dd>If a cursor is specified, it will be used whenever the pointer is in the window. If None is speci- fied, the parent&#8217;s cursor will be used when the pointer is in the window, and any change in the parent&#8217;s cursor will cause an immediate change in the displayed cursor.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>value_list</i></p>
<dd>Values for each of the attributes specified in the bitmask <i>value_mask</i>. The order has to correspond to the order of possible <i>value_mask</i> bits. See the example.</dl>
<h2>Description</h2>
<p>Changes the attributes specified by <i>value_mask</i> for the specified <i>window</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_window_attributes_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_access_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_colormap_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_cursor_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_pixmap_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>window</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
