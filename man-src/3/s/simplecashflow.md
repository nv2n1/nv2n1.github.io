---
title: "simplecashflow(3)"
name: "simplecashflow"
section: "3"
letter: "s"
url: "/docs/linux/man/3-simplecashflow/"
description: "QuantLib::SimpleCashFlow – Predetermined cash flow."
---

<p>QuantLib::SimpleCashFlow &#8211; Predetermined cash flow. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/cashflows/simplecashflow.hpp&gt; </p>
<p> Inherits <code>QuantLib::CashFlow</code>. </p>
<h3>Public Member Functions</h3>
<p><code>SimpleCashFlow</code> (<code>Real</code> amount, const <code>Date</code> &amp;date) </p>
<p> <code>Event interface</code> </p>
<p> <code>Date</code> <code>date</code> () const </p>
<p> <code>CashFlow interface</code> </p>
<p> <code>Real</code> <code>amount</code> () const<br />
 <i>returns the amount of the cash flow </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>Predetermined cash flow. </p>
<p> This cash flow pays a predetermined amount at a given date.</p>
<h2>Member Function Documentation</h2>
<h3><code>Date</code> date () const [virtual]</h3>
<p><code>Note:</code></p>
<dl COMPACT>
<dd>This is inheriited from the event class</dl>
<p> Implements <code>CashFlow</code>.</p>
<h3><code>Real</code> amount () const [virtual]</h3>
<p>returns the amount of the cash flow </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The amount is not discounted, i.e., it is the actual amount paid at the cash flow date.</dl>
<p> Implements <code>CashFlow</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
