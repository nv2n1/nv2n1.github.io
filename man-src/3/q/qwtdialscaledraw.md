---
title: "qwtdialscaledraw(3)"
name: "qwtdialscaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdialscaledraw/"
description: "QwtDialScaleDraw – A special scale draw made for QwtDial."
---

<p>QwtDialScaleDraw &#8211; A special scale draw made for <code>QwtDial</code>. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_dial.h">qwt_dial.h</a>&gt; </p>
<p> Inherits <code>QwtRoundScaleDraw</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtDialScaleDraw</code> (<code>QwtDial</code> *) </p>
<p> virtual <code>QwtText</code> <code>label</code> (double value) const </p>
<p> void <code>setPenWidth</code> (uint) </p>
<p> uint <code>penWidth</code> () const </p>
<h2>Detailed Description</h2>
<p>A special scale draw made for <code>QwtDial</code>. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtDial</code>, <code>QwtCompass</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDialScaleDraw::QwtDialScaleDraw (<code>QwtDial</code> * parent) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent dial widget</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtText</code> QwtDialScaleDraw::label (double value) const [virtual]</h3>
<p>Call <code>QwtDial::scaleLabel</code> of the parent dial widget. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value to display</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>QwtDial::scaleLabel()</code></dl>
<p> Reimplemented from <code>QwtAbstractScaleDraw</code>.</p>
<h3>uint QwtDialScaleDraw::penWidth () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pen width used for painting the scale</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setPenWidth</code>, <code>QwtDial::drawScale()</code></dl>
<h3>void QwtDialScaleDraw::setPenWidth (uint penWidth)</h3>
<p>Set the pen width used for painting the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>penWidth</i> Pen width</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>penWidth()</code>, <code>QwtDial::drawScale()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
