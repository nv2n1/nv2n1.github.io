---
title: "qwtabstractscale(3)"
name: "qwtabstractscale"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtabstractscale/"
description: "QwtAbstractScale –"
---

<p>QwtAbstractScale &#8211; </p>
<p> An abstract base class for widgets having a scale.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_abstract_scale.h&gt; </p>
<p> Inherits QWidget. </p>
<p> Inherited by <code>QwtAbstractSlider</code>, and <code>QwtThermo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>QwtAbstractScale</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtAbstractScale</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setScale</code> (double <code>lowerBound</code>, double <code>upperBound</code>)<br />
 <i>Specify a scale. </i><br />
 void <code>setScale</code> (const <code>QwtInterval</code> &amp;)<br />
 <i>Specify a scale. </i><br />
 void <code>setScale</code> (const <code>QwtScaleDiv</code> &amp;)<br />
 <i>Specify a scale. </i><br />
 const <code>QwtScaleDiv</code> &amp; <code>scaleDiv</code> () const </p>
<p> void <code>setLowerBound</code> (double value) </p>
<p> double <code>lowerBound</code> () const </p>
<p> void <code>setUpperBound</code> (double value) </p>
<p> double <code>upperBound</code> () const </p>
<p> void <code>setScaleStepSize</code> (double stepSize)<br />
 <i>Set the step size used for calculating a scale division. </i><br />
 double <code>scaleStepSize</code> () const </p>
<p> void <code>setScaleMaxMajor</code> (int ticks)<br />
 <i>Set the maximum number of major tick intervals. </i><br />
 int <code>scaleMaxMinor</code> () const </p>
<p> void <code>setScaleMaxMinor</code> (int ticks)<br />
 <i>Set the maximum number of minor tick intervals. </i><br />
 int <code>scaleMaxMajor</code> () const </p>
<p> void <code>setScaleEngine</code> (<code>QwtScaleEngine</code> *)<br />
 <i>Set a scale engine. </i><br />
 const <code>QwtScaleEngine</code> * <code>scaleEngine</code> () const </p>
<p> <code>QwtScaleEngine</code> * <code>scaleEngine</code> () </p>
<p> int <code>transform</code> (double) const </p>
<p> double <code>invTransform</code> (int) const </p>
<p> bool <code>isInverted</code> () const </p>
<p> double <code>minimum</code> () const </p>
<p> double <code>maximum</code> () const </p>
<p> const <code>QwtScaleMap</code> &amp; <code>scaleMap</code> () const </p>
<h3>Protected Member Functions</h3>
<p>void <code>rescale</code> (double <code>lowerBound</code>, double <code>upperBound</code>, double stepSize) </p>
<p> void <code>setAbstractScaleDraw</code> (<code>QwtAbstractScaleDraw</code> *)<br />
 <i>Set a scale draw. </i><br />
 const <code>QwtAbstractScaleDraw</code> * <code>abstractScaleDraw</code> () const </p>
<p> <code>QwtAbstractScaleDraw</code> * <code>abstractScaleDraw</code> () </p>
<p> virtual void <code>scaleChange</code> ()<br />
 <i>Notify changed scale. </i></p>
<h2>Detailed Description</h2>
<p>An abstract base class for widgets having a scale. </p>
<p> The scale of an <code>QwtAbstractScale</code> is determined by a <code>QwtScaleDiv</code> definition, that contains the boundaries and the ticks of the scale. The scale is painted using a <code>QwtScaleDraw</code> object. </p>
<p> The scale division might be assigned explicitly &#8211; but usually it is calculated from the boundaries using a <code>QwtScaleEngine</code>. </p>
<p> The scale engine also decides the type of transformation of the scale ( linear, logarithmic &#8230; ).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAbstractScale::QwtAbstractScale (QWidget *parent = NULL)</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<p> Creates a default <code>QwtScaleDraw</code> and a <code>QwtLinearScaleEngine</code>. The initial scale boundaries are set to [ 0.0, 100.0 ] </p>
<p> The <code>scaleStepSize()</code> is initialized to 0.0, <code>scaleMaxMajor()</code> to 5 and scaleMaxMajor to 3.</p>
<h2>Member Function Documentation</h2>
<h3>const <code>QwtAbstractScaleDraw</code> * QwtAbstractScale::abstractScaleDraw () const [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale draw</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAbstractScaleDraw()</code></dl>
<h3><code>QwtAbstractScaleDraw</code> * QwtAbstractScale::abstractScaleDraw () [protected]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale draw</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAbstractScaleDraw()</code></dl>
<h3>double QwtAbstractScale::invTransform (intvalue) const</h3>
<p>Translate a widget coordinate into a scale value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Widget coordinate</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Corresponding scale coordinate for value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleMap()</code>, <code>transform()</code></dl>
<h3>bool QwtAbstractScale::isInverted () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the scale is increasing in opposite direction to the widget coordinates</dl>
<h3>double QwtAbstractScale::lowerBound () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Lower bound of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setLowerBound()</code>, <code>setScale()</code>, <code>upperBound()</code></dl>
<h3>double QwtAbstractScale::maximum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The boundary with the larger value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimum()</code>, <code>lowerBound()</code>, <code>upperBound()</code></dl>
<h3>double QwtAbstractScale::minimum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The boundary with the smaller value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>maximum()</code>, <code>lowerBound()</code>, <code>upperBound()</code></dl>
<h3>void QwtAbstractScale::rescale (doublelowerBound, doubleupperBound, doublestepSize) [protected]</h3>
<p>Recalculate the scale division and update the scale. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> Lower limit of the scale interval<br />
 <i>upperBound</i> Upper limit of the scale interval<br />
 <i>stepSize</i> Major step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleChange()</code></dl>
<h3>const <code>QwtScaleDiv</code> &amp; QwtAbstractScale::scaleDiv () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale boundaries and positions of the ticks</dl>
<p> The scale division might have been assigned explicitly or calculated implicitly by <code>rescale()</code>.</p>
<h3>const <code>QwtScaleEngine</code> * QwtAbstractScale::scaleEngine () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleEngine()</code></dl>
<h3><code>QwtScaleEngine</code> * QwtAbstractScale::scaleEngine ()</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleEngine()</code></dl>
<h3>const <code>QwtScaleMap</code> &amp; QwtAbstractScale::scaleMap () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Map to translate between scale and widget coordinates</dl>
<h3>int QwtAbstractScale::scaleMaxMajor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximal number of major tick intervals</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleMaxMajor()</code>, <code>scaleMaxMinor()</code></dl>
<h3>int QwtAbstractScale::scaleMaxMinor () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Maximal number of minor tick intervals</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleMaxMinor()</code>, <code>scaleMaxMajor()</code></dl>
<h3>double QwtAbstractScale::scaleStepSize () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Hint for the step size of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setScaleStepSize()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<h3>void QwtAbstractScale::setAbstractScaleDraw (<code>QwtAbstractScaleDraw</code> *scaleDraw) [protected]</h3>
<p>Set a scale draw. scaleDraw has to be created with new and will be deleted in the destructor or the next call of <code>setAbstractScaleDraw()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>abstractScaleDraw()</code></dl>
<h3>void QwtAbstractScale::setLowerBound (doublevalue)</h3>
<p>Set the lower bound of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Lower bound</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>lowerBound()</code>, <code>setScale()</code>, <code>setUpperBound()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>For inverted scales the lower bound is greater than the upper bound</dl>
<h3>void QwtAbstractScale::setScale (doublelowerBound, doubleupperBound)</h3>
<p>Specify a scale. Define a scale by an interval </p>
<p> The ticks are calculated using <code>scaleMaxMinor()</code>, <code>scaleMaxMajor()</code> and <code>scaleStepSize()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lowerBound</i> lower limit of the scale interval<br />
 <i>upperBound</i> upper limit of the scale interval</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>For inverted scales the lower bound is greater than the upper bound</dl>
<h3>void QwtAbstractScale::setScale (const <code>QwtInterval</code> &amp;interval)</h3>
<p>Specify a scale. Define a scale by an interval </p>
<p> The ticks are calculated using <code>scaleMaxMinor()</code>, <code>scaleMaxMajor()</code> and <code>scaleStepSize()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval</dl>
<h3>void QwtAbstractScale::setScale (const <code>QwtScaleDiv</code> &amp;scaleDiv)</h3>
<p>Specify a scale. <code>scaleMaxMinor()</code>, <code>scaleMaxMajor()</code> and <code>scaleStepSize()</code> and have no effect. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>scaleDiv</i> Scale division</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>setAutoScale()</dl>
<h3>void QwtAbstractScale::setScaleEngine (<code>QwtScaleEngine</code> *scaleEngine)</h3>
<p>Set a scale engine. The scale engine is responsible for calculating the scale division and provides a transformation between scale and widget coordinates. </p>
<p> scaleEngine has to be created with new and will be deleted in the destructor or the next call of setScaleEngine.</p>
<h3>void QwtAbstractScale::setScaleMaxMajor (intticks)</h3>
<p>Set the maximum number of major tick intervals. The scale&#8217;s major ticks are calculated automatically such that the number of major intervals does not exceed ticks. </p>
<p> The default value is 5. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ticks</i> Maximal number of major ticks.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleMaxMajor()</code>, <code>setScaleMaxMinor()</code>, <code>setScaleStepSize()</code>, <code>QwtScaleEngine::divideInterval()</code></dl>
<h3>void QwtAbstractScale::setScaleMaxMinor (intticks)</h3>
<p>Set the maximum number of minor tick intervals. The scale&#8217;s minor ticks are calculated automatically such that the number of minor intervals does not exceed ticks. The default value is 3. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ticks</i> Maximal number of minor ticks.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleMaxMajor()</code>, <code>setScaleMaxMinor()</code>, <code>setScaleStepSize()</code>, <code>QwtScaleEngine::divideInterval()</code></dl>
<h3>void QwtAbstractScale::setScaleStepSize (doublestepSize)</h3>
<p>Set the step size used for calculating a scale division. The step size is hint for calculating the intervals for the major ticks of the scale. A value of 0.0 is interpreted as no hint. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepSize</i> Hint for the step size of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleStepSize()</code>, <code>QwtScaleEngine::divideScale()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Position and distance between the major ticks also depends on <code>scaleMaxMajor()</code>.</dl>
<h3>void QwtAbstractScale::setUpperBound (doublevalue)</h3>
<p>Set the upper bound of the scale </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Upper bound</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>upperBound()</code>, <code>setScale()</code>, <code>setLowerBound()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>For inverted scales the lower bound is greater than the upper bound</dl>
<h3>int QwtAbstractScale::transform (doublevalue) const</h3>
<p>Translate a scale value into a widget coordinate </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Scale value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Corresponding widget coordinate for value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>scaleMap()</code>, <code>invTransform()</code></dl>
<h3>double QwtAbstractScale::upperBound () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Upper bound of the scale</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setUpperBound()</code>, <code>setScale()</code>, <code>lowerBound()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
