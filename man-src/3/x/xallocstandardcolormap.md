---
title: "xallocstandardcolormap(3)"
name: "xallocstandardcolormap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xallocstandardcolormap/"
description: "XAllocStandardColormap, XSetRGBColormaps, XGetRGBColormaps, XStandardColormap – allocate, set, or read a standard colormap structure"
---

<p>XAllocStandardColormap, XSetRGBColormaps, XGetRGBColormaps, XStandardColormap &#8211; allocate, set, or read a standard colormap structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XStandardColormap *XAllocStandardColormap(void);</p>
<dd>void XSetRGBColormaps(Display *<i>display</i>, Window <i>w</i>, XStandardColormap *<i>std_colormap</i>, int <i>count</i>, Atom <i>property</i>);</p>
<dd>Status XGetRGBColormaps(Display *<i>display</i>, Window <i>w</i>, XStandardColormap **<i>std_colormap_return</i>, int *<i>count_return</i>, Atom <i>property</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>count</i></p>
<dd>Specifies the number of colormaps.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of colormaps.</p>
<dt><i>property</i></p>
<dd>Specifies the property name.</p>
<dt><i>std_colormap</i></p>
<dd>Specifies the <code>XStandardColormap</code> structure to be used.</p>
<dt><i>std_colormap_return</i></p>
<dd>Returns the <code>XStandardColormap</code> structure.</dl>
<h2>Description</h2>
<p>The <code>XAllocStandardColormap</code> function allocates and returns a pointer to a <code>XStandardColormap</code> structure. Note that all fields in the <code>XStandardColormap</code> structure are initially set to zero. If insufficient memory is available, <code>XAllocStandardColormap</code> returns NULL. To free the memory allocated to this structure, use <code>XFree</code>. </p>
<p> The <code>XSetRGBColormaps</code> function replaces the RGB colormap definition in the specified property on the named window. If the property does not already exist, <code>XSetRGBColormaps</code> sets the RGB colormap definition in the specified property on the named window. The property is stored with a type of RGB_COLOR_MAP and a format of 32. Note that it is the caller&#8217;s responsibility to honor the ICCCM restriction that only RGB_DEFAULT_MAP contain more than one definition. </p>
<p> The <code>XSetRGBColormaps</code> function usually is only used by window or session managers. To create a standard colormap, follow this procedure:</p>
<dl COMPACT>
<dt>1.</p>
<dd>Open a new connection to the same server.</p>
<dt>2.</p>
<dd>Grab the server.</p>
<dt>3.</p>
<dd>See if the property is on the property list of the root window for the screen.</p>
<dt>4.</p>
<dd>If the desired property is not present:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd>Create a colormap (unless you are using the default colormap of the screen).</p>
<dt>&bull;</p>
<dd>Determine the color characteristics of the visual.</p>
<dt>&bull;</p>
<dd>Allocate cells in the colormap (or create it with <code>AllocAll</code>).</p>
<dt>&bull;</p>
<dd>Call <code>XStoreColors</code> to store appropriate color values in the colormap.</p>
<dt>&bull;</p>
<dd>Fill in the descriptive members in the <code>XStandardColormap</code> structure.</p>
<dt>&bull;</p>
<dd>Attach the property to the root window.</p>
<dt>&bull;</p>
<dd>Use <code>XSetCloseDownMode</code> to make the resource permanent.</dl>
</dl>
<dt>5.</p>
<dd>Ungrab the server.</dl>
<p> <code>XSetRGBColormaps</code> can generate <code>BadAlloc</code>, <code>BadAtom</code>, and <code>BadWindow</code> errors. </p>
<p> The <code>XGetRGBColormaps</code> function returns the RGB colormap definitions stored in the specified property on the named window. If the property exists, is of type RGB_COLOR_MAP, is of format 32, and is long enough to contain a colormap definition, <code>XGetRGBColormaps</code> allocates and fills in space for the returned colormaps and returns a nonzero status. If the visualid is not present, <code>XGetRGBColormaps</code> assumes the default visual for the screen on which the window is located; if the killid is not present, <code>None</code> is assumed, which indicates that the resources cannot be released. Otherwise, none of the fields are set, and <code>XGetRGBColormaps</code> returns a zero status. Note that it is the caller&#8217;s responsibility to honor the ICCCM restriction that only RGB_DEFAULT_MAP contain more than one definition. </p>
<p> <code>XGetRGBColormaps</code> can generate <code>BadAtom</code> and <code>BadWindow</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XStandardColormap</code> structure contains: </p>
<p> /* Hints */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>ReleaseByFreeingColormap</code> </td>
<td> ( (XID) 1L)
</td>
</tr>
</table>
<p> /* Values */ typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Colormap colormap;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long red_max;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long red_mult;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long green_max;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long green_mult;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long blue_max;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long blue_mult;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long base_pixel;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VisualID visualid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XID killid; } XStandardColormap; </p>
<p> The colormap member is the colormap created by the <code>XCreateColormap</code> function. The red_max, green_max, and blue_max members give the maximum red, green, and blue values, respectively. Each color coefficient ranges from zero to its max, inclusive. For example, a common colormap allocation is 3/3/2 (3 planes for red, 3 planes for green, and 2 planes for blue). This colormap would have red_max = 7, green_max = 7, and blue_max = 3. An alternate allocation that uses only 216 colors is red_max = 5, green_max = 5, and blue_max = 5. </p>
<p> The red_mult, green_mult, and blue_mult members give the scale factors used to compose a full pixel value. (See the discussion of the base_pixel members for further information.) For a 3/3/2 allocation, red_mult might be 32, green_mult might be 4, and blue_mult might be 1. For a 6-colors-each allocation, red_mult might be 36, green_mult might be 6, and blue_mult might be 1. </p>
<p> The base_pixel member gives the base pixel value used to compose a full pixel value. Usually, the base_pixel is obtained from a call to the <code>XAllocColorPlanes</code> function. Given integer red, green, and blue coefficients in their appropriate ranges, one then can compute a corresponding pixel value by using the following expression: </p>
<p> (r * red_mult + g * green_mult + b * blue_mult + base_pixel) &amp; 0xFFFFFFFF </p>
<p> For <code>GrayScale</code> colormaps, only the colormap, red_max, red_mult, and base_pixel members are defined. The other members are ignored. To compute a <code>GrayScale</code> pixel value, use the following expression: </p>
<p> (gray * red_mult + base_pixel) &amp; 0xFFFFFFFF </p>
<p> Negative multipliers can be represented by converting the 2&#8217;s complement representation of the multiplier into an unsigned long and storing the result in the appropriate _mult field. The step of masking by 0xFFFFFFFF effectively converts the resulting positive multiplier into a negative one. The masking step will take place automatically on many machine architectures, depending on the size of the integer type used to do the computation, </p>
<p> The visualid member gives the ID number of the visual from which the colormap was created. The killid member gives a resource ID that indicates whether the cells held by this standard colormap are to be released by freeing the colormap ID or by calling the <code>XKillClient</code> function on the indicated resource. (Note that this method is necessary for allocating out of an existing colormap.) </p>
<p> The properties containing the <code>XStandardColormap</code> information have the type RGB_COLOR_MAP.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadAtom</code></p>
<dd>A value for an Atom argument does not name a defined Atom.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xalloccolor/">XAllocColor</a>(3), <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3), <a href="/docs/linux/man/3-xsetclosedownmode/">XSetCloseDownMode</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
