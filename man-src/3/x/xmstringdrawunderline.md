---
title: "xmstringdrawunderline(3)"
name: "xmstringdrawunderline"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmstringdrawunderline/"
description: "XmStringDrawUnderline — A compound string function that underlines a string drawn in an X Window"
---

<p><code>XmStringDrawUnderline</code> &#8212; A compound string function that underlines a string drawn in an X Window</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmStringDrawUnderline</code>(
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
<code>XRectangle * clip</code>,
<code>XmString underline</code>);</pre>
<h2>Description</h2>
<p><code>XmStringDrawUnderline</code> draws a compound string in an X Window. If the substring identified by <i>underline</i> can be matched in <i>string</i>, the substring will be underlined. Once a match has occurred, no further matches or underlining will be done. Only the first text component of <i>underline</i> is used for matching. </p>
<p> If a compound string segment uses a rendition that contains a font set, the graphic context passed to this routine will have the GC font member left in an undefined state. The underlying <code>XmbStringDraw</code> function called by this routine modifies the font ID field of the GC passed into it and does not attempt to restore the font ID to the incoming value. If the compound string segment is not drawn using a font set, the graphic context must contain a valid font member. Graphic contexts created by <code>XtGetGC</code> are not accepted by this routine; instead, use <code>XtAllocateGC</code> to create a graphic context.</p>
<dl COMPACT>
<dt><i>d</i></dt>
<dd>Specifies the display.</dd>
<dt><i>w</i></dt>
<dd>Specifies the window.</dd>
<dt><i>rendertable</i></dt>
<dd>Specifies the render table.</dd>
<dt><i>string</i></dt>
<dd>Specifies the string.</dd>
<dt><i>gc</i></dt>
<dd>Specifies the graphics context to use.</dd>
<dt><i>x</i></dt>
<dd>Specifies a coordinate of the rectangle that will contain the displayed compound string.</dd>
<dt><i>y</i></dt>
<dd>Specifies a coordinate of the rectangle that will contain the displayed compound string.</dd>
<dt><i>width</i></dt>
<dd>Specifies the width of the rectangle that will contain the displayed compound string.</dd>
<dt><i>alignment</i></dt>
<dd>Specifies how the string will be aligned within the specified rectangle. It is one of <code>XmALIGNMENT_BEGINNING</code>, <code>XmALIGNMENT_CENTER</code>, or <code>XmALIGNMENT_END</code>.</dd>
<dt><i>layout_direction</i></dt>
<dd>Controls the direction in which the segments of the compound string will be laid out. It also determines the meaning of the <i>alignment</i> parameter.</dd>
<dt><i>clip</i></dt>
<dd>Allows the application to restrict the area into which the compound string will be drawn. If it is NULL, clipping will be determined by the GC.</dd>
<dt><i>underline</i></dt>
<dd>Specifies the substring to be underlined.</dd></dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmstringcreate/">XmStringCreate</a></code>(3).</p>
