---
title: "rounded(3)"
name: "rounded"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rounded/"
description: "QuantLib::Quantity – Amount of a commodity."
---

<p>QuantLib::Quantity &#8211; Amount of a commodity. </p>
<h2>Synopsis</h2>
<pre><code>Quantity operator+ () const



Quantity operator- () const



Quantity &amp; operator+= (const Quantity &amp;)



Quantity &amp; operator-= (const Quantity &amp;)



Quantity &amp; operator*= (Real)



Quantity &amp; operator/= (Real)



Friends
std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Quantity &amp;)



Related Functions

(Note that these are not member functions.)


Quantity operator+ (const Quantity &amp;, const Quantity &amp;)



Quantity operator- (const Quantity &amp;, const Quantity &amp;)



Quantity operator* (const Quantity &amp;, Real)



Quantity operator* (Real, const Quantity &amp;)



Quantity operator/ (const Quantity &amp;, Real)



Real operator/ (const Quantity &amp;, const Quantity &amp;)



bool operator== (const Quantity &amp;, const Quantity &amp;)



bool operator!= (const Quantity &amp;, const Quantity &amp;)



bool operator&lt; (const Quantity &amp;, const Quantity &amp;)



bool operator&lt;= (const Quantity &amp;, const Quantity &amp;)



bool operator&gt; (const Quantity &amp;, const Quantity &amp;)



bool operator&gt;= (const Quantity &amp;, const Quantity &amp;)



bool close (const Quantity &amp;, const Quantity &amp;, Size n=42)



bool close_enough (const Quantity &amp;, const Quantity &amp;, Size n=42)



Conversion settings

These parameters are used for combining quantity amounts in different currencies


enum ConversionType { NoConversion, BaseUnitOfMeasureConversion, AutomatedConversion }



static ConversionType conversionType



static UnitOfMeasure baseUnitOfMeasure</code></pre>
<h3>Public Member Functions</h3>
<p><code>Constructors</code> </p>
<p> <code>Quantity</code> () </p>
<p> <code>Quantity</code> (const <code>CommodityType</code> &amp;commodityType, const <code>UnitOfMeasure</code> &amp;unitOfMeasure, Real amount)<br />
 <code>Inspectors</code><br />
 Quantity operator+ () const</p>
<p>Quantity operator- () const</p>
<p>Quantity &amp; operator+= (const Quantity &amp;)</p>
<p>Quantity &amp; operator-= (const Quantity &amp;)</p>
<p>Quantity &amp; operator*= (Real)</p>
<p>Quantity &amp; operator/= (Real)</p>
<p>Friends<br />
std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Quantity &amp;)</p>
<p>Related Functions</p>
<p>(Note that these are not member functions.)</p>
<p>Quantity operator+ (const Quantity &amp;, const Quantity &amp;)</p>
<p>Quantity operator- (const Quantity &amp;, const Quantity &amp;)</p>
<p>Quantity operator* (const Quantity &amp;, Real)</p>
<p>Quantity operator* (Real, const Quantity &amp;)</p>
<p>Quantity operator/ (const Quantity &amp;, Real)</p>
<p>Real operator/ (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator== (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator!= (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator&lt; (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator&lt;= (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator&gt; (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool operator&gt;= (const Quantity &amp;, const Quantity &amp;)</p>
<p>bool close (const Quantity &amp;, const Quantity &amp;, Size n=42)</p>
<p>bool close_enough (const Quantity &amp;, const Quantity &amp;, Size n=42)</p>
<p>Conversion settings</p>
<p>These parameters are used for combining quantity amounts in different currencies</p>
<p>enum ConversionType { NoConversion, BaseUnitOfMeasureConversion, AutomatedConversion }</p>
<p>static ConversionType conversionType</p>
<p>static UnitOfMeasure baseUnitOfMeasure <code>Quantity arithmetics</code><br />
 See below for non-member functions and for settings which determine the behavior of the operators. </p>
<pre><code>Quantity operator+ () const



Quantity operator- () const



Quantity &amp; operator+= (const Quantity &amp;)



Quantity &amp; operator-= (const Quantity &amp;)



Quantity &amp; operator*= (Real)



Quantity &amp; operator/= (Real)



Friends
std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const Quantity &amp;)



Related Functions

(Note that these are not member functions.)


Quantity operator+ (const Quantity &amp;, const Quantity &amp;)



Quantity operator- (const Quantity &amp;, const Quantity &amp;)



Quantity operator* (const Quantity &amp;, Real)



Quantity operator* (Real, const Quantity &amp;)



Quantity operator/ (const Quantity &amp;, Real)



Real operator/ (const Quantity &amp;, const Quantity &amp;)



bool operator== (const Quantity &amp;, const Quantity &amp;)



bool operator!= (const Quantity &amp;, const Quantity &amp;)



bool operator&lt; (const Quantity &amp;, const Quantity &amp;)



bool operator&lt;= (const Quantity &amp;, const Quantity &amp;)



bool operator&gt; (const Quantity &amp;, const Quantity &amp;)



bool operator&gt;= (const Quantity &amp;, const Quantity &amp;)



bool close (const Quantity &amp;, const Quantity &amp;, Size n=42)



bool close_enough (const Quantity &amp;, const Quantity &amp;, Size n=42)



Conversion settings

These parameters are used for combining quantity amounts in different currencies


enum ConversionType { NoConversion, BaseUnitOfMeasureConversion, AutomatedConversion }



static ConversionType conversionType



static UnitOfMeasure baseUnitOfMeasure</code></pre>
<h2>Detailed Description</h2>
<p>Amount of a commodity.</p>
<h2>Member Enumeration Documentation</h2>
<h3>enum <code>ConversionType</code></h3>
<p><code>Enumerator: </code></p>
<dl>
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
