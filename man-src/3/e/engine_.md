---
title: "engine_(3)"
name: "engine_"
section: "3"
letter: "e"
url: "/docs/linux/man/3-engine_/"
description: "QuantLib::Instrument – Abstract instrument class."
---

<h2 class="name">NAME</h2>
<p> QuantLib::Instrument &#8211; Abstract instrument class. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/instrument.hpp&gt; </p>
<p> Inherits <code>QuantLib::LazyObject</code>. </p>
<p> Inherited by <code>Bond</code>, <code>CapFloor</code>, <code>CDO</code>, <code>CdsOption</code>, <code>Commodity</code>, <code>CompositeInstrument</code>, <code>CreditDefaultSwap</code>, <code>Forward</code>, <code>InflationSwap</code>, <code>NthToDefault</code>, <code>Option</code>, <code>PathMultiAssetOption</code>, <code>RiskyAssetSwap</code>, <code>Stock</code>, <code>Swap</code>, <code>SyntheticCDO</code>, <code>VarianceOption</code>, and <code>VarianceSwap</code>. </p>
<h3>Public Member Functions</h3>
<p> virtual void <code>setupArguments</code> (PricingEngine::arguments *) const </p>
<p> virtual void <code>fetchResults</code> (const PricingEngine::results *) const </p>
<p> <code>Inspectors</code> </p>
<p> <code>Real</code> <code>NPV</code> () const<br />
 <i>returns the net present value of the instrument. </i><br />
 <code>Real</code> <code>errorEstimate</code> () const<br />
 <i>returns the error estimate on the NPV when available. </i><br />
 template&lt;typename T &gt; T <code>result</code> (const std::string &amp;tag) const<br />
 <i>returns any additional result returned by the pricing engine. </i><br />
 const std::map&lt; std::string, boost::any &gt; &amp; <code>additionalResults</code> () const<br />
 <i>returns all additional result returned by the pricing engine. </i><br />
 virtual bool <code>isExpired</code> () const =0<br />
 <i>returns whether the instrument is still tradable. </i> </p>
<p> <code>Modifiers</code> </p>
<p> void <code>setPricingEngine</code> (const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp;)<br />
 <i>set the pricing engine to be used. </i></p>
<h3>Protected Member Functions</h3>
<p> <code>Calculations</code> </p>
<p> void <code>calculate</code> () const </p>
<p> virtual void <code>setupExpired</code> () const </p>
<p> virtual void <code>performCalculations</code> () const </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>PricingEngine</code> &gt; <code>engine_</code> </p>
<p> <code>Results</code><br />
 The value of this attribute and any other that derived classes might declare must be set during calculation. </p>
<p> <code>Real</code> <code>NPV_</code> </p>
<p> <code>Real</code> <code>errorEstimate_</code> </p>
<p> std::map&lt; std::string, boost::any &gt; <code>additionalResults_</code> </p>
<h2>Detailed Description</h2>
<p> Abstract instrument class. </p>
<p> This class is purely abstract and defines the interface of concrete instruments which will be derived from this one. </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> observability of class instances is checked.</dl>
<h2>Member Function Documentation</h2>
<h3>void setPricingEngine (const boost::shared_ptr&lt; <code>PricingEngine</code> &gt; &amp; e)</h3>
<p> set the pricing engine to be used. </p>
<p> <code>Warning</code></p>
<dl>
<dt>
<dd> calling this method will have no effects in case the <code>performCalculation</code> method was overridden in a derived class.</dl>
<h3>void setupArguments (PricingEngine::arguments *) const [virtual]</h3>
<p> When a derived argument structure is defined for an instrument, this method should be overridden to fill it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented in <code>CallableBond</code>, <code>CallableFixedRateBond</code>, <code>EnergyCommodity</code>, <code>SyntheticCDO</code>, <code>DividendBarrierOption</code>, <code>PathMultiAssetOption</code>, <code>VarianceOption</code>, <code>ContinuousAveragingAsianOption</code>, <code>DiscreteAveragingAsianOption</code>, <code>AssetSwap</code>, <code>BarrierOption</code>, <code>Bond</code>, <code>CapFloor</code>, <code>CliquetOption</code>, <code>CreditDefaultSwap</code>, <code>DividendVanillaOption</code>, <code>ForwardVanillaOption</code>, <code>HimalayaOption</code>, <code>ContinuousFloatingLookbackOption</code>, <code>ContinuousFixedLookbackOption</code>, <code>MultiAssetOption</code>, <code>PagodaOption</code>, <code>Swap</code>, <code>Swaption</code>, <code>VanillaSwap</code>, <code>VarianceSwap</code>, and <code>Option</code>.</p>
<h3>void fetchResults (const PricingEngine::results * r) const [virtual]</h3>
<p> When a derived result structure is defined for an instrument, this method should be overridden to read from it. This is mandatory in case a pricing engine is used. </p>
<p> Reimplemented in <code>EnergyCommodity</code>, <code>SyntheticCDO</code>, <code>AssetSwap</code>, <code>Bond</code>, <code>CreditDefaultSwap</code>, <code>ForwardVanillaOption</code>, <code>MultiAssetOption</code>, <code>OneAssetOption</code>, <code>QuantoBarrierOption</code>, <code>QuantoForwardVanillaOption</code>, <code>QuantoVanillaOption</code>, <code>Swap</code>, <code>VanillaSwap</code>, and <code>VarianceSwap</code>.</p>
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
<p> Reimplemented from <code>LazyObject</code>.</p>
<h3>void setupExpired () const [protected, virtual]</h3>
<p> This method must leave the instrument in a consistent state when the expiration condition is met. </p>
<p> Reimplemented in <code>PathMultiAssetOption</code>, <code>Bond</code>, <code>CreditDefaultSwap</code>, <code>MultiAssetOption</code>, <code>OneAssetOption</code>, <code>Swap</code>, <code>VarianceSwap</code>, and <code>YearOnYearInflationSwap</code>.</p>
<h3>void performCalculations () const [protected, virtual]</h3>
<p> In case a pricing engine is <code>not</code> used, this method must be overridden to perform the actual calculations and set any needed results. In case a pricing engine is used, the default implementation can be used. </p>
<p> Implements <code>LazyObject</code>. </p>
<p> Reimplemented in <code>EnergyBasisSwap</code>, <code>EnergyFuture</code>, <code>EnergyVanillaSwap</code>, <code>ConvertibleBond</code>, <code>CompositeInstrument</code>, <code>FixedRateBondForward</code>, <code>Forward</code>, <code>Stock</code>, <code>YearOnYearInflationSwap</code>, and <code>ZeroCouponInflationSwap</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
