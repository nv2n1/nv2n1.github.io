---
title: "forwardforwardmappings(3)"
name: "forwardforwardmappings"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forwardforwardmappings/"
description: "ql/models/marketmodels/forwardforwardmappings.hpp – Utility functions for mapping between forward rates of varying tenor."
---

<h2 class="name">NAME</h2>
<p> ql/models/marketmodels/forwardforwardmappings.hpp &#8211; Utility functions for mapping between forward rates of varying tenor. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrix.hpp&gt; </p>
<h3>Functions</h3>
<p> Disposable&lt; Matrix &gt; <code>ForwardForwardJacobian</code> (const CurveState &amp;cs, Size multiplier, Size offset) </p>
<p> Disposable&lt; Matrix &gt; <code>YMatrix</code> (const CurveState &amp;cs, const std::vector&lt; Spread &gt; &amp;shortDisplacements, const std::vector&lt; Spread &gt; &amp;longDisplacements, Size Multiplier, Size offset) </p>
<p> LMMCurveState <code>RestrictCurveState</code> (const CurveState &amp;cs, Size multiplier, Size offSet) </p>
<h2>Detailed Description</h2>
<p> Utility functions for mapping between forward rates of varying tenor. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
