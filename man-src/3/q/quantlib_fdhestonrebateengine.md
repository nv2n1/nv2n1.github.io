---
title: "quantlib_fdhestonrebateengine(3)"
name: "quantlib_fdhestonrebateengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fdhestonrebateengine/"
description: "QuantLib::FdHestonRebateEngine – Finite-Differences Heston Barrier Option rebate helper engine."
---

<p>QuantLib::FdHestonRebateEngine &#8211; Finite-Differences Heston <code>Barrier</code> <code>Option</code> rebate helper engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/finitedifferences/fdhestonrebateengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; HestonModel, DividendBarrierOption::arguments, DividendBarrierOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FdHestonRebateEngine</code> (const boost::shared_ptr&lt; <code>HestonModel</code> &gt; &amp;model, Size tGrid=100, Size xGrid=100, Size vGrid=20) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Finite-Differences Heston <code>Barrier</code> <code>Option</code> rebate helper engine. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
