---
title: "qwtcolumnrect(3)"
name: "qwtcolumnrect"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcolumnrect/"
description: "QwtColumnRect –"
---

<p>QwtColumnRect &#8211; </p>
<p> Directed rectangle representing bounding rectangle and orientation of a column.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_column_symbol.h&gt;</p>
<h3>Public Types</h3>
<p>enum <code>Direction</code> { <code>LeftToRight</code>, <code>RightToLeft</code>, <code>BottomToTop</code>, <code>TopToBottom</code> }<br />
 <i>Direction of the column. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtColumnRect</code> ()<br />
 <i>Build an rectangle with invalid intervals directed BottomToTop. </i><br />
 QRectF <code>toRect</code> () const </p>
<p> Qt::Orientation <code>orientation</code> () const </p>
<h3>Public Attributes</h3>
<p><code>QwtInterval</code> <code>hInterval</code><br />
 <i>Interval for the horizontal coordinates. </i><br />
 <code>QwtInterval</code> <code>vInterval</code><br />
 <i>Interval for the vertical coordinates. </i><br />
 <code>Direction</code> <code>direction</code><br />
 <i>Direction. </i></p>
<h2>Detailed Description</h2>
<p>Directed rectangle representing bounding rectangle and orientation of a column.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtColumnRect::Direction</code></h3>
<p>Direction of the column. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>LeftToRight </i></p>
<dd>From left to right.</p>
<dt><i>RightToLeft </i></p>
<dd>From right to left.</p>
<dt><i>BottomToTop </i></p>
<dd>From bottom to top.</p>
<dt><i>TopToBottom </i></p>
<dd>From top to bottom.</dl>
<h2>Member Function Documentation</h2>
<h3>Qt::Orientation QwtColumnRect::orientation () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Orientation</dl>
<h3>QRectF QwtColumnRect::toRect () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>A normalized QRect built from the intervals</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
