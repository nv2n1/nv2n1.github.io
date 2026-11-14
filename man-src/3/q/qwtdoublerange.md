---
title: "qwtdoublerange(3)"
name: "qwtdoublerange"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtdoublerange/"
description: "QwtDoubleRange – A class which controls a value within an interval."
---

<p>QwtDoubleRange &#8211; A class which controls a value within an interval. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/qwt_double_range.h">qwt_double_range.h</a>&gt; </p>
<p> Inherited by <code>QwtAbstractSlider</code>, and <code>QwtCounter</code>. </p>
<h3>Public Member Functions</h3>
<p><code>QwtDoubleRange</code> () </p>
<p> virtual <code>~QwtDoubleRange</code> () </p>
<p> void <code>setRange</code> (double vmin, double vmax, double vstep=0.0, int pagesize=1) </p>
<p> void <code>setValid</code> (bool) </p>
<p> bool <code>isValid</code> () const </p>
<p> virtual void <code>setValue</code> (double) </p>
<p> double <code>value</code> () const </p>
<p> void <code>setPeriodic</code> (bool tf) </p>
<p> bool <code>periodic</code> () const </p>
<p> void <code>setStep</code> (double) </p>
<p> double <code>step</code> () const </p>
<p> double <code>maxValue</code> () const </p>
<p> double <code>minValue</code> () const </p>
<p> int <code>pageSize</code> () const </p>
<p> virtual void <code>incValue</code> (int) </p>
<p> virtual void <code>incPages</code> (int) </p>
<p> virtual void <code>fitValue</code> (double) </p>
<h3>Protected Member Functions</h3>
<p>double <code>exactValue</code> () const </p>
<p> double <code>exactPrevValue</code> () const </p>
<p> double <code>prevValue</code> () const </p>
<p> virtual void <code>valueChange</code> () </p>
<p> virtual void <code>stepChange</code> () </p>
<p> virtual void <code>rangeChange</code> () </p>
<h2>Detailed Description</h2>
<p>A class which controls a value within an interval. </p>
<p> This class is useful as a base class or a member for sliders. It represents an interval of type double within which a value can be moved. The value can be either an arbitrary point inside the interval (see <code>QwtDoubleRange::setValue</code>), or it can be fitted into a step raster (see <code>QwtDoubleRange::fitValue</code> and <code>QwtDoubleRange::incValue</code>). </p>
<p> As a special case, a <code>QwtDoubleRange</code> can be periodic, which means that a value outside the interval will be mapped to a value inside the interval when <code>QwtDoubleRange::setValue()</code>, <code>QwtDoubleRange::fitValue()</code>, <code>QwtDoubleRange::incValue()</code> or <code>QwtDoubleRange::incPages()</code> are called.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtDoubleRange::QwtDoubleRange ()</h3>
<p>The range is initialized to [0.0, 100.0], the step size to 1.0, and the value to 0.0.</p>
<h3>QwtDoubleRange::~QwtDoubleRange () [virtual]</h3>
<p>Destroys the <code>QwtDoubleRange</code>. </p>
<h2>Member Function Documentation</h2>
<h3>double QwtDoubleRange::exactPrevValue () const [protected]</h3>
<p>Returns the exact previous value. </p>
<h3>double QwtDoubleRange::exactValue () const [protected]</h3>
<p>Returns the exact value. </p>
<p> The exact value is the value which <code>QwtDoubleRange::value</code> would return if the value were not adjusted to the step raster. It differs from the current value only if <code>QwtDoubleRange::fitValue</code> or <code>QwtDoubleRange::incValue</code> have been used before. This function is intended for internal use in derived classes.</p>
<h3>void QwtDoubleRange::fitValue (double x) [virtual]</h3>
<p>Adjust the value to the closest point in the step raster. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> value</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The value is clipped when it lies outside the range. When the range is <code>QwtDoubleRange::periodic</code>, it will be mapped to a point in the interval such that </p>
<pre>new value := x + n * (max. value - min. value)</pre>
<p>&nbsp;<wbr>with an integer number n.&nbsp;<wbr></dl>
<p> Reimplemented in <code>QwtAbstractSlider</code>.</p>
<h3>void QwtDoubleRange::incPages (int nPages) [virtual]</h3>
<p>Increment the value by a specified number of pages. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nPages</i> Number of pages to increment. A negative number decrements the value.</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The Page size is specified in the constructor.</dl>
<h3>void QwtDoubleRange::incValue (int nSteps) [virtual]</h3>
<p>Increment the value by a specified number of steps. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nSteps</i> Number of steps to increment</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>As a result of this operation, the new value will always be adjusted to the step raster.</dl>
<p> Reimplemented in <code>QwtAbstractSlider</code>.</p>
<h3>bool QwtDoubleRange::isValid () const</h3>
<p>Indicates if the value is valid. </p>
<p> Reimplemented in <code>QwtAbstractSlider</code>.</p>
<h3>double QwtDoubleRange::maxValue () const</h3>
<p>Returns the value of the second border of the range. </p>
<p> maxValue returns the value which has been specified as the second parameter in <code>QwtDoubleRange::setRange</code>. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code></dl>
<h3>double QwtDoubleRange::minValue () const</h3>
<p>Returns the value at the first border of the range. </p>
<p> minValue returns the value which has been specified as the first parameter in <code>setRange()</code>. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code></dl>
<h3>int QwtDoubleRange::pageSize () const</h3>
<p>Returns the page size in steps. </p>
<h3>bool QwtDoubleRange::periodic () const</h3>
<p>Returns true if the range is periodic. </p>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setPeriodic()</code></dl>
<h3>double QwtDoubleRange::prevValue () const [protected]</h3>
<p>Returns the previous value. </p>
<h3>void QwtDoubleRange::rangeChange () [protected, virtual]</h3>
<p>Notify a change of the range. </p>
<p> This virtual function is called whenever the range changes. The default implementation does nothing. </p>
<p> Reimplemented in <code>QwtCounter</code>, <code>QwtDial</code>, and <code>QwtSlider</code>.</p>
<h3>void QwtDoubleRange::setPeriodic (bool tf)</h3>
<p>Make the range periodic. </p>
<p> When the range is periodic, the value will be set to a point inside the interval such that </p>
<pre>point = value + n * width .fi
if the user tries to set a new value which is outside the range. If the range is nonperiodic (the default), values outside the range will be clipped.
<code>Parameters:</code>
<dl COMPACT><dt><dd><i>tf</i> true for a periodic range 
</dl></pre>
<h3>void QwtDoubleRange::setRange (double vmin, double vmax, double vstep = 0.0, int pageSize = 1)</h3>
<p>Specify range and step size. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>vmin</i> lower boundary of the interval<br />
 <i>vmax</i> higher boundary of the interval<br />
 <i>vstep</i> step width<br />
 <i>pageSize</i> page size in steps</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>A change of the range changes the value if it lies outside the new range. The current value will *not* be adjusted to the new step raster.</p>
<dt>*</p>
<dd>vmax &lt; vmin is allowed.</p>
<dt>*</p>
<dd>If the step size is left out or set to zero, it will be set to 1/100 of the interval length.</p>
<dt>*</p>
<dd>If the step size has an absurd value, it will be corrected to a better one.</dl>
</dl>
<h3>void QwtDoubleRange::setStep (double vstep)</h3>
<p>Change the step raster. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>vstep</i> new step width</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The value will <i>not</i> be adjusted to the new step raster.</dl>
<p> Reimplemented in <code>QwtCounter</code>.</p>
<h3>void QwtDoubleRange::setValid (bool isValid)</h3>
<p>Set the value to be valid/invalid. </p>
<p> Reimplemented in <code>QwtAbstractSlider</code>.</p>
<h3>void QwtDoubleRange::setValue (double x) [virtual]</h3>
<p>Set a new value without adjusting to the step raster. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>x</i> new value</dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The value is clipped when it lies outside the range. When the range is <code>QwtDoubleRange::periodic</code>, it will be mapped to a point in the interval such that </p>
<pre>new value := x + n * (max. value - min. value)</pre>
<p>&nbsp;<wbr>with an integer number n.&nbsp;<wbr></dl>
<p> Reimplemented in <code>QwtAbstractSlider</code>, and <code>QwtCounter</code>.</p>
<h3>double QwtDoubleRange::step () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the step size</dl>
<p> <code>See also:</code></p>
<dl COMPACT>
<dd><code>setStep()</code>, <code>setRange()</code></dl>
<p> Reimplemented in <code>QwtCounter</code>.</p>
<h3>void QwtDoubleRange::stepChange () [protected, virtual]</h3>
<p>Notify a change of the step size. </p>
<p> This virtual function is called whenever the step size changes. The default implementation does nothing.</p>
<h3>double QwtDoubleRange::value () const</h3>
<p>Returns the current value. </p>
<p> Reimplemented in <code>QwtCounter</code>.</p>
<h3>void QwtDoubleRange::valueChange () [protected, virtual]</h3>
<p>Notify a change of value. </p>
<p> This virtual function is called whenever the value changes. The default implementation does nothing. </p>
<p> Reimplemented in <code>QwtAbstractSlider</code>, <code>QwtDial</code>, <code>QwtSlider</code>, and <code>QwtWheel</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
