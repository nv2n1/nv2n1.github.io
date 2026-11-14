---
title: "amount_(3)"
name: "amount_"
section: "3"
letter: "a"
url: "/docs/linux/man/3-amount_/"
description: "QuantLib::FixedDividend – Predetermined cash flow."
---

<h2 class="name">NAME</h2>
<p> QuantLib::FixedDividend &#8211; Predetermined cash flow. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/cashflows/dividend.hpp&gt; </p>
<p> Inherits <code>QuantLib::Dividend</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>FixedDividend</code> (Real amount, const <code>Date</code> &amp;date) </p>
<p> <code>Dividend interface</code> </p>
<p> virtual Real <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i><br />
 virtual Real <code>amount</code> (Real) const </p>
<h3>Protected Attributes</h3>
<p> Real <code>amount_</code> </p>
<h2>Detailed Description</h2>
<p> Predetermined cash flow. </p>
<p> This cash flow pays a predetermined amount at a given date. </p>
<p> <code>Examples: </code> </p>
<p> <code>ConvertibleBonds.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual Real amount () const [virtual]</h3>
<p> returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>Dividend</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
