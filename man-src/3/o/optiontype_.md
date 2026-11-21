---
title: "optiontype_(3)"
name: "optiontype_"
section: "3"
letter: "o"
url: "/docs/linux/man/3-optiontype_/"
description: "QuantLib::ImpliedStdDevQuote – quote for the implied standard deviation of an underlying"
---
<p>QuantLib::ImpliedStdDevQuote &#8211; quote for the implied standard deviation of an underlying </p>
<h2>SYNOPSIS</h2>
<p> <br />
 </p>
<p>#include &lt;ql/quotes/impliedstddevquote.hpp&gt; </p>
<p>Inherits <code>QuantLib::Quote</code>, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Member Functions</h3>
<p> <br />
 <code>ImpliedStdDevQuote</code> (Option::Type optionType, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;forward, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;price, <code>Real</code> strike, <code>Real</code> guess, <code>Real</code> accuracy=1.0e-6, Natural maxIter=100) <br />
 </p>
<p> <code>Quote interface</code> <br />
 </p>
<p> <br />
 <code>Real</code> <code>value</code> () const <br />
 <i>returns the current value </i> <br />
 bool <code>isValid</code> () const <br />
 <i>returns true if the </i><code>Quote</code> holds a valid value  </p>
<h3>Protected Member Functions</h3>
<p> <br />
 void <code>performCalculations</code> () const <br />
  </p>
<h3>Protected Attributes</h3>
<p> <br />
 <code>Real</code> <code>impliedStdev_</code> <br />
 <br />
 Option::Type <code>optionType_</code> <br />
 <br />
 <code>Real</code> <code>strike_</code> <br />
 <br />
 <code>Real</code> <code>accuracy_</code> <br />
 <br />
 <code>Natural</code> <code>maxIter_</code> <br />
 <br />
 <code>Handle</code>&lt; <code>Quote</code> &gt; <code>forward_</code> <br />
 <br />
 <code>Handle</code>&lt; <code>Quote</code> &gt; <code>price_</code> <br />
  </p>
<h2>Detailed Description</h2>
<p>quote for the implied standard deviation of an underlying  </p>
<h2>Member Function Documentation</h2>
<h3>void performCalculations () const [protected, virtual]</h3>
<p>This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p>Implements <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAD">Public Member Functions</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Protected Member Functions</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">Protected Attributes</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAG">Detailed Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Member Function Documentation</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAI">void performCalculations () const [protected, virtual]</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAJ">Author</a></dt>
<dd>  </dd></dl>
