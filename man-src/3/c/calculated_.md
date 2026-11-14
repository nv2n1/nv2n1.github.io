---
title: "calculated_(3)"
name: "calculated_"
section: "3"
letter: "c"
url: "/docs/linux/man/3-calculated_/"
description: "QuantLib::LazyObject – Framework for calculation on demand and result caching."
---

<h2 class="name">NAME</h2>
<p> QuantLib::LazyObject &#8211; Framework for calculation on demand and result caching. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/patterns/lazyobject.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by <code>AbcdAtmVolCurve</code>, <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, <code>CmsMarket</code>, <code>EurodollarFuturesImpliedStdDevQuote</code>, FdmBlackScholesSolver [private], FdmHestonSolver [private], <code>FittedBondDiscountCurve</code>, <code>FlatForward</code>, <code>ForwardSwapQuote</code>, <code>ImpliedStdDevQuote</code>, <code>Instrument</code>, InterpolatedSmileSection&lt; Interpolator &gt;, <code>OneFactorCopula</code>, <code>PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</code>, <code>PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, SabrInterpolatedSmileSection, <code>StrippedOptionletAdapter</code>, <code>StrippedOptionletBase</code>, and SwaptionVolatilityDiscrete. </p>
<h3>Public Member Functions</h3>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Protected Attributes</h3>
<p> bool <code>calculated_</code> </p>
<p> bool <code>frozen_</code> </p>
<h3>Calculations</h3>
<p> These methods do not modify the structure of the object and are therefore declared as const. Data members which will be calculated on demand need to be declared as mutable.<br />
 void <code>recalculate</code> () </p>
<p> void <code>freeze</code> () </p>
<p> void <code>unfreeze</code> () </p>
<p> virtual void <code>calculate</code> () const </p>
<p> virtual void <code>performCalculations</code> () const =0 </p>
<h2>Detailed Description</h2>
<p> Framework for calculation on demand and result caching. </p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p> This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>AbcdAtmVolCurve</code>, <code>ForwardSwapQuote</code>, <code>PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</code>, <code>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</code>, <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, <code>StrippedOptionletAdapter</code>, <code>CmsMarket</code>, <code>FittedBondDiscountCurve</code>, <code>FlatForward</code>, and <code>PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</code>.</p>
<h3>void recalculate ()</h3>
<p> This method force the recalculation of any results which would otherwise be cached. It is not declared as const since it needs to call the non-const <i></i><code>notifyObservers</code> method. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> Explicit invocation of this method is <code>not</code> necessary if the object registered itself as observer with the structures on which such results depend. It is strongly advised to follow this policy when possible.</dl>
<h3>void freeze ()</h3>
<p> This method constrains the object to return the presently cached results on successive invocations, even if arguments upon which they depend should change.</p>
<h3>void unfreeze ()</h3>
<p> This method reverts the effect of the <i></i><code>freeze</code> method, thus re-enabling recalculations.</p>
<h3>void calculate () const [protected, virtual]</h3>
<p> This method performs all needed calculations by calling the <i></i><code>performCalculations</code> method. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> Objects cache the results of the previous calculation. Such results will be returned upon later invocations of <i></i><code>calculate</code>. When the results depend on arguments which could change between invocations, the lazy object must register itself as observer of such objects for the calculations to be performed again when they change.</dl>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> Should this method be redefined in derived classes, <code>LazyObject::calculate()</code> should be called in the overriding method.</dl>
<p> Reimplemented in <code>Instrument</code>.</p>
<h3>virtual void performCalculations () const [protected, pure virtual]</h3>
<p> This method must implement any calculations which must be (re)done in order to calculate the desired results. </p>
<p> Implemented in <code>EnergyBasisSwap</code>, <code>EnergyFuture</code>, <code>EnergyVanillaSwap</code>, <code>AbcdAtmVolCurve</code>, <code>Instrument</code>, <code>ConvertibleBond</code>, <code>CompositeInstrument</code>, <code>FixedRateBondForward</code>, <code>Forward</code>, <code>Stock</code>, <code>YearOnYearInflationSwap</code>, <code>ZeroCouponInflationSwap</code>, <code>EurodollarFuturesImpliedStdDevQuote</code>, <code>ForwardSwapQuote</code>, <code>ImpliedStdDevQuote</code>, <code>CapFloorTermVolCurve</code>, <code>CapFloorTermVolSurface</code>, <code>OptionletStripper1</code>, <code>OptionletStripper2</code>, <code>StrippedOptionletAdapter</code>, <code>SwaptionVolatilityMatrix</code>, and <code>FlatForward</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
