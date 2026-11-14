---
title: "premium(3)"
name: "premium"
section: "3"
letter: "p"
url: "/docs/linux/man/3-premium/"
description: "QuantLib::NthToDefault – N-th to default swap."
---

<p>QuantLib::NthToDefault &#8211; N-th to default swap. </p>
<h2>Synopsis</h2>
<pre><code>NthToDefault (Size n, const std::vector&lt; Issuer &gt; &amp;basket, const Handle&lt; OneFactorCopula &gt; &amp;copula, Protection::Side side, Real nominal, const Schedule &amp;premiumSchedule, Rate premiumRate, const DayCounter &amp;dayCounter, bool settlePremiumAccrual, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS, const Period &amp;integrationStepSize, boost::shared_ptr&lt; Claim &gt; claim=boost::shared_ptr&lt; Claim &gt;())



bool isExpired () const


returns whether the instrument is still tradable.


Rate fairPremium () const



Rate premium () const



Real nominal () const



DayCounter dayCounter () const



Protection::Side side () const



Size rank () const



Size basketSize () const</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>NthToDefault (Size n, const std::vector&lt; Issuer &gt; &amp;basket, const Handle&lt; OneFactorCopula &gt; &amp;copula, Protection::Side side, Real nominal, const Schedule &amp;premiumSchedule, Rate premiumRate, const DayCounter &amp;dayCounter, bool settlePremiumAccrual, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS, const Period &amp;integrationStepSize, boost::shared_ptr&lt; Claim &gt; claim=boost::shared_ptr&lt; Claim &gt;())



bool isExpired () const


returns whether the instrument is still tradable.


Rate fairPremium () const



Rate premium () const



Real nominal () const



DayCounter dayCounter () const



Protection::Side side () const



Size rank () const



Size basketSize () const</code></pre>
<h2>Detailed Description</h2>
<p>N-th to default swap. </p>
<p> A NTD instrument exchanges protection against the nth default in a basket of underlying credits for premium payments based on the protected notional amount. </p>
<p> The pricing is analogous to the pricing of a CDS instrument which represents protection against default of a single underlying credit. The only difference is the calculation of the probability of default. In the CDS case, it is the probabilty of single name default; in the NTD case the probability of at least N defaults in the portfolio of underlying credits. </p>
<p> This probability is computed using the algorithm in John Hull and Alan White, &#8216;Valuation of a <code>CDO</code> and nth to default CDS without Monte Carlo simulation&#8217;, Journal of Derivatives 12, 2, 2004. </p>
<p> The algorithm allows for varying probability of default across the basket. Otherwise, for identical probabilities of default, the probability of n defaults is given by the binomial distribution. </p>
<p> Default correlation is modeled using a one-factor Gaussian copula approach. </p>
<p> The class is tested against data in Hull-White (see reference above.)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
