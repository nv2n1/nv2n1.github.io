---
title: "quantlib_localvolsurface(3)"
name: "quantlib_localvolsurface"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_localvolsurface/"
description: "QuantLib::LocalVolSurface – Local volatility surface derived from a Black vol surface."
---

<p>QuantLib::LocalVolSurface &#8211; Local volatility surface derived from a Black vol surface. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/volatility/equityfx/localvolsurface.hpp&gt; </p>
<p> Inherits <code>QuantLib::LocalVolTermStructure</code>. </p>
<h3>Public Member Functions</h3>
<p><code>LocalVolSurface</code> (const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;underlying) </p>
<p> <code>LocalVolSurface</code> (const <code>Handle</code>&lt; <code>BlackVolTermStructure</code> &gt; &amp;blackTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;riskFreeTS, const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;dividendTS, Real underlying) </p>
<p> <code>TermStructure interface</code> </p>
<p> const <code>Date</code> &amp; <code>referenceDate</code> () const<br />
 <i>the date at which discount = 1.0 and/or variance = 0.0 </i><br />
 <code>DayCounter</code> <code>dayCounter</code> () const<br />
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
<p><code>Volatility</code> <code>localVolImpl</code> (Time, Real) const<br />
 <i>local vol calculation </i></p>
<h2>Detailed Description</h2>
<p>Local volatility surface derived from a Black vol surface. </p>
<p> For details about this implementation refer to &#8216;Stochastic Volatility and Local Volatility,&#8217; in &#8216;Case Studies and Financial Modelling Course Notes,&#8217; by Jim Gatheral, Fall Term, 2003 </p>
<p> see <a rel="nofollow" href="http://www.math.nyu.edu">www.math.nyu.edu</a>/fellows_fin_math/gatheral/Lecture1_Fall02.pdf </p>
<p> <code>Bug</code></p>
<dl COMPACT>
<dd>this class is untested, probably unreliable.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
