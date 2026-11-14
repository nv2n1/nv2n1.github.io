---
title: "eta_(3)"
name: "eta_"
section: "3"
letter: "e"
url: "/docs/linux/man/3-eta_/"
description: "QuantLib::G2ForwardProcess – Forward G2 stochastic process"
---

<h2 class="name">NAME</h2>
<p> QuantLib::G2ForwardProcess &#8211; Forward G2 stochastic process </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/processes/g2process.hpp&gt; </p>
<p> Inherits <code>QuantLib::ForwardMeasureProcess</code>. </p>
<h3>Public Member Functions</h3>
<p> <code>G2ForwardProcess</code> (<code>Real</code> a, <code>Real</code> sigma, <code>Real</code> b, <code>Real</code> eta, <code>Real</code> rho) </p>
<p> <code>StochasticProcess interface</code> </p>
<p> Size <code>size</code> () const<br />
 <i>returns the number of dimensions of the stochastic process </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>initialValues</code> () const<br />
 <i>returns the initial values of the state variables </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x) const<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, mathrm{x}_t) $ </i><br />
 <code>Disposable</code>&lt; <code>Array</code> &gt; <code>expectation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>stdDeviation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<h3>Protected Member Functions</h3>
<p> <code>Real</code> <code>xForwardDrift</code> (Time t, Time T) const </p>
<p> <code>Real</code> <code>yForwardDrift</code> (Time t, Time T) const </p>
<p> <code>Real</code> <code>Mx_T</code> (<code>Real</code> s, <code>Real</code> t, <code>Real</code> T) const </p>
<p> <code>Real</code> <code>My_T</code> (<code>Real</code> s, <code>Real</code> t, <code>Real</code> T) const </p>
<h3>Protected Attributes</h3>
<p> <code>Real</code> <code>x0_</code> </p>
<p> <code>Real</code> <code>y0_</code> </p>
<p> <code>Real</code> <code>a_</code> </p>
<p> <code>Real</code> <code>sigma_</code> </p>
<p> <code>Real</code> <code>b_</code> </p>
<p> <code>Real</code> <code>eta_</code> </p>
<p> <code>Real</code> <code>rho_</code> </p>
<p> boost::shared_ptr&lt; <code>QuantLib::OrnsteinUhlenbeckProcess</code> &gt; <code>xProcess_</code> </p>
<p> boost::shared_ptr&lt; <code>QuantLib::OrnsteinUhlenbeckProcess</code> &gt; <code>yProcess_</code> </p>
<h2>Detailed Description</h2>
<p> Forward G2 stochastic process </p>
<h2>Member Function Documentation</h2>
<h3><code>Disposable</code>&lt;<code>Array</code>&gt; expectation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the expectation $ E(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; stdDeviation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the standard deviation $ S(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>.</p>
<h3><code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the covariance $ V(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given discretization. This method can be overridden in derived classes which want to hard-code a particular discretization. </p>
<p> Reimplemented from <code>StochasticProcess</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
