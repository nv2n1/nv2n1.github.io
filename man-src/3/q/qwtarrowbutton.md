---
title: "qwtarrowbutton(3)"
name: "qwtarrowbutton"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtarrowbutton/"
description: "QwtArrowButton –"
---

<p>QwtArrowButton &#8211; </p>
<p> Arrow Button.</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_arrow_button.h&gt; </p>
<p> Inherits QPushButton.</p>
<h3>Public Member Functions</h3>
<p><code>QwtArrowButton</code> (int <code>num</code>, Qt::ArrowType, QWidget *parent=NULL) </p>
<p> virtual <code>~QwtArrowButton</code> ()<br />
 <i>Destructor. </i><br />
 Qt::ArrowType <code>arrowType</code> () const<br />
 <i>The direction of the arrows. </i><br />
 int <code>num</code> () const<br />
 <i>The number of arrows. </i><br />
 virtual QSize <code>sizeHint</code> () const </p>
<p> virtual QSize <code>minimumSizeHint</code> () const<br />
 <i>Return a minimum size hint. </i></p>
<h3>Protected Member Functions</h3>
<p>virtual void <code>paintEvent</code> (QPaintEvent *event) </p>
<p> virtual void <code>drawButtonLabel</code> (QPainter *p)<br />
 <i>Draw the button label. </i><br />
 virtual void <code>drawArrow</code> (QPainter *, const QRect &amp;, Qt::ArrowType) const </p>
<p> virtual QRect <code>labelRect</code> () const </p>
<p> virtual QSize <code>arrowSize</code> (Qt::ArrowType, const QSize &amp;boundingSize) const </p>
<p> virtual void <code>keyPressEvent</code> (QKeyEvent *)<br />
 <i>autoRepeat for the space keys </i></p>
<h2>Detailed Description</h2>
<p>Arrow Button. </p>
<p> A push button with one or more filled triangles on its front. An Arrow button can have 1 to 3 arrows in a row, pointing up, down, left or right.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtArrowButton::QwtArrowButton (intnum, Qt::ArrowTypearrowType, QWidget *parent = NULL) [explicit]</h3>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>num</i> Number of arrows<br />
 <i>arrowType</i> see Qt::ArrowType in the Qt docs.<br />
 <i>parent</i> Parent widget</dl>
<h2>Member Function Documentation</h2>
<h3>QSize QwtArrowButton::arrowSize (Qt::ArrowTypearrowType, const QSize &amp;boundingSize) const [protected], [virtual]</h3>
<p>Calculate the size for a arrow that fits into a rectangle of a given size </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>arrowType</i> Arrow type<br />
 <i>boundingSize</i> Bounding size</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Size of the arrow</dl>
<h3>void QwtArrowButton::drawArrow (QPainter *painter, const QRect &amp;r, Qt::ArrowTypearrowType) const [protected], [virtual]</h3>
<p>Draw an arrow int a bounding rectangle </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter<br />
 <i>r</i> Rectangle where to paint the arrow<br />
 <i>arrowType</i> Arrow type</dl>
<h3>void QwtArrowButton::drawButtonLabel (QPainter *painter) [protected], [virtual]</h3>
<p>Draw the button label. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>painter</i> Painter</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>The Qt Manual for QPushButton</dl>
<h3>QRect QwtArrowButton::labelRect () const [protected], [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>the bounding rectangle for the label</dl>
<h3>void QwtArrowButton::paintEvent (QPaintEvent *event) [protected], [virtual]</h3>
<p>Paint event handler </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> Paint event</dl>
<h3>QSize QwtArrowButton::sizeHint () const [virtual]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>a size hint</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
