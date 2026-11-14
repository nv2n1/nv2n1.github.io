---
title: "qwtsetsample(3)"
name: "qwtsetsample"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtsetsample/"
description: "QwtSetSample –"
---

<p>QwtSetSample &#8211; </p>
<p> A sample of the types (x1&#8230;xn, y) or (x, y1..yn)</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_samples.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtSetSample</code> () </p>
<p> <code>QwtSetSample</code> (double, const QVector&lt; double &gt; &amp;=QVector&lt; double &gt;()) </p>
<p> bool <code>operator==</code> (const <code>QwtSetSample</code> &amp;other) const<br />
 <i>Compare operator. </i><br />
 bool <code>operator!=</code> (const <code>QwtSetSample</code> &amp;other) const<br />
 <i>Compare operator. </i><br />
 double <code>added</code> () const </p>
<h3>Public Attributes</h3>
<p>double <code>value</code><br />
 <i>value </i><br />
 QVector&lt; double &gt; <code>set</code><br />
 <i>Vector of values associated to value. </i></p>
<h2>Detailed Description</h2>
<p>A sample of the types (x1&#8230;xn, y) or (x, y1..yn)</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtSetSample::QwtSetSample () [inline]</h3>
<p>Constructor The value is set to 0.0</p>
<h3>QwtSetSample::QwtSetSample (doublev, const QVector&lt; double &gt; &amp;s = QVector&lt;double&gt;()) [inline]</h3>
<p>Constructor </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>v</i> Value<br />
 <i>s</i> Set of values</dl>
<h2>Member Function Documentation</h2>
<h3>double QwtSetSample::added () const [inline]</h3>
<p><code>Returns:</code></p>
<dl COMPACT>
<dd>All values of the set added</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
