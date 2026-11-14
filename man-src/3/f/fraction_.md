---
title: "fraction_(3)"
name: "fraction_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fraction_/"
description: "QuantLib::PagodaOption – Roofed Asian option on a number of assets."
---

<h2 class="name">NAME</h2>
<p> QuantLib::PagodaOption &#8211; Roofed Asian option on a number of assets. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instruments/pagodaoption.hpp&gt; </p>
<p> Inherits <code>QuantLib::MultiAssetOption</code>. </p>
<h3>Classes</h3>
<p> class <code>engine</code><br />
 <i>Pagoda-option engine base class </i></p>
<h3>Public Member Functions</h3>
<p> <code>PagodaOption</code> (const std::vector&lt; <code>Date</code> &gt; &amp;fixingDates, <code>Real</code> roof, <code>Real</code> fraction) </p>
<p> void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<h3>Protected Attributes</h3>
<p> std::vector&lt; <code>Date</code> &gt; <code>fixingDates_</code> </p>
<p> <code>Real</code> <code>roof_</code> </p>
<p> <code>Real</code> <code>fraction_</code> </p>
<h2>Detailed Description</h2>
<p> Roofed Asian option on a number of assets. </p>
<p> The payoff is a given fraction multiplied by the minimum between a given roof and the positive portfolio performance. If the performance of the portfolio is below then the payoff is null. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> This implementation still does not manage seasoned options.</dl>
<h2>Member Function Documentation</h2>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p> When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing <code>engine</code> is used. </p>
<p> Reimplemented from <code>MultiAssetOption</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
