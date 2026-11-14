---
title: "quantlib_blackkarasinski(3)"
name: "quantlib_blackkarasinski"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_blackkarasinski/"
description: "QuantLib::BlackKarasinski – Standard Black-Karasinski model class."
---

<p>QuantLib::BlackKarasinski &#8211; Standard Black-Karasinski model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodels/blackkarasinski.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorModel</code>, and <code>QuantLib::TermStructureConsistentModel</code>. </p>
<h3>Classes</h3>
<p>class <code>Dynamics</code><br />
 <i>Short-rate dynamics in the Black-Karasinski model. </i></p>
<h3>Public Member Functions</h3>
<p><code>BlackKarasinski</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure, <code>Real</code> a=0.1, <code>Real</code> sigma=0.1) </p>
<p> boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const<br />
 <i>returns the short-rate dynamics </i><br />
 boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Return by default a trinomial recombining tree. </i></p>
<h2>Detailed Description</h2>
<p>Standard Black-Karasinski model class. </p>
<p> This class implements the standard Black-Karasinski model defined by [ d</p>
<hr>
<p>stants. </p>
<p> <code>Examples: </code> </p>
<p> <code>BermudanSwaption.cpp</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
