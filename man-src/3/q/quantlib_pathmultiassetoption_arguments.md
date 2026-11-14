---
title: "quantlib_pathmultiassetoption_arguments(3)"
name: "quantlib_pathmultiassetoption_arguments"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathmultiassetoption_arguments/"
description: "QuantLib::PathMultiAssetOption::arguments – Arguments for multi-asset option calculation"
---

<p>QuantLib::PathMultiAssetOption::arguments &#8211; Arguments for multi-asset option calculation </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/mcbasket/pathmultiassetoption.hpp&gt; </p>
<p> Inherits QuantLib::PricingEngine::arguments. </p>
<h3>Public Member Functions</h3>
<p>void <code>validate</code> () const </p>
<h3>Public Attributes</h3>
<p>boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; <code>stochasticProcess</code> </p>
<p> boost::shared_ptr&lt; <code>PathPayoff</code> &gt; <code>payoff</code> </p>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixingDates</code> </p>
<h2>Detailed Description</h2>
<p>Arguments for multi-asset option calculation </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
