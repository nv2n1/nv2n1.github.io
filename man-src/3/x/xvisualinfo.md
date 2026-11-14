---
title: "xvisualinfo(3)"
name: "xvisualinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvisualinfo/"
description: "XGetVisualInfo, XMatchVisualInfo, XVisualIDFromVisual, XVisualInfo – obtain visual information and visual structure"
---

<p>XGetVisualInfo, XMatchVisualInfo, XVisualIDFromVisual, XVisualInfo &#8211; obtain visual information and visual structure </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XVisualInfo *XGetVisualInfo(Display *<i>display</i>, long <i>vinfo_mask</i>, XVisualInfo *<i>vinfo_template</i>, int *<i>nitems_return</i>);</p>
<dd>Status XMatchVisualInfo(Display *<i>display</i>, int <i>screen</i>, int <i>depth</i>, int <i>class</i>, XVisualInfo *<i>vinfo_return</i>);</p>
<dd>VisualID XVisualIDFromVisual(Visual *<i>visual</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>class</i></p>
<dd>Specifies the class of the screen.</p>
<dt><i>depth</i></p>
<dd>Specifies the depth of the screen.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>nitems_return</i></p>
<dd>Returns the number of matching visual structures.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen.</p>
<dt><i>visual</i></p>
<dd>Specifies the visual type.</p>
<dt><i>vinfo_mask</i></p>
<dd>Specifies the visual mask value.</p>
<dt><i>vinfo_return</i></p>
<dd>Returns the matched visual information.</p>
<dt><i>vinfo_template</i></p>
<dd>Specifies the visual attributes that are to be used in matching the visual structures.</dl>
<h2>Description</h2>
<p>The <code>XGetVisualInfo</code> function returns a list of visual structures that have attributes equal to the attributes specified by vinfo_template. If no visual structures match the template using the specified vinfo_mask, <code>XGetVisualInfo</code> returns a NULL. To free the data returned by this function, use <code>XFree</code>. </p>
<p> The <code>XMatchVisualInfo</code> function returns the visual information for a visual that matches the specified depth and class for a screen. Because multiple visuals that match the specified depth and class can exist, the exact visual chosen is undefined. If a visual is found, <code>XMatchVisualInfo</code> returns nonzero and the information on the visual to vinfo_return. Otherwise, when a visual is not found, <code>XMatchVisualInfo</code> returns zero. </p>
<p> The <code>XVisualIDFromVisual</code> function returns the visual ID for the specified visual type.</p>
<h2>Structures</h2>
<p>The <code>XVisualInfo</code> structure contains: </p>
<p> /* Visual information mask bits */ </p>
<table>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualNoMask</code> </td>
<td> 0x0
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualIDMask</code> </td>
<td> 0x1
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualScreenMask</code> </td>
<td> 0x2
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualDepthMask</code> </td>
<td> 0x4
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualClassMask</code> </td>
<td> 0x8
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualRedMaskMask</code> </td>
<td> 0x10
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualGreenMaskMask</code> </td>
<td> 0x20
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualBlueMaskMask</code> </td>
<td> 0x40
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualColormapSizeMask</code> </td>
<td> 0x80
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualBitsPerRGBMask</code> </td>
<td> 0x100
</td>
</tr>
<tr VALIGN=top>
<td> #define </td>
<td> <code>VisualAllMask</code> </td>
<td> 0x1FF
</td>
</tr>
</table>
<p> /* Values */ </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Visual&nbsp;*visual;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;VisualID visualid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int screen;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int depth;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int class;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long red_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long green_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long blue_mask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int colormap_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bits_per_rgb; } XVisualInfo;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xfree/">XFree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
