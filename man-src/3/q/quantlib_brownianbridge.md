---
title: "quantlib_brownianbridge(3)"
name: "quantlib_brownianbridge"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_brownianbridge/"
description: "QuantLib::BrownianBridge – Builds Wiener process paths using Gaussian variates."
---

<p>QuantLib::BrownianBridge &#8211; Builds Wiener process paths using Gaussian variates. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/methods/montecarlo/brownianbridge.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>BrownianBridge</code> (Size steps)<br />
 <i>unit-time path </i><br />
 <code>BrownianBridge</code> (const std::vector&lt; <code>Time</code> &gt; &amp;times)<br />
 <i>generic times </i><br />
 <code>BrownianBridge</code> (const <code>TimeGrid</code> &amp;timeGrid)<br />
 <i>generic times </i> </p>
<p> <code>inspectors</code> </p>
<p> Size <code>size</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>times</code> () const </p>
<h3>Brownian-bridge constructor</h3>
<p>template&lt;class RandomAccessIterator1 , class RandomAccessIterator2 &gt; void <code>transform</code> (RandomAccessIterator1 begin, RandomAccessIterator1 end, RandomAccessIterator2 output) const </p>
<h2>Detailed Description</h2>
<p>Builds Wiener process paths using Gaussian variates. </p>
<p> This class generates normalized (i.e., unit-variance) paths as sequences of variations. In order to obtain the actual path of the underlying, the returned variations must be multiplied by the integrated variance (including time) over the corresponding time step.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>BrownianBridge</code> (const std::vector&lt; <code>Time</code> &gt; &amp; times)</h3>
<p>generic times </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>the starting time of the path is assumed to be 0 and must not be included</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
