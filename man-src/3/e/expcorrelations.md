---
title: "expcorrelations(3)"
name: "expcorrelations"
section: "3"
letter: "e"
url: "/docs/linux/man/3-expcorrelations/"
description: "ql/models/marketmodels/correlations/expcorrelations.hpp – exponential correlation matrix"
---

<h2 class="name">NAME</h2>
<p> ql/models/marketmodels/correlations/expcorrelations.hpp &#8211; exponential correlation matrix </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrix.hpp&gt;<br />
 #include &lt;ql/utilities/disposable.hpp&gt;<br />
 #include &lt;ql/models/marketmodels/piecewiseconstantcorrelation.hpp&gt; </p>
<h3>Functions</h3>
<p> Disposable&lt; Matrix &gt; <code>exponentialCorrelations</code> (const std::vector&lt; Time &gt; &amp;rateTimes, Real longTermCorr=0.5, Real beta=0.2, Real gamma=1.0, Time t=0.0) </p>
<h2>Detailed Description</h2>
<p> exponential correlation matrix </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
