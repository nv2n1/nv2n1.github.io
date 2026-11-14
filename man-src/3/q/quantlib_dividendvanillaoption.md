---
title: "quantlib_dividendvanillaoption(3)"
name: "quantlib_dividendvanillaoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dividendvanillaoption/"
description: "QuantLib::DividendVanillaOption – Single-asset vanilla option (no barriers) with discrete dividends."
---

<p>QuantLib::DividendVanillaOption &#8211; Single-asset vanilla option (no barriers) with discrete dividends. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/instruments/dividendvanillaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneAssetOption</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for dividend vanilla option calculation </i><br />
 class <code>engine</code><br />
 <i>Dividend-vanilla-option engine base class </i></p>
<h3>Public Member Functions</h3>
<p><code>DividendVanillaOption</code> (const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise, const std::vector&lt; <code>Date</code> &gt; &amp;dividendDates, const std::vector&lt; <code>Real</code> &gt; &amp;dividends) </p>
<p> <code>Volatility</code> <code>impliedVolatility</code> (<code>Real</code> price, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;process, <code>Real</code> accuracy=1.0e-4, Size maxEvaluations=100, Volatility minVol=1.0e-7, Volatility maxVol=4.0) const </p>
<h3>Protected Member Functions</h3>
<p>void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h2>Detailed Description</h2>
<p>Single-asset vanilla option (no barriers) with discrete dividends. </p>
<h2>Member Function Documentation</h2>
<h3><code>Volatility</code> impliedVolatility (<code>Real</code> price, const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp; process, <code>Real</code> accuracy = 1.0e-4, Size maxEvaluations = 100, <code>Volatility</code> minVol = 1.0e-7, <code>Volatility</code> maxVol = 4.0) const</h3>
<p><code>Warning</code></p>
<dl COMPACT>
<dd>see <code>VanillaOption</code> for notes on implied-volatility calculation.</dl>
<h3>void setupArguments (PricingEngine::arguments *) const [protected, virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Option</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
