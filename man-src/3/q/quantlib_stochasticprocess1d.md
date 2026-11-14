---
title: "quantlib_stochasticprocess1d(3)"
name: "quantlib_stochasticprocess1d"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_stochasticprocess1d/"
description: "QuantLib::StochasticProcess1D – 1-dimensional stochastic process"
---

<p>QuantLib::StochasticProcess1D &#8211; 1-dimensional stochastic process </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/stochasticprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess</code>. </p>
<p> Inherited by HelperProcess, <code>ForwardMeasureProcess1D</code>, <code>GeneralizedBlackScholesProcess</code>, <code>GeometricBrownianMotionProcess</code>, <code>HullWhiteProcess</code>, <code>Merton76Process</code>, <code>OrnsteinUhlenbeckProcess</code>, and <code>SquareRootProcess</code>. </p>
<h3>Classes</h3>
<p>class <code>discretization</code><br />
 <i></i><code>discretization</code> of a 1-D stochastic process</p>
<h3>Public Member Functions</h3>
<p><code>1-D stochastic process interface</code> </p>
<p> virtual Real <code>x0</code> () const =0<br />
 <i>returns the initial value of the state variable </i><br />
 virtual Real <code>drift</code> (Time t, Real x) const =0<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 virtual Real <code>diffusion</code> (Time t, Real x) const =0<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i><br />
 virtual Real <code>expectation</code> (Time t0, Real x0, Time dt) const </p>
<p> virtual Real <code>stdDeviation</code> (Time t0, Real x0, Time dt) const </p>
<p> virtual Real <code>variance</code> (Time t0, Real x0, Time dt) const </p>
<p> virtual Real <code>evolve</code> (Time t0, Real x0, Time dt, Real dw) const </p>
<p> virtual Real <code>apply</code> (Real x0, Real dx) const </p>
<h3>Protected Member Functions</h3>
<p><code>StochasticProcess1D</code> (const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;) </p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; <code>discretization</code> &gt; <code>discretization_</code> </p>
<h2>Detailed Description</h2>
<p>1-dimensional stochastic process </p>
<p> This class describes a stochastic process governed by [ dx_t = mu(t, x_t)dt + igma(t, x_t)dW_t. ]</p>
<h2>Member Function Documentation</h2>
<h3>virtual Real expectation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the expectation $ E(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>HullWhiteProcess</code>, <code>HullWhiteForwardProcess</code>, and <code>OrnsteinUhlenbeckProcess</code>.</p>
<h3>virtual Real stdDeviation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the standard deviation $ S(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>HullWhiteProcess</code>, <code>HullWhiteForwardProcess</code>, and <code>OrnsteinUhlenbeckProcess</code>.</p>
<h3>virtual Real variance (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the variance $ V(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>HullWhiteProcess</code>, <code>HullWhiteForwardProcess</code>, and <code>OrnsteinUhlenbeckProcess</code>.</p>
<h3>virtual Real evolve (Time t0, Real x0, Time dt, Real dw) const [virtual]</h3>
<p>returns the asset value after a time interval $ Delta t $ according to the given <code>discretization</code>. By default, it returns [ E(x_0,t_0,Delta t) + S(x_0,t_0,Delta t) dot Delta w ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented in <code>ExtendedBlackScholesMertonProcess</code>.</p>
<h3>virtual Real apply (Real x0, Real dx) const [virtual]</h3>
<p>applies a change to the asset value. By default, it returns $ x + Delta x $. </p>
<p> Reimplemented in <code>GeneralizedBlackScholesProcess</code>, and <code>Merton76Process</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
