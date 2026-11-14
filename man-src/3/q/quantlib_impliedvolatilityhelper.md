---
title: "quantlib_impliedvolatilityhelper(3)"
name: "quantlib_impliedvolatilityhelper"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_impliedvolatilityhelper/"
description: "QuantLib::ImpliedVolatilityHelper – helper class for one-asset implied-volatility calculation"
---

<p>QuantLib::ImpliedVolatilityHelper &#8211; helper class for one-asset implied-volatility calculation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/impliedvolatility.hpp&gt; </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Volatility</code> <code>calculate</code> (const <code>Instrument</code> &amp;instrument, const <code>PricingEngine</code> &amp;engine, <code>SimpleQuote</code> &amp;volQuote, <code>Real</code> targetValue, <code>Real</code> accuracy, <code>Natural</code> maxEvaluations, <code>Volatility</code> minVol, <code>Volatility</code> maxVol) </p>
<p> static boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>clone</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, const boost::shared_ptr&lt; <code>SimpleQuote</code> &gt; &amp;volQuote) </p>
<h2>Detailed Description</h2>
<p>helper class for one-asset implied-volatility calculation </p>
<p> The passed engine must be linked to the passed quote (see, e.g., <code>VanillaOption</code> to see how this can be achieved.)</p>
<h2>Member Function Documentation</h2>
<h3>static boost::shared_ptr&lt;<code>GeneralizedBlackScholesProcess</code>&gt; clone (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp; process, const boost::shared_ptr&lt; <code>SimpleQuote</code> &gt; &amp; volQuote) [static]</h3>
<p>The returned process is equal to the passed one, except for the volatility which is flat and whose value is driven by the passed quote. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
