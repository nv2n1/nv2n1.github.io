---
title: "qwtpixelmatrix(3)"
name: "qwtpixelmatrix"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtpixelmatrix/"
description: "QwtPixelMatrix –"
---

<p>QwtPixelMatrix &#8211; </p>
<p> A bit field corresponding to the pixels of a rectangle.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_pixel_matrix.h&gt; </p>
<p> Inherits QBitArray.</p>
<h3>Public Member Functions</h3>
<p><code>QwtPixelMatrix</code> (const QRect &amp;<code>rect</code>)<br />
 <i>Constructor. </i><br />
 <code>~QwtPixelMatrix</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setRect</code> (const QRect &amp;<code>rect</code>) </p>
<p> QRect <code>rect</code> () const </p>
<p> bool <code>testPixel</code> (int x, int y) const<br />
 <i>Test if a pixel has been set. </i><br />
 bool <code>testAndSetPixel</code> (int x, int y, bool on)<br />
 <i>Set a pixel and test if a pixel has been set before. </i><br />
 int <code>index</code> (int x, int y) const<br />
 <i>Calculate the index in the bit field corresponding to a position. </i></p>
<h2>Detailed Description</h2>
<p>A bit field corresponding to the pixels of a rectangle. </p>
<p> <code>QwtPixelMatrix</code> is intended to filter out duplicates in an unsorted array of points.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtPixelMatrix::QwtPixelMatrix (const QRect &amp;rect)</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle for the matrix</dl>
<h2>Member Function Documentation</h2>
<h3>int QwtPixelMatrix::index (intx, inty) const [inline]</h3>
<p>Calculate the index in the bit field corresponding to a position. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X-coordinate<br />
 <i>y</i> Y-coordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Index, when <code>rect()</code> contains pos &#8211; otherwise -1.</dl>
<h3>QRect QwtPixelMatrix::rect () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Bounding rectangle</dl>
<h3>void QwtPixelMatrix::setRect (const QRect &amp;rect)</h3>
<p>Set the bounding rectangle of the matrix </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>rect</i> Bounding rectangle</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>All bits are cleared</dl>
<h3>bool QwtPixelMatrix::testAndSetPixel (intx, inty, boolon) [inline]</h3>
<p>Set a pixel and test if a pixel has been set before. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X-coordinate<br />
 <i>y</i> Y-coordinate<br />
 <i>on</i> Set/Clear the pixel</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when pos is outside of <code>rect()</code>, or when the pixel was set before.</dl>
<h3>bool QwtPixelMatrix::testPixel (intx, inty) const [inline]</h3>
<p>Test if a pixel has been set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> X-coordinate<br />
 <i>y</i> Y-coordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>true, when pos is outside of <code>rect()</code>, or when the pixel has already been set.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
