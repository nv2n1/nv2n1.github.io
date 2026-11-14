---
title: "xgetwindowattributes(3)"
name: "xgetwindowattributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetwindowattributes/"
description: "XGetWindowAttributes, XGetGeometry, XWindowAttributes – get current window attribute or geometry and current window attributes structure"
---

<p>XGetWindowAttributes, XGetGeometry, XWindowAttributes &#8211; get current window attribute or geometry and current window attributes structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XGetWindowAttributes(Display *<i>display</i>, Window <i>w</i>, XWindowAttributes *<i>window_attributes_return</i>);</p>
<dd>Status XGetGeometry(Display *<i>display</i>, Drawable <i>d</i>, Window *<i>root_return</i>, int *<i>x_return</i>, int *<i>y_return</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>, unsigned int *<i>border_width_return</i>, unsigned int *<i>depth_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>border_width_return</i></p>
<dd>Returns the border width in pixels.</p>
<dt><i>d</i></p>
<dd>Specifies the drawable, which can be a window or a pixmap.</p>
<dt><i>depth_return</i></p>
<dd>Returns the depth of the drawable (bits per pixel for the object).</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>root_return</i></p>
<dd>Returns the root window.</p>
<dt><i>w</i></p>
<dd>Specifies the window whose current attributes you want to obtain.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the drawable&#8217;s dimensions (width and height).</p>
<dt><i>window_attributes_return</i></p>
<dd>Returns the specified window&#8217;s attributes in the <code>XWindowAttributes</code> structure.</p>
<dt><i>x_return</i></p>
<dd>
<dt><i>y_return</i></p>
<dd>Return the x and y coordinates that define the location of the drawable. For a window, these coordinates specify the upper-left outer corner relative to its parent&#8217;s origin. For pixmaps, these coordinates are always zero.</dl>
<h2>Description</h2>
<p>The <code>XGetWindowAttributes</code> function returns the current attributes for the specified window to an <code>XWindowAttributes</code> structure. It returns a nonzero status on success; otherwise, it returns a zero status. </p>
<p> <code>XGetWindowAttributes</code> can generate <code>BadDrawable</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XGetGeometry</code> function returns the root window and the current geometry of the drawable. The geometry of the drawable includes the x and y coordinates, width and height, border width, and depth. These are described in the argument list. It is legal to pass to this function a window whose class is <code>InputOnly</code>. It returns a nonzero status on success; otherwise, it returns a zero status.</p>
<h2>Structures</h2>
<p>The <code>XWindowAttributes</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int x, y;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;location of window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int width, height;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;width and height of window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int border_width;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;border width of window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int depth;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;depth of window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Visual&nbsp;*visual;&nbsp;/*&nbsp;the associated visual structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Window root;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;root of screen containing window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int class;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;InputOutput, InputOnly*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bit_gravity;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;one of the bit gravity values&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int win_gravity;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;one of the window gravity values&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int backing_store;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;NotUseful, WhenMapped, Always&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long backing_planes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;planes to be preserved if possible&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long backing_pixel;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;value to be used when restoring planes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool save_under;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;boolean, should bits under be saved?&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Colormap colormap;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;color map to be associated with window&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool map_installed;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;boolean, is color map currently installed*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int map_state;&nbsp;<wbr>&nbsp;/*&nbsp;IsUnmapped, IsUnviewable, IsViewable&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long all_event_masks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;set of events all people have interest in*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long your_event_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;my event mask&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long do_not_propagate_mask;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;set of events that should not propagate&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Bool override_redirect;&nbsp;/*&nbsp;boolean value for override-redirect&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Screen&nbsp;*screen;&nbsp;/*&nbsp;back pointer to correct screen&nbsp;*/ } XWindowAttributes; </p>
<p> The x and y members are set to the upper-left outer corner relative to the parent window&#8217;s origin. The width and height members are set to the inside size of the window, not including the border. The border_width member is set to the window&#8217;s border width in pixels. The depth member is set to the depth of the window (that is, bits per pixel for the object). The visual member is a pointer to the screen&#8217;s associated <code>Visual</code> structure. The root member is set to the root window of the screen containing the window. The class member is set to the window&#8217;s class and can be either <code>InputOutput</code> or <code>InputOnly</code>. </p>
<p> The bit_gravity member is set to the window&#8217;s bit gravity and can be one of the following: </p>
<table>
<tr VALIGN=top>
<td> <code>ForgetGravity</code> </td>
<td> <code>EastGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthWestGravity</code> </td>
<td> <code>SouthWestGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthGravity</code> </td>
<td> <code>SouthGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthEastGravity</code> </td>
<td> <code>SouthEastGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>WestGravity</code> </td>
<td> <code>StaticGravity</code>
</td>
</tr>
</table>
<p> The win_gravity member is set to the window&#8217;s window gravity and can be one of the following: </p>
<table>
<tr VALIGN=top>
<td> <code>UnmapGravity</code> </td>
<td> <code>EastGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthWestGravity</code> </td>
<td> <code>SouthWestGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthGravity</code> </td>
<td> <code>SouthGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>NorthEastGravity</code> </td>
<td> <code>SouthEastGravity</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>WestGravity</code> </td>
<td> <code>StaticGravity</code>
</td>
</tr>
</table>
<p> For additional information on gravity, see section 3.3. </p>
<p> The backing_store member is set to indicate how the X server should maintain the contents of a window and can be <code>WhenMapped</code>, <code>Always</code>, or <code>NotUseful</code>. The backing_planes member is set to indicate (with bits set to 1) which bit planes of the window hold dynamic data that must be preserved in backing_stores and during save_unders. The backing_pixel member is set to indicate what values to use for planes not set in backing_planes. </p>
<p> The save_under member is set to <code>True</code> or <code>False</code>. The colormap member is set to the colormap for the specified window and can be a colormap ID or <code>None</code>. The map_installed member is set to indicate whether the colormap is currently installed and can be <code>True</code> or <code>False</code>. The map_state member is set to indicate the state of the window and can be <code>IsUnmapped</code>, <code>IsUnviewable</code>, or <code>IsViewable</code>. <code>IsUnviewable</code> is used if the window is mapped but some ancestor is unmapped. </p>
<p> The all_event_masks member is set to the bitwise inclusive OR of all event masks selected on the window by all clients. The your_event_mask member is set to the bitwise inclusive OR of all event masks selected by the querying client. The do_not_propagate_mask member is set to the bitwise inclusive OR of the set of events that should not propagate. </p>
<p> The override_redirect member is set to indicate whether this window overrides structure control facilities and can be <code>True</code> or <code>False</code>. Window manager clients should ignore the window if this member is <code>True</code>. </p>
<p> The screen member is set to a screen pointer that gives you a back pointer to the correct screen. This makes it easier to obtain the screen information without having to loop over the root window fields to see which field matches.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xquerypointer/">XQueryPointer</a>(3), <a href="/docs/linux/man/3-xquerytree/">XQueryTree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
