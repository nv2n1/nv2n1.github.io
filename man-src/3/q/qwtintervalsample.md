---
title: "qwtintervalsample(3)"
name: "qwtintervalsample"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qwtintervalsample/"
description: "QwtIntervalSample –"
---

<p>QwtIntervalSample &#8211; </p>
<p> A sample of the types (x1-x2, y) or (x, y1-y2)</p>
<h2>Synopsis</h2>
<p>#include &lt;qwt_samples.h&gt;</p>
<h3>Public Member Functions</h3>
<p><code>QwtIntervalSample</code> () </p>
<p> <code>QwtIntervalSample</code> (double, const <code>QwtInterval</code> &amp;)<br />
 <i>Constructor. </i><br />
 <code>QwtIntervalSample</code> (double <code>value</code>, double min, double max)<br />
 <i>Constructor. </i><br />
 bool <code>operator==</code> (const <code>QwtIntervalSample</code> &amp;) const<br />
 <i>Compare operator. </i><br />
 bool <code>operator!=</code> (const <code>QwtIntervalSample</code> &amp;) const<br />
 <i>Compare operator. </i></p>
<h3>Public Attributes</h3>
<p>double <code>value</code><br />
 <i>Value. </i><br />
 <code>QwtInterval</code> <code>interval</code><br />
 <i>Interval. </i></p>
<h2>Detailed Description</h2>
<p>A sample of the types (x1-x2, y) or (x, y1-y2)</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>QwtIntervalSample::QwtIntervalSample () [inline]</h3>
<p>Constructor The value is set to 0.0, the interval is invalid </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Qwt User&#8217;s Guide from the source code.</p>
