---
title: "wfmath_segment(3)"
name: "wfmath_segment"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wfmath_segment/"
description: "WFMath::Segment – A line segment embedded in dim dimensions."
---

<p>WFMath::Segment &#8211; A line segment embedded in dim dimensions. </p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/segment.h">segment.h</a>&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Segment</code> ()<br />
 <i>construct an uninitialized segment </i><br />
 <code>Segment</code> (const <code>Point</code>&lt; dim &gt; &amp;p1, const <code>Point</code>&lt; dim &gt; &amp;p2)<br />
 <i>construct a segment with endpoints p1 and p2 </i><br />
 <code>Segment</code> (const <code>Segment</code> &amp;s)<br />
 <i>construct a copy of a segment </i><br />
 const <code>Point</code>&lt; dim &gt; &amp; <code>endpoint</code> (const int i) const<br />
 <i>get one end of the segment </i><br />
 <code>Point</code>&lt; dim &gt; &amp; <code>endpoint</code> (const int i)<br />
 <i>get one end of the segment </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;const int dim&gt; class WFMath::Segment&lt; dim &gt;</h3>
<p>A line segment embedded in dim dimensions. </p>
<p> This class implements the full shape interface, as described in the fake class <code>Shape</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for WFMath from the source code.</p>
