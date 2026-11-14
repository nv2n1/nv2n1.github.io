---
title: "priceimpl(3)"
name: "priceimpl"
section: "3"
letter: "p"
url: "/docs/linux/man/3-priceimpl/"
description: "QuantLib::CommodityCurve – Commodity term structure."
---

<p>QuantLib::CommodityCurve &#8211; <code>Commodity</code> term structure. </p>
<h2>Synopsis</h2>
<pre><code>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;out, const CommodityCurve &amp;curve)



std::string name_



CommodityType commodityType_



UnitOfMeasure unitOfMeasure_



Currency currency_



std::vector&lt; Date &gt; dates_



std::vector&lt; Time &gt; times_



std::vector&lt; Real &gt; data_



Interpolation interpolation_



ForwardFlat interpolator_



boost::shared_ptr&lt; CommodityCurve &gt; basisOfCurve_



Real basisOfCurveUomConversionFactor_



const std::string &amp; name () const



const CommodityType &amp; commodityType () const



const UnitOfMeasure &amp; unitOfMeasure () const



const Currency &amp; currency () const



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Real &gt; &amp; prices () const



std::vector&lt; std::pair&lt; Date, Real &gt; &gt; nodes () const



bool empty () const



void setPrices (std::map&lt; Date, Real &gt; &amp;prices)



void setBasisOfCurve (const boost::shared_ptr&lt; CommodityCurve &gt; &amp;basisOfCurve)



Real price (const Date &amp;d, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const



Real basisOfPrice (const Date &amp;d) const



Date underlyingPriceDate (const Date &amp;date, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const



const boost::shared_ptr&lt; CommodityCurve &gt; &amp; basisOfCurve () const



Real basisOfPriceImpl (Time t) const



Real priceImpl (Time t) const</code></pre>
<p> Inherits <code>QuantLib::TermStructure</code>.</p>
<h3>Public Member Functions</h3>
<p>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;out, const CommodityCurve &amp;curve)</p>
<p>std::string name_</p>
<p>CommodityType commodityType_</p>
<p>UnitOfMeasure unitOfMeasure_</p>
<p>Currency currency_</p>
<p>std::vector&lt; Date &gt; dates_</p>
<p>std::vector&lt; Time &gt; times_</p>
<p>std::vector&lt; Real &gt; data_</p>
<p>Interpolation interpolation_</p>
<p>ForwardFlat interpolator_</p>
<p>boost::shared_ptr&lt; CommodityCurve &gt; basisOfCurve_</p>
<p>Real basisOfCurveUomConversionFactor_</p>
<p>const std::string &amp; name () const</p>
<p>const CommodityType &amp; commodityType () const</p>
<p>const UnitOfMeasure &amp; unitOfMeasure () const</p>
<p>const Currency &amp; currency () const</p>
<p>Date maxDate () const</p>
<p>the latest date for which the curve can return values</p>
<p>const std::vector&lt; Time &gt; &amp; times () const</p>
<p>const std::vector&lt; Date &gt; &amp; dates () const</p>
<p>const std::vector&lt; Real &gt; &amp; prices () const</p>
<p>std::vector&lt; std::pair&lt; Date, Real &gt; &gt; nodes () const</p>
<p>bool empty () const</p>
<p>void setPrices (std::map&lt; Date, Real &gt; &amp;prices)</p>
<p>void setBasisOfCurve (const boost::shared_ptr&lt; CommodityCurve &gt; &amp;basisOfCurve)</p>
<p>Real price (const Date &amp;d, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const</p>
<p>Real basisOfPrice (const Date &amp;d) const</p>
<p>Date underlyingPriceDate (const Date &amp;date, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const</p>
<p>const boost::shared_ptr&lt; CommodityCurve &gt; &amp; basisOfCurve () const</p>
<p>Real basisOfPriceImpl (Time t) const</p>
<p>Real priceImpl (Time t) const<br />
 class <code>CommodityIndex</code></p>
<h3>Inspectors</h3>
<pre><code>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;out, const CommodityCurve &amp;curve)



std::string name_



CommodityType commodityType_



UnitOfMeasure unitOfMeasure_



Currency currency_



std::vector&lt; Date &gt; dates_



std::vector&lt; Time &gt; times_



std::vector&lt; Real &gt; data_



Interpolation interpolation_



ForwardFlat interpolator_



boost::shared_ptr&lt; CommodityCurve &gt; basisOfCurve_



Real basisOfCurveUomConversionFactor_



const std::string &amp; name () const



const CommodityType &amp; commodityType () const



const UnitOfMeasure &amp; unitOfMeasure () const



const Currency &amp; currency () const



Date maxDate () const


the latest date for which the curve can return values


const std::vector&lt; Time &gt; &amp; times () const



const std::vector&lt; Date &gt; &amp; dates () const



const std::vector&lt; Real &gt; &amp; prices () const



std::vector&lt; std::pair&lt; Date, Real &gt; &gt; nodes () const



bool empty () const



void setPrices (std::map&lt; Date, Real &gt; &amp;prices)



void setBasisOfCurve (const boost::shared_ptr&lt; CommodityCurve &gt; &amp;basisOfCurve)



Real price (const Date &amp;d, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const



Real basisOfPrice (const Date &amp;d) const



Date underlyingPriceDate (const Date &amp;date, const boost::shared_ptr&lt; ExchangeContracts &gt; &amp;exchangeContracts, Integer nearbyOffset) const



const boost::shared_ptr&lt; CommodityCurve &gt; &amp; basisOfCurve () const



Real basisOfPriceImpl (Time t) const



Real priceImpl (Time t) const</code></pre>
<h2>Detailed Description</h2>
<p><code>Commodity</code> term structure.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
