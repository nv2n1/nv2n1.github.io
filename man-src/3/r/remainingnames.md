---
title: "remainingnames(3)"
name: "remainingnames"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remainingnames/"
description: "QuantLib::Basket –"
---

<p>QuantLib::Basket &#8211;</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/experimental/credit/basket.hpp&gt;</code></pre>
<h3>Public Member Functions</h3>
<pre><code>Basket (const std::vector&lt; std::string &gt; &amp;names, const std::vector&lt; Real &gt; &amp;notionals, const boost::shared_ptr&lt; Pool &gt; pool, Real attachmentRatio=0.0, Real detachmentRatio=1.0)



Size size () const



const std::vector&lt; std::string &gt; &amp; names () const



const std::vector&lt; Real &gt; &amp; notionals () const



Real notional ()



boost::shared_ptr&lt; Pool &gt; pool () const



const std::vector&lt; Real &gt; &amp; LGDs () const



Real lgd ()



Real attachmentRatio () const



Real detachmentRatio () const



Real basketNotional () const



Real basketLGD () const



Real trancheNotional () const



Real attachmentAmount () const



Real detachmentAmount () const



std::vector&lt; Real &gt; probabilities (const Date &amp;d) const



Real cumulatedLoss (const Date &amp;startDate, const Date &amp;endDate) const



Real remainingNotional (const Date &amp;startDate, const Date &amp;endDate) const



std::vector&lt; Real &gt; remainingNotionals (const Date &amp;startDate, const Date &amp;endDate) const



std::vector&lt; std::string &gt; remainingNames (const Date &amp;startDate, const Date &amp;endDate) const



Real remainingAttachmentRatio (const Date &amp;startDate, const Date &amp;endDate) const



Real remainingAttachmentAmount (const Date &amp;startDate, const Date &amp;endDate) const



Real remainingDetachmentRatio (const Date &amp;startDate, const Date &amp;endDate) const



Real remainingDetachmentAmount (const Date &amp;startDate, const Date &amp;endDate) const



void updateScenarioLoss (bool zeroRecovery=false)



Real scenarioTrancheLoss (Date endDate) const



std::vector&lt; Loss &gt; scenarioIncrementalBasketLosses () const



std::vector&lt; Loss &gt; scenarioIncrementalTrancheLosses (Date startDate=Date::minDate(), Date endDate=Date::maxDate()) const</code></pre>
<h2>Detailed Description</h2>
<p>Credit <code>Basket</code> A basket is a collection of credit names, represented by a unique identifier (a text string), associated notional amounts, a pool and tranche information. The pool is a map of &#8216;names&#8217; to issuers. The <code>Basket</code> structure is motivated by <code>CDO</code> squared instruments containing various underlying inner CDOs which can be represented by respective baskets including their tranche structure. The role of the Pool is providing a unique list of relevant issuers while names may appear multiple times across different baskets (overlap).</p>
<h2>Member Function Documentation</h2>
<h3>const std::vector&lt;<code>Real</code>&gt;&amp; LGDs () const</h3>
<p>Loss Given Default for all issuers/notionals based on expected recovery rates for the respective issuers.</p>
<h3><code>Real</code> attachmentRatio () const</h3>
<p>Attachment point expressed as a fraction of the total pool notional.</p>
<h3><code>Real</code> detachmentRatio () const</h3>
<p>Detachment point expressed as a fraction of the total pool notional.</p>
<h3><code>Real</code> basketNotional () const</h3>
<p>Original basket notional ignoring any losses.</p>
<h3><code>Real</code> basketLGD () const</h3>
<p>Original expected basket LGD.</p>
<h3><code>Real</code> trancheNotional () const</h3>
<p>Original tranche notional ignoring any losses.</p>
<h3><code>Real</code> attachmentAmount () const</h3>
<p>Attachment amount = <code>attachmentRatio()</code> * <code>basketNotional()</code></p>
<h3><code>Real</code> detachmentAmount () const</h3>
<p>Detachment amount = <code>detachmentRatio()</code> * <code>basketNotional()</code></p>
<h3>std::vector&lt;<code>Real</code>&gt; probabilities (const <code>Date</code> &amp; d) const</h3>
<p>Vector of cumulative default probability to date d for al issuers in the basket.</p>
<h3><code>Real</code> cumulatedLoss (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>Actual basket losses between start and end date, taking the actual recovery rates of loss events into account.</p>
<h3><code>Real</code> remainingNotional (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>Remaining basket notional after losses between start and end date. The full notional for defaulted names is subracted, recovery ignored.</p>
<h3>std::vector&lt;<code>Real</code>&gt; remainingNotionals (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>Vector of surviving notionals after losses between start and end date, recovery ignored.</p>
<h3>std::vector&lt;std::string&gt; remainingNames (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>Vector of surviving issuers after defaults between start and end date.</p>
<h3><code>Real</code> remainingAttachmentRatio (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>The remaining attachment amount is RAA = max (0, attachmentAmount &#8211; <code>cumulatedLoss()</code>) </p>
<p> The remaining attachment ratio is then RAR = RAA / <code>remainingNotional()</code></p>
<h3><code>Real</code> remainingDetachmentRatio (const <code>Date</code> &amp; startDate, const <code>Date</code> &amp; endDate) const</h3>
<p>The remaining detachment amount is RDA = max (0, detachmentAmount &#8211; <code>cumulatedLoss()</code>) </p>
<p> The remaining detachment ratio is then RDR = RDA / <code>remainingNotional()</code></p>
<h3>void updateScenarioLoss (bool zeroRecovery = false)</h3>
<p>Based on the default times stored in the Pool for each name, update the vector of incremental basket losses (sorted by default time) for this basket. If zeroRecovery is set to true, losses are full notional amounts, otherwise loss give defaults.</p>
<h3><code>Real</code> scenarioTrancheLoss (<code>Date</code> endDate) const</h3>
<p>Cumulative tranche loss up to end date under the current scenario</p>
<h3>std::vector&lt;Loss&gt; scenarioIncrementalBasketLosses () const</h3>
<p>Vector of incremental basket losses under the current scenario</p>
<h3>std::vector&lt;Loss&gt; scenarioIncrementalTrancheLosses (<code>Date</code> startDate = Date::minDate(), <code>Date</code> endDate = Date::maxDate()) const</h3>
<p>Vector of incremental tranche losses under the current scenario</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
