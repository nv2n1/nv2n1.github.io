---
title: "quantlib_impliedvoltermstructure(3)"
name: "quantlib_impliedvoltermstructure"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_impliedvoltermstructure/"
description: "QuantLib::ImpliedVolTermStructure – Implied vol term structure at a given date in the future."
---

<p>QuantLib::ImpliedVolTermStructure &#8211; Implied vol term structure at a given date in the future. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/impliedvoltermstructure.hpp&gt; </p>
<p> Inherits <code>QuantLib::BlackVarianceTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ImpliedVolTermStructure</code> (const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;origTS, const <code>Date</code> &amp;referenceDate) </p>
<p> <code>TermStructure interface</code> </p>
<p> <code>DayCounter</code> <code>dayCounter</code> () const<br />
 <i>the day counter used for date/time conversion </i><br />
 <code>Date</code> <code>maxDate</code> () const<br />
 <i>the latest date for which the curve can return values </i> </p>
<p> <code>VolatilityTermStructure interface</code> </p>
<p> Real <code>minStrike</code> () const<br />
 <i>the minimum strike for which the term structure can return vols </i><br />
 Real <code>maxStrike</code> () const<br />
 <i>the maximum strike for which the term structure can return vols </i> </p>
<p> <code>Visitability</code> </p>
<p> virtual void <code>accept</code> (<code>AcyclicVisitor</code> &amp;) </p>
<h3>Protected Member Functions</h3>
<p>virtual Real <code>blackVarianceImpl</code> (Time t, Real strike) const<br />
 <i>Black variance calculation. </i></p>
<h2>Detailed Description</h2>
<p>Implied vol term structure at a given date in the future. </p>
<p> The given date will be the implied reference date. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This term structure will remain linked to the original structure, i.e., any changes in the latter will be reflected in this structure as well.</dl>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>It doesn&#8217;t make financial sense to have an asset-dependant implied Vol Term Structure. This class should be used with term structures that are time dependant only.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
