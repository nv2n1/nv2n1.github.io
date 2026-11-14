---
title: "commoditytypes_(3)"
name: "commoditytypes_"
section: "3"
letter: "c"
url: "/docs/linux/man/3-commoditytypes_/"
description: "QuantLib::CommodityType – commodity type"
---

<p>QuantLib::CommodityType &#8211; commodity type </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/commodities/commoditytype.hpp&gt; </p>
<p> Inherited by NullCommodityType. </p>
<h3>Public Member Functions</h3>
<p><code>CommodityType</code> ()<br />
 <i>default constructor </i><br />
 <code>CommodityType</code> (const std::string &amp;code, const std::string &amp;name) </p>
<p> <code>Inspectors</code> </p>
<p> const std::string &amp; <code>code</code> () const<br />
 <i>commodity code, e.g, &#8216;HO&#8217; </i><br />
 const std::string &amp; <code>name</code> () const<br />
 <i>name, e.g, &#8216;Heating Oil&#8217; </i> </p>
<p> <code>Other information</code> </p>
<p> bool <code>empty</code> () const<br />
 <i>is this a usable instance? </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Data &gt; <code>data_</code> </p>
<h3>Static Protected Attributes</h3>
<p>static std::map&lt; std::string, boost::shared_ptr&lt; Data &gt; &gt; <code>commodityTypes_</code> </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>CommodityType</code> &amp;, const <code>CommodityType</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>CommodityType</code> &amp;, const <code>CommodityType</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>CommodityType</code> &amp;) </p>
<h2>Detailed Description</h2>
<p>commodity type</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CommodityType</code> ()</h3>
<p>default constructor </p>
<p> Instances built via this constructor have undefined behavior. Such instances can only act as placeholders and must be reassigned to a valid currency before being used.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>CommodityType</code> &amp;, const <code>CommodityType</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>CommodityType</code> &amp;, const <code>CommodityType</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>CommodityType</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
