---
title: "quantity(3)"
name: "quantity"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantity/"
description: "QuantLib::Quantity – Amount of a commodity."
---

<p>QuantLib::Quantity &#8211; Amount of a commodity. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/quantity.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>Quantity</code> () </p>
<p> <code>Quantity</code> (const <code>CommodityType</code> &amp;commodityType, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, Real amount) </p>
<p> <code>Inspectors</code> </p>
<p> const <code>CommodityType</code> &amp; <code>commodityType</code> () const </p>
<p> const <code>UnitOfMeasure</code> &amp; <code>unitOfMeasure</code> () const </p>
<p> Real <code>amount</code> () const </p>
<p> <code>Quantity</code> <code>rounded</code> () const </p>
<p> <code>Quantity arithmetics</code><br />
 See below for non-member functions and for settings which determine the behavior of the operators. </p>
<p> <code>Quantity</code> <code>operator+</code> () const </p>
<p> <code>Quantity</code> <code>operator-</code> () const </p>
<p> <code>Quantity</code> &amp; <code>operator+=</code> (const <code>Quantity</code> &amp;) </p>
<p> <code>Quantity</code> &amp; <code>operator-=</code> (const <code>Quantity</code> &amp;) </p>
<p> <code>Quantity</code> &amp; <code>operator*=</code> (Real) </p>
<p> <code>Quantity</code> &amp; <code>operator/=</code> (Real) </p>
<h3>Friends</h3>
<p>std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Quantity</code> &amp;) </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 <code>Quantity</code> <code>operator+</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> <code>Quantity</code> <code>operator-</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> <code>Quantity</code> <code>operator*</code> (const <code>Quantity</code> &amp;, Real) </p>
<p> <code>Quantity</code> <code>operator*</code> (Real, const <code>Quantity</code> &amp;) </p>
<p> <code>Quantity</code> <code>operator/</code> (const <code>Quantity</code> &amp;, Real) </p>
<p> Real <code>operator/</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator==</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator&lt;</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator&lt;=</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator&gt;</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>operator&gt;=</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) </p>
<p> bool <code>close</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;, Size n=42) </p>
<p> bool <code>close_enough</code> (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;, Size n=42) </p>
<h3>Conversion settings</h3>
<p>These parameters are used for combining quantity amounts in different currencies<br />
 enum <code>ConversionType</code> { <code>NoConversion</code>, <code>BaseUnitOfMeasureConversion</code>, <code>AutomatedConversion</code> } </p>
<p> static <code>ConversionType</code> <code>conversionType</code> </p>
<p> static <code>UnitOfMeasure</code> <code>baseUnitOfMeasure</code> </p>
<h2>Detailed Description</h2>
<p>Amount of a commodity.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>ConversionType</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>NoConversion </i></p>
<dd>do not perform conversions</p>
<dt><i>BaseUnitOfMeasureConversion </i></p>
<dd>convert both operands to the base unitOfMeasure before converting</p>
<dt><i>AutomatedConversion </i></p>
<dd>return the result in the unitOfMeasure of the first operand</dl>
<h2>Friends And Related Function Documentation</h2>
<h3><code>Quantity</code> operator+ (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3><code>Quantity</code> operator- (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3><code>Quantity</code> operator* (const <code>Quantity</code> &amp;, Real) [related]</h3>
<h3><code>Quantity</code> operator* (Real, const <code>Quantity</code> &amp;) [related]</h3>
<h3><code>Quantity</code> operator/ (const <code>Quantity</code> &amp;, Real) [related]</h3>
<h3>Real operator/ (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator== (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator&lt; (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator&lt;= (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator&gt; (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool operator&gt;= (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;) [related]</h3>
<h3>bool close (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;, Size n = 42) [related]</h3>
<h3>bool close_enough (const <code>Quantity</code> &amp;, const <code>Quantity</code> &amp;, Size n = 42) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
