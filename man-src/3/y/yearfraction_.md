---
title: "yearfraction_(3)"
name: "yearfraction_"
section: "3"
letter: "y"
url: "/docs/linux/man/3-yearfraction_/"
description: "QuantLib::GarmanKlassAbstract – Garman-Klass volatility model."
---

<p>QuantLib::GarmanKlassAbstract &#8211; Garman-Klass volatility model. </p>
<h2>Synopsis</h2>
<pre><code>virtual Real calculatePoint (const IntervalPrice &amp;p)=0



Protected Attributes</code></pre>
<p> Inherits QuantLib::LocalVolatilityEstimator&lt;IntervalPrice&gt;. Inherited by GarmanKlassSigma4, GarmanKlassSigma5, GarmanKlassSimpleSigma, and ParkinsonSigma.</p>
<h3>Public Member Functions</h3>
<p><code>GarmanKlassAbstract</code> (<code>Real</code> y) </p>
<p> <code>TimeSeries</code>&lt; <code>Volatility</code> &gt; <code>calculate</code> (const <code>TimeSeries</code>&lt; <code>IntervalPrice</code> &gt; &amp;quoteSeries)</p>
<h3>Protected Member Functions</h3>
<pre><code>virtual Real calculatePoint (const IntervalPrice &amp;p)=0



Protected Attributes</code></pre>
<p> <code>Real</code> <code>yearFraction_</code></p>
<h2>Detailed Description</h2>
<p>Garman-Klass volatility model. </p>
<p> This class implements a concrete volatility model based on high low formulas using the method of Garman and Klass in their paper &#8216;On the Estimation of the Security Price from Historical Data&#8217; at <a rel="nofollow" href="http://www.fea.com/resources/pdf/a_estimation_of_security_price.pdf">http://www.fea.com/resources/pdf/a_estimation_of_security_price.pdf</a> </p>
<p> Volatilities are assumed to be expressed on an annual basis.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
