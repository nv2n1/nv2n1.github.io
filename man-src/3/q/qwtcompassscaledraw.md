---
title: "qwtcompassscaledraw(3)"
name: "qwtcompassscaledraw"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcompassscaledraw/"
description: "QwtCompassScaleDraw –"
---

<p>QwtCompassScaleDraw &#8211; </p>
<p> A special scale draw made for <code>QwtCompass</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_compass.h&gt; </p>
<p> Inherits <code>QwtRoundScaleDraw</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtCompassScaleDraw</code> ()<br />
 <i>Constructor. </i><br />
 <code>QwtCompassScaleDraw</code> (const QMap&lt; double, QString &gt; &amp;map)<br />
 <i>Constructor. </i><br />
 void <code>setLabelMap</code> (const QMap&lt; double, QString &gt; &amp;map)<br />
 <i>Set a map, mapping values to labels. </i><br />
 QMap&lt; double, QString &gt; <code>labelMap</code> () const </p>
<p> virtual <code>QwtText</code> <code>label</code> (double value) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>A special scale draw made for <code>QwtCompass</code>. </p>
<p> <code>QwtCompassScaleDraw</code> maps values to strings using a special map, that can be modified by the application </p>
<p> The default map consists of the labels N, NE, E, SE, S, SW, W, NW. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtCompass</code></dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtCompassScaleDraw::QwtCompassScaleDraw () [explicit]</h3>
<p>Constructor. Initializes a label map for multiples of 45 degrees</p>
<h3>QwtCompassScaleDraw::QwtCompassScaleDraw (const QMap&lt; double, QString &gt; &amp;map) [explicit]</h3>
<p>Constructor. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>map</i> Value to label map</dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtText</code> QwtCompassScaleDraw::label (doublevalue) const [virtual]</h3>
<p>Map a value to a corresponding label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Value that will be mapped</dl>
<p> <code>label()</code> looks in the <code>labelMap()</code> for a corresponding label for value or returns an null text. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Label, or QString::null</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>labelMap()</code>, <code>setLabelMap()</code></dl>
<p> Reimplemented from <code>QwtAbstractScaleDraw</code>.</p>
<h3>QMap&lt; double, QString &gt; QwtCompassScaleDraw::labelMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>map, mapping values to labels</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLabelMap()</code></dl>
<h3>void QwtCompassScaleDraw::setLabelMap (const QMap&lt; double, QString &gt; &amp;map)</h3>
<p>Set a map, mapping values to labels. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>map</i> Value to label map</dl>
<p> The values of the major ticks are found by looking into this map. The default map consists of the labels N, NE, E, SE, S, SW, W, NW. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The map will have no effect for values that are no major tick values. Major ticks can be changed by QwtScaleDraw::setScale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>labelMap()</code>, scaleDraw(), setScale()</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
