---
title: "quantlib_fdhestonbarrierengine(3)"
name: "quantlib_fdhestonbarrierengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_fdhestonbarrierengine/"
description: "QuantLib::FdHestonBarrierEngine – Finite-Differences Heston Barrier Option engine."
---

<p>QuantLib::FdHestonBarrierEngine &#8211; Finite-Differences Heston <code>Barrier</code> <code>Option</code> engine. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/finitedifferences/fdhestonbarrierengine.hpp&gt; </p>
<p> Inherits <code>GenericModelEngine&lt; HestonModel, DividendBarrierOption::arguments, DividendBarrierOption::results &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p><code>FdHestonBarrierEngine</code> (const boost::shared_ptr&lt; <code>HestonModel</code> &gt; &amp;model, Size tGrid=100, Size xGrid=100, Size vGrid=20) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Finite-Differences Heston <code>Barrier</code> <code>Option</code> engine. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned value is tested by reproducing results available in web/literature and comparison with Black pricing.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
