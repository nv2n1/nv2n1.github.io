---
title: "h_(3)"
name: "h_"
section: "3"
letter: "h"
url: "/docs/linux/man/3-h_/"
description: "QuantLib::HullWhiteProcess – Hull-White stochastic process."
---

<h2 class="name">NAME</h2>
<p> QuantLib::HullWhiteProcess &#8211; Hull-White stochastic process. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/processes/hullwhiteprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>HullWhiteProcess</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;h, Real a, Real sigma) </p>
<p> <code>StochasticProcess1D interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>drift</code> (Time t, Real x) const<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 Real <code>diffusion</code> (Time t, Real x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i><br />
 Real <code>expectation</code> (Time t0, Real x0, Time dt) const </p>
<p> Real <code>stdDeviation</code> (Time t0, Real x0, Time dt) const </p>
<p> Real <code>variance</code> (Time t0, Real x0, Time dt) const </p>
<p> Real <code>a</code> () const </p>
<p> Real <code>sigma</code> () const </p>
<p> Real <code>alpha</code> (Time t) const </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>QuantLib::OrnsteinUhlenbeckProcess</code> &gt; <code>process_</code> </p>
<p> <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; <code>h_</code> </p>
<p> Real <code>a_</code> </p>
<p> Real <code>sigma_</code> </p>
<h2>Detailed Description</h2>
<p> Hull-White stochastic process. </p>
<h2>Member Function Documentation</h2>
<h3>Real expectation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p> returns the expectation $ E(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Real stdDeviation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p> returns the standard deviation $ S(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Real variance (Time t0, Real x0, Time dt) const [virtual]</h3>
<p> returns the variance $ V(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
