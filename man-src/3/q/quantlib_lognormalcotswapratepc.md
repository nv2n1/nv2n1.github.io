---
title: "quantlib_lognormalcotswapratepc(3)"
name: "quantlib_lognormalcotswapratepc"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_lognormalcotswapratepc/"
description: "QuantLib::LogNormalCotSwapRatePc – Predictor-Corrector."
---

<p>QuantLib::LogNormalCotSwapRatePc &#8211; Predictor-Corrector. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolvers/lognormalcotswapratepc.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelEvolver</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LogNormalCotSwapRatePc</code> (const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;, const BrownianGeneratorFactory &amp;, const std::vector&lt; Size &gt; &amp;numeraires, Size initialStep=0) </p>
<p> <code>MarketModel interface</code> </p>
<p> const std::vector&lt; Size &gt; &amp; <code>numeraires</code> () const </p>
<p> <code>Real</code> <code>startNewPath</code> () </p>
<p> <code>Real</code> <code>advanceStep</code> () </p>
<p> Size <code>currentStep</code> () const </p>
<p> const <code>CurveState</code> &amp; <code>currentState</code> () const </p>
<p> void <code>setInitialState</code> (const <code>CurveState</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Predictor-Corrector. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
