---
title: "fairupfrontpremium(3)"
name: "fairupfrontpremium"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fairupfrontpremium/"
description: "QuantLib::SyntheticCDO – Synthetic Collateralized Debt Obligation."
---

<p>QuantLib::SyntheticCDO &#8211; Synthetic Collateralized Debt Obligation. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/syntheticcdo.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Classes</h3>
<p>class <code>engine</code><br />
 <i></i><code>CDO</code> base <code>engine</code>.</p>
<h3>Public Member Functions</h3>
<p><code>SyntheticCDO</code> (const boost::shared_ptr&lt; <code>Basket</code> &gt; basket, Protection::Side side, const <code>Schedule</code> &amp;schedule, <code>Rate</code> upfrontRate, <code>Rate</code> runningRate, const <code>DayCounter</code> &amp;dayCounter, <code>BusinessDayConvention</code> paymentConvention, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;yieldTS) </p>
<p> boost::shared_ptr&lt; <code>Basket</code> &gt; <code>basket</code> () const </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 <code>Rate</code> <code>fairPremium</code> () const </p>
<p> <code>Rate</code> <code>fairUpfrontPremium</code> () const </p>
<p> <code>Rate</code> <code>premiumValue</code> () const </p>
<p> <code>Rate</code> <code>protectionValue</code> () const </p>
<p> Real <code>remainingNotional</code> () const </p>
<p> std::vector&lt; Real &gt; <code>expectedTrancheLoss</code> () const </p>
<p> Size <code>error</code> () const </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<h2>Detailed Description</h2>
<p>Synthetic Collateralized Debt Obligation. </p>
<p> The instrument prices a mezzanine <code>CDO</code> tranche with loss given default between attachment point $ D_1$ and detachment point $ D_2 &gt; D_1 $. </p>
<p> For purchased protection, the instrument value is given by the difference of the protection value $ V_1 $ and premium value $ V_2 $, </p>
<p> [ V = V_1 &#8211; V_2. ].PP The protection leg is priced as follows: </p>
<dl COMPACT>
<dt>*</p>
<dd>Build the probability distribution for volume of defaults $ L $ (before recovery) or Loss Given Default $ LGD = (1-r),L $ at times/dates $ t_i, i=1, &#8230;, N$ (premium schedule times with intermediate steps)</dl>
<dl COMPACT>
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
<dl COMPACT>
<dd>Investigate and fix cases $ E_{i+1} &lt; E_i. $</dl>
<h2>Member Function Documentation</h2>
<h3>Real remainingNotional () const</h3>
<p>Total outstanding tranche notional, not wiped out</p>
<h3>std::vector&lt;Real&gt; expectedTrancheLoss () const</h3>
<p>Expected tranche loss for all payment dates</p>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p>When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
