---
title: "quantlib_onefactormodel_shortratedynamics(3)"
name: "quantlib_onefactormodel_shortratedynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_onefactormodel_shortratedynamics/"
description: "QuantLib::OneFactorModel::ShortRateDynamics – Base class describing the short-rate dynamics."
---

<p>QuantLib::OneFactorModel::ShortRateDynamics &#8211; Base class describing the short-rate dynamics. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/onefactormodel.hpp&gt; </p>
<p> Inherited by <code>Dynamics</code>, <code>Dynamics</code>, <code>Dynamics</code>, and <code>Dynamics</code>. </p>
<h3>Public Member Functions</h3>
<p><code>ShortRateDynamics</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;process) </p>
<p> virtual Real <code>variable</code> (Time t, Rate r) const =0<br />
 <i>Compute state variable from short rate. </i><br />
 virtual Rate <code>shortRate</code> (Time t, Real variable) const =0<br />
 <i>Compute short rate from state variable. </i><br />
 const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp; <code>process</code> ()<br />
 <i>Returns the risk-neutral dynamics of the state variable. </i></p>
<h2>Detailed Description</h2>
<p>Base class describing the short-rate dynamics. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
