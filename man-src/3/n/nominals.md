---
title: "nominals(3)"
name: "nominals"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nominals/"
description: "QuantLib::CDO – collateralized debt obligation"
---

<p>QuantLib::CDO &#8211; collateralized debt obligation </p>
<h2>Synopsis</h2>
<pre><code>CDO (Real attachment, Real detachment, const std::vector&lt; Real &gt; &amp;nominals, const std::vector&lt; Handle&lt; DefaultProbabilityTermStructure &gt; &gt; &amp;basket, const Handle&lt; OneFactorCopula &gt; &amp;copula, bool protectionSeller, const Schedule &amp;premiumSchedule, Rate premiumRate, const DayCounter &amp;dayCounter, Rate recoveryRate, Rate upfrontPremiumRate, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS, Size nBuckets, const Period &amp;integrationStep=Period(10, Years))



Real nominal ()



Real lgd ()



Real attachment ()



Real detachment ()



std::vector&lt; Real &gt; nominals ()



Size size ()



bool isExpired () const


returns whether the instrument is still tradable.


Rate fairPremium () const



Rate premiumValue () const



Rate protectionValue () const



Size error () const</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>CDO (Real attachment, Real detachment, const std::vector&lt; Real &gt; &amp;nominals, const std::vector&lt; Handle&lt; DefaultProbabilityTermStructure &gt; &gt; &amp;basket, const Handle&lt; OneFactorCopula &gt; &amp;copula, bool protectionSeller, const Schedule &amp;premiumSchedule, Rate premiumRate, const DayCounter &amp;dayCounter, Rate recoveryRate, Rate upfrontPremiumRate, const Handle&lt; YieldTermStructure &gt; &amp;yieldTS, Size nBuckets, const Period &amp;integrationStep=Period(10, Years))



Real nominal ()



Real lgd ()



Real attachment ()



Real detachment ()



std::vector&lt; Real &gt; nominals ()



Size size ()



bool isExpired () const


returns whether the instrument is still tradable.


Rate fairPremium () const



Rate premiumValue () const



Rate protectionValue () const



Size error () const</code></pre>
<h2>Detailed Description</h2>
<p>collateralized debt obligation </p>
<p> The instrument prices a mezzanine <code>CDO</code> tranche with loss given default between attachment point $ D_1$ and detachment point $ D_2 &gt; D_1 $. </p>
<p> For purchased protection, the instrument value is given by the difference of the protection value $ V_1 $ and premium value $ V_2 $, </p>
<p> [ V = V_1 &#8211; V_2. ].PP The protection leg is priced as follows: </p>
<dl>
<dt>*</p>
<dd>Build the probability distribution for volume of defaults $ L $ (before recovery) or Loss Given Default $ LGD = (1-r),L $ at times/dates $ t_i, i=1, &#8230;, N$ (premium schedule times with intermediate steps)</p>
<dt>*</p>
<dd>Determine the expected value $ E_i = E_{t_i},</p>
<hr>
<p> protection payoff $ Pay(LGD) $ at each time $ t_i$ where [ Pay(L) = min (D_1, LGD) &#8211; min (D_2, LGD) = </p>
<hr>
<p> LGD &#8211; D_1 &amp;;&amp; D_1 </p>
<hr>
<p> protection value is then calculated as [ V_1 :=: um_{i=1}^N (E_i &#8211; E_{i-1}) dot d_i ] where $ d_i$ is the discount factor at time/date $ t_i $</dl>
<p> The premium is paid on the protected notional amount, initially $ D_2 &#8211; D_1. $ This notional amount is reduced by the expected protection payments $ E_i $ at times $ t_i, $ so that the premium value is calculated as </p>
<p> [ V_2 = m , dot um_{i=1}^N ,(D_2 &#8211; D_1 &#8211; E_i) dot Delta_{i-1,i},d_i ].PPwhere $ m $ is the premium rate, $ Delta_{i-1, i}$ is the day count fraction between date/time $ t_{i-1}$ and $ t_i.$ </p>
<p> The construction of the portfolio loss distribution $ E_i $ is based on the probability bucketing algorithm described in </p>
<p> <code> John Hull and Alan White, &#8216;Valuation of a CDO</code> and nth to default CDS without Monte Carlo simulation&#8217;, Journal of Derivatives 12, 2, 2004 </p>
<p> The pricing algorithm allows for varying notional amounts and default termstructures of the underlyings. </p>
<p> <code>Possible enhancements</code></p>
<dl>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CDO</code> (<code>Real</code> attachment, <code>Real</code> detachment, const std::vector&lt; <code>Real</code> &gt; &amp; nominals, const std::vector&lt; <code>Handle</code>&lt; <code>DefaultProbabilityTermStructure</code> &gt; &gt; &amp; basket, const <code>Handle</code>&lt; <code>OneFactorCopula</code> &gt; &amp; copula, bool protectionSeller, const <code>Schedule</code> &amp; premiumSchedule, <code>Rate</code> premiumRate, const <code>DayCounter</code> &amp; dayCounter, <code>Rate</code> recoveryRate, <code>Rate</code> upfrontPremiumRate, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; yieldTS, Size nBuckets, const <code>Period</code> &amp; integrationStep = <code>Period</code>(10, Years))</h3>
<p><code>Parameters:</code></p>
<dl>
<dd><i>attachment</i> fraction of the LGD where protection starts<br />
 <i>detachment</i> fraction of the LGD where protection ends<br />
 <i>nominals</i> vector of basket nominal amounts<br />
 <i>basket</i> default basket represented by a vector of default term structures that allow computing single name default probabilities depending on time<br />
 <i>protectionSeller</i> sold protection if set to true, purchased otherwise<br />
 <i>premiumSchedule</i> schedule for premium payments<br />
 <i>premiumRate</i> annual premium rate, e.g. 0.05 for 5% p.a.<br />
 <i>dayCounter</i> day count convention for the premium rate<br />
 <i>upfrontPremiumRate</i> premium as a tranche notional fraction<br />
 <i>yieldTS</i> yield term structure handle<br />
 <i>integrationStep</i> time step for integrating over one premium period; if larger than premium period length, a single step is taken</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
