---
title: "earliestdate(3)"
name: "earliestdate"
section: "3"
letter: "e"
url: "/docs/linux/man/3-earliestdate/"
description: "QuantLib::BootstrapHelper – Base helper class for bootstrapping."
---

<p>QuantLib::BootstrapHelper &#8211; Base helper class for bootstrapping. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/bootstraphelper.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>RelativeDateRateHelper</code>. </p>
<h3>Public Member Functions</h3>
<p><code>BootstrapHelper</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;quote) </p>
<p> <code>BootstrapHelper</code> (Real quote) </p>
<p> <code>BootstrapHelper interface</code> </p>
<p> Real <code>quoteError</code> () const </p>
<p> Real <code>quoteValue</code> () const </p>
<p> bool <code>quoteIsValid</code> () const </p>
<p> virtual Real <code>impliedQuote</code> () const =0 </p>
<p> virtual void <code>setTermStructure</code> (TS *)<br />
 <i>sets the term structure to be used for pricing </i><br />
 virtual <code>Date</code> <code>earliestDate</code> () const<br />
 <i>earliest relevant date </i><br />
 virtual <code>Date</code> <code>latestDate</code> () const<br />
 <i>latest relevant date </i> </p>
<p> <code>Observer interface</code> </p>
<p> virtual void <code>update</code> () </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Handle</code>&lt; <code>Quote</code> &gt; <code>quote_</code> </p>
<p> TS * <code>termStructure_</code> </p>
<p> <code>Date</code> <code>earliestDate_</code> </p>
<p> <code>Date</code> <code>latestDate_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class TS&gt; class QuantLib::BootstrapHelper&lt; TS &gt;</h3>
<p>Base helper class for bootstrapping. </p>
<p> This class provides an abstraction for the instruments used to bootstrap a term structure. </p>
<p> It is advised that a bootstrap helper for an instrument contains an instance of the actual instrument class to ensure consistancy between the algorithms used during bootstrapping and later instrument pricing. This is not yet fully enforced in the available rate helpers.</p>
<h2>Member Function Documentation</h2>
<h3>void setTermStructure (TS * t) [virtual]</h3>
<p>sets the term structure to be used for pricing </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>Being a pointer and not a shared_ptr, the term structure is not guaranteed to remain allocated for the whole life of the rate helper. It is responsibility of the programmer to ensure that the pointer remains valid. It is advised that this method is called only inside the term structure being bootstrapped, setting the pointer to <code>this</code>, i.e., the term structure itself.</dl>
<p> Reimplemented in <code>CdsHelper</code>, <code>ZciisInflationHelper</code>, <code>YyiisInflationHelper</code>, and <code>FixedRateBondHelper</code>.</p>
<h3><code>Date</code> earliestDate () const [virtual]</h3>
<p>earliest relevant date </p>
<p> The earliest date at which data are needed by the helper in order to provide a quote.</p>
<h3><code>Date</code> latestDate () const [virtual]</h3>
<p>latest relevant date </p>
<p> The latest date at which data are needed by the helper in order to provide a quote. It does not necessarily equal the maturity of the underlying instrument.</p>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>RelativeDateRateHelper</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
