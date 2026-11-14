---
title: "getarguments(3)"
name: "getarguments"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getarguments/"
description: "QuantLib::PricingEngine – interface for pricing engines"
---

<p>QuantLib::PricingEngine &#8211; interface for pricing engines </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengine.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>GenericEngine&lt; Arguments, Results &gt;</code>, <code>GenericEngine&lt; ArgumentsType, ResultsType &gt;</code>, <code>GenericEngine&lt; BarrierOption::arguments, BarrierOption::results &gt;</code>, <code>GenericEngine&lt; BasketOption::arguments, BasketOption::results &gt;</code>, <code>GenericEngine&lt; Bond::arguments, Bond::results &gt;</code>, <code>GenericEngine&lt; CallableBond::arguments, CallableBond::results &gt;</code>, <code>GenericEngine&lt; CapFloor::arguments, CapFloor::results &gt;</code>, <code>GenericEngine&lt; CliquetOption::arguments, CliquetOption::results &gt;</code>, <code>GenericEngine&lt; ContinuousAveragingAsianOption::arguments, ContinuousAveragingAsianOption::results &gt;</code>, <code>GenericEngine&lt; ContinuousFixedLookbackOption::arguments, ContinuousFixedLookbackOption::results &gt;</code>, <code>GenericEngine&lt; ContinuousFloatingLookbackOption::arguments, ContinuousFloatingLookbackOption::results &gt;</code>, <code>GenericEngine&lt; ConvertibleBond::option::arguments, ConvertibleBond::option::results &gt;</code>, <code>GenericEngine&lt; CreditDefaultSwap::arguments, CreditDefaultSwap::results &gt;</code>, <code>GenericEngine&lt; DiscreteAveragingAsianOption::arguments, DiscreteAveragingAsianOption::results &gt;</code>, <code>GenericEngine&lt; DividendBarrierOption::arguments, DividendBarrierOption::results &gt;</code>, <code>GenericEngine&lt; DividendVanillaOption::arguments, DividendVanillaOption::results &gt;</code>, <code>GenericEngine&lt; EnergyCommodity::arguments, EnergyCommodity::results &gt;</code>, <code>GenericEngine&lt; EverestOption::arguments, EverestOption::results &gt;</code>, <code>GenericEngine&lt; ForwardOptionArguments&lt; VanillaOption::arguments &gt;, VanillaOption::results &gt;</code>, <code>GenericEngine&lt; HimalayaOption::arguments, HimalayaOption::results &gt;</code>, <code>GenericEngine&lt; Instr::arguments, QuantoOptionResults&lt; Instr::results &gt; &gt;</code>, <code>GenericEngine&lt; MultiAssetOption::arguments, MultiAssetOption::results &gt;</code>, <code>GenericEngine&lt; OneAssetOption::arguments, OneAssetOption::results &gt;</code>, <code>GenericEngine&lt; PagodaOption::arguments, PagodaOption::results &gt;</code>, <code>GenericEngine&lt; PathMultiAssetOption::arguments, PathMultiAssetOption::results &gt;</code>, <code>GenericEngine&lt; Swap::arguments, Swap::results &gt;</code>, <code>GenericEngine&lt; Swaption::arguments, Swaption::results &gt;</code>, <code>GenericEngine&lt; SyntheticCDO::arguments, SyntheticCDO::results &gt;</code>, <code>GenericEngine&lt; VanillaOption::arguments, VanillaOption::results &gt;</code>, <code>GenericEngine&lt; VanillaSwap::arguments, VanillaSwap::results &gt;</code>, <code>GenericEngine&lt; VarianceOption::arguments, VarianceOption::results &gt;</code>, <code>GenericEngine&lt; VarianceSwap::arguments, VarianceSwap::results &gt;</code>, and <code>GenericEngine&lt; ArgumentsType, ResultsType &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>virtual arguments * <code>getArguments</code> () const =0 </p>
<p> virtual const results * <code>getResults</code> () const =0 </p>
<p> virtual void <code>reset</code> ()=0 </p>
<p> virtual void <code>calculate</code> () const =0 </p>
<h2>Detailed Description</h2>
<p>interface for pricing engines </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
