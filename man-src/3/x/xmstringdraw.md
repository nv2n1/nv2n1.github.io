---
title: "xmstringdraw(3)"
name: "xmstringdraw"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringdraw/"
description: "XmStringDraw — A compound string function that draws a compound string in an X window"
---

<p><code>XmStringDraw</code> &#8212; A compound string function that draws a compound string in an X window</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmStringDraw</code>(
<code>Display * d</code>,
<code>Window w</code>,
<code>XmRenderTable rendertable</code>,
<code>XmString string</code>,
<code>GC gc</code>,
<code>Position x</code>,
<code>Position y</code>,
<code>Dimension width</code>,
<code>unsigned char alignment</code>,
<code>unsigned char layout_direction</code>,
<code>XRectangle * clip</code>);</pre>
<h2>Description</h2>
<p><code>XmStringDraw</code> draws a compound string in an X Window. If a compound string segment uses a rendition that contains a font set, the graphic context passed to this routine will have the GC font member left in an undefined state. The underlying <code>XmbStringDraw</code> function called by this routine modifies the font ID field of the GC passed into it and does not attempt to restore the font ID to the incoming value. If the compound string segment is not drawn using a font set, the graphic context must contain a valid font member. Graphic contexts created by <code>XtGetGC</code> are not valid for this routine; instead, use <code>XtAllocateGC</code> to create a graphic context.</p>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the display.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</p>
<dt><i>rendertable</i></p>
<dd>Specifies the render table.</p>
<dt><i>string</i></p>
<dd>Specifies the string.</p>
<dt><i>gc</i></p>
<dd>Specifies the graphics context to use.</p>
<dt><i>x</i></p>
<dd>Specifies a coordinate of the rectangle that will contain the displayed compound string.</p>
<dt><i>y</i></p>
<dd>Specifies a coordinate of the rectangle that will contain the displayed compound string.</p>
<dt><i>width</i></p>
<dd>Specifies the width of the rectangle that will contain the displayed compound string.</p>
<dt><i>alignment</i></p>
<dd>Specifies how the string will be aligned within the specified rectangle. It is either <code>XmALIGNMENT_BEGINNING</code>, <code>XmALIGNMENT_CENTER</code>, or <code>XmALIGNMENT_END</code>.</p>
<dt><i>layout_direction</i></p>
<dd>Controls the direction in which the segments of the compound string will be laid out. It also determines the meaning of the <i>alignment</i> parameter.</p>
<dt><i>clip</i></p>
<dd>Allows the application to restrict the area into which the compound string will be drawn. If the value is NULL, clipping will be determined by the GC.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
