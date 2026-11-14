---
title: "quantlib_money(3)"
name: "quantlib_money"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_money/"
description: "QuantLib::Money – amount of cash"
---

<p>QuantLib::Money &#8211; amount of cash </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/money.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>Money</code> () </p>
<p> <code>Money</code> (const <code>Currency</code> &amp;currency, Decimal value) </p>
<p> <code>Money</code> (Decimal value, const <code>Currency</code> &amp;currency) </p>
<p> <code>Inspectors</code> </p>
<p> const <code>Currency</code> &amp; <code>currency</code> () const </p>
<p> Decimal <code>value</code> () const </p>
<p> <code>Money</code> <code>rounded</code> () const </p>
<p> <code>Money arithmetics</code><br />
 See below for non-member functions and for settings which determine the behavior of the operators. </p>
<p> <code>Money</code> <code>operator+</code> () const </p>
<p> <code>Money</code> <code>operator-</code> () const </p>
<p> <code>Money</code> &amp; <code>operator+=</code> (const <code>Money</code> &amp;) </p>
<p> <code>Money</code> &amp; <code>operator-=</code> (const <code>Money</code> &amp;) </p>
<p> <code>Money</code> &amp; <code>operator*=</code> (Decimal) </p>
<p> <code>Money</code> &amp; <code>operator/=</code> (Decimal) </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 <code>Money</code> <code>operator+</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> <code>Money</code> <code>operator-</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> <code>Money</code> <code>operator*</code> (const <code>Money</code> &amp;, Decimal) </p>
<p> <code>Money</code> <code>operator*</code> (Decimal, const <code>Money</code> &amp;) </p>
<p> <code>Money</code> <code>operator/</code> (const <code>Money</code> &amp;, Decimal) </p>
<p> Decimal <code>operator/</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator==</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator&lt;</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator&lt;=</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator&gt;</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>operator&gt;=</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;) </p>
<p> bool <code>close</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;, Size n=42) </p>
<p> bool <code>close_enough</code> (const <code>Money</code> &amp;, const <code>Money</code> &amp;, Size n=42) </p>
<p> <code>Money</code> <code>operator*</code> (Decimal, const <code>Currency</code> &amp;) </p>
<p> <code>Money</code> <code>operator*</code> (const <code>Currency</code> &amp;, Decimal) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Money</code> &amp;) </p>
<h3>Conversion settings</h3>
<p>These parameters are used for combining money amounts in different currencies<br />
 enum <code>ConversionType</code> { <code>NoConversion</code>, <code>BaseCurrencyConversion</code>, <code>AutomatedConversion</code> } </p>
<p> static <code>ConversionType</code> <code>conversionType</code> </p>
<p> static <code>Currency</code> <code>baseCurrency</code> </p>
<h2>Detailed Description</h2>
<p>amount of cash </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>money arithmetic is tested with and without currency conversions.</dl>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>ConversionType</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>NoConversion </i></p>
<dd>do not perform conversions</p>
<dt><i>BaseCurrencyConversion </i></p>
<dd>convert both operands to the base currency before converting</p>
<dt><i>AutomatedConversion </i></p>
<dd>return the result in the currency of the first operand</dl>
<h2>Friends And Related Function Documentation</h2>
<h3><code>Money</code> operator+ (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3><code>Money</code> operator- (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3><code>Money</code> operator* (const <code>Money</code> &amp;, Decimal) [related]</h3>
<h3><code>Money</code> operator* (Decimal, const <code>Money</code> &amp;) [related]</h3>
<h3><code>Money</code> operator/ (const <code>Money</code> &amp;, Decimal) [related]</h3>
<h3>Decimal operator/ (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator== (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator&lt; (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator&lt;= (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator&gt; (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool operator&gt;= (const <code>Money</code> &amp;, const <code>Money</code> &amp;) [related]</h3>
<h3>bool close (const <code>Money</code> &amp;, const <code>Money</code> &amp;, Size n = 42) [related]</h3>
<h3>bool close_enough (const <code>Money</code> &amp;, const <code>Money</code> &amp;, Size n = 42) [related]</h3>
<h3><code>Money</code> operator* (Decimal, const <code>Currency</code> &amp;) [related]</h3>
<h3><code>Money</code> operator* (const <code>Currency</code> &amp;, Decimal) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Money</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
