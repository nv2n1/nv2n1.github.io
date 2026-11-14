---
title: "quantlib_genericengine(3)"
name: "quantlib_genericengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_genericengine/"
description: "QuantLib::GenericEngine – template base class for option pricing engines"
---

<p>QuantLib::GenericEngine &#8211; template base class for option pricing engines </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::PricingEngine</code>, and <code>QuantLib::Observer</code>. </p>
<p> Inherited by <code>MCLongstaffSchwartzEngine&lt; GenericEngine, MC, RNG, S &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>PricingEngine::arguments * <code>getArguments</code> () const </p>
<p> const PricingEngine::results * <code>getResults</code> () const </p>
<p> void <code>reset</code> () </p>
<p> void <code>update</code> () </p>
<h3>Protected Attributes</h3>
<p>ArgumentsType <code>arguments_</code> </p>
<p> ResultsType <code>results_</code> </p>
<h2>Detailed Description</h2>
<h3>template&lt;class ArgumentsType, class ResultsType&gt; class QuantLib::GenericEngine&lt; ArgumentsType, ResultsType &gt;</h3>
<p>template base class for option pricing engines </p>
<p> Derived engines only need to implement the calculate() method.</p>
<h2>Member Function Documentation</h2>
<h3>void update () [virtual]</h3>
<p>This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>LatticeShortRateModelEngine&lt; Arguments, Results &gt;</code>, <code>AnalyticHestonHullWhiteEngine</code>, <code>LatticeShortRateModelEngine&lt; CapFloor::arguments, CapFloor::results &gt;</code>, <code>LatticeShortRateModelEngine&lt; Swaption::arguments, Swaption::results &gt;</code>, <code>LatticeShortRateModelEngine&lt; VanillaSwap::arguments, VanillaSwap::results &gt;</code>, and <code>LatticeShortRateModelEngine&lt; CallableBond::arguments, CallableBond::results &gt;</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
