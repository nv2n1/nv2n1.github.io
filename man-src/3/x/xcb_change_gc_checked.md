---
title: "xcb_change_gc_checked(3)"
name: "xcb_change_gc_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_gc_checked/"
description: "xcb_change_gc – change graphics context components"
---

<p>xcb_change_gc &#8211; change graphics context components</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_change_gc(xcb_connection_t *conn, xcb_gcontext_t gc, uint32_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>gc</i></p>
<dd>The graphics context to change.</p>
<dt><i>value_mask</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_GC_FUNCTION</i></p>
<dd>TODO: Refer to GX</p>
<dt><i>XCB_GC_PLANE_MASK</i></p>
<dd>In graphics operations, given a source and destination pixel, the result is computed bitwise on corresponding bits of the pixels; that is, a Boolean operation is performed in each bit plane. The plane-mask restricts the operation to a subset of planes, so the result is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>((src FUNC dst)&nbsp;<wbr>AND plane-mask)&nbsp;<wbr>OR&nbsp;<wbr>(dst AND&nbsp;<wbr>(NOT plane-mask))</p>
<dt><i>XCB_GC_FOREGROUND</i></p>
<dd>Foreground colorpixel.</p>
<dt><i>XCB_GC_BACKGROUND</i></p>
<dd>Background colorpixel.</p>
<dt><i>XCB_GC_LINE_WIDTH</i></p>
<dd>The line-width is measured in pixels and can be greater than or equal to one, a wide line, or the special value zero, a thin line.</p>
<dt><i>XCB_GC_LINE_STYLE</i></p>
<dd>The line-style defines which sections of a line are drawn: Solid The full path of the line is drawn. DoubleDash The full path of the line is drawn, but the even dashes are filled differently<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>than the odd dashes&nbsp;<wbr>(see fill-style), with Butt cap-style used where even and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>odd dashes meet. OnOffDash Only the even dashes are drawn, and cap-style applies to all internal ends of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the individual dashes&nbsp;<wbr>(except NotLast is treated as Butt).</p>
<dt><i>XCB_GC_CAP_STYLE</i></p>
<dd>The cap-style defines how the endpoints of a path are drawn: NotLast The result is equivalent to Butt, except that for a line-width of zero the final<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>endpoint is not drawn. Butt The result is square at the endpoint (perpendicular to the slope of the line)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>with no projection beyond. Round The result is a circular arc with its diameter equal to the line-width, centered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on the endpoint;&nbsp;<wbr>it is equivalent to Butt for line-width zero. Projecting The result is square at the end, but the path continues beyond the endpoint for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>a distance equal to half the line-width;&nbsp;<wbr>it is equivalent to Butt for line-width<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>zero.</p>
<dt><i>XCB_GC_JOIN_STYLE</i></p>
<dd>The join-style defines how corners are drawn for wide lines: Miter The outer edges of the two lines extend to meet at an angle. However, if the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>angle is less than 11 degrees, a Bevel join-style is used instead. Round The result is a circular arc with a diameter equal to the line-width, centered<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>on the joinpoint. Bevel The result is Butt endpoint styles, and then the triangular notch is filled.</p>
<dt><i>XCB_GC_FILL_STYLE</i></p>
<dd>The fill-style defines the contents of the source for line, text, and fill requests. For all text and fill requests (for example, PolyText8, PolyText16, PolyFillRectangle, FillPoly, and PolyFillArc) as well as for line requests with line-style Solid, (for example, PolyLine, PolySegment, PolyRectangle, PolyArc) and for the even dashes for line requests with line-style OnOffDash or DoubleDash: Solid Foreground Tiled Tile OpaqueStippled A tile with the same width and height as stipple but with background<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>everywhere stipple has a zero and with foreground everywhere stipple<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>has a one Stippled Foreground masked by stipple For the odd dashes for line requests with line-style DoubleDash: Solid Background Tiled Same as for even dashes OpaqueStippled Same as for even dashes Stippled Background masked by stipple</p>
<dt><i>XCB_GC_FILL_RULE</i></p>
<dd>
<dt><i>XCB_GC_TILE</i></p>
<dd>The tile/stipple represents an infinite two-dimensional plane with the tile/stipple replicated in all dimensions. When that plane is superimposed on the drawable for use in a graphics operation, the upper-left corner of some instance of the tile/stipple is at the coordinates within the drawable specified by the tile/stipple origin. The tile/stipple and clip origins are interpreted relative to the origin of whatever destination drawable is specified in a graphics request. The tile pixmap must have the same root and depth as the gcontext (or a Match error results). The stipple pixmap must have depth one and must have the same root as the gcontext (or a Match error results). For fill-style Stippled (but not fill-style OpaqueStippled), the stipple pattern is tiled in a single plane and acts as an additional clip mask to be ANDed with the clip-mask. Any size pixmap can be used for tiling or stippling, although some sizes may be faster to use than others.</p>
<dt><i>XCB_GC_STIPPLE</i></p>
<dd>The tile/stipple represents an infinite two-dimensional plane with the tile/stipple replicated in all dimensions. When that plane is superimposed on the drawable for use in a graphics operation, the upper-left corner of some instance of the tile/stipple is at the coordinates within the drawable specified by the tile/stipple origin. The tile/stipple and clip origins are interpreted relative to the origin of whatever destination drawable is specified in a graphics request. The tile pixmap must have the same root and depth as the gcontext (or a Match error results). The stipple pixmap must have depth one and must have the same root as the gcontext (or a Match error results). For fill-style Stippled (but not fill-style OpaqueStippled), the stipple pattern is tiled in a single plane and acts as an additional clip mask to be ANDed with the clip-mask. Any size pixmap can be used for tiling or stippling, although some sizes may be faster to use than others.</p>
<dt><i>XCB_GC_TILE_STIPPLE_ORIGIN_X</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_TILE_STIPPLE_ORIGIN_Y</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_FONT</i></p>
<dd>Which font to use for the <i>ImageText8</i> and <i>ImageText16</i> requests.</p>
<dt><i>XCB_GC_SUBWINDOW_MODE</i></p>
<dd>For ClipByChildren, both source and destination windows are additionally clipped by all viewable InputOutput children. For IncludeInferiors, neither source nor destination window is clipped by inferiors. This will result in including subwindow contents in the source and drawing through subwindow boundaries of the destination. The use of IncludeInferiors with a source or destination window of one depth with mapped inferiors of differing depth is not illegal, but the semantics is undefined by the core protocol.</p>
<dt><i>XCB_GC_GRAPHICS_EXPOSURES</i></p>
<dd>Whether ExposureEvents should be generated (1) or not (0). </p>
<p> The default is 1.</p>
<dt><i>XCB_GC_CLIP_ORIGIN_X</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_CLIP_ORIGIN_Y</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_CLIP_MASK</i></p>
<dd>The clip-mask restricts writes to the destination drawable. Only pixels where the clip-mask has bits set to 1 are drawn. Pixels are not drawn outside the area covered by the clip-mask or where the clip-mask has bits set to 0. The clip-mask affects all graphics requests, but it does not clip sources. The clip-mask origin is interpreted relative to the origin of whatever destination drawable is specified in a graphics request. If a pixmap is specified as the clip-mask, it must have depth 1 and have the same root as the gcontext (or a Match error results). If clip-mask is None, then pixels are always drawn, regardless of the clip origin. The clip-mask can also be set with the SetClipRectangles request.</p>
<dt><i>XCB_GC_DASH_OFFSET</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_DASH_LIST</i></p>
<dd>TODO</p>
<dt><i>XCB_GC_ARC_MODE</i></p>
<dd>TODO</dl>
</dl>
<dl>
<dd></dl>
<dt><i>value_list</i></p>
<dd>Values for each of the components specified in the bitmask <i>value_mask</i>. The order has to correspond to the order of possible <i>value_mask</i> bits. See the example.</dl>
<h2>Description</h2>
<p>Changes the components specified by <i>value_mask</i> for the specified graphics context.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_gc_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></p>
<dd>The X server could not allocate the requested resources (no memory?).</p>
<dt><i>xcb_font_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_pixmap_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>Example</h2>
<pre><code>/*
 * Changes the foreground color component of the specified graphics context.
 *
 */
void my_example(xcb_connection_t *conn, xcb_gcontext_t gc, uint32_t fg, uint32_t bg)
{
    /* C99 allows us to use a compact way of changing a single component: */
    xcb_change_gc(conn, gc, XCB_GC_FOREGROUND, (uint32_t[]){fg});

    /* The more explicit way. Beware that the order of values is important! */
    uint32_t mask = 0;
    mask |= XCB_GC_FOREGROUND;
    mask |= XCB_GC_BACKGROUND;

    uint32_t values[] = {
        fg,
        bg};
    xcb_change_gc(conn, gc, mask, values);
    xcb_flush(conn);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
