---
title: "ornsteinuhlenbeckprocess(3)"
name: "ornsteinuhlenbeckprocess"
section: "3"
letter: "o"
url: "/docs/linux/man/3-ornsteinuhlenbeckprocess/"
description: "QuantLib::OrnsteinUhlenbeckProcess – Ornstein-Uhlenbeck process class."
---

<p>QuantLib::OrnsteinUhlenbeckProcess &#8211; Ornstein-Uhlenbeck process class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/processes/ornsteinuhlenbeckprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::StochasticProcess1D</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OrnsteinUhlenbeckProcess</code> (Real speed, <code>Volatility</code> vol, Real x0=0.0, Real level=0.0) </p>
<p> <code>StochasticProcess interface</code> </p>
<p> Real <code>x0</code> () const<br />
 <i>returns the initial value of the state variable </i><br />
 Real <code>speed</code> () const </p>
<p> Real <code>volatility</code> () const </p>
<p> Real <code>level</code> () const </p>
<p> Real <code>drift</code> (Time t, Real x) const<br />
 <i>returns the drift part of the equation, i.e. $ mu(t, x_t) $ </i><br />
 Real <code>diffusion</code> (Time t, Real x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, x_t) $ </i><br />
 Real <code>expectation</code> (Time t0, Real x0, Time dt) const </p>
<p> Real <code>stdDeviation</code> (Time t0, Real x0, Time dt) const </p>
<p> Real <code>variance</code> (Time t0, Real x0, Time dt) const </p>
<h2>Detailed Description</h2>
<p>Ornstein-Uhlenbeck process class. </p>
<p> This class describes the Ornstein-Uhlenbeck process governed by [ dx = a (r &#8211; x_t) dt + igma dW_t. ]</p>
<h2>Member Function Documentation</h2>
<h3>Real expectation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the expectation $ E(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Real stdDeviation (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the standard deviation $ S(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>.</p>
<h3>Real variance (Time t0, Real x0, Time dt) const [virtual]</h3>
<p>returns the variance $ V(x_{t_0 + Delta t} | x_{t_0} = x_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess1D</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
