---
title: "qwtanalogclock(3)"
name: "qwtanalogclock"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtanalogclock/"
description: "QwtAnalogClock –"
---

<p>QwtAnalogClock &#8211; </p>
<p> An analog clock.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_analog_clock.h&gt; </p>
<p> Inherits <code>QwtDial</code>.</p>
<h3>Public Types</h3>
<p>enum <code>Hand</code> { <code>SecondHand</code>, <code>MinuteHand</code>, <code>HourHand</code>, <code>NHands</code> } </p>
<h3>Public Slots</h3>
<p>void <code>setCurrentTime</code> ()<br />
 <i>Set the current time. </i><br />
 void <code>setTime</code> (const QTime &amp;) </p>
<h3>Public Member Functions</h3>
<p><code>QwtAnalogClock</code> (QWidget *parent=NULL) </p>
<p> virtual <code>~QwtAnalogClock</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setHand</code> (<code>Hand</code>, <code>QwtDialNeedle</code> *) </p>
<p> const <code>QwtDialNeedle</code> * <code>hand</code> (<code>Hand</code>) const </p>
<p> <code>QwtDialNeedle</code> * <code>hand</code> (<code>Hand</code>) </p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>drawNeedle</code> (QPainter *, const QPointF &amp;, double radius, double direction, QPalette::ColorGroup) const<br />
 <i>Draw the needle. </i><br />
 virtual void <code>drawHand</code> (QPainter *, <code>Hand</code>, const QPointF &amp;, double radius, double direction, QPalette::ColorGroup) const </p>
<h3>Additional Inherited Members</h3>
<h2>Detailed Description</h2>
<p>An analog clock. </p>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>#include &lt;qwt_analog_clock.h&gt;
QwtAnalogClock *clock = new QwtAnalogClock(...);
clock-&gt;scaleDraw()-&gt;<a href="//www.systutorials.com/docs/linux/man/3-setPenWidth/">setPenWidth</a>(3);
clock-&gt;<a href="//www.systutorials.com/docs/linux/man/6-setLineWidth/">setLineWidth</a>(6);
clock-&gt;setFrameShadow(QwtDial::Sunken);
clock-&gt;setTime();
// update the clock every second
QTimer *timer = new QTimer(clock);
timer-&gt;connect(timer, SIGNAL(timeout()), clock, SLOT(setCurrentTime()));
timer-&gt;start(1000);</pre>
</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The examples/dials example shows how to use <code>QwtAnalogClock</code>.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>QwtAnalogClock::Hand</code></h3>
<p>Hand type </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setHand()</code>, <code>hand()</code></dl>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>SecondHand </i></p>
<dd>Needle displaying the seconds.</p>
<dt><i>MinuteHand </i></p>
<dd>Needle displaying the minutes.</p>
<dt><i>HourHand </i></p>
<dd>Needle displaying the hours.</p>
<dt><i>NHands </i></p>
<dd>Number of needles.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtAnalogClock::QwtAnalogClock (QWidget *parent = NULL) [explicit]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>void QwtAnalogClock::drawHand (QPainter *painter, <code>Hand</code>hd, const QPointF &amp;center, doubleradius, doubledirection, QPalette::ColorGroupcg) const [protected], [virtual]</h3>
<p>Draw a clock hand </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>hd</i> Specify the type of hand<br />
 <i>center</i> Center of the clock<br />
 <i>radius</i> Maximum length for the hands<br />
 <i>direction</i> Direction of the hand in degrees, counter clockwise<br />
 <i>cg</i> ColorGroup</dl>
<h3>void QwtAnalogClock::drawNeedle (QPainter *painter, const QPointF &amp;center, doubleradius, doubledir, QPalette::ColorGroupcolorGroup) const [protected], [virtual]</h3>
<p>Draw the needle. A clock has no single needle but three hands instead. <code>drawNeedle()</code> translates <code>value()</code> into directions for the hands and calls <code>drawHand()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>center</i> Center of the clock<br />
 <i>radius</i> Maximum length for the hands<br />
 <i>dir</i> Dummy, not used.<br />
 <i>colorGroup</i> ColorGroup</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>drawHand()</code></dl>
<p> Reimplemented from <code>QwtDial</code>.</p>
<h3>const <code>QwtDialNeedle</code> * QwtAnalogClock::hand (<code>Hand</code>hd) const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Clock hand</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hd</i> Specifies the type of hand</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setHand()</code></dl>
<h3><code>QwtDialNeedle</code> * QwtAnalogClock::hand (<code>Hand</code>hd)</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Clock hand</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hd</i> Specifies the type of hand</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setHand()</code></dl>
<h3>void QwtAnalogClock::setHand (<code>Hand</code>hand, <code>QwtDialNeedle</code> *needle)</h3>
<p>Set a clock hand </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>hand</i> Specifies the type of hand<br />
 <i>needle</i> Hand</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>hand()</code></dl>
<h3>void QwtAnalogClock::setTime (const QTime &amp;time) [slot]</h3>
<p>Set a time </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>time</i> Time to display</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
