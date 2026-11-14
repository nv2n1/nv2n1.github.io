---
title: "inflationtermstructure(3)"
name: "inflationtermstructure"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inflationtermstructure/"
description: "ql/termstructures/inflationtermstructure.hpp – Base classes for inflation term structures."
---

<h2 class="name">NAME</h2>
<p> ql/termstructures/inflationtermstructure.hpp &#8211; Base classes for inflation term structures. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/termstructures/yieldtermstructure.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>InflationTermStructure</code><br />
 <i>Interface for inflation term structures. </i><br />
 class <code>ZeroInflationTermStructure</code><br />
 <i>Interface for zero inflation term structures. </i><br />
 class <code>YoYInflationTermStructure</code><br />
 <i>Base class for year-on-year inflation term structures. </i></p>
<h3>Functions</h3>
<p> std::pair&lt; Date, Date &gt; <code>inflationPeriod</code> (const Date &amp;, Frequency)<br />
 <i>utility function giving the inflation period for a given date </i></p>
<h2>Detailed Description</h2>
<p> Base classes for inflation term structures. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
