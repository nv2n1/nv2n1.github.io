---
title: "discretization_(3)"
name: "discretization_"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discretization_/"
description: "QuantLib::StochasticProcess – multi-dimensional stochastic process class."
---

<h2 class="name">NAME</h2>
<p> QuantLib::StochasticProcess &#8211; multi-dimensional stochastic process class. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/stochasticprocess.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observer</code>, and <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>ForwardMeasureProcess</code>, <code>G2Process</code>, <code>GJRGARCHProcess</code>, <code>HestonProcess</code>, JointStochasticProcess, <code>LiborForwardModelProcess</code>, <code>StochasticProcess1D</code>, and <code>StochasticProcessArray</code>. </p>
<h3>Classes</h3>
<p> class <code>discretization</code><br />
 <i></i><code>discretization</code> of a stochastic process over a given time interval</p>
<h3>Public Member Functions</h3>
<p> <code>Stochastic process interface</code> </p>
<p> virtual Size <code>size</code> () const =0<br />
 <i>returns the number of dimensions of the stochastic process </i><br />
 virtual Size <code>factors</code> () const<br />
 <i>returns the number of independent factors of the process </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>initialValues</code> () const =0<br />
 <i>returns the initial values of the state variables </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>drift</code> (Time t, const <code>Array</code> &amp;x) const =0<br />
 <i>returns the drift part of the equation, i.e., $ mu(t, mathrm{x}_t) $ </i><br />
 virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>diffusion</code> (Time t, const <code>Array</code> &amp;x) const =0<br />
 <i>returns the diffusion part of the equation, i.e. $ igma(t, mathrm{x}_t) $ </i><br />
 virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>expectation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>stdDeviation</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> virtual <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>covariance</code> (Time t0, const <code>Array</code> &amp;x0, Time dt) const </p>
<p> virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>evolve</code> (Time t0, const <code>Array</code> &amp;x0, Time dt, const <code>Array</code> &amp;dw) const </p>
<p> virtual <code>Disposable</code>&lt; <code>Array</code> &gt; <code>apply</code> (const <code>Array</code> &amp;x0, const <code>Array</code> &amp;dx) const </p>
<p> <code>utilities</code> </p>
<p> virtual Time <code>time</code> (const <code>Date</code> &amp;) const </p>
<p> <code>Observer interface</code> </p>
<p> void <code>update</code> () </p>
<h3>Protected Member Functions</h3>
<p> <code>StochasticProcess</code> (const boost::shared_ptr&lt; <code>discretization</code> &gt; &amp;) </p>
<h3>Protected Attributes</h3>
<p> boost::shared_ptr&lt; <code>discretization</code> &gt; <code>discretization_</code> </p>
<h2>Detailed Description</h2>
<p> multi-dimensional stochastic process class. </p>
<p> This class describes a stochastic process governed by [ dmathrm{x}_t = mu(t, x_t)mathrm{d}t + igma(t, mathrm{x}_t) dot dmathrm{W}_t. ]</p>
<h2>Member Function Documentation</h2>
<h3>virtual <code>Disposable</code>&lt;<code>Array</code>&gt; expectation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the expectation $ E(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>G2Process</code>, <code>G2ForwardProcess</code>, and <code>StochasticProcessArray</code>.</p>
<h3>virtual <code>Disposable</code>&lt;<code>Matrix</code>&gt; stdDeviation (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the standard deviation $ S(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>G2Process</code>, <code>G2ForwardProcess</code>, and <code>StochasticProcessArray</code>.</p>
<h3>virtual <code>Disposable</code>&lt;<code>Matrix</code>&gt; covariance (Time t0, const <code>Array</code> &amp; x0, Time dt) const [virtual]</h3>
<p> returns the covariance $ V(mathrm{x}_{t_0 + Delta t} | mathrm{x}_{t_0} = mathrm{x}_0) $ of the process after a time interval $ Delta t $ according to the given <code>discretization</code>. This method can be overridden in derived classes which want to hard-code a particular <code>discretization</code>. </p>
<p> Reimplemented in <code>LiborForwardModelProcess</code>, <code>G2Process</code>, <code>G2ForwardProcess</code>, and <code>StochasticProcessArray</code>.</p>
<h3>virtual <code>Disposable</code>&lt;<code>Array</code>&gt; evolve (Time t0, const <code>Array</code> &amp; x0, Time dt, const <code>Array</code> &amp; dw) const [virtual]</h3>
<p> returns the asset value after a time interval $ Delta t $ according to the given <code>discretization</code>. By default, it returns [ E(mathrm{x}_0,t_0,Delta t) + S(mathrm{x}_0,t_0,Delta t) dot Delta mathrm{w} ] where $ E $ is the expectation and $ S $ the standard deviation. </p>
<p> Reimplemented in <code>LiborForwardModelProcess</code>, <code>BatesProcess</code>, <code>GJRGARCHProcess</code>, <code>HestonProcess</code>, and <code>StochasticProcessArray</code>.</p>
<h3>virtual <code>Disposable</code>&lt;<code>Array</code>&gt; apply (const <code>Array</code> &amp; x0, const <code>Array</code> &amp; dx) const [virtual]</h3>
<p> applies a change to the asset value. By default, it returns $ mathrm{x} + Delta mathrm{x} $. </p>
<p> Reimplemented in <code>LiborForwardModelProcess</code>, <code>GJRGARCHProcess</code>, <code>HestonProcess</code>, and <code>StochasticProcessArray</code>.</p>
<h3>virtual Time time (const <code>Date</code> &amp;) const [virtual]</h3>
<p> returns the time value corresponding to the given date in the reference system of the stochastic process. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> As a number of processes might not need this functionality, a default implementation is given which raises an exception.</dl>
<p> Reimplemented in <code>GeneralizedBlackScholesProcess</code>, <code>GJRGARCHProcess</code>, <code>HestonProcess</code>, <code>Merton76Process</code>, and <code>StochasticProcessArray</code>.</p>
<h3>void update () [virtual]</h3>
<p> This method must be implemented in derived classes. An instance of Observer does not call this method directly: instead, it will be called by the observables the instance registered with when they need to notify any changes. </p>
<p> Implements <code>Observer</code>. </p>
<p> Reimplemented in <code>GeneralizedBlackScholesProcess</code>, and <code>HybridHestonHullWhiteProcess</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">Author</a></p>
<dd></dl>
