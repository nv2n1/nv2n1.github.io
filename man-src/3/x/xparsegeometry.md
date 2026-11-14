---
title: "xparsegeometry(3)"
name: "xparsegeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xparsegeometry/"
description: "XParseGeometry, XWMGeometry – parse window geometry"
---

<p>XParseGeometry, XWMGeometry &#8211; parse window geometry </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XParseGeometry(char *<i>parsestring</i>, int *<i>x_return</i>, int *<i>y_return</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>);</p>
<dd>int XWMGeometry(Display *<i>display</i>, int <i>screen</i>, char *<i>user_geom</i>, char *<i>def_geom</i>, unsigned int <i>bwidth</i>, XSizeHints *<i>hints</i>, int *<i>x_return</i>, int *<i>y_return</i>, int *<i>width_return</i>, int *<i>height_return</i>, int *<i>gravity_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>position</i></p>
<dd>
<dt><i>default_position</i></p>
<dd>Specify the geometry specifications.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>fheight</i></p>
<dd>
<dt><i>fwidth</i></p>
<dd>Specify the font height and width in pixels (increment size).</p>
<dt><i>parsestring</i></p>
<dd>Specifies the string you want to parse.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the width and height determined.</p>
<dt><i>xadder</i></p>
<dd>
<dt><i>yadder</i></p>
<dd>Specify additional interior padding needed in the window.</p>
<dt><i>x_return</i></p>
<dd>
<dt><i>y_return</i></p>
<dd>Return the x and y offsets.</p>
<dt><i>bwidth</i></p>
<dd>Specifies the border width.</p>
<dt><i>hints</i></p>
<dd>Specifies the size hints for the window in its normal state.</p>
<dt><i>def_geom</i></p>
<dd>Specifies the application&#8217;s default geometry or NULL.</p>
<dt><i>gravity_return</i></p>
<dd>Returns the window gravity.</p>
<dt><i>user_geom</i></p>
<dd>Specifies the user-specified geometry or NULL.</dl>
<h2>Description</h2>
<p>By convention, X applications use a standard string to indicate window size and placement. <code>XParseGeometry</code> makes it easier to conform to this standard because it allows you to parse the standard window geometry. Specifically, this function lets you parse strings of the form: </p>
<p> [=][&lt;<i>width</i>&gt;{xX}&lt;<i>height</i>&gt;][{+-}&lt;<i>xoffset</i>&gt;{+-}&lt;<i>yoffset</i>&gt;] </p>
<p> The fields map into the arguments associated with this function. (Items enclosed in &lt;&gt; are integers, items in [] are optional, and items enclosed in {} indicate &#8220;choose one of.&#8221; Note that the brackets should not appear in the actual string.) If the string is not in the Host Portable Character Encoding, the result is implementation-dependent. </p>
<p> The <code>XParseGeometry</code> function returns a bitmask that indicates which of the four values (width, height, xoffset, and yoffset) were actually found in the string and whether the x and y values are negative. By convention, -0 is not equal to +0, because the user needs to be able to say &#8220;position the window relative to the right or bottom edge.&#8221; For each value found, the corresponding argument is updated. For each value not found, the argument is left unchanged. The bits are represented by <code>XValue</code>, <code>YValue</code>, <code>WidthValue</code>, <code>HeightValue</code>, <code>XNegative</code>, or <code>YNegative</code> and are defined in They will be set whenever one of the values is defined or one of the signs is set. </p>
<p> If the function returns either the <code>XValue</code> or <code>YValue</code> flag, you should place the window at the requested position. </p>
<p> The <code>XWMGeometry</code> function combines any geometry information (given in the format used by <code>XParseGeometry</code>) specified by the user and by the calling program with size hints (usually the ones to be stored in WM_NORMAL_HINTS) and returns the position, size, and gravity <code>NorthEastGravity</code>, <code>SouthEastGravity</code>, or <code>SouthWestGravity</code>) that describe the window. If the base size is not set in the <code>XSizeHints</code> structure, the minimum size is used if set. Otherwise, a base size of zero is assumed. If no minimum size is set in the hints structure, the base size is used. A mask (in the form returned by <code>XParseGeometry</code>) that describes which values came from the user specification and whether or not the position coordinates are relative to the right and bottom edges is returned. Note that these coordinates will have already been accounted for in the x_return and y_return values. </p>
<p> Note that invalid geometry specifications can cause a width or height of zero to be returned. The caller may pass the address of the hints win_gravity field as gravity_return to update the hints directly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xsetwmproperties/">XSetWMProperties</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
