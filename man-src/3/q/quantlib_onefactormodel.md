---
title: "quantlib_onefactormodel(3)"
name: "quantlib_onefactormodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_onefactormodel/"
description: "QuantLib::OneFactorModel – Single-factor short-rate model abstract class."
---

<p>QuantLib::OneFactorModel &#8211; Single-factor short-rate model abstract class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::ShortRateModel</code>. </p>
<p> Inherited by <code>BlackKarasinski</code>, and <code>OneFactorAffineModel</code>. </p>
<h3>Classes</h3>
<p>class <code>ShortRateDynamics</code><br />
 <i>Base class describing the short-rate dynamics. </i><br />
 class <code>ShortRateTree</code><br />
 <i>Recombining trinomial tree discretizing the state variable. </i></p>
<h3>Public Member Functions</h3>
<p><code>OneFactorModel</code> (Size nArguments) </p>
<p> virtual boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const =0<br />
 <i>returns the short-rate dynamics </i><br />
 boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Return by default a trinomial recombining tree. </i></p>
<h2>Detailed Description</h2>
<p>Single-factor short-rate model abstract class. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
