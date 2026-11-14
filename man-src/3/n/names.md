---
title: "names(3)"
name: "names"
section: "3"
letter: "n"
url: "/docs/linux/man/3-names/"
description: "QuantLib::Basket –"
---

<p>QuantLib::Basket &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/basket.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Basket</code> (const std::vector&lt; std::string &gt; &amp;names, const std::vector&lt; <code>Real</code> &gt; &amp;notionals, const boost::shared_ptr&lt; Pool &gt; pool, <code>Real</code> attachmentRatio=0.0, <code>Real</code> detachmentRatio=1.0) </p>
<p> Size <code>size</code> () const </p>
<p> const std::vector&lt; std::string &gt; &amp; <code>names</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>notionals</code> () const </p>
<p> <code>Real</code> <code>notional</code> () </p>
<p> boost::shared_ptr&lt; Pool &gt; <code>pool</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>LGDs</code> () const </p>
<p> <code>Real</code> <code>lgd</code> () </p>
<p> <code>Real</code> <code>attachmentRatio</code> () const </p>
<p> <code>Real</code> <code>detachmentRatio</code> () const </p>
<p> <code>Real</code> <code>basketNotional</code> () const </p>
<p> <code>Real</code> <code>basketLGD</code> () const </p>
<p> <code>Real</code> <code>trancheNotional</code> () const </p>
<p> <code>Real</code> <code>attachmentAmount</code> () const </p>
<p> <code>Real</code> <code>detachmentAmount</code> () const </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>probabilities</code> (const <code>Date</code> &amp;d) const </p>
<p> <code>Real</code> <code>cumulatedLoss</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> <code>Real</code> <code>remainingNotional</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> std::vector&lt; <code>Real</code> &gt; <code>remainingNotionals</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> std::vector&lt; std::string &gt; <code>remainingNames</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> <code>Real</code> <code>remainingAttachmentRatio</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> <code>Real</code> <code>remainingAttachmentAmount</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> <code>Real</code> <code>remainingDetachmentRatio</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> <code>Real</code> <code>remainingDetachmentAmount</code> (const <code>Date</code> &amp;startDate, const <code>Date</code> &amp;endDate) const </p>
<p> void <code>updateScenarioLoss</code> (bool zeroRecovery=false) </p>
<p> <code>Real</code> <code>scenarioTrancheLoss</code> (<code>Date</code> endDate) const </p>
<p> std::vector&lt; Loss &gt; <code>scenarioIncrementalBasketLosses</code> () const </p>
<p> std::vector&lt; Loss &gt; <code>scenarioIncrementalTrancheLosses</code> (<code>Date</code> startDate=Date::minDate(), <code>Date</code> endDate=Date::maxDate()) const </p>
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
<p>Vector of incremental tranche losses under the current scenario </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
