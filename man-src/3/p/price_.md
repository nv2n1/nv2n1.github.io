---
title: "price_(3)"
name: "price_"
section: "3"
letter: "p"
url: "/docs/linux/man/3-price_/"
description: "QuantLib::ImpliedStdDevQuote – quote for the implied standard deviation of an underlying"
---

<p>QuantLib::ImpliedStdDevQuote &#8211; quote for the implied standard deviation of an underlying </p>
<h2>Synopsis</h2>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::LazyObject</code>.</p>
<h3>Public Member Functions</h3>
<p>void performCalculations () const</p>
<p>Protected Attributes <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value</p>
<h3>Protected Member Functions</h3>
<pre><code>void performCalculations () const



Protected Attributes</code></pre>
<p> <code>Real</code> <code>impliedStdev_</code> </p>
<p> Option::Type <code>optionType_</code> </p>
<p> <code>Real</code> <code>strike_</code> </p>
<p> <code>Real</code> <code>accuracy_</code> </p>
<p> <code>Natural</code> <code>maxIter_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>forward_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>price_</code></p>
<h2>Detailed Description</h2>
<p>quote for the implied standard deviation of an underlying</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
