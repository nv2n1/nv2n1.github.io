---
title: "frozen_(3)"
name: "frozen_"
section: "3"
letter: "f"
url: "/docs/linux/man/3-frozen_/"
---

<h2 class="name">NAME</h2>
 

 QuantLib::LazyObject - Framework for calculation on demand and result caching. 

<h2>SYNOPSIS</h2>

 
 

 #include &lt;ql/patterns/lazyobject.hpp&gt; 

 Inherits <b>QuantLib::Observable</b>, and <b>QuantLib::Observer</b>. 

 Inherited by <b>AbcdAtmVolCurve</b>, <b>CapFloorTermVolCurve</b>, <b>CapFloorTermVolSurface</b>, <b>CmsMarket</b>, <b>EurodollarFuturesImpliedStdDevQuote</b>, FdmBlackScholesSolver [private], FdmHestonSolver [private], <b>FittedBondDiscountCurve</b>, <b>FlatForward</b>, <b>ForwardSwapQuote</b>, <b>ImpliedStdDevQuote</b>, <b>Instrument</b>, InterpolatedSmileSection&lt; Interpolator &gt;, <b>OneFactorCopula</b>, <b>PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</b>, <b>PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</b>, <b>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</b>, <b>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</b>, SabrInterpolatedSmileSection, <b>StrippedOptionletAdapter</b>, <b>StrippedOptionletBase</b>, and SwaptionVolatilityDiscrete. 

<h3>Public Member Functions</h3>

 

 

 <b>Observer interface</b> 
 

 
 void <b>update</b> () 

<h3>Protected Attributes</h3>

 

 
 bool <b>calculated_</b> 
 
 bool <b>frozen_</b> 

<h3>Calculations</h3>

 These methods do not modify the structure of the object and are therefore declared as const. Data members which will be calculated on demand need to be declared as mutable. 
 void <b>recalculate</b> () 
 
 void <b>freeze</b> () 
 
 void <b>unfreeze</b> () 
 
 virtual void <b>calculate</b> () const 
 
 virtual void <b>performCalculations</b> () const =0 

<h2>Detailed Description</h2>

 

 Framework for calculation on demand and result caching. 

 

<h2>Member Function Documentation</h2>

 

<h3>void update () [virtual]</h3>

 

 This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. 

 Implements <b>Observer</b>. 

 Reimplemented in <b>AbcdAtmVolCurve</b>, <b>ForwardSwapQuote</b>, <b>PiecewiseDefaultCurve&lt; Traits, Interpolator, Bootstrap &gt;</b>, <b>PiecewiseYoYInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</b>, <b>PiecewiseZeroInflationCurve&lt; Interpolator, Bootstrap, Traits &gt;</b>, <b>CapFloorTermVolCurve</b>, <b>CapFloorTermVolSurface</b>, <b>StrippedOptionletAdapter</b>, <b>CmsMarket</b>, <b>FittedBondDiscountCurve</b>, <b>FlatForward</b>, and <b>PiecewiseYieldCurve&lt; Traits, Interpolator, Bootstrap &gt;</b>.

<h3>void recalculate ()</h3>

 

 This method force the recalculation of any results which would otherwise be cached. It is not declared as const since it needs to call the non-const <i></i><b>notifyObservers</b> method. 

 <b>Note:</b>
<dl>
<dt>
<dd> Explicit invocation of this method is <b>not</b> necessary if the object registered itself as observer with the structures on which such results depend. It is strongly advised to follow this policy when possible.</dl>
 

 

<h3>void freeze ()</h3>

 

 This method constrains the object to return the presently cached results on successive invocations, even if arguments upon which they depend should change.

<h3>void unfreeze ()</h3>

 

 This method reverts the effect of the <i></i><b>freeze</b> method, thus re-enabling recalculations.

<h3>void calculate () const [protected, virtual]</h3>

 

 This method performs all needed calculations by calling the <i></i><b>performCalculations</b> method. 

 <b>Warning</b>
<dl>
<dt>
<dd> Objects cache the results of the previous calculation. Such results will be returned upon later invocations of <i></i><b>calculate</b>. When the results depend on arguments which could change between invocations, the lazy object must register itself as observer of such objects for the calculations to be performed again when they change.</dl>
 

 <b>Warning</b>
<dl>
<dt>
<dd> Should this method be redefined in derived classes, <b>LazyObject::calculate()</b> should be called in the overriding method.</dl>
 

 

 

 Reimplemented in <b>Instrument</b>.

<h3>virtual void performCalculations () const [protected, pure virtual]</h3>

 

 This method must implement any calculations which must be (re)done in order to calculate the desired results. 

 Implemented in <b>EnergyBasisSwap</b>, <b>EnergyFuture</b>, <b>EnergyVanillaSwap</b>, <b>AbcdAtmVolCurve</b>, <b>Instrument</b>, <b>ConvertibleBond</b>, <b>CompositeInstrument</b>, <b>FixedRateBondForward</b>, <b>Forward</b>, <b>Stock</b>, <b>YearOnYearInflationSwap</b>, <b>ZeroCouponInflationSwap</b>, <b>EurodollarFuturesImpliedStdDevQuote</b>, <b>ForwardSwapQuote</b>, <b>ImpliedStdDevQuote</b>, <b>CapFloorTermVolCurve</b>, <b>CapFloorTermVolSurface</b>, <b>OptionletStripper1</b>, <b>OptionletStripper2</b>, <b>StrippedOptionletAdapter</b>, <b>SwaptionVolatilityMatrix</b>, and <b>FlatForward</b>. 

<h2>Author</h2>

 

 Generated automatically by Doxygen for QuantLib from the source code. 

<h2>Index</h2>


