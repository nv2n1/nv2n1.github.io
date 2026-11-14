---
title: "quantlib_multistepswaption(3)"
name: "quantlib_multistepswaption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_multistepswaption/"
description: "QuantLib::MultiStepSwaption –"
---

<p>QuantLib::MultiStepSwaption &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/products/multistep/multistepswaption.hpp&gt; </p>
<p> Inherits <code>QuantLib::MultiProductMultiStep</code>. </p>
<h3>Public Member Functions</h3>
<p><code>MultiStepSwaption</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes, Size startIndex, Size endIndex, boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;) </p>
<p> <code>MarketModelMultiProduct interface</code> </p>
<p> std::vector&lt; <code>Time</code> &gt; <code>possibleCashFlowTimes</code> () const </p>
<p> Size <code>numberOfProducts</code> () const </p>
<p> Size <code>maxNumberOfCashFlowsPerProductPerStep</code> () const </p>
<p> void <code>reset</code> ()<br />
 <i>during simulation put product at start of path </i><br />
 bool <code>nextTimeStep</code> (const <code>CurveState</code> &amp;currentState, std::vector&lt; Size &gt; &amp;numberCashFlowsThisStep, std::vector&lt; std::vector&lt; CashFlow &gt; &gt; &amp;cashFlowsGenerated)<br />
 <i>return value indicates whether path is finished, TRUE means done </i><br />
 std::auto_ptr&lt; <code>MarketModelMultiProduct</code> &gt; <code>clone</code> () const<br />
 <i>returns a newly-allocated copy of itself </i></p>
<h2>Detailed Description</h2>
<p>Price a swaption associated to a contiguous subset of rates. Useful only for testing purposes. Steps through all rate times up to start of swap. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
