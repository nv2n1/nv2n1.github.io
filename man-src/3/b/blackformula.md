---
title: "blackformula(3)"
name: "blackformula"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blackformula/"
description: "ql/pricingengines/blackformula.hpp – Black formula."
---

<h2 class="name">NAME</h2>
<p> ql/pricingengines/blackformula.hpp &#8211; Black formula. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/option.hpp&gt;<br />
 #include &lt;ql/instruments/payoffs.hpp&gt; </p>
<h3>Functions</h3>
<p> Real <code>blackFormula</code> (Option::Type optionType, Real strike, Real forward, Real stdDev, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormula</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real stdDev, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormulaImpliedStdDevApproximation</code> (Option::Type optionType, Real strike, Real forward, Real blackPrice, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormulaImpliedStdDevApproximation</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real blackPrice, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormulaImpliedStdDev</code> (Option::Type optionType, Real strike, Real forward, Real blackPrice, Real discount=1.0, Real displacement=0.0, Real guess=Null&lt; Real &gt;(), Real accuracy=1.0e-6, Natural maxIterations=100) </p>
<p> Real <code>blackFormulaImpliedStdDev</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real blackPrice, Real discount=1.0, Real displacement=0.0, Real guess=Null&lt; Real &gt;(), Real accuracy=1.0e-6, Natural maxIterations=100) </p>
<p> Real <code>blackFormulaCashItmProbability</code> (Option::Type optionType, Real strike, Real forward, Real stdDev, Real displacement=0.0) </p>
<p> Real <code>blackFormulaCashItmProbability</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real stdDev, Real displacement=0.0) </p>
<p> Real <code>blackFormulaStdDevDerivative</code> (Real strike, Real forward, Real stdDev, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormulaVolDerivative</code> (Real strike, Real forward, Real stdDev, Real expiry, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>blackFormulaStdDevDerivative</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real stdDev, Real discount=1.0, Real displacement=0.0) </p>
<p> Real <code>bachelierBlackFormula</code> (Option::Type optionType, Real strike, Real forward, Real stdDev, Real discount=1.0) </p>
<p> Real <code>bachelierBlackFormula</code> (const boost::shared_ptr&lt; PlainVanillaPayoff &gt; &amp;payoff, Real forward, Real stdDev, Real discount=1.0) </p>
<h2>Detailed Description</h2>
<p> Black formula. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
