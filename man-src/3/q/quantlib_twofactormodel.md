---
title: "quantlib_twofactormodel(3)"
name: "quantlib_twofactormodel"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_twofactormodel/"
description: "QuantLib::TwoFactorModel – Abstract base-class for two-factor models."
---

<p>QuantLib::TwoFactorModel &#8211; Abstract base-class for two-factor models. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/twofactormodel.hpp&gt; </p>
<p> Inherits <code>QuantLib::ShortRateModel</code>. </p>
<p> Inherited by <code>G2</code>. </p>
<h3>Classes</h3>
<p>class <code>ShortRateDynamics</code><br />
 <i>Class describing the dynamics of the two state variables. </i><br />
 class <code>ShortRateTree</code><br />
 <i>Recombining two-dimensional tree discretizing the state variable. </i></p>
<h3>Public Member Functions</h3>
<p><code>TwoFactorModel</code> (Size nParams) </p>
<p> virtual boost::shared_ptr&lt; <code>ShortRateDynamics</code> &gt; <code>dynamics</code> () const =0<br />
 <i>Returns the short-rate dynamics. </i><br />
 boost::shared_ptr&lt; <code>Lattice</code> &gt; <code>tree</code> (const <code>TimeGrid</code> &amp;grid) const<br />
 <i>Returns a two-dimensional trinomial tree. </i></p>
<h2>Detailed Description</h2>
<p>Abstract base-class for two-factor models. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
