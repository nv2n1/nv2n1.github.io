---
title: "rate_(3)"
name: "rate_"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rate_/"
description: "QuantLib::FractionalDividend – Predetermined cash flow."
---

<p>QuantLib::FractionalDividend &#8211; Predetermined cash flow. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/cashflows/dividend.hpp&gt;</code></pre>
<p> Inherits <code>QuantLib::Dividend</code>.</p>
<h3>Public Member Functions</h3>
<p><code>FractionalDividend</code> (Real rate, const <code>Date</code> &amp;date) </p>
<p> <code>FractionalDividend</code> (Real rate, Real nominal, const <code>Date</code> &amp;date)<br />
 <code>Dividend interface</code> </p>
<p> virtual Real <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i><br />
 virtual Real <code>amount</code> (Real underlying) const<br />
 <code>Inspectors</code> </p>
<p> Real <code>rate</code> () const </p>
<p> Real <code>nominal</code> () const</p>
<h3>Protected Attributes</h3>
<p>Real <code>rate_</code> </p>
<p> Real <code>nominal_</code></p>
<h2>Detailed Description</h2>
<p>Predetermined cash flow. </p>
<p> This cash flow pays a predetermined amount at a given date.</p>
<h2>Member Function Documentation</h2>
<h3>virtual Real amount () const [virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>Dividend</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
