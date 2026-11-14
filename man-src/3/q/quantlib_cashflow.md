---
title: "quantlib_cashflow(3)"
name: "quantlib_cashflow"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_cashflow/"
description: "QuantLib::CashFlow – Base class for cash flows."
---

<p>QuantLib::CashFlow &#8211; Base class for cash flows. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflow.hpp&gt; </p>
<p> Inherits <code>QuantLib::Event</code>. </p>
<p> Inherited by CommodityCashFlow, <code>Coupon</code>, <code>Dividend</code>, and <code>SimpleCashFlow</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Event interface</code> </p>
<p> virtual <code>Date</code> <code>date</code> () const =0 </p>
<p> <code>CashFlow interface</code> </p>
<p> virtual <code>Real</code> <code>amount</code> () const =0<br />
 <i>returns the amount of the cash flow </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Base class for cash flows. </p>
<p> This class is purely virtual and acts as a base class for the actual cash flow implementations.</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Date</code> date () const [pure virtual]</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>This is inheriited from the event class</dl>
<p> Implements <code>Event</code>. </p>
<p> Implemented in <code>Coupon</code>, <code>Dividend</code>, and <code>SimpleCashFlow</code>.</p>
<h3>virtual <code>Real</code> amount () const [pure virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implemented in <code>Dividend</code>, <code>FixedDividend</code>, <code>FractionalDividend</code>, <code>FixedRateCoupon</code>, <code>FloatingRateCoupon</code>, and <code>SimpleCashFlow</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
