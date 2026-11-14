---
title: "quantlib_marketmodelevolver(3)"
name: "quantlib_marketmodelevolver"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_marketmodelevolver/"
description: "QuantLib::MarketModelEvolver – Market-model evolver."
---

<p>QuantLib::MarketModelEvolver &#8211; Market-model evolver. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolver.hpp&gt; </p>
<p> Inherited by <code>ConstrainedEvolver</code>, <code>LogNormalCmSwapRatePc</code>, <code>LogNormalCotSwapRatePc</code>, <code>LogNormalFwdRateEuler</code>, <code>LogNormalFwdRateIpc</code>, <code>LogNormalFwdRatePc</code>, <code>NormalFwdRatePc</code>, and <code>SVDDFwdRatePc</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual const std::vector&lt; Size &gt; &amp; <code>numeraires</code> () const =0 </p>
<p> virtual <code>Real</code> <code>startNewPath</code> ()=0 </p>
<p> virtual <code>Real</code> <code>advanceStep</code> ()=0 </p>
<p> virtual Size <code>currentStep</code> () const =0 </p>
<p> virtual const <code>CurveState</code> &amp; <code>currentState</code> () const =0 </p>
<p> virtual void <code>setInitialState</code> (const <code>CurveState</code> &amp;)=0 </p>
<h2>Detailed Description</h2>
<p>Market-model evolver. </p>
<p> Abstract base class. The evolver does the actual gritty work of evolving the forward rates from one time to the next. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
