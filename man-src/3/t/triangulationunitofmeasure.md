---
title: "triangulationunitofmeasure(3)"
name: "triangulationunitofmeasure"
section: "3"
letter: "t"
url: "/docs/linux/man/3-triangulationunitofmeasure/"
description: "QuantLib::UnitOfMeasure – Unit of measure specification"
---

<p>QuantLib::UnitOfMeasure &#8211; Unit of measure specification </p>
<h2>Synopsis</h2>
<pre><code>const std::string &amp; name () const


name, e.g, 'Barrels'


const std::string &amp; code () const


code, e.g, 'BBL', 'MT'


Type unitType () const


unit type (mass, volume...)</code></pre>
<p> Inherited by BarrelUnitOfMeasure, GallonUnitOfMeasure, KilolitreUnitOfMeasure, LitreUnitOfMeasure, LotUnitOfMeasure, MBUnitOfMeasure, MTUnitOfMeasure, and TokyoKilolitreUnitOfMeasure.</p>
<h3>Public Types</h3>
<p>enum <code>Type</code> { <code>Mass</code>, <code>Volume</code>, <code>Energy</code>, <code>Quantity</code> }</p>
<h3>Public Member Functions</h3>
<p><code>UnitOfMeasure</code> ()<br />
 <i>default constructor </i><br />
 <code>UnitOfMeasure</code> (const std::string &amp;name, const std::string &amp;code, Type unitType)<br />
 <code>Inspectors</code> </p>
<pre><code>const std::string &amp; name () const


name, e.g, 'Barrels'


const std::string &amp; code () const


code, e.g, 'BBL', 'MT'


Type unitType () const


unit type (mass, volume...)</code></pre>
<p> <code>Other information</code> </p>
<p> bool <code>empty</code> () const<br />
 <i>is this a usable instance? </i><br />
 const <code>Rounding</code> &amp; <code>rounding</code> () const </p>
<p> const <code>UnitOfMeasure</code> &amp; <code>triangulationUnitOfMeasure</code> () const<br />
 <i>unit used for triangulation when required </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Data &gt; <code>data_</code></p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>UnitOfMeasure</code> &amp;, const <code>UnitOfMeasure</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>UnitOfMeasure</code> &amp;, const <code>UnitOfMeasure</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>UnitOfMeasure</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>Unit of measure specification</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>UnitOfMeasure</code> ()</h3>
<p>default constructor </p>
<p> Instances built via this constructor have undefined behavior. Such instances can only act as placeholders and must be reassigned to a valid currency before being used.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>UnitOfMeasure</code> &amp;, const <code>UnitOfMeasure</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>UnitOfMeasure</code> &amp;, const <code>UnitOfMeasure</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>UnitOfMeasure</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
