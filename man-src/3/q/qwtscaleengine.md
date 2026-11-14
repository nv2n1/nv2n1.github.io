---
title: "qwtscaleengine(3)"
name: "qwtscaleengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtscaleengine/"
description: "QwtScaleEngine –"
---

<p>QwtScaleEngine &#8211; </p>
<p> Base class for scale engines.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_scale_engine.h&gt; </p>
<p> Inherited by <code>QwtLinearScaleEngine</code>, and <code>QwtLogScaleEngine</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Attribute</code> { <code>NoAttribute</code> = 0x00, <code>IncludeReference</code> = 0x01, <code>Symmetric</code> = 0x02, <code>Floating</code> = 0x04, <code>Inverted</code> = 0x08 } </p>
<p> typedef QFlags&lt; <code>Attribute</code> &gt; <code>Attributes</code><br />
 <i>Layout attributes. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtScaleEngine</code> (uint <code>base</code>=10) </p>
<p> virtual <code>~QwtScaleEngine</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setBase</code> (uint <code>base</code>) </p>
<p> uint <code>base</code> () const </p>
<p> void <code>setAttribute</code> (<code>Attribute</code>, bool on=true) </p>
<p> bool <code>testAttribute</code> (<code>Attribute</code>) const </p>
<p> void <code>setAttributes</code> (<code>Attributes</code>) </p>
<p> <code>Attributes</code> <code>attributes</code> () const </p>
<p> void <code>setReference</code> (double <code>reference</code>)<br />
 <i>Specify a reference point. </i><br />
 double <code>reference</code> () const </p>
<p> void <code>setMargins</code> (double lower, double upper)<br />
 <i>Specify margins at the scale&#8217;s endpoints. </i><br />
 double <code>lowerMargin</code> () const </p>
<p> double <code>upperMargin</code> () const </p>
<p> virtual void <code>autoScale</code> (int maxNumSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const =0 </p>
<p> virtual <code>QwtScaleDiv</code> <code>divideScale</code> (double x1, double x2, int maxMajorSteps, int maxMinorSteps, double stepSize=0.0) const =0<br />
 <i>Calculate a scale division. </i><br />
 void <code>setTransformation</code> (<code>QwtTransform</code> *) </p>
<p> <code>QwtTransform</code> * <code>transformation</code> () const </p>
<h3>Protected Member Functions</h3>
<p>bool <code>contains</code> (const <code>QwtInterval</code> &amp;, double val) const </p>
<p> QList&lt; double &gt; <code>strip</code> (const QList&lt; double &gt; &amp;, const <code>QwtInterval</code> &amp;) const </p>
<p> double <code>divideInterval</code> (double interval, int numSteps) const </p>
<p> <code>QwtInterval</code> <code>buildInterval</code> (double v) const<br />
 <i>Build an interval around a value. </i></p>
<h2>Detailed Description</h2>
<p>Base class for scale engines. </p>
<p> A scale engine tries to find &#8216;reasonable&#8217; ranges and step sizes for scales. </p>
<p> The layout of the scale can be varied with <code>setAttribute()</code>. </p>
<p> Qwt offers implementations for logarithmic and linear scales.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtScaleEngine::Attribute</code></h3>
<p>Layout attributes </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setAttribute()</code>, <code>testAttribute()</code>, <code>reference()</code>, <code>lowerMargin()</code>, <code>upperMargin()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>NoAttribute </i></p>
<dd>No attributes.</p>
<dt><i>IncludeReference </i></p>
<dd>Build a scale which includes the <code>reference()</code> value.</p>
<dt><i>Symmetric </i></p>
<dd>Build a scale which is symmetric to the <code>reference()</code> value.</p>
<dt><i>Floating </i></p>
<dd>The endpoints of the scale are supposed to be equal the outmost included values plus the specified margins (see <code>setMargins()</code>). If this attribute is <i>not</i> set, the endpoints of the scale will be integer multiples of the step size.</p>
<dt><i>Inverted </i></p>
<dd>Turn the scale upside down.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtScaleEngine::QwtScaleEngine (uintbase = 10) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>base</i> Base of the scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBase()</code></dl>
<h2>Member Function Documentation</h2>
<h3><code>QwtScaleEngine::Attributes</code> QwtScaleEngine::attributes () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Scale attributes</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>setAttributes()</code>, <code>testAttribute()</code></dl>
<h3>virtual void QwtScaleEngine::autoScale (intmaxNumSteps, double &amp;x1, double &amp;x2, double &amp;stepSize) const [pure virtual]</h3>
<p>Align and divide an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>maxNumSteps</i> Max. number of steps<br />
 <i>x1</i> First limit of the interval (In/Out)<br />
 <i>x2</i> Second limit of the interval (In/Out)<br />
 <i>stepSize</i> Step size (Return value)</dl>
<p> Implemented in <code>QwtLogScaleEngine</code>, <code>QwtLinearScaleEngine</code>, and <code>QwtDateScaleEngine</code>.</p>
<h3>uint QwtScaleEngine::base () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>base Base of the scale engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setBase()</code></dl>
<h3><code>QwtInterval</code> QwtScaleEngine::buildInterval (doublevalue) const [protected]</h3>
<p>Build an interval around a value. In case of v == 0.0 the interval is [-0.5, 0.5], otherwide it is [0.5 * v, 1.5 * v] </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Initial value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated interval</dl>
<h3>bool QwtScaleEngine::contains (const <code>QwtInterval</code> &amp;interval, doublevalue) const [protected]</h3>
<p>Check if an interval &#8216;contains&#8217; a value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>interval</i> Interval<br />
 <i>value</i> Value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the value is inside the interval</dl>
<h3>double QwtScaleEngine::divideInterval (doubleintervalSize, intnumSteps) const [protected]</h3>
<p>Calculate a step size for an interval size </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>intervalSize</i> Interval size<br />
 <i>numSteps</i> Number of steps</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Step size</dl>
<h3>virtual <code>QwtScaleDiv</code> QwtScaleEngine::divideScale (doublex1, doublex2, intmaxMajorSteps, intmaxMinorSteps, doublestepSize = 0.0) const [pure virtual]</h3>
<p>Calculate a scale division. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x1</i> First interval limit<br />
 <i>x2</i> Second interval limit<br />
 <i>maxMajorSteps</i> Maximum for the number of major steps<br />
 <i>maxMinorSteps</i> Maximum number of minor steps<br />
 <i>stepSize</i> Step size. If stepSize == 0.0, the scaleEngine calculates one.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Calculated scale division</dl>
<p> Implemented in <code>QwtLogScaleEngine</code>, <code>QwtLinearScaleEngine</code>, and <code>QwtDateScaleEngine</code>.</p>
<h3>double QwtScaleEngine::lowerMargin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the margin at the lower end of the scale The default margin is 0.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargins()</code></dl>
<h3>double QwtScaleEngine::reference () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the reference value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setReference()</code>, <code>setAttribute()</code></dl>
<h3>void QwtScaleEngine::setAttribute (<code>Attribute</code>attribute, boolon = true)</h3>
<p>Change a scale attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute to change<br />
 <i>on</i> On/Off</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>testAttribute()</code></dl>
<h3>void QwtScaleEngine::setAttributes (<code>Attributes</code>attributes)</h3>
<p>Change the scale attribute </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attributes</i> Set scale attributes</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>attributes()</code></dl>
<h3>void QwtScaleEngine::setBase (uintbase)</h3>
<p>Set the base of the scale engine </p>
<p> While a base of 10 is what 99.9% of all applications need certain scales might need a different base: f.e 2 </p>
<p> The default setting is 10 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>base</i> Base of the engine</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>base()</code></dl>
<h3>void QwtScaleEngine::setMargins (doublelower, doubleupper)</h3>
<p>Specify margins at the scale&#8217;s endpoints. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lower</i> minimum distance between the scale&#8217;s lower boundary and the smallest enclosed value<br />
 <i>upper</i> minimum distance between the scale&#8217;s upper boundary and the greatest enclosed value</dl>
<p> Margins can be used to leave a minimum amount of space between the enclosed intervals and the boundaries of the scale. </p>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>&bull;</p>
<dd><code>QwtLogScaleEngine</code> measures the margins in decades.</dl>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>upperMargin()</code>, <code>lowerMargin()</code></dl>
<h3>void QwtScaleEngine::setReference (doubler)</h3>
<p>Specify a reference point. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>r</i> new reference value</dl>
<p> The reference point is needed if options IncludeReference or Symmetric are active. Its default value is 0.0. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code></dl>
<h3>void QwtScaleEngine::setTransformation (<code>QwtTransform</code> *transform)</h3>
<p>Assign a transformation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>transform</i> Transformation</dl>
<p> The transformation object is used as factory for clones that are returned by <code>transformation()</code> </p>
<p> The scale engine takes ownership of the transformation. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTransform::copy()</code>, <code>transformation()</code></dl>
<h3>QList&lt; double &gt; QwtScaleEngine::strip (const QList&lt; double &gt; &amp;ticks, const <code>QwtInterval</code> &amp;interval) const [protected]</h3>
<p>Remove ticks from a list, that are not inside an interval </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ticks</i> Tick list<br />
 <i>interval</i> Interval</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Stripped tick list</dl>
<h3>bool QwtScaleEngine::testAttribute (<code>Attribute</code>attribute) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if attribute is enabled.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>attribute</i> Attribute to be tested</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>Attribute</code>, <code>setAttribute()</code></dl>
<h3><code>QwtTransform</code> * QwtScaleEngine::transformation () const</h3>
<p>Create and return a clone of the transformation of the engine. When the engine has no special transformation NULL is returned, indicating no transformation. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A clone of the transfomation</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setTransformation()</code></dl>
<h3>double QwtScaleEngine::upperMargin () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the margin at the upper end of the scale The default margin is 0.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setMargins()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
