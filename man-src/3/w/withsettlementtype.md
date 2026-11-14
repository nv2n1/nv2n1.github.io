---
title: "withsettlementtype(3)"
name: "withsettlementtype"
section: "3"
letter: "w"
url: "/docs/linux/man/3-withsettlementtype/"
---

QuantLib::MakeSwaption - helper class 

<h2>Synopsis</h2>

<pre><code>MakeSwaption (const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, const Period &amp;optionTenor, Rate strike=Null&lt; Rate &gt;())



operator Swaption () const



operator boost::shared_ptr&lt; Swaption &gt; () const



MakeSwaption &amp; withSettlementType (Settlement::Type delivery)



MakeSwaption &amp; withOptionConvention (BusinessDayConvention bdc)



MakeSwaption &amp; withExerciseDate (const Date &amp;)



MakeSwaption &amp; withPricingEngine (const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine)</code></pre>

<h3>Public Member Functions</h3>

<pre><code>MakeSwaption (const boost::shared_ptr&lt; SwapIndex &gt; &amp;swapIndex, const Period &amp;optionTenor, Rate strike=Null&lt; Rate &gt;())



operator Swaption () const



operator boost::shared_ptr&lt; Swaption &gt; () const



MakeSwaption &amp; withSettlementType (Settlement::Type delivery)



MakeSwaption &amp; withOptionConvention (BusinessDayConvention bdc)



MakeSwaption &amp; withExerciseDate (const Date &amp;)



MakeSwaption &amp; withPricingEngine (const boost::shared_ptr&lt; PricingEngine &gt; &amp;engine)</code></pre>

<h2>Detailed Description</h2>

helper class 

 This class provides a more comfortable way to instantiate standard market swaption.

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
