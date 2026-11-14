---
title: "simplequote(3)"
name: "simplequote"
section: "3"
letter: "s"
url: "/docs/linux/man/3-simplequote/"
description: "QuantLib::SimpleQuote – market element returning a stored value"
---

<p>QuantLib::SimpleQuote &#8211; market element returning a stored value </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/simplequote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SimpleQuote</code> (Real value=<code>Null</code>&lt; Real &gt;()) </p>
<p> <code>Quote interface</code> </p>
<p> Real <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value </p>
<p> <code>Modifiers</code> </p>
<p> Real <code>setValue</code> (Real value=<code>Null</code>&lt; Real &gt;())<br />
 <i>returns the difference between the new value and the old value </i><br />
 void <code>reset</code> () </p>
<h2>Detailed Description</h2>
<p>market element returning a stored value </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>, <code>Bonds.cpp</code>, <code>CallableBonds.cpp</code>, <code>CDS.cpp</code>, <code>ConvertibleBonds.cpp</code>, <code>DiscreteHedging.cpp</code>, <code>EquityOption.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, <code>Replication.cpp</code>, and <code>swapvaluation.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
