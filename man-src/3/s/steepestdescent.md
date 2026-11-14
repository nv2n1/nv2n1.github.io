---
title: "steepestdescent(3)"
name: "steepestdescent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-steepestdescent/"
description: "QuantLib::SteepestDescent – Multi-dimensional steepest-descent class."
---

<p>QuantLib::SteepestDescent &#8211; Multi-dimensional steepest-descent class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/optimization/steepestdescent.hpp&gt; </p>
<p> Inherits QuantLib::LineSearchBasedMethod. </p>
<h3>Public Member Functions</h3>
<p><code>SteepestDescent</code> (const boost::shared_ptr&lt; <code>LineSearch</code> &gt; &amp;lineSearch=boost::shared_ptr&lt; <code>LineSearch</code> &gt;()) </p>
<p> virtual EndCriteria::Type <code>minimize</code> (<code>Problem</code> &amp;P, const <code>EndCriteria</code> &amp;endCriteria)<br />
 <i>minimize the optimization problem P </i></p>
<h2>Detailed Description</h2>
<p>Multi-dimensional steepest-descent class. </p>
<p> User has to provide line-search method and optimization end criteria </p>
<p> search direction $ = &#8211; f'(x) $ </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
