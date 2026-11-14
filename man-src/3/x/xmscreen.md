---
title: "xmscreen(3)"
name: "xmscreen"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscreen/"
description: "XmScreen — The Screen widget class"
---

<p><code>XmScreen</code> &#8212; The Screen widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Screen.h&gt;</pre>
<h2>Description</h2>
<p>The XmScreen object is used by Motif widgets to store information that is specific to a screen. It also allows the toolkit to store certain information on widget hierarchies that would otherwise be unavailable. Each client has one XmScreen object for each screen that it accesses. </p>
<p> An XmScreen object is automatically created when the application creates the first shell on a screen (usually accomplished by a call to <code>XtAppInitialize</code> or <code>XtAppCreateShell</code>). It is not necessary to create an XmScreen object by any other means. An application can use the function <code>XmGetXmScreen</code> to obtain the widget ID of the XmScreen object for a given screen. </p>
<p> An application cannot supply initial values for XmScreen resources as arguments to a call to any function that creates widgets. The application or user can supply initial values in a resource file. After creating the first shell on the screen, the application can use <code>XmGetXmScreen</code> to obtain the widget ID of the XmScreen object and then call <code>XtSetValues</code> to set the XmScreen resources.</p>
<h3>Classes</h3>
<p>Screen inherits behavior and resources from <code>Core</code>. </p>
<p> The class pointer is <code>xmScreenClass</code>. </p>
<p> The class name is <code>XmScreen</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in an <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in an <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmScreen Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbitmapConversionModel</td>
<td>XmCBitmapConversionModel</td>
<td>XtEnum</td>
<td>XmPIXMAP</td>
<td>CSG??
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolorAllocationProc</td>
<td>XmCColorAllocationProc</td>
<td>XtProc</td>
<td>NULL</td>
<td>CSG??
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolorCalculationProc</td>
<td>XmCColorCalculationProc</td>
<td>XtProc</td>
<td>NULL</td>
<td>CSG??
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdarkThreshold</td>
<td>XmCDarkThreshold</td>
<td>int</td>
<td>dynamic</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultCopyCursorIcon</td>
<td>XmCDefaultCopyCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultInvalidCursorIcon</td>
<td>XmCDefaultInvalidCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultLinkCursorIcon</td>
<td>XmCDefaultLinkCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultMoveCursorIcon</td>
<td>XmCDefaultMoveCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultNoneCursorIcon</td>
<td>XmCDefaultNoneCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultSourceCursorIcon</td>
<td>XmCDefaultSourceCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultValidCursorIcon</td>
<td>XmCDefaultValidCursorIcon</td>
<td>Widget</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNfont</td>
<td>XmCFont</td>
<td>XFontStruct *</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNforegroundThreshold</td>
<td>XmCForegroundThreshold</td>
<td>int</td>
<td>dynamic</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhorizontalFontUnit</td>
<td>XmCHorizontalFontUnit</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinsensitiveStippleBitmap</td>
<td>XmCinsensitiveStippleBitmap</td>
<td>Bitmap</td>
<td>&quot;50_foreground&quot;</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlightThreshold</td>
<td>XmCLightThreshold</td>
<td>int</td>
<td>dynamic</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmenuCursor</td>
<td>XmCCursor</td>
<td>Cursor</td>
<td>arrow</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmoveOpaque</td>
<td>XmCMoveOpaque</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunpostBehavior</td>
<td>XmCUnpostBehavior</td>
<td>unsigned char</td>
<td>XmUNPOST_AND_REPLAY</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuseColorObject</td>
<td>XmCUseColorObject</td>
<td>Boolean</td>
<td>False</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNverticalFontUnit</td>
<td>XmCVerticalFontUnit</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNbitmapConversionModel</code></p>
<dd>Provides a policy for the conversion of xbm and xpm files to the <code>Pixmap</code> type. This resource takes the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmMATCH_DEPTH</code></p>
<dd>From a supplied xbm or xpm file, generates a converted pixmap file having the same depth as the widget.</p>
<dt><code>XmDYNAMIC_DEPTH</code></p>
<dd>Converts an input xbm file to a <code>Pixmap</code> of depth 1, or converts an input xpm file to a <code>Pixmap</code> having the same depth as the widget.</dl>
</dl>
<dt><code>XmNcolorAllocationProc</code></p>
<dd>Identifies the procedure to be used for color allocation. Normally, this procedure is an application-defined color allocation procedure. However, if no application-defined color allocation procedure is set, the system uses Motif&#8217;s predefined color allocation procedure.</p>
<dt><code>XmNcolorCalculationProc</code></p>
<dd>Identifies the procedure to be used for per-widget color calculation. Normally, this procedure is an application-defined color calculation procedure. However, if no application-defined color calculation procedure is set, the system uses Motif&#8217;s predefined color calculation procedure.</p>
<dt><code>XmNdarkThreshold</code></p>
<dd>An integer between 0 (zero) and 100, inclusive, that specifies a level of perceived brightness for a color. If the perceived brightness of the background color is below this level, Motif treats the background as &quot;dark&quot; when computing default shadow and select colors. If this resource is specified for a particular screen, it applies to widgets created on that screen; otherwise it applies to widgets created on all screens. The default value is implementation specific.</p>
<dt><code>XmNdefaultCopyCursorIcon</code></p>
<dd>Specifies the DragIcon used during a drag operation when the operation is a copy and no other pixmap is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultInvalidCursorIcon</code></p>
<dd>Specifies the DragIcon used to indicate that the cursor is over an invalid drop site during a drag operation when no other pixmap symbol is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultLinkCursorIcon</code></p>
<dd>Specifies the DragIcon used during a drag operation when the operation is a link and no other pixmap is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultMoveCursorIcon</code></p>
<dd>Specifies the DragIcon used during a drag operation when the operation is a move and no other pixmap is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultNoneCursorIcon</code></p>
<dd>Specifies the DragIcon used to indicate that the cursor is not over a drop site during a drag operation when no other pixmap is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultSourceCursorIcon</code></p>
<dd>Specifies the depth-1 pixmap used as a cursor when an <code>XmNsourceCursorIcon</code> is not provided by the DragContext, or it is not usable. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNdefaultValidCursorIcon</code></p>
<dd>Specifies the DragIcon used to indicate that the cursor is over a valid drop site during a drag operation when no other pixmap is specified by the application. If this resource is NULL, a system default icon is used. The system default icon is determined by the Display resource <code>XmNenableDragIcon</code>.</p>
<dt><code>XmNfont</code></p>
<dd>Specifies a font for use in computing values for <code>XmNhorizontalFontUnit</code> and <code>XmNverticalFontUnit</code>. When an application is initialized, this resource can be supplied in a resource file or through the standard command line options <code>-fn</code>, <code>-font</code>, and <code>-xrm</code>. Note that this resource is used only for the calculation of the font unit values. To specify a font to be used to display text, use a widget&#8217;s render table resource (<code>XmNrenderTable</code>).</p>
<dt><code>XmNforegroundThreshold</code></p>
<dd>An integer between 0 (zero) and 100, inclusive, that specifies a level of perceived brightness for a color. If the perceived brightness of the background color is equal to or below this level, Motif treats the background as &quot;dark&quot; when computing the default foreground and highlight colors. If the perceived brightness of the background color is above this level, Motif treats the background as &quot;light&quot; when computing the default foreground and highlight colors. When the background is &quot;dark,&quot; the default foreground and highlight is white; when the background is &quot;light,&quot; the default foreground and highlight is black. If this resource is specified for a particular screen, it applies to widgets created on that screen; otherwise, it applies to widgets created on all screens. The default value is implementation specific.</p>
<dt><code>XmNhorizontalFontUnit</code></p>
<dd>Specifies the horizontal component of the font units used by <code>XmConvertUnits</code>, and is used to interpret the values of geometry resources when the <code>XmNshellUnitType</code> resource of VendorShell or the <code>XmNunitType</code> resource of Gadget, Manager, or Primitive has the value <code>Xm100TH_FONT_UNITS</code>. If no initial value is supplied for this resource, the default is computed from the font specified in <code>XmNfont</code>. If no initial value is supplied for this resource or for <code>XmNfont</code>, the default is 10.</p>
<dd>If a call to <code>XtSetValues</code> specifies a value for <code>XmNhorizontalFontUnit</code>, this resource is set to that value. If a call to <code>XtSetValues</code> specifies a value for <code>XmNfont</code> but not for <code>XmNhorizontalFontUnit</code>, this resource is set to a value computed from the new <code>XmNfont</code>.</p>
<dd>A horizontal font unit is derived from a font as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>If the font has an <code>AVERAGE_WIDTH</code> property, the horizontal font unit is the <code>AVERAGE_WIDTH</code> property divided by 10.</p>
<dt> &bull;</p>
<dd>If the font has no <code>AVERAGE_WIDTH</code> property but has a <code>QUAD_WIDTH</code> property, the horizontal font unit is the <code>QUAD_WIDTH</code> property.</p>
<dt> &bull;</p>
<dd>If the font has no <code>AVERAGE_WIDTH</code> or <code>QUAD_WIDTH</code> property, the horizontal font unit is the sum of the font structure&#8217;s <i>min_bounds.width</i> and <i>max_bounds.width</i> divided by 2.3.</dl>
</dl>
<dt><code>XmNinsensitiveStippleBitmap</code></p>
<dd>Provides widgets with the bitmap to use when generating the insensitive visual. This bitmap is to be used as the stipple for the rendering of insensitive visuals.</p>
<dt><code>XmNlightThreshold</code></p>
<dd>An integer between 0 (zero) and 100, inclusive, that specifies a level of perceived brightness for a color. If the perceived brightness of the background color is above this level, Motif treats the background as &quot;light&quot; when computing default shadow and select colors. If this resource is specified for a particular screen, it applies to widgets created on that screen; otherwise, it applies to widgets created on all screens. The default value is implementation specific.</p>
<dt><code>XmNmenuCursor</code></p>
<dd>Sets a variable that controls the cursor used whenever this application posts a menu. This resource can be specified only once at application startup time, either by placing it within a defaults file or by using the <code>-xrm</code> command line argument. For example:</p>
<dd><code>myProg -xrm &quot;*menuCursor: arrow&quot;</code></p>
<dd>The menu cursor can also be selected in the program through the function <code>XmSetMenuCursor</code>. The following list shows acceptable cursor names. If the application does not specify a cursor or if an invalid name is supplied, the default cursor (an arrow pointing up and to the right) is used.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>X_cursor</code></p>
<dd><i>leftbutton</i></p>
<dt><i>arrow</i></p>
<dd><code>ll_angle</code></p>
<dt><code>based_arrow_down</code></p>
<dd><code>lr_angle</code></p>
<dt><code>based_arrow_up</code></p>
<dd><i>man</i></p>
<dt><i>boat</i></p>
<dd><i>middlebutton</i></p>
<dt><i>bogosity</i></p>
<dd><i>mouse</i></p>
<dt><code>bottom_left_corner</code></p>
<dd><i>pencil</i></p>
<dt><code>bottom_right_corner</code></p>
<dd><i>pirate</i></p>
<dt><code>bottom_side</code></p>
<dd><i>plus</i></p>
<dt><code>bottom_tee</code></p>
<dd><code>question_arrow</code></p>
<dt><code>box_spiral</code></p>
<dd><code>right_ptr</code></p>
<dt><code>center_ptr</code></p>
<dd><code>right_side</code></p>
<dt><i>circle</i></p>
<dd><code>right_tee</code></p>
<dt><i>clock</i></p>
<dd><i>rightbutton</i></p>
<dt><code>coffee_mug</code></p>
<dd><code>rtl_logo</code></p>
<dt><i>cross</i></p>
<dd><i>sailboat</i></p>
<dt><code>cross_reverse</code></p>
<dd><code>sb_down_arrow</code></p>
<dt><i>crosshair</i></p>
<dd><code>sb_h_double_arrow</code></p>
<dt><code>diamond_cross</code></p>
<dd><code>sb_left_arrow</code></p>
<dt><i>dot</i></p>
<dd><code>sb_right_arrow</code></p>
<dt><i>dotbox</i></p>
<dd><code>sb_up_arrow</code></p>
<dt><code>double_arrow</code></p>
<dd><code>sb_v_double_arrow</code></p>
<dt><code>draft_large</code></p>
<dd><i>shuttle</i></p>
<dt><code>draft_small</code></p>
<dd><i>sizing</i></p>
<dt><code>draped_box</code></p>
<dd><i>spider</i></p>
<dt><i>exchange</i></p>
<dd><i>spraycan</i></p>
<dt><i>fleur</i></p>
<dd><i>star</i></p>
<dt><i>gobbler</i></p>
<dd><i>target</i></p>
<dt><i>gumby</i></p>
<dd><i>tcross</i></p>
<dt><code>hand1</code></p>
<dd><code>top_left_arrow</code></p>
<dt><code>hand2</code></p>
<dd><code>top_left_corner</code></p>
<dt><i>heart</i></p>
<dd><code>top_right_corner</code></p>
<dt><i>icon</i></p>
<dd><code>top_side</code></p>
<dt><code>iron_cross</code></p>
<dd><code>left_ptr</code></p>
<dt><code>left_side</code></p>
<dd><code>top_tee</code></p>
<dt><code>left_tee</code></p>
<dd><i>trek</i></p>
<dt><code>ul_angle</code></p>
<dd><i>umbrella</i></p>
<dt><code>ur_angle</code></p>
<dd><i>watch</i></p>
<dt><code>xterm</code></p>
<dd></dl>
</dl>
<dt><code>XmNmoveOpaque</code></p>
<dd>Specifies whether an interactive operation that moves a window, such as tearing off and dragging a tear-off menu or moving a window in MWM, displays an outline of the window or a representation of the window itself during the move. If the value is True, the operation displays a representation of the window during the move. If the value is False, the operation displays an outline of the window.</p>
<dt><code>XmNunpostBehavior</code></p>
<dd>Specifies the behavior of an active menu posted in traversal mode when a subsequent menu button selection is made outside the posted menu. When the value is <code>XmUNPOST_AND_REPLAY</code>, the resource unposts the menu hierarchy and causes the server to replay the event to the window in which the pointer is located. When the value is <code>XmUNPOST</code>, the resource unposts the hierarchy without replaying the event.</p>
<dt><code>XmNuseColorObject</code></p>
<dd>Enables and disables the sharing of colors between widgets, and the dynamic changing of colors. A value of False disables this, and a value of True enables it.</p>
<dt><code>XmNuserData</code></p>
<dd>Allows the application to attach any necessary specific data to the widget. This is an internally unused resource.</p>
<dt><code>XmNverticalFontUnit</code></p>
<dd>Specifies the vertical component of the font units used by <code>XmConvertUnits</code> and used to interpret the values of geometry resources when the <code>XmNshellUnitType</code> resource of VendorShell or the <code>XmNunitType</code> resource of Gadget, Manager, or Primitive has the value <code>Xm100TH_FONT_UNITS</code>. If no initial value is supplied for this resource, the default is computed from the font specified in <code>XmNfont</code>. If no initial value is supplied for this resource or for <code>XmNfont</code>, the default is 10.</p>
<dd>If a call to <code>XtSetValues</code> specifies a value for <code>XmNverticalFontUnit</code>, this resource is set to that value. If a call to <code>XtSetValues</code> specifies a value for <code>XmNfont</code> but not for <code>XmNverticalFontUnit</code>, this resource is set to a value computed from the new <code>XmNfont</code>.</p>
<dd>A vertical font unit is derived from a font as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>If the font has a <code>PIXEL_SIZE</code> property, the vertical font unit is the <code>PIXEL_SIZE</code> property divided by 1.8.</p>
<dt> &bull;</p>
<dd>If the font has no <code>PIXEL_SIZE</code> property but has <code>POINT_SIZE</code> and <code>RESOLUTION_Y</code> properties, the vertical font unit is the product of the <code>POINT_SIZE</code> and <code>RESOLUTION_Y</code> properties divided by 1400.</p>
<dt> &bull;</p>
<dd>If the font has no <code>PIXEL_SIZE</code>, <code>POINT_SIZE</code>, or <code>RESOLUTION_Y</code> properties, the vertical font unit is the sum of the font structure&#8217;s <i>max_bounds.ascent</i> and <i>max_bounds.descent</i> divided by 2.2.</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>All of the superclass resources inherited by <code>XmScreen</code> are designated N/A (not applicable).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmgetxmscreen/">XmGetXmScreen</a></code>(3), and <code><a href="/docs/linux/man/3-xmsetmenucursor/">XmSetMenuCursor</a></code>(3),</p>
