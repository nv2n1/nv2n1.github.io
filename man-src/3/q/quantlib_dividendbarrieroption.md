---
title: "quantlib_dividendbarrieroption(3)"
name: "quantlib_dividendbarrieroption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dividendbarrieroption/"
description: "QuantLib::DividendBarrierOption – Single-asset barrier option with discrete dividends."
---

<p>QuantLib::DividendBarrierOption &#8211; Single-asset barrier option with discrete dividends. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/finitedifferences/dividendbarrieroption.hpp&gt; </p>
<p> Inherits <code>QuantLib::BarrierOption</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for dividend barrier option calculation </i><br />
 class <code>engine</code><br />
 <i>Dividend-barrier-option engine base class </i></p>
<h3>Public Member Functions</h3>
<p><code>DividendBarrierOption</code> (Barrier::Type barrierType, <code>Real</code> barrier, <code>Real</code> rebate, const boost::shared_ptr&lt; <code>StrikedTypePayoff</code> &gt; &amp;payoff, const boost::shared_ptr&lt; <code>Exercise</code> &gt; &amp;exercise, const std::vector&lt; <code>Date</code> &gt; &amp;dividendDates, const std::vector&lt; <code>Real</code> &gt; &amp;dividends) </p>
<h3>Protected Member Functions</h3>
<p>void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h2>Detailed Description</h2>
<p>Single-asset barrier option with discrete dividends. </p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [protected, virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>BarrierOption</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
