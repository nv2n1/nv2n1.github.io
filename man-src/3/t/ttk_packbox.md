---
title: "ttk_packbox(3)"
name: "ttk_packbox"
section: "3"
letter: "t"
url: "/docs/linux/man/3-ttk_packbox/"
description: "Ttk_MakeBox, Ttk_PadBox, Ttk_ExpandBox, Ttk_PackBox, Ttk_StickBox, Ttk_PlaceBox, Ttk_BoxContains, Ttk_MakePadding, Ttk_UniformPadding, Ttk_AddPadding, Ttk_RelievePadding, Ttk_GetPaddingFromObj, Ttk..."
---

<p>Ttk_MakeBox, Ttk_PadBox, Ttk_ExpandBox, Ttk_PackBox, Ttk_StickBox, Ttk_PlaceBox, Ttk_BoxContains, Ttk_MakePadding, Ttk_UniformPadding, Ttk_AddPadding, Ttk_RelievePadding, Ttk_GetPaddingFromObj, Ttk_GetBorderFromObj, Ttk_GetStickyFromObj &#8211; Tk themed geometry utilities </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tkTheme.h&gt;</code>
Ttk_Box
<code>Ttk_MakeBox</code>(int <i>x</i>, int <i>y</i>, int <i>width</i>, int <i>height</i>);
Ttk_Box
<code>Ttk_PadBox</code>(Ttk_Box <i>parcel</i>, Ttk_Padding <i>padding</i>);
Ttk_Box
<code>Ttk_ExpandBox</code>(Ttk_Box <i>parcel</i>, Ttk_Padding <i>padding</i>);
Ttk_Box
<code>Ttk_PackBox</code>(Ttk_Box *<i>cavity</i>, int <i>width</i>, int <i>height</i>, Ttk_Side <i>side</i>);
Ttk_Box
<code>Ttk_StickBox</code>(Ttk_Box <i>parcel</i>, int <i>width</i>, int <i>height</i>, unsigned <i>sticky</i>);
Ttk_Box
<code>Ttk_PlaceBox</code>(Ttk_Box *<i>cavity</i>, int <i>width</i>, int <i>height</i>, Ttk_Side <i>side</i>, unsigned <i>sticky</i>);
Ttk_Box
<code>Ttk_AnchorBox</code>(Ttk_Box <i>parcel</i>, int <i>width</i>, int <i>height</i>, Tk_Anchor <i>anchor</i>);
Ttk_Padding
<code>Ttk_MakePadding</code>(short <i>left</i>, short <i>top</i>, short <i>right</i>, short <i>bottom</i>);
Ttk_Padding
<code>Ttk_UniformPadding</code>(short <i>border</i>);
Ttk_Padding
<code>Ttk_AddPadding</code>(Ttk_Padding <i>padding1</i>, Ttk_Padding <i>padding2</i>;
Ttk_Padding
<code>Ttk_RelievePadding</code>(Ttk_Padding <i>padding</i>, int <i>relief</i>);
int
<code>Ttk_BoxContains</code>(Ttk_Box <i>box</i>, int <i>x</i>, int <i>y</i>);
int
<code>Ttk_GetPaddingFromObj</code>(Tcl_Interp *<i>interp</i>, Tk_Window <i>tkwin</i>, Tcl_Obj *<i>objPtr</i>, Ttk_Padding *<i>padding_rtn</i>);
int
<code>Ttk_GetBorderFromObj</code>(Tcl_Interp *<i>interp</i>, Tcl_Obj *<i>objPtr</i>, Ttk_Padding *<i>padding_rtn</i>);
int
<code>Ttk_GetStickyFromObj</code>(Tcl_Interp *<i>interp</i>, Tcl_Obj *<i>objPtr</i>, int *<i>sticky_rtn</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Anchor <i>anchor</i> (in) One of the symbolic constants <code>TK_ANCHOR_N</code>, <code>TK_ANCHOR_NE</code>, etc. See <i><a href="/docs/linux/man/3-tk_getanchorfromobj/">Tk_GetAnchorFromObj</a>(3)</i>.</p>
<dd>Ttk_Box * <i>cavity</i> (in/out) A rectangular region from which a parcel is allocated.</p>
<dd>short <i>border</i> (in) Extra padding (in pixels) to add uniformly to each side of a region.</p>
<dd>short <i>bottom</i> (in) Extra padding (in pixels) to add to the bottom of a region.</p>
<dd>Ttk_Box <i>box</i> (in)</p>
<dd>Ttk_Box * <i>box_rtn</i> (out) Specifies a rectangular region.</p>
<dd>int <i>height</i> (in) The height in pixels of a region.</p>
<dd>Tcl_Interp * <i>interp</i> (in) Used to store error messages.</p>
<dd>int <i>left</i> (in) Extra padding (in pixels) to add to the left side of a region.</p>
<dd>Tcl_Obj * <i>objPtr</i> (in) String value contains a symbolic name to be converted to an enumerated value or bitmask. Internal rep may be be modified to cache corresponding value.</p>
<dd>Ttk_Padding <i>padding</i> (in)</p>
<dd>Ttk_Padding * <i>padding_rtn</i> (out) Extra padding to add on the inside of a region.</p>
<dd>Ttk_Box <i>parcel</i> (in) A rectangular region, allocated from a cavity.</p>
<dd>int <i>relief</i> (in) One of the standard Tk relief options (TK_RELIEF_RAISED, TK_RELIEF_SUNKEN, etc.). See <code>Tk_GetReliefFromObj</code>.</p>
<dd>short <i>right</i> (in) Extra padding (in pixles) to add to the right side of a region.</p>
<dd>Ttk_Side <i>side</i> (in) One of <code>TTK_SIDE_LEFT</code>, <code>TTK_SIDE_TOP</code>, <code>TTK_SIDE_RIGHT</code>, or <code>TTK_SIDE_BOTTOM</code>.</p>
<dd>unsigned <i>sticky</i> (in) A bitmask containing one or more of the bits <code>TTK_STICK_W</code> (west, or left), <code>TTK_STICK_E</code> (east, or right, <code>TTK_STICK_N</code> (north, or top), and <code>TTK_STICK_S</code> (south, or bottom). <code>TTK_FILL_X</code> is defined as a synonym for (TTK_STICK_W|TTK_STICK_E), <code>TTK_FILL_Y</code> is a synonym for (TTK_STICK_N|TTK_STICK_S), and <code>TTK_FILL_BOTH</code> and <code>TTK_STICK_ALL</code> are synonyms for (TTK_FILL_X|TTK_FILL_Y). See also: <i><a href="/docs/linux/man/n-grid/">grid</a>(n)</i>.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window whose screen geometry determines the conversion between absolute units and pixels.</p>
<dd>short <i>top</i> (in) Extra padding at the top of a region.</p>
<dd>int <i>width</i> (in) The width in pixels of a region.</p>
<dd>int <i>x</i> (in) X coordinate of upper-left corner of region.</p>
<dd>int <i>y</i> (in) Y coordinate of upper-left corner of region.
</dl>
<h2>Boxes</h2>
<p>The <code>Ttk_Box</code> structure represents a rectangular region of a window:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 int <i>x</i>;
 int <i>y</i>;
 int <i>width</i>;
 int <i>height</i>;
} <code>Ttk_Box</code>;</pre>
</dl>
<p> All coordinates are relative to the window. </p>
<p> <code>Ttk_MakeBox</code> is a convenience routine that contsructs a <code>Ttk_Box</code> structure representing a region <i>width</i> pixels wide, <i>height</i> pixels tall, at the specified <i>x, y</i> coordinates. </p>
<p> <code>Ttk_PadBox</code> returns a new box located inside the specified <i>parcel</i>, shrunken according to the left, top, right, and bottom margins specified by <i>padding</i>. </p>
<p> <code>Ttk_ExpandBox</code> is the inverse of <code>Ttk_PadBox</code>: it returns a new box surrounding the specified <i>parcel</i>, expanded according to the left, top, right, and bottom margins specified by <i>padding</i>. </p>
<p> <code>Ttk_PackBox</code> allocates a parcel <i>width</i> by <i>height</i> pixels wide on the specified <i>side</i> of the <i>cavity</i>, and shrinks the <i>cavity</i> accordingly. </p>
<p> <code>Ttk_StickBox</code> places a box with the requested <i>width</i> and <i>height</i> inside the <i>parcel</i> according to the <i>sticky</i> bits. </p>
<p> <code>Ttk_PlaceBox</code> combines <code>Ttk_PackBox</code> and <code>Ttk_StickBox</code>: it allocates a parcel on the specified <i>side</i> of the <i>cavity</i>, places a box of the requested size inside the parcel according to <i>sticky</i>, and shrinks the <i>cavity</i>. </p>
<p> <code>Ttk_AnchorBox</code> places a box with the requested <i>width</i> and <i>height</i> inside the <i>parcel</i> according to the specified <i>anchor</i> option. </p>
<p> <code>Ttk_BoxContains</code> tests if the specified <i>x, y</i> coordinate lies within the rectangular region <i>box</i>.</p>
<h2>Paddding</h2>
<p>The <code>Ttk_Padding</code> structure is used to represent borders, internal padding, and external margins:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 short <i>left</i>;
 short <i>top</i>;
 short <i>right</i>;
 short <i>bottom</i>;
} <code>Ttk_Padding</code>;</pre>
</dl>
<p> <code>Ttk_MakePadding</code> is a convenience routine that contsructs a <code>Ttk_Padding</code> structure with the specified left, top, right, and bottom components. </p>
<p> <code>Ttk_UniformPadding</code> constructs a <code>Ttk_Padding</code> structure with all components equal to the specified <i>border</i>. </p>
<p> <code>Ttk_AddPadding</code> adds two <code>Ttk_Padding</code>s together and returns a combined padding containing the sum of the individual padding components. </p>
<p> <code>Ttk_RelievePadding</code> adds an extra 2 pixels of padding to <i>padding</i> according to the specified <i>relief</i>. If <i>relief</i> is <code>TK_RELIEF_SUNKEN</code>, adds two pixels at the top and left so the inner region is shifted down and to the left. If it is <code>TK_RELIEF_RAISED</code>, adds two pixels at the bottom and right so the inner region is shifted up and to the right. Otherwise, adds 1 pixel on all sides. This is typically used in element geometry procedures to simulate a &#8220;pressed-in&#8221; look for pushbuttons.</p>
<h2>Conversion Routines</h2>
<p><code>Ttk_GetPaddingFromObj</code> converts the string in <i>objPtr</i> to a <code>Ttk_Padding</code> structure. The string representation is a list of up to four length specifications &#8220;<i>left top right bottom</i>&#8221;. If fewer than four elements are specified, <i>bottom</i> defaults to <i>top</i>, <i>right</i> defaults to <i>left</i>, and <i>top</i> defaults to <i>left</i>. See <code><a href="/docs/linux/man/3-tk_getpixelsfromobj/">Tk_GetPixelsFromObj</a>(3)</code> for the syntax of length specifications. </p>
<p> <code>Ttk_GetBorderFromObj</code> is the same as <code>Ttk_GetPaddingFromObj</code> except that the lengths are specified as integers (i.e., resolution-dependant values like <i>3m</i> are not allowed). </p>
<p> <code>Ttk_GetStickyFromObj</code> converts the string in <i>objPtr</i> to a <i>sticky</i> bitmask. The string contains zero or more of the characters <code>n</code>, <code>s</code>, <code>e</code>, or <code>w</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tk_getrelieffromobj/">Tk_GetReliefFromObj</a>(3), <a href="/docs/linux/man/3-tk_getpixelsfromobj/">Tk_GetPixelsFromObj</a>(3), <a href="/docs/linux/man/3-tk_getanchorfromobj/">Tk_GetAnchorFromObj</a>(3)</p>
<h2>Keywords</h2>
<p>geometry, padding, margins, box, region, sticky, relief</p>
