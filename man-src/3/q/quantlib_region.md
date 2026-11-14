---
title: "quantlib_region(3)"
name: "quantlib_region"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_region/"
description: "QuantLib::Region – Region class, used for inflation applicability."
---

<p>QuantLib::Region &#8211; <code>Region</code> class, used for inflation applicability. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/indexes/region.hpp&gt; </p>
<p> Inherited by <code>AustraliaRegion</code>, <code>EURegion</code>, <code>FranceRegion</code>, and <code>UKRegion</code>. </p>
<h3>Public Member Functions</h3>
<p><code>Inspectors</code> </p>
<p> const std::string &amp; <code>name</code> () const </p>
<p> const std::string &amp; <code>code</code> () const </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Data &gt; <code>data_</code> </p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>Region</code> &amp;, const <code>Region</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Region</code> &amp;, const <code>Region</code> &amp;) </p>
<h2>Detailed Description</h2>
<p><code>Region</code> class, used for inflation applicability.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>Region</code> &amp;, const <code>Region</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Region</code> &amp;, const <code>Region</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
