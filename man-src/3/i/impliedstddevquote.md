---
title: "impliedstddevquote(3)"
name: "impliedstddevquote"
section: "3"
letter: "i"
url: "/docs/linux/man/3-impliedstddevquote/"
description: "QuantLib::ImpliedStdDevQuote – quote for the implied standard deviation of an underlying"
---

<p>QuantLib::ImpliedStdDevQuote &#8211; quote for the implied standard deviation of an underlying </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/quotes/impliedstddevquote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ImpliedStdDevQuote</code> (Option::Type optionType, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;forward, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;price, <code>Real</code> strike, <code>Real</code> guess, <code>Real</code> accuracy=1.0e-6, Natural maxIter=100) </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value</p>
<h3>Protected Member Functions</h3>
<p>void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p><code>Real</code> <code>impliedStdev_</code> </p>
<p> Option::Type <code>optionType_</code> </p>
<p> <code>Real</code> <code>strike_</code> </p>
<p> <code>Real</code> <code>accuracy_</code> </p>
<p> <code>Natural</code> <code>maxIter_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>forward_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>price_</code> </p>
<h2>Detailed Description</h2>
<p>quote for the implied standard deviation of an underlying</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
