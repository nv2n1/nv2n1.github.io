---
title: "nthtodefault(3)"
name: "nthtodefault"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nthtodefault/"
description: "QuantLib::NthToDefault – N-th to default swap."
---

<p>QuantLib::NthToDefault &#8211; N-th to default swap. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/nthtodefault.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Public Member Functions</h3>
<p><code>NthToDefault</code> (Size n, const std::vector&lt; Issuer &gt; &amp;basket, const <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; &amp;copula, Protection::Side side, <code>Real</code> nominal, const <code>Schedule</code> &amp;premiumSchedule, <code>Rate</code> premiumRate, const <code>DayCounter</code> &amp;dayCounter, bool settlePremiumAccrual, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS, const <code>Period</code> &amp;integrationStepSize, boost::shared_ptr&lt; <code>Claim</code> &gt; claim=boost::shared_ptr&lt; <code>Claim</code> &gt;()) </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 <code>Rate</code> <code>fairPremium</code> () const </p>
<p> <code>Rate</code> <code>premium</code> () const </p>
<p> <code>Real</code> <code>nominal</code> () const </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const </p>
<p> Protection::Side <code>side</code> () const </p>
<p> Size <code>rank</code> () const </p>
<p> Size <code>basketSize</code> () const </p>
<h2>Detailed Description</h2>
<p>N-th to default swap. </p>
<p> A NTD instrument exchanges protection against the nth default in a basket of underlying credits for premium payments based on the protected notional amount. </p>
<p> The pricing is analogous to the pricing of a CDS instrument which represents protection against default of a single underlying credit. The only difference is the calculation of the probability of default. In the CDS case, it is the probabilty of single name default; in the NTD case the probability of at least N defaults in the portfolio of underlying credits. </p>
<p> This probability is computed using the algorithm in John Hull and Alan White, &#8216;Valuation of a <code>CDO</code> and nth to default CDS without Monte Carlo simulation&#8217;, Journal of Derivatives 12, 2, 2004. </p>
<p> The algorithm allows for varying probability of default across the basket. Otherwise, for identical probabilities of default, the probability of n defaults is given by the binomial distribution. </p>
<p> Default correlation is modeled using a one-factor Gaussian copula approach. </p>
<p> The class is tested against data in Hull-White (see reference above.) </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
