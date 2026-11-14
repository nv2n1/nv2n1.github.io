---
title: "xmdirection(3)"
name: "xmdirection"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdirection/"
description: "XmDirection — Data type for the direction of widget components"
---

<p><code>XmDirection</code> &#8212; Data type for the direction of widget components</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmDirection</code> is the data type specifying the direction in which the system displays subwidgets, children of widgets, or other visual components that are to be laid out. This data type also affects traversal order within tab groups. </p>
<p> <code>XmDirection</code> is implemented as an unsigned char bit mask. The horizontal and vertical directions can be specified independent of each other. <code>XmDirection</code> also specifies the precedence of the horizontal and vertical directions relative to each other. For example, a value of <code>XmRIGHT_TO_LEFT_TOP_TO_BOTTOM</code> lays out a component horizontally from right to left first, then vertically top to bottom. </p>
<p> <code>XmDirection</code> provides the following masks, each of which corresponds to a particular bit in <code>XmDirection</code>:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmRIGHT_TO_LEFT_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmLEFT_TO_RIGHT_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmTOP_TO_BOTTOM_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmBOTTOM_TO_TOP_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmPRECEDENCE_HORIZ_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmPRECEDENCE_VERT_MASK</code></dl>
<p> In addition to the preceding single bit masks, <code>XmDirection</code> also provides the following multiple bit masks. These multiple bit masks are particularly useful as arguments to <code>XmDirectionMatchPartial</code>:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmHORIZONTAL_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmPRECEDENCE_MASK</code></p>
<dt> &bull;</p>
<dd><code>XmVERTICAL_MASK</code></dl>
<p> Motif also provides the following enumerated constants for specifying various combinations of directions:</p>
<dl COMPACT>
<dt><code>XmRIGHT_TO_LEFT_TOP_TO_BOTTOM</code></p>
<dd>Specifies that the components are laid out from right to left first, then top to bottom.</p>
<dt><code>XmLEFT_TO_RIGHT_TOP_TO_BOTTOM</code></p>
<dd>Specifies that the components are laid out from left to right first, then top to bottom.</p>
<dt><code>XmRIGHT_TO_LEFT_BOTTOM_TO_TOP</code></p>
<dd>Specifies that the components are laid out from right to left first, then bottom to top.</p>
<dt><code>XmLEFT_TO_RIGHT_BOTTOM_TO_TOP</code></p>
<dd>Specifies that the components are laid out from left to right first, then bottom to top.</p>
<dt><code>XmTOP_TO_BOTTOM_RIGHT_TO_LEFT</code></p>
<dd>Specifies that the components are laid out from top to bottom first, then right to left.</p>
<dt><code>XmTOP_TO_BOTTOM_LEFT_TO_RIGHT</code></p>
<dd>Specifies that the components are laid out from top to bottom first, then left to right.</p>
<dt><code>XmBOTTOM_TO_TOP_RIGHT_TO_LEFT</code></p>
<dd>Specifies that the components are laid out from bottom to top first, then right to left.</p>
<dt><code>XmBOTTOM_TO_TOP_LEFT_TO_RIGHT</code></p>
<dd>Specifies that the components are laid out from bottom to top first, then left to right.</p>
<dt><code>XmTOP_TO_BOTTOM</code></p>
<dd>Specifies that the components are laid out from top to bottom. If horizontal direction is important, do not use this constant.</p>
<dt><code>XmBOTTOM_TO_TOP</code></p>
<dd>Specifies that the components are laid out from bottom to top. If horizontal direction is important, do not use this constant.</p>
<dt><code>XmDEFAULT_DIRECTION</code></p>
<dd>Specifies that the components are laid out according to the default direction. (This constant is primarily for widget writers.)</p>
<dt><code>XmLEFT_TO_RIGHT</code></p>
<dd>Specifies that the components are laid out from left to right. If vertical direction is important, do not use this constant.</p>
<dt><code>XmRIGHT_TO_LEFT</code></p>
<dd>Specifies that the components are laid out from right to left. If vertical direction is important, do not use this constant.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdirectionmatch/">XmDirectionMatch</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectionmatchpartial/">XmDirectionMatchPartial</a></code>(3), <code><a href="/docs/linux/man/3-xmdirectiontostringdirection/">XmDirectionToStringDirection</a></code>(3), <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3), <code><a href="/docs/linux/man/3-xmstringdirection/">XmStringDirection</a></code>(3), and <code><a href="/docs/linux/man/3-xmstringdirectiontodirection/">XmStringDirectionToDirection</a></code>(3).</p>
