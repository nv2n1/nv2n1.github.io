---
title: "quantlib_svddfwdratepc(3)"
name: "quantlib_svddfwdratepc"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_svddfwdratepc/"
description: "QuantLib::SVDDFwdRatePc –"
---

<p>QuantLib::SVDDFwdRatePc &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolvers/svddfwdratepc.hpp&gt; </p>
<p> Inherits <code>QuantLib::MarketModelEvolver</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SVDDFwdRatePc</code> (const boost::shared_ptr&lt; <code>MarketModel</code> &gt; &amp;, const BrownianGeneratorFactory &amp;, const boost::shared_ptr&lt; <code>MarketModelVolProcess</code> &gt; &amp;volProcess, Size firstVolatilityFactor, Size volatilityFactorStep, const std::vector&lt; Size &gt; &amp;numeraires, Size initialStep=0) </p>
<p> <code>MarketModel interface</code> </p>
<p> const std::vector&lt; Size &gt; &amp; <code>numeraires</code> () const </p>
<p> <code>Real</code> <code>startNewPath</code> () </p>
<p> <code>Real</code> <code>advanceStep</code> () </p>
<p> Size <code>currentStep</code> () const </p>
<p> const <code>CurveState</code> &amp; <code>currentState</code> () const </p>
<p> void <code>setInitialState</code> (const <code>CurveState</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Displaced diffusion LMM with uncorrelated vol process. Called &#8216;Shifted BGM&#8217; with Heston vol by Brac in &#8216;Engineering BGM.&#8217; Vol process is an external input. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
