---
title: "accuracy_(3)"
name: "accuracy_"
section: "3"
letter: "a"
url: "/docs/linux/man/3-accuracy_/"
description: "QuantLib::EurodollarFuturesImpliedStdDevQuote – quote for the Eurodollar-future implied standard deviation"
---

<h2 class="name">NAME</h2>
<p> QuantLib::EurodollarFuturesImpliedStdDevQuote &#8211; quote for the Eurodollar-future implied standard deviation </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/quotes/eurodollarfuturesquote.hpp&gt; </p>
<p> Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>EurodollarFuturesImpliedStdDevQuote</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;forward, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;callPrice, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;putPrice, <code>Real</code> strike, <code>Real</code> guess=.15, <code>Real</code> accuracy=1.0e-6, Natural maxIter=100) </p>
<p> <code>Quote interface</code> </p>
<p> <code>Real</code> <code>value</code> () const<br />
 <i>returns the current value </i><br />
 bool <code>isValid</code> () const<br />
 <i>returns true if the </i><code>Quote</code> holds a valid value</p>
<h3>Protected Member Functions</h3>
<p> void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p> <code>Real</code> <code>impliedStdev_</code> </p>
<p> <code>Real</code> <code>strike_</code> </p>
<p> <code>Real</code> <code>accuracy_</code> </p>
<p> <code>Natural</code> <code>maxIter_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>forward_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>callPrice_</code> </p>
<p> <code>Handle</code>&lt; <code>Quote</code> &gt; <code>putPrice_</code> </p>
<h2>Detailed Description</h2>
<p> quote for the Eurodollar-future implied standard deviation</p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p> This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
