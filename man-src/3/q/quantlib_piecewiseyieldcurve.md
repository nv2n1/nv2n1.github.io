---
title: "quantlib_piecewiseyieldcurve(3)"
name: "quantlib_piecewiseyieldcurve"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_piecewiseyieldcurve/"
description: "QuantLib::PiecewiseYieldCurve – Piecewise yield term structure."
---

<p>QuantLib::PiecewiseYieldCurve &#8211; Piecewise yield term structure. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/yield/piecewiseyieldcurve.hpp&gt; </p>
<p> Inherits Traits::template curve::type&lt;Interpolator&gt;, and <code>QuantLib::LazyObject</code>. </p>
<h3>Public Types</h3>
<p>typedef Traits <code>traits_type</code> </p>
<p> typedef Interpolator <code>interpolator_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>PiecewiseYieldCurve</code> (const <code>Date</code> &amp;referenceDate, const std::vector&lt; boost::shared_ptr&lt; typename Traits::helper &gt; &gt; &amp;instruments, const <code>DayCounter</code> &amp;dayCounter, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;jumps=std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt;(), const std::vector&lt; <code>Date</code> &gt; &amp;jumpDates=std::vector&lt; <code>Date</code> &gt;(), <code>Real</code> accuracy=1.0e-12, const Interpolator &amp;i=Interpolator(), const Bootstrap&lt; this_curve &gt; &amp;bootstrap=Bootstrap&lt; this_curve &gt;()) </p>
<p> <code>PiecewiseYieldCurve</code> (<code>Natural</code> settlementDays, const <code>Calendar</code> &amp;calendar, const std::vector&lt; boost::shared_ptr&lt; typename Traits::helper &gt; &gt; &amp;instruments, const <code>DayCounter</code> &amp;dayCounter, const std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt; &amp;jumps=std::vector&lt; <code>Handle</code>&lt; <code>Quote</code> &gt; &gt;(), const std::vector&lt; <code>Date</code> &gt; &amp;jumpDates=std::vector&lt; <code>Date</code> &gt;(), <code>Real</code> accuracy=1.0e-12, const Interpolator &amp;i=Interpolator(), const Bootstrap&lt; this_curve &gt; &amp;bootstrap=Bootstrap&lt; this_curve &gt;()) </p>
<p> <code>YieldTermStructure interface</code> </p>
<p> <code>Date</code> <code>maxDate</code> () const </p>
<p> <code>Inspectors</code> </p>
<p> const std::vector&lt; Time &gt; &amp; <code>times</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>dates</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>data</code> () const </p>
<p> std::vector&lt; std::pair&lt; <code>Date</code>, <code>Real</code> &gt; &gt; <code>nodes</code> () const </p>
<p> const std::vector&lt; <code>Date</code> &gt; &amp; <code>jumpDates</code> () const </p>
<p> const std::vector&lt; Time &gt; &amp; <code>jumpTimes</code> () const </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Friends</h3>
<p>class <code>Bootstrap&lt; this_curve &gt;</code> </p>
<p> class <code>BootstrapError&lt; this_curve &gt;</code> </p>
<p> class <code>PenaltyFunction&lt; this_curve &gt;</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class Traits, class Interpolator, template&lt; class &gt; class Bootstrap = IterativeBootstrap&gt; class QuantLib::PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</h3>
<p>Piecewise yield term structure. </p>
<p> This term structure is bootstrapped on a number of interest rate instruments which are passed as a vector of handles to RateHelper instances. Their maturities mark the boundaries of the interpolated segments. </p>
<p> Each segment is determined sequentially starting from the earliest period to the latest and is chosen so that the instrument whose maturity marks the end of such segment is correctly repriced on the curve. </p>
<p> <code>Warning</code></p>
<dl COMPACT>
<dd>The bootstrapping algorithm will raise an exception if any two instruments have the same maturity date.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned values is tested by checking them against the original inputs.</p>
<dt>*</p>
<dd>the observability of the term structure is tested.</dl>
</dl>
<p> <code>Examples: </code> </p>
<p> <code>Bonds.cpp</code>, <code>FittedBondCurve.cpp</code>, <code>FRA.cpp</code>, and <code>swapvaluation.cpp</code>.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Reimplemented from <code>LazyObject</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
