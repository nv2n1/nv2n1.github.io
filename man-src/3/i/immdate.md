---
title: "immdate(3)"
name: "immdate"
section: "3"
letter: "i"
url: "/docs/linux/man/3-immdate/"
description: "QuantLib::FuturesConvAdjustmentQuote – quote for the futures-convexity adjustment of an index"
---

<p>QuantLib::FuturesConvAdjustmentQuote &#8211; quote for the futures-convexity adjustment of an index </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/futuresconvadjustmentquote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::Observer</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FuturesConvAdjustmentQuote</code> (const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const <code>Date</code> &amp;futuresDate, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;futuresQuote, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion) </p>
<p> <code>FuturesConvAdjustmentQuote</code> (const boost::shared_ptr&lt; <code>IborIndex</code> &gt; &amp;index, const std::string &amp;immCode, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;futuresQuote, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;volatility, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;meanReversion) </p>
<p> void <code>update</code> () </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value </p>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>futuresValue</code> () const </p>
<p> <code>Real</code> <code>volatility</code> () const </p>
<p> <code>Real</code> <code>meanReversion</code> () const </p>
<p> <code>Date</code> <code>immDate</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>DayCounter</code> <code>dc_</code> </p>
<p> const <code>Date</code> <code>futuresDate_</code> </p>
<p> const <code>Date</code> <code>indexMaturityDate_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>futuresQuote_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>volatility_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>meanReversion_</code> </p>
<h2>Detailed Description</h2>
<p>quote for the futures-convexity adjustment of an index</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
