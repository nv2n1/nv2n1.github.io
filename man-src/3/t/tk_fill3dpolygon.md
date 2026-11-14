---
title: "tk_fill3dpolygon(3)"
name: "tk_fill3dpolygon"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_fill3dpolygon/"
description: "Tk_Alloc3DBorderFromObj, Tk_Get3DBorder, Tk_Get3DBorderFromObj, Tk_Draw3DRectangle, Tk_Fill3DRectangle, Tk_Draw3DPolygon, Tk_Fill3DPolygon, Tk_3DVerticalBevel, Tk_3DHorizontalBevel, Tk_SetBackgroun..."
---

<p>Tk_Alloc3DBorderFromObj, Tk_Get3DBorder, Tk_Get3DBorderFromObj, Tk_Draw3DRectangle, Tk_Fill3DRectangle, Tk_Draw3DPolygon, Tk_Fill3DPolygon, Tk_3DVerticalBevel, Tk_3DHorizontalBevel, Tk_SetBackgroundFromBorder, Tk_NameOf3DBorder, Tk_3DBorderColor, Tk_3DBorderGC, Tk_Free3DBorderFromObj, Tk_Free3DBorder &#8211; draw borders with three-dimensional appearance </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Tk_3DBorder
<code>Tk_Alloc3DBorderFromObj(</code><i>interp, tkwin, objPtr</i><code>)</code>
Tk_3DBorder
<code>Tk_Get3DBorder(</code><i>interp, tkwin, colorName</i><code>)</code>
Tk_3DBorder
<code>Tk_Get3DBorderFromObj(</code><i>tkwin, objPtr</i><code>)</code>
void
<code>Tk_Draw3DRectangle(</code><i>tkwin, drawable, border, x, y, width, height, borderWidth, relief</i><code>)</code>
void
<code>Tk_Fill3DRectangle(</code><i>tkwin, drawable, border, x, y, width, height, borderWidth, relief</i><code>)</code>
void
<code>Tk_Draw3DPolygon(</code><i>tkwin, drawable, border, pointPtr, numPoints, polyBorderWidth, leftRelief</i><code>)</code>
void
<code>Tk_Fill3DPolygon(</code><i>tkwin, drawable, border, pointPtr, numPoints, polyBorderWidth, leftRelief</i><code>)</code>
void
<code>Tk_3DVerticalBevel</code>(<i>tkwin, drawable, border, x, y, width, height, leftBevel, relief</i><code>)</code>
void
<code>Tk_3DHorizontalBevel</code>(<i>tkwin, drawable, border, x, y, width, height, leftIn, rightIn, topBevel, relief</i><code>)</code>
void
<code>Tk_SetBackgroundFromBorder(</code><i>tkwin, border</i><code>)</code>
const char *
<code>Tk_NameOf3DBorder(</code><i>border</i><code>)</code>
XColor *
<code>Tk_3DBorderColor(</code><i>border</i><code>)</code>
GC *
<code>Tk_3DBorderGC(</code><i>tkwin, border, which</i><code>)</code>
<code>Tk_Free3DBorderFromObj(</code><i>tkwin, objPtr</i><code>)</code>
<code>Tk_Free3DBorder(</code><i>border</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>Tk_Window <i>tkwin</i> (in) Token for window (for all procedures except <code>Tk_Get3DBorder</code>, must be the window for which the border was allocated).</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) Pointer to object whose value describes color corresponding to background (flat areas). Illuminated edges will be brighter than this and shadowed edges will be darker than this.</p>
<dd>char <i>*colorName</i> (in) Same as <i>objPtr</i> except value is supplied as a string rather than an object.</p>
<dd>Drawable <i>drawable</i> (in) X token for window or pixmap; indicates where graphics are to be drawn. Must either be the X window for <i>tkwin</i> or a pixmap with the same screen and depth as <i>tkwin</i>.</p>
<dd>Tk_3DBorder <i>border</i> (in) Token for border previously allocated in call to <code>Tk_Get3DBorder</code>.</p>
<dd>int <i>x</i> (in) X-coordinate of upper-left corner of rectangle describing border or bevel, in pixels.</p>
<dd>int <i>y</i> (in) Y-coordinate of upper-left corner of rectangle describing border or bevel, in pixels.</p>
<dd>int <i>width</i> (in) Width of rectangle describing border or bevel, in pixels.</p>
<dd>int <i>height</i> (in) Height of rectangle describing border or bevel, in pixels.</p>
<dd>int <i>borderWidth</i> (in) Width of border in pixels. Positive means border is inside rectangle given by <i>x</i>, <i>y</i>, <i>width</i>, <i>height</i>, negative means border is outside rectangle.</p>
<dd>int <i>relief</i> (in) Indicates 3-D position of interior of object relative to exterior; should be <code>TK_RELIEF_RAISED</code>, <code>TK_RELIEF_SUNKEN</code>, <code>TK_RELIEF_GROOVE</code>, <code>TK_RELIEF_SOLID</code>, or <code>TK_RELIEF_RIDGE</code> (may also be <code>TK_RELIEF_FLAT</code> for <code>Tk_Fill3DRectangle</code>).</p>
<dd>XPoint <i>*pointPtr</i> (in) Pointer to array of points describing the set of vertices in a polygon. The polygon need not be closed (it will be closed automatically if it is not).</p>
<dd>int <i>numPoints</i> (in) Number of points at <i>*pointPtr</i>.</p>
<dd>int <i>polyBorderWidth</i> (in) Width of border in pixels. If positive, border is drawn to left of trajectory given by <i>pointPtr</i>; if negative, border is drawn to right of trajectory. If <i>leftRelief</i> is <code>TK_RELIEF_GROOVE</code> or <code>TK_RELIEF_RIDGE</code> then the border is centered on the trajectory.</p>
<dd>int <i>leftRelief</i> (in) Height of left side of polygon&#8217;s path relative to right. <code>TK_RELIEF_RAISED</code> means left side should appear higher and <code>TK_RELIEF_SUNKEN</code> means right side should appear higher; <code>TK_RELIEF_GROOVE</code> and <code>TK_RELIEF_RIDGE</code> mean the obvious things. For <code>Tk_Fill3DPolygon</code>, <code>TK_RELIEF_FLAT</code> may also be specified to indicate no difference in height.</p>
<dd>int <i>leftBevel</i> (in) Non-zero means this bevel forms the left side of the object; zero means it forms the right side.</p>
<dd>int <i>leftIn</i> (in) Non-zero means that the left edge of the horizontal bevel angles in, so that the bottom of the edge is farther to the right than the top. Zero means the edge angles out, so that the bottom is farther to the left than the top.</p>
<dd>int <i>rightIn</i> (in) Non-zero means that the right edge of the horizontal bevel angles in, so that the bottom of the edge is farther to the left than the top. Zero means the edge angles out, so that the bottom is farther to the right than the top.</p>
<dd>int <i>topBevel</i> (in) Non-zero means this bevel forms the top side of the object; zero means it forms the bottom side.</p>
<dd>int <i>which</i> (in) Specifies which of the border&#8217;s graphics contexts is desired. Must be <code>TK_3D_FLAT_GC</code>, <code>TK_3D_LIGHT_GC</code>, or <code>TK_3D_DARK_GC</code>. </p>
</dl>
<h2>Description</h2>
<p>These procedures provide facilities for drawing window borders in a way that produces a three-dimensional appearance. <code>Tk_Alloc3DBorderFromObj</code> allocates colors and Pixmaps needed to draw a border in the window given by the <i>tkwin</i> argument. The value of <i>objPtr</i> is a standard Tk color name that determines the border colors. The color indicated by <i>objPtr</i> will not actually be used in the border; it indicates the background color for the window (i.e. a color for flat surfaces). The illuminated portions of the border will appear brighter than indicated by <i>objPtr</i>, and the shadowed portions of the border will appear darker than <i>objPtr</i>. </p>
<p> <code>Tk_Alloc3DBorderFromObj</code> returns a token that may be used in later calls to <code>Tk_Draw3DRectangle</code>. If an error occurs in allocating information for the border (e.g. a bogus color name was given) then NULL is returned and an error message is left in <i>interp-&gt;result</i>. If it returns successfully, <code>Tk_Alloc3DBorderFromObj</code> caches information about the return value in <i>objPtr</i>, which speeds up future calls to <code>Tk_Alloc3DBorderFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> <code>Tk_Get3DBorder</code> is identical to <code>Tk_Alloc3DBorderFromObj</code> except that the color is specified with a string instead of an object. This prevents <code>Tk_Get3DBorder</code> from caching the return value, so <code>Tk_Get3DBorder</code> is less efficient than <code>Tk_Alloc3DBorderFromObj</code>. </p>
<p> <code>Tk_Get3DBorderFromObj</code> returns the token for an existing border, given the window and color name used to create the border. <code>Tk_Get3DBorderFromObj</code> does not actually create the border; it must already have been created with a previous call to <code>Tk_Alloc3DBorderFromObj</code> or <code>Tk_Get3DBorder</code>. The return value is cached in <i>objPtr</i>, which speeds up future calls to <code>Tk_Get3DBorderFromObj</code> with the same <i>objPtr</i> and <i>tkwin</i>. </p>
<p> Once a border structure has been created, <code>Tk_Draw3DRectangle</code> may be invoked to draw the border. The <i>tkwin</i> argument specifies the window for which the border was allocated, and <i>drawable</i> specifies a window or pixmap in which the border is to be drawn. <i>Drawable</i> need not refer to the same window as <i>tkwin</i>, but it must refer to a compatible pixmap or window: one associated with the same screen and with the same depth as <i>tkwin</i>. The <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i> arguments define the bounding box of the border region within <i>drawable</i> (usually <i>x</i> and <i>y</i> are zero and <i>width</i> and <i>height</i> are the dimensions of the window), and <i>borderWidth</i> specifies the number of pixels actually occupied by the border. The <i>relief</i> argument indicates which of several three-dimensional effects is desired: <code>TK_RELIEF_RAISED</code> means that the interior of the rectangle should appear raised relative to the exterior of the rectangle, and <code>TK_RELIEF_SUNKEN</code> means that the interior should appear depressed. <code>TK_RELIEF_GROOVE</code> and <code>TK_RELIEF_RIDGE</code> mean that there should appear to be a groove or ridge around the exterior of the rectangle. </p>
<p> <code>Tk_Fill3DRectangle</code> is somewhat like <code>Tk_Draw3DRectangle</code> except that it first fills the rectangular area with the background color (one corresponding to the color used to create <i>border</i>). Then it calls <code>Tk_Draw3DRectangle</code> to draw a border just inside the outer edge of the rectangular area. The argument <i>relief</i> indicates the desired effect (<code>TK_RELIEF_FLAT</code> means no border should be drawn; all that happens is to fill the rectangle with the background color). </p>
<p> The procedure <code>Tk_Draw3DPolygon</code> may be used to draw more complex shapes with a three-dimensional appearance. The <i>pointPtr</i> and <i>numPoints</i> arguments define a trajectory, <i>polyBorderWidth</i> indicates how wide the border should be (and on which side of the trajectory to draw it), and <i>leftRelief</i> indicates which side of the trajectory should appear raised. <code>Tk_Draw3DPolygon</code> draws a border around the given trajectory using the colors from <i>border</i> to produce a three-dimensional appearance. If the trajectory is non-self-intersecting, the appearance will be a raised or sunken polygon shape. The trajectory may be self-intersecting, although it&#8217;s not clear how useful this is. </p>
<p> <code>Tk_Fill3DPolygon</code> is to <code>Tk_Draw3DPolygon</code> what <code>Tk_Fill3DRectangle</code> is to <code>Tk_Draw3DRectangle</code>: it fills the polygonal area with the background color from <i>border</i>, then calls <code>Tk_Draw3DPolygon</code> to draw a border around the area (unless <i>leftRelief</i> is <code>TK_RELIEF_FLAT</code>; in this case no border is drawn). </p>
<p> The procedures <code>Tk_3DVerticalBevel</code> and <code>Tk_3DHorizontalBevel</code> provide lower-level drawing primitives that are used by procedures such as <code>Tk_Draw3DRectangle</code>. These procedures are also useful in their own right for drawing rectilinear border shapes. <code>Tk_3DVerticalBevel</code> draws a vertical beveled edge, such as the left or right side of a rectangle, and <code>Tk_3DHorizontalBevel</code> draws a horizontal beveled edge, such as the top or bottom of a rectangle. Each procedure takes <i>x</i>, <i>y</i>, <i>width</i>, and <i>height</i> arguments that describe the rectangular area of the beveled edge (e.g., <i>width</i> is the border width for <code>Tk_3DVerticalBevel</code>). The <i>leftBorder</i> and <i>topBorder</i> arguments indicate the position of the border relative to the &#8220;inside&#8221; of the object, and <i>relief</i> indicates the relief of the inside of the object relative to the outside. <code>Tk_3DVerticalBevel</code> just draws a rectangular region. <code>Tk_3DHorizontalBevel</code> draws a trapezoidal region to generate mitered corners; it should be called after <code>Tk_3DVerticalBevel</code> (otherwise <code>Tk_3DVerticalBevel</code> will overwrite the mitering in the corner). The <i>leftIn</i> and <i>rightIn</i> arguments to <code>Tk_3DHorizontalBevel</code> describe the mitering at the corners; a value of 1 means that the bottom edge of the trapezoid will be shorter than the top, 0 means it will be longer. For example, to draw a rectangular border the top bevel should be drawn with 1 for both <i>leftIn</i> and <i>rightIn</i>, and the bottom bevel should be drawn with 0 for both arguments. </p>
<p> The procedure <code>Tk_SetBackgroundFromBorder</code> will modify the background pixel and/or pixmap of <i>tkwin</i> to produce a result compatible with <i>border</i>. For color displays, the resulting background will just be the color specified when <i>border</i> was created; for monochrome displays, the resulting background will be a light stipple pattern, in order to distinguish the background from the illuminated portion of the border. </p>
<p> Given a token for a border, the procedure <code>Tk_NameOf3DBorder</code> will return the color name that was used to create the border. </p>
<p> The procedure <code>Tk_3DBorderColor</code> returns the XColor structure that will be used for flat surfaces drawn for its <i>border</i> argument by procedures like <code>Tk_Fill3DRectangle</code>. The return value corresponds to the color name that was used to create the border. The XColor, and its associated pixel value, will remain allocated as long as <i>border</i> exists. </p>
<p> The procedure <code>Tk_3DBorderGC</code> returns one of the X graphics contexts that are used to draw the border. The argument <i>which</i> selects which one of the three possible GC&#8217;s: <code>TK_3D_FLAT_GC</code> returns the context used for flat surfaces, <code>TK_3D_LIGHT_GC</code> returns the context for light shadows, and <code>TK_3D_DARK_GC</code> returns the context for dark shadows. </p>
<p> When a border is no longer needed, <code>Tk_Free3DBorderFromObj</code> or <code>Tk_Free3DBorder</code> should be called to release the resources associated with it. For <code>Tk_Free3DBorderFromObj</code> the border to release is specified with the window and color name used to create the border; for <code>Tk_Free3DBorder</code> the border to release is specified with the Tk_3DBorder token for the border. There should be exactly one call to <code>Tk_Free3DBorderFromObj</code> or <code>Tk_Free3DBorder</code> for each call to <code>Tk_Alloc3DBorderFromObj</code> or <code>Tk_Get3DBorder</code>. </p>
<h2>Keywords</h2>
<p>3D, background, border, color, depressed, illumination, object, polygon, raised, shadow, three-dimensional effect</p>
