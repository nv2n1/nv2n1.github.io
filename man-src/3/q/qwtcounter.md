---
title: "qwtcounter(3)"
name: "qwtcounter"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtcounter/"
description: "QwtCounter –"
---

<p>QwtCounter &#8211; </p>
<p> The Counter Widget.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_counter.h&gt; </p>
<p> Inherits QWidget.</p>
<h3>Public Types</h3>
<p>enum <code>Button</code> { <code>Button1</code>, <code>Button2</code>, <code>Button3</code>, <code>ButtonCnt</code> }<br />
 <i>Button index. </i></p>
<h3>Public Slots</h3>
<p>void <code>setValue</code> (double)<br />
 <i>Set a new value without adjusting to the step raster. </i></p>
<h3>Signals</h3>
<p>void <code>buttonReleased</code> (double <code>value</code>) </p>
<p> void <code>valueChanged</code> (double <code>value</code>) </p>
<h3>Public Member Functions</h3>
<p><code>QwtCounter</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtCounter</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setValid</code> (bool) </p>
<p> bool <code>isValid</code> () const </p>
<p> void <code>setWrapping</code> (bool)<br />
 <i>En/Disable wrapping. </i><br />
 bool <code>wrapping</code> () const </p>
<p> bool <code>isReadOnly</code> () const </p>
<p> void <code>setReadOnly</code> (bool)<br />
 <i>Allow/disallow the user to manually edit the value. </i><br />
 void <code>setNumButtons</code> (int n) </p>
<p> int <code>numButtons</code> () const </p>
<p> void <code>setIncSteps</code> (<code>QwtCounter::Button</code> btn, int nSteps) </p>
<p> int <code>incSteps</code> (<code>QwtCounter::Button</code> btn) const </p>
<p> virtual QSize <code>sizeHint</code> () const<br />
 <i>A size hint. </i><br />
 double <code>singleStep</code> () const </p>
<p> void <code>setSingleStep</code> (double s)<br />
 <i>Set the step size of the counter. </i><br />
 void <code>setRange</code> (double min, double max)<br />
 <i>Set the minimum and maximum values. </i><br />
 double <code>minimum</code> () const </p>
<p> void <code>setMinimum</code> (double min) </p>
<p> double <code>maximum</code> () const </p>
<p> void <code>setMaximum</code> (double max) </p>
<p> void <code>setStepButton1</code> (int nSteps) </p>
<p> int <code>stepButton1</code> () const<br />
 <i>returns the number of increment steps for button 1 </i><br />
 void <code>setStepButton2</code> (int nSteps) </p>
<p> int <code>stepButton2</code> () const<br />
 <i>returns the number of increment steps for button 2 </i><br />
 void <code>setStepButton3</code> (int nSteps) </p>
<p> int <code>stepButton3</code> () const<br />
 <i>returns the number of increment steps for button 3 </i><br />
 double <code>value</code> () const </p>
<h3>Protected Member Functions</h3>
<p>virtual bool <code>event</code> (QEvent *) </p>
<p> virtual void <code>wheelEvent</code> (QWheelEvent *) </p>
<p> virtual void <code>keyPressEvent</code> (QKeyEvent *) </p>
<h2>Detailed Description</h2>
<p>The Counter Widget. </p>
<p> A Counter consists of a label displaying a number and one ore more (up to three) push buttons on each side of the label which can be used to increment or decrement the counter&#8217;s value. </p>
<p> A counter has a range from a minimum value to a maximum value and a step size. When the wrapping property is set the counter is circular. </p>
<p> The number of steps by which a button increments or decrements the value can be specified using <code>setIncSteps()</code>. The number of buttons can be changed with <code>setNumButtons()</code>. </p>
<p> Example: </p>
<pre>#include &lt;qwt_counter.h&gt;
QwtCounter *counter = new QwtCounter(parent);
counter-&gt;setRange(0.0, 100.0); // From 0.0 to 100
counter-&gt;setSingleStep( 1.0 ); // Step size 1.0
counter-&gt;<a href="//www.systutorials.com/docs/linux/man/2-setNumButtons/">setNumButtons</a>(2); // Two buttons each side
counter-&gt;setIncSteps(QwtCounter::Button1, 1); // Button 1 increments 1 step
counter-&gt;setIncSteps(QwtCounter::Button2, 20); // Button 2 increments 20 steps
connect(counter, SIGNAL(valueChanged(double)), myClass, SLOT(newValue(double)));</pre>
<p>&nbsp;<wbr></p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtCounter::Button</code></h3>
<p>Button index. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>Button1 </i></p>
<dd>Button intended for minor steps.</p>
<dt><i>Button2 </i></p>
<dd>Button intended for medium steps.</p>
<dt><i>Button3 </i></p>
<dd>Button intended for large steps.</p>
<dt><i>ButtonCnt </i></p>
<dd>Number of buttons.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtCounter::QwtCounter (QWidget *parent = NULL) [explicit]</h3>
<p>The counter is initialized with a range is set to [0.0, 1.0] with 0.01 as single step size. The value is invalid. </p>
<p> The default number of buttons is set to 2. The default increments are: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Button 1: 1 step</p>
<dt>&bull;</p>
<dd>Button 2: 10 steps</p>
<dt>&bull;</p>
<dd>Button 3: 100 steps</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i></dl>
<h2>Member Function Documentation</h2>
<h3>void QwtCounter::buttonReleased (doublevalue) [signal]</h3>
<p>This signal is emitted when a button has been released </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> The new value</dl>
<h3>bool QwtCounter::event (QEvent *event) [protected], [virtual]</h3>
<p>Handle QEvent::PolishRequest events </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Event</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>see QWidget::event()</dl>
<h3>int QwtCounter::incSteps (<code>QwtCounter::Button</code>button) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The number of steps by which a specified button increments the value or 0 if the button is invalid.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>button</i> Button index</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setIncSteps()</code></dl>
<h3>bool QwtCounter::isReadOnly () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when the line line edit is read only. (default is no)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setReadOnly()</code></dl>
<h3>bool QwtCounter::isValid () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, if the value is valid</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValid()</code>, <code>setValue()</code></dl>
<h3>void QwtCounter::keyPressEvent (QKeyEvent *event) [protected], [virtual]</h3>
<p>Handle key events </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Ctrl + Qt::Key_Home </p>
<p>&nbsp;<wbr>Step to&nbsp;<wbr><code>minimum()</code></p>
<dt>&bull;</p>
<dd>Ctrl + Qt::Key_End </p>
<p>&nbsp;<wbr>Step to&nbsp;<wbr><code>maximum()</code></p>
<dt>&bull;</p>
<dd>Qt::Key_Up </p>
<p>&nbsp;<wbr>Increment by incSteps(QwtCounter::Button1)</p>
<dt>&bull;</p>
<dd>Qt::Key_Down </p>
<p>&nbsp;<wbr>Decrement by incSteps(QwtCounter::Button1)</p>
<dt>&bull;</p>
<dd>Qt::Key_PageUp </p>
<p>&nbsp;<wbr>Increment by incSteps(QwtCounter::Button2)</p>
<dt>&bull;</p>
<dd>Qt::Key_PageDown </p>
<p>&nbsp;<wbr>Decrement by incSteps(QwtCounter::Button2)</p>
<dt>&bull;</p>
<dd>Shift + Qt::Key_PageUp </p>
<p>&nbsp;<wbr>Increment by incSteps(QwtCounter::Button3)</p>
<dt>&bull;</p>
<dd>Shift + Qt::Key_PageDown </p>
<p>&nbsp;<wbr>Decrement by incSteps(QwtCounter::Button3)</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Key event</dl>
<h3>double QwtCounter::maximum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The maximum of the range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMaximum()</code>, <code>minimum()</code></dl>
<h3>double QwtCounter::minimum () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The minimum of the range</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMinimum()</code>, <code>maximum()</code></dl>
<h3>int QwtCounter::numButtons () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>The number of buttons on each side of the widget.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setNumButtons()</code></dl>
<h3>void QwtCounter::setIncSteps (<code>QwtCounter::Button</code>button, intnumSteps)</h3>
<p>Specify the number of steps by which the value is incremented or decremented when a specified button is pushed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>button</i> Button index<br />
 <i>numSteps</i> Number of steps</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>incSteps()</code></dl>
<h3>void QwtCounter::setMaximum (doublevalue)</h3>
<p>Set the maximum value of the range </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Maximum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMinimum()</code>, <code>maximum()</code></dl>
<h3>void QwtCounter::setMinimum (doublevalue)</h3>
<p>Set the minimum value of the range </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> Minimum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setRange()</code>, <code>setMaximum()</code>, <code>minimum()</code></dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The maximum is adjusted if necessary to ensure that the range remains valid.</dl>
<h3>void QwtCounter::setNumButtons (intnumButtons)</h3>
<p>Specify the number of buttons on each side of the label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>numButtons</i> Number of buttons</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>numButtons()</code></dl>
<h3>void QwtCounter::setRange (doublemin, doublemax)</h3>
<p>Set the minimum and maximum values. The maximum is adjusted if necessary to ensure that the range remains valid. The value might be modified to be inside of the range. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>min</i> Minimum value<br />
 <i>max</i> Maximum value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>minimum()</code>, <code>maximum()</code></dl>
<h3>void QwtCounter::setReadOnly (boolon)</h3>
<p>Allow/disallow the user to manually edit the value. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> True disable editing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isReadOnly()</code></dl>
<h3>void QwtCounter::setSingleStep (doublestepSize)</h3>
<p>Set the step size of the counter. A value &lt;= 0.0 disables stepping </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>stepSize</i> Single step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>singleStep()</code></dl>
<h3>void QwtCounter::setStepButton1 (intnSteps)</h3>
<p>Set the number of increment steps for button 1 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nSteps</i> Number of steps</dl>
<h3>void QwtCounter::setStepButton2 (intnSteps)</h3>
<p>Set the number of increment steps for button 2 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nSteps</i> Number of steps</dl>
<h3>void QwtCounter::setStepButton3 (intnSteps)</h3>
<p>Set the number of increment steps for button 3 </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nSteps</i> Number of steps</dl>
<h3>void QwtCounter::setValid (boolon)</h3>
<p>Set the counter to be in valid/invalid state </p>
<p> When the counter is set to invalid, no numbers are displayed and the buttons are disabled. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> If true the counter will be set as valid</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValue()</code>, <code>isValid()</code></dl>
<h3>void QwtCounter::setValue (doublevalue) [slot]</h3>
<p>Set a new value without adjusting to the step raster. The state of the counter is set to be valid. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> New value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>isValid()</code>, <code>value()</code>, <code>valueChanged()</code></dl>
<p> <code>Warning:</code></p>
<dl COMPACT>
<dd>The value is clipped when it lies outside the range.</dl>
<h3>void QwtCounter::setWrapping (boolon)</h3>
<p>En/Disable wrapping. If wrapping is true stepping up from <code>maximum()</code> value will take you to the <code>minimum()</code> value and vice versa. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> En/Disable wrapping</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>wrapping()</code></dl>
<h3>double QwtCounter::singleStep () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Single step size</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSingleStep()</code></dl>
<h3>double QwtCounter::value () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Current value of the counter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setValue()</code>, <code>valueChanged()</code></dl>
<h3>void QwtCounter::valueChanged (doublevalue) [signal]</h3>
<p>This signal is emitted when the counter&#8217;s value has changed </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>value</i> The new value</dl>
<h3>void QwtCounter::wheelEvent (QWheelEvent *event) [protected], [virtual]</h3>
<p>Handle wheel events </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Wheel event</dl>
<h3>bool QwtCounter::wrapping () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>True, when wrapping is set</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setWrapping()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
