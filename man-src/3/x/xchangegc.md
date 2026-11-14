---
title: "xchangegc(3)"
name: "xchangegc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xchangegc/"
description: "XCreateGC, XCopyGC, XChangeGC, XGetGCValues, XFreeGC, XGContextFromGC, XGCValues – create or free graphics contexts and graphics context structure"
---

<p>XCreateGC, XCopyGC, XChangeGC, XGetGCValues, XFreeGC, XGContextFromGC, XGCValues &#8211; create or free graphics contexts and graphics context structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>GC XCreateGC(Display *<i>display</i>, Drawable <i>d</i>, unsigned long <i>valuemask</i>, XGCValues *<i>values</i>);</p>
<dd>int XCopyGC(Display *<i>display</i>, GC <i>src</i>, unsigned long <i>valuemask</i>, GC <i>dest</i>);</p>
<dd>int XChangeGC(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>valuemask</i>, XGCValues *<i>values</i>);</p>
<dd>Status XGetGCValues(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>valuemask</i>, XGCValues *<i>values_return</i>);</p>
<dd>int XFreeGC(Display *<i>display</i>, GC <i>gc</i>);</p>
<dd>GContext XGContextFromGC(GC <i>gc</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>dest</i></p>
<dd>Specifies the destination GC.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>src</i></p>
<dd>Specifies the components of the source GC.</p>
<dt><i>valuemask</i></p>
<dd>Specifies which components in the GC are to be set, copied, changed, or returned. This argument is the bitwise inclusive OR of zero or more of the valid GC component mask bits.</p>
<dt><i>values</i></p>
<dd>Specifies any values as specified by the valuemask.</p>
<dt><i>values_return</i></p>
<dd>Returns the GC values in the specified <code>XGCValues</code> structure.</dl>
<h2>Description</h2>
<p>The <code>XCreateGC</code> function creates a graphics context and returns a GC. The GC can be used with any destination drawable having the same root and depth as the specified drawable. Use with other drawables results in a <code>BadMatch</code> error. </p>
<p> <code>XCreateGC</code> can generate <code>BadAlloc</code>, <code>BadDrawable</code>, <code>BadFont</code>, <code>BadMatch</code>, <code>BadPixmap</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XCopyGC</code> function copies the specified components from the source GC to the destination GC. The source and destination GCs must have the same root and depth, or a <code>BadMatch</code> error results. The valuemask specifies which component to copy, as for <code>XCreateGC</code>. </p>
<p> <code>XCopyGC</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadMatch</code> errors. </p>
<p> The <code>XChangeGC</code> function changes the components specified by valuemask for the specified GC. The values argument contains the values to be set. The values and restrictions are the same as for <code>XCreateGC</code>. Changing the clip-mask overrides any previous <code>XSetClipRectangles</code> request on the context. Changing the dash-offset or dash-list overrides any previous <code>XSetDashes</code> request on the context. The order in which components are verified and altered is server dependent. If an error is generated, a subset of the components may have been altered. </p>
<p> <code>XChangeGC</code> can generate <code>BadAlloc</code>, <code>BadFont</code>, <code>BadGC</code>, <code>BadMatch</code>, <code>BadPixmap</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XGetGCValues</code> function returns the components specified by valuemask for the specified GC. If the valuemask contains a valid set of GC mask bits <code>GCPlaneMask</code>, <code>GCForeground</code>, <code>GCBackground</code>, <code>GCLineWidth</code>, <code>GCLineStyle</code>, <code>GCCapStyle</code>, <code>GCJoinStyle</code>, <code>GCFillStyle</code>, <code>GCFillRule</code>, <code>GCTile</code>, <code>GCStipple</code>, <code>GCTileStipXOrigin</code>, <code>GCTileStipYOrigin</code>, <code>GCFont</code>, <code>GCSubwindowMode</code>, <code>GCGraphicsExposures</code>, <code>GCClipXOrigin</code>, <code>GCCLipYOrigin</code>, <code>GCDashOffset</code>, or <code>GCArcMode</code>) and no error occurs, <code>XGetGCValues</code> sets the requested components in values_return and returns a nonzero status. Otherwise, it returns a zero status. Note that the clip-mask and dash-list (represented by the <code>GCClipMask</code> and <code>GCDashList</code> bits, respectively, in the valuemask) cannot be requested. Also note that an invalid resource ID (with one or more of the three most significant bits set to 1) will be returned for <code>GCFont</code>, <code>GCTile</code>, and <code>GCStipple</code> if the component has never been explicitly set by the client. </p>
<p> The <code>XFreeGC</code> function destroys the specified GC as well as all the associated storage. </p>
<p> <code>XFreeGC</code> can generate a <code>BadGC</code> error.</p>
<h2>Structures</h2>
<p>The <code>XGCValues</code> structure contains: </p>
<p> /* GC attribute value mask bits */ </p>
<table>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCFunction</code> </td>
<td> (1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCPlaneMask</code> </td>
<td> (1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCForeground</code> </td>
<td> (1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCBackground</code> </td>
<td> (1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCLineWidth</code> </td>
<td> (1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCLineStyle</code> </td>
<td> (1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCCapStyle</code> </td>
<td> (1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCJoinStyle</code> </td>
<td> (1L&lt;&lt;7)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCFillStyle</code> </td>
<td> (1L&lt;&lt;8)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCFillRule</code> </td>
<td> (1L&lt;&lt;9)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCTile</code> </td>
<td> (1L&lt;&lt;10)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCStipple</code> </td>
<td> (1L&lt;&lt;11)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCTileStipXOrigin</code> </td>
<td> (1L&lt;&lt;12)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCTileStipYOrigin</code> </td>
<td> (1L&lt;&lt;13)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCFont</code> </td>
<td> (1L&lt;&lt;14)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCSubwindowMode</code> </td>
<td> (1L&lt;&lt;15)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCGraphicsExposures</code> </td>
<td> (1L&lt;&lt;16)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCClipXOrigin</code> </td>
<td> (1L&lt;&lt;17)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCClipYOrigin</code> </td>
<td> (1L&lt;&lt;18)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCClipMask</code> </td>
<td> (1L&lt;&lt;19)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCDashOffset</code> </td>
<td> (1L&lt;&lt;20)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCDashList</code> </td>
<td> (1L&lt;&lt;21)
</td>
</tr>
<tr VALIGN=top>
<td>#define</td>
<td> <code>GCArcMode</code> </td>
<td> (1L&lt;&lt;22)
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int function;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;logical operation&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long plane_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;plane mask&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long foreground;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;foreground pixel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long background;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;background pixel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int line_width;&nbsp;/*&nbsp;line width&nbsp;(in pixels)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int line_style;&nbsp;/*&nbsp;LineSolid, LineOnOffDash, LineDoubleDash&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int cap_style;&nbsp;<wbr>&nbsp;/*&nbsp;CapNotLast, CapButt, CapRound, CapProjecting&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int join_style;&nbsp;/*&nbsp;JoinMiter, JoinRound, JoinBevel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fill_style;&nbsp;/*&nbsp;FillSolid, FillTiled, FillStippled FillOpaqueStippled*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fill_rule;&nbsp;<wbr>&nbsp;/*&nbsp;EvenOddRule, WindingRule&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int arc_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ArcChord, ArcPieSlice&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap tile;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;tile pixmap for tiling operations&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap stipple;&nbsp;/*&nbsp;stipple 1 plane pixmap for stippling&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ts_x_origin;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;offset for tile or stipple operations&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ts_y_origin;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Font font;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;default text font for text operations&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int subwindow_mode;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;ClipByChildren, IncludeInferiors&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool graphics_exposures;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;boolean, should exposures be generated&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int clip_x_origin;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;origin for clipping&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int clip_y_origin;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pixmap clip_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;bitmap clipping;&nbsp;other calls for rects&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int dash_offset;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;patterned/dashed line information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char dashes; } XGCValues; </p>
<p> The function attributes of a GC are used when you update a section of a drawable (the destination) with bits from somewhere else (the source). The function in a GC defines how the new destination bits are to be computed from the source bits and the old destination bits. <code>GXcopy</code> is typically the most useful because it will work on a color display, but special applications may use other functions, particularly in concert with particular planes of a color display. The 16 GC functions, defined in are: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Function Name</td>
<td ALIGN=center>Value</td>
<td>Operation
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXclear</code> </td>
<td ALIGN=center> 0x0 </td>
<td> 0
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXand</code> </td>
<td ALIGN=center> 0x1 </td>
<td> src AND dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXandReverse</code> </td>
<td ALIGN=center> 0x2 </td>
<td> src AND NOT dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXcopy</code> </td>
<td ALIGN=center> 0x3 </td>
<td> src
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXandInverted</code> </td>
<td ALIGN=center> 0x4 </td>
<td> (NOT src) AND dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXnoop</code> </td>
<td ALIGN=center> 0x5 </td>
<td> dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXxor</code> </td>
<td ALIGN=center> 0x6 </td>
<td> src XOR dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXor</code> </td>
<td ALIGN=center> 0x7 </td>
<td> src OR dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXnor</code> </td>
<td ALIGN=center> 0x8 </td>
<td> (NOT src) AND (NOT dst)
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXequiv</code> </td>
<td ALIGN=center> 0x9 </td>
<td> (NOT src) XOR dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXinvert</code> </td>
<td ALIGN=center> 0xa </td>
<td> NOT dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXorReverse</code> </td>
<td ALIGN=center> 0xb </td>
<td> src OR (NOT dst)
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXcopyInverted</code> </td>
<td ALIGN=center> 0xc </td>
<td> NOT src
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXorInverted</code> </td>
<td ALIGN=center> 0xd </td>
<td> (NOT src) OR dst
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXnand</code> </td>
<td ALIGN=center> 0xe </td>
<td> (NOT src) OR (NOT dst)
</td>
</tr>
<tr VALIGN=top>
<td> <code>GXset</code> </td>
<td ALIGN=center> 0xf </td>
<td> 1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<p> Many graphics operations depend on either pixel values or planes in a GC. The planes attribute is of type long, and it specifies which planes of the destination are to be modified, one bit per plane. A monochrome display has only one plane and will be the least significant bit of the word. As planes are added to the display hardware, they will occupy more significant bits in the plane mask. </p>
<p> In graphics operations, given a source and destination pixel, the result is computed bitwise on corresponding bits of the pixels. That is, a Boolean operation is performed in each bit plane. The plane_mask restricts the operation to a subset of planes. A macro constant <code>AllPlanes</code> can be used to refer to all planes of the screen simultaneously. The result is computed by the following: </p>
<p> ((src FUNC dst) AND plane-mask) OR (dst AND (NOT plane-mask)) </p>
<p> Range checking is not performed on the values for foreground, background, or plane_mask. They are simply truncated to the appropriate number of bits. The line-width is measured in pixels and either can be greater than or equal to one (wide line) or can be the special value zero (thin line). </p>
<p> Wide lines are drawn centered on the path described by the graphics request. Unless otherwise specified by the join-style or cap-style, the bounding box of a wide line with endpoints [x1, y1], [x2, y2] and width w is a rectangle with vertices at the following real coordinates: </p>
<p> [x1-(w*sn/2), y1+(w*cs/2)], [x1+(w*sn/2), y1-(w*cs/2)], [x2-(w*sn/2), y2+(w*cs/2)], [x2+(w*sn/2), y2-(w*cs/2)] </p>
<p> Here sn is the sine of the angle of the line, and cs is the cosine of the angle of the line. A pixel is part of the line and so is drawn if the center of the pixel is fully inside the bounding box (which is viewed as having infinitely thin edges). If the center of the pixel is exactly on the bounding box, it is part of the line if and only if the interior is immediately to its right (x increasing direction). Pixels with centers on a horizontal edge are a special case and are part of the line if and only if the interior or the boundary is immediately below (y increasing direction) and the interior or the boundary is immediately to the right (x increasing direction). </p>
<p> Thin lines (zero line-width) are one-pixel-wide lines drawn using an unspecified, device-dependent algorithm. There are only two constraints on this algorithm.</p>
<dl COMPACT>
<dt>1.</p>
<dd>If a line is drawn unclipped from [x1,y1] to [x2,y2] and if another line is drawn unclipped from [x1+dx,y1+dy] to [x2+dx,y2+dy], a point [x,y] is touched by drawing the first line if and only if the point [x+dx,y+dy] is touched by drawing the second line.</p>
<dt>2.</p>
<dd>The effective set of points comprising a line cannot be affected by clipping. That is, a point is touched in a clipped line if and only if the point lies inside the clipping region and the point would be touched by the line when drawn unclipped.</dl>
<p> A wide line drawn from [x1,y1] to [x2,y2] always draws the same pixels as a wide line drawn from [x2,y2] to [x1,y1], not counting cap-style and join-style. It is recommended that this property be true for thin lines, but this is not required. A line-width of zero may differ from a line-width of one in which pixels are drawn. This permits the use of many manufacturers&#8217; line drawing hardware, which may run many times faster than the more precisely specified wide lines. </p>
<p> In general, drawing a thin line will be faster than drawing a wide line of width one. However, because of their different drawing algorithms, thin lines may not mix well aesthetically with wide lines. If it is desirable to obtain precise and uniform results across all displays, a client should always use a line-width of one rather than a line-width of zero. </p>
<p> The line-style defines which sections of a line are drawn: </p>
<table>
<tr VALIGN=top>
<td> <code>LineSolid</code> </td>
<td> The full path of the line is drawn.
</td>
</tr>
<tr VALIGN=top>
<td> <code>LineDoubleDash</code> </td>
<td> The full path of the line is drawn, but the even dashes are filled differently from the odd dashes (see fill-style) with <code>CapButt</code> style used where even and odd dashes meet.
</td>
</tr>
<tr VALIGN=top>
<td> <code>LineOnOffDash</code> </td>
<td> Only the even dashes are drawn, and cap-style applies to all internal ends of the individual dashes, except <code>CapNotLast</code> is treated as <code>CapButt</code>.
</td>
</tr>
</table>
<p> The cap-style defines how the endpoints of a path are drawn: </p>
<table>
<tr VALIGN=top>
<td> <code>CapNotLast</code> </td>
<td> This is equivalent to <code>CapButt</code> except that for a line-width of zero the final endpoint is not drawn.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapButt</code> </td>
<td> The line is square at the endpoint (perpendicular to the slope of the line) with no projection beyond.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapRound</code> </td>
<td> The line has a circular arc with the diameter equal to the line-width, centered on the endpoint. (This is equivalent to <code>CapButt</code> for line-width of zero).
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapProjecting</code> </td>
<td> The line is square at the end, but the path continues beyond the endpoint for a distance equal to half the line-width. (This is equivalent to <code>CapButt</code> for line-width of zero).
</td>
</tr>
</table>
<p> The join-style defines how corners are drawn for wide lines: </p>
<table>
<tr VALIGN=top>
<td> <code>JoinMiter</code> </td>
<td> The outer edges of two lines extend to meet at an angle. However, if the angle is less than 11 degrees, then a <code>JoinBevel</code> join-style is used instead.
</td>
</tr>
<tr VALIGN=top>
<td> <code>JoinRound</code> </td>
<td> The corner is a circular arc with the diameter equal to the line-width, centered on the joinpoint.
</td>
</tr>
<tr VALIGN=top>
<td> <code>JoinBevel</code> </td>
<td> The corner has <code>CapButt</code> endpoint styles with the triangular notch filled.
</td>
</tr>
</table>
<p> For a line with coincident endpoints (x1=x2, y1=y2), when the cap-style is applied to both endpoints, the semantics depends on the line-width and the cap-style: </p>
<table>
<tr VALIGN=top>
<td> <code>CapNotLast</code> </td>
<td> thin </td>
<td> The results are device dependent, but the desired effect is that nothing is drawn.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapButt</code> </td>
<td> thin </td>
<td> The results are device dependent, but the desired effect is that a single pixel is drawn.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapRound</code> </td>
<td> thin </td>
<td> The results are the same as for <code>CapButt</code>/thin.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapProjecting</code> </td>
<td> thin </td>
<td> The results are the same as for <code>CapButt</code>/thin.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapButt</code> </td>
<td> wide </td>
<td> Nothing is drawn.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapRound</code> </td>
<td> wide </td>
<td> The closed path is a circle, centered at the endpoint, and with the diameter equal to the line-width.
</td>
</tr>
<tr VALIGN=top>
<td> <code>CapProjecting</code> </td>
<td> wide </td>
<td> The closed path is a square, aligned with the coordinate axes, centered at the endpoint, and with the sides equal to the line-width.
</td>
</tr>
</table>
<p> For a line with coincident endpoints (x1=x2, y1=y2), when the join-style is applied at one or both endpoints, the effect is as if the line was removed from the overall path. However, if the total path consists of or is reduced to a single point joined with itself, the effect is the same as when the cap-style is applied at both endpoints. </p>
<p> The tile/stipple represents an infinite two-dimensional plane, with the tile/stipple replicated in all dimensions. When that plane is superimposed on the drawable for use in a graphics operation, the upper-left corner of some instance of the tile/stipple is at the coordinates within the drawable specified by the tile/stipple origin. The tile/stipple and clip origins are interpreted relative to the origin of whatever destination drawable is specified in a graphics request. The tile pixmap must have the same root and depth as the GC, or a <code>BadMatch</code> error results. The stipple pixmap must have depth one and must have the same root as the GC, or a <code>BadMatch</code> error results. For stipple operations where the fill-style is <code>FillStippled</code> but not <code>FillOpaqueStippled</code>, the stipple pattern is tiled in a single plane and acts as an additional clip mask to be ANDed with the clip-mask. Although some sizes may be faster to use than others, any size pixmap can be used for tiling or stippling. </p>
<p> The fill-style defines the contents of the source for line, text, and fill requests. For all text and fill requests (for example, <code>XDrawText</code>, <code>XDrawText16</code>, <code>XFillRectangle</code>, <code>XFillPolygon</code>, and <code>XFillArc</code>); for line requests with line-style <code>LineSolid</code> (for example, <code>XDrawLine</code>, <code>XDrawSegments</code>, <code>XDrawRectangle</code>, <code>XDrawArc</code>); and for the even dashes for line requests with line-style <code>LineOnOffDash</code> or <code>LineDoubleDash</code>, the following apply: </p>
<table>
<tr VALIGN=top>
<td> <code>FillSolid</code> </td>
<td> Foreground
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillTiled</code> </td>
<td> Tile
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillOpaqueStippled</code> </td>
<td> A tile with the same width and height as stipple, but with background everywhere stipple has a zero and with foreground everywhere stipple has a one
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillStippled</code> </td>
<td> Foreground masked by stipple
</td>
</tr>
</table>
<p> When drawing lines with line-style <code>LineDoubleDash</code>, the odd dashes are controlled by the fill-style in the following manner: </p>
<table>
<tr VALIGN=top>
<td> <code>FillSolid</code> </td>
<td> Background
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillTiled</code> </td>
<td> Same as for even dashes
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillOpaqueStippled</code> </td>
<td> Same as for even dashes
</td>
</tr>
<tr VALIGN=top>
<td> <code>FillStippled</code> </td>
<td> Background masked by stipple
</td>
</tr>
</table>
<p> Storing a pixmap in a GC might or might not result in a copy being made. If the pixmap is later used as the destination for a graphics request, the change might or might not be reflected in the GC. If the pixmap is used simultaneously in a graphics request both as a destination and as a tile or stipple, the results are undefined. </p>
<p> For optimum performance, you should draw as much as possible with the same GC (without changing its components). The costs of changing GC components relative to using different GCs depend on the display hardware and the server implementation. It is quite likely that some amount of GC information will be cached in display hardware and that such hardware can only cache a small number of GCs. </p>
<p> The dashes value is actually a simplified form of the more general patterns that can be set with <code>XSetDashes</code>. Specifying a value of N is equivalent to specifying the two-element list [N, N] in <code>XSetDashes</code>. The value must be nonzero, or a <code>BadValue</code> error results. </p>
<p> The clip-mask restricts writes to the destination drawable. If the clip-mask is set to a pixmap, it must have depth one and have the same root as the GC, or a <code>BadMatch</code> error results. If clip-mask is set to <code>None</code>, the pixels are always drawn regardless of the clip origin. The clip-mask also can be set by calling the <code>XSetClipRectangles</code> or <code>XSetRegion</code> functions. Only pixels where the clip-mask has a bit set to 1 are drawn. Pixels are not drawn outside the area covered by the clip-mask or where the clip-mask has a bit set to 0. The clip-mask affects all graphics requests. The clip-mask does not clip sources. The clip-mask origin is interpreted relative to the origin of whatever destination drawable is specified in a graphics request. </p>
<p> You can set the subwindow-mode to <code>ClipByChildren</code> or <code>IncludeInferiors</code>. For <code>ClipByChildren</code>, both source and destination windows are additionally clipped by all viewable <code>InputOutput</code> children. For <code>IncludeInferiors</code>, neither source nor destination window is clipped by inferiors. This will result in including subwindow contents in the source and drawing through subwindow boundaries of the destination. The use of <code>IncludeInferiors</code> on a window of one depth with mapped inferiors of differing depth is not illegal, but the semantics are undefined by the core protocol. </p>
<p> The fill-rule defines what pixels are inside (drawn) for paths given in <code>XFillPolygon</code> requests and can be set to <code>EvenOddRule</code> or <code>WindingRule</code>. For <code>EvenOddRule</code>, a point is inside if an infinite ray with the point as origin crosses the path an odd number of times. For <code>WindingRule</code>, a point is inside if an infinite ray with the point as origin crosses an unequal number of clockwise and counterclockwise directed path segments. A clockwise directed path segment is one that crosses the ray from left to right as observed from the point. A counterclockwise segment is one that crosses the ray from right to left as observed from the point. The case where a directed line segment is coincident with the ray is uninteresting because you can simply choose a different ray that is not coincident with a segment. </p>
<p> For both <code>EvenOddRule</code> and <code>WindingRule</code>, a point is infinitely small, and the path is an infinitely thin line. A pixel is inside if the center point of the pixel is inside and the center point is not on the boundary. If the center point is on the boundary, the pixel is inside if and only if the polygon interior is immediately to its right (x increasing direction). Pixels with centers on a horizontal edge are a special case and are inside if and only if the polygon interior is immediately below (y increasing direction). </p>
<p> The arc-mode controls filling in the <code>XFillArcs</code> function and can be set to <code>ArcPieSlice</code> or <code>ArcChord</code>. For <code>ArcPieSlice</code>, the arcs are pie-slice filled. For <code>ArcChord</code>, the arcs are chord filled. </p>
<p> The graphics-exposure flag controls <code>GraphicsExpose</code> event generation for <code>XCopyArea</code> and <code>XCopyPlane</code> requests (and any similar requests defined by extensions).</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-xcopyarea/">XCopyArea</a>(3), <a href="/docs/linux/man/3-xcreateregion/">XCreateRegion</a>(3), <a href="/docs/linux/man/3-xdrawarc/">XDrawArc</a>(3), <a href="/docs/linux/man/3-xdrawline/">XDrawLine</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xfillrectangle/">XFillRectangle</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
