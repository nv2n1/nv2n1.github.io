---
title: "isvalid(3)"
name: "isvalid"
section: "3"
letter: "i"
url: "/docs/linux/man/3-isvalid/"
description: "QuantLib::Quote – purely virtual base class for market observables"
---

<p>QuantLib::Quote &#8211; purely virtual base class for market observables </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>CompositeQuote&lt; BinaryFunction &gt;</code>, <code>DerivedQuote&lt; UnaryFunction &gt;</code>, <code>EurodollarFuturesImpliedStdDevQuote</code>, <code>ForwardSwapQuote</code>, <code>ForwardValueQuote</code>, <code>FuturesConvAdjustmentQuote</code>, <code>ImpliedStdDevQuote</code>, <code>LastFixingQuote</code>, and <code>SimpleQuote</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual <code>Real</code> <code>value</code> () const =0<br />
 <i>returns the current value </i><br />
 virtual bool <code>isValid</code> () const =0<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value</p>
<h2>Detailed Description</h2>
<p>purely virtual base class for market observables </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the observability of class instances is tested.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
