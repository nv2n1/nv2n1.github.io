---
title: "quantlib_twofactormodel_shortratedynamics(3)"
name: "quantlib_twofactormodel_shortratedynamics"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_twofactormodel_shortratedynamics/"
description: "QuantLib::TwoFactorModel::ShortRateDynamics – Class describing the dynamics of the two state variables."
---

<p>QuantLib::TwoFactorModel::ShortRateDynamics &#8211; Class describing the dynamics of the two state variables. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/shortrate/twofactormodel.hpp&gt; </p>
<p> Inherited by Dynamics. </p>
<h3>Public Member Functions</h3>
<p><code>ShortRateDynamics</code> (const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;xProcess, const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp;yProcess, Real correlation) </p>
<p> virtual <code>Rate</code> <code>shortRate</code> (Time t, Real x, Real y) const =0 </p>
<p> const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp; <code>xProcess</code> () const<br />
 <i>Risk-neutral dynamics of the first state variable x. </i><br />
 const boost::shared_ptr&lt; <code>StochasticProcess1D</code> &gt; &amp; <code>yProcess</code> () const<br />
 <i>Risk-neutral dynamics of the second state variable y. </i><br />
 Real <code>correlation</code> () const<br />
 <i>Correlation $ ho $ between the two brownian motions. </i><br />
 boost::shared_ptr&lt; <code>StochasticProcess</code> &gt; <code>process</code> () const<br />
 <i>Joint process of the two variables. </i></p>
<h2>Detailed Description</h2>
<p>Class describing the dynamics of the two state variables. </p>
<p> We assume here that the short-rate is a function of two state variables x and y. [ r_t = f(t, x_t, y_t) ] of two state variables $ x_t $ and $ y_t $. These stochastic processes satisfy [ x_t = mu_x(t, x_t)dt + igma_x(t, x_t) dW_t^x ] and [ y_t = mu_y(t,y_t)dt + igma_y(t, y_t) dW_t^y ] where $ W^x $ and $ W^y $ are two brownian motions satisfying [ dW^x_t dW^y_t = ho dt ]. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
