---
title: "qwtlegendlabel(3)"
name: "qwtlegendlabel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtlegendlabel/"
description: "QwtLegendLabel –"
---

<p>QwtLegendLabel &#8211; </p>
<p> A widget representing something on a <code>QwtLegend</code>.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_legend_label.h&gt; </p>
<p> Inherits <code>QwtTextLabel</code>.</p>
<h3>Public Slots</h3>
<p>void <code>setChecked</code> (bool on) </p>
<h3>Signals</h3>
<p>void <code>clicked</code> ()<br />
 <i>Signal, when the legend item has been clicked. </i><br />
 void <code>pressed</code> ()<br />
 <i>Signal, when the legend item has been pressed. </i><br />
 void <code>released</code> ()<br />
 <i>Signal, when the legend item has been released. </i><br />
 void <code>checked</code> (bool)<br />
 <i>Signal, when the legend item has been toggled. </i></p>
<h3>Public Member Functions</h3>
<p><code>QwtLegendLabel</code> (QWidget *parent=0) </p>
<p> virtual <code>~QwtLegendLabel</code> ()<br />
 <i>Destructor. </i><br />
 void <code>setData</code> (const <code>QwtLegendData</code> &amp;) </p>
<p> const <code>QwtLegendData</code> &amp; <code>data</code> () const </p>
<p> void <code>setItemMode</code> (<code>QwtLegendData::Mode</code>) </p>
<p> <code>QwtLegendData::Mode</code> <code>itemMode</code> () const </p>
<p> void <code>setSpacing</code> (int <code>spacing</code>)<br />
 <i>Change the spacing between icon and text. </i><br />
 int <code>spacing</code> () const </p>
<p> virtual void <code>setText</code> (const <code>QwtText</code> &amp;) </p>
<p> void <code>setIcon</code> (const QPixmap &amp;) </p>
<p> QPixmap <code>icon</code> () const </p>
<p> virtual QSize <code>sizeHint</code> () const<br />
 <i>Return a size hint. </i><br />
 bool <code>isChecked</code> () const<br />
 <i>Return true, if the item is checked. </i></p>
<h3>Protected Member Functions</h3>
<p>void <code>setDown</code> (bool)<br />
 <i>Set the item being down. </i><br />
 bool <code>isDown</code> () const<br />
 <i>Return true, if the item is down. </i><br />
 virtual void <code>paintEvent</code> (QPaintEvent *)<br />
 <i>Paint event. </i><br />
 virtual void <code>mousePressEvent</code> (QMouseEvent *)<br />
 <i>Handle mouse press events. </i><br />
 virtual void <code>mouseReleaseEvent</code> (QMouseEvent *)<br />
 <i>Handle mouse release events. </i><br />
 virtual void <code>keyPressEvent</code> (QKeyEvent *)<br />
 <i>Handle key press events. </i><br />
 virtual void <code>keyReleaseEvent</code> (QKeyEvent *)<br />
 <i>Handle key release events. </i></p>
<h2>Detailed Description</h2>
<p>A widget representing something on a <code>QwtLegend</code>.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtLegendLabel::QwtLegendLabel (QWidget *parent = 0) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>const <code>QwtLegendData</code> &amp; QwtLegendLabel::data () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Attributes of the label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setData()</code>, <code>QwtPlotItem::legendData()</code></dl>
<h3>QPixmap QwtLegendLabel::icon () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Pixmap representing a plot item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setIcon()</code></dl>
<h3><code>QwtLegendData::Mode</code> QwtLegendLabel::itemMode () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Item mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemMode()</code></dl>
<h3>void QwtLegendLabel::setChecked (boolon) [slot]</h3>
<p>Check/Uncheck a the item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>on</i> check/uncheck</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setItemMode()</code></dl>
<h3>void QwtLegendLabel::setData (const <code>QwtLegendData</code> &amp;legendData)</h3>
<p>Set the attributes of the legend label </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>legendData</i> Attributes of the label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>data()</code></dl>
<h3>void QwtLegendLabel::setIcon (const QPixmap &amp;icon)</h3>
<p>Assign the icon </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>icon</i> Pixmap representing a plot item</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>icon()</code>, <code>QwtPlotItem::legendIcon()</code></dl>
<h3>void QwtLegendLabel::setItemMode (<code>QwtLegendData::Mode</code>mode)</h3>
<p>Set the item mode The default is <code>QwtLegendData::ReadOnly</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>mode</i> Item mode</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>itemMode()</code></dl>
<h3>void QwtLegendLabel::setSpacing (intspacing)</h3>
<p>Change the spacing between icon and text. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>spacing</i> Spacing</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>spacing()</code>, <code>QwtTextLabel::margin()</code></dl>
<h3>void QwtLegendLabel::setText (const <code>QwtText</code> &amp;text) [virtual]</h3>
<p>Set the text to the legend item </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>text</i> Text label</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>QwtTextLabel::text()</code></dl>
<p> Reimplemented from <code>QwtTextLabel</code>.</p>
<h3>int QwtLegendLabel::spacing () const</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>Spacing between icon and text</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>setSpacing()</code>, <code>QwtTextLabel::margin()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
