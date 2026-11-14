---
title: "stochasticprocess_(3)"
name: "stochasticprocess_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stochasticprocess_/"
description: "QuantLib::PathMultiAssetOption – Base class for path-dependent options on multiple assets."
---

<p>QuantLib::PathMultiAssetOption &#8211; Base class for path-dependent options on multiple assets. </p>
<h2>Synopsis</h2>
<pre><code>PathMultiAssetOption (const boost::shared_ptr&lt; StochasticProcess &gt; &amp;, const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine=boost::shared_ptr&lt; PricingEngine &gt;())



Instrument interface
boost::shared_ptr&lt; StochasticProcess &gt; stochasticProcess_



bool isExpired () const


returns whether the instrument is still tradable.


void setupArguments (PricingEngine::arguments *) const



virtual boost::shared_ptr&lt; PathPayoff &gt; pathPayoff () const =0



virtual std::vector&lt; Date &gt; fixingDates () const =0



virtual Size numberOfAssets () const =0



void setupExpired () const</code></pre>
<p> Inherits <code>QuantLib::Instrument</code>.</p>
<h3>Classes</h3>
<p>class <code>arguments</code><br />
 <i>Arguments for multi-asset option calculation </i><br />
 class <code>results</code><br />
 <i>Results from multi-asset option calculation </i></p>
<h3>Public Member Functions</h3>
<pre><code>PathMultiAssetOption (const boost::shared_ptr&lt; StochasticProcess &gt; &amp;, const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine=boost::shared_ptr&lt; PricingEngine &gt;())



Instrument interface
boost::shared_ptr&lt; StochasticProcess &gt; stochasticProcess_



bool isExpired () const


returns whether the instrument is still tradable.


void setupArguments (PricingEngine::arguments *) const



virtual boost::shared_ptr&lt; PathPayoff &gt; pathPayoff () const =0



virtual std::vector&lt; Date &gt; fixingDates () const =0



virtual Size numberOfAssets () const =0



void setupExpired () const</code></pre>
<h2>Detailed Description</h2>
<p>Base class for path-dependent options on multiple assets.</p>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p>When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p>This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented from <code>Instrument</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
