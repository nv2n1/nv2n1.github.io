---
title: "quantlib_dividend(3)"
name: "quantlib_dividend"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_dividend/"
description: "QuantLib::Dividend – Predetermined cash flow."
---

<p>QuantLib::Dividend &#8211; Predetermined cash flow. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/dividend.hpp&gt; </p>
<p> Inherits <code>QuantLib::CashFlow</code>. </p>
<p> Inherited by <code>FixedDividend</code>, and <code>FractionalDividend</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Dividend</code> (const <code>Date</code> &amp;date) </p>
<p> virtual Real <code>amount</code> (Real underlying) const =0 </p>
<p> <code>Event interface</code> </p>
<p> <code>Date</code> <code>date</code> () const </p>
<p> <code>CashFlow interface</code> </p>
<p> virtual Real <code>amount</code> () const =0<br />
 <i>returns the amount of the cash flow </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Attributes</h3>
<p><code>Date</code> <code>date_</code> </p>
<h2>Detailed Description</h2>
<p>Predetermined cash flow. </p>
<p> This cash flow pays a predetermined amount at a given date.</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> date () const [virtual]</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>This is inheriited from the event class</dl>
<p> Implements <code>CashFlow</code>.</p>
<h3>virtual Real amount () const [pure virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>CashFlow</code>. </p>
<p> Implemented in <code>FixedDividend</code>, and <code>FractionalDividend</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
