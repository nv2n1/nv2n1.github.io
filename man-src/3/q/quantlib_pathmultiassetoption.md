---
title: "quantlib_pathmultiassetoption(3)"
name: "quantlib_pathmultiassetoption"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_pathmultiassetoption/"
description: "QuantLib::PathMultiAssetOption – Base class for path-dependent options on multiple assets."
---

<p>QuantLib::PathMultiAssetOption &#8211; Base class for path-dependent options on multiple assets. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/mcbasket/pathmultiassetoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::Instrument</code>. </p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for multi-asset option calculation </i><br />
 class <code>results</code><br />
 <i>Results from multi-asset option calculation </i></p>
<h3>Public Member Functions</h3>
<p><code>PathMultiAssetOption</code> (const boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; &amp;, const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp;engine=boost::shared_ptr&lt; <code>PricingEngine</code> &gt;()) </p>
<h3>Instrument interface</h3>
<p>boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; <code>stochasticProcess_</code> </p>
<p> bool <code>isExpired</code> () const<br />
 <i>returns whether the instrument is still tradable. </i><br />
 void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> virtual boost::shared_ptr&lt; <code>PathPayoff</code> &gt; <code>pathPayoff</code> () const =0 </p>
<p> virtual std::vector&lt; <code>Date</code> &gt; <code>fixingDates</code> () const =0 </p>
<p> virtual Size <code>numberOfAssets</code> () const =0 </p>
<p> void <code>setupExpired</code> () const </p>
<h2>Detailed Description</h2>
<p>Base class for path-dependent options on multiple assets.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
